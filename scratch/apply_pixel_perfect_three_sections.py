import os

html_replacement = '''<!-- ============================================
     SECTION 8: TEAM
     ============================================ -->
<section class="team" id="team">
  <div class="container team__container">
    <div class="team__sidebar">
      <div class="section-tag"><span class="tag-bar"></span> A TEAM THAT CARES</div>
      <h2 class="team__title">Skilled Hands.<br>Compassionate Hearts.</h2>
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
      <h2 class="stories__title">Real People.<br>Real Transformations.</h2>
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
      <h2 class="locations__title">At Max Hospitals,<br>Across Delhi NCR</h2>
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
'''

css_replacement = '''/* ============================================================
   PIXEL-PERFECT SECTIONS: TEAM, STORIES, LOCATIONS (Exact Mockup Match)
   ============================================================ */

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

/* --- SECTION 8: TEAM --- */
.team {
  padding: 60px 0;
  background: var(--cream);
  position: relative;
  overflow: hidden;
}
.team__container {
  display: grid;
  grid-template-columns: 240px 1fr 60px;
  gap: 32px;
  align-items: center;
}
.team__sidebar {
  max-width: 240px;
}
.team__title {
  font-family: var(--ff-serif);
  font-size: 2.1rem;
  font-weight: 700;
  line-height: 1.12;
  color: var(--ink);
  margin-bottom: 12px;
}
.team__text {
  font-size: 0.82rem;
  line-height: 1.65;
  color: var(--ink-light);
  margin-bottom: 20px;
}
.team__visual {
  width: 100%;
}
.team__photo {
  width: 100%;
  height: 240px;
  object-fit: cover;
  border-radius: 10px;
  box-shadow: 0 4px 16px rgba(0,0,0,0.05);
  display: block;
}

/* --- SECTION 9: PATIENT STORIES --- */
.stories {
  padding: 60px 0;
  background: var(--cream);
}
.stories__container {
  display: grid;
  grid-template-columns: 240px 1fr;
  gap: 32px;
  align-items: center;
}
.stories__sidebar {
  max-width: 240px;
}
.stories__title {
  font-family: var(--ff-serif);
  font-size: 2.1rem;
  font-weight: 700;
  line-height: 1.12;
  color: var(--ink);
  margin-bottom: 12px;
}
.stories__text {
  font-size: 0.82rem;
  line-height: 1.65;
  color: var(--ink-light);
  margin-bottom: 20px;
}
.stories__carousel-wrap {
  display: flex;
  align-items: center;
  gap: 12px;
  position: relative;
}
.stories__arrow {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  border: 1.5px solid #a8947f;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #6a513d;
  background: transparent;
  flex-shrink: 0;
  font-size: 1.25rem;
  line-height: 1;
  padding-bottom: 2px;
  transition: all .25s ease;
  cursor: pointer;
}
.stories__arrow:hover {
  background: var(--ink);
  color: var(--white);
  border-color: var(--ink);
}
.stories__grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
  flex: 1;
}
.story-card {
  background: var(--white);
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 2px 10px rgba(0,0,0,0.04);
  transition: transform .35s var(--ease), box-shadow .35s var(--ease);
  cursor: pointer;
}
.story-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 20px rgba(0,0,0,0.08);
}
.story-card__thumb-wrap {
  position: relative;
  aspect-ratio: 16/10;
  overflow: hidden;
}
.story-card__image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform .5s var(--ease);
}
.story-card:hover .story-card__image {
  transform: scale(1.04);
}
.story-card__play {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 38px;
  height: 38px;
  background: rgba(255,255,255,0.92);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--gold);
  box-shadow: 0 3px 12px rgba(0,0,0,0.18);
}
.story-card__body {
  padding: 12px 14px;
  display: flex;
  align-items: center;
  gap: 10px;
}
.story-card__icon {
  color: var(--gold);
  flex-shrink: 0;
}
.story-card__category {
  font-size: 0.72rem;
  color: var(--warm-gray);
  font-weight: 600;
  line-height: 1.2;
}
.story-card__name {
  font-family: var(--ff-serif);
  font-size: 0.88rem;
  font-weight: 700;
  color: var(--ink);
  line-height: 1.2;
}

/* --- SECTION 10: HOSPITAL LOCATIONS --- */
.locations {
  padding: 60px 0;
  background: var(--cream);
}
.locations__container {
  display: grid;
  grid-template-columns: 240px 1fr;
  gap: 32px;
  align-items: center;
}
.locations__sidebar {
  max-width: 240px;
}
.locations__title {
  font-family: var(--ff-serif);
  font-size: 2.1rem;
  font-weight: 700;
  line-height: 1.12;
  color: var(--ink);
  margin-bottom: 12px;
}
.locations__text {
  font-size: 0.82rem;
  line-height: 1.65;
  color: var(--ink-light);
  margin-bottom: 20px;
}
.locations__content-wrap {
  padding-left: 44px; /* Align precisely with the 3 stories cards */
}
.locations__grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
}
.location-card {
  border-radius: 10px;
  overflow: hidden;
  background: var(--white);
  box-shadow: 0 2px 10px rgba(0,0,0,0.04);
  transition: transform .35s var(--ease), box-shadow .35s var(--ease);
}
.location-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 20px rgba(0,0,0,0.08);
}
.location-card__thumb-wrap {
  position: relative;
  aspect-ratio: 16/10;
  overflow: hidden;
}
.location-card__image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.location-card__thumb-pin {
  position: absolute;
  top: 8px;
  right: 8px;
  color: var(--gold);
}
.location-card__body {
  padding: 12px 14px;
}
.location-card__header {
  display: flex;
  align-items: flex-start;
  gap: 8px;
  margin-bottom: 8px;
}
.location-card__pin-icon {
  color: var(--gold);
  flex-shrink: 0;
  margin-top: 1px;
}
.location-card__name {
  font-family: var(--ff-serif);
  font-size: 0.86rem;
  font-weight: 700;
  color: var(--ink);
  line-height: 1.25;
}
.location-card__link {
  color: var(--gold);
  font-weight: 600;
  font-size: 0.72rem;
  display: inline-flex;
  align-items: center;
  gap: 4px;
  text-decoration: underline;
  text-underline-offset: 3px;
}
'''

