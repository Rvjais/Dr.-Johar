import os

# Script to apply the comprehensive audit fixes to HTML and CSS across all folders

def update_files():
    targets = [
        '6ce732e63260f60c0203ef7caa72248ad6fedf5c',
        '6ce732e',
        'latest'
    ]

    html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>KRTAM Skin Clinic | Plastic, Reconstructive & Aesthetic Surgery by Dr. Manoj Johar</title>
<meta name="description" content="KRTAM Skin Clinic — Advanced Plastic, Reconstructive and Aesthetic Care by Dr. Manoj Johar and Team at Max Hospitals, Delhi NCR.">
<meta property="og:title" content="KRTAM Skin Clinic | Reconstruct · Restore · Redefine">
<meta property="og:description" content="Advanced Plastic, Reconstructive and Aesthetic Care by Dr. Manoj Johar and Team at Max Hospitals, Delhi NCR.">
<meta property="og:type" content="website">
<meta name="theme-color" content="#9e5145">
<link rel="icon" type="image/png" href="assets/img/mockup/krtam-logo-transparent.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;0,700;0,800;1,500;1,600;1,700&family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500;1,600;1,700&family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Great+Vibes&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/krtam-mockup.css">
</head>
<body>

<div class="scroll-progress" id="scrollProgress"></div>

<!-- ============================================
     SECTION 1: HEADER (Navbar)
     ============================================ -->
<header class="site-header" id="siteHeader">
  <div class="container site-header__inner">
    <a href="index.html" class="site-header__brand" aria-label="KRTAM Skin Clinic home">
      <img src="assets/img/mockup/krtam-logo-transparent.png" alt="KRTAM Skin Clinic" class="site-header__logo">
      <span class="site-header__tagline">RECONSTRUCT · RESTORE · REDEFINE.</span>
    </a>
    <nav class="site-header__nav" aria-label="Main navigation">
      <a href="index.html" class="is-active">Home</a>
      <a href="about.html">About</a>
      <a href="surgical-treatments.html">Reconstructive Surgery</a>
      <a href="treatments.html">Aesthetic Treatments</a>
      <a href="testimonials.html">Patient Stories</a>
      <a href="gallery.html">Gallery</a>
      <a href="contact.html">Locations</a>
      <a href="contact.html">Contact</a>
    </nav>
    <a href="appointments.html" class="site-header__cta">Book an Appointment &rarr;</a>
    <button class="hamburger" type="button" aria-label="Open menu" aria-expanded="false">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>

<!-- Mobile Drawer -->
<div class="mobile-drawer" id="mobileDrawer" aria-hidden="true">
  <div class="mobile-drawer__scrim"></div>
  <div class="mobile-drawer__panel">
    <div class="mobile-drawer__head">
      <img src="assets/img/mockup/krtam-logo-transparent.png" alt="KRTAM Skin Clinic" style="height:34px">
      <button class="mobile-drawer__close" type="button" aria-label="Close menu">&times;</button>
    </div>
    <nav class="mobile-drawer__nav">
      <a href="index.html">Home</a>
      <a href="about.html">About</a>
      <a href="surgical-treatments.html">Reconstructive Surgery</a>
      <a href="treatments.html">Aesthetic Treatments</a>
      <a href="testimonials.html">Patient Stories</a>
      <a href="gallery.html">Gallery</a>
      <a href="contact.html">Locations</a>
      <a href="contact.html">Contact</a>
      <a href="appointments.html" class="btn btn--primary" style="margin-top:20px;text-align:center;">Book an Appointment &rarr;</a>
    </nav>
  </div>
</div>

<!-- ============================================
     SECTION 2: HERO (Exact Mockup Alignment)
     ============================================ -->
<section class="hero" id="hero">
  <div class="container hero__container">
    <div class="hero__content">
      <div class="hero__tag"><span class="tag-bar"></span> SCIENCE MEETS HUMANITY</div>
      <h1 class="hero__title">
        Restoring<br>
        Confidence.<br>
        <span class="title-gold">Changing Lives.</span>
      </h1>
      <p class="hero__subtitle">Advanced Plastic, Reconstructive and Aesthetic Care by Dr. Manoj Johar and Team at Max Hospitals, Delhi NCR.</p>
      <div class="hero__buttons">
        <a href="appointments.html" class="btn btn--primary">Book a Consultation &rarr;</a>
        <a href="about.html" class="btn btn--outline">Explore Our Approach</a>
      </div>
      <div class="hero__badges">
        <div class="hero__badge">
          <div class="hero__badge-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg>
          </div>
          <span class="hero__badge-text">Compassionate<br>Care</span>
        </div>
        <div class="hero__badge">
          <div class="hero__badge-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
          </div>
          <span class="hero__badge-text">Advanced<br>Surgical Expertise</span>
        </div>
        <div class="hero__badge">
          <div class="hero__badge-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M3 21h18M3 10h18M3 7l9-4 9 4M4 10v11M20 10v11M8 14v3M12 14v3M16 14v3"/></svg>
          </div>
          <span class="hero__badge-text">At Max Hospitals<br>(Delhi/NCR)</span>
        </div>
        <div class="hero__badge">
          <div class="hero__badge-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>
          </div>
          <span class="hero__badge-text">Trusted by<br>Thousands</span>
        </div>
      </div>
    </div>
    <div class="hero__quote-box">
      <span class="hero__quote-mark">&ldquo;</span>
      <p class="hero__quote-text">Every face,<br>every form,<br>every story<br><em>matters.</em>&rdquo;</p>
      <cite class="hero__quote-author">&mdash; DR. MANOJ JOHAR</cite>
    </div>
  </div>
</section>

<!-- ============================================
     SECTION 3: PHILOSOPHY (Full Panoramic Background)
     ============================================ -->
<section class="philosophy" id="philosophy">
  <div class="container philosophy__container">
    <div class="philosophy__content">
      <div class="section-tag"><span class="tag-bar"></span> OUR PHILOSOPHY</div>
      <h2 class="philosophy__title">More Than Procedures.<br><span class="title-gold">A More Human Approach.</span></h2>
      <p class="philosophy__text">At KRTAM, we believe in combining science, surgical skill and human understanding to help you look better, feel stronger and live more confidently.</p>
      <a href="vision-mission.html" class="philosophy__link">Our Philosophy &rarr;</a>
    </div>
    <div class="vertical-text" aria-hidden="true">
      <span>FORM</span>
      <span>FUNCTION</span>
      <span>FREEDOM</span>
      <span>A BRIGHTER</span>
      <span>TOMORROW</span>
    </div>
  </div>
</section>

<!-- ============================================
     SECTION 4: SERVICES GRID
     ============================================ -->
