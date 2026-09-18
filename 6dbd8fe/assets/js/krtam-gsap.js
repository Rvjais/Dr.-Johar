/* ============================================================
   KRTAM Skin Clinic — GSAP Motion
   One motion language: short fade-up reveals, a single ease,
   each animation plays once. Hover states stay in CSS.
   ============================================================ */

document.addEventListener('DOMContentLoaded', () => {
  if (typeof gsap === 'undefined' || typeof ScrollTrigger === 'undefined') {
    console.warn('GSAP or ScrollTrigger not loaded');
    return;
  }

  gsap.registerPlugin(ScrollTrigger);

  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  const EASE = 'power3.out';
  const DURATION = 0.9;
  const DISTANCE = 28;
  // Several targets (cards, buttons) have a CSS `transition: transform` for
  // their hover state. It fights GSAP's per-frame updates, so it is disabled
  // while a reveal runs and every inline style is handed back to CSS after.
  const CLEAR = 'transform,opacity,transition';

  gsap.defaults({ ease: EASE, duration: DURATION });

  const hidden = (extra = {}) => ({ opacity: 0, y: DISTANCE, transition: 'none', ...extra });
  const shown = (extra = {}) => ({ opacity: 1, y: 0, clearProps: CLEAR, ...extra });

  // Fade-up a group of elements once, when `trigger` scrolls into view
  function reveal(targets, trigger, { start = 'top 80%', stagger = 0.1 } = {}) {
    const els = gsap.utils.toArray(targets);
    if (!els.length) return;
    gsap.set(els, hidden());
    gsap.to(els, shown({
      stagger,
      scrollTrigger: { trigger, start, once: true }
    }));
  }

  // Card grids: rows reveal together as they enter, staggered left to right
  function revealCards(selector) {
    const cards = gsap.utils.toArray(selector);
    if (!cards.length) return;
    gsap.set(cards, hidden());
    ScrollTrigger.batch(cards, {
      start: 'top 88%',
      once: true,
      onEnter: batch => gsap.to(batch, shown({ stagger: 0.08, overwrite: true }))
    });
  }

  // Decorative vertical words: opacity only, so their CSS layout is untouched
  function revealWords(container) {
    const words = container.querySelectorAll('span');
    if (!words.length) return;
    gsap.set(words, { opacity: 0 });
    gsap.to(words, {
      opacity: 1,
      duration: 1.2,
      stagger: 0.15,
      clearProps: 'opacity',
      scrollTrigger: { trigger: container, start: 'top 85%', once: true }
    });
  }

  // 1. HEADER + HERO (on load)
  gsap.set('.site-header', { opacity: 0 });
  gsap.set(['.hero__tag', '.hero__title', '.hero__subtitle', '.hero__buttons a', '.hero__badge'], hidden());
  gsap.set(['.hero__quote-box', '.hero__scroll'], { opacity: 0 });

  gsap.timeline({ delay: 0.1 })
    .to('.site-header', { opacity: 1, duration: 0.8, clearProps: 'opacity' })
    .to('.hero__tag', shown(), 0.15)
    .to('.hero__title', shown({ duration: 1.1 }), 0.25)
    .to('.hero__subtitle', shown(), 0.4)
    .to('.hero__buttons a', shown({ stagger: 0.1 }), 0.55)
    .to('.hero__badge', shown({ stagger: 0.07 }), 0.7)
    .to('.hero__quote-box', { opacity: 1, duration: 1.2, clearProps: 'opacity' }, 0.6)
    .to('.hero__scroll', { opacity: 1, duration: 1, clearProps: 'opacity' }, 1.1);

  // 2. SECTION CONTENT
  reveal('.philosophy__content > *', '.philosophy', { stagger: 0.12 });
  reveal('.services__header > *', '.services__header', { stagger: 0.12 });
  reveal('.reconstructive__content > *', '.reconstructive', { stagger: 0.12 });
  reveal('.expert__info > *', '.expert');
  reveal('.expert__quote', '.expert');
  reveal('.stat', '.stats', { start: 'top 88%', stagger: 0.08 });
  reveal('.team__sidebar > *', '.team');
  reveal('.stories__sidebar > *', '.stories');
  reveal('.locations__sidebar > *', '.locations');
  reveal('.cta-banner__content > *', '.cta-banner', { stagger: 0.12 });

  // 3. CARD GRIDS
  revealCards('.service-card');
  revealCards('.story-card');
  revealCards('.location-card');

  // 4. IMAGERY
  // Expert portrait: slow fade, then the experience badge settles in
  gsap.set('.expert__portrait > img', { opacity: 0 });
  gsap.set('.expert__badge', hidden({ y: 16 }));
  gsap.timeline({ scrollTrigger: { trigger: '.expert', start: 'top 80%', once: true } })
    .to('.expert__portrait > img', { opacity: 1, duration: 1.4, ease: 'power2.out', clearProps: 'opacity' })
    .to('.expert__badge', shown(), 0.5);

  // Team photo: fades in while easing back from a slight zoom (frame clips the overflow)
  gsap.set('.team__photo', { opacity: 0, scale: 1.06 });
  gsap.to('.team__photo', {
    opacity: 1,
    scale: 1,
    duration: 1.6,
    ease: 'power2.out',
    clearProps: 'transform,opacity',
    scrollTrigger: { trigger: '.team__visual', start: 'top 85%', once: true }
  });

  // 5. DECORATIVE TEXT
  gsap.utils.toArray('.side-words, .hero__center-words, .cta-banner__script').forEach(revealWords);

  // 6. STAT COUNTERS
  document.querySelectorAll('.stat__number').forEach(stat => {
    const text = stat.textContent.trim();
    const match = text.match(/\d[\d,]*/);
    if (!match) return;

    const target = parseInt(match[0].replace(/,/g, ''), 10);
    const prefix = text.slice(0, match.index);
    const suffix = text.slice(match.index + match[0].length);
    const counter = { val: 0 };
    const render = () => {
      stat.textContent = prefix + Math.round(counter.val).toLocaleString('en-US') + suffix;
    };

    render();
    gsap.to(counter, {
      val: target,
      duration: 1.8,
      ease: 'power2.out',
      onUpdate: render,
      scrollTrigger: { trigger: '.stats', start: 'top 88%', once: true }
    });
  });
});
