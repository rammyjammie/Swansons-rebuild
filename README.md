# Swanson's Welding & Fabrication — website rebuild

A modern rebuild of [swansonswelding.com](https://swansonswelding.com) for
Swanson's Welding & Fabrication, Inc. of Springdale, Arkansas.

Plain HTML, CSS, and a little JavaScript — **no build step, no framework, no
dependencies**. Edit a file, refresh the browser, done. It will host anywhere
that serves static files.

## Preview it locally

Open `index.html` directly in a browser, or serve the folder so links behave
exactly as they will in production:

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
contact.html      Contact form, shop info, map
404.html          Not-found page
robots.txt        Search engine directives
sitemap.xml       Page list for search engines
assets/css/       styles.css — the whole design system, organized and commented
assets/js/        main.js — mobile nav, sticky header, scroll reveal
assets/img/       logo, favicon, and photos (see assets/img/README.md)
```

Page filenames deliberately match the old site (`about-us.html`,
`projects.html`, `contact.html`) so existing links, bookmarks, and search
rankings carry over.

## Before this goes live

These are the things that need real assets or a decision. Everything else works.

1. **Drop in the real logo.** Replace `assets/img/logo.svg` (and
   `assets/img/favicon.svg`) — keep the filenames and every page picks it up
   automatically. The current mark is a placeholder.
2. **Add photos.** Every image slot is a placeholder frame with a commented
   `<img>` tag showing exactly what to paste. See `assets/img/README.md`.
   Real shop and project photos will do more for this site than any other
   single change.
3. **Connect the contact form.** A static site can't send email by itself.
   Create a free endpoint at [Formspree](https://formspree.io) (or use Netlify
   Forms) and replace `YOUR_FORM_ID` in `contact.html`. Until then the phone
   number and email address are the working ways to reach the shop.
4. **Verify the business details.** Please confirm these with Micah's family —
   they were reconstructed from public business listings, not from the live
   site (see note below):
   - Phone: (479) 419-9050
   - Email: office@swansonswelding.com
   - Address: 1921 Ford Avenue, Springdale, AR 72764
   - Shop hours: **Monday–Friday, 7:00 AM – 3:30 PM** — the days were inferred;
     the hours were listed. Worth double-checking.
   - The "30+ years combined experience" figure
5. **Set the brand color.** The accent is `--spark: #ff6a13` at the top of
   `assets/css/styles.css`. Change that one value and the whole site follows.
   Match it to the real logo.

## A note on the content

This environment's network policy blocked access to `swansonswelding.com`, so
the existing pages could not be copied directly. The structure and copy here
were rebuilt from public business listings and search results, and the wording
is original rather than lifted. **Every claim on the site should be read over by
the family before launch** — particularly the service list, the experience
figure, and the service-area towns on the About page.

If you can send me an export of the old site, or even screenshots, I can
reconcile this against the original copy.

## Deploying

**GitHub Pages** — push this branch, then Settings → Pages → deploy from
branch. Add a `CNAME` file containing `swansonswelding.com` to use the real
domain.

**Netlify / Cloudflare Pages** — connect the repo. There is no build command;
the publish directory is the repository root.

## Design notes

- Palette, type scale, spacing, and radii are CSS custom properties at the top
  of `styles.css`. Change tokens there rather than hunting through rules.
- Typefaces are Barlow Condensed (headings) and Inter (body), loaded from
  Google Fonts with system fallbacks.
- Responsive from 320px up; no horizontal scroll at any width.
- Accessibility: semantic landmarks, skip link, visible focus rings, labelled
  form fields, `aria-current` on the active nav item, and
  `prefers-reduced-motion` support.
- The scroll-reveal animation is decorative only — content stays visible with
  JavaScript disabled, and a safety timer guarantees nothing can stay hidden.
- `LocalBusiness` structured data is embedded in `index.html` for search
  engines and Google Business listings.