<section class="services" id="services">
  <div class="container">
    <div class="services__header">
      <div>
        <div class="section-tag"><span class="tag-bar"></span> OUR SERVICES</div>
        <h2 class="services__title">Comprehensive Care<br><span class="title-gold">for Every Journey</span></h2>
      </div>
      <div>
        <p class="services__intro">From reconstructive procedures to advanced aesthetic treatments, we offer personalized, evidence-based solutions tailored to you.</p>
        <a href="treatments.html" class="services__link">View All Services &rarr;</a>
      </div>
    </div>
    <div class="services__grid">
      <div class="service-card">
        <img src="assets/img/mockup/service-1-facial.png" alt="Facial Rejuvenation" class="service-card__image">
        <h3 class="service-card__title">Facial<br>Rejuvenation</h3>
        <p class="service-card__tagline">Look refreshed. Be you.</p>
        <a href="treatments/face-care-rejuvenation.html" class="service-card__link">Know More &rarr;</a>
      </div>
      <div class="service-card">
        <img src="assets/img/mockup/service-2-breast.png" alt="Breast Surgery" class="service-card__image">
        <h3 class="service-card__title">Breast<br>Surgery</h3>
        <p class="service-card__tagline">Restoration and confidence.</p>
        <a href="treatments/breast-surgery.html" class="service-card__link">Know More &rarr;</a>
      </div>
      <div class="service-card">
        <img src="assets/img/mockup/service-3-body.png" alt="Body Contouring" class="service-card__image">
        <h3 class="service-card__title">Body<br>Contouring</h3>
        <p class="service-card__tagline">A stronger, more confident you.</p>
        <a href="treatments.html" class="service-card__link">Know More &rarr;</a>
      </div>
      <div class="service-card">
        <img src="assets/img/mockup/service-4-reconstructive.png" alt="Reconstructive Surgery" class="service-card__image">
        <h3 class="service-card__title">Reconstructive<br>Surgery</h3>
        <p class="service-card__tagline">Healing beyond the surface.</p>
        <a href="treatments/cancer-reconstruction-surgery.html" class="service-card__link">Know More &rarr;</a>
      </div>
      <div class="service-card">
        <img src="assets/img/mockup/service-5-male.png" alt="Male Aesthetics" class="service-card__image">
        <h3 class="service-card__title">Male<br>Aesthetics</h3>
        <p class="service-card__tagline">Subtle changes. Stronger confidence.</p>
        <a href="treatments.html" class="service-card__link">Know More &rarr;</a>
      </div>
      <div class="service-card">
        <img src="assets/img/mockup/service-6-nonsurgical.png" alt="Non-Surgical Aesthetics" class="service-card__image">
        <h3 class="service-card__title">Non-Surgical<br>Aesthetics</h3>
        <p class="service-card__tagline">Enhance. Preserve. Refresh.</p>
        <a href="nonsurgical-treatments.html" class="service-card__link">Know More &rarr;</a>
      </div>
    </div>
  </div>
</section>

<!-- ============================================
     SECTION 5: RECONSTRUCTIVE FOCUS
     ============================================ -->
<section class="reconstructive" id="reconstructive">
  <div class="container reconstructive__container">
    <div class="reconstructive__content">
      <div class="section-tag"><span class="tag-bar"></span> RECONSTRUCTIVE SURGERY</div>
      <h2 class="reconstructive__title">Restoring Function.<br><span class="title-gold"><em>Reclaiming Possibilities.</em></span></h2>
      <p class="reconstructive__text">From cancer reconstruction to trauma repair, congenital conditions to post-surgical correction — we help you regain form, function and freedom.</p>
      <a href="surgical-treatments.html" class="reconstructive__btn btn btn--primary">Explore Reconstructive Surgery &rarr;</a>
    </div>
    <div class="vertical-text" aria-hidden="true">
      <span>HEALING</span>
      <span>RESTORATION</span>
      <span>RECONSTRUCTION</span>
      <span>NEW BEGINNINGS</span>
    </div>
  </div>
</section>

<!-- ============================================
     SECTION 6: MEET THE EXPERT
     ============================================ -->
<section class="expert" id="expert">
  <div class="container expert__container">
    <div class="expert__portrait">
      <img src="assets/img/mockup/expert-dr-johar.png" alt="Dr. Manoj Johar">
      <div class="expert__badge">
        <div class="expert__badge-number">25+</div>
        <div class="expert__badge-text">Years of Clinical<br>Experience</div>
      </div>
    </div>
    <div class="expert__info">
      <div class="section-tag"><span class="tag-bar"></span> MEET THE EXPERT</div>
      <h2 class="expert__name">Dr. Manoj Johar</h2>
      <p class="expert__role">Senior Consultant &mdash; Plastic, Reconstructive & Aesthetic Surgeon</p>
      <p class="expert__bio">With over 25 years of experience, Dr. Manoj Johar is known for his surgical expertise, compassionate approach and commitment to patient-centred care. At KRTAM, he leads a multidisciplinary team dedicated to delivering safe, effective and natural-looking results.</p>
      <a href="about.html" class="btn-outline-box">Know More About Dr. Manoj Johar &rarr;</a>
      <div style="margin-top:14px;"><img src="assets/img/mockup/dr-johar-signature-transparent.png" alt="Dr. Manoj Johar signature" class="expert__signature"></div>
    </div>
    <div class="expert__quote">
      <span class="expert__quote-mark">&ldquo;</span>
      <p>Surgery gives me the opportunity not just to change appearances, but to restore what matters most &mdash; confidence, dignity and a better quality of life.</p>
      <cite class="expert__quote-author">&mdash; DR. MANOJ JOHAR</cite>
    </div>
  </div>
</section>

<!-- ============================================
     SECTION 7: STATISTICS BAR
     ============================================ -->
<section class="stats" id="stats">
  <div class="container">
    <div class="stats__grid">
      <div class="stat">
        <div class="stat__icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
        </div>
        <div class="stat__number">25+</div>
        <div class="stat__label">Years of Experience</div>
      </div>
      <div class="stat">
        <div class="stat__icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2M9 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM23 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/></svg>
        </div>
        <div class="stat__number">10,000+</div>
        <div class="stat__label">Happy Patients</div>
      </div>
      <div class="stat">
        <div class="stat__icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 4.354a4 4 0 110 15.292M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/><path d="M15 9h-3v3m0 0h3m-3 0v3"/></svg>
        </div>
        <div class="stat__number">Multidisciplinary</div>
        <div class="stat__label">Team</div>
      </div>
      <div class="stat">
        <div class="stat__icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg>
        </div>
        <div class="stat__number">Advanced Technology</div>
        <div class="stat__label">& Safe Practices</div>
      </div>
      <div class="stat">
        <div class="stat__icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/></svg>
        </div>
        <div class="stat__number">At Max Hospitals</div>
        <div class="stat__label">(Delhi NCR)</div>
      </div>
    </div>
  </div>
