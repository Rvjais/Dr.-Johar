# -*- coding: utf-8 -*-
"""Static site generator for Dr. Johar's Plastic Surgery Group redesign.
Run:  python _build/build.py   (from the Dr.johar_renew folder)
"""
import os, re, json, html, sys
sys.path.insert(0, os.path.dirname(__file__))
from data import *  # noqa

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
BUILD_DIR = os.path.dirname(os.path.abspath(__file__))

def esc(s): return html.escape(str(s), quote=True)

# ------------------------------------------------------------------ icons
ICONS = {
    "phone": '<svg class="icon" viewBox="0 0 24 24"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.5 2.7.7a2 2 0 0 1 1.9 2.1z"/></svg>',
    "mail": '<svg class="icon" viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>',
    "pin": '<svg class="icon" viewBox="0 0 24 24"><path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/></svg>',
    "clock": '<svg class="icon" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
    "arrow": '<svg class="icon" viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
    "arrow-up": '<svg class="icon" viewBox="0 0 24 24"><path d="M12 19V5M6 11l6-6 6 6"/></svg>',
    "chev-left": '<svg class="icon" viewBox="0 0 24 24"><path d="m15 6-6 6 6 6"/></svg>',
    "chev-right": '<svg class="icon" viewBox="0 0 24 24"><path d="m9 6 6 6-6 6"/></svg>',
    "caret": '<svg class="icon caret" viewBox="0 0 24 24"><path d="m6 9 6 6 6-6"/></svg>',
    "check": '<svg class="icon" viewBox="0 0 24 24"><path d="m5 12 5 5L20 7"/></svg>',
    "plus": '<svg class="icon" viewBox="0 0 24 24"><path d="M12 5v14M5 12h14"/></svg>',
    "close": '<svg class="icon" viewBox="0 0 24 24"><path d="M6 6l12 12M18 6L6 18"/></svg>',
    "star": '<svg viewBox="0 0 24 24"><path d="M12 2.5l2.9 6 6.6.9-4.8 4.6 1.2 6.5L12 17.4l-5.9 3.1 1.2-6.5L2.5 9.4l6.6-.9z"/></svg>',
    "play": '<svg viewBox="0 0 24 24"><path d="M7 4.5v15l12-7.5z"/></svg>',
    "calendar": '<svg class="icon" viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M8 3v4M16 3v4M3 10h18"/></svg>',
    "video": '<svg class="icon" viewBox="0 0 24 24"><rect x="3" y="6" width="13" height="12" rx="2"/><path d="m16 10 5-3v10l-5-3z"/></svg>',
    "message": '<svg class="icon" viewBox="0 0 24 24"><path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-5.1A8 8 0 1 1 21 12z"/></svg>',
    "upload": '<svg class="icon" viewBox="0 0 24 24"><path d="M12 16V4M6 10l6-6 6 6M4 20h16"/></svg>',
    "award": '<svg class="icon" viewBox="0 0 24 24"><circle cx="12" cy="9" r="6"/><path d="m8.5 14-1.5 8 5-3 5 3-1.5-8"/></svg>',
    "globe": '<svg class="icon" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/></svg>',
    "users": '<svg class="icon" viewBox="0 0 24 24"><circle cx="9" cy="8" r="4"/><path d="M2 21a7 7 0 0 1 14 0M16 4a4 4 0 0 1 0 8M22 21a7 7 0 0 0-5-6.7"/></svg>',
    "user": '<svg class="icon" viewBox="0 0 24 24"><circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/></svg>',
    "heart": '<svg class="icon" viewBox="0 0 24 24"><path d="M12 21s-7.5-4.6-9.5-9A5.3 5.3 0 0 1 12 6.5 5.3 5.3 0 0 1 21.5 12c-2 4.4-9.5 9-9.5 9z"/></svg>',
    "shield": '<svg class="icon" viewBox="0 0 24 24"><path d="M12 2.5 4 6v6c0 5 3.4 8.6 8 9.5 4.6-.9 8-4.5 8-9.5V6z"/><path d="m9 12 2 2 4-4"/></svg>',
    "scalpel": '<svg class="icon" viewBox="0 0 24 24"><path d="M3 21c5-1 9-3 12-6l6-6-3-3-6 6c-3 3-5 7-6 12z"/><path d="m14 7 3 3"/></svg>',
    "sparkle": '<svg class="icon" viewBox="0 0 24 24"><path d="M12 3v4M12 17v4M3 12h4M17 12h4M5.6 5.6l2.8 2.8M15.6 15.6l2.8 2.8M5.6 18.4l2.8-2.8M15.6 8.4l2.8-2.8"/><circle cx="12" cy="12" r="2.5"/></svg>',
    "leaf": '<svg class="icon" viewBox="0 0 24 24"><path d="M5 19c8 0 14-6 14-15-9 0-15 6-15 14 0 .3 0 .7.1 1z"/><path d="M5 19c2-4 5-7 9-9"/></svg>',
    "search": '<svg class="icon" viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>',
    "external": '<svg class="icon" viewBox="0 0 24 24"><path d="M14 4h6v6M20 4l-9 9M19 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1h5"/></svg>',
    "doc": '<svg class="icon" viewBox="0 0 24 24"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5M9 13h6M9 17h6"/></svg>',
    "hospital": '<svg class="icon" viewBox="0 0 24 24"><path d="M3 21h18M5 21V5a1 1 0 0 1 1-1h12a1 1 0 0 1 1 1v16"/><path d="M12 8v6M9 11h6M9 21v-4h6v4"/></svg>',
    "stetho": '<svg class="icon" viewBox="0 0 24 24"><path d="M6 3v6a5 5 0 0 0 10 0V3"/><path d="M11 14v2a4 4 0 0 0 8 0v-3"/><circle cx="19" cy="11" r="2"/></svg>',
    "flask": '<svg class="icon" viewBox="0 0 24 24"><path d="M9 3h6M10 3v6L4.5 19a1.5 1.5 0 0 0 1.3 2.2h12.4a1.5 1.5 0 0 0 1.3-2.2L14 9V3"/></svg>',
    "grad": '<svg class="icon" viewBox="0 0 24 24"><path d="m2 9 10-5 10 5-10 5z"/><path d="M6 11.5V17c0 1.5 3 3 6 3s6-1.5 6-3v-5.5M22 9v6"/></svg>',
    "quote": '<svg class="icon" viewBox="0 0 24 24"><path d="M7 7h4v6H5V9a2 2 0 0 1 2-2zM17 7h4v6h-6V9a2 2 0 0 1 2-2z"/><path d="M11 13c0 3-2 5-5 5M21 13c0 3-2 5-5 5"/></svg>',
    "camera": '<svg class="icon" viewBox="0 0 24 24"><path d="M4 8h3l2-3h6l2 3h3a1 1 0 0 1 1 1v10a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V9a1 1 0 0 1 1-1z"/><circle cx="12" cy="13" r="3.5"/></svg>',
    "gift": '<svg class="icon" viewBox="0 0 24 24"><rect x="3" y="8" width="18" height="4"/><path d="M5 12v9h14v-9M12 8v13M12 8s-3-5-5-3 5 3 5 3zM12 8s3-5 5-3-5 3-5 3z"/></svg>',
    "briefcase": '<svg class="icon" viewBox="0 0 24 24"><rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2M3 12h18"/></svg>',
    "plane": '<svg class="icon" viewBox="0 0 24 24"><path d="M21 12 3 4l3 8-3 8z"/><path d="M6 12h15"/></svg>',
    "wa": '<svg viewBox="0 0 24 24"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.6.8-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.8-1.4a.5.5 0 0 0 0-.5l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.8 12 12 0 0 0 4.6 4c1.7.7 2.4.8 3.2.7a2.8 2.8 0 0 0 1.8-1.3 2.2 2.2 0 0 0 .2-1.3c-.1-.1-.3-.2-.5-.3z"/></svg>',
    "fb": '<svg viewBox="0 0 24 24"><path d="M13.5 22v-8h2.7l.4-3.2h-3.1V8.8c0-.9.3-1.6 1.6-1.6h1.7V4.4a22 22 0 0 0-2.5-.1c-2.4 0-4.1 1.5-4.1 4.2v2.3H7.5V14h2.7v8z"/></svg>',
    "ig": '<svg viewBox="0 0 24 24"><path d="M12 7.3a4.7 4.7 0 1 0 0 9.4 4.7 4.7 0 0 0 0-9.4zm0 7.7a3 3 0 1 1 0-6 3 3 0 0 1 0 6zm6-7.9a1.1 1.1 0 1 1-2.2 0 1.1 1.1 0 0 1 2.2 0zM21.1 8.2c-.1-1.5-.4-2.8-1.5-3.9S17.3 2.9 15.8 2.8c-1.5-.1-6.1-.1-7.6 0-1.5.1-2.8.4-3.9 1.5S2.9 6.7 2.8 8.2c-.1 1.5-.1 6.1 0 7.6.1 1.5.4 2.8 1.5 3.9s2.4 1.4 3.9 1.5c1.5.1 6.1.1 7.6 0 1.5-.1 2.8-.4 3.9-1.5s1.4-2.4 1.5-3.9c.1-1.5.1-6.1 0-7.6zm-2 9.3a3 3 0 0 1-1.7 1.7c-1.2.5-4 .4-5.4.4s-4.2.1-5.4-.4a3 3 0 0 1-1.7-1.7c-.5-1.2-.4-4-.4-5.4s-.1-4.2.4-5.4a3 3 0 0 1 1.7-1.7c1.2-.5 4-.4 5.4-.4s4.2-.1 5.4.4a3 3 0 0 1 1.7 1.7c.5 1.2.4 4 .4 5.4s.1 4.2-.4 5.4z"/></svg>',
    "yt": '<svg viewBox="0 0 24 24"><path d="M22.5 7.2a2.7 2.7 0 0 0-1.9-1.9C18.9 5 12 5 12 5s-6.9 0-8.6.3A2.7 2.7 0 0 0 1.5 7.2 28 28 0 0 0 1 12a28 28 0 0 0 .5 4.8 2.7 2.7 0 0 0 1.9 1.9C5.1 19 12 19 12 19s6.9 0 8.6-.3a2.7 2.7 0 0 0 1.9-1.9A28 28 0 0 0 23 12a28 28 0 0 0-.5-4.8zM9.8 15V9l5.7 3z"/></svg>',
    "tw": '<svg viewBox="0 0 24 24"><path d="M17.5 3h3.1l-6.8 7.8L21.8 21h-6.3l-4.9-6.4L5 21H1.9l7.3-8.3L1.5 3H8l4.4 5.9zm-1.1 16.2h1.7L7 4.7H5.2z"/></svg>',
}
def ic(name, cls=None):
    s = ICONS[name]
    if cls: s = s.replace('class="icon"', f'class="icon {cls}"', 1) if 'class="icon"' in s else s.replace('<svg', f'<svg class="{cls}"', 1)
    return s

# ------------------------------------------------------------------ helpers
SURG = [t for t in TREATMENTS if t["cat"] == "surgical"]
NONSURG = [t for t in TREATMENTS if t["cat"] == "nonsurgical"]
T_BY_SLUG = {t["slug"]: t for t in TREATMENTS}
CAT_BY_SLUG = {c["slug"]: c for c in CATEGORIES}

def turl(root, t): return f"{root}treatments/{t['slug']}.html"
def photo(root, f): return f"{root}assets/img/photos/{f}"

def btn(label, href, style="", icon="arrow", extra=""):
    return f'<a class="btn {style}" href="{href}" {extra}>{esc(label)}{ic(icon) if icon else ""}</a>'

def link_arrow(label, href, style=""):
    return f'<a class="link-arrow {style}" href="{href}">{esc(label)}{ic("arrow")}</a>'

def eyebrow(text, center=False):
    return f'<div class="eyebrow{" eyebrow--center" if center else ""}">{esc(text)}</div>'

def section_head(eb, title, desc=None, center=False, row=False, right=""):
    cls = "section-head" + (" section-head--center" if center else "") + (" section-head--row" if row else "")
    inner = f'{eyebrow(eb, center)}<h2 class="h2">{title}</h2>' + (f'<p class="lead">{desc}</p>' if desc else "")
    if row:
        return f'<div class="{cls}"><div>{inner}</div>{right}</div>'
    return f'<div class="{cls}">{inner}</div>'

# ------------------------------------------------------------------ header / footer
def nav_about(root):
    items = [("About Us", "about.html", "user"), ("Vision & Mission", "vision-mission.html", "heart"), ("Our Team", "team.html", "users"),
             ("Certifications & Awards", "certifications-awards.html", "award"), ("News & Events", "news-events.html", "globe"),
             ("Education & Training", "education-training.html", "grad")]
    return "".join(f'<a href="{root}{h}">{ic(i)}{esc(l)}</a>' for l, h, i in items)

def nav_patient(root):
    items = [("First Visit", "first-visit.html"), ("FAQ's", "faqs.html"), ("Patient Testimonials", "testimonials.html"), ("Video Logs", "video-logs.html"),
             ("Patient Education Videos", "education-videos.html"), ("Gallery", "gallery.html"), ("Offers", "offers.html"), ("International Patients", "international-patients.html"),
             ("Blog", "blog.html"), ("Healthcare News", "news.html")]
    return "".join(f'<a href="{root}{h}">{ic("arrow")}{esc(l)}</a>' for l, h in items)

def nav_appts(root):
    items = [("Book an Appointment", "appointments.html"), ("Urgent Appointments", "urgent-appointments.html"), ("Virtual Appointments", "virtual-appointments.html"),
             ("Submit a Query / Reports", "submit-query.html"), ("International Patients", "international-patients.html"), ("Career", "career.html"), ("Contact Us", "contact.html")]
    return "".join(f'<a href="{root}{h}">{ic("arrow")}{esc(l)}</a>' for l, h in items)

def mega(root):
    half = (len(SURG) + 1) // 2
    cats = "".join(f'<a href="{root}{c["slug"]}.html"><span class="icon-tile">{ic(c["icon"])}</span>{esc(c["name"])}</a>' for c in CATEGORIES)
    s1 = "".join(f'<a href="{turl(root,t)}">{esc(t["menu"])}</a>' for t in SURG[:half])
    s2 = "".join(f'<a href="{turl(root,t)}">{esc(t["menu"])}</a>' for t in SURG[half:])
    ns = "".join(f'<a href="{turl(root,t)}">{esc(t["menu"])}</a>' for t in NONSURG)
    return f'''<div class="mega">
      <div class="mega__col"><div class="mega__title">Explore <a href="{root}treatments.html">View all</a></div><div class="mega__cats">{cats}</div></div>
      <div class="mega__col"><div class="mega__title">Surgical <a href="{root}surgical-treatments.html">All surgical</a></div><div class="mega__list">{s1}</div></div>
      <div class="mega__col"><div class="mega__title">&nbsp;</div><div class="mega__list">{s2}</div></div>
      <div class="mega__col"><div class="mega__title">Non-Surgical <a href="{root}nonsurgical-treatments.html">All non-surgical</a></div><div class="mega__list">{ns}</div></div>
    </div>'''

