# Swanson's Welding & Fabrication — website redesign

Static redesign of https://swansonswelding.com. Plain HTML, one stylesheet,
one small script. No build step, no framework.

## Pages

| File | Page |
|---|---|
| `index.html` | Home |
| `services.html` | Services (welding & fabrication, machine shop, design) |
| `products.html` | Products, PPE Cubby brochure |
| `about.html` | About, leadership |
| `contact.html` | Contact info and quote form |

`assets/css/styles.css` holds all styling. `assets/js/main.js` handles the
mobile menu, current-page highlight, back-to-top button, and the contact
form. `assets/img/` has the logo mark; `assets/doc/` has the Cubby brochure.

Stock photography sources and credits are in `STOCK-IMAGES.md`.

## Preview locally

```bash
python -m http.server 8765
```

Then open http://localhost:8765/.

## Design notes

- Header is a persistent dark bar: logo mark, wordmark in Chakra Petch, nav
  links, and a quote button. Collapses to a hamburger below 900px.
- Fonts: Chakra Petch for the wordmark and headings, Plus Jakarta Sans for
  body text, both from Google Fonts.
- Accent color is an ember orange (`--accent` in `styles.css`). Change the
  CSS variables at the top of the stylesheet to retheme.
- The contact form has no backend yet. Submitting opens the visitor's mail
  client with the fields pre-filled. Swap in Formspree, Netlify Forms, or
  similar when hosting is decided.

## Original site

`original/` is an untouched offline mirror of the WordPress site as captured
on 2026-09-02, kept for reference (copy, brochure, old images). It is not
linked from the new pages.