</section>

<!-- ============================================
     SECTION 8: TEAM
     ============================================ -->
<section class="team" id="team">
  <div class="container team__container">
    <div class="team__sidebar">
      <div class="section-tag"><span class="tag-bar"></span> A TEAM THAT CARES</div>
      <h2 class="team__title">Skilled Hands.<br><span class="title-gold">Compassionate Hearts.</span></h2>
      <p class="team__text">Our team of skilled surgeons, clinicians and support staff work together to deliver seamless, patient-first care.</p>
      <a href="team.html" class="btn-outline-box">Meet Our Team &rarr;</a>
    </div>
    <div class="team__visual">
      <img src="assets/img/mockup/team-clinic-hires.jpg" alt="KRTAM Skin Clinic Team" class="team__photo">
    </div>
    <div class="vertical-text" aria-hidden="true">
      <span>EXPERIENCE</span>
      <span>COLLABORATION</span>
      <span>COMPASSION</span>
      <span>A COMMON</span>
      <span>PURPOSE.</span>
    </div>
  </div>
</section>

<!-- ============================================
     SECTION 9: PATIENT STORIES
     ============================================ -->
<section class="stories" id="stories">
  <div class="container stories__container">
    <div class="stories__sidebar">
      <div class="section-tag"><span class="tag-bar"></span> PATIENT STORIES</div>
      <h2 class="stories__title">Real People.<br><span class="title-gold">Real Transformations.</span></h2>
      <p class="stories__text">Every patient's journey is a testament to the power of expert care and human connection.</p>
      <a href="testimonials.html" class="btn-outline-box">View All Stories &rarr;</a>
    </div>
    <div class="stories__carousel-wrap">
      <button class="stories__arrow stories__arrow--prev" aria-label="Previous story">&lsaquo;</button>
      <div class="stories__grid">
        <div class="story-card">
          <div class="story-card__thumb-wrap">
            <img src="assets/img/mockup/story-1.png" alt="Breast Reconstruction" class="story-card__image">
            <div class="story-card__play">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><polygon points="6 3 20 12 6 21 6 3"/></svg>
            </div>
          </div>
          <div class="story-card__body">
            <div class="story-card__icon">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 3"/></svg>
            </div>
            <div class="story-card__meta">
              <div class="story-card__category">Breast Reconstruction &ndash;</div>
              <div class="story-card__name">A New Beginning</div>
            </div>
          </div>
        </div>
        <div class="story-card">
          <div class="story-card__thumb-wrap">
            <img src="assets/img/mockup/story-2.png" alt="Reconstructive Surgery" class="story-card__image">
            <div class="story-card__play">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><polygon points="6 3 20 12 6 21 6 3"/></svg>
            </div>
          </div>
          <div class="story-card__body">
            <div class="story-card__icon">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="4"/></svg>
            </div>
            <div class="story-card__meta">
              <div class="story-card__category">Reconstructive Surgery &ndash;</div>
              <div class="story-card__name">Back to Life</div>
            </div>
          </div>
        </div>
        <div class="story-card">
          <div class="story-card__thumb-wrap">
            <img src="assets/img/mockup/story-3.png" alt="Patient Consultation" class="story-card__image">
            <div class="story-card__play">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><polygon points="6 3 20 12 6 21 6 3"/></svg>
            </div>
          </div>
          <div class="story-card__body">
            <div class="story-card__icon">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="4"/></svg>
            </div>
            <div class="story-card__meta">
              <div class="story-card__category">Patient Consultation &ndash;</div>
              <div class="story-card__name">Trusted Guidance</div>
            </div>
          </div>
        </div>
      </div>
      <button class="stories__arrow stories__arrow--next" aria-label="Next story">&rsaquo;</button>
    </div>
  </div>
</section>

<!-- ============================================
     SECTION 10: HOSPITAL LOCATIONS
     ============================================ -->
<section class="locations" id="locations">
  <div class="container locations__container">
    <div class="locations__sidebar">
      <div class="section-tag"><span class="tag-bar"></span> OUR LOCATIONS</div>
      <h2 class="locations__title">At Max Hospitals,<br><span class="title-gold">Across Delhi NCR</span></h2>
      <p class="locations__text">We are available at leading Max Hospitals to make world-class care accessible to you.</p>
      <a href="contact.html" class="btn-outline-box">View All Locations &rarr;</a>
    </div>
    <div class="locations__content-wrap">
      <div class="locations__grid">
        <div class="location-card">
          <div class="location-card__thumb-wrap">
            <img src="assets/img/mockup/hospital-saket.png" alt="Max Saket, Delhi" class="location-card__image">
            <div class="location-card__thumb-pin">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5a2.5 2.5 0 110-5 2.5 2.5 0 010 5z"/></svg>
            </div>
          </div>
          <div class="location-card__body">
            <div class="location-card__header">
              <div class="location-card__pin-icon">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5a2.5 2.5 0 110-5 2.5 2.5 0 010 5z"/></svg>
              </div>
              <div class="location-card__name">
                Max Super Speciality Hospital<br>Saket, Delhi
              </div>
            </div>
            <a href="https://maps.google.com/?q=Max+Super+Speciality+Hospital+Saket+Delhi" target="_blank" rel="noopener" class="location-card__link">Get Directions &rarr;</a>
          </div>
        </div>
        <div class="location-card">
          <div class="location-card__thumb-wrap">
            <img src="assets/img/mockup/hospital-noida.png" alt="Max Noida" class="location-card__image">
            <div class="location-card__thumb-pin">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5a2.5 2.5 0 110-5 2.5 2.5 0 010 5z"/></svg>
            </div>
          </div>
          <div class="location-card__body">
            <div class="location-card__header">
              <div class="location-card__pin-icon">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5a2.5 2.5 0 110-5 2.5 2.5 0 010 5z"/></svg>
              </div>
              <div class="location-card__name">
                Max Super Speciality Hospital<br>Noida
              </div>
            </div>
            <a href="https://maps.google.com/?q=Max+Super+Speciality+Hospital+Noida" target="_blank" rel="noopener" class="location-card__link">Get Directions &rarr;</a>
          </div>
        </div>
        <div class="location-card">
          <div class="location-card__thumb-wrap">
            <img src="assets/img/mockup/hospital-patparganj.png" alt="Max Patparganj, Delhi" class="location-card__image">
            <div class="location-card__thumb-pin">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5a2.5 2.5 0 110-5 2.5 2.5 0 010 5z"/></svg>
            </div>
          </div>
          <div class="location-card__body">
            <div class="location-card__header">
              <div class="location-card__pin-icon">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5a2.5 2.5 0 110-5 2.5 2.5 0 010 5z"/></svg>
              </div>
              <div class="location-card__name">
                Max Super Speciality Hospital<br>Patparganj, Delhi
              </div>
            </div>
            <a href="https://maps.google.com/?q=Max+Super+Speciality+Hospital+Patparganj+Delhi" target="_blank" rel="noopener" class="location-card__link">Get Directions &rarr;</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ============================================
     SECTION 11: DARK CTA BANNER
     ============================================ -->
