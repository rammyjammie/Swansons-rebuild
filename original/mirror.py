"""Mirror swansonswelding.com into a static, offline-browsable folder.

Crawls same-host HTML pages, downloads same-host assets (css/js/images/fonts/pdf),
rewrites references to relative local paths.
"""
import os, re, sys, time, json, posixpath
from urllib.parse import urljoin, urlparse, urldefrag, unquote
import requests
from bs4 import BeautifulSoup

ROOT = "https://swansonswelding.com/"
HOST = urlparse(ROOT).netloc
OUT = sys.argv[1] if len(sys.argv) > 1 else "mirror"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) site-mirror/1.0"

SKIP_PAGE_RE = re.compile(
    r"(feed=|rest_route=|xmlrpc\.php|wp-admin|wp-login|wp-json|\?s=|/feed/?$|\?p=\d+&|replytocom=|\?attachment_id=)",
    re.I,
)
ASSET_EXT = {
    ".css", ".js", ".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".avif", ".ico",
    ".woff", ".woff2", ".ttf", ".otf", ".eot", ".pdf", ".mp4", ".webm", ".mp3", ".json",
    ".xml", ".txt", ".map",
}

sess = requests.Session()
sess.headers["User-Agent"] = UA

pages = {}      # url -> local filename
assets = {}     # url (no query) -> local relative path
page_queue = []
asset_queue = []
failed = []


def norm(u):
    u, _ = urldefrag(u)
    return u


def same_host(u):
    p = urlparse(u)
    return p.netloc in (HOST, "www." + HOST) and p.scheme in ("http", "https")


def is_asset_url(u):
    path = urlparse(u).path
    ext = posixpath.splitext(path)[1].lower()
    return ext in ASSET_EXT


def asset_local(u):
    """Local relative path for a same-host asset, query stripped."""
    p = urlparse(u)
    path = unquote(p.path).lstrip("/")
    if not path or path.endswith("/"):
        path = path + "index"
    return path


def page_local(u):
    """Local filename for a page URL. Decided after fetch (needs title) — placeholder."""
    p = urlparse(u)
    path = p.path.strip("/")
    q = p.query
    if not path and not q:
        return "index.html"
    m = re.search(r"page_id=(\d+)", q)
    if m and not path:
        return f"page-{m.group(1)}.html"
    slug = re.sub(r"[^a-z0-9]+", "-", (path + ("-" + q if q else "")).lower()).strip("-")
    return (slug or "page") + ".html"


def slugify(s):
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return s[:60]


def fetch(u, binary=False):
    for attempt in range(3):
        try:
            r = sess.get(u, timeout=30)
            if r.status_code == 200:
                return r
            print(f"  ! {r.status_code} {u}")
            return None
        except Exception as e:
            print(f"  ! error {u}: {e}")
            time.sleep(1)
    return None


def enqueue_asset(u):
    u = norm(u)
    if not same_host(u):
        return None
    key = u.split("?")[0]
    if key not in assets:
        assets[key] = asset_local(key)
        asset_queue.append(key)
    return assets[key]


def enqueue_page(u):
    u = norm(u)
    if not same_host(u) or SKIP_PAGE_RE.search(u):
        return None
    if is_asset_url(u):
        return None
    # normalise trailing slash / www
    p = urlparse(u)
    u = f"https://{HOST}{p.path or '/'}" + (f"?{p.query}" if p.query else "")
    if p.path in ("", "/") and not p.query:
        u = ROOT
    if u not in pages:
        pages[u] = page_local(u)
        page_queue.append(u)
    return u


def rel(from_file, to_path):
    """Relative path from a local file to a local path."""
    from_dir = posixpath.dirname(from_file)
    r = posixpath.relpath(to_path, from_dir) if from_dir else to_path
    return r


CSS_URL_RE = re.compile(r"url\(\s*(['\"]?)([^'\")]+)\1\s*\)")
CSS_IMPORT_RE = re.compile(r"@import\s+(?:url\()?['\"]?([^'\")]+)['\"]?\)?")


def rewrite_css(css_text, base_url, local_file):
    """Enqueue assets referenced in CSS and rewrite to relative paths."""
    def repl(m):
        quote, ref = m.group(1), m.group(2).strip()
        if ref.startswith(("data:", "#", "about:")):
            return m.group(0)
        absu = urljoin(base_url, ref)
        loc = enqueue_asset(absu)
        if loc is None:
            return m.group(0)
        return f"url({quote}{rel(local_file, loc)}{quote})"
    css_text = CSS_URL_RE.sub(repl, css_text)

    def repl_imp(m):
        ref = m.group(1).strip()
        absu = urljoin(base_url, ref)
        loc = enqueue_asset(absu)
        if loc is None:
            return m.group(0)
        return f'@import url("{rel(local_file, loc)}")'
    css_text = CSS_IMPORT_RE.sub(repl_imp, css_text)
    return css_text