def header(root):
    social = "".join(f'<a href="{SITE["social"][k]}" target="_blank" rel="noopener" aria-label="{k}">{ic(i)}</a>' for k, i in [("facebook","fb"),("instagram","ig"),("youtube","yt"),("twitter","tw")])
    return f'''
<div class="topbar">
  <div class="container">
    <ul class="topbar__list">
      <li><a href="tel:{SITE['phone1_raw']}">{ic("phone")}{SITE['phone1']}</a></li>
      <li class="topbar__list--secondary"><a href="tel:{SITE['phone2_raw']}">{ic("phone")}{SITE['phone2']}</a></li>
      <li class="topbar__list--secondary"><span class="topbar__sep"></span></li>
      <li class="topbar__list--secondary"><a href="{root}contact.html">{ic("pin")}Noida · Vaishali · Patparganj</a></li>
    </ul>
    <ul class="topbar__list">
      <li class="topbar__list--secondary"><a href="{root}international-patients.html">{ic("globe")}International Patients</a></li>
      <li class="topbar__list--secondary"><a href="{root}urgent-appointments.html">{ic("clock")}Urgent Appointments</a></li>
      <li><div class="topbar__social">{social}</div></li>
    </ul>
  </div>
</div>
<header class="header">
  <div class="container header__inner">
    <a class="brand" href="{root}index.html" aria-label="{esc(SITE['name'])}"><img src="{root}assets/img/logo.png" alt="{esc(SITE['name'])}"></a>
    <nav aria-label="Main">
      <ul class="nav">
        <li><a href="{root}index.html">Home</a></li>
        <li><button type="button" aria-haspopup="true">About{ic("caret")}</button><div class="dropdown">{nav_about(root)}</div></li>
        <li class="has-mega"><button type="button" aria-haspopup="true">Treatments{ic("caret")}</button>{mega(root)}</li>
        <li><button type="button" aria-haspopup="true">Patient Guide{ic("caret")}</button><div class="dropdown">{nav_patient(root)}</div></li>
        <li><button type="button" aria-haspopup="true">Appointments{ic("caret")}</button><div class="dropdown">{nav_appts(root)}</div></li>
        <li><a href="{root}contact.html">Contact</a></li>
      </ul>
    </nav>
    <div class="header__cta">
      <a class="header__phone" href="tel:{SITE['phone1_raw']}">{ic("phone")}{SITE['phone1']}</a>
      <a class="btn btn--gold btn--sm" href="{root}appointments.html">Book an Appointment</a>
      <button class="nav-toggle" aria-label="Open menu"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>
<div class="drawer" aria-hidden="true">
  <div class="drawer__scrim"></div>
  <div class="drawer__panel">
    <div class="drawer__head"><img src="{root}assets/img/logo.png" alt=""><button class="drawer__close" aria-label="Close menu">{ic("close")}</button></div>
    <ul class="drawer__nav">
      <li><a href="{root}index.html">Home</a></li>
      <li><button type="button">About{ic("caret")}</button><div class="drawer__sub">{nav_about(root)}</div></li>
      <li><button type="button">Treatments{ic("caret")}</button><div class="drawer__sub">
        <div class="drawer__sub-title">Categories</div>{"".join(f'<a href="{root}{c["slug"]}.html">{esc(c["name"])}</a>' for c in CATEGORIES)}
        <div class="drawer__sub-title">Surgical</div>{"".join(f'<a href="{turl(root,t)}">{esc(t["menu"])}</a>' for t in SURG)}
        <div class="drawer__sub-title">Non-Surgical</div>{"".join(f'<a href="{turl(root,t)}">{esc(t["menu"])}</a>' for t in NONSURG)}
      </div></li>
      <li><button type="button">Patient Guide{ic("caret")}</button><div class="drawer__sub">{nav_patient(root)}</div></li>
      <li><button type="button">Appointments{ic("caret")}</button><div class="drawer__sub">{nav_appts(root)}</div></li>
      <li><a href="{root}contact.html">Contact Us</a></li>
    </ul>
    <div class="drawer__foot">
      <a class="btn btn--gold" href="{root}appointments.html">Book an Appointment</a>
      <a class="btn btn--outline" href="tel:{SITE['phone1_raw']}">{ic("phone")}{SITE['phone1']}</a>
    </div>
  </div>
</div>'''

def footer(root):
    social = "".join(f'<a href="{SITE["social"][k]}" target="_blank" rel="noopener" aria-label="{k}">{ic(i)}</a>' for k, i in [("facebook","fb"),("instagram","ig"),("youtube","yt"),("twitter","tw")])
    locs = "".join(f'<li>{ic("pin")}<span><strong style="color:#fff;font-weight:600">{esc(l["name"])}</strong><br>{esc(l["address"])}</span></li>' for l in LOCATIONS)
    quick = [("About Us","about.html"),("Our Team","team.html"),("Surgical Treatments","surgical-treatments.html"),("Non-Surgical Treatments","nonsurgical-treatments.html"),("Patient Testimonials","testimonials.html"),("Video Logs","video-logs.html"),("Blog","blog.html"),("Healthcare News","news.html"),("Careers","career.html")]
    pat = [("Book an Appointment","appointments.html"),("Urgent Appointments","urgent-appointments.html"),("Virtual Consultation","virtual-appointments.html"),("First Visit Guide","first-visit.html"),("FAQ's","faqs.html"),("International Patients","international-patients.html"),("Submit a Query","submit-query.html"),("Offers","offers.html"),("Contact Us","contact.html")]
    return f'''
<footer class="footer">
  <div class="container">
    <div class="footer__top">
      <div class="footer__brand">
        <img src="{root}assets/img/logo-light.png" alt="{esc(SITE['name'])}">
        <p>Dr. Manoj K Johar and his team offer the complete spectrum of plastic, aesthetic and reconstructive surgery — with compassion, honesty and a commitment to excellence — at Max Healthcare hospitals across Delhi-NCR.</p>
        <div class="footer__social">{social}</div>
      </div>
      <div><h4>Quick Links</h4><ul class="footer__links">{"".join(f'<li><a href="{root}{h}">{esc(l)}</a></li>' for l,h in quick)}</ul></div>
      <div><h4>For Patients</h4><ul class="footer__links">{"".join(f'<li><a href="{root}{h}">{esc(l)}</a></li>' for l,h in pat)}</ul></div>
      <div><h4>Contact</h4>
        <ul class="footer__contact">
          <li>{ic("phone")}<span><a href="tel:{SITE['phone1_raw']}">{SITE['phone1']}</a><br><a href="tel:{SITE['phone2_raw']}">{SITE['phone2']}</a></span></li>
          <li>{ic("message")}<span><a href="https://api.whatsapp.com/send?phone={SITE['whatsapp']}" target="_blank" rel="noopener">WhatsApp us</a></span></li>
          <li>{ic("clock")}<span>{SITE['hours']}</span></li>
          {locs}
        </ul>
      </div>
    </div>
    <p class="footer__disclaimer">The information on this website is for general educational purposes only and is not a substitute for professional medical advice. Individual results vary. Please consult Dr. Johar or a qualified specialist for advice about your specific condition.</p>
    <div class="footer__bottom">
      <div>© <span data-year>2026</span> {esc(SITE['name'])}. All rights reserved.</div>
      <ul><li><a href="{root}disclaimer.html">Disclaimer</a></li><li><a href="{root}privacy.html">Privacy</a></li><li><a href="{root}sitemap.html">Sitemap</a></li><li><a href="{root}contact.html">Feedback</a></li></ul>
    </div>
  </div>
</footer>
<a class="float-wa" href="https://api.whatsapp.com/send?phone={SITE['whatsapp']}&text=Hello%20Dr.%20Johar%27s%20team%2C%20I%20would%20like%20to%20book%20a%20consultation." target="_blank" rel="noopener" aria-label="Chat on WhatsApp">{ic("wa")}</a>
<button class="to-top" aria-label="Back to top">{ic("arrow-up")}</button>
<div class="mobile-cta"><a class="btn btn--outline" href="tel:{SITE['phone1_raw']}">{ic("phone")}Call</a><a class="btn btn--gold" href="{root}appointments.html">{ic("calendar")}Book</a></div>
<script src="{root}assets/js/main.js"></script>'''

def page(title, desc, body, root="", canonical="", og_img=None):
    og = og_img or f"{root}assets/img/photos/hero-main.jpg"
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:type" content="website">
<meta property="og:image" content="{og}">
<meta name="theme-color" content="#15171b">
<link rel="icon" type="image/png" href="{root}assets/img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500;1,600&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}assets/css/style.css">
</head>
<body>
{header(root)}
<main>
{body}
</main>
{footer(root)}
</body>
</html>'''

def page_hero(root, title, crumbs, desc="", img=None, meta="", actions="", plain=False, visual=None):
    crumb_html = ""
    for i, (label, href) in enumerate(crumbs):
        if i: crumb_html += ic("chev-right")
        crumb_html += f'<a href="{root}{href}">{esc(label)}</a>' if href else f'<span>{esc(label)}</span>'
    bg = f'<img class="page-hero__bg" src="{photo(root, img)}" alt="">' if img and not plain else ""
    inner = f'<div class="crumbs">{crumb_html}</div><h1 class="h1">{title}</h1>' + (f'<p>{desc}</p>' if desc else "") + meta + (f'<div class="page-hero__actions">{actions}</div>' if actions else "")
    if visual:
        inner = f'<div class="page-hero__grid"><div>{inner}</div><div class="page-hero__visual">{visual}</div></div>'
    return f'<section class="page-hero{" page-hero--plain" if plain else ""}">{bg}<div class="container">{inner}</div></section>'

def cta_band(root, title="Ready to take the first step?", text="Book a consultation with Dr. Manoj K Johar and his team. We listen first, then guide you honestly to the treatment that is right for you.", img="operating-room.jpg"):
    return f'''
<section class="section section--sm"><div class="container">
  <div class="cta reveal">
    <img src="{photo(root,img)}" alt="">
    <div class="cta__grid">
      <div><h2 class="h2">{title}</h2><p>{text}</p>
        <div class="cta__actions">{btn("Book an Appointment", root+"appointments.html", "btn--gold", "calendar")}{btn("Virtual Consultation", root+"virtual-appointments.html", "btn--light-outline", "video")}</div>
      </div>
      <div class="cta__contact">
        <a href="tel:{SITE['phone1_raw']}"><span class="icon-tile">{ic("phone")}</span><span><small>Call us</small><strong>{SITE['phone1']}</strong></span></a>
        <a href="https://api.whatsapp.com/send?phone={SITE['whatsapp']}" target="_blank" rel="noopener"><span class="icon-tile">{ic("message")}</span><span><small>WhatsApp</small><strong>Chat with our team</strong></span></a>
        <a href="{root}contact.html"><span class="icon-tile">{ic("pin")}</span><span><small>Visit</small><strong>Max Hospitals — Noida · Vaishali · Patparganj</strong></span></a>
      </div>
    </div>
  </div>
</div></section>'''

def team_grid(root, compact=False):
    cards = ""
    for m in TEAM:
        cards += f'''<div class="team-card{" team-card--lead" if m.get("lead") else ""}">
          <div class="team-card__img"><img src="{root}assets/img/team/{m["img"]}" alt="{esc(m["name"])}"></div>
          <h3>{esc(m["name"])}</h3><p>{esc(m["role"])}<br>{esc(m["dept"])}</p>
          {link_arrow("View Profile", root+"team.html#"+m["slug"], "link-arrow--gold")}
        </div>'''
    return f'<div class="grid grid-5 reveal-stagger">{cards}</div>'

def testimonial_cards(dark=False):
    out = ""
    for t in TESTIMONIALS:
        initials = "".join(w[0] for w in t["name"].split()[:2]).upper()
        out += f'''<article class="testi{" testi--dark" if dark else ""}"><span class="testi__quote">“</span>
          <div class="testi__stars">{ic("star")*5}</div>
          <p>{esc(t["text"])}</p>
          <div class="testi__author"><span class="avatar">{initials}</span><span><strong>{esc(t["name"])}</strong><span>{esc(t["for"])}</span></span></div>
        </article>'''
    return out

def testimonials_section(root, dark=True):
    return f'''
<section class="section {"bg-ink" if dark else "bg-cream"}"><div class="container">
  <div class="section-head section-head--row reveal">
    <div>{eyebrow("Patient Stories")}<h2 class="h2">Trusted by patients<br>across Delhi-NCR &amp; beyond</h2></div>
    <div class="flex items-center gap-2 wrap"><span class="google-badge"><span class="g">G</span><span>Google Reviews <span class="stars">★★★★★</span></span></span><div class="slider-nav {"slider-nav--light" if dark else ""}"><button data-prev aria-label="Previous">{ic("chev-left")}</button><button data-next aria-label="Next">{ic("chev-right")}</button></div></div>
  </div>
  <div class="testi-wrap" data-slider><div class="testi-track">{testimonial_cards(dark)}</div></div>
  <div class="mt-4 flex gap-2 wrap">{btn("View All Testimonials", root+"testimonials.html", "btn--light-outline" if dark else "btn--outline")}{btn("Share Your Story", root+"testimonials.html#submit", "btn--gold", "heart")}</div>