<section class="cta-banner" id="ctaBanner">
  <div class="container cta-banner__container">
    <p class="cta-banner__eyebrow">CONFIDENCE LOOKS GOOD ON YOU</p>
    <h2 class="cta-banner__title"><span class="title-gold"><em>Let's Begin Your Journey</em></span></h2>
    <p class="cta-banner__text">Book a consultation with Dr. Manoj Johar and his team at KRTAM Skin Clinic. Together, we'll create a plan that's personal, precise and possible.</p>
    <div class="cta-banner__features">
      <div class="cta-banner__feature">
        <div class="cta-banner__feature-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2M9 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8z"/></svg></div>
        <span>Personalized Guidance</span>
      </div>
      <div class="cta-banner__feature">
        <div class="cta-banner__feature-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M9 5H7a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V7a2 2 0 0 0-2-2h-2M9 5a2 2 0 0 0 2 2h2a2 2 0 0 0 2-2M9 5a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2m-6 9l2 2 4-4"/></svg></div>
        <span>Clear Treatment Plans</span>
      </div>
      <div class="cta-banner__feature">
        <div class="cta-banner__feature-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg></div>
        <span>Compassionate Care</span>
      </div>
    </div>
    <a href="appointments.html" class="cta-banner__btn btn btn--primary">Book an Appointment &rarr;</a>
  </div>
  <div class="cta-banner__script" aria-hidden="true">A Brighter You</div>
</section>

<!-- ============================================
     SECTION 12: FOOTER
     ============================================ -->
<footer class="site-footer" id="footer">
  <div class="container">
    <div class="site-footer__top">
      <div class="site-footer__brand">
        <img src="assets/img/mockup/krtam-logo-transparent.png" alt="KRTAM Skin Clinic" class="site-footer__logo">
        <span class="site-footer__tagline">RECONSTRUCT · RESTORE · REDEFINE.</span>
      </div>
      <nav class="site-footer__nav" aria-label="Footer navigation">
        <a href="index.html">Home</a>
        <a href="about.html">About</a>
        <a href="surgical-treatments.html">Reconstructive Surgery</a>
        <a href="treatments.html">Aesthetic Treatments</a>
        <a href="testimonials.html">Patient Stories</a>
        <a href="gallery.html">Gallery</a>
        <a href="contact.html">Locations</a>
        <a href="contact.html">Contact</a>
      </nav>
      <div class="site-footer__social">
        <a href="https://instagram.com" target="_blank" rel="noopener" aria-label="Instagram">IG</a>
        <a href="https://facebook.com" target="_blank" rel="noopener" aria-label="Facebook">FB</a>
        <a href="https://youtube.com" target="_blank" rel="noopener" aria-label="YouTube">YT</a>
        <a href="https://linkedin.com" target="_blank" rel="noopener" aria-label="LinkedIn">IN</a>
      </div>
    </div>
    <div class="site-footer__bottom">
      <p>&copy; 2024 KRTAM Skin Clinic. All rights reserved.</p>
      <div class="site-footer__legal">
        <a href="privacy.html">Privacy Policy</a>
        <a href="disclaimer.html">Terms of Use</a>
      </div>
      <p class="site-footer__motto">Care. Science. Confidence.</p>
    </div>
  </div>
</footer>

<script>
(function() {
  const progressBar = document.getElementById('scrollProgress');
  window.addEventListener('scroll', () => {
    const s = window.scrollY;
    const d = document.documentElement.scrollHeight - window.innerHeight;
    if (progressBar) progressBar.style.width = (d > 0 ? (s / d) * 100 : 0) + '%';
  }, { passive: true });

  const header = document.getElementById('siteHeader');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) header.classList.add('is-scrolled');
    else header.classList.remove('is-scrolled');
  }, { passive: true });

  const hamburger = document.querySelector('.hamburger');
  const drawer = document.getElementById('mobileDrawer');
  const drawerClose = document.querySelector('.mobile-drawer__close');
  const drawerScrim = document.querySelector('.mobile-drawer__scrim');

  function openD() { drawer.classList.add('is-open'); }
  function closeD() { drawer.classList.remove('is-open'); }
  if (hamburger) hamburger.addEventListener('click', openD);
  if (drawerClose) drawerClose.addEventListener('click', closeD);
  if (drawerScrim) drawerScrim.addEventListener('click', closeD);
})();
</script>

<!-- GSAP & ScrollTrigger Animation Suite -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
<script src="assets/js/krtam-gsap.js"></script>

</body>
</html>
'''

    css_content = '''/* ============================================================
   KRTAM Skin Clinic — Full Mockup-Faithful Stylesheet
   ============================================================ */

:root {
  --cream: #faf6f1;
  --cream-light: #faf7f2;
  --cream-dark: #f0e8dc;
  --ink: #1c222e;
  --ink-light: #55505c;
  --gold: #9c6d48;
  --gold-dark: #795020;
  --gold-light: #b5835c;
  --warm-gray: #8a8279;
  --white: #ffffff;
  --cta-bg: #1d1813;
  --footer-bg: #f5efe9;
  --ff-serif: 'Playfair Display', 'Cormorant Garamond', Georgia, serif;
  --ff-sans: 'Plus Jakarta Sans', 'Segoe UI', sans-serif;
  --ff-script: 'Great Vibes', cursive;
  --ease: cubic-bezier(.23, 1, .32, 1);
  --ease-out: cubic-bezier(.33, 1, .68, 1);
}

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; -webkit-font-smoothing: antialiased; }
body {
  font-family: var(--ff-sans);
  background: var(--cream);
  color: var(--ink);
  line-height: 1.6;
  overflow-x: hidden;
}
img { max-width: 100%; height: auto; display: block; }
a { color: inherit; text-decoration: none; }
button { font: inherit; border: none; background: none; cursor: pointer; }
ul, ol { list-style: none; }

