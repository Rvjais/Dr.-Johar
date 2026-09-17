import os, shutil

targets = [
    '6ce732e63260f60c0203ef7caa72248ad6fedf5c',
    '6ce732e',
    'latest'
]

# 1. Copy the 4 downloaded thumbnails to all targets
thumbs = ['yt-thumb-1.jpg', 'yt-thumb-2.jpg', 'yt-thumb-3.jpg', 'yt-thumb-4.jpg']
for t in targets:
    dest_dir = os.path.join(t, 'assets', 'img', 'mockup')
    os.makedirs(dest_dir, exist_ok=True)
    for thumb in thumbs:
        src = os.path.join('assets', 'img', 'mockup', thumb)
        shutil.copy2(src, os.path.join(dest_dir, thumb))
print('Copied all 4 YouTube thumbnails to all targets')

# 2. HTML replacement for Section 9: Patient Stories
html_stories_replacement = '''<!-- ============================================
     SECTION 9: PATIENT STORIES (Live YouTube Case Stories)
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
      <button class="stories__arrow stories__arrow--prev" id="storiesPrevBtn" aria-label="Previous story">&lsaquo;</button>
      <div class="stories__track-window">
        <div class="stories__grid" id="storiesGrid">
          <div class="story-card">
            <a href="https://www.youtube.com/watch?v=R6inggloZRc" target="_blank" rel="noopener" class="story-card__link-wrap" aria-label="Watch Carpal Tunnel Syndrome video">
              <div class="story-card__thumb-wrap">
                <img src="assets/img/mockup/yt-thumb-1.jpg" alt="Carpal Tunnel Syndrome Treatment" class="story-card__image">
                <div class="story-card__play">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><polygon points="6 3 20 12 6 21 6 3"/></svg>
                </div>
              </div>
              <div class="story-card__body">
                <div class="story-card__icon">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 3"/></svg>
                </div>
                <div class="story-card__meta">
                  <div class="story-card__category">Hand Surgery &ndash;</div>
                  <div class="story-card__name">Carpal Tunnel Syndrome</div>
                </div>
              </div>
            </a>
          </div>
          <div class="story-card">
            <a href="https://www.youtube.com/watch?v=-ckc0orgMVo" target="_blank" rel="noopener" class="story-card__link-wrap" aria-label="Watch Dupuytren's Contracture video">
              <div class="story-card__thumb-wrap">
                <img src="assets/img/mockup/yt-thumb-2.jpg" alt="Dupuytren's Contracture Treatment" class="story-card__image">
                <div class="story-card__play">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><polygon points="6 3 20 12 6 21 6 3"/></svg>
                </div>
              </div>
              <div class="story-card__body">
                <div class="story-card__icon">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="4"/></svg>
                </div>
                <div class="story-card__meta">
                  <div class="story-card__category">Hand Reconstruction &ndash;</div>
                  <div class="story-card__name">Dupuytren's Contracture</div>
                </div>
              </div>
            </a>
          </div>
          <div class="story-card">
            <a href="https://www.youtube.com/watch?v=ShN5jvy0JNU" target="_blank" rel="noopener" class="story-card__link-wrap" aria-label="Watch Liposuction vs Tummy Tuck video">
              <div class="story-card__thumb-wrap">
                <img src="assets/img/mockup/yt-thumb-3.jpg" alt="Liposuction vs Tummy Tuck" class="story-card__image">
                <div class="story-card__play">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><polygon points="6 3 20 12 6 21 6 3"/></svg>
                </div>
              </div>
              <div class="story-card__body">
                <div class="story-card__icon">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="4"/></svg>
                </div>
                <div class="story-card__meta">
                  <div class="story-card__category">Body Contouring &ndash;</div>
                  <div class="story-card__name">Liposuction vs Tummy Tuck</div>
                </div>
              </div>
            </a>
          </div>
          <div class="story-card">
            <a href="https://www.youtube.com/watch?v=qjWf7uwm02s" target="_blank" rel="noopener" class="story-card__link-wrap" aria-label="Watch Gynecomastia Treatment video">
              <div class="story-card__thumb-wrap">
                <img src="assets/img/mockup/yt-thumb-4.jpg" alt="Gynecomastia Treatment" class="story-card__image">
                <div class="story-card__play">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><polygon points="6 3 20 12 6 21 6 3"/></svg>
                </div>
              </div>
              <div class="story-card__body">
                <div class="story-card__icon">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 3"/></svg>
                </div>
                <div class="story-card__meta">
                  <div class="story-card__category">Male Aesthetics &ndash;</div>
                  <div class="story-card__name">Gynecomastia Treatment</div>
                </div>
              </div>
            </a>
          </div>
        </div>
      </div>
      <button class="stories__arrow stories__arrow--next" id="storiesNextBtn" aria-label="Next story">&rsaquo;</button>
    </div>
  </div>
</section>
'''