</div></section>'''

def faq_accordion(items, light=False, open_first=True):
    out = ""
    for i, (q, a) in enumerate(items):
        out += f'''<div class="acc{" is-open" if (open_first and i == 0) else ""}"><button class="acc__btn" aria-expanded="{"true" if (open_first and i==0) else "false"}"><span>{esc(q)}</span><span class="acc__icon">{ic("plus")}</span></button><div class="acc__panel"><div class="acc__body"><p>{esc(a)}</p></div></div></div>'''
    return f'<div class="accordion{" accordion--light" if light else ""}">{out}</div>'

def video_card(root, v, large=False):
    return f'''<a class="video-card{" video-card--lg" if large else ""}" href="{SITE['social']['youtube']}" target="_blank" rel="noopener">
      <img src="{root}assets/img/videos/{v["img"]}" alt="{esc(v["title"])}"><span class="video-card__play">{ic("play")}</span><span class="video-card__title">{esc(v["title"])}</span></a>'''

def locations_cards(root):
    out = ""
    for l in LOCATIONS:
        out += f'''<div class="loc-card"><span class="icon-tile">{ic("hospital")}</span><h3>{esc(l["name"])}</h3><address>{esc(l["address"])}</address>
          <div class="loc-card__foot">{btn("Directions", l["map"], "btn--outline btn--sm", "pin", 'target="_blank" rel="noopener"')}<a class="btn btn--sm btn--gold" href="tel:{SITE['phone1_raw']}">{ic("phone")}Call</a></div></div>'''
    return f'<div class="grid grid-3 reveal-stagger">{out}</div>'

def tcard(root, t, idx=None):
    facts = t["facts"]
    keys = list(facts.keys())[:2]
    chips = "".join(f'<span class="chip chip--muted">{esc(k)}: {esc(facts[k])}</span>' for k in keys)
    cat = "Surgical" if t["cat"] == "surgical" else "Non-Surgical"
    return f'''<a class="tcard" href="{turl(root,t)}" data-treatment-item="{esc((t["name"]+" "+t["tagline"]+" "+cat).lower())}">
      <div class="tcard__top"><span class="chip{'' if t['cat']=='surgical' else ' chip--muted'}">{cat}</span>{f'<span class="tcard__idx">{idx:02d}</span>' if idx else ''}</div>
      <h3>{esc(t["name"])}</h3><p>{esc(t["tagline"])}</p>
      <div class="tcard__meta">{chips}</div>
      <span class="link-arrow link-arrow--gold">Learn more{ic("arrow")}</span></a>'''

def blog_all():
    """Merge scraped articles + newly authored ones into a single list, newest first."""
    arts = []
    for a in NEW_ARTICLES:
        arts.append(dict(a, source="new"))
    with open(os.path.join(BUILD_DIR, "blog_articles.json"), encoding="utf-8") as f:
        old = json.load(f)
    for a in old:
        title = a["title"].replace("’", "'").replace("�", "'")
        slug, cat, img = OLD_ARTICLE_META.get(title, (re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-'), "Wellness", "facial-spa.jpg"))
        blocks = []
        for b in a["blocks"]:
            for k, v in b.items():
                blocks.append({k: v.replace("�", "'")})
        excerpt = next((b["p"] for b in blocks if "p" in b), "")
        excerpt = excerpt[:150].rsplit(" ", 1)[0] + "…" if len(excerpt) > 150 else excerpt
        d = a["date"]  # 10-Jun-2022
        dd, mm, yy = d.split("-")
        arts.append(dict(slug=slug, title=title, date=f"{int(dd)} {mm} {yy}", cat=cat, img=img, excerpt=excerpt, blocks=blocks, source="old"))
    return arts

def news_all():
    with open(os.path.join(BUILD_DIR, "news.json"), encoding="utf-8") as f:
        news = json.load(f)
    imgs = ["consultation.jpg", "face-natural.jpg", "surgeons-operating.jpg", "woman-smiling.jpg", "mature-woman.jpg", "baby-feet.jpg", "facial-spa.jpg", "body-fitness.jpg", "hospital-room.jpg", "skin-closeup.jpg"]
    out = []
    from datetime import datetime
    for i, n in enumerate(news):
        slug = re.sub(r'[^a-z0-9]+', '-', n["title"].lower()).strip('-')[:70].rstrip('-')
        dt = datetime.strptime(n["date"], "%d-%b-%Y")
        out.append(dict(n, slug=slug, dt=dt, date=dt.strftime("%d %b %Y"), img=imgs[i % len(imgs)]))
    out.sort(key=lambda x: x["dt"], reverse=True)
    return out

def post_card(root, a, path="blog"):
    return f'''<article class="post-card"><a class="post-card__img" href="{root}{path}/{a["slug"]}.html"><img src="{photo(root,a["img"])}" alt="" loading="lazy"><span class="chip post-tag">{esc(a.get("cat") or a.get("source",""))}</span></a>
      <div class="post-card__body"><div class="post-card__meta"><span>{esc(a["date"])}</span><i></i><span>{esc(a.get("cat","News"))}</span></div>
      <h3><a href="{root}{path}/{a["slug"]}.html">{esc(a["title"])}</a></h3><p>{esc(a["excerpt"])}</p>{link_arrow("Read article", f"{root}{path}/{a['slug']}.html", "link-arrow--gold")}</div></article>'''

# ------------------------------------------------------------------ HOME
def build_home():
    root = ""
    cred = "".join(f'<div class="marquee__item"><img src="assets/img/credentials/{f}" alt="{esc(n)}"><span>{esc(n)}</span></div>' for f, n in CREDENTIALS)
    cat_tiles = ""
    for i, c in enumerate(CATEGORIES):
        cat_tiles += f'''<a class="cat-tile{" cat-tile--tall" if i == 0 else ""}" href="{c["slug"]}.html"><img src="{photo(root,c["img"])}" alt="" loading="lazy"><span class="cat-tile__num">0{i+1}</span>
          <h3>{esc(c["name"])}</h3><p>{esc(c["tag"])} — {esc(c["desc"][:120])}…</p><span class="link-arrow">Explore{ic("arrow")}</span></a>'''
    surg_top = ["rhinoplasty-nose-job","facelift","liposuction","abdominoplasty-tummy-tuck-mommy-makeover","breast-surgery","gynaecomastia","hair-transplant","blepharoplasty-eyelid-surgery"]
    ns_top = ["botox","fillers","lasers","prp","acne-and-acne-scars","skin-tightening","thread-lift","chemical-peel"]
    surg_links = "".join(f'<a href="{turl(root,T_BY_SLUG[s])}">{esc(T_BY_SLUG[s]["menu"])}</a>' for s in surg_top)
    ns_links = "".join(f'<a href="{turl(root,T_BY_SLUG[s])}">{esc(T_BY_SLUG[s]["menu"])}</a>' for s in ns_top)
    faq_items = FAQS[:6]
    arts = blog_all()[:3]
    body = f'''
<!-- HERO -->
<section class="hero">
  <div class="hero__bg-text" aria-hidden="true">Beauty</div>
  <div class="container hero__grid">
    <div class="hero__content">
      <div class="hero__badge reveal"><span class="dot">{ic("award")}</span>Plastic, Aesthetic &amp; Reconstructive Surgery · Max Healthcare</div>
      <h1 class="display-1 hero__title reveal">Committed to Excellence in <em>Plastic &amp; Reconstructive</em> Surgery</h1>
      <p class="lead hero__lead reveal">Experience a more beautiful, more confident you. Dr. Manoj K Johar — one of Noida's most trusted plastic surgeons — offers surgical and non-surgical solutions with honesty, artistry and care.</p>
      <div class="hero__actions reveal">{btn("Book an Appointment", "appointments.html", "btn--gold btn--lg", "calendar")}{btn("Explore Treatments", "treatments.html", "btn--outline btn--lg")}</div>
      <div class="hero__trust reveal">
        <div class="hero__trust-item"><strong>3</strong><span>Max Hospitals</span></div>
        <div class="hero__trust-item"><strong>35+</strong><span>Treatments</span></div>
        <div class="hero__trust-item"><strong>5</strong><span>Specialist Doctors</span></div>
        <div class="hero__trust-item"><strong>24/7</strong><span>Urgent Care</span></div>
      </div>
    </div>
    <div class="hero__visual reveal">
      <span class="hero__ring"></span><span class="hero__ring hero__ring--2"></span>
      <div class="hero__frame"><img src="{photo(root,'hero-main.jpg')}" alt="Aesthetic plastic surgery in Noida" fetchpriority="high"></div>
      <div class="hero__card hero__card--1"><span class="icon-tile">{ic("shield")}</span><span><strong>Accredited Hospitals</strong><span>Max Healthcare, Delhi-NCR</span></span></div>
      <div class="hero__card hero__card--2"><span class="icon-tile">{ic("heart")}</span><span><strong>Personalised Care</strong><span>Every plan begins with listening</span></span></div>
    </div>
  </div>
  <div class="hero__scroll"><span>Scroll</span><i></i></div>
</section>

<!-- CREDENTIALS -->
<div class="strip"><div class="container strip__inner"><span class="strip__label">Affiliations</span><div class="marquee"><div class="marquee__track">{cred}</div></div></div></div>

<!-- ABOUT DOCTOR -->
<section class="section"><div class="container">
  <div class="split split--wide">
    <div class="doc-visual reveal">
      <div class="doc-visual__pattern"></div>
      <div class="doc-visual__frame"><img src="assets/img/team/dr-manoj-johar.jpg" alt="Dr. Manoj K Johar"></div>
      <div class="doc-visual__badge"><span><strong>Max</strong><span>Group Head</span></span></div>
      <div class="doc-visual__quote"><p>“Surgery is as much an art as a science — the goal is a result that looks like you, only rested.”</p><span>Dr. Manoj K Johar</span></div>
    </div>
    <div class="reveal">
      {eyebrow("Meet the Surgeon")}
      <h2 class="h2">Best Plastic Surgeon in Noida:<br>Dr. Manoj K Johar</h2>
      <p class="lead mt-3">Dr. Manoj K. Johar is a renowned cosmetic and plastic surgeon with extensive experience in both cosmetic and reconstructive procedures. He is dedicated to providing highly personalised care that meets the unique needs of every patient.</p>
      <p class="mt-2 muted">Whether you are seeking cosmetic surgery to enhance your appearance or reconstructive surgery to address a medical condition, his compassionate approach and commitment to excellence have made him one of the most trusted plastic surgeons in the region.</p>
      <ul class="checklist mt-4 two-col">
        <li>Aesthetic &amp; cosmetic surgery</li><li>Breast surgery &amp; reconstruction</li><li>Craniofacial &amp; cleft surgery</li><li>Cancer reconstruction</li><li>Limb preservation</li><li>Non-surgical rejuvenation</li>
      </ul>
      <div class="flex items-center gap-3 wrap mt-4">{btn("About Dr. Johar", "about.html", "btn--gold")}{link_arrow("Meet the full team", "team.html")}</div>
      <div class="signature">Dr. Manoj K Johar<small>Principal Director &amp; Group Head, Max Healthcare</small></div>
    </div>
  </div>
</div></section>

<!-- CATEGORIES -->
<section class="section bg-white"><div class="container">
  {section_head("Transformative Treatments", "Five pathways to a<br>more confident you", "From complex reconstruction to a lunchtime glow — every treatment is chosen for you after an honest consultation.", row=True, right=btn("View All Treatments", "treatments.html", "btn--outline"))}
  <div class="grid grid-3 reveal-stagger" style="grid-template-rows:auto auto">{cat_tiles}</div>
</div></section>

<!-- SURGICAL / NON-SURGICAL SHOWCASE -->
<section class="section bg-ink"><div class="container">
  <div class="split">
    <div class="reveal">
      {eyebrow("Surgical Treatments")}
      <h2 class="h2">Reconstructive &amp; aesthetic surgery at accredited hospitals</h2>
      <p class="lead mt-3">Plastic surgery improves aesthetic appearance and function by reconstructing parts of the body damaged by burns, trauma, disease or congenital conditions — as well as refining features you were born with. Dr. Johar performs the full spectrum at Max Healthcare.</p>
      <div class="mega__list mt-4" style="display:grid;grid-template-columns:1fr 1fr;gap:4px">{surg_links.replace('<a ', '<a style="color:#d9d4ca;border:1px solid rgba(255,255,255,.1);padding:10px 14px;border-radius:10px" ')}</div>
      <div class="mt-4">{btn("All Surgical Treatments", "surgical-treatments.html", "btn--gold")}</div>
    </div>
    <div class="reveal">
      <div class="page-hero__visual" style="aspect-ratio:4/3"><img src="{photo(root,'surgeons-operating.jpg')}" alt="Surgical team at Max Hospital" loading="lazy"></div>
    </div>
  </div>
  <div class="split split--rev mt-5" style="margin-top:clamp(56px,7vw,96px)">
    <div class="reveal">
      {eyebrow("Non-Surgical Treatments")}
      <h2 class="h2">Look your best — without surgery</h2>
      <p class="lead mt-3">We offer a range of non-surgical treatments that improve your appearance with little or no downtime. After a thorough evaluation, Dr. Johar discusses the options — injectables, lasers, peels, PRP, threads and more — that best suit your concern.</p>
      <div class="mega__list mt-4" style="display:grid;grid-template-columns:1fr 1fr;gap:4px">{ns_links.replace('<a ', '<a style="color:#d9d4ca;border:1px solid rgba(255,255,255,.1);padding:10px 14px;border-radius:10px" ')}</div>
      <div class="mt-4">{btn("All Non-Surgical Treatments", "nonsurgical-treatments.html", "btn--gold")}</div>
    </div>
    <div class="reveal">
      <div class="page-hero__visual" style="aspect-ratio:4/3"><img src="{photo(root,'facial-spa.jpg')}" alt="Non-surgical facial rejuvenation" loading="lazy"></div>
    </div>
  </div>
</div></section>

<!-- WHY CHOOSE -->
<section class="section"><div class="container">
  {section_head("Why Dr. Johar's", "Care that puts you first", "A group practice built on honesty, safety and results that stand the test of time.", center=True)}
  <div class="grid grid-4 reveal-stagger">
    <div class="card"><span class="icon-tile">{ic("stetho")}</span><h3 class="h4">Expert-Led Team</h3><p>Every case is planned and led by Dr. Johar with a team of senior consultant plastic surgeons and allied specialists.</p></div>
    <div class="card"><span class="icon-tile">{ic("hospital")}</span><h3 class="h4">Accredited Hospitals</h3><p>Surgery is performed only in fully equipped Max Healthcare operating theatres with dedicated anaesthesia and ICU support.</p></div>
    <div class="card"><span class="icon-tile">{ic("heart")}</span><h3 class="h4">Honest Advice</h3><p>We tell you when a procedure is not right for you, when a non-surgical option will do, and what a result can realistically achieve.</p></div>
    <div class="card"><span class="icon-tile">{ic("sparkle")}</span><h3 class="h4">Natural Results</h3><p>Our philosophy is refinement, not transformation — results that look like you, only rested and confident.</p></div>
  </div>
</div></section>

<!-- TEAM -->
<section class="section bg-white section--flush-top"><div class="container">
  {section_head("Our Team", "Meet the specialists", row=True, right=btn("View Full Team", "team.html", "btn--outline"))}
  {team_grid(root)}
</div></section>

<!-- VIDEO LOGS -->
<section class="section bg-cream-2"><div class="container">
  {section_head("Video Logs", "Real stories, real results", "Patient journeys and DocTalks with Dr. Manoj Johar — from chest-wall correction to finger preservation.", row=True, right=btn("All Videos", "video-logs.html", "btn--outline", "video"))}
  <div class="grid grid-2 reveal-stagger">
    {video_card(root, VIDEOS[3], True)}
    <div class="grid grid-2">{"".join(video_card(root, v) for v in [VIDEOS[0], VIDEOS[2], VIDEOS[4], VIDEOS[8]])}</div>
  </div>
</div></section>

{testimonials_section(root, dark=True)}

<!-- RESOURCES + FAQ -->
<section class="section"><div class="container">
  <div class="split" style="align-items:start">
    <div class="reveal">
      {eyebrow("Patient Resources")}
      <h2 class="h2">Everything you need before your first visit</h2>
      <div class="grid grid-2 mt-4">
        <a class="card" href="first-visit.html"><span class="icon-tile">{ic("doc")}</span><h3 class="h4">First Visit Guide</h3><p>What to bring, what to expect, and how to prepare.</p></a>
        <a class="card" href="education-videos.html"><span class="icon-tile">{ic("video")}</span><h3 class="h4">Education Videos</h3><p>Understand procedures through DocTalks and explainers.</p></a>
        <a class="card" href="first-visit.html#post-op"><span class="icon-tile">{ic("shield")}</span><h3 class="h4">Post-op Instructions</h3><p>Recovery guidance to protect your result.</p></a>
        <a class="card" href="faqs.html#insurance"><span class="icon-tile">{ic("award")}</span><h3 class="h4">Insurance Info</h3><p>What is typically covered and how we help.</p></a>
      </div>
    </div>
    <div class="reveal">
      {eyebrow("Overview")}
      <h2 class="h2">Frequently asked questions</h2>
      <div class="mt-4">{faq_accordion(faq_items)}</div>
      <div class="mt-3">{link_arrow("View all FAQs", "faqs.html", "link-arrow--gold")}</div>
    </div>
  </div>
</div></section>