.container { max-width: 1240px; margin: 0 auto; padding: 0 40px; }

/* Scroll Progress Bar */
.scroll-progress {
  position: fixed; top: 0; left: 0; height: 3px; width: 0;
  background: linear-gradient(90deg, var(--gold), var(--gold-light));
  z-index: 10000; transition: width .1s linear;
  pointer-events: none;
}

/* Color utility */
.title-gold {
  color: var(--gold) !important;
  font-style: normal;
  display: inline-block;
}

/* Outline box button matching mockup */
.btn-outline-box {
  border: 1.5px solid #a8947f;
  color: #6a513d;
  background: transparent;
  padding: 8px 18px;
  border-radius: 4px;
  font-size: 0.78rem;
  font-weight: 600;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  transition: all .25s ease;
  width: fit-content;
  text-decoration: none;
}
.btn-outline-box:hover {
  background: var(--ink);
  color: var(--white);
  border-color: var(--ink);
}

/* ============================================================
   HEADER (Transparent Overlay with Underline Nav)
   ============================================================ */
.site-header {
  position: absolute; top: 0; left: 0; right: 0; z-index: 1000;
  background: transparent;
  backdrop-filter: none; -webkit-backdrop-filter: none;
  border-bottom: none;
  transition: background .4s ease, padding .3s ease, box-shadow .3s ease, backdrop-filter .4s ease;
}
.site-header.is-scrolled {
  position: fixed;
  background: rgba(250,246,241,0.95);
  backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px);
  box-shadow: 0 2px 20px rgba(0,0,0,0.06);
  border-bottom: 1px solid rgba(0,0,0,0.04);
}
.site-header__inner {
  display: flex; align-items: center; justify-content: space-between;
  padding: 18px 0; gap: 20px;
}
.site-header__brand { display: flex; align-items: center; gap: 12px; }
.site-header__logo { height: 38px; width: auto; }
.site-header__tagline {
  font-size: 0.58rem; letter-spacing: 0.2em; color: var(--warm-gray);
  text-transform: uppercase; display: block; border-left: 1px solid rgba(41,38,46,0.18);
  padding-left: 12px; margin-left: 2px;
}
.site-header__nav {
  display: flex; gap: 26px; align-items: center;
  font-size: 0.78rem; font-weight: 500; letter-spacing: 0.02em;
}
.site-header__nav a {
  color: var(--ink); transition: color .3s ease; position: relative;
  padding: 4px 0;
}
.site-header__nav a.is-active::after {
  content: ''; position: absolute; bottom: -3px; left: 0; right: 0;
  height: 2px; background: var(--gold); border-radius: 2px;
}
.site-header__nav a:hover { color: var(--gold); }
.site-header__cta {
  background: linear-gradient(135deg, #a77148, #865532);
  color: var(--white) !important;
  padding: 11px 24px; border-radius: 6px;
  font-size: 0.78rem; font-weight: 600; letter-spacing: .03em;
  display: inline-flex; align-items: center; gap: 6px;
  transition: transform .3s var(--ease), box-shadow .3s var(--ease);
  white-space: nowrap;
  box-shadow: 0 4px 14px rgba(134,85,50,0.3);
}
.site-header__cta:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(134,85,50,0.4);
}
.hamburger { display: none; flex-direction: column; gap: 5px; width: 28px; }
.hamburger span { display: block; height: 2px; background: var(--ink); border-radius: 2px; }

/* Mobile Drawer */
.mobile-drawer {
  position: fixed; inset: 0; z-index: 9999;
  pointer-events: none; opacity: 0; transition: opacity .3s ease;
}
.mobile-drawer.is-open { pointer-events: all; opacity: 1; }
.mobile-drawer__scrim { position: absolute; inset: 0; background: rgba(0,0,0,0.4); }
.mobile-drawer__panel {
  position: absolute; right: 0; top: 0; bottom: 0; width: 320px; max-width: 85vw;
  background: var(--cream-light); padding: 24px;
  transform: translateX(100%); transition: transform .4s var(--ease);
  overflow-y: auto;
}
.mobile-drawer.is-open .mobile-drawer__panel { transform: translateX(0); }
.mobile-drawer__head { display: flex; justify-content: space-between; align-items: center; margin-bottom: 32px; }
.mobile-drawer__nav { display: flex; flex-direction: column; gap: 16px; }
.mobile-drawer__nav a { font-size: 1rem; font-weight: 500; padding: 8px 0; border-bottom: 1px solid rgba(0,0,0,0.04); }

/* ============================================================
   HERO SECTION (Exact Mockup Match)
   ============================================================ */
