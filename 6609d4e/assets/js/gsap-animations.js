/**
 * Kratam Hospital – GSAP Premium Animation Engine (Ivory & Champagne Gold)
 * Cinematic, GSAP-powered animations with ScrollTrigger and Lenis smooth scroll.
 */
(function () {
  'use strict';

  if (typeof gsap === 'undefined') {
    console.warn('[Kratam] GSAP not loaded – skipping animations');
    return;
  }
  gsap.registerPlugin(ScrollTrigger);

  var prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)');
  if (prefersReduced.matches) return;

  gsap.defaults({ ease: 'power3.out', duration: 1 });
  ScrollTrigger.config({ limitCallbacks: true });

  /* ================================================================
     UTILITIES
  ================================================================ */
  function disableLegacy() {
    document.querySelectorAll('.reveal, .reveal-stagger').forEach(function (el) {
      el.classList.remove('reveal', 'reveal-stagger', 'is-visible');
    });
  }

  function splitLines(el) {
    if (!el) return [];
    var html = el.innerHTML;
    var frags = html.split(/<br\s*\/?>/gi);
    el.setAttribute('aria-label', el.textContent);
    el.innerHTML = frags
      .map(function (f) {
        return '<div class="ln-mask"><div class="ln-inner">' + f.trim() + '</div></div>';
      })
      .join('');
    return el.querySelectorAll('.ln-inner');
  }

  function st(trigger, start) {
    return { trigger: trigger, start: start || 'top 80%', toggleActions: 'play none none reverse' };
  }

  /* ================================================================
     0. LENIS SMOOTH SCROLL INTEGRATION
  ================================================================ */
  var lenis = null;
  function initLenis() {
    if (typeof Lenis === 'undefined') return;
    try {
      lenis = new Lenis({
        duration: 1.25,
        easing: function (t) { return Math.min(1, 1.001 - Math.pow(2, -10 * t)); },
        orientation: 'vertical',
        smoothWheel: true,
        wheelMultiplier: 0.95
      });

      lenis.on('scroll', ScrollTrigger.update);
      gsap.ticker.add(function (time) {
        lenis.raf(time * 1000);
      });
      gsap.ticker.lagSmoothing(0);
    } catch (e) {
      console.warn('[Kratam] Lenis init failed:', e);
    }
  }

  /* ================================================================
     1. HERO CINEMATIC ENTRANCE
  ================================================================ */
  function heroEntrance() {
    var hero = document.querySelector('.hero');
    if (!hero) return;

    var tl = gsap.timeline({ defaults: { ease: 'power4.out' } });

    // Background watermark "Beauty" scrub parallax
    var bgText = hero.querySelector('.hero__bg-text');
    if (bgText) {
      gsap.to(bgText, {
        xPercent: 25,
        ease: 'none',
        scrollTrigger: {
          trigger: hero,
          start: 'top top',
          end: 'bottom top',
          scrub: 0.8
        }
      });
    }

    // Hero Badge
    var badge = hero.querySelector('.hero__badge');
    if (badge) {
      gsap.set(badge, { opacity: 0, y: -25 });
      tl.to(badge, { opacity: 1, y: 0, duration: 0.9, ease: 'back.out(2)' }, 0.1);
    }

    // Main H1 Title - line mask reveal
    var title = hero.querySelector('.hero__title');
    if (title) {
      var lines = splitLines(title);
      gsap.set(lines, { yPercent: 120 });
      tl.to(lines, {
        yPercent: 0, duration: 1.3, stagger: 0.18, ease: 'power4.out'
      }, 0.25);
    }

    // Lead text
    var lead = hero.querySelector('.hero__lead');
    if (lead) {
      gsap.set(lead, { opacity: 0, y: 30 });
      tl.to(lead, { opacity: 1, y: 0, duration: 1 }, 0.7);
    }

    // Action buttons
    var actions = hero.querySelectorAll('.hero__actions .btn');
    if (actions.length) {
      gsap.set(actions, { opacity: 0, y: 22, scale: 0.9 });
      tl.to(actions, {
        opacity: 1, y: 0, scale: 1, duration: 0.8, stagger: 0.15, ease: 'back.out(2)'
      }, 0.9);
    }

    // Trust items & counters
    var trustItems = hero.querySelectorAll('.hero__trust-item');
    if (trustItems.length) {
      gsap.set(trustItems, { opacity: 0, y: 25 });
      tl.to(trustItems, {
        opacity: 1, y: 0, duration: 0.8, stagger: 0.12, ease: 'power3.out'
      }, 1.1);

      trustItems.forEach(function (item) {
        var countEl = item.querySelector('[data-count]');
        if (!countEl) return;
        var target = parseFloat(countEl.getAttribute('data-count'));
        var suffix = countEl.getAttribute('data-suffix') || '';
        countEl.removeAttribute('data-count');
        var proxy = { val: 0 };
        gsap.to(proxy, {
          val: target,
          duration: 2.2,
          ease: 'power2.out',
          delay: 1.1,
          onUpdate: function () {
            countEl.textContent = Math.round(proxy.val) + suffix;
          },
          onComplete: function () {
            gsap.fromTo(countEl, { scale: 1 }, { scale: 1.25, duration: 0.25, yoyo: true, repeat: 1 });
          }
        });
      });
    }

    // Visual Frame & Image
    var frameImg = hero.querySelector('.hero__frame img');
    if (frameImg) {
      gsap.set(frameImg, { scale: 1.35, filter: 'blur(6px) brightness(0.7)' });
      tl.to(frameImg, {
        scale: 1, filter: 'blur(0px) brightness(1)', duration: 2.4, ease: 'power3.out'
      }, 0.2);

      gsap.to(frameImg, {
        yPercent: 18,
        ease: 'none',
        scrollTrigger: {
          trigger: hero,
          start: 'top top',
          end: 'bottom top',
          scrub: 0.8
        }
      });
    }

    // Decorative Rotating Rings
    var ring1 = hero.querySelector('.hero__ring');
    var ring2 = hero.querySelector('.hero__ring--2');
    if (ring1) {
      gsap.to(ring1, { rotation: 360, duration: 32, ease: 'none', repeat: -1 });
    }
    if (ring2) {
      gsap.to(ring2, { rotation: -360, duration: 42, ease: 'none', repeat: -1 });
    }

    // Floating Hero Badges
    var card1 = hero.querySelector('.hero__card--1');
    var card2 = hero.querySelector('.hero__card--2');
    if (card1) {
      gsap.set(card1, { opacity: 0, x: -50, scale: 0.85 });
      tl.to(card1, { opacity: 1, x: 0, scale: 1, duration: 1.1, ease: 'back.out(1.8)' }, 0.95);
      gsap.to(card1, { y: -8, duration: 2.6, yoyo: true, repeat: -1, ease: 'sine.inOut' });
    }
    if (card2) {
      gsap.set(card2, { opacity: 0, x: 50, scale: 0.85 });
      tl.to(card2, { opacity: 1, x: 0, scale: 1, duration: 1.1, ease: 'back.out(1.8)' }, 1.15);
      gsap.to(card2, { y: 8, duration: 3.2, yoyo: true, repeat: -1, ease: 'sine.inOut' });
    }
  }

  /* ================================================================
     2. MEET THE SURGEON SECTION
  ================================================================ */
  function surgeonSection() {
    var docVisual = document.querySelector('.doc-visual');
    if (!docVisual) return;

    var frame = docVisual.querySelector('.doc-visual__frame');
    if (frame) {
      gsap.set(frame, { clipPath: 'inset(0 100% 0 0)' });
      gsap.to(frame, {
        clipPath: 'inset(0 0% 0 0)',
        duration: 1.5,
        ease: 'power4.inOut',
        scrollTrigger: st(docVisual, 'top 75%')
      });

      var dImg = frame.querySelector('img');
      if (dImg) {
        gsap.to(dImg, {
          yPercent: -12,
          ease: 'none',
          scrollTrigger: {
            trigger: docVisual,
            start: 'top bottom',
            end: 'bottom top',
            scrub: 0.8
          }
        });
      }
    }

    var badge = docVisual.querySelector('.doc-visual__badge');
    if (badge) {
      gsap.from(badge, {
        scale: 0, opacity: 0, duration: 0.9, delay: 0.8, ease: 'back.out(2.5)',
        scrollTrigger: st(docVisual, 'top 75%')
      });
      gsap.to(badge, { y: -5, duration: 2.8, yoyo: true, repeat: -1, ease: 'sine.inOut' });
    }

    var quote = docVisual.querySelector('.doc-visual__quote');
    if (quote) {
      gsap.from(quote, {
        y: 40, opacity: 0, duration: 1, delay: 0.9,
        scrollTrigger: st(docVisual, 'top 75%')
      });
    }

    // Right Column Copy
    var rightCol = docVisual.nextElementSibling;
    if (rightCol) {
      var h2 = rightCol.querySelector('h2');
      if (h2) {
        var lines = splitLines(h2);
        gsap.set(lines, { yPercent: 110 });
        gsap.to(lines, {
          yPercent: 0, duration: 1.2, stagger: 0.16, ease: 'power4.out',
          scrollTrigger: st(rightCol, 'top 80%')
        });
      }

      var items = rightCol.querySelectorAll('.checklist li');
      if (items.length) {
        gsap.from(items, {
          x: 35, opacity: 0, duration: 0.7, stagger: 0.08, ease: 'power3.out',
          scrollTrigger: st(rightCol, 'top 65%')
        });
      }

      var sig = rightCol.querySelector('.signature');
      if (sig) {
        gsap.from(sig, {
          y: 20, opacity: 0, duration: 1, delay: 0.4,
          scrollTrigger: st(rightCol, 'top 60%')
        });
      }
    }
  }

  /* ================================================================
     3. CATEGORY TILES (3D ENTRANCE + TILT)
  ================================================================ */
  function categoryTiles() {
    var tiles = document.querySelectorAll('.cat-tile');
    if (!tiles.length) return;

    gsap.from(tiles, {
      y: 90, opacity: 0, rotationY: 12, scale: 0.88,
      duration: 1.1, stagger: 0.16, ease: 'power3.out',
      scrollTrigger: st('.cat-tile', 'top 82%')
    });

    if (window.matchMedia('(hover: hover) and (pointer: fine)').matches) {
      tiles.forEach(function (tile) {
        var shine = document.createElement('span');
        shine.className = 'card-specular-shine';
        shine.style.cssText = 'position:absolute!important;inset:0!important;width:100%!important;height:100%!important;pointer-events:none!important;z-index:4!important;border-radius:inherit!important;';
        tile.appendChild(shine);

        tile.addEventListener('pointermove', function (e) {
          var rect = tile.getBoundingClientRect();
          var x = (e.clientX - rect.left) / rect.width - 0.5;
          var y = (e.clientY - rect.top) / rect.height - 0.5;
          gsap.to(tile, {
            rotationY: x * 10,
            rotationX: y * -10,
            duration: 0.35,
            ease: 'power2.out',
            transformPerspective: 800
          });
          tile.style.setProperty('--shine-x', (e.clientX - rect.left) + 'px');
          tile.style.setProperty('--shine-y', (e.clientY - rect.top) + 'px');
        });

        tile.addEventListener('pointerleave', function () {
          gsap.to(tile, {
            rotationY: 0,
            rotationX: 0,
            duration: 0.8,
            ease: 'elastic.out(1, 0.4)'
          });
        });
      });
    }
  }

  /* ================================================================
     4. SECTION HEADINGS LINE REVEAL
  ================================================================ */
  function sectionHeadings() {
    document.querySelectorAll('.section-head, .split > div, .strip').forEach(function (sec) {
      var h2 = sec.querySelector('h2.h2');
      if (h2) {
        var lines = splitLines(h2);
        gsap.set(lines, { yPercent: 110 });
        gsap.to(lines, {
          yPercent: 0, duration: 1.2, stagger: 0.15, ease: 'power4.out',
          scrollTrigger: st(sec, 'top 82%')
        });
      }

      var eyebrow = sec.querySelector('.eyebrow');
      if (eyebrow) {
        gsap.from(eyebrow, {
          y: 20, opacity: 0, duration: 0.8,
          scrollTrigger: st(sec, 'top 85%')
        });
      }
    });
  }

  /* ================================================================
     5. GENERAL IMAGE PARALLAX
  ================================================================ */
  function imageParallax() {
    var images = document.querySelectorAll('.page-hero__visual img, .cat-tile img');
    images.forEach(function (img) {
      gsap.to(img, {
        yPercent: -10,
        ease: 'none',
        scrollTrigger: {
          trigger: img.parentElement,
          start: 'top bottom',
          end: 'bottom top',
          scrub: 0.6
        }
      });
    });
  }

  /* ================================================================
     6. CUSTOM CHAMPAGNE CURSOR
  ================================================================ */
  function customCursor() {
    if (!window.matchMedia('(hover: hover) and (pointer: fine)').matches) return;

    var dot = document.createElement('div');
    dot.className = 'kratam-cursor-dot';
    var ring = document.createElement('div');
    ring.className = 'kratam-cursor-ring';
    document.body.appendChild(dot);
    document.body.appendChild(ring);

    var setDotX = gsap.quickTo(dot, 'x', { duration: 0.08, ease: 'power2.out' });
    var setDotY = gsap.quickTo(dot, 'y', { duration: 0.08, ease: 'power2.out' });
    var setRingX = gsap.quickTo(ring, 'x', { duration: 0.28, ease: 'power3.out' });
    var setRingY = gsap.quickTo(ring, 'y', { duration: 0.28, ease: 'power3.out' });

    window.addEventListener('pointermove', function (e) {
      setDotX(e.clientX);
      setDotY(e.clientY);
      setRingX(e.clientX);
      setRingY(e.clientY);
    }, { passive: true });

    var hoverSelectors = 'a, button, .btn, .cat-tile, .card, .tcard, input, select, textarea';
    document.addEventListener('mouseover', function (e) {
      if (e.target && e.target.closest(hoverSelectors)) {
        document.body.classList.add('cursor-active');
      }
    });
    document.addEventListener('mouseout', function (e) {
      if (e.target && e.target.closest(hoverSelectors)) {
        document.body.classList.remove('cursor-active');
      }
    });
  }

  /* ================================================================
     7. AMBIENT GLOW ORBS
  ================================================================ */
  function ambientGlow() {
    if (document.querySelector('.ambient-glow-wrapper')) return;
    var wrapper = document.createElement('div');
    wrapper.className = 'ambient-glow-wrapper';
    wrapper.innerHTML = '<div class="ambient-glow ambient-glow--1"></div><div class="ambient-glow ambient-glow--2"></div>';
    document.body.insertBefore(wrapper, document.body.firstChild);

    var orb1 = wrapper.querySelector('.ambient-glow--1');
    var orb2 = wrapper.querySelector('.ambient-glow--2');

    if (orb1) {
      gsap.to(orb1, {
        y: '50vh', x: '15vw', ease: 'none',
        scrollTrigger: { trigger: document.body, start: 'top top', end: 'bottom bottom', scrub: 1.2 }
      });
    }
    if (orb2) {
      gsap.to(orb2, {
        y: '-40vh', x: '-12vw', ease: 'none',
        scrollTrigger: { trigger: document.body, start: 'top top', end: 'bottom bottom', scrub: 1.5 }
      });
    }
  }

  /* ================================================================
     8. MAGNETIC BUTTONS & RIPPLE
  ================================================================ */
  function magneticButtons() {
    if (!window.matchMedia('(hover: hover) and (pointer: fine)').matches) return;

    document.querySelectorAll('.btn').forEach(function (btn) {
      btn.addEventListener('pointermove', function (e) {
        var rect = btn.getBoundingClientRect();
        var cx = rect.left + rect.width / 2;
        var cy = rect.top + rect.height / 2;
        var dx = (e.clientX - cx) * 0.18;
        var dy = (e.clientY - cy) * 0.18;
        gsap.to(btn, { x: dx, y: dy, duration: 0.35, ease: 'power2.out' });
      });
      btn.addEventListener('pointerleave', function () {
        gsap.to(btn, { x: 0, y: 0, duration: 0.7, ease: 'elastic.out(1, 0.35)' });
      });

      // Click ripple
      btn.style.position = 'relative';
      btn.style.overflow = 'hidden';
      btn.addEventListener('click', function (e) {
        var rect = btn.getBoundingClientRect();
        var ripple = document.createElement('span');
        var size = Math.max(rect.width, rect.height) * 2.5;
        ripple.style.cssText =
          'position:absolute;width:' + size + 'px;height:' + size + 'px;' +
          'border-radius:50%;background:rgba(255,255,255,0.35);pointer-events:none;z-index:1;' +
          'left:' + (e.clientX - rect.left - size / 2) + 'px;' +
          'top:' + (e.clientY - rect.top - size / 2) + 'px;';
        btn.appendChild(ripple);
        gsap.fromTo(ripple,
          { scale: 0, opacity: 1 },
          { scale: 1, opacity: 0, duration: 0.75, ease: 'power2.out', onComplete: function () { ripple.remove(); } }
        );
      });
    });
  }

  /* ================================================================
     INIT
  ================================================================ */
  function init() {
    disableLegacy();
    initLenis();
    ambientGlow();
    customCursor();
    heroEntrance();
    surgeonSection();
    categoryTiles();
    sectionHeadings();
    imageParallax();
    magneticButtons();

    ScrollTrigger.refresh();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    requestAnimationFrame(function () { requestAnimationFrame(init); });
  }
})();
