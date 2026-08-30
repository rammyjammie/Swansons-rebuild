# Content brief

Every `[bracketed slot]` in the HTML corresponds to a line below. Fill these in
with the family, and the site can be populated in one pass.

Nothing here is pre-filled. An earlier draft used details gathered from
third-party business directories; those turned out to be unreliable (the owner
name was wrong), so all of it was removed rather than left to be corrected.

---

## 1. Global — appears on every page

Used in the header, footer, page titles, and structured data.

| Slot | Value |
| --- | --- |
| `[BUSINESS NAME]` | |
| `[Descriptor line]` (small text under the name) | |
| `[Primary CTA]` (button label, e.g. "Request a Quote") | |
| `[PHONE NUMBER]` | |
| `[EMAIL ADDRESS]` | |
| `[STREET ADDRESS]` | |
| `[CITY, STATE ZIP]` | |
| `[Days]` (e.g. Monday – Friday) | |
| `[Opening]` / `[Closing]` times | |
| Footer description (~20 words) | |

## 2. Home — `index.html`

| Slot | Value |
| --- | --- |
| `[Location or eyebrow label]` | |
| `[Headline]` + `[Second line]` (the accent-coloured line) | |
| Hero supporting sentence (~25–35 words) | |
| `[Secondary CTA]` button label | |
| `[Selling point one/two/three]` (3–4 words each) | |
| Hero badge `[00]` + `[Stat label]` | |
| Four stat tiles: number + label | |
| Services section: label, heading, intro | |
| Six service names + one-sentence descriptions | |
| Capabilities: label, heading, intro, 12 list items | |
| Projects: label, heading, intro | |
| Three project names + captions + tags | |
| About preview: label, heading, two paragraphs | |
| Closing CTA: label, heading, one sentence | |

## 3. Services — `services.html`

| Slot | Value |
| --- | --- |
| Banner sentence | |
| Section label, heading, intro | |
| Six services, each with a 2–3 sentence description | |
| Capability groups: four group names, ~5 items each | |
| Industries: heading + three sectors with descriptions | |

## 4. Projects — `projects.html`

| Slot | Value |
| --- | --- |
| Banner sentence | |
| Six projects: name, short caption, category tag | |

Photos matter more than words on this page — see section 7.

## 5. About — `about-us.html`

| Slot | Value |
| --- | --- |
| Banner sentence | |
| Story heading + three paragraphs (~25 / 45 / 45 words) | |
| Three values: name + two lines each | |
| Service area: heading, intro, six towns or regions | |

## 6. Contact — `contact.html`

| Slot | Value |
| --- | --- |
| Banner sentence | |
| Form heading + intro | |
| Four service options for the dropdown | |
| Textarea placeholder prompt + hint line | |
| Submit button label | |
| Reassurance line under the form | |

## 7. Assets

| Item | Notes |
| --- | --- |
| Logo | `assets/img/logo.svg` — SVG preferred. Replace the file, keep the name. |
| Favicon | `assets/img/favicon.svg` |
| Hero photo | Landscape, 1600×1200 or larger |
| Project photos ×6 | 4:3 or square, shots of finished work |
| Shop photo, team photo | Optional, used on the About page |

See `assets/img/README.md` for exactly where each one goes.

## 8. Technical decisions

| Item | Notes |
| --- | --- |
| Contact form endpoint | Replace `YOUR_FORM_ID` in `contact.html` — see the comment in that file |
| Brand accent colour | `--spark` at the top of `assets/css/styles.css`; match it to the logo |
| Google Maps embed | Commented block in `contact.html`, needs the confirmed address |
| Structured data | Commented `LocalBusiness` block in `index.html`, needs name/address/phone/hours |
| Meta descriptions | One per page, ~150 characters |