.hero {
  position: relative;
  background-color: #faf6f1;
  background-image: url('../img/mockup/hero-bg.png');
  background-position: center center;
  background-size: cover;
  background-repeat: no-repeat;
  min-height: 720px;
  display: flex;
  align-items: center;
  padding: 110px 0 50px;
  overflow: hidden;
}
.hero__container {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  width: 100%;
  position: relative;
  z-index: 2;
}
.hero__content {
  max-width: 540px;
  padding-top: 10px;
}
.hero__tag {
  display: flex; align-items: center; gap: 8px;
  text-transform: uppercase; letter-spacing: 0.25em; font-size: 0.72rem;
  color: var(--gold); font-weight: 600; margin-bottom: 16px;
}
.tag-bar { width: 18px; height: 1.5px; background: var(--gold); display: inline-block; }
.hero__title {
  font-family: var(--ff-serif);
  font-size: clamp(3rem, 5.2vw, 4.3rem);
  font-weight: 700;
  line-height: 1.06;
  color: var(--ink);
  margin-bottom: 18px;
  letter-spacing: -0.02em;
}
.hero__subtitle {
  font-size: 0.95rem; line-height: 1.7; color: var(--ink-light);
  max-width: 460px; margin-bottom: 30px;
}
.hero__buttons { display: flex; gap: 14px; flex-wrap: wrap; margin-bottom: 32px; }
.btn { transition: transform .3s var(--ease), box-shadow .3s var(--ease); }
.btn:hover { transform: translateY(-2px); }
.btn--primary {
  background: linear-gradient(135deg, #a77148, #865532);
  color: var(--white) !important; padding: 13px 28px; border-radius: 6px;
  font-weight: 600; font-size: 0.88rem; display: inline-flex; align-items: center; gap: 8px;
  box-shadow: 0 4px 16px rgba(134,85,50,0.3);
}
.btn--outline {
  border: 1.5px solid #a8947f; color: #5a422e; padding: 13px 26px;
  border-radius: 6px; font-weight: 600; font-size: 0.88rem;
  background: rgba(255,255,255,0.4); display: inline-flex; align-items: center; gap: 8px;
}
.btn--outline:hover { background: var(--ink); color: var(--white); border-color: var(--ink); }

/* HERO BADGES (4 Columns with Dividers) */
.hero__badges {
  display: flex;
  align-items: center;
  padding-top: 24px;
  border-top: 1px solid rgba(168, 148, 127, 0.25);
  max-width: 520px;
}
.hero__badge {
  flex: 1;
  text-align: center;
  padding: 0 10px;
  position: relative;
}
.hero__badge:not(:last-child)::after {
  content: '';
  position: absolute;
  right: 0;
  top: 15%;
  height: 70%;
  width: 1px;
  background: rgba(168, 148, 127, 0.3);
}
.hero__badge-icon {
  width: 24px;
  height: 24px;
  color: var(--gold);
  margin: 0 auto 6px;
}
.hero__badge-icon svg { width: 100%; height: 100%; }
.hero__badge-text {
  font-size: 0.72rem;
  font-weight: 500;
  color: #6a6156;
  line-height: 1.25;
  display: block;
}

/* HERO QUOTE */
.hero__quote-box {
  max-width: 230px; text-align: left; padding-top: 40px; margin-right: 40px;
}
.hero__quote-mark {
  font-size: 3.5rem; color: var(--gold); line-height: 0.6; display: block;
  font-family: var(--ff-serif); margin-bottom: 12px;
}
.hero__quote-text {
  font-family: var(--ff-serif); font-style: italic; font-size: 1.25rem;
  line-height: 1.35; color: var(--ink); margin-bottom: 8px;
}
.hero__quote-author {
  font-size: 0.68rem; letter-spacing: 0.15em; text-transform: uppercase;
  color: var(--warm-gray);
}

/* ============================================================
   PHILOSOPHY SECTION
   ============================================================ */
.philosophy {
  position: relative;
  background-color: #f7efe6;
  background-image: url('../img/mockup/philosophy-bg.png');
  background-position: center right;
  background-size: cover;
  background-repeat: no-repeat;
  min-height: 520px;
  display: flex;
  align-items: center;
  padding: 80px 0;
  overflow: hidden;
}
.philosophy__container {
  display: flex; justify-content: space-between; align-items: center;
  width: 100%; position: relative; z-index: 2;
}
.philosophy__content { max-width: 480px; }
.section-tag {
  display: flex; align-items: center; gap: 8px;
  text-transform: uppercase; letter-spacing: 0.25em; font-size: 0.68rem;
  color: var(--gold); font-weight: 600; margin-bottom: 14px;
}
.philosophy__title {
  font-family: var(--ff-serif); font-size: clamp(2.1rem, 3.6vw, 2.9rem);
  font-weight: 700; line-height: 1.15; margin-bottom: 20px; letter-spacing: -0.01em;
}
.philosophy__text {
  font-size: 0.92rem; line-height: 1.8; color: var(--ink-light); margin-bottom: 24px;
}
.philosophy__link {
  color: var(--gold); font-weight: 600; font-size: 0.88rem;
  display: inline-flex; align-items: center; gap: 6px;
  border-bottom: 1.5px solid var(--gold); padding-bottom: 2px;
}
.vertical-text {
  display: flex; flex-direction: column; gap: 8px;
  writing-mode: vertical-rl;
  font-family: var(--ff-serif); font-size: 0.8rem; letter-spacing: 0.28em;
  text-transform: uppercase; color: rgba(41,38,46,0.3); line-height: 2.2;
}

/* ============================================================
   SERVICES GRID
   ============================================================ */
.services { padding: 80px 0 90px; background: var(--cream); }
.services__header {
  display: flex; justify-content: space-between; align-items: flex-end;
  margin-bottom: 40px; gap: 40px;
}
.services__title {
  font-family: var(--ff-serif); font-size: clamp(2rem, 3.2vw, 2.6rem);
  font-weight: 700; line-height: 1.15; letter-spacing: -0.01em;
}
.services__intro { max-width: 380px; font-size: 0.88rem; color: var(--ink-light); line-height: 1.7; margin-bottom: 10px; }
.services__link { color: var(--gold); font-weight: 600; font-size: 0.86rem; display: inline-flex; align-items: center; gap: 4px; }
.services__grid { display: grid; grid-template-columns: repeat(6, 1fr); gap: 18px; }
.service-card {
  background: var(--white); border-radius: 12px; padding: 14px;
  text-align: center; cursor: pointer;
  box-shadow: 0 2px 10px rgba(0,0,0,0.03);
  transition: transform .4s var(--ease), box-shadow .4s var(--ease);
}
.service-card:hover { transform: translateY(-6px); box-shadow: 0 12px 28px rgba(0,0,0,0.08); }
.service-card__image {
  width: 100%; aspect-ratio: 1/1; object-fit: cover;
  border-radius: 8px; margin-bottom: 12px;
}
.service-card__title {
  font-family: var(--ff-serif); font-size: 0.88rem; font-weight: 700;
  letter-spacing: 0.02em; text-transform: uppercase; margin-bottom: 4px; line-height: 1.25;
}
.service-card__tagline { font-size: 0.68rem; color: var(--warm-gray); font-style: italic; margin-bottom: 8px; }
.service-card__link { font-size: 0.72rem; color: var(--gold); font-weight: 600; display: inline-flex; align-items: center; gap: 4px; }

/* ============================================================
   RECONSTRUCTIVE SECTION
   ============================================================ */
.reconstructive {
  position: relative;
  background-color: #f7f1e9;
  background-image: url('../img/mockup/reconstructive-bg.png');
  background-position: center right;
  background-size: cover;
  background-repeat: no-repeat;
  min-height: 520px;
  display: flex;
  align-items: center;
  padding: 80px 0;
  overflow: hidden;
}
.reconstructive__container {
  display: flex; justify-content: space-between; align-items: center;
  width: 100%; position: relative; z-index: 2;
}
.reconstructive__content { max-width: 480px; }
.reconstructive__title {
  font-family: var(--ff-serif); font-size: clamp(2.1rem, 3.6vw, 2.9rem);
  font-weight: 700; line-height: 1.12; margin-bottom: 20px; letter-spacing: -0.01em;
}
.reconstructive__text { font-size: 0.92rem; line-height: 1.8; color: var(--ink-light); margin-bottom: 28px; }

/* ============================================================
   MEET THE EXPERT
   ============================================================ */
.expert { padding: 90px 0; background: var(--cream-light); }
.expert__container {
  display: grid; grid-template-columns: 260px 1fr 340px; gap: 36px; align-items: center;
}
.expert__portrait { position: relative; }
.expert__portrait > img { width: 100%; border-radius: 12px; }
.expert__badge {
  position: absolute; bottom: -10px; right: -10px;
  background: var(--white); padding: 10px 14px; border-radius: 8px;
  box-shadow: 0 4px 16px rgba(0,0,0,0.08); text-align: left;
}
.expert__badge-number { font-family: var(--ff-serif); font-size: 1.8rem; font-weight: 700; color: var(--gold); line-height: 1; }
.expert__badge-text { font-size: 0.6rem; color: var(--warm-gray); line-height: 1.2; margin-top: 2px; }
.expert__name { font-family: var(--ff-serif); font-size: 2.3rem; font-weight: 700; margin-bottom: 4px; letter-spacing: -0.01em; }
.expert__role { font-size: 0.85rem; color: var(--warm-gray); margin-bottom: 18px; }
.expert__bio { font-size: 0.88rem; line-height: 1.8; color: var(--ink-light); margin-bottom: 20px; }
.expert__signature { height: 38px; width: auto; margin-top: 14px; }
.expert__quote {
  background: var(--white); border-radius: 12px; padding: 28px;
  box-shadow: 0 2px 16px rgba(0,0,0,0.04); position: relative;
}
.expert__quote-mark { font-size: 3rem; color: var(--gold); line-height: 0.5; display: block; margin-bottom: 12px; }
.expert__quote p { font-family: var(--ff-serif); font-style: italic; font-size: 1.05rem; line-height: 1.5; color: var(--ink); margin-bottom: 12px; }
.expert__quote-author { font-size: 0.68rem; letter-spacing: 0.15em; text-transform: uppercase; color: var(--warm-gray); }

/* ============================================================
   STATS BAR
   ============================================================ */
.stats {
  padding: 44px 0; background: var(--cream);
  border-top: 1px solid rgba(0,0,0,0.06); border-bottom: 1px solid rgba(0,0,0,0.06);
}
.stats__grid { display: grid; grid-template-columns: repeat(5, 1fr); gap: 16px; text-align: center; }
.stat__icon { width: 30px; height: 30px; color: var(--gold); margin: 0 auto 8px; }
.stat__icon svg { width: 100%; height: 100%; }
.stat__number { font-family: var(--ff-serif); font-size: 1.55rem; font-weight: 700; color: var(--ink); margin-bottom: 2px; }
.stat__label { font-size: 0.72rem; color: var(--warm-gray); line-height: 1.4; }

/* ============================================================
   SECTION 8: TEAM
   ============================================================ */
.team { padding: 60px 0; background: var(--cream); position: relative; overflow: hidden; }
.team__container {
  display: grid; grid-template-columns: 240px 1fr 60px;
  gap: 32px; align-items: center;
}
.team__sidebar { max-width: 240px; }
.team__title {
  font-family: var(--ff-serif); font-size: 2.1rem; font-weight: 700;
  line-height: 1.12; color: var(--ink); margin-bottom: 12px; letter-spacing: -0.01em;
}
.team__text { font-size: 0.82rem; line-height: 1.65; color: var(--ink-light); margin-bottom: 20px; }
.team__visual { width: 100%; display: flex; align-items: center; justify-content: center; }
.team__photo {
  max-width: 100%; height: auto; max-height: 380px; object-fit: contain;
  border-radius: 12px; box-shadow: 0 6px 24px rgba(0,0,0,0.06); display: block;
}

/* ============================================================
   SECTION 9: PATIENT STORIES
   ============================================================ */
.stories { padding: 60px 0; background: var(--cream); }
.stories__container {
  display: grid; grid-template-columns: 240px 1fr;
  gap: 32px; align-items: center;
}
.stories__sidebar { max-width: 240px; }
.stories__title {
  font-family: var(--ff-serif); font-size: 2.1rem; font-weight: 700;
  line-height: 1.12; color: var(--ink); margin-bottom: 12px; letter-spacing: -0.01em;
}
.stories__text { font-size: 0.82rem; line-height: 1.65; color: var(--ink-light); margin-bottom: 20px; }
.stories__carousel-wrap { display: flex; align-items: center; gap: 12px; position: relative; }
.stories__arrow {
  width: 32px; height: 32px; border-radius: 50%; border: 1.5px solid #a8947f;
  display: flex; align-items: center; justify-content: center; color: #6a513d;
  background: transparent; flex-shrink: 0; font-size: 1.25rem; line-height: 1;
  padding-bottom: 2px; transition: all .25s ease; cursor: pointer;
}
.stories__arrow:hover { background: var(--ink); color: var(--white); border-color: var(--ink); }
.stories__grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; flex: 1; }
.story-card {
  background: var(--white); border-radius: 10px; overflow: hidden;
  box-shadow: 0 2px 10px rgba(0,0,0,0.04); transition: transform .35s var(--ease), box-shadow .35s var(--ease);
  cursor: pointer;
}
.story-card:hover { transform: translateY(-4px); box-shadow: 0 8px 20px rgba(0,0,0,0.08); }
.story-card__thumb-wrap { position: relative; aspect-ratio: 16/10; overflow: hidden; }
.story-card__image { width: 100%; height: 100%; object-fit: cover; transition: transform .5s var(--ease); }
.story-card:hover .story-card__image { transform: scale(1.04); }
.story-card__play {
  position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
  width: 38px; height: 38px; background: rgba(255,255,255,0.92); border-radius: 50%;
  display: flex; align-items: center; justify-content: center; color: var(--gold);
  box-shadow: 0 3px 12px rgba(0,0,0,0.18);
}
.story-card__body { padding: 12px 14px; display: flex; align-items: center; gap: 10px; }
.story-card__icon { color: var(--gold); flex-shrink: 0; }
.story-card__category { font-size: 0.72rem; color: var(--warm-gray); font-weight: 600; line-height: 1.2; }
.story-card__name { font-family: var(--ff-serif); font-size: 0.88rem; font-weight: 700; color: var(--ink); line-height: 1.2; }

