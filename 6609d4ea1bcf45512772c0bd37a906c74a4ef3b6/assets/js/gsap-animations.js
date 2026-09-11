/**
 * Kratam Hospital – GSAP Premium Animation Engine (Ivory & Champagne Gold)
 * Comprehensive, high-end animation system featuring:
 * - Lenis smooth inertia scroll
 * - Dynamic scroll progress line
 * - Marquee scroll velocity acceleration
 * - Hero sequence with rotating rings and "Beauty" background text parallax
 * - Split-line typography mask reveals with champagne shimmer
 * - 3D Category tiles with specular glare tracking
 * - Dual dark section reveals with alternating treatment links
 * - 3D Team cards with perspective tilt and photo zoom
 * - Magnetic video play button with radar pulse
 * - Sequential golden star twinkle on testimonials
 * - Location cards 3D entrance
 * - Golden particle sparkle explosion on button click
 * - Custom champagne magnetic follower cursor
 * - Ambient drifting champagne glow orbs
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
      el.classList.add('is-visible');
      el.classList.remove('reveal', 'reveal-stagger');
    });
    var hv = document.querySelector('.hero__visual');
    if (hv) hv.classList.add('is-visible');
    var dv = document.querySelector('.doc-visual');
    if (dv) dv.classList.add('is-visible');
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
     1. SCROLL PROGRESS BAR (GOLD GLOW)
  ================================================================ */
  function scrollProgressBar() {
    var bar = document.createElement('div');
    bar.className = 'scroll-progress-line';
    document.body.appendChild(bar);

    gsap.to(bar, {
      scaleX: 1,
      ease: 'none',
      scrollTrigger: {
        trigger: document.body,
        start: 'top top',
        end: 'bottom bottom',
        scrub: 0.3
      }
    });
  }

  /* ================================================================
     2. HERO CINEMATIC ENTRANCE
  ================================================================ */
  function heroEntrance() {
    var hero = document.querySelector('.hero');
    if (!hero) return;

    var tl = gsap.timeline({ defaults: { ease: 'power4.out' } });

    // Background watermark "Beauty" scrub parallax
    var bgText = hero.querySelector('.hero__bg-text');
    if (bgText) {
      gsap.to(bgText, {
        xPercent: 30,
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
        var raw = countEl.getAttribute('data-count');
        var target = parseFloat(raw);
        if (isNaN(target)) return;
        var suffix = countEl.getAttribute('data-suffix') || '';
        countEl.textContent = '0' + suffix;
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
    var heroVisual = hero.querySelector('.hero__visual');
    if (heroVisual) {
      heroVisual.classList.add('is-visible');
    }

    var heroFrame = hero.querySelector('.hero__frame');
    if (heroFrame) {
      gsap.set(heroFrame, { opacity: 0, scale: 0.94, y: 25 });
      tl.to(heroFrame, {
        opacity: 1, scale: 1, y: 0, duration: 1.4, ease: 'power3.out'
      }, 0.2);
    }

    var frameImg = hero.querySelector('.hero__frame img');
    if (frameImg) {
      gsap.set(frameImg, { scale: 1.25, filter: 'blur(8px) brightness(0.8)', opacity: 1 });
      tl.to(frameImg, {
        scale: 1, filter: 'blur(0px) brightness(1)', duration: 2.0, ease: 'power3.out'
      }, 0.3);

      gsap.to(frameImg, {
        yPercent: 15,
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
     3. MARQUEE VELOCITY ACCELERATION ON SCROLL
  ================================================================ */
  function marqueeScrollAcceleration() {
    var track = document.querySelector('.marquee__track');
    if (!track) return;

    ScrollTrigger.create({
      trigger: '.strip',
      start: 'top bottom',
      end: 'bottom top',
      onUpdate: function (self) {
        var vel = Math.abs(self.getVelocity() / 300);
        var clamped = Math.min(vel, 3);
        gsap.to(track, {
          timeScale: 1 + clamped,
          duration: 0.3,
          ease: 'power2.out',
          overwrite: 'auto'
        });
      }
    });
  }

  /* ================================================================
     4. MEET THE SURGEON SECTION
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
     5. CATEGORY TILES (3D ENTRANCE + TILT)
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
     6. DUAL DARK SHOWCASE SECTIONS (SURGICAL / NON-SURGICAL)
  ================================================================ */
  function darkShowcaseSections() {
    var darkSec = document.querySelector('section.bg-ink');
    if (!darkSec) return;

    // Splits inside the dark section
    var splits = darkSec.querySelectorAll('.split');
    splits.forEach(function (sp, i) {
      var textSide = sp.querySelector('div:first-child');
      var visualSide = sp.querySelector('.page-hero__visual');

      if (textSide) {
        var listItems = textSide.querySelectorAll('.mega__list a');
        if (listItems.length) {
          gsap.from(listItems, {
            x: i % 2 === 0 ? -30 : 30,
            opacity: 0,
            duration: 0.7,
            stagger: 0.06,
            ease: 'power3.out',
            scrollTrigger: st(sp, 'top 75%')
          });
        }
      }

      if (visualSide) {
        var img = visualSide.querySelector('img');
        if (img) {
          gsap.set(visualSide, { clipPath: 'inset(0 100% 0 0)' });
          gsap.to(visualSide, {
            clipPath: 'inset(0 0% 0 0)',
            duration: 1.3,
            ease: 'power4.inOut',
            scrollTrigger: st(sp, 'top 78%')
          });

          gsap.to(img, {
            scale: 1.1,
            yPercent: -10,
            ease: 'none',
            scrollTrigger: {
              trigger: visualSide,
              start: 'top bottom',
              end: 'bottom top',
              scrub: 0.7
            }
          });
        }
      }
    });
  }

  /* ================================================================
     7. "WHY CHOOSE" 4 CARDS 3D UNFOLD
  ================================================================ */
  function whyChooseCards() {
    var cards = document.querySelectorAll('.grid-4 .card');
    if (!cards.length) return;

    gsap.from(cards, {
      y: 70,
      opacity: 0,
      rotationX: 18,
      duration: 1.1,
      stagger: 0.15,
      ease: 'back.out(1.5)',
      scrollTrigger: st('.grid-4', 'top 78%')
    });

    cards.forEach(function (card) {
      var icon = card.querySelector('.icon-tile');
      if (icon) {
        card.addEventListener('mouseenter', function () {
          gsap.to(icon, { scale: 1.15, rotation: 6, duration: 0.35, ease: 'back.out(2)' });
        });
        card.addEventListener('mouseleave', function () {
          gsap.to(icon, { scale: 1, rotation: 0, duration: 0.6, ease: 'elastic.out(1, 0.4)' });
        });
      }
    });
  }

  /* ================================================================
     8. TEAM CARDS (5 SPECIALISTS 3D ELEVATION)
  ================================================================ */
  function teamCards() {
    var team = document.querySelectorAll('.team-card');
    if (!team.length) return;

    gsap.from(team, {
      y: 85,
      opacity: 0,
      rotationY: 15,
      duration: 1.1,
      stagger: 0.12,
      ease: 'power3.out',
      scrollTrigger: st('.grid-5', 'top 75%')
    });

    if (window.matchMedia('(hover: hover) and (pointer: fine)').matches) {
      team.forEach(function (card) {
        card.addEventListener('pointermove', function (e) {
          var rect = card.getBoundingClientRect();
          var x = (e.clientX - rect.left) / rect.width - 0.5;
          var y = (e.clientY - rect.top) / rect.height - 0.5;
          gsap.to(card, {
            rotationY: x * 12,
            rotationX: y * -12,
            y: -10,
            duration: 0.35,
            ease: 'power2.out',
            transformPerspective: 900
          });
        });

        card.addEventListener('pointerleave', function () {
          gsap.to(card, {
            rotationY: 0,
            rotationX: 0,
            y: 0,
            duration: 0.85,
            ease: 'elastic.out(1, 0.4)'
          });
        });
      });
    }
  }

  /* ================================================================
     9. VIDEO LOGS MAGNETIC PLAY BUTTON
  ================================================================ */
  function videoLogsMagneticPlay() {
    var videos = document.querySelectorAll('.video-card');
    if (!videos.length) return;

    gsap.from(videos, {
      scale: 0.9,
      opacity: 0,
      y: 50,
      duration: 1,
      stagger: 0.12,
      ease: 'power3.out',
      scrollTrigger: st('.video-card', 'top 80%')
    });

    if (!window.matchMedia('(hover: hover) and (pointer: fine)').matches) return;

    videos.forEach(function (v) {
      var playBtn = v.querySelector('.video-card__play');
      if (!playBtn) return;

      v.addEventListener('pointermove', function (e) {
        var rect = v.getBoundingClientRect();
        var cx = rect.left + rect.width / 2;
        var cy = rect.top + rect.height / 2;
        var dx = (e.clientX - cx) * 0.15;
        var dy = (e.clientY - cy) * 0.15;
        gsap.to(playBtn, { x: dx, y: dy, scale: 1.12, duration: 0.35, ease: 'power2.out' });
      });

      v.addEventListener('pointerleave', function () {
        gsap.to(playBtn, { x: 0, y: 0, scale: 1, duration: 0.7, ease: 'elastic.out(1, 0.4)' });
      });
    });
  }

  /* ================================================================
     10. TESTIMONIAL STARS TWINKLE
  ================================================================ */
  function testimonialTwinkle() {
    var testimonials = document.querySelectorAll('.testi');
    if (!testimonials.length) return;

    testimonials.forEach(function (t) {
      var stars = t.querySelectorAll('.testi__stars svg');
      if (stars.length) {
        gsap.from(stars, {
          scale: 0,
          opacity: 0,
          rotation: -45,
          duration: 0.5,
          stagger: 0.08,
          ease: 'back.out(3)',
          scrollTrigger: st(t, 'top 80%')
        });
      }
    });
  }

  /* ================================================================
     11. SECTION HEADINGS LINE REVEAL
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
     12. GENERAL IMAGE PARALLAX
  ================================================================ */
  function imageParallax() {
    var images = document.querySelectorAll('.page-hero__visual img, .cat-tile img, .cta img');
    images.forEach(function (img) {
      gsap.to(img, {
        yPercent: -12,
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
     13. CUSTOM CHAMPAGNE CURSOR
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

    var hoverSelectors = 'a, button, .btn, .cat-tile, .card, .tcard, .team-card, .video-card, input, select, textarea';
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
     14. AMBIENT GLOW ORBS
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
     15. MAGNETIC BUTTONS & GOLDEN SPARKLE BURST
  ================================================================ */
  function magneticButtons() {
    var isDesktop = window.matchMedia('(hover: hover) and (pointer: fine)').matches;

    document.querySelectorAll('.btn').forEach(function (btn) {
      if (isDesktop) {
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
      }

      // Sparkle Particle Explosion on Click
      btn.addEventListener('click', function (e) {
        var rect = btn.getBoundingClientRect();
        var x = e.clientX - rect.left;
        var y = e.clientY - rect.top;

        for (var i = 0; i < 8; i++) {
          var p = document.createElement('span');
          p.className = 'btn-sparkle';
          p.style.left = x + 'px';
          p.style.top = y + 'px';
          btn.appendChild(p);

          var angle = (Math.PI * 2 * i) / 8 + (Math.random() - 0.5);
          var dist = 25 + Math.random() * 35;
          var targetX = x + Math.cos(angle) * dist;
          var targetY = y + Math.sin(angle) * dist;

          gsap.to(p, {
            x: Math.cos(angle) * dist,
            y: Math.sin(angle) * dist,
            opacity: 0,
            scale: Math.random() * 1.5 + 0.5,
            duration: 0.6 + Math.random() * 0.3,
            ease: 'power2.out',
            onComplete: function () {
              p.remove();
            }
          });
        }
      });
    });
  }

  /* ================================================================
     INIT
  ================================================================ */
  function init() {
    disableLegacy();
    initLenis();
    scrollProgressBar();
    ambientGlow();
    customCursor();
    heroEntrance();
    marqueeScrollAcceleration();
    surgeonSection();
    categoryTiles();
    darkShowcaseSections();
    whyChooseCards();
    teamCards();
    videoLogsMagneticPlay();
    testimonialTwinkle();
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