targets = [
    '6ce732e63260f60c0203ef7caa72248ad6fedf5c',
    '6ce732e',
    'latest'
]

for t in targets:
    html_file = os.path.join(t, 'index.html')
    css_file = os.path.join(t, 'assets', 'css', 'krtam-mockup.css')

    # 1. HTML
    with open(html_file, 'r', encoding='utf-8') as f:
        html = f.read()

    old_team = html.find('<!-- ============================================\n     SECTION 8: TEAM')
    old_cta = html.find('<!-- ============================================\n     SECTION 11: DARK CTA BANNER')
    if old_team != -1 and old_cta != -1:
        html = html[:old_team] + html_replacement + html[old_cta:]
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'HTML updated in {html_file}')

    # 2. CSS
    with open(css_file, 'r', encoding='utf-8') as f:
        css = f.read()

    css_start = css.find('/* ============================================================\n   SHARED SIDEBAR + CARDS')
    if css_start == -1:
        css_start = css.find('/* ============================================================\n   PIXEL-PERFECT SECTIONS')
    if css_start == -1:
        css_start = css.find('/* TEAM */')
    css_end = css.find('/* ============================================================\n   DARK CTA BANNER')

    if css_start != -1 and css_end != -1:
        css = css[:css_start] + css_replacement + '\n' + css[css_end:]
        with open(css_file, 'w', encoding='utf-8') as f:
            f.write(css)
        print(f'CSS updated in {css_file}')

print('ALL DONE!')

