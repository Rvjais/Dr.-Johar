/**
 * Kratam Hospital – GSAP Premium Animation Engine
 * Cinematic, GSAP-powered animations with ScrollTrigger.
 * Requires: gsap.min.js + ScrollTrigger.min.js loaded before this file.
 */
(function () {
  'use strict';

  /* ── Guard ─────────────────────────────────────────────── */
  if (typeof gsap === 'undefined') {
    console.warn('[Kratam] GSAP not loaded – skipping animations');
    return;
  }
  gsap.registerPlugin(ScrollTrigger);

  const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)');
  if (prefersReduced.matches) return;

  /* ── Defaults ──────────────────────────────────────────── */
  gsap.defaults({ ease: 'power3.out', duration: 1 });
  ScrollTrigger.config({ limitCallbacks: true });

  /* ================================================================
     UTILITIES
  ================================================================ */

  /** Remove old animation systems so they don't fight GSAP */
  function disableLegacy() {
    document.querySelectorAll('.reveal, .reveal-stagger').forEach(el => {
      el.classList.remove('reveal', 'reveal-stagger', 'is-visible');
    });
    document.querySelectorAll('.hero-entry').forEach(el => {
      el.style.animation = 'none';
      el.style.opacity = '';
    });
    // Remove anim classes from previous CSS-only system
    document.querySelectorAll('[class*="anim-"]').forEach(el => {
      [...el.classList].filter(c => c.startsWith('anim-')).forEach(c => el.classList.remove(c));
    });
  }

  /**
   * Splits element innerHTML by <br> into overflow-hidden line masks.
   * Returns NodeList of .ln-inner divs for GSAP targeting.
   */
  function splitLines(el) {
    if (!el) return [];
    const html = el.innerHTML;
    const frags = html.split(/<br\s*\/?>/gi);
    el.setAttribute('aria-label', el.textContent);
    el.innerHTML = frags
      .map(f => '<div class="ln-mask" style="overflow:hidden;display:block">' +
                '<div class="ln-inner" style="display:block;will-change:transform">' +
                f.trim() + '</div></div>')
      .join('');
    return el.querySelectorAll('.ln-inner');
  }

  /** Shorthand for common ScrollTrigger config */
  function st(trigger, start) {
    return { trigger: trigger, start: start || 'top 80%', toggleActions: 'play none none reverse' };
  }

  /* ================================================================
     1. HERO – Cinematic entrance sequence
  ================================================================ */
  function heroEntrance() {
    var hero = document.querySelector('.studio-hero');
    if (!hero) return;

    var tl = gsap.timeline({ defaults: { ease: 'power4.out' } });

    /* ── Hero photograph: scale-down + de-blur ── */
    var img = hero.querySelector('.hero-photograph img');
    if (img) {
      gsap.set(img, { scale: 1.35, filter: 'blur(8px) brightness(0.65)' });
      tl.to(img, {
        scale: 1.05, filter: 'blur(0px) brightness(1)',
        duration: 2.6, ease: 'power2.out'
      }, 0);
    }

    /* ── Kicker: letter-spacing narrows ── */
    var kicker = hero.querySelector('.hero-copy > .kicker');
    if (kicker) {
      gsap.set(kicker, { opacity: 0, y: 28, letterSpacing: '0.4em' });
      tl.to(kicker, {
        opacity: 1, y: 0, letterSpacing: '0.18em', duration: 1.2
      }, 0.2);
    }

    /* ── H1: line-by-line mask reveal (THE premium effect) ── */
    var h1 = hero.querySelector('h1');
    if (h1) {
      var lines = splitLines(h1);
      gsap.set(lines, { yPercent: 120 });
      tl.to(lines, {
        yPercent: 0, duration: 1.3, stagger: 0.2, ease: 'power4.out'
      }, 0.3);
    }

    /* ── Sub-paragraph ── */
    var para = hero.querySelector('.hero-copy > p:not([class])');
    if (para) {
      gsap.set(para, { opacity: 0, y: 35 });
      tl.to(para, { opacity: 1, y: 0, duration: 1 }, 0.9);
    }

    /* ── CTA buttons: spring pop-in ── */
    var btns = hero.querySelectorAll('.hero-links > a');
    if (btns.length) {
      gsap.set(btns, { opacity: 0, y: 22, scale: 0.88 });
      tl.to(btns, {
        opacity: 1, y: 0, scale: 1,
        duration: 0.85, stagger: 0.14, ease: 'back.out(2.5)'
      }, 1.15);
    }

    /* ── Seal: elastic spin-in ── */
    var seal = hero.querySelector('.hero-seal');
    if (seal) {
      gsap.set(seal, { opacity: 0, scale: 0, rotation: -200 });
      tl.to(seal, {
        opacity: 1, scale: 1, rotation: 0,
        duration: 1.8, ease: 'elastic.out(1, 0.4)'
      }, 0.65);

      // Continuous slow rotation on the SVG text
      var sealSvg = seal.querySelector('svg');
      if (sealSvg) {
        gsap.to(sealSvg, {
          rotation: 360, duration: 28, ease: 'none',
          repeat: -1, transformOrigin: '50% 50%'
        });
      }
    }

    /* ── Doctor card: perspective slide ── */
    var docCard = hero.querySelector('.hero-doctor-card');
    if (docCard) {
      gsap.set(docCard, { opacity: 0, x: 60, rotationY: 15 });
      tl.to(docCard, {
        opacity: 1, x: 0, rotationY: 0, duration: 1.2
      }, 0.95);
    }

    /* ── Footnote ── */
    var fn = hero.querySelector('.hero-footnote');
    if (fn) {
      gsap.set(fn, { opacity: 0, x: -30 });
      tl.to(fn, { opacity: 1, x: 0, duration: 0.9 }, 1.25);
    }

    /* ── Hero caption ── */
    var caption = hero.querySelector('.hero-caption');
    if (caption) {
      gsap.set(caption, { opacity: 0 });
      tl.to(caption, { opacity: 1, duration: 1.4 }, 1.6);
    }

    /* ── Scroll: hero image parallax ── */
    if (img) {
      gsap.to(img, {
        yPercent: 20, ease: 'none',
        scrollTrigger: {
          trigger: hero, start: 'top top', end: 'bottom top', scrub: 0.8
        }
      });
    }

    /* ── Continuous Ken Burns on hero image ── */
    if (img) {
      gsap.to(img, { scale: 1, duration: 25, ease: 'none', delay: 2.6 });
    }
  }

  /* ================================================================
     2. PRACTICE FACTS – Counter with flair
  ================================================================ */
  function practiceFacts() {
    var section = document.querySelector('.practice-facts');
    if (!section) return;

    var tagline = section.querySelector('.container > p');
    var statDivs = section.querySelectorAll('.container > div');
    var counters = section.querySelectorAll('[data-count]');

    if (tagline) {
      gsap.from(tagline, {
        y: 55, opacity: 0, duration: 1.1,
        scrollTrigger: st(section, 'top 82%')
      });
    }

    if (statDivs.length) {
      gsap.from(statDivs, {
        y: 80, opacity: 0, scale: 0.82, duration: 1.1,
        stagger: 0.2, ease: 'back.out(1.6)',
        scrollTrigger: st(section, 'top 75%')
      });
    }

    counters.forEach(function (el) {
      var target = parseInt(el.getAttribute('data-count'), 10);
      el.removeAttribute('data-count'); // prevent old counter in main.js
      var proxy = { v: 0 };

      ScrollTrigger.create({
        trigger: el, start: 'top 82%',
        onEnter: function () {
          gsap.to(proxy, {
            v: target, duration: 2.4, ease: 'power2.out',
            onUpdate: function () { el.textContent = Math.round(proxy.v); },
            onComplete: function () {
              gsap.fromTo(el,
                { scale: 1 },
                { scale: 1.3, duration: 0.3, yoyo: true, repeat: 1, ease: 'power2.inOut' }
              );
            }
          });
        },
        once: true
      });
    });
  }

  /* ================================================================
     3. SECTION HEADINGS – Line-by-line reveal (global)
  ================================================================ */
  function sectionHeadings() {
    document.querySelectorAll('.studio-heading').forEach(function (heading) {
      var h2 = heading.querySelector('h2');
      if (h2) {
        var lines = splitLines(h2);
        gsap.set(lines, { yPercent: 110 });
        gsap.to(lines, {
          yPercent: 0, duration: 1.2, stagger: 0.18,
          ease: 'power4.out',
          scrollTrigger: st(heading, 'top 82%')
        });
      }

      var kick = heading.querySelector('.kicker');
      if (kick) {
        gsap.from(kick, {
          y: 22, opacity: 0, duration: 0.9,
          scrollTrigger: st(heading, 'top 85%')
        });
      }

      var p = heading.querySelector('p');
      if (p) {
        gsap.from(p, {
          y: 28, opacity: 0, duration: 1, delay: 0.25,
          scrollTrigger: st(heading, 'top 82%')
        });
      }

      var link = heading.querySelector('.text-link');
      if (link) {
        gsap.from(link, {
          y: 16, opacity: 0, duration: 0.8, delay: 0.45,
          scrollTrigger: st(heading, 'top 82%')
        });
      }
    });
  }

  /* ================================================================
     4. DISCOVERY – Tabs section
  ================================================================ */
  function discovery() {
    var section = document.querySelector('.discovery');
    if (!section) return;

    var tabBtns = section.querySelectorAll('.tab-buttons button');
    if (tabBtns.length) {
      gsap.from(tabBtns, {
        y: 35, opacity: 0, duration: 0.8,
        stagger: 0.1, ease: 'power3.out',
        scrollTrigger: st(section, 'top 72%')
      });
    }

    // Active panel content slide
    var activePanel = section.querySelector('.discovery-panel.is-active');
    if (activePanel) {
      var content = activePanel.querySelector('.discovery-content');
      if (content) {
        gsap.from(content, {
          x: 70, opacity: 0, duration: 1.1,
          scrollTrigger: st(section, 'top 65%')
        });
      }
      var dImg = activePanel.querySelector('.discovery-image');
      if (dImg) {
        gsap.set(dImg, { clipPath: 'inset(0 100% 0 0)' });
        gsap.to(dImg, {
          clipPath: 'inset(0 0% 0 0)', duration: 1.4,
          ease: 'power4.inOut',
          scrollTrigger: st(section, 'top 68%')
        });
      }
    }

    // Image parallax on all discovery images
    section.querySelectorAll('.discovery-image img').forEach(function (img) {
      gsap.to(img, {
        yPercent: -10, ease: 'none',
        scrollTrigger: {
          trigger: img.closest('.discovery-panel') || section,
          start: 'top bottom', end: 'bottom top', scrub: 0.6
        }
      });
    });
  }

  /* ================================================================
     5. SURGEON STORY – Split-screen dramatic reveal
  ================================================================ */
  function surgeonStory() {
    var section = document.querySelector('.surgeon-story');
    if (!section) return;

    /* Portrait – horizontal clip-path wipe (left to right) */
    var portrait = section.querySelector('.surgeon-portrait');
    if (portrait) {
      gsap.set(portrait, { clipPath: 'inset(0 100% 0 0)' });
      gsap.to(portrait, {
        clipPath: 'inset(0 0% 0 0)', duration: 1.5,
        ease: 'power4.inOut',
        scrollTrigger: st(section, 'top 72%')
      });

      var pImg = portrait.querySelector('img');
      if (pImg) {
        // Parallax
        gsap.to(pImg, {
          yPercent: -12, ease: 'none',
          scrollTrigger: {
            trigger: section, start: 'top bottom',
            end: 'bottom top', scrub: 0.8
          }
        });
      }

      var cap = portrait.querySelector('.portrait-caption');
      if (cap) {
        gsap.from(cap, {
          y: 25, opacity: 0, duration: 0.9, delay: 0.8,
          scrollTrigger: st(section, 'top 72%')
        });
      }

      var marker = portrait.querySelector('.portrait-marker');
      if (marker) {
        gsap.from(marker, {
          scale: 0, opacity: 0, duration: 0.7, delay: 1.1,
          ease: 'back.out(4)',
          scrollTrigger: st(section, 'top 72%')
        });
      }
    }

    /* Copy – slide from right */
    var copy = section.querySelector('.surgeon-copy');
    if (copy) {
      var intro = copy.querySelector('.surgeon-intro');
      if (intro) {
        gsap.from(intro, {
          x: 55, opacity: 0, duration: 1.1,
          scrollTrigger: st(copy, 'top 78%')
        });
      }

      copy.querySelectorAll('p:not(.surgeon-intro)').forEach(function (p, i) {
        gsap.from(p, {
          x: 45, opacity: 0, duration: 1, delay: 0.12 * i,
          scrollTrigger: st(copy, 'top 78%')
        });
      });

      var principles = copy.querySelectorAll('.surgeon-principles > div');
      if (principles.length) {
        gsap.from(principles, {
          x: 45, opacity: 0, duration: 0.75, stagger: 0.12,
          ease: 'power3.out',
          scrollTrigger: st(copy, 'top 62%')
        });
      }

      var copyBtns = copy.querySelectorAll('.btn, .surgeon-signature');
      if (copyBtns.length) {
        gsap.from(copyBtns, {
          y: 22, opacity: 0, scale: 0.93, duration: 0.8,
          stagger: 0.12, ease: 'back.out(1.7)',
          scrollTrigger: st(copy, 'top 58%')
        });
      }
    }
  }

  /* ================================================================
     6. CARE JOURNEY – 3D staggered cards
  ================================================================ */
  function careJourney() {
    var section = document.querySelector('.care-journey');
    if (!section) return;

    var cards = section.querySelectorAll('.journey-grid article');
    if (cards.length) {
      gsap.from(cards, {
        y: 90, opacity: 0, rotationX: 15, scale: 0.88,
        duration: 1.1, stagger: 0.22, ease: 'power3.out',
        scrollTrigger: st(section, 'top 72%')
      });
    }

    var numbers = section.querySelectorAll('.journey-number');
    if (numbers.length) {
      gsap.from(numbers, {
        scale: 0, duration: 0.7, stagger: 0.18,
        ease: 'elastic.out(1, 0.35)',
        scrollTrigger: st(section, 'top 68%')
      });
    }
  }

  /* ================================================================
     7. SPECIALISTS – Dramatic card entrance with 3D
  ================================================================ */
  function specialists() {
    var section = document.querySelector('.specialists');
    if (!section) return;

    /* Watermark parallax */
    var watermark = section.querySelector('.specialists-watermark');
    if (watermark) {
      gsap.to(watermark, {
        xPercent: -20, ease: 'none',
        scrollTrigger: {
          trigger: section, start: 'top bottom',
          end: 'bottom top', scrub: 0.5
        }
      });
    }

    /* Cards – 3D rotation + scale entrance */
    var cards = section.querySelectorAll('.specialist-card');
    if (cards.length) {
      gsap.from(cards, {
        y: 110, opacity: 0, rotationY: 18, rotationX: 6, scale: 0.85,
        duration: 1.2, stagger: { each: 0.18, from: 'start' },
        ease: 'power3.out',
        scrollTrigger: st(section, 'top 74%')
      });
    }

    /* Hover image zoom */
    cards.forEach(function (card) {
      var cImg = card.querySelector('img');
      if (!cImg) return;
      card.addEventListener('mouseenter', function () {
        gsap.to(cImg, { scale: 1.1, duration: 0.7, ease: 'power2.out' });
      });
      card.addEventListener('mouseleave', function () {
        gsap.to(cImg, { scale: 1, duration: 0.7, ease: 'power2.out' });
      });
    });
  }

  /* ================================================================
     8. PATIENT STORIES
  ================================================================ */
  function patientStories() {
    var section = document.querySelector('.stories');
    if (!section) return;

    var glyph = section.querySelector('.quote-glyph');
    if (glyph) {
      gsap.from(glyph, {
        scale: 0, opacity: 0, rotation: -20, duration: 1.2,
        ease: 'elastic.out(1, 0.3)',
        scrollTrigger: st(section, 'top 76%')
      });
    }

    var quote = section.querySelector('blockquote');
    if (quote) {
      gsap.from(quote, {
        y: 35, opacity: 0, duration: 1.1, delay: 0.25,
        scrollTrigger: st(section, 'top 76%')
      });
    }

    var figcaption = section.querySelector('figcaption');
    if (figcaption) {
      gsap.from(figcaption, {
        y: 20, opacity: 0, duration: 0.9, delay: 0.5,
        scrollTrigger: st(section, 'top 76%')
      });
    }

    var video = section.querySelector('.story-video');
    if (video) {
      gsap.from(video, {
        x: 90, opacity: 0, rotationY: -10, duration: 1.3,
        ease: 'power3.out',
        scrollTrigger: st(section, 'top 74%')
      });
    }
  }

  /* ================================================================
     9. JOURNAL
  ================================================================ */
  function journalSection() {
    var section = document.querySelector('.journal');
    if (!section) return;

    var feature = section.querySelector('.journal-feature');
    if (feature) {
      gsap.set(feature, { clipPath: 'inset(0 100% 0 0)' });
      gsap.to(feature, {
        clipPath: 'inset(0 0% 0 0)', duration: 1.3,
        ease: 'power4.inOut',
        scrollTrigger: st(section, 'top 72%')
      });
    }

    var sides = section.querySelectorAll('.journal-side > a');
    if (sides.length) {
      gsap.from(sides, {
        x: 70, opacity: 0, duration: 1,
        stagger: 0.2, ease: 'power3.out',
        scrollTrigger: st(section, 'top 68%')
      });
    }

    // Image parallax
    section.querySelectorAll('.journal-image img, .journal-side img').forEach(function (jImg) {
      gsap.to(jImg, {
        yPercent: -12, ease: 'none',
        scrollTrigger: {
          trigger: jImg, start: 'top bottom',
          end: 'bottom top', scrub: 0.5
        }
      });
    });
  }

  /* ================================================================
     10. FAQ
  ================================================================ */
  function faqSection() {
    var section = document.querySelector('.studio-faq');
    if (!section) return;

    // Left column elements
    var leftCol = section.querySelector('.faq-layout > div:first-child');
    if (leftCol) {
      var kick = leftCol.querySelector('.kicker');
      if (kick) {
        gsap.from(kick, {
          y: 22, opacity: 0, duration: 0.9,
          scrollTrigger: st(section, 'top 82%')
        });
      }
      var h2 = leftCol.querySelector('h2');
      if (h2) {
        var lines = splitLines(h2);
        gsap.set(lines, { yPercent: 110 });
        gsap.to(lines, {
          yPercent: 0, duration: 1.2, stagger: 0.16,
          ease: 'power4.out',
          scrollTrigger: st(section, 'top 80%')
        });
      }
      var lp = leftCol.querySelector('p');
      if (lp) {
        gsap.from(lp, {
          y: 25, opacity: 0, duration: 0.9, delay: 0.3,
          scrollTrigger: st(section, 'top 80%')
        });
      }
    }

    // FAQ items cascade
    var details = section.querySelectorAll('.native-faq details');
    if (details.length) {
      gsap.from(details, {
        y: 35, opacity: 0, duration: 0.8,
        stagger: 0.1, ease: 'power3.out',
        scrollTrigger: st(section.querySelector('.native-faq'), 'top 80%')
      });
    }
  }

  /* ================================================================
     11. LOCATIONS
  ================================================================ */
  function locationsSection() {
    var section = document.querySelector('.locations-section');
    if (!section) return;

    var explorer = section.querySelector('.location-explorer');
    if (explorer) {
      gsap.from(explorer, {
        y: 65, opacity: 0, duration: 1.2,
        ease: 'power3.out',
        scrollTrigger: st(section, 'top 74%')
      });
    }

    var photo = section.querySelector('.location-photo');
    if (photo) {
      gsap.set(photo, { clipPath: 'inset(100% 0 0 0)' });
      gsap.to(photo, {
        clipPath: 'inset(0% 0 0 0)', duration: 1.4,
        ease: 'power4.inOut',
        scrollTrigger: st(photo, 'top 80%')
      });

      var locImg = photo.querySelector('img');
      if (locImg) {
        gsap.to(locImg, {
          yPercent: -14, ease: 'none',
          scrollTrigger: {
            trigger: photo, start: 'top bottom',
            end: 'bottom top', scrub: 0.7
          }
        });
      }
    }
  }

  /* ================================================================
     12. CONSULTATION CTA – Dramatic entrance
  ================================================================ */
  function consultationCTA() {
    var section = document.querySelector('.consultation-invitation');
    if (!section) return;

    var kick = section.querySelector('.kicker');
    if (kick) {
      gsap.from(kick, {
        y: 24, opacity: 0, duration: 0.9,
        scrollTrigger: st(section, 'top 82%')
      });
    }

    var h2 = section.querySelector('h2');
    if (h2) {
      var lines = splitLines(h2);
      gsap.set(lines, { yPercent: 115 });
      gsap.to(lines, {
        yPercent: 0, duration: 1.3, stagger: 0.18,
        ease: 'power4.out',
        scrollTrigger: st(section, 'top 78%')
      });
    }

    var para = section.querySelector('p');
    if (para) {
      gsap.from(para, {
        y: 28, opacity: 0, duration: 1, delay: 0.3,
        scrollTrigger: st(section, 'top 78%')
      });
    }

    var ctaBtns = section.querySelectorAll('.btn, .text-link');
    if (ctaBtns.length) {
      gsap.from(ctaBtns, {
        y: 22, opacity: 0, scale: 0.9, duration: 0.85,
        stagger: 0.14, ease: 'back.out(2)',
        scrollTrigger: st(section, 'top 72%')
      });
    }

    // Flower – continuous rotation + elastic entrance
    var flower = section.querySelector('.invitation-flower');
    if (flower) {
      gsap.from(flower, {
        scale: 0, opacity: 0, rotation: -90, duration: 1.2,
        ease: 'elastic.out(1, 0.45)',
        scrollTrigger: st(section, 'top 76%')
      });
      gsap.to(flower, {
        rotation: 360, duration: 18, ease: 'none', repeat: -1
      });
    }
  }

  /* ================================================================
     13. FOOTER – Stagger entrance
  ================================================================ */
  function footerSection() {
    var ft = document.querySelector('.studio-footer');
    if (!ft) return;

    var opening = ft.querySelector('.footer-opening');
    if (opening) {
      gsap.from(opening, {
        y: 45, opacity: 0, duration: 1.1,
        scrollTrigger: st(ft, 'top 86%')
      });

      var orb = opening.querySelector('.footer-orb');
      if (orb) {
        gsap.from(orb, {
          scale: 0, rotation: -120, duration: 1.2, delay: 0.3,
          ease: 'elastic.out(1, 0.45)',
          scrollTrigger: st(ft, 'top 86%')
        });
      }
    }

    var cols = ft.querySelectorAll('.footer__top > div');
    if (cols.length) {
      gsap.from(cols, {
        y: 55, opacity: 0, duration: 1,
        stagger: 0.14,
        scrollTrigger: st(ft, 'top 82%')
      });
    }
  }

  /* ================================================================
     14. MAGNETIC BUTTONS – Cursor-following effect
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
    });
  }

  /* ================================================================
     15. 3D CARD TILT – Perspective hover effect
  ================================================================ */
  function cardTilt() {
    if (!window.matchMedia('(hover: hover) and (pointer: fine)').matches) return;

    var tiltTargets = document.querySelectorAll(
      '.specialist-card, .journey-grid article, .journal-feature, .story-video'
    );

    tiltTargets.forEach(function (card) {
      card.addEventListener('pointermove', function (e) {
        var rect = card.getBoundingClientRect();
        var x = (e.clientX - rect.left) / rect.width - 0.5;
        var y = (e.clientY - rect.top) / rect.height - 0.5;
        gsap.to(card, {
          rotationY: x * 10, rotationX: y * -10,
          duration: 0.4, ease: 'power2.out',
          transformPerspective: 800
        });
      });
      card.addEventListener('pointerleave', function () {
        gsap.to(card, {
          rotationY: 0, rotationX: 0,
          duration: 0.9, ease: 'elastic.out(1, 0.45)'
        });
      });
    });
  }

  /* ================================================================
     16. RIPPLE EFFECT – Click feedback on buttons
  ================================================================ */
  function rippleEffect() {
    document.querySelectorAll('.btn').forEach(function (btn) {
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
          { scale: 1, opacity: 0, duration: 0.75, ease: 'power2.out',
            onComplete: function () { ripple.remove(); }
          }
        );
      });
    });
  }

  /* ================================================================
     17. FLOATING ELEMENTS – Gentle ambient motion
  ================================================================ */
  function floatingElements() {
    document.querySelectorAll('.small-cross, .portrait-marker').forEach(function (el, i) {
      gsap.to(el, {
        y: -7, duration: 2.2 + i * 0.6,
        yoyo: true, repeat: -1, ease: 'sine.inOut'
      });
    });

    var wa = document.querySelector('.float-wa');
    if (wa) {
      gsap.to(wa, {
        y: -5, duration: 2.8,
        yoyo: true, repeat: -1, ease: 'sine.inOut'
      });
    }
  }

  /* ================================================================
     18. SMOOTH HEADER – Progressive backdrop blur on scroll
  ================================================================ */
  function smoothHeader() {
    var header = document.querySelector('.studio-header');
    if (!header) return;

    ScrollTrigger.create({
      start: 0, end: 200,
      onUpdate: function (self) {
        var progress = self.progress;
        var blur = Math.round(progress * 12);
        var bg = 'rgba(41,38,46,' + (progress * 0.85).toFixed(2) + ')';
        header.style.backdropFilter = 'blur(' + blur + 'px)';
        header.style.webkitBackdropFilter = 'blur(' + blur + 'px)';
        header.style.backgroundColor = bg;
      }
    });
  }

  /* ================================================================
     19. GENERAL PARALLAX – Images throughout the site
  ================================================================ */
  function generalParallax() {
    var parallaxTargets = document.querySelectorAll(
      '.location-photo img, .story-video img'
    );

    parallaxTargets.forEach(function (el) {
      // Skip if already has a ScrollTrigger from section-specific code
      if (el.dataset.parallaxDone) return;
      el.dataset.parallaxDone = '1';

      gsap.to(el, {
        yPercent: -10, ease: 'none',
        scrollTrigger: {
          trigger: el, start: 'top bottom',
          end: 'bottom top', scrub: 0.6
        }
      });
    });
  }

  /* ================================================================
     20. SCRUBBED TEXT SCALE on Consultation Section
         Text scales down from larger as user scrolls through
  ================================================================ */
  function scrubbedCTA() {
    var section = document.querySelector('.consultation-invitation');
    if (!section) return;

    // Scale the entire container content with scrub for a cinematic feel
    gsap.fromTo(section.querySelector('.container'), 
      { scale: 0.92, opacity: 0.7 },
      {
        scale: 1, opacity: 1, ease: 'none',
        scrollTrigger: {
          trigger: section,
          start: 'top 90%',
          end: 'top 40%',
          scrub: 0.5
        }
      }
    );
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
     21. LUXURY CUSTOM MAGNETIC CURSOR
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

    var hoverSelectors = 'a, button, .btn, .specialist-card, .journey-grid article, .journal-feature, .story-video, input, select, textarea, [role="tab"], summary';
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
     22. AMBIENT GLOWING DEPTH ORBS
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
        y: '45vh',
        x: '15vw',
        ease: 'none',
        scrollTrigger: {
          trigger: document.body,
          start: 'top top',
          end: 'bottom bottom',
          scrub: 1.2
        }
      });
    }

    if (orb2) {
      gsap.to(orb2, {
        y: '-35vh',
        x: '-12vw',
        ease: 'none',
        scrollTrigger: {
          trigger: document.body,
          start: 'top top',
          end: 'bottom bottom',
          scrub: 1.5
        }
      });
    }
  }

  /* ================================================================
     23. CARD SPECULAR HIGHLIGHT
  ================================================================ */
  function cardSpecular() {
    if (!window.matchMedia('(hover: hover) and (pointer: fine)').matches) return;
    var cards = document.querySelectorAll('.specialist-card, .journey-grid article, .journal-feature');
    cards.forEach(function (card) {
      if (!card.querySelector('.card-specular-shine')) {
        var shine = document.createElement('div');
        shine.className = 'card-specular-shine';
        card.appendChild(shine);
      }
      card.addEventListener('pointermove', function (e) {
        var rect = card.getBoundingClientRect();
        var x = e.clientX - rect.left;
        var y = e.clientY - rect.top;
        card.style.setProperty('--shine-x', x + 'px');
        card.style.setProperty('--shine-y', y + 'px');
      }, { passive: true });
    });
  }

  /* ================================================================
     INIT – Orchestrate everything
  ================================================================ */
  function init() {
    disableLegacy();

    // Smooth inertia scroll
    initLenis();

    // Ambient luxury background
    ambientGlow();

    // Custom interactive cursor
    customCursor();

    // Core section animations
    heroEntrance();
    practiceFacts();
    sectionHeadings();
    discovery();
    surgeonStory();
    careJourney();
    specialists();
    patientStories();
    journalSection();
    faqSection();
    locationsSection();
    consultationCTA();
    footerSection();

    // Effects & micro-interactions
    magneticButtons();
    cardTilt();
    cardSpecular();
    rippleEffect();
    floatingElements();
    smoothHeader();
    generalParallax();
    scrubbedCTA();

    // Refresh after setup
    ScrollTrigger.refresh();
  }

  /* ── Boot ── */
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    requestAnimationFrame(function () { requestAnimationFrame(init); });
  }
})();