<!-- BLOG -->
<section class="section bg-white"><div class="container">
  {section_head("From the Blog", "Insights &amp; patient education", row=True, right=btn("Visit the Blog", "blog.html", "btn--outline"))}
  <div class="grid grid-3 reveal-stagger">{"".join(post_card(root, a) for a in arts)}</div>
</div></section>

<!-- LOCATIONS -->
<section class="section"><div class="container">
  {section_head("Practice Locations", "Consult Dr. Johar at three Max Healthcare hospitals", "Noida · Vaishali · Patparganj — with urgent and virtual appointments available.", center=True)}
  {locations_cards(root)}
</div></section>

{cta_band(root)}

<!-- NEWSLETTER -->
<section class="section section--sm bg-cream-2"><div class="container">
  <div class="split">
    <div>{eyebrow("Newsletter")}<h2 class="h3">Stay updated on the latest news, events and research in plastic surgery</h2></div>
    <form class="newsletter" novalidate><input type="email" placeholder="Your email address" aria-label="Email address" required><button class="btn btn--gold" type="submit">Subscribe</button></form>
  </div>
</div></section>
'''
    return page("Best Plastic Surgeon in Noida | Dr. Manoj K Johar — Dr. Johar's Plastic Surgery Group",
                "Dr. Manoj K Johar is a renowned plastic, aesthetic and reconstructive surgeon in Noida offering surgical and non-surgical treatments at Max Healthcare hospitals in Noida, Vaishali and Patparganj.",
                body, root)

# ------------------------------------------------------------------ ABOUT pages
def build_about():
    root = ""
    lead = TEAM[0]
    body = page_hero(root, "About Dr. Johar's Plastic Surgery Group", [("Home","index.html"),("About Us",None)],
        "A group practice led by Dr. Manoj K Johar, offering the complete spectrum of plastic, aesthetic and reconstructive surgery at Max Healthcare hospitals across Delhi-NCR.", img="consultation.jpg")
    body += f'''
<section class="section"><div class="container">
  <div class="split split--wide">
    <div class="doc-visual reveal">
      <div class="doc-visual__pattern"></div>
      <div class="doc-visual__frame"><img src="assets/img/team/dr-manoj-johar.jpg" alt="Dr. Manoj K Johar"></div>
      <div class="doc-visual__badge"><span><strong>Max</strong><span>Group Head</span></span></div>
    </div>
    <div class="reveal">
      {eyebrow("Dr. Manoj K Johar")}
      <h2 class="h2">Principal Director &amp; Group Head</h2>
      <p class="lead mt-3">{esc(lead["bio"][0])}</p>
      <p class="mt-2 muted">{esc(lead["bio"][1])}</p>
      <p class="mt-2 muted">{esc(lead["bio"][2])}</p>
      <div class="flex gap-1 wrap mt-3">{"".join(f'<span class="chip">{esc(e)}</span>' for e in lead["expertise"])}</div>
      <div class="flex gap-2 wrap mt-4">{btn("Book a Consultation","appointments.html","btn--gold","calendar")}{btn("Certifications & Awards","certifications-awards.html","btn--outline")}</div>
    </div>
  </div>
</div></section>

<section class="section bg-white"><div class="container">
  {section_head("Our Philosophy", "Refinement, not transformation", "Three principles guide every consultation, every operation and every follow-up.", center=True)}
  <div class="grid grid-3 reveal-stagger">
    <div class="card"><span class="icon-tile">{ic("heart")}</span><h3 class="h4">Listen first</h3><p>We begin by understanding what concerns you and what you hope for — then we explain what is realistic, and how.</p></div>
    <div class="card"><span class="icon-tile">{ic("shield")}</span><h3 class="h4">Safety without compromise</h3><p>Every procedure is performed in accredited Max Healthcare theatres with dedicated anaesthesia, ICU and blood-bank support.</p></div>
    <div class="card"><span class="icon-tile">{ic("sparkle")}</span><h3 class="h4">Natural, lasting results</h3><p>Our techniques favour structure over tension, so results age gracefully and never look 'done'.</p></div>
  </div>
</div></section>

<section class="section"><div class="container">
  <div class="stats reveal-stagger">
    <div class="stat"><strong>3</strong><span>Max Healthcare hospitals — Noida, Vaishali &amp; Patparganj</span></div>
    <div class="stat"><strong>35<sup>+</sup></strong><span>Surgical &amp; non-surgical treatments offered</span></div>
    <div class="stat"><strong>5</strong><span>Consultant surgeons and specialists in the group</span></div>
    <div class="stat"><strong>6</strong><span>Professional affiliations and memberships</span></div>
  </div>
</div></section>

<section class="section bg-white section--flush-top"><div class="container">
  {section_head("Our Team", "The specialists behind the group", row=True, right=btn("Full Profiles", "team.html", "btn--outline"))}
  {team_grid(root)}
</div></section>

<section class="quote-band"><div class="container reveal"><blockquote>“Whether you are seeking cosmetic surgery to enhance your appearance or reconstructive surgery to address a medical condition — you deserve honest advice, safe hands and a result that feels like you.”<cite>Dr. Manoj K Johar</cite></blockquote></div></section>
{cta_band(root)}'''
    return page("About Us | Dr. Johar's Plastic Surgery Group, Noida", "About Dr. Manoj K Johar and Dr. Johar's Plastic Surgery Group — plastic, aesthetic and reconstructive surgery at Max Healthcare, Delhi-NCR.", body, root)

def build_vision():
    root = ""
    body = page_hero(root, "Vision &amp; Mission", [("Home","index.html"),("About","about.html"),("Vision & Mission",None)],
        "What we stand for — and how we work every day to live up to it.", img="face-natural.jpg")
    body += f'''
<section class="section"><div class="container">
  <div class="grid grid-2 reveal-stagger">
    <div class="card card--dark"><span class="icon-tile">{ic("sparkle")}</span><h3 class="h3">Our Vision</h3><p>To be the most trusted centre for plastic, aesthetic and reconstructive surgery in North India — where every patient, whether seeking a cosmetic refinement or life-changing reconstruction, receives world-class care with compassion and honesty.</p></div>
    <div class="card card--gold"><span class="icon-tile">{ic("heart")}</span><h3 class="h3">Our Mission</h3><p>To deliver safe, personalised, evidence-based treatment; to train the next generation of plastic surgeons; and to make advanced reconstruction — including limb preservation and cancer reconstruction — accessible to all who need it.</p></div>
  </div>
  <div class="mt-5">
    {section_head("Our Values", "What guides us")}
    <div class="grid grid-4 reveal-stagger">
      <div class="card"><span class="icon-tile">{ic("shield")}</span><h3 class="h4">Safety</h3><p>Accredited hospitals, full anaesthesia teams and rigorous protocols — always.</p></div>
      <div class="card"><span class="icon-tile">{ic("heart")}</span><h3 class="h4">Honesty</h3><p>Realistic expectations, transparent estimates, and the courage to say 'not yet'.</p></div>
      <div class="card"><span class="icon-tile">{ic("users")}</span><h3 class="h4">Team</h3><p>A multidisciplinary group across surgery, neurosciences, oncology and rehabilitation.</p></div>
      <div class="card"><span class="icon-tile">{ic("grad")}</span><h3 class="h4">Learning</h3><p>Fellowships, observerships and continuous education keep our practice at the frontier.</p></div>
    </div>
  </div>
</div></section>
{cta_band(root)}'''
    return page("Vision & Mission | Dr. Johar's Plastic Surgery Group", "The vision, mission and values of Dr. Johar's Plastic Surgery Group.", body, root)

def build_team():
    root = ""
    body = page_hero(root, "Our Team", [("Home","index.html"),("About","about.html"),("Our Team",None)],
        "Senior consultant plastic surgeons and allied specialists working together across Max Healthcare hospitals.", img="doctor-arms-crossed.jpg")
    body += f'<section class="section"><div class="container">{team_grid(root)}</div></section>'
    profiles = ""
    for i, m in enumerate(TEAM):
        alt = i % 2 == 1
        profiles += f'''
<section id="{m["slug"]}" class="section {"bg-white" if alt else ""} section--sm"><div class="container">
  <div class="split split--wide{" split--rev" if alt else ""}" style="align-items:start">
    <div class="reveal"><div class="doc-visual__frame" style="max-width:360px"><img src="assets/img/team/{m["img"]}" alt="{esc(m["name"])}"></div></div>
    <div class="reveal">
      {eyebrow(m["role"])}
      <h2 class="h2">{esc(m["name"])}</h2>
      <p class="text-gold" style="font-weight:700;letter-spacing:.04em;margin-top:6px">{esc(m["dept"])}</p>
      {"".join(f'<p class="muted mt-2">{esc(p)}</p>' for p in m["bio"])}
      <h4 class="h4 mt-3 mb-2">Areas of expertise</h4>
      <div class="flex gap-1 wrap">{"".join(f'<span class="chip">{esc(e)}</span>' for e in m["expertise"])}</div>
      <div class="mt-4">{btn("Book with " + m["name"].split()[0] + " " + m["name"].split()[-1], "appointments.html", "btn--gold", "calendar")}</div>
    </div>
  </div>
</div></section>'''
    body += profiles + cta_band(root)
    return page("Our Team | Dr. Johar's Plastic Surgery Group", "Meet Dr. Manoj K Johar and the consultant plastic surgeons of Dr. Johar's Plastic Surgery Group.", body, root)

def build_certifications():
    root = ""
    body = page_hero(root, "Certifications &amp; Awards", [("Home","index.html"),("About","about.html"),("Certifications & Awards",None)],
        "Professional memberships, affiliations and recognitions of Dr. Manoj K Johar and the group.", img="surgeon-portrait.jpg")
    logos = "".join(f'<div class="card text-center card--flat" style="display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px;min-height:190px"><img src="assets/img/credentials/{f}" alt="{esc(n)}" style="height:70px;width:auto"><strong style="font-size:.9rem;color:var(--ink)">{esc(n)}</strong></div>' for f, n in CREDENTIALS)
    body += f'''
<section class="section"><div class="container">
  {section_head("Affiliations", "Memberships &amp; affiliations", "Dr. Johar is affiliated with the leading professional bodies in plastic and aesthetic surgery in India and internationally.")}
  <div class="grid grid-3 reveal-stagger">{logos}</div>
</div></section>
<section class="section bg-white"><div class="container">
  <div class="split">
    <div class="reveal">{eyebrow("Recognition")}<h2 class="h2">A career built on trust</h2>
      <p class="lead mt-3">Dr. Manoj K Johar is widely regarded as one of the best plastic surgeons in Noida and Delhi-NCR. As Principal Director &amp; Group Head at Max Healthcare, he leads plastic, aesthetic and reconstructive surgery across three hospitals and is a regular speaker, teacher and DocTalk host on cosmetic and reconstructive surgery.</p>
      <ul class="checklist mt-4">
        <li>Member — Association of Plastic Surgeons of India (APSI)</li>
        <li>Member — Indian Association of Aesthetic Plastic Surgeons (IAAPS)</li>
        <li>Fellow — International College of Surgeons</li>
        <li>Registered — Medical Council of India / National Medical Commission</li>
        <li>Principal Director &amp; Group Head — Max Healthcare</li>
      </ul>
    </div>
    <div class="reveal"><div class="page-hero__visual"><img src="{photo(root,'consultation.jpg')}" alt=""></div></div>
  </div>
</div></section>
{cta_band(root)}'''
    return page("Certifications & Awards | Dr. Manoj K Johar", "Professional memberships, affiliations and recognitions of Dr. Manoj K Johar.", body, root)

def build_news_events():
    root = ""
    news = news_all()[:6]
    body = page_hero(root, "News &amp; Events", [("Home","index.html"),("About","about.html"),("News & Events",None)],
        "In the news, DocTalks, camps and community events from Dr. Johar's Plastic Surgery Group.", img="reception.jpg")
    body += f'''
<section class="section"><div class="container">
  {section_head("In the News", "Latest from the world of plastic surgery", row=True, right=btn("All Healthcare News","news.html","btn--outline"))}
  <div class="grid grid-3 reveal-stagger">{"".join(post_card(root, n, "news") for n in news)}</div>
</div></section>
<section class="section bg-white"><div class="container">
  {section_head("Events & Talks", "DocTalks with Dr. Johar", "Follow our YouTube channel and social pages for upcoming talks, awareness camps and live Q&amp;A sessions.", row=True, right=btn("Follow on YouTube", SITE["social"]["youtube"], "btn--outline", "video", 'target="_blank" rel="noopener"'))}
  <div class="grid grid-2 reveal-stagger">{video_card(root, VIDEOS[0], True)}{video_card(root, VIDEOS[1], True)}</div>
</div></section>
{cta_band(root)}'''
    return page("News & Events | Dr. Johar's Plastic Surgery Group", "News, events and DocTalks from Dr. Johar's Plastic Surgery Group.", body, root)

def build_education():
    root = ""
    body = page_hero(root, "Education &amp; Training", [("Home","index.html"),("About","about.html"),("Education & Training",None)],
        "Fellowships, internships / observerships and an alumni network — training the next generation of plastic surgeons.", img="operating-room.jpg",
        actions=btn("Fellowships","#fellowships","btn--gold")+btn("Internships / Observership","#internships","btn--light-outline")+btn("Alumni","#alumni","btn--light-outline"))
    fel = "".join(f'<div class="card"><span class="icon-tile">{ic("grad")}</span><span class="chip mt-3">{esc(f["dur"])}</span><h3 class="h4">{esc(f["title"])}</h3><p>{esc(f["desc"])}</p></div>' for f in FELLOWSHIPS)
    body += f'''
<section id="fellowships" class="section"><div class="container">
  {section_head("Fellowships", "Structured fellowship programmes", "Hands-on training across aesthetic, reconstructive and microsurgical practice at Max Healthcare hospitals.")}
  <div class="grid grid-3 reveal-stagger">{fel}</div>
  <div class="callout mt-4"><strong>Eligibility:</strong> MCh / DNB (Plastic Surgery) or equivalent; overseas applicants require a temporary NMC registration. To apply, send your CV and a statement of purpose via the <a href="career.html" style="color:var(--gold);font-weight:700">Career page</a>.</div>
</div></section>
<section id="internships" class="section bg-white"><div class="container">
  <div class="split">
    <div class="reveal">{eyebrow("Internships / Observership")}<h2 class="h2">Observe. Learn. Grow.</h2>
      <p class="lead mt-3">Short observerships (2–8 weeks) are open to medical students, residents and practising surgeons who wish to observe Dr. Johar's clinical and operative practice.</p>
      <ul class="checklist mt-3"><li>Out-patient clinics, ward rounds and multidisciplinary meetings</li><li>Observation in operating theatres at Max Hospital</li><li>Case discussions and journal reviews</li><li>Certificate of observership on completion</li></ul>
      <div class="mt-4">{btn("Apply for Observership","career.html","btn--gold")}</div></div>
    <div class="reveal"><div class="page-hero__visual"><img src="{photo(root,'surgeons-operating.jpg')}" alt=""></div></div>
  </div>
