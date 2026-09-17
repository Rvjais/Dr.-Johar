import os, shutil

targets = [
    '6ce732e63260f60c0203ef7caa72248ad6fedf5c',
    '6ce732e',
    'latest'
]

# 1. Copy transparent script image to all targets
src_img = 'assets/img/mockup/a-brighter-you-transparent.png'
for t in targets:
    dest_dir = os.path.join(t, 'assets', 'img', 'mockup')
    os.makedirs(dest_dir, exist_ok=True)
    shutil.copy2(src_img, os.path.join(dest_dir, 'a-brighter-you-transparent.png'))
print('Copied a-brighter-you-transparent.png to all targets')

# 2. HTML replacement for Section 11
html_cta_replacement = '''<!-- ============================================
     SECTION 11: DARK CTA BANNER (Exact Mockup Match)
     ============================================ -->
<section class="cta-banner" id="ctaBanner">
  <div class="container cta-banner__container">
    <div class="cta-banner__left-space" aria-hidden="true"></div>
    <div class="cta-banner__main">
      <div class="cta-banner__content">
        <p class="cta-banner__eyebrow">CONFIDENCE LOOKS GOOD ON YOU</p>
        <h2 class="cta-banner__title">Let's Begin Your Journey</h2>
        <p class="cta-banner__text">Book a consultation with Dr. Manoj Johar and his team<br>at KRTAM Skin Clinic. Together, we'll create a plan that's personal, precise and possible.</p>
        <div class="cta-banner__bar">
          <div class="cta-banner__features">
            <div class="cta-banner__feature">
              <div class="cta-banner__feature-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
              </div>
              <span>Personalized Guidance</span>
            </div>
            <div class="cta-banner__divider" aria-hidden="true"></div>
            <div class="cta-banner__feature">
              <div class="cta-banner__feature-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="3"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2"/></svg>
              </div>
              <span>Clear Treatment Plans</span>
            </div>
            <div class="cta-banner__divider" aria-hidden="true"></div>
            <div class="cta-banner__feature">
              <div class="cta-banner__feature-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg>
              </div>
              <span>Compassionate Care</span>
            </div>
          </div>
          <a href="appointments.html" class="cta-banner__btn">Book an Appointment &rarr;</a>
        </div>
      </div>
      <div class="cta-banner__script-box" aria-hidden="true">
        <img src="assets/img/mockup/a-brighter-you-transparent.png" alt="A Brighter You" class="cta-banner__script-img">
      </div>
    </div>
  </div>
</section>
'''

css_cta_replacement = '''/* ============================================================
   SECTION 11: DARK CTA BANNER (Exact Mockup Match)
   ============================================================ */
.cta-banner {
  position: relative;
  background-color: #1a140e;
  background-image: url('../img/mockup/cta-bg.png');
  background-position: left center;
  background-size: cover;
  background-repeat: no-repeat;
  min-height: 380px;
  display: flex;
  align-items: center;
  padding: 50px 0;
  color: var(--white);
  overflow: hidden;
}
.cta-banner__container {
  display: flex;
  align-items: center;
  width: 100%;
  position: relative;
  z-index: 2;
}
.cta-banner__left-space {
  width: 28%;
  flex-shrink: 0;
}
.cta-banner__main {
  flex: 1;
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  position: relative;
}
.cta-banner__content {
  flex: 1;
  text-align: left;
}
.cta-banner__eyebrow {
  text-transform: uppercase;
  letter-spacing: 0.22em;
  font-size: 0.68rem;
  color: #a69a8b;
  font-weight: 600;
  margin-bottom: 8px;
}
.cta-banner__title {
  font-family: var(--ff-serif);
  font-size: clamp(2.2rem, 3.4vw, 2.8rem);
  font-weight: 500;
  color: #ffffff;
  line-height: 1.15;
  margin-bottom: 12px;
  letter-spacing: -0.01em;
}
.cta-banner__text {
  font-size: 0.85rem;
  color: rgba(255, 255, 255, 0.76);
  line-height: 1.65;
  margin-bottom: 24px;
  max-width: 540px;
}
.cta-banner__bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 20px;
  max-width: 760px;
}
.cta-banner__features {
  display: flex;
  align-items: center;
  gap: 16px;
}
.cta-banner__feature {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 0.74rem;
  color: rgba(255, 255, 255, 0.85);
  white-space: nowrap;
}
.cta-banner__feature-icon {
  width: 22px;
  height: 22px;
  color: #d4a373;
  flex-shrink: 0;
}
.cta-banner__feature-icon svg {
  width: 100%;
  height: 100%;
}
.cta-banner__divider {
  width: 1px;
  height: 20px;
  background: rgba(255, 255, 255, 0.2);
}
.cta-banner__btn {
  background: linear-gradient(135deg, #a87948, #86572e);
  color: #ffffff !important;
  padding: 10px 22px;
  border-radius: 6px;
  font-weight: 600;
  font-size: 0.8rem;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  white-space: nowrap;
  box-shadow: 0 4px 16px rgba(134, 87, 46, 0.35);
  transition: transform 0.3s var(--ease), box-shadow 0.3s var(--ease);
}
.cta-banner__btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(134, 87, 46, 0.45);
}
.cta-banner__script-box {
  position: absolute;
  right: 0;
  top: -20px;
  pointer-events: none;
}
.cta-banner__script-img {
  height: 110px;
  width: auto;
  opacity: 0.85;
}
'''

for t in targets:
    # Update HTML
    html_file = os.path.join(t, 'index.html')
    with open(html_file, 'r', encoding='utf-8') as f:
        html = f.read()

    start_cta = html.find('<!-- ============================================\n     SECTION 11: DARK CTA BANNER')
    end_cta = html.find('<!-- ============================================\n     SECTION 12: FOOTER')
    if start_cta != -1 and end_cta != -1:
        html = html[:start_cta] + html_cta_replacement + html[end_cta:]
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'Updated HTML in {html_file}')

    # Update CSS
    css_file = os.path.join(t, 'assets', 'css', 'krtam-mockup.css')
    with open(css_file, 'r', encoding='utf-8') as f:
        css = f.read()

    start_css = css.find('/* ============================================================\n   SECTION 11: DARK CTA BANNER')
    end_css = css.find('/* ============================================================\n   SECTION 12: FOOTER')
    if start_css != -1 and end_css != -1:
        css = css[:start_css] + css_cta_replacement + '\n' + css[end_css:]
        with open(css_file, 'w', encoding='utf-8') as f:
            f.write(css)
        print(f'Updated CSS in {css_file}')

print('ALL TARGETS UPDATED WITH EXACT CTA BANNER MATCH!')

