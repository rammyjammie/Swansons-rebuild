# Swansons Welding & Fabrication — site mirror

Static snapshot of https://swansonswelding.com captured 2026-09-02 as the
starting point for a revamp. Cloned with the site owner's permission.

## What's here

| File | Source page |
|---|---|
| `index.html` | `/` (home) |
| `services.html` | `/?page_id=2` |
| `products.html` | `/?page_id=70` |
| `about-us.html` | `/?page_id=71` |
| `contact-swansons.html` | `/?page_id=69` |

`wp-content/` and `wp-includes/` hold every same-host asset the pages
reference (theme CSS/JS, plugin CSS/JS, uploaded images, fonts, the Cubby
brochure PDF). All references were rewritten to relative paths, so the
snapshot opens fully offline. `MIRROR-MANIFEST.json` lists the page map and
the two Open Sans TTFs that 404 on the live server too.

## Preview locally

```bash
python -m http.server 8765
```

Then open http://localhost:8765/.

## Notes for the revamp

- The original is WordPress (FotaWP theme, Cozy Addons, Forminator). The HTML
  is bloated with inline block CSS; treat it as a content and asset reference,
  not a codebase to extend.
- The contact form posted to WordPress (Forminator). It will not submit from
  the static copy.
- Canonical / og:url / RSS / REST links still point at the live domain
  intentionally.