# 3. CSS for Carousel Window & Track
css_carousel_patch = '''/* ============================================================
   SECTION 9: PATIENT STORIES (Exact Thumbnail Dimensions & Carousel)
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
.stories__carousel-wrap { display: flex; align-items: center; gap: 12px; position: relative; width: 100%; overflow: hidden; }
.stories__arrow {
  width: 32px; height: 32px; border-radius: 50%; border: 1.5px solid #a8947f;
  display: flex; align-items: center; justify-content: center; color: #6a513d;
  background: transparent; flex-shrink: 0; font-size: 1.25rem; line-height: 1;
  padding-bottom: 2px; transition: all .25s ease; cursor: pointer; z-index: 10;
}
.stories__arrow:hover { background: var(--ink); color: var(--white); border-color: var(--ink); }
.stories__track-window {
  flex: 1;
  overflow: hidden;
  width: 100%;
}
.stories__grid {
  display: flex;
  gap: 16px;
  transition: transform 0.45s cubic-bezier(.23, 1, .32, 1);
}
.story-card {
  flex: 0 0 calc((100% - 32px) / 3);
  min-width: 230px;
  background: var(--white);
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 2px 10px rgba(0,0,0,0.04);
  transition: transform .35s var(--ease), box-shadow .35s var(--ease);
  cursor: pointer;
}
.story-card:hover { transform: translateY(-4px); box-shadow: 0 8px 20px rgba(0,0,0,0.08); }
.story-card__link-wrap {
  display: block;
  color: inherit;
  text-decoration: none;
}
.story-card__thumb-wrap {
  position: relative;
  aspect-ratio: 16/10;
  overflow: hidden;
  background: #000;
}
.story-card__image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform .5s var(--ease);
}
.story-card:hover .story-card__image { transform: scale(1.05); }
.story-card__play {
  position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
  width: 38px; height: 38px; background: rgba(255,255,255,0.92); border-radius: 50%;
  display: flex; align-items: center; justify-content: center; color: var(--gold);
  box-shadow: 0 3px 12px rgba(0,0,0,0.18); transition: transform 0.3s ease, background 0.3s ease;
}
.story-card:hover .story-card__play {
  transform: translate(-50%, -50%) scale(1.12);
  background: #ffffff;
}
.story-card__body { padding: 12px 14px; display: flex; align-items: center; gap: 10px; }
.story-card__icon { color: var(--gold); flex-shrink: 0; }
.story-card__category { font-size: 0.72rem; color: var(--warm-gray); font-weight: 600; line-height: 1.2; }
.story-card__name { font-family: var(--ff-serif); font-size: 0.88rem; font-weight: 700; color: var(--ink); line-height: 1.2; }
'''

carousel_script = '''
  // Patient Stories Carousel Slider
  const storiesGrid = document.getElementById('storiesGrid');
  const prevBtn = document.getElementById('storiesPrevBtn');
  const nextBtn = document.getElementById('storiesNextBtn');
  if (storiesGrid && prevBtn && nextBtn) {
    let currentIdx = 0;
    const cards = storiesGrid.querySelectorAll('.story-card');
    const totalCards = cards.length;
    function updateCarousel() {
      const cardWidth = cards[0].offsetWidth + 16; // width + gap
      const maxIdx = Math.max(0, totalCards - 3);
      if (currentIdx > maxIdx) currentIdx = maxIdx;
      if (currentIdx < 0) currentIdx = 0;
      storiesGrid.style.transform = `translateX(-${currentIdx * cardWidth}px)`;
      prevBtn.style.opacity = currentIdx === 0 ? '0.4' : '1';
      nextBtn.style.opacity = currentIdx >= maxIdx ? '0.4' : '1';
    }
    prevBtn.addEventListener('click', () => {
      if (currentIdx > 0) { currentIdx--; updateCarousel(); }
    });
    nextBtn.addEventListener('click', () => {
      const maxIdx = Math.max(0, totalCards - 3);
      if (currentIdx < maxIdx) { currentIdx++; updateCarousel(); }
    });
    window.addEventListener('resize', updateCarousel, { passive: true });
    updateCarousel();
  }
'''

for t in targets:
    # 1. Update HTML
    html_file = os.path.join(t, 'index.html')
    with open(html_file, 'r', encoding='utf-8') as f:
        html = f.read()

    start_stories = html.find('<!-- ============================================\n     SECTION 9: PATIENT STORIES')
    end_stories = html.find('<!-- ============================================\n     SECTION 10: HOSPITAL LOCATIONS')
    if start_stories != -1 and end_stories != -1:
        html = html[:start_stories] + html_stories_replacement + html[end_stories:]

    # Add carousel script if not present
    if 'storiesPrevBtn' not in html:
        script_anchor = '})();\n</script>'
        if script_anchor in html:
            html = html.replace(script_anchor, carousel_script + '\n' + script_anchor)

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'Updated HTML in {html_file}')

    # 2. Update CSS
    css_file = os.path.join(t, 'assets', 'css', 'krtam-mockup.css')
    with open(css_file, 'r', encoding='utf-8') as f:
        css = f.read()

    start_css = css.find('/* ============================================================\n   SECTION 9: PATIENT STORIES')
    end_css = css.find('/* ============================================================\n   SECTION 10: HOSPITAL LOCATIONS')
    if start_css != -1 and end_css != -1:
        css = css[:start_css] + css_carousel_patch + '\n' + css[end_css:]
        with open(css_file, 'w', encoding='utf-8') as f:
            f.write(css)
        print(f'Updated CSS in {css_file}')

print('ALL TARGETS UPDATED WITH YOUTUBE VIDEOS & EXACT THUMBNAIL DIMENSIONS!')

