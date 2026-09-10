# Dr. Johar's Plastic Surgery Group — Website Redesign

A complete, modern redesign of **theaesthetic.in** (Dr. Manoj K Johar, Noida). Static HTML/CSS/JS — no framework, no server required. Open `index.html` in a browser or upload the folder to any host.

## What's inside

| Path | Purpose |
|---|---|
| `index.html` | Home page |
| `about.html`, `vision-mission.html`, `team.html`, `certifications-awards.html`, `news-events.html`, `education-training.html` | About section |
| `treatments.html` | Treatments hub (all 37, with live search) |
| `surgical-treatments.html`, `nonsurgical-treatments.html`, `cosmetic-medicine.html`, `preventive-aesthetics.html`, `age-reversal.html` | Category pages |
| `treatments/*.html` | 37 individual treatment pages (22 surgical, 15 non-surgical) |
| `first-visit.html`, `faqs.html`, `testimonials.html`, `video-logs.html`, `education-videos.html`, `gallery.html`, `offers.html`, `international-patients.html` | Patient guide |
| `appointments.html`, `urgent-appointments.html`, `virtual-appointments.html`, `submit-query.html`, `career.html`, `contact.html` | Forms & contact |
| `blog.html`, `blog/*.html` | Blog — 6 original articles from the old site + 6 new ones |
| `news.html`, `news/*.html` | Healthcare news — 26 items carried over from the old site |
| `disclaimer.html`, `privacy.html`, `sitemap.html`, `404.html`, `sitemap.xml`, `robots.txt` | Legal / SEO |
| `assets/css/style.css` | The whole design system (one file) |
| `assets/js/main.js` | Navigation, mega menu, mobile drawer, animations, sliders, accordions, lightbox, forms |
| `assets/img/` | Logo (dark + light), team photos, affiliation logos, video thumbnails, stock photography |
| `_build/` | Generator: `data.py` (all content) + `build.py` (templates). **Not needed for hosting** — you can delete it or keep it for editing. |

**102 HTML pages** are generated. Every internal link and asset reference has been verified (0 broken).

## Editing content

All text lives in `_build/data.py` — phones, locations, team bios, testimonials, treatments (name, tagline, overview, benefits, candidates, steps, at-a-glance facts, FAQs), offers, fellowships, blog articles, etc.

1. Edit `_build/data.py`
2. Run `python _build/build.py` from this folder (needs Python 3 — no other dependencies)
3. All pages regenerate in place.

To edit a single page by hand instead, just open its `.html` — the markup is clean and readable.

## Forms (no backend needed)

Every form (appointments, urgent, virtual, query/reports, career, contact, testimonial) validates in the browser and then opens **WhatsApp** (`+91 85277 78462`) with the message pre-filled, so enquiries work immediately with zero setup. To route to email/CRM instead, point the `<form>` at Formspree / Netlify Forms / your own endpoint and remove the `data-form` attribute (the WhatsApp handler is in `main.js`).

## Design notes

- Palette: ivory `#faf7f1`, ink `#15171b`, champagne gold `#b08a49` — pulled from the existing JPSG logo.
- Type: Cormorant Garamond (display) + Manrope (body) via Google Fonts, with system fallbacks so it still renders offline.
- Fully responsive (desktop / tablet / mobile), sticky glass header, mega menu, mobile drawer, sticky "Call / Book" bar on phones, floating WhatsApp button, scroll-reveal animations, accessible focus states, print styles.
- SEO: unique `<title>`/description per page, Open Graph tags, `sitemap.xml`, `robots.txt`, breadcrumbs.

## Please confirm / replace before going live

- **Stock photos** in `assets/img/photos/` are royalty-free (Unsplash licence) placeholders. Replace with real clinic, team and (consented) patient photography for maximum impact — same filenames, no code change.
- **Clinic hours** shown as *Mon–Sat, 10 AM–6 PM* — adjust in `data.py` → `SITE["hours"]`.
- **Offers** and **fellowship** details are illustrative — update to current programmes.
- **Video links** point to the YouTube channel (the old site had no per-video URLs). Add specific video URLs in `data.py` → `VIDEOS` if desired.
- **Google Maps** embeds use place-name search; swap for exact embed URLs from Google Maps if preferred.