/* ============================================================
   SECTION 10: HOSPITAL LOCATIONS
   ============================================================ */
.locations { padding: 60px 0; background: var(--cream); }
.locations__container {
  display: grid; grid-template-columns: 240px 1fr;
  gap: 32px; align-items: center;
}
.locations__sidebar { max-width: 240px; }
.locations__title {
  font-family: var(--ff-serif); font-size: 2.1rem; font-weight: 700;
  line-height: 1.12; color: var(--ink); margin-bottom: 12px; letter-spacing: -0.01em;
}
.locations__text { font-size: 0.82rem; line-height: 1.65; color: var(--ink-light); margin-bottom: 20px; }
.locations__content-wrap { padding-left: 44px; }
.locations__grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; }
.location-card {
  border-radius: 10px; overflow: hidden; background: var(--white);
  box-shadow: 0 2px 10px rgba(0,0,0,0.04); transition: transform .35s var(--ease), box-shadow .35s var(--ease);
}
.location-card:hover { transform: translateY(-4px); box-shadow: 0 8px 20px rgba(0,0,0,0.08); }
.location-card__thumb-wrap { position: relative; aspect-ratio: 16/10; overflow: hidden; }
.location-card__image { width: 100%; height: 100%; object-fit: cover; }
.location-card__thumb-pin { position: absolute; top: 8px; right: 8px; color: var(--gold); }
.location-card__body { padding: 12px 14px; }
.location-card__header { display: flex; align-items: flex-start; gap: 8px; margin-bottom: 8px; }
.location-card__pin-icon { color: var(--gold); flex-shrink: 0; margin-top: 1px; }
.location-card__name { font-family: var(--ff-serif); font-size: 0.86rem; font-weight: 700; color: var(--ink); line-height: 1.25; }
.location-card__link {
  color: var(--gold); font-weight: 600; font-size: 0.72rem;
  display: inline-flex; align-items: center; gap: 4px;
  text-decoration: underline; text-underline-offset: 3px;
}

