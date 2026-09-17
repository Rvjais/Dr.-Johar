import os

# Write a script to update index.html and krtam-mockup.css in all targets

def update_all():
    targets = [
        '6ce732e63260f60c0203ef7caa72248ad6fedf5c',
        '6ce732e',
        'latest'
    ]

    for t in targets:
        html_file = os.path.join(t, 'index.html')
        css_file = os.path.join(t, 'assets', 'css', 'krtam-mockup.css')

        # 1. Update HTML
        with open(html_file, 'r', encoding='utf-8') as f:
            html = f.read()

        # Update Team Section HTML
        old_team_start = html.find('<!-- ============================================\n     SECTION 8: TEAM')
        old_stories_start = html.find('<!-- ============================================\n     SECTION 9: PATIENT STORIES')
        old_locations_start = html.find('<!-- ============================================\n     SECTION 10: HOSPITAL LOCATIONS')
        old_cta_start = html.find('<!-- ============================================\n     SECTION 11: DARK CTA BANNER')

        if old_team_start != -1 and old_stories_start != -1 and old_locations_start != -1 and old_cta_start != -1:
            new_sections = '''<!-- ============================================
     SECTION 8: TEAM
     ============================================ -->
<section class="team" id="team">
  <div class="container team__container">
    <div class="team__sidebar">
      <div class="section-tag"><span class="tag-bar"></span> A TEAM THAT CARES</div>
      <h2 class="team__title">Skilled Hands.<br>Compassionate Hearts.</h2>
      <p class="team__text">Our team of skilled surgeons, clinicians and support staff work together to deliver seamless, patient-first care.</p>
      <a href="team.html" class="team__link btn-outline-pill">Meet Our Team &rarr;</a>
    </div>
    <div class="team__visual">
      <img src="assets/img/mockup/team-clinic-hires.jpg" alt="KRTAM Skin Clinic Team">
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
      <a href="testimonials.html" class="stories__link btn-outline-pill">View All Stories &rarr;</a>
    </div>
    <div class="stories__content-wrap">
      <button class="stories__arrow stories__arrow--prev" aria-label="Previous">&larr;</button>
      <div class="stories__grid">
        <div class="story-card">
          <div class="story-card__thumb-wrap">
            <img src="assets/img/mockup/story-1.png" alt="Breast Reconstruction" class="story-card__image">
            <div class="story-card__play"><svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><polygon points="5 3 19 12 5 21 5 3"/></svg></div>
          </div>
          <div class="story-card__body">
            <div class="story-card__badge-row">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg>
              <span>Breast Reconstruction</span>
            </div>
            <h3 class="story-card__title">A New Beginning</h3>
          </div>
        </div>
        <div class="story-card">
          <div class="story-card__thumb-wrap">
            <img src="assets/img/mockup/story-2.png" alt="Reconstructive Surgery" class="story-card__image">
            <div class="story-card__play"><svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><polygon points="5 3 19 12 5 21 5 3"/></svg></div>
          </div>
          <div class="story-card__body">
            <div class="story-card__badge-row">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="4"/></svg>
              <span>Reconstructive Surgery</span>
            </div>
            <h3 class="story-card__title">Back to Life</h3>
          </div>
        </div>
        <div class="story-card">
          <div class="story-card__thumb-wrap">
            <img src="assets/img/mockup/story-3.png" alt="Patient Consultation" class="story-card__image">
            <div class="story-card__play"><svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><polygon points="5 3 19 12 5 21 5 3"/></svg></div>
          </div>
          <div class="story-card__body">
            <div class="story-card__badge-row">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
              <span>Patient Consultation</span>
            </div>
            <h3 class="story-card__title">Trusted Guidance</h3>
          </div>
        </div>
      </div>
      <button class="stories__arrow stories__arrow--next" aria-label="Next">&rarr;</button>
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
      <p class="locations__text">We're available at leading Max Hospitals to make world-class care accessible to you.</p>
      <a href="contact.html" class="locations__link btn-outline-pill">View All Locations &rarr;</a>
    </div>
    <div class="locations__grid">
      <div class="location-card">
        <div class="location-card__image-wrap">
          <img src="assets/img/mockup/hospital-saket.png" alt="Max Saket" class="location-card__image">
          <div class="location-card__pin"><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5a2.5 2.5 0 110-5 2.5 2.5 0 010 5z"/></svg></div>
        </div>
        <div class="location-card__body">
          <h3 class="location-card__name">Max Super Speciality Hospital<br>Saket, Delhi</h3>
          <a href="https://maps.google.com" target="_blank" rel="noopener" class="location-card__link">Get Directions &rarr;</a>
        </div>
      </div>
      <div class="location-card">
        <div class="location-card__image-wrap">
          <img src="assets/img/mockup/hospital-noida.png" alt="Max Noida" class="location-card__image">
          <div class="location-card__pin"><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5a2.5 2.5 0 110-5 2.5 2.5 0 010 5z"/></svg></div>
        </div>
        <div class="location-card__body">
          <h3 class="location-card__name">Max Super Speciality Hospital<br>Noida</h3>
          <a href="https://maps.google.com" target="_blank" rel="noopener" class="location-card__link">Get Directions &rarr;</a>
        </div>
      </div>
      <div class="location-card">
        <div class="location-card__image-wrap">
          <img src="assets/img/mockup/hospital-patparganj.png" alt="Max Patparganj" class="location-card__image">
          <div class="location-card__pin"><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5a2.5 2.5 0 110-5 2.5 2.5 0 010 5z"/></svg></div>
        </div>
        <div class="location-card__body">
          <h3 class="location-card__name">Max Super Speciality Hospital<br>Patparganj, Delhi</h3>
          <a href="https://maps.google.com" target="_blank" rel="noopener" class="location-card__link">Get Directions &rarr;</a>
        </div>
      </div>
    </div>
  </div>
</section>
'''
            html = html[:old_team_start] + new_sections + html[old_cta_start:]
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f'Updated HTML sections in {html_file}')

        # 2. Update CSS
        with open(css_file, 'r', encoding='utf-8') as f:
            css = f.read()

        # Update CSS for Team, Stories, Locations
        css_replacement = '''/* ============================================================
   SHARED SIDEBAR + CARDS 2-COLUMN LAYOUT (Mockup-Faithful)
   ============================================================ */
.btn-outline-pill {
  border: 1.5px solid #a89f91;
  color: var(--ink);
  padding: 10px 22px;
  border-radius: 6px;
  font-weight: 600;
  font-size: 0.82rem;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  transition: all .3s ease;
  background: transparent;
  width: fit-content;
}
.btn-outline-pill:hover {
  background: var(--ink);
  color: var(--white);
  border-color: var(--ink);
}

/* TEAM */
.team { padding: 80px 0; background: var(--cream); position: relative; overflow: hidden; }
.team__container {
  display: grid;
  grid-template-columns: 290px 1fr 80px;
  gap: 36px;
  align-items: center;
}
.team__sidebar { max-width: 290px; }
.team__title {
  font-family: var(--ff-serif);
  font-size: clamp(1.8rem, 2.8vw, 2.3rem);
  font-weight: 600;
  line-height: 1.15;
  color: var(--ink);
  margin-bottom: 16px;
}
.team__text {
  font-size: 0.88rem;
  line-height: 1.75;
  color: var(--ink-light);
  margin-bottom: 22px;
}
.team__visual img {
  width: 100%;
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.06);
  display: block;
}

/* PATIENT STORIES */
.stories { padding: 80px 0; background: var(--cream); }
.stories__container {
  display: grid;
  grid-template-columns: 290px 1fr;
  gap: 36px;
  align-items: center;
}
.stories__sidebar { max-width: 290px; }
.stories__title {
  font-family: var(--ff-serif);
  font-size: clamp(1.8rem, 2.8vw, 2.3rem);
  font-weight: 600;
  line-height: 1.15;
  color: var(--ink);
  margin-bottom: 16px;
}
.stories__text {
  font-size: 0.88rem;
  line-height: 1.75;
  color: var(--ink-light);
  margin-bottom: 22px;
}
.stories__content-wrap {
  display: flex;
  align-items: center;
  gap: 12px;
  position: relative;
}
.stories__arrow {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  border: 1.5px solid rgba(41,38,46,0.18);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--ink);
  background: transparent;
  flex-shrink: 0;
  font-size: 1rem;
  transition: all .3s;
}
.stories__arrow:hover {
  background: var(--ink);
  color: var(--white);
  border-color: var(--ink);
}
.stories__grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 18px;
  flex: 1;
}
.story-card {
  background: var(--white);
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 2px 10px rgba(0,0,0,0.03);
  transition: transform .4s var(--ease), box-shadow .4s var(--ease);
  cursor: pointer;
}
.story-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 24px rgba(0,0,0,0.08);
}
.story-card__thumb-wrap {
  position: relative;
  aspect-ratio: 16/11;
  overflow: hidden;
}
.story-card__image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform .6s var(--ease);
}
.story-card:hover .story-card__image { transform: scale(1.05); }
.story-card__play {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 44px;
  height: 44px;
  background: rgba(255,255,255,0.92);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--gold);
  box-shadow: 0 4px 14px rgba(0,0,0,0.18);
}
.story-card__body {
  padding: 14px 16px;
}
.story-card__badge-row {
  display: flex;
  align-items: center;
  gap: 6px;
  color: var(--warm-gray);
  font-size: 0.72rem;
  margin-bottom: 4px;
}
.story-card__badge-row svg { color: var(--gold); }
.story-card__title {
  font-family: var(--ff-serif);
  font-size: 0.98rem;
  font-weight: 600;
  color: var(--ink);
  line-height: 1.3;
}

/* HOSPITAL LOCATIONS */
.locations { padding: 80px 0; background: var(--cream); }
.locations__container {
  display: grid;
  grid-template-columns: 290px 1fr;
  gap: 36px;
  align-items: center;
}
.locations__sidebar { max-width: 290px; }
.locations__title {
  font-family: var(--ff-serif);
  font-size: clamp(1.8rem, 2.8vw, 2.3rem);
  font-weight: 600;
  line-height: 1.15;
  color: var(--ink);
  margin-bottom: 16px;
}
.locations__text {
  font-size: 0.88rem;
  line-height: 1.75;
  color: var(--ink-light);
  margin-bottom: 22px;
}
.locations__grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 18px;
}
.location-card {
  border-radius: 12px;
  overflow: hidden;
  background: var(--white);
  box-shadow: 0 2px 10px rgba(0,0,0,0.03);
  transition: transform .4s var(--ease), box-shadow .4s var(--ease);
}
.location-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 24px rgba(0,0,0,0.08);
}
.location-card__image-wrap {
  position: relative;
  aspect-ratio: 16/10;
  overflow: hidden;
}
.location-card__image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.location-card__pin {
  position: absolute;
  top: 10px;
  right: 10px;
  color: var(--gold);
}
.location-card__body {
  padding: 14px 16px;
}
.location-card__name {
  font-family: var(--ff-serif);
  font-size: 0.95rem;
  font-weight: 600;
  color: var(--ink);
  margin-bottom: 8px;
  line-height: 1.3;
}
.location-card__link {
  color: var(--gold);
  font-weight: 600;
  font-size: 0.76rem;
  display: inline-flex;
  align-items: center;
  gap: 4px;
}
'''

        # Replace old team/stories/locations CSS blocks
        team_idx = css.find('/* ============================================================\n   TEAM SECTION')
        cta_idx = css.find('/* ============================================================\n   DARK CTA BANNER')

        if team_idx != -1 and cta_idx != -1:
            css = css[:team_idx] + css_replacement + '\n' + css[cta_idx:]
            with open(css_file, 'w', encoding='utf-8') as f:
                f.write(css)
            print(f'Updated CSS layouts in {css_file}')

update_all()
print('ALL TARGETS UPDATED SUCCESSFULLY!')

