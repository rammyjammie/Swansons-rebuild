# swansonswelding.com — rebuild

A modern rebuild of [swansonswelding.com](https://swansonswelding.com), currently
a **content-free template**: the design, layout, and front-end are complete, and
every piece of business copy is a clearly-marked placeholder waiting for real
content.

Plain HTML, CSS, and a little JavaScript — **no build step, no framework, no
dependencies**. Edit a file, refresh the browser, done. It hosts anywhere that
serves static files.

## Status

| | |
| --- | --- |
| Design system, layout, responsive behaviour | Done |
| Accessibility and cross-page QA | Done |
| Business copy | **Placeholder** — see [CONTENT.md](CONTENT.md) |
| Logo, favicon, photography | **Placeholder** — see [assets/img/README.md](assets/img/README.md) |
| Contact form endpoint | **Not connected** — see `contact.html` |

Every slot needing real content is written as `[a bracketed label]` in the HTML,
so nothing false can ship by accident. [CONTENT.md](CONTENT.md) lists all of them
as a fill-in-the-blanks brief.

### Why there is no copy

An earlier draft was written from third-party business directories, because the
live site could not be reached from the environment this was built in (the cloud
session's network policy allows only package registries and GitHub, so
`swansonswelding.com` returned a proxy `403`). That sourcing proved unreliable —
it had the owner's name wrong — so all of it was removed rather than left for
someone to correct. The next pass should take copy from the real site or from
the family directly.

## Preview it locally

Open `index.html` in a browser, or serve the folder so links behave exactly as
they will in production:

```bash
npx http-server -p 8080 .      # then visit http://127.0.0.1:8080
# or, with Python already installed:
python3 -m http.server 8080
```

## What's in here

```
index.html        Home
services.html     Services & capabilities
projects.html     Project gallery
about-us.html     About the company
contact.html      Contact form, shop info, map slot
404.html          Not-found page
CONTENT.md        Fill-in-the-blanks content brief
robots.txt        Search engine directives
sitemap.xml       Page list for search engines
assets/css/       styles.css — the whole design system, organized and commented
assets/js/        main.js — mobile nav, sticky header, scroll reveal
assets/img/       logo, favicon, photos (see assets/img/README.md)
```

Page filenames deliberately match the old site (`about-us.html`,
`projects.html`, `contact.html`) so existing links, bookmarks, and search
rankings carry over.

## Filling it in

1. Work through [CONTENT.md](CONTENT.md) with the family.
2. Drop the real logo in as `assets/img/logo.svg`, keeping the filename — every
   page picks it up automatically. Same for `favicon.svg`.
3. Add photos per [assets/img/README.md](assets/img/README.md). Each image slot
   is a placeholder frame with a commented `<img>` tag showing what to paste.
4. Set the brand accent: `--spark` at the top of `assets/css/styles.css`. One
   value, and the whole site follows.
5. Connect the contact form — a static site can't send email by itself. Create a
   free endpoint at [Formspree](https://formspree.io) and replace `YOUR_FORM_ID`
   in `contact.html`.
6. Uncomment and complete the `LocalBusiness` structured data block in
   `index.html`, and the Google Maps embed in `contact.html`.

## Deploying

**GitHub Pages** — push this branch, then Settings → Pages → deploy from branch.
Add a `CNAME` file containing `swansonswelding.com` to use the real domain.

**Netlify / Cloudflare Pages** — connect the repo. There is no build command;
the publish directory is the repository root.

## Design notes

- Palette, type scale, spacing, and radii are CSS custom properties at the top
  of `styles.css`. Change tokens there rather than hunting through rules.
- Typefaces are Barlow Condensed (headings) and Inter (body), loaded from Google
  Fonts with system fallbacks.
- Responsive from 320px up; verified no horizontal scroll at any width.
- Accessibility: semantic landmarks, skip link, visible focus rings, labelled
  form fields, `aria-current` on the active nav item, and
  `prefers-reduced-motion` support.
- The scroll-reveal animation is decorative only — content stays visible with
  JavaScript disabled, and a safety timer guarantees nothing can stay hidden.
  This is verified in all three cases (no scroll, no JS, normal use).
