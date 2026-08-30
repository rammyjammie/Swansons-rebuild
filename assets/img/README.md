# Image assets

Drop the real brand and project files in here. Filenames referenced by the site:

| File | Used by | Notes |
| --- | --- | --- |
| `logo.svg` | header + footer on every page | Currently a placeholder mark. Replace this file (keep the name) and the whole site updates. SVG preferred; a PNG works if you also change the `src` in each page's header. |
| `favicon.svg` | browser tab icon | Placeholder. |
| `hero.jpg` | homepage hero | Not yet wired up — see the commented `<img>` slot in `index.html`. Landscape, ~1600×1200 or larger. |
| `project-01.jpg` … `project-06.jpg` | projects gallery | Square-ish or 4:3 shots of finished work. |
| `shop.jpg`, `team.jpg` | about page | Optional. |

Every image slot in the HTML is a `<div class="...__frame">` or `<div class="split__media">`
containing a placeholder icon. To use a real photo, replace the inner `<svg>` with:

```html
<img src="assets/img/project-01.jpg" alt="Describe what is pictured" width="1200" height="900" loading="lazy">
```

Always write real `alt` text — it matters for both screen readers and search.