</div></section>
<section id="alumni" class="section"><div class="container">
  {section_head("Alumni", "A growing network of surgeons", "Fellows and observers trained with Dr. Johar's group now practise across India and abroad. Alumni are invited to our annual meet, case-discussion forums and continuing-education sessions.", center=True)}
  <div class="grid grid-3 reveal-stagger">
    <div class="card text-center"><span class="icon-tile mx-auto">{ic("users")}</span><h3 class="h4">Alumni Network</h3><p>Stay connected with peers, share cases and collaborate on research.</p></div>
    <div class="card text-center"><span class="icon-tile mx-auto">{ic("calendar")}</span><h3 class="h4">Annual Meet</h3><p>A yearly gathering with talks, live surgery and awards.</p></div>
    <div class="card text-center"><span class="icon-tile mx-auto">{ic("mail")}</span><h3 class="h4">Get in Touch</h3><p>Alumni wishing to reconnect can write to us via the contact page.</p></div>
  </div>
</div></section>
{cta_band(root, "Interested in training with us?", "Send your CV and a short statement of purpose — we review applications throughout the year.", "consultation.jpg")}'''
    return page("Education & Training | Fellowships & Observership | Dr. Johar", "Fellowships, internships / observerships and alumni network of Dr. Johar's Plastic Surgery Group.", body, root)

# ------------------------------------------------------------------ TREATMENT hub pages
def build_treatments_hub():
    root = ""
    body = page_hero(root, "Transformative Treatments", [("Home","index.html"),("Treatments",None)],
        "Surgical and non-surgical solutions, cosmetic medicine, preventive aesthetics and age reversal — the complete spectrum under one expert team.", img="hero-main.jpg")
    cat_tiles = "".join(f'''<a class="cat-tile" href="{c["slug"]}.html"><img src="{photo(root,c["img"])}" alt="" loading="lazy"><span class="cat-tile__num">0{i+1}</span><h3>{esc(c["name"])}</h3><p>{esc(c["tag"])}</p><span class="link-arrow">Explore{ic("arrow")}</span></a>''' for i, c in enumerate(CATEGORIES))
    all_cards = "".join(tcard(root, t, i+1) for i, t in enumerate(TREATMENTS))
    body += f'''
<section class="section"><div class="container">
  {section_head("Categories", "Choose your pathway", center=True)}
  <div class="grid grid-5 reveal-stagger" style="--min:300px">{cat_tiles}</div>
</div></section>
<section class="section bg-white"><div class="container">
  <div class="section-head section-head--row"><div>{eyebrow("A – Z")}<h2 class="h2">All treatments</h2></div>
    <div class="newsletter" style="max-width:380px"><span style="display:grid;place-items:center;color:var(--gold)">{ic("search")}</span><input type="search" placeholder="Search treatments…" data-treatment-search aria-label="Search treatments"></div></div>
  <div class="grid grid-3 reveal-stagger">{all_cards}</div>
  <p class="muted text-center mt-4" data-treatment-empty style="display:none">No treatments match your search — please <a href="contact.html" style="color:var(--gold);font-weight:700">contact us</a> and we will help.</p>
</div></section>
{cta_band(root)}'''
    return page("Treatments | Surgical & Non-Surgical | Dr. Johar's Plastic Surgery Group", "Browse all surgical and non-surgical treatments offered by Dr. Manoj K Johar in Noida, Vaishali and Patparganj.", body, root)

def build_category(cat):
    root = ""
    if cat["slug"] in ("surgical-treatments", "nonsurgical-treatments"):
        items = SURG if cat["slug"] == "surgical-treatments" else NONSURG
    else:
        items = [T_BY_SLUG[s] for s in CATEGORY_TREATMENTS[cat["slug"]]]
    body = page_hero(root, cat["name"], [("Home","index.html"),("Treatments","treatments.html"),(cat["name"],None)], cat["desc"], img=cat["img"],
                     actions=btn("Book a Consultation","appointments.html","btn--gold","calendar")+btn("Ask a Question","submit-query.html","btn--light-outline","message"))
    cards = "".join(tcard(root, t, i+1) for i, t in enumerate(items))
    extra = ""
    if cat["slug"] == "cosmetic-medicine":
        extra = f'''<section class="section bg-white"><div class="container"><div class="split"><div class="reveal">{eyebrow("Approach")}<h2 class="h2">Doctor-led skin &amp; hair health</h2><p class="lead mt-3">Cosmetic medicine is where dermatology meets aesthetics. We build a prescription regimen and an in-clinic programme around your skin type, season and goals — then adjust it as your skin changes.</p><ul class="checklist mt-3"><li>Skin analysis and prescription skincare</li><li>Medical facials, peels and microdermabrasion</li><li>PRP and growth-factor therapies for skin and hair</li><li>Laser programmes for pigmentation and hair removal</li></ul></div><div class="reveal"><div class="page-hero__visual"><img src="{photo(root,'facial-brush.jpg')}" alt=""></div></div></div></div></section>'''
    elif cat["slug"] == "preventive-aesthetics":
        extra = f'''<section class="section bg-white"><div class="container"><div class="split split--rev"><div class="reveal">{eyebrow("Philosophy")}<h2 class="h2">The best treatment is the one you never need</h2><p class="lead mt-3">Small, well-timed steps in your late 20s and 30s — sun protection, collagen stimulation, skin-quality boosters and light Botox — delay the changes that later need bigger procedures.</p><ul class="checklist mt-3"><li>Daily SPF and antioxidant skincare</li><li>Collagen-stimulating RF / microneedling</li><li>'Baby' Botox for expression lines</li><li>Annual skin health review</li></ul></div><div class="reveal"><div class="page-hero__visual"><img src="{photo(root,'cream-hand.jpg')}" alt=""></div></div></div></div></section>'''
    elif cat["slug"] == "age-reversal":
        extra = f'''<section class="section bg-white"><div class="container"><div class="split"><div class="reveal">{eyebrow("Layered Approach")}<h2 class="h2">Restore what time has taken</h2><p class="lead mt-3">Ageing changes bone, fat, muscle and skin. Real rejuvenation addresses each layer — restoring volume, lifting what has descended, and resurfacing the skin — with a combination tailored to you.</p><ul class="checklist mt-3"><li>Volume: fat grafting and fillers</li><li>Lift: facelift, neck lift, brow lift, threads</li><li>Skin: lasers, peels, skin tightening</li><li>Expression: Botox</li></ul></div><div class="reveal"><div class="page-hero__visual"><img src="{photo(root,'woman-dark.jpg')}" alt=""></div></div></div></div></section>'''
    body += f'''
<section class="section"><div class="container">
  {section_head(cat["tag"], f'{cat["name"]} we offer', row=True, right=btn("All Treatments","treatments.html","btn--outline"))}
  <div class="grid grid-3 reveal-stagger">{cards}</div>
</div></section>
{extra}
{cta_band(root)}'''
    return page(f'{cat["name"]} in Noida | Dr. Manoj K Johar', cat["desc"][:155], body, root, og_img=photo(root, cat["img"]))

def build_treatment(t):
    root = "../"
    cat = CAT_BY_SLUG[CAT_MAP[t["cat"]]]
    siblings = SURG if t["cat"] == "surgical" else NONSURG
    side_links = "".join(f'<a href="{s["slug"]}.html"{" class=\"is-active\"" if s["slug"]==t["slug"] else ""}>{esc(s["menu"])}{ic("chev-right")}</a>' for s in siblings)
    facts = "".join(f'<li><span>{esc(k)}</span><strong>{esc(v)}</strong></li>' for k, v in t["facts"].items())
    benefits = "".join(f'<li>{esc(b)}</li>' for b in t["benefits"])
    cands = "".join(f'<li>{esc(c)}</li>' for c in t["candidates"])
    steps = "".join(f'<li><div><strong>{esc(a)}</strong><p>{esc(b)}</p></div></li>' for a, b in t["steps"])
    faqs = faq_accordion(t["faqs"] + [FAQS[5], FAQS[6]], open_first=True)
    # related: 3 other treatments in same category
    idx = siblings.index(t)
    rel = [siblings[(idx + k) % len(siblings)] for k in (1, 2, 3)]
    rel_cards = "".join(tcard(root, r) for r in rel)
    meta = f'<div class="page-hero__meta"><span class="chip chip--ink">{esc(cat["short"])}</span>' + "".join(f'<span class="chip" style="background:rgba(255,255,255,.08);border-color:rgba(255,255,255,.14);color:#fff">{esc(k)}: {esc(v)}</span>' for k, v in list(t["facts"].items())[:2]) + '</div>'
    body = page_hero(root, t["name"], [("Home","index.html"),("Treatments","treatments.html"),(cat["name"], cat["slug"]+".html"),(t["menu"],None)], t["tagline"], img=t["img"], meta=meta,
                     actions=btn("Book a Consultation", root+"appointments.html", "btn--gold", "calendar")+btn("Ask about this treatment", root+"submit-query.html", "btn--light-outline", "message"))
    body += f'''
<section class="section"><div class="container">
  <div class="detail">
    <div class="detail__content">
      <section class="reveal">
        {eyebrow("Overview")}
        <h2>About {esc(t["menu"])}</h2>
        <p class="lead">{esc(t["overview"][0])}</p>
        <div class="detail__img"><img src="{photo(root,t["img"])}" alt="{esc(t["name"])}"></div>
        <p>{esc(t["overview"][1])}</p>
      </section>
      <section class="reveal">
        <div class="grid grid-2">
          <div class="card card--flat"><span class="icon-tile">{ic("sparkle")}</span><h3 style="margin-top:18px">Benefits</h3><ul class="checklist mt-2">{benefits}</ul></div>
          <div class="card card--flat"><span class="icon-tile">{ic("user")}</span><h3 style="margin-top:18px">Ideal candidates</h3><ul class="checklist mt-2">{cands}</ul></div>
        </div>
      </section>
      <section class="reveal">
        {eyebrow("Your Journey")}
        <h2>What to expect</h2>
        <ol class="steps mt-3">{steps}</ol>
      </section>
      <section class="reveal">
        <div class="callout"><strong>A note from Dr. Johar:</strong> Every patient is different. The details above are a general guide — your consultation will give you a personalised plan, timeline and estimate.</div>
      </section>
      <section class="reveal">
        {eyebrow("FAQ")}
        <h2>Common questions</h2>
        <div class="mt-3">{faqs}</div>
      </section>
    </div>
    <aside class="sidebar">
      <div class="side-card side-card--dark"><h3>Book a consultation</h3><p>Speak with Dr. Johar's team about {esc(t["menu"])} — in person or online.</p>
        {btn("Book an Appointment", root+"appointments.html", "btn--gold", "calendar")}{btn("WhatsApp Us", "https://api.whatsapp.com/send?phone="+SITE["whatsapp"]+"&text="+esc(("Hello, I would like to know more about "+t["name"]+".").replace(" ", "%20")), "btn--wa", "message", 'target="_blank" rel="noopener"')}
        <a class="btn btn--light-outline" style="margin-top:10px;width:100%" href="tel:{SITE['phone1_raw']}">{ic("phone")}{SITE['phone1']}</a></div>
      <div class="side-card"><h4>At a glance</h4><ul class="facts">{facts}</ul></div>
      <div class="side-card"><h4>Your surgeon</h4><div class="side-doc"><img src="{root}assets/img/team/dr-manoj-johar.jpg" alt="Dr. Manoj K Johar"><span><strong>Dr. Manoj K Johar</strong><span>Principal Director &amp; Group Head, Max Healthcare</span></span></div><div class="mt-3">{link_arrow("View profile", root+"team.html#dr-manoj-k-johar", "link-arrow--gold")}</div></div>
      <div class="side-card"><h4>{esc(cat["name"])}</h4><div class="side-links">{side_links}</div></div>
    </aside>
  </div>
</div></section>
<section class="section bg-white section--sm"><div class="container">
  {section_head("Related", "You may also be interested in", row=True, right=btn("All "+cat["name"], root+cat["slug"]+".html", "btn--outline"))}
  <div class="grid grid-3 reveal-stagger">{rel_cards}</div>
</div></section>
{cta_band(root)}'''
    return page(f'{t["name"]} in Noida | Dr. Manoj K Johar', f'{t["name"]} by Dr. Manoj K Johar — {t["tagline"]} {t["overview"][0][:100]}', body, root, og_img=photo(root, t["img"]))

# ------------------------------------------------------------------ PATIENT GUIDE pages
def build_first_visit():
    root = ""
    body = page_hero(root, "Your First Visit", [("Home","index.html"),("Patient Guide",None),("First Visit",None)],
        "What to expect, what to bring and how to prepare — so your first consultation is relaxed and productive.", img="consultation.jpg")
    body += f'''
<section class="section"><div class="container">
  <div class="split" style="align-items:start">
    <div class="reveal">{eyebrow("Step by Step")}<h2 class="h2">How your consultation works</h2>
      <ol class="steps mt-4">
        <li><div><strong>Book</strong><p>Call, WhatsApp or book online. Choose Noida, Vaishali or Patparganj — or a virtual consultation.</p></div></li>
        <li><div><strong>Arrive &amp; register</strong><p>Please arrive 15 minutes early with your ID and any previous reports.</p></div></li>
        <li><div><strong>Consult</strong><p>Dr. Johar listens to your concerns, examines you, and discusses all suitable options — surgical and non-surgical.</p></div></li>
        <li><div><strong>Plan &amp; estimate</strong><p>You receive a personalised plan, timeline and a transparent written estimate. No pressure to decide on the day.</p></div></li>
        <li><div><strong>Prepare</strong><p>When you are ready, our coordinators arrange tests, dates and admission if needed.</p></div></li>
      </ol></div>
    <div class="reveal">
      <div class="card"><span class="icon-tile">{ic("doc")}</span><h3 class="h4">What to bring</h3><ul class="checklist mt-2"><li>Photo ID and contact details</li><li>List of current medications and allergies</li><li>Previous reports, scans or discharge summaries</li><li>Insurance details (for reconstructive procedures)</li><li>Your list of questions</li></ul></div>
      <div class="card mt-3"><span class="icon-tile">{ic("clock")}</span><h3 class="h4">Good to know</h3><ul class="checklist mt-2"><li>First consultations usually last 20–40 minutes</li><li>Come without makeup if the concern is facial skin</li><li>You are welcome to bring a family member</li><li>Clinical photographs are taken with consent and kept confidential</li></ul></div>
    </div>
  </div>
</div></section>
<section id="post-op" class="section bg-white"><div class="container">
  {section_head("After Surgery", "General post-operative instructions", "You will receive procedure-specific written instructions. These general principles apply to most patients.")}
  <div class="grid grid-3 reveal-stagger">
    <div class="card"><span class="icon-tile">{ic("shield")}</span><h3 class="h4">Wound &amp; dressing care</h3><p>Keep dressings dry and intact until your review. Do not apply creams unless advised. Report redness, discharge or increasing pain immediately.</p></div>
    <div class="card"><span class="icon-tile">{ic("heart")}</span><h3 class="h4">Activity</h3><p>Walk short distances several times a day. Avoid lifting, bending and strenuous exercise for the period advised. Do not drive while on strong painkillers.</p></div>
    <div class="card"><span class="icon-tile">{ic("leaf")}</span><h3 class="h4">Diet &amp; medication</h3><p>Eat a protein-rich diet, stay hydrated and complete all prescribed medications. No smoking or alcohol until cleared.</p></div>
    <div class="card"><span class="icon-tile">{ic("clock")}</span><h3 class="h4">Swelling &amp; bruising</h3><p>Normal for 1–3 weeks. Cold compresses in the first 48 hours and elevation help. Final results take weeks to months.</p></div>
    <div class="card"><span class="icon-tile">{ic("sparkle")}</span><h3 class="h4">Scar care</h3><p>Once healed: silicone gel/sheets, gentle massage and strict sun protection for 12 months.</p></div>
    <div class="card"><span class="icon-tile">{ic("phone")}</span><h3 class="h4">When to call us</h3><p>Fever, breathlessness, sudden one-sided swelling, bleeding or severe pain — call {SITE['phone1']} at any time.</p></div>
  </div>