/* ============================================================
   SECTION 11: DARK CTA BANNER
   ============================================================ */
.cta-banner {
  position: relative;
  background-color: #1d1813;
  background-image: url('../img/mockup/cta-bg.png');
  background-position: center center;
  background-size: cover;
  background-repeat: no-repeat;
  min-height: 440px;
  display: flex;
  align-items: center;
  padding: 80px 0;
  color: var(--white);
  text-align: center;
  overflow: hidden;
}
.cta-banner__container { position: relative; z-index: 2; max-width: 720px; margin: 0 auto; }
.cta-banner__eyebrow { text-transform: uppercase; letter-spacing: 0.25em; font-size: 0.68rem; color: rgba(255,255,255,0.6); margin-bottom: 12px; }
.cta-banner__title { font-family: var(--ff-serif); font-size: clamp(2.2rem, 3.8vw, 3rem); font-weight: 700; margin-bottom: 14px; letter-spacing: -0.01em; }
.cta-banner__text { font-size: 0.9rem; color: rgba(255,255,255,0.75); max-width: 520px; margin: 0 auto 30px; line-height: 1.7; }
.cta-banner__features { display: flex; justify-content: center; gap: 36px; margin-bottom: 32px; flex-wrap: wrap; }
.cta-banner__feature { display: flex; align-items: center; gap: 8px; font-size: 0.82rem; color: rgba(255,255,255,0.85); }
.cta-banner__feature-icon { width: 24px; height: 24px; color: var(--gold); }
.cta-banner__feature-icon svg { width: 100%; height: 100%; }
.cta-banner__btn {
  background: linear-gradient(135deg, #a77148, #865532);
  color: var(--white); padding: 13px 32px; border-radius: 6px; font-weight: 600; font-size: 0.9rem;
  display: inline-flex; align-items: center; gap: 8px; box-shadow: 0 4px 20px rgba(134,85,50,0.4);
}
.cta-banner__script {
  position: absolute; right: 60px; top: 45%; transform: translateY(-50%);
  font-family: var(--ff-script); font-size: 3rem; color: rgba(212,175,55,0.35);
  white-space: nowrap; pointer-events: none;
}

/* ============================================================
   SECTION 12: FOOTER
   ============================================================ */
.site-footer { padding: 48px 0 24px; background: var(--footer-bg); }
.site-footer__top {
  display: flex; justify-content: space-between; align-items: center;
  padding-bottom: 24px; border-bottom: 1px solid rgba(0,0,0,0.06); margin-bottom: 20px; gap: 24px;
}
.site-footer__brand { display: flex; align-items: center; gap: 12px; }
.site-footer__logo { height: 36px; width: auto; }
.site-footer__tagline { font-size: 0.58rem; letter-spacing: 0.18em; text-transform: uppercase; color: var(--warm-gray); border-left: 1px solid rgba(0,0,0,0.1); padding-left: 12px; }
.site-footer__nav { display: flex; gap: 24px; font-size: 0.8rem; flex-wrap: wrap; }
.site-footer__nav a:hover { color: var(--gold); }
.site-footer__social { display: flex; gap: 12px; }
.site-footer__social a {
  width: 34px; height: 34px; border-radius: 50%; border: 1px solid rgba(0,0,0,0.1);
  display: flex; align-items: center; justify-content: center; color: var(--ink); transition: all .3s;
}
.site-footer__social a:hover { background: var(--gold); color: var(--white); border-color: var(--gold); }
.site-footer__bottom { display: flex; justify-content: space-between; align-items: center; font-size: 0.72rem; color: var(--warm-gray); gap: 16px; }
.site-footer__legal { display: flex; gap: 20px; }
.site-footer__legal a:hover { color: var(--gold); }
.site-footer__motto { font-style: italic; }

/* Responsive */
@media (max-width: 1024px) {
  .services__grid { grid-template-columns: repeat(3, 1fr); }
  .expert__container { grid-template-columns: 1fr; }
  .team__container { grid-template-columns: 1fr; }
  .vertical-text { display: none; }
}
@media (max-width: 768px) {
  .site-header__nav { display: none; }
  .hamburger { display: flex; }
  .site-header__cta { display: none; }
  .hero__container { flex-direction: column; }
  .hero__quote-box { margin-right: 0; padding-top: 20px; }
  .hero__badges { flex-wrap: wrap; gap: 12px; }
  .hero__badge:not(:last-child)::after { display: none; }
  .philosophy__container, .reconstructive__container { flex-direction: column; }
  .stories__container, .locations__container { grid-template-columns: 1fr; }
  .locations__content-wrap { padding-left: 0; }
  .services__grid { grid-template-columns: repeat(2, 1fr); }
  .stats__grid { grid-template-columns: repeat(2, 1fr); }
  .stories__grid { grid-template-columns: 1fr; }
  .locations__grid { grid-template-columns: 1fr; }
  .cta-banner__script { display: none; }
  .site-footer__top { flex-direction: column; text-align: center; }
  .site-footer__bottom { flex-direction: column; text-align: center; }
}
'''

    for t in targets:
        html_file = os.path.join(t, 'index.html')
        css_file = os.path.join(t, 'assets', 'css', 'krtam-mockup.css')

        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        with open(css_file, 'w', encoding='utf-8') as f:
            f.write(css_content)
        print(f'Fully audited and updated {t}')

update_files()
print('ALL TARGETS UPDATED SUCCESSFULLY!')