def rewrite_srcset(val, base_url, local_file):
    parts = []
    for cand in val.split(","):
        cand = cand.strip()
        if not cand:
            continue
        bits = cand.split()
        u = urljoin(base_url, bits[0])
        loc = enqueue_asset(u)
        bits[0] = rel(local_file, loc) if loc else bits[0]
        parts.append(" ".join(bits))
    return ", ".join(parts)


URL_ATTRS = ["src", "href", "data-src", "data-bg", "data-background", "poster", "content"]
SRCSET_ATTRS = ["srcset", "data-srcset"]


def process_page(u):
    local = pages[u]
    print(f"page {u} -> {local}")
    r = fetch(u)
    if r is None:
        failed.append(u)
        return
    html = r.text
    soup = BeautifulSoup(html, "html.parser")

    # nicer filename from title for page_id pages
    if local.startswith("page-"):
        t = soup.title.string if soup.title and soup.title.string else ""
        t = re.split(r"\s[-|–]\s", t)[0].strip()
        if t:
            cand = slugify(t) + ".html"
            if cand not in pages.values():
                pages[u] = local = cand
                print(f"   renamed -> {local}")

    for tag in soup.find_all(True):
        for attr in URL_ATTRS:
            if attr == "content" and not (tag.name == "meta" and tag.get("property", "").startswith("og:image")):
                continue
            val = tag.get(attr)
            if not val or not isinstance(val, str):
                continue
            v = val.strip()
            if v.startswith(("data:", "javascript:", "mailto:", "tel:", "#", "about:")):
                continue
            absu = urljoin(u, v)
            if not same_host(absu):
                continue
            if tag.name == "a" and attr == "href" and not is_asset_url(absu):
                pu = enqueue_page(absu)
                if pu:
                    tag[attr] = "__PAGE__" + pu  # resolved after crawl
                continue
            if tag.name == "link" and attr == "href":
                rels = [x.lower() for x in (tag.get("rel") or [])]
                if any(x in rels for x in ("canonical", "alternate", "shortlink", "profile", "pingback", "edituri", "wlwmanifest", "https://api.w.org/")):
                    continue
                if "dns-prefetch" in rels or "preconnect" in rels:
                    continue
            if is_asset_url(absu) or tag.name in ("img", "script", "link", "source", "video", "audio", "iframe"):
                loc = enqueue_asset(absu)
                if loc:
                    tag[attr] = rel(local, loc)
        for attr in SRCSET_ATTRS:
            val = tag.get(attr)
            if val:
                tag[attr] = rewrite_srcset(val, u, local)
        st = tag.get("style")
        if st and "url(" in st:
            tag["style"] = rewrite_css(st, u, local)

    for style in soup.find_all("style"):
        if style.string:
            style.string.replace_with(rewrite_css(style.string, u, local))

    pages_html[u] = str(soup)


pages_html = {}


def process_asset(key):
    loc = assets[key]
    dest = os.path.join(OUT, loc)
    r = fetch(key)
    if r is None:
        failed.append(key)
        return
    os.makedirs(os.path.dirname(dest) or OUT, exist_ok=True)
    if loc.lower().endswith(".css"):
        text = rewrite_css(r.text, key, loc)
        with open(dest, "w", encoding="utf-8") as f:
            f.write(text)
    else:
        with open(dest, "wb") as f:
            f.write(r.content)
    print(f"asset {loc} ({len(r.content)} B)")


def main():
    os.makedirs(OUT, exist_ok=True)
    enqueue_page(ROOT)
    while page_queue:
        u = page_queue.pop(0)
        process_page(u)
        time.sleep(0.3)
    while asset_queue:
        k = asset_queue.pop(0)
        process_asset(k)
        time.sleep(0.05)

    # resolve page links & write html
    for u, html in pages_html.items():
        local = pages[u]
        for pu, pl in sorted(pages.items(), key=lambda kv: -len(kv[0])):
            html = html.replace("__PAGE__" + pu, rel(local, pl))
        with open(os.path.join(OUT, local), "w", encoding="utf-8") as f:
            f.write(html)

    manifest = {
        "source": ROOT,
        "pages": {u: pages[u] for u in pages},
        "asset_count": len(assets),
        "failed": failed,
    }
    with open(os.path.join(OUT, "MIRROR-MANIFEST.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)
    print(f"\nDONE: {len(pages)} pages, {len(assets)} assets, {len(failed)} failed")
    for fu in failed:
        print("  FAILED:", fu)


if __name__ == "__main__":
    main()