</div></section>
{cta_band(root)}'''
    return page("First Visit Guide | Dr. Johar's Plastic Surgery Group", "What to expect at your first consultation with Dr. Manoj K Johar — preparation, what to bring and post-operative care.", body, root)

def build_faqs():
    root = ""
    body = page_hero(root, "Frequently Asked Questions", [("Home","index.html"),("Patient Guide",None),("FAQ's",None)],
        "Straight answers to the questions patients ask most often.", img="face-natural.jpg")
    body += f'''
<section class="section"><div class="container container--narrow">
  {section_head("General", "About plastic surgery &amp; your visit")}
  {faq_accordion(FAQS[:5])}
  <div id="insurance" class="mt-5">{section_head("Costs & Insurance", "Estimates, payment &amp; cover")}{faq_accordion(FAQS[5:] + [
      ("Do you offer EMI or payment plans?", "Yes — payment plans and EMI options through partner providers are available for many elective procedures. Please ask our coordinators."),
      ("How do I get an estimate?", "Use the 'Know Your Estimate' option on the Submit a Query page, or book a consultation for a precise, itemised estimate."),
  ], open_first=False)}</div>
  <div class="mt-5">{section_head("Safety", "Risks, anaesthesia &amp; hospitals")}{faq_accordion([
      ("Is plastic surgery safe?", "All surgery carries some risk, but in accredited hospitals with an experienced team the risk of serious complications is low. We discuss the specific risks of your procedure openly before you decide."),
      ("Where are procedures performed?", "Surgical procedures are performed at Max Healthcare hospitals in Noida, Vaishali and Patparganj, with full anaesthesia, ICU and blood-bank support. Many non-surgical treatments are performed in the clinic."),
      ("Who will do my surgery?", "Dr. Manoj K Johar leads and performs your surgery with the support of the group's consultant plastic surgeons and anaesthesia team."),
      ("Can I have a virtual consultation?", "Yes — video consultations are available for initial advice, second opinions and follow-ups, particularly for outstation and international patients."),
  ], open_first=False)}</div>
</div></section>
{cta_band(root, "Still have a question?", "Send us your query and a member of the team will get back to you — or book a consultation and ask Dr. Johar directly.", "consultation.jpg")}'''
    return page("FAQ's | Dr. Johar's Plastic Surgery Group", "Answers to frequently asked questions about plastic surgery, consultations, costs, insurance and safety.", body, root)

def build_testimonials():
    root = ""
    body = page_hero(root, "Patient Testimonials", [("Home","index.html"),("Patient Guide",None),("Testimonials",None)],
        "In their own words — what patients say about their experience with Dr. Johar and the team.", img="woman-smiling.jpg")
    body += f'''
<section class="section"><div class="container">
  <div class="flex items-center justify-between wrap gap-2 mb-4"><span class="google-badge"><span class="g">G</span><span>Rated on Google <span class="stars">★★★★★</span></span></span>{btn("Read Google Reviews", "https://www.google.com/search?q=Dr.+Manoj+K+Johar", "btn--outline btn--sm", "external", 'target="_blank" rel="noopener"')}</div>
  <div class="grid grid-2 reveal-stagger">{testimonial_cards()}</div>
</div></section>
<section class="section bg-white"><div class="container">
  <div class="grid grid-2 reveal-stagger">{video_card(root, VIDEOS[2], True)}{video_card(root, VIDEOS[8], True)}</div>
</div></section>
<section id="submit" class="section"><div class="container container--narrow">
  {section_head("Share Your Story", "Submit a testimonial", "Your experience helps others take the first step. Submissions are reviewed before publishing; you may choose to remain anonymous.")}
  <div class="form-panel"><form class="form" data-form="Testimonial Submission" novalidate>
    <div class="form-row"><div class="field"><label>Your name <em>*</em></label><input name="Name" data-label="Name" required></div><div class="field"><label>Treatment received</label><input name="Treatment" data-label="Treatment"></div></div>
    <div class="field"><label>Your testimonial <em>*</em></label><textarea name="Testimonial" data-label="Testimonial" required></textarea></div>
    <div class="field"><label>Display preference</label><div class="radio-group"><label><input type="radio" name="Display" value="Full name" checked>Show my full name</label><label><input type="radio" name="Display" value="First name only">First name only</label><label><input type="radio" name="Display" value="Anonymous">Anonymous</label></div></div>
    <div class="form__actions"><button class="btn btn--gold" type="submit">Submit via WhatsApp{ic("arrow")}</button><span class="form__note">Your message opens in WhatsApp for you to send.</span></div>
  </form><div class="form-success mt-3">Thank you! Your testimonial has been prepared in WhatsApp — please tap send.</div></div>
</div></section>'''
    return page("Patient Testimonials | Dr. Johar's Plastic Surgery Group", "Read what patients say about Dr. Manoj K Johar and Dr. Johar's Plastic Surgery Group.", body, root)

def build_video_logs():
    root = ""
    body = page_hero(root, "Video Logs", [("Home","index.html"),("Patient Guide",None),("Video Logs",None)],
        "Patient journeys, case stories and DocTalks with Dr. Manoj Johar.", img="surgeons-operating.jpg",
        actions=btn("Subscribe on YouTube", SITE["social"]["youtube"], "btn--gold", "video", 'target="_blank" rel="noopener"'))
    body += f'''
<section class="section"><div class="container">
  <div class="grid grid-2 reveal-stagger mb-4">{video_card(root, VIDEOS[3], True)}{video_card(root, VIDEOS[2], True)}</div>
  <div class="grid grid-3 reveal-stagger">{"".join(video_card(root, v) for v in VIDEOS if v not in (VIDEOS[3], VIDEOS[2]))}</div>
</div></section>
{cta_band(root)}'''
    return page("Video Logs | Dr. Johar's Plastic Surgery Group", "Watch patient stories and DocTalks from Dr. Manoj Johar.", body, root)

def build_education_videos():
    root = ""
    body = page_hero(root, "Patient Education Videos", [("Home","index.html"),("Patient Guide",None),("Education Videos",None)],
        "Understand your procedure before you decide — explainers, DocTalks and recovery guidance.", img="consultation.jpg")
    body += f'''
<section class="section"><div class="container">
  {section_head("DocTalks", "Cosmetic surgery explained")}
  <div class="grid grid-2 reveal-stagger mb-5">{video_card(root, VIDEOS[0], True)}{video_card(root, VIDEOS[1], True)}</div>
  {section_head("Case Stories", "Reconstruction in action")}
  <div class="grid grid-3 reveal-stagger">{"".join(video_card(root, v) for v in VIDEOS[3:])}</div>
  <div class="mt-4">{btn("More on YouTube", SITE["social"]["youtube"], "btn--outline", "video", 'target="_blank" rel="noopener"')}</div>
</div></section>
{cta_band(root)}'''
    return page("Patient Education Videos | Dr. Johar", "Educational videos and DocTalks on plastic and cosmetic surgery by Dr. Manoj Johar.", body, root)

def build_gallery():
    root = ""
    items = [("reception.jpg","Reception & patient lounge"),("operating-room.jpg","Modular operating theatre, Max Hospital"),("consultation.jpg","Consultation & planning"),("hospital-room.jpg","Private recovery room"),
             ("surgeons-operating.jpg","Dr. Johar's surgical team"),("facial-spa.jpg","Non-surgical treatment suite"),("facial-brush.jpg","Skin & laser care"),("hair-care.jpg","Hair restoration"),("cream-hand.jpg","Medical skincare")]
    g = "".join(f'<a href="{photo(root,f)}" data-lightbox data-caption="{esc(c)}"><img src="{photo(root,f)}" alt="{esc(c)}" loading="lazy"><span>{esc(c)}</span></a>' for f, c in items)
    body = page_hero(root, "Gallery", [("Home","index.html"),("Patient Guide",None),("Gallery",None)],
        "A look inside our clinics and hospitals. Before-and-after photographs of patients are shown during your consultation, with consent, to protect patient privacy.", img="reception.jpg")
    body += f'''
<section class="section"><div class="container"><div class="gallery reveal">{g}</div>
<div class="callout mt-4"><strong>Before &amp; after results:</strong> To respect patient confidentiality we do not publish patient photographs online. During your consultation Dr. Johar will show you results of patients with concerns similar to yours.</div></div></section>
{cta_band(root)}'''
    return page("Gallery | Dr. Johar's Plastic Surgery Group", "Gallery of Dr. Johar's Plastic Surgery Group clinics and facilities.", body, root)

def build_offers():
    root = ""
    body = page_hero(root, "Offers", [("Home","index.html"),("Patient Guide",None),("Offers",None)],
        "Current packages and seasonal offers on non-surgical treatments. Terms apply — please ask our team for details.", img="cream-hand.jpg")
    cards = "".join(f'<div class="offer"><span class="chip offer__tag">{esc(o["tag"])}</span><h3>{esc(o["title"])}</h3><p>{esc(o["desc"])}</p><small>{esc(o["note"])}</small><div class="mt-2">{btn("Enquire", "submit-query.html", "btn--outline btn--sm")}</div></div>' for o in OFFERS)
    body += f'<section class="section"><div class="container"><div class="grid grid-2 reveal-stagger">{cards}</div><p class="muted small mt-4">Offers apply to non-surgical and elective treatments only, cannot be combined, and may be withdrawn without notice. Medical suitability is always assessed first.</p></div></section>' + cta_band(root)
    return page("Offers | Dr. Johar's Plastic Surgery Group", "Current offers and packages on non-surgical aesthetic treatments.", body, root)

def build_international():
    root = ""
    body = page_hero(root, "International Patients", [("Home","index.html"),("Patient Guide",None),("International Patients",None)],
        "World-class plastic and reconstructive surgery in Delhi-NCR — with dedicated coordination for patients travelling from abroad.", img="hospital-room.jpg",
        actions=btn("Request a Virtual Consultation","virtual-appointments.html","btn--gold","video")+btn("WhatsApp Our Coordinator","https://api.whatsapp.com/send?phone="+SITE["whatsapp"],"btn--light-outline","message",'target="_blank" rel="noopener"'))
    body += f'''
<section class="section"><div class="container">
  {section_head("How it Works", "Your journey, coordinated end to end")}
  <ol class="steps reveal" style="max-width:820px">
    <li><div><strong>Share your concern</strong><p>Send photographs and reports through the Submit a Query page or WhatsApp. Dr. Johar reviews and advises on suitability.</p></div></li>
    <li><div><strong>Virtual consultation</strong><p>A video consultation to discuss options, plan, estimate and duration of stay.</p></div></li>
    <li><div><strong>Travel &amp; visa support</strong><p>We provide the medical visa invitation letter, hospital details and guidance on accommodation near Max Hospital.</p></div></li>
    <li><div><strong>Treatment</strong><p>Pre-operative tests, surgery and recovery at Max Healthcare with international-patient services and interpreter support.</p></div></li>
    <li><div><strong>Follow-up</strong><p>Reviews before you fly home and video follow-ups afterwards, with written instructions for your local doctor.</p></div></li>
  </ol>
</div></section>
<section class="section bg-white"><div class="container">
  <div class="grid grid-4 reveal-stagger">
    <div class="card"><span class="icon-tile">{ic("plane")}</span><h3 class="h4">Airport pick-up</h3><p>Coordinated transfers from Indira Gandhi International Airport.</p></div>
    <div class="card"><span class="icon-tile">{ic("hospital")}</span><h3 class="h4">JCI-standard hospitals</h3><p>Max Healthcare hospitals with international patient lounges.</p></div>
    <div class="card"><span class="icon-tile">{ic("globe")}</span><h3 class="h4">Interpreters</h3><p>Language assistance available on request.</p></div>
    <div class="card"><span class="icon-tile">{ic("video")}</span><h3 class="h4">Tele-follow-up</h3><p>Continued care by video after you return home.</p></div>
  </div>
</div></section>
{cta_band(root, "Planning treatment in India?", "Our international patient coordinator will guide you from first message to full recovery.", "reception.jpg")}'''
    return page("International Patients | Dr. Johar's Plastic Surgery Group", "Plastic and reconstructive surgery in India for international patients — virtual consultation, visa support and coordinated care.", body, root)

# ------------------------------------------------------------------ BLOG / NEWS
def article_blocks(blocks):
    out = ""
    for b in blocks:
        if "h" in b: out += f'<h2>{esc(b["h"])}</h2>'
        elif "p" in b: out += f'<p>{esc(b["p"])}</p>'
        elif "ul" in b: out += '<ul>' + "".join(f'<li>{esc(x)}</li>' for x in b["ul"]) + '</ul>'
        elif "blockquote" in b: out += f'<blockquote>{esc(b["blockquote"])}</blockquote>'
    return out

def build_blog_index(arts):
    root = ""
    body = page_hero(root, "Blog", [("Home","index.html"),("Blog",None)], "Insights, patient education and skin, hair and wellness advice from Dr. Johar's team.", img="skin-closeup.jpg")
    feat = arts[0]
    body += f'''
<section class="section"><div class="container">
  <article class="post-card post-card--row reveal mb-5"><a class="post-card__img" href="blog/{feat["slug"]}.html"><img src="{photo(root,feat["img"])}" alt=""><span class="chip post-tag">Featured</span></a>
    <div class="post-card__body" style="justify-content:center;padding:36px"><div class="post-card__meta"><span>{esc(feat["date"])}</span><i></i><span>{esc(feat["cat"])}</span></div><h3 class="h2"><a href="blog/{feat["slug"]}.html">{esc(feat["title"])}</a></h3><p class="lead">{esc(feat["excerpt"])}</p>{btn("Read article", "blog/"+feat["slug"]+".html", "btn--gold", extra='style="align-self:flex-start;margin-top:10px"')}</div></article>
  <div class="grid grid-3 reveal-stagger">{"".join(post_card(root, a) for a in arts[1:])}</div>
</div></section>
<section class="section section--sm bg-cream-2"><div class="container"><div class="split"><div>{eyebrow("Newsletter")}<h2 class="h3">Get new articles and clinic updates in your inbox</h2></div><form class="newsletter" novalidate><input type="email" placeholder="Your email address" required><button class="btn btn--gold" type="submit">Subscribe</button></form></div></div></section>'''
    return page("Blog | Dr. Johar's Plastic Surgery Group", "Articles on plastic surgery, skin, hair and wellness from Dr. Manoj K Johar's team.", body, root)

def build_article(a, prev_a, next_a, arts):
    root = "../"
    related = [x for x in arts if x["slug"] != a["slug"]][:3]
    nav = ""
    if prev_a or next_a:
        nav = '<div class="article-nav">'
        nav += f'<a href="{prev_a["slug"]}.html"><small>← Previous</small><strong>{esc(prev_a["title"])}</strong></a>' if prev_a else '<span></span>'
        nav += f'<a class="next" href="{next_a["slug"]}.html"><small>Next →</small><strong>{esc(next_a["title"])}</strong></a>' if next_a else ''
        nav += '</div>'
    body = page_hero(root, esc(a["title"]), [("Home","index.html"),("Blog","blog.html"),(a["title"][:40]+("…" if len(a["title"])>40 else ""),None)], "", img=a["img"],
                     meta=f'<div class="article__meta" style="margin-top:8px;color:var(--gold-2)"><span>{esc(a["date"])}</span><span class="dot"></span><span>{esc(a["cat"])}</span><span class="dot"></span><span>By Dr. Johar\'s Team</span></div>')
    body += f'''
<section class="section"><div class="container">
  <div class="article">
    <div class="article__hero reveal"><img src="{photo(root,a["img"])}" alt=""></div>
    <div class="article__body reveal">{article_blocks(a["blocks"])}</div>
    <div class="article__share"><span>Share</span><a href="https://www.facebook.com/sharer/sharer.php?u=" target="_blank" rel="noopener" aria-label="Share on Facebook">{ic("fb")}</a><a href="https://twitter.com/intent/tweet?text={esc(a["title"])}" target="_blank" rel="noopener" aria-label="Share on X">{ic("tw")}</a><a href="https://api.whatsapp.com/send?text={esc(a["title"])}" target="_blank" rel="noopener" aria-label="Share on WhatsApp">{ic("wa")}</a></div>
    <div class="article__author"><img src="{root}assets/img/team/dr-manoj-johar.jpg" alt="Dr. Manoj K Johar"><div><strong>Dr. Manoj K Johar</strong><p>Principal Director &amp; Group Head — Plastic, Aesthetic &amp; Reconstructive Surgery, Max Healthcare. Articles are reviewed by Dr. Johar's clinical team and are for general education only.</p></div></div>
    {nav}
  </div>
</div></section>
<section class="section bg-white section--sm"><div class="container">{section_head("Keep Reading", "Related articles", row=True, right=btn("All Articles", root+"blog.html", "btn--outline"))}<div class="grid grid-3 reveal-stagger">{"".join(post_card(root, r) for r in related)}</div></div></section>
{cta_band(root)}'''
    return page(f'{a["title"]} | Dr. Johar\'s Blog', a["excerpt"][:155], body, root, og_img=photo(root, a["img"]))

def build_news_index(news):
    root = ""
    body = page_hero(root, "Healthcare News", [("Home","index.html"),("Healthcare News",None)], "Curated news from the world of plastic and aesthetic surgery — from ASPS, Medical News Today and other trusted sources.", img="consultation.jpg")
    body += f'<section class="section"><div class="container"><div class="grid grid-3 reveal-stagger">{"".join(post_card(root, n, "news") for n in news)}</div></div></section>' + cta_band(root)
    return page("Healthcare News | Dr. Johar's Plastic Surgery Group", "Curated plastic surgery news and articles.", body, root)

def build_news_item(n, news):
    root = "../"
    related = [x for x in news if x["slug"] != n["slug"]][:3]
    body = page_hero(root, esc(n["title"]), [("Home","index.html"),("Healthcare News","news.html"),(n["title"][:40]+"…",None)], "", img=n["img"],
                     meta=f'<div class="article__meta" style="margin-top:8px;color:var(--gold-2)"><span>{esc(n["date"])}</span><span class="dot"></span><span>Source: {esc(n["source"])}</span></div>')
    body += f'''
<section class="section"><div class="container"><div class="article">
  <div class="article__hero reveal"><img src="{photo(root,n["img"])}" alt=""></div>
  <div class="article__body reveal"><p class="lead">{esc(n["excerpt"])}</p><p class="mt-3">This article was published by <strong>{esc(n["source"])}</strong>. Read the full story at the source.</p>
  <div class="mt-4">{btn("Read the full article", n["link"] or SITE["domain"], "btn--gold", "external", 'target="_blank" rel="noopener"')}</div>
  <div class="callout mt-4"><strong>Have a question about this topic?</strong> Dr. Johar and his team are happy to discuss how it applies to you. <a href="{root}submit-query.html" style="color:var(--gold);font-weight:700">Submit a query</a> or <a href="{root}appointments.html" style="color:var(--gold);font-weight:700">book a consultation</a>.</div></div>
</div></div></section>
<section class="section bg-white section--sm"><div class="container">{section_head("More News", "You may also like", row=True, right=btn("All News", root+"news.html", "btn--outline"))}<div class="grid grid-3 reveal-stagger">{"".join(post_card(root, r, "news") for r in related)}</div></div></section>
{cta_band(root)}'''
    return page(f'{n["title"]} | Healthcare News', n["excerpt"][:155], body, root, og_img=photo(root, n["img"]))

# ------------------------------------------------------------------ FORMS / CONTACT
def form_common(kind):
    tre = "".join(f'<option>{esc(t["name"])}</option>' for t in TREATMENTS)
    loc = "".join(f'<option>{esc(l["name"])}</option>' for l in LOCATIONS)
    return tre, loc

def build_appointments():
    root = ""
    tre, loc = form_common("appt")
    body = page_hero(root, "Book an Appointment", [("Home","index.html"),("Appointments",None)],
        "Choose your preferred hospital, date and time. Our team confirms your appointment by phone or WhatsApp.", img="reception.jpg")
    body += f'''
<section class="section"><div class="container">
  <div class="split" style="align-items:start;grid-template-columns:1.2fr .8fr">
    <div class="form-panel reveal"><form class="form" data-form="General Appointment Request" novalidate>
      <div class="form-row"><div class="field"><label>Full name <em>*</em></label><input name="Name" data-label="Name" required></div><div class="field"><label>Mobile number <em>*</em></label><input name="Phone" data-label="Phone" type="tel" required></div></div>
      <div class="form-row"><div class="field"><label>Email</label><input name="Email" data-label="Email" type="email"></div><div class="field"><label>Age</label><input name="Age" data-label="Age" type="number" min="0"></div></div>
      <div class="form-row"><div class="field"><label>Preferred hospital <em>*</em></label><select name="Location" data-label="Location" required><option value="">Select…</option>{loc}<option>Virtual (video) consultation</option></select></div><div class="field"><label>Treatment of interest</label><select name="Treatment" data-label="Treatment"><option value="">Not sure / General consultation</option>{tre}</select></div></div>
      <div class="form-row"><div class="field"><label>Preferred date</label><input name="Date" data-label="Preferred date" type="date"></div><div class="field"><label>Preferred time</label><select name="Time" data-label="Preferred time"><option>Morning (10 AM – 1 PM)</option><option>Afternoon (1 – 4 PM)</option><option>Evening (4 – 6 PM)</option></select></div></div>
      <div class="field"><label>Your concern</label><textarea name="Message" data-label="Message" placeholder="Briefly describe your concern…"></textarea></div>
      <div class="form__actions"><button class="btn btn--gold btn--lg" type="submit">Request Appointment{ic("arrow")}</button><span class="form__note">Your request opens in WhatsApp for you to send to our team. Alternatively call {SITE['phone1']}.</span></div>
    </form><div class="form-success mt-3">Thank you — your appointment request has been prepared. Please tap send in WhatsApp; our team will confirm shortly.</div></div>
    <div class="reveal" style="display:grid;gap:16px">
      <div class="info-block"><span class="icon-tile">{ic("phone")}</span><div><h4>Call to book</h4><a href="tel:{SITE['phone1_raw']}">{SITE['phone1']}</a><a href="tel:{SITE['phone2_raw']}" style="display:block">{SITE['phone2']}</a><small>{SITE['hours']}</small></div></div>
      <div class="info-block"><span class="icon-tile">{ic("clock")}</span><div><h4>Need to be seen urgently?</h4><a href="urgent-appointments.html">Urgent appointments →</a><small>Trauma, wounds, post-operative concerns</small></div></div>
      <div class="info-block"><span class="icon-tile">{ic("video")}</span><div><h4>Prefer online?</h4><a href="virtual-appointments.html">Virtual consultation →</a><small>Video consult from anywhere</small></div></div>
      <div class="info-block"><span class="icon-tile">{ic("globe")}</span><div><h4>Travelling from abroad?</h4><a href="international-patients.html">International patients →</a><small>Coordinated care and visa support</small></div></div>
    </div>
  </div>
</div></section>
<section class="section bg-white"><div class="container">{section_head("Locations", "Where would you like to be seen?", center=True)}{locations_cards(root)}</div></section>'''
    return page("Book an Appointment | Dr. Manoj K Johar, Noida", "Book a consultation with Dr. Manoj K Johar at Max Hospitals in Noida, Vaishali or Patparganj.", body, root)

def build_urgent():
    root = ""
    body = page_hero(root, "Urgent Appointments", [("Home","index.html"),("Appointments","appointments.html"),("Urgent Appointments",None)],
        "For injuries, wounds, infections, post-operative concerns or any situation that cannot wait — call us directly.", img="operating-room.jpg",
        actions=f'<a class="btn btn--gold btn--lg" href="tel:{SITE["phone1_raw"]}">{ic("phone")}Call {SITE["phone1"]}</a>'+btn("WhatsApp Now","https://api.whatsapp.com/send?phone="+SITE["whatsapp"]+"&text=URGENT%3A%20I%20need%20an%20urgent%20appointment.","btn--light-outline","message",'target="_blank" rel="noopener"'))
    body += f'''
<section class="section"><div class="container">
  <div class="grid grid-3 reveal-stagger">
    <div class="card"><span class="icon-tile">{ic("shield")}</span><h3 class="h4">Facial &amp; hand injuries</h3><p>Lacerations, facial fractures, finger and hand injuries — early expert repair gives the best functional and cosmetic result.</p></div>
    <div class="card"><span class="icon-tile">{ic("heart")}</span><h3 class="h4">Wounds &amp; infections</h3><p>Non-healing wounds, diabetic foot, burns and infected wounds needing urgent debridement or cover.</p></div>
    <div class="card"><span class="icon-tile">{ic("clock")}</span><h3 class="h4">Post-operative concerns</h3><p>Our own patients with fever, bleeding, sudden swelling or pain — call at any time.</p></div>
  </div>
  <div class="callout mt-4"><strong>Life-threatening emergency?</strong> Please go to the nearest Max Hospital emergency department (Noida, Vaishali or Patparganj) or call 112. Inform the emergency team that you are a patient of Dr. Johar so we can be contacted.</div>
</div></section>
<section class="section bg-white"><div class="container container--narrow">
  {section_head("Request", "Urgent appointment request")}
  <div class="form-panel"><form class="form" data-form="URGENT Appointment Request" novalidate>
    <div class="form-row"><div class="field"><label>Full name <em>*</em></label><input name="Name" data-label="Name" required></div><div class="field"><label>Mobile <em>*</em></label><input name="Phone" data-label="Phone" type="tel" required></div></div>
    <div class="field"><label>What has happened? <em>*</em></label><textarea name="Details" data-label="Details" required></textarea></div>
    <div class="field"><label>Nearest hospital</label><div class="radio-group">{"".join(f'<label><input type="radio" name="Hospital" value="{esc(l["short"])}"{" checked" if l.get("primary") else ""}>{esc(l["short"])}</label>' for l in LOCATIONS)}</div></div>
    <div class="form__actions"><button class="btn btn--gold btn--lg" type="submit">Send Urgent Request{ic("arrow")}</button></div>
  </form><div class="form-success mt-3">Your urgent request has been prepared in WhatsApp — please tap send, and call us if you do not hear back within 15 minutes.</div></div>
</div></section>'''
    return page("Urgent Appointments | Dr. Johar's Plastic Surgery Group", "Urgent plastic surgery appointments for injuries, wounds and post-operative concerns.", body, root)

def build_virtual():
    root = ""
    tre, loc = form_common("virtual")
    body = page_hero(root, "Virtual Appointments", [("Home","index.html"),("Appointments","appointments.html"),("Virtual Appointments",None)],
        "Consult Dr. Johar by video from anywhere — for initial advice, second opinions and follow-ups.", img="consultation.jpg")
    body += f'''
<section class="section"><div class="container">
  <div class="split" style="align-items:start">
    <div class="reveal">{eyebrow("How it Works")}<h2 class="h2">Expert advice, wherever you are</h2>
      <ol class="steps mt-4">
        <li><div><strong>Request a slot</strong><p>Fill in the form; our coordinator confirms a time and shares payment details.</p></div></li>
        <li><div><strong>Share photos &amp; reports</strong><p>Send clear photographs of the area of concern and any reports via WhatsApp or the Submit a Query page.</p></div></li>
        <li><div><strong>Video consultation</strong><p>15–20 minutes with Dr. Johar on a secure video link.</p></div></li>
        <li><div><strong>Written summary</strong><p>You receive a plan, prescription if appropriate, and next steps.</p></div></li>
      </ol>
      <div class="callout mt-4">Video consultations are ideal for advice and planning. A physical examination is required before any surgery.</div>
    </div>
    <div class="form-panel reveal"><form class="form" data-form="Virtual Consultation Request" novalidate>
      <div class="form-row"><div class="field"><label>Full name <em>*</em></label><input name="Name" data-label="Name" required></div><div class="field"><label>WhatsApp number <em>*</em></label><input name="Phone" data-label="Phone" type="tel" required></div></div>
      <div class="form-row"><div class="field"><label>Email</label><input name="Email" data-label="Email" type="email"></div><div class="field"><label>Country / City</label><input name="City" data-label="City"></div></div>
      <div class="field"><label>Treatment of interest</label><select name="Treatment" data-label="Treatment"><option value="">Not sure / General advice</option>{tre}</select></div>
      <div class="field"><label>Your concern <em>*</em></label><textarea name="Message" data-label="Message" required></textarea></div>
      <div class="form__actions"><button class="btn btn--gold" type="submit">Request Video Consult{ic("arrow")}</button></div>
    </form><div class="form-success mt-3">Thank you — please tap send in WhatsApp and we will confirm your slot.</div></div>
  </div>
</div></section>'''
    return page("Virtual Appointments | Video Consultation with Dr. Johar", "Book a video consultation with Dr. Manoj K Johar.", body, root)

def build_query():
    root = ""
    tre, loc = form_common("query")
    body = page_hero(root, "Submit a Query / Reports", [("Home","index.html"),("Appointments","appointments.html"),("Submit a Query",None)],
        "Ask a question, request an estimate, get a second opinion, or send your reports for review.", img="face-natural.jpg")
    body += f'''
<section class="section"><div class="container">
  <div class="split" style="align-items:start;grid-template-columns:1.2fr .8fr">
    <div class="form-panel reveal"><form class="form" data-form="Query / Reports" novalidate>
      <div class="field"><label>I would like to</label><div class="radio-group"><label><input type="radio" name="Type" value="Get information" checked>Get information</label><label><input type="radio" name="Type" value="Know my estimate">Know my estimate</label><label><input type="radio" name="Type" value="Second opinion">Second opinion</label><label><input type="radio" name="Type" value="Submit reports">Submit reports</label></div></div>
      <div class="form-row"><div class="field"><label>Full name <em>*</em></label><input name="Name" data-label="Name" required></div><div class="field"><label>Mobile / WhatsApp <em>*</em></label><input name="Phone" data-label="Phone" type="tel" required></div></div>
      <div class="form-row"><div class="field"><label>Email</label><input name="Email" data-label="Email" type="email"></div><div class="field"><label>Treatment</label><select name="Treatment" data-label="Treatment"><option value="">Select…</option>{tre}</select></div></div>
      <div class="field"><label>Your query <em>*</em></label><textarea name="Query" data-label="Query" required></textarea></div>
      <label class="file-drop"><input type="file" multiple accept="image/*,.pdf">{ic("upload")}<strong>Attach photos or reports</strong>Files are shared securely via WhatsApp after you tap send — you can attach them in the chat.</label>
      <div class="form__actions"><button class="btn btn--gold" type="submit">Send Query{ic("arrow")}</button><span class="form__note">Opens WhatsApp with your message pre-filled.</span></div>
    </form><div class="form-success mt-3">Thank you — please tap send in WhatsApp and attach any reports in the chat.</div></div>
    <div class="reveal" style="display:grid;gap:16px">
      <div class="info-block"><span class="icon-tile">{ic("doc")}</span><div><h4>Know your estimate</h4><p>Tell us the treatment and we will share an indicative range within one working day.</p></div></div>
      <div class="info-block"><span class="icon-tile">{ic("stetho")}</span><div><h4>Second opinion</h4><p>Send your diagnosis and reports; Dr. Johar will review and advise on next steps.</p></div></div>
      <div class="info-block"><span class="icon-tile">{ic("shield")}</span><div><h4>Privacy</h4><p>Reports and photographs are handled confidentially and used only for your care.</p></div></div>
    </div>
  </div>
</div></section>'''
    return page("Submit a Query / Reports | Dr. Johar's Plastic Surgery Group", "Ask a question, request an estimate or send reports to Dr. Manoj K Johar's team.", body, root)

def build_career():
    root = ""
    body = page_hero(root, "Careers", [("Home","index.html"),("Career",None)],
        "Join a group that values skill, compassion and continuous learning — clinical, nursing, coordination and training roles.", img="doctor-arms-crossed.jpg")
    body += f'''
<section class="section"><div class="container">
  <div class="grid grid-3 reveal-stagger mb-5">
    <div class="card"><span class="icon-tile">{ic("stetho")}</span><h3 class="h4">Clinical</h3><p>Consultant and fellow plastic surgeons, anaesthetists and dermatology associates.</p></div>
    <div class="card"><span class="icon-tile">{ic("users")}</span><h3 class="h4">Nursing &amp; allied</h3><p>OT and ward nurses, laser and aesthetic therapists, physiotherapists.</p></div>
    <div class="card"><span class="icon-tile">{ic("briefcase")}</span><h3 class="h4">Coordination</h3><p>Patient coordinators, international patient services and front-desk roles.</p></div>
  </div>
  <div class="container--narrow" style="margin:0 auto">
  {section_head("Apply", "Send us your application", "Also for fellowship and observership applications — see Education &amp; Training.")}
  <div class="form-panel"><form class="form" data-form="Career / Fellowship Application" novalidate>
    <div class="form-row"><div class="field"><label>Full name <em>*</em></label><input name="Name" data-label="Name" required></div><div class="field"><label>Mobile <em>*</em></label><input name="Phone" data-label="Phone" type="tel" required></div></div>
    <div class="form-row"><div class="field"><label>Email <em>*</em></label><input name="Email" data-label="Email" type="email" required></div><div class="field"><label>Applying for</label><select name="Role" data-label="Role"><option>Fellowship</option><option>Observership / Internship</option><option>Consultant / Clinical role</option><option>Nursing / Allied</option><option>Coordination / Admin</option><option>Other</option></select></div></div>
    <div class="field"><label>Qualifications &amp; experience <em>*</em></label><textarea name="Details" data-label="Details" required></textarea></div>
    <label class="file-drop"><input type="file" accept=".pdf,.doc,.docx">{ic("upload")}<strong>Attach your CV</strong>You can attach the file in WhatsApp after tapping send.</label>
    <div class="form__actions"><button class="btn btn--gold" type="submit">Submit Application{ic("arrow")}</button></div>
  </form><div class="form-success mt-3">Thank you — please tap send in WhatsApp and attach your CV in the chat.</div></div></div>
</div></section>'''
    return page("Careers | Dr. Johar's Plastic Surgery Group", "Careers, fellowships and observership applications at Dr. Johar's Plastic Surgery Group.", body, root)

def build_contact():
    root = ""
    body = page_hero(root, "Contact Us", [("Home","index.html"),("Contact Us",None)],
        "We are here to help — call, WhatsApp, write to us or visit any of our three Max Healthcare locations.", img="reception.jpg")
    maps = "".join(f'<div><h3 class="h4 mb-2">{esc(l["name"])}</h3><div class="loc-map"><iframe src="{l["embed"]}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Map — {esc(l["name"])}"></iframe></div><p class="muted small mt-2">{esc(l["address"])} · <a href="{l["map"]}" target="_blank" rel="noopener" style="color:var(--gold);font-weight:700">Directions</a></p></div>' for l in LOCATIONS)
    body += f'''
<section class="section"><div class="container">
  <div class="grid grid-4 reveal-stagger mb-5">
    <div class="info-block"><span class="icon-tile">{ic("phone")}</span><div><h4>Phone</h4><a href="tel:{SITE['phone1_raw']}">{SITE['phone1']}</a><a href="tel:{SITE['phone2_raw']}" style="display:block">{SITE['phone2']}</a></div></div>
    <div class="info-block"><span class="icon-tile">{ic("message")}</span><div><h4>WhatsApp</h4><a href="https://api.whatsapp.com/send?phone={SITE['whatsapp']}" target="_blank" rel="noopener">Chat with us</a><small>Fastest way to reach the team</small></div></div>
    <div class="info-block"><span class="icon-tile">{ic("clock")}</span><div><h4>Hours</h4><p>{SITE['hours']}</p><small>Urgent appointments outside hours</small></div></div>
    <div class="info-block"><span class="icon-tile">{ic("globe")}</span><div><h4>Social</h4><p><a href="{SITE['social']['instagram']}" target="_blank" rel="noopener">Instagram</a> · <a href="{SITE['social']['facebook']}" target="_blank" rel="noopener">Facebook</a> · <a href="{SITE['social']['youtube']}" target="_blank" rel="noopener">YouTube</a></p></div></div>
  </div>
  <div class="split" style="align-items:start;grid-template-columns:.9fr 1.1fr">
    <div class="reveal">{eyebrow("Write to us")}<h2 class="h2">Send a message</h2><p class="muted mt-2">For appointments please use the <a href="appointments.html" style="color:var(--gold);font-weight:700">booking page</a>. For everything else — feedback, tell a friend, general questions — use this form.</p>
      <div class="form-panel mt-3"><form class="form" data-form="Contact Message" novalidate>
        <div class="form-row"><div class="field"><label>Name <em>*</em></label><input name="Name" data-label="Name" required></div><div class="field"><label>Mobile <em>*</em></label><input name="Phone" data-label="Phone" type="tel" required></div></div>
        <div class="field"><label>Email</label><input name="Email" data-label="Email" type="email"></div>
        <div class="field"><label>Subject</label><select name="Subject" data-label="Subject"><option>General enquiry</option><option>Feedback</option><option>Tell a friend</option><option>Media / press</option><option>Other</option></select></div>
        <div class="field"><label>Message <em>*</em></label><textarea name="Message" data-label="Message" required></textarea></div>
        <div class="form__actions"><button class="btn btn--gold" type="submit">Send Message{ic("arrow")}</button></div>
      </form><div class="form-success mt-3">Thank you — please tap send in WhatsApp.</div></div>
    </div>
    <div class="reveal" style="display:grid;gap:28px">{maps}</div>
  </div>
</div></section>'''
    return page("Contact Us | Dr. Johar's Plastic Surgery Group, Noida", "Contact Dr. Manoj K Johar — phone, WhatsApp and Max Hospital locations in Noida, Vaishali and Patparganj.", body, root)

# ------------------------------------------------------------------ LEGAL / SITEMAP
def build_legal(kind):
    root = ""
    if kind == "disclaimer":
        title = "Disclaimer"; content = f'''
<h2>Medical information</h2><p>The content on this website is provided for general educational and informational purposes only. It is not intended to be, and should not be taken as, medical advice, diagnosis or treatment. Always seek the advice of Dr. Manoj K Johar or another qualified healthcare professional with any questions you may have regarding a medical condition or procedure.</p>
<h2>Results vary</h2><p>Descriptions of procedures, recovery times and outcomes are general in nature. Individual results vary depending on anatomy, health, lifestyle and adherence to instructions. No guarantee of a specific outcome is made or implied.</p>
<h2>Photographs</h2><p>Stock photography on this website is used for illustrative purposes and does not depict actual patients unless stated. Patient photographs are shown only during consultation, with consent.</p>
<h2>External links</h2><p>Links to third-party websites (including news sources) are provided for convenience. {esc(SITE["name"])} is not responsible for the content or privacy practices of external sites.</p>
<h2>Emergency</h2><p>If you have a medical emergency, call your local emergency number or go to the nearest hospital emergency department immediately.</p>'''
    else:
        title = "Privacy Policy"; content = f'''
<h2>Information we collect</h2><p>When you contact us through this website, by phone, WhatsApp or email, we may collect your name, contact details, and any health information you choose to share with us for the purpose of providing care and responding to your enquiry.</p>
<h2>How we use it</h2><ul><li>To respond to your enquiry and schedule appointments</li><li>To provide medical care and follow-up</li><li>To send you information you have requested, such as newsletters (you can unsubscribe at any time)</li></ul>
<h2>Confidentiality</h2><p>Your medical information is treated as confidential and handled in accordance with applicable Indian law and professional medical ethics. We do not sell your personal information.</p>
<h2>Third-party services</h2><p>This website may use analytics and embedded services (such as Google Maps and Google Fonts) which may set cookies or collect usage data under their own privacy policies. Messages sent via WhatsApp are subject to WhatsApp's terms and privacy policy.</p>
<h2>Your rights</h2><p>You may request access to, correction of, or deletion of your personal information by contacting us at {SITE["phone1"]}.</p>
<h2>Updates</h2><p>This policy may be updated from time to time. Please check this page periodically.</p>'''
    body = page_hero(root, title, [("Home","index.html"),(title,None)], "", plain=True)
    body += f'<section class="section"><div class="container"><div class="prose reveal">{content}<p class="small muted mt-4">Last updated: August 2026</p></div></div></section>'
    return page(f'{title} | {SITE["name"]}', f'{title} for {SITE["name"]} website.', body, root)

def build_sitemap(arts, news):
    root = ""
    def col(title, items):
        return f'<div><h3>{title}</h3><ul>{"".join(f"<li><a href=\"{h}\">{esc(l)}</a></li>" for l,h in items)}</ul></div>'
    main = [("Home","index.html"),("About Us","about.html"),("Vision & Mission","vision-mission.html"),("Our Team","team.html"),("Certifications & Awards","certifications-awards.html"),("News & Events","news-events.html"),("Education & Training","education-training.html"),("Contact Us","contact.html"),("Careers","career.html"),("Disclaimer","disclaimer.html"),("Privacy","privacy.html")]
    tr = [("All Treatments","treatments.html")] + [(c["name"], c["slug"]+".html") for c in CATEGORIES] + [(t["name"], f"treatments/{t['slug']}.html") for t in TREATMENTS]
    pg = [("First Visit","first-visit.html"),("FAQ's","faqs.html"),("Patient Testimonials","testimonials.html"),("Video Logs","video-logs.html"),("Education Videos","education-videos.html"),("Gallery","gallery.html"),("Offers","offers.html"),("International Patients","international-patients.html"),("Book an Appointment","appointments.html"),("Urgent Appointments","urgent-appointments.html"),("Virtual Appointments","virtual-appointments.html"),("Submit a Query","submit-query.html")]
    bl = [("Blog","blog.html")] + [(a["title"], f"blog/{a['slug']}.html") for a in arts] + [("Healthcare News","news.html")] + [(n["title"], f"news/{n['slug']}.html") for n in news]
    body = page_hero(root, "Sitemap", [("Home","index.html"),("Sitemap",None)], "", plain=True)
    body += f'<section class="section"><div class="container"><div class="sitemap-cols reveal">{col("Main", main)}{col("Treatments", tr)}{col("Patient Guide", pg)}{col("Blog & News", bl)}</div></div></section>'
    return page(f'Sitemap | {SITE["name"]}', "Sitemap", body, root)

def build_404():
    root = ""
    body = f'''<section class="section" style="min-height:60vh;display:flex;align-items:center"><div class="container text-center"><div class="eyebrow eyebrow--center">404</div><h1 class="display-2">Page not found</h1><p class="lead mt-3 maxw-sm mx-auto">The page you are looking for may have moved. Try the treatments list or head back home.</p><div class="flex gap-2 wrap mt-4" style="justify-content:center">{btn("Go Home","index.html","btn--gold")}{btn("All Treatments","treatments.html","btn--outline")}</div></div></section>'''
    return page("Page not found | " + SITE["name"], "Page not found", body, root)

# ------------------------------------------------------------------ MAIN
def write(path, content):
    full = os.path.join(ROOT_DIR, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)

def main():
    arts = blog_all()
    news = news_all()
    pages = {
        "index.html": build_home(), "about.html": build_about(), "vision-mission.html": build_vision(), "team.html": build_team(),
        "certifications-awards.html": build_certifications(), "news-events.html": build_news_events(), "education-training.html": build_education(),
        "treatments.html": build_treatments_hub(), "first-visit.html": build_first_visit(), "faqs.html": build_faqs(), "testimonials.html": build_testimonials(),
        "video-logs.html": build_video_logs(), "education-videos.html": build_education_videos(), "gallery.html": build_gallery(), "offers.html": build_offers(),
        "international-patients.html": build_international(), "blog.html": build_blog_index(arts), "news.html": build_news_index(news),
        "appointments.html": build_appointments(), "urgent-appointments.html": build_urgent(), "virtual-appointments.html": build_virtual(),
        "submit-query.html": build_query(), "career.html": build_career(), "contact.html": build_contact(),
        "disclaimer.html": build_legal("disclaimer"), "privacy.html": build_legal("privacy"), "sitemap.html": build_sitemap(arts, news), "404.html": build_404(),
    }
    for c in CATEGORIES: pages[c["slug"] + ".html"] = build_category(c)
    for t in TREATMENTS: pages[f"treatments/{t['slug']}.html"] = build_treatment(t)
    for i, a in enumerate(arts):
        pages[f"blog/{a['slug']}.html"] = build_article(a, arts[i-1] if i > 0 else None, arts[i+1] if i+1 < len(arts) else None, arts)
    for n in news: pages[f"news/{n['slug']}.html"] = build_news_item(n, news)
    for p, c in pages.items(): write(p, c)
    # sitemap.xml + robots
    urls = "".join(f"<url><loc>{SITE['domain']}/{p}</loc></url>" for p in pages if p != "404.html")
    write("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>')
    write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {SITE['domain']}/sitemap.xml\n")
    print(f"Built {len(pages)} pages.")

if __name__ == "__main__":
    main()
