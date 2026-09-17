/* ============================================================
   KRTAM Skin Clinic — Comprehensive GSAP Animation Engine
   ============================================================ */

document.addEventListener('DOMContentLoaded', () => {
  // Check if GSAP and ScrollTrigger are loaded
  if (typeof gsap === 'undefined' || typeof ScrollTrigger === 'undefined') {
    console.warn('GSAP or ScrollTrigger not loaded');
    return;
  }

  gsap.registerPlugin(ScrollTrigger);

  const isReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (isReducedMotion) return;

  // 1. HEADER ENTRANCE
  gsap.from('.site-header', {
    y: -40,
    opacity: 0,
    duration: 1.2,
    ease: 'power3.out'
  });

  // 2. HERO SECTION ENTRANCE (Orchestrated Timeline)
  const heroTL = gsap.timeline({ delay: 0.2 });

  heroTL
    .from('.hero__tag', {
      x: -30,
      opacity: 0,
      duration: 0.8,
      ease: 'power3.out'
    })
    .from('.hero__title', {
      y: 50,
      opacity: 0,
      duration: 1.1,
      ease: 'power4.out'
    }, '-=0.5')
    .from('.hero__subtitle', {
      y: 30,
      opacity: 0,
      duration: 0.9,
      ease: 'power3.out'
    }, '-=0.6')
    .from('.hero__buttons a', {
      y: 25,
      opacity: 0,
      stagger: 0.12,
      duration: 0.8,
      ease: 'back.out(1.5)'
    }, '-=0.5')
    .from('.hero__quote-box', {
      x: 40,
      opacity: 0,
      duration: 1,
      ease: 'power3.out'
    }, '-=0.7')
    .from('.hero__badge', {
      y: 20,
      opacity: 0,
      stagger: 0.08,
      duration: 0.8,
      ease: 'power3.out'
    }, '-=0.5');

  // Hero Background Parallax
  gsap.to('.hero', {
    scrollTrigger: {
      trigger: '.hero',
      start: 'top top',
      end: 'bottom top',
      scrub: 1.5
    },
    backgroundPositionY: '30%',
    ease: 'none'
  });

  // Floating Hero Quote
  gsap.to('.hero__quote-box', {
    y: -10,
    duration: 3,
    repeat: -1,
    yoyo: true,
    ease: 'sine.inOut'
  });

  // 3. PHILOSOPHY SECTION REVEAL
  gsap.from('.philosophy__content > *', {
    scrollTrigger: {
      trigger: '.philosophy',
      start: 'top 75%',
      toggleActions: 'play none none none'
    },
    y: 40,
    opacity: 0,
    stagger: 0.15,
    duration: 1,
    ease: 'power3.out'
  });

  gsap.to('.philosophy', {
    scrollTrigger: {
      trigger: '.philosophy',
      start: 'top bottom',
      end: 'bottom top',
      scrub: 1.2
    },
    backgroundPositionY: '60%',
    ease: 'none'
  });

  // 4. SERVICES GRID STAGGER REVEAL + 3D CARDS
  gsap.from('.services__header > *', {
    scrollTrigger: {
      trigger: '.services',
      start: 'top 80%'
    },
    y: 35,
    opacity: 0,
    stagger: 0.15,
    duration: 0.9,
    ease: 'power3.out'
  });

  gsap.from('.service-card', {
    scrollTrigger: {
      trigger: '.services__grid',
      start: 'top 82%'
    },
    y: 60,
    opacity: 0,
    scale: 0.92,
    stagger: 0.08,
    duration: 0.9,
    ease: 'power3.out'
  });

  // Service Card 3D Tilt Effect
  document.querySelectorAll('.service-card').forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left - rect.width / 2;
      const y = e.clientY - rect.top - rect.height / 2;
      gsap.to(card, {
        rotateY: x * 0.08,
        rotateX: -y * 0.08,
        transformPerspective: 800,
        scale: 1.04,
        duration: 0.3,
        ease: 'power2.out'
      });
    });
    card.addEventListener('mouseleave', () => {
      gsap.to(card, {
        rotateX: 0,
        rotateY: 0,
        scale: 1,
        duration: 0.6,
        ease: 'power3.out'
      });
    });
  });

  // 5. RECONSTRUCTIVE SECTION
  gsap.from('.reconstructive__content > *', {
    scrollTrigger: {
      trigger: '.reconstructive',
      start: 'top 75%'
    },
    y: 40,
    opacity: 0,
    stagger: 0.15,
    duration: 1,
    ease: 'power3.out'
  });

  gsap.to('.reconstructive', {
    scrollTrigger: {
      trigger: '.reconstructive',
      start: 'top bottom',
      end: 'bottom top',
      scrub: 1.2
    },
    backgroundPositionY: '60%',
    ease: 'none'
  });

  // 6. MEET THE EXPERT
  const expertTL = gsap.timeline({
    scrollTrigger: {
      trigger: '.expert',
      start: 'top 75%'
    }
  });

  expertTL
    .from('.expert__portrait > img', {
      x: -50,
      opacity: 0,
      scale: 0.95,
      duration: 1.1,
      ease: 'power3.out'
    })
    .from('.expert__badge', {
      scale: 0,
      opacity: 0,
      duration: 0.7,
      ease: 'back.out(2)'
    }, '-=0.5')
    .from('.expert__info > *', {
      y: 30,
      opacity: 0,
      stagger: 0.1,
      duration: 0.8,
      ease: 'power3.out'
    }, '-=0.6')
    .from('.expert__quote', {
      x: 40,
      opacity: 0,
      duration: 0.9,
      ease: 'power3.out'
    }, '-=0.6');

  // 7. STATS BAR COUNTER ANIMATION
  ScrollTrigger.create({
    trigger: '.stats',
    start: 'top 85%',
    onEnter: () => {
      document.querySelectorAll('.stat__number').forEach(stat => {
        const text = stat.textContent.trim();
        const match = text.match(/(\d[\d,]*)/);
        if (match) {
          const target = parseInt(match[0].replace(/,/g, ''), 10);
          const suffix = text.replace(match[0], '');
          const obj = { val: 0 };
          gsap.to(obj, {
            val: target,
            duration: 2,
            ease: 'power2.out',
            onUpdate: () => {
              stat.textContent = Math.floor(obj.val).toLocaleString() + suffix;
            }
          });
        }
      });
    },
    once: true
  });

  gsap.from('.stat', {
    scrollTrigger: {
      trigger: '.stats',
      start: 'top 85%'
    },
    y: 30,
    opacity: 0,
    stagger: 0.1,
    duration: 0.8,
    ease: 'power3.out'
  });

  // 8. TEAM SECTION (Natural image, no cropping, smooth reveal)
  gsap.from('.team__sidebar > *', {
    scrollTrigger: {
      trigger: '.team',
      start: 'top 75%'
    },
    y: 35,
    opacity: 0,
    stagger: 0.12,
    duration: 0.9,
    ease: 'power3.out'
  });

  gsap.from('.team__photo', {
    scrollTrigger: {
      trigger: '.team',
      start: 'top 75%'
    },
    scale: 0.94,
    opacity: 0,
    duration: 1.2,
    ease: 'power3.out'
  });

  // 9. PATIENT STORIES REVEAL & HOVER TILT
  gsap.from('.stories__sidebar > *', {
    scrollTrigger: {
      trigger: '.stories',
      start: 'top 75%'
    },
    y: 35,
    opacity: 0,
    stagger: 0.12,
    duration: 0.9,
    ease: 'power3.out'
  });

  gsap.from('.story-card', {
    scrollTrigger: {
      trigger: '.stories__grid',
      start: 'top 80%'
    },
    y: 45,
    opacity: 0,
    stagger: 0.12,
    duration: 0.9,
    ease: 'power3.out'
  });

  // Story card 3D tilt
  document.querySelectorAll('.story-card').forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left - rect.width / 2;
      const y = e.clientY - rect.top - rect.height / 2;
      gsap.to(card, {
        rotateY: x * 0.06,
        rotateX: -y * 0.06,
        transformPerspective: 800,
        scale: 1.03,
        duration: 0.3,
        ease: 'power2.out'
      });
    });
    card.addEventListener('mouseleave', () => {
      gsap.to(card, {
        rotateX: 0,
        rotateY: 0,
        scale: 1,
        duration: 0.6,
        ease: 'power3.out'
      });
    });
  });

  // 10. HOSPITAL LOCATIONS REVEAL
  gsap.from('.locations__sidebar > *', {
    scrollTrigger: {
      trigger: '.locations',
      start: 'top 75%'
    },
    y: 35,
    opacity: 0,
    stagger: 0.12,
    duration: 0.9,
    ease: 'power3.out'
  });

  gsap.from('.location-card', {
    scrollTrigger: {
      trigger: '.locations__grid',
      start: 'top 80%'
    },
    y: 45,
    opacity: 0,
    stagger: 0.12,
    duration: 0.9,
    ease: 'power3.out'
  });

  // Location card hover lift
  document.querySelectorAll('.location-card').forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left - rect.width / 2;
      const y = e.clientY - rect.top - rect.height / 2;
      gsap.to(card, {
        rotateY: x * 0.05,
        rotateX: -y * 0.05,
        transformPerspective: 800,
        scale: 1.03,
        duration: 0.3,
        ease: 'power2.out'
      });
    });
    card.addEventListener('mouseleave', () => {
      gsap.to(card, {
        rotateX: 0,
        rotateY: 0,
        scale: 1,
        duration: 0.6,
        ease: 'power3.out'
      });
    });
  });

  // 11. DARK CTA BANNER REVEAL
  gsap.from('.cta-banner__container > *', {
    scrollTrigger: {
      trigger: '.cta-banner',
      start: 'top 75%'
    },
    y: 35,
    opacity: 0,
    stagger: 0.12,
    duration: 1,
    ease: 'power3.out'
  });

  // Floating script "A Brighter You"
  gsap.to('.cta-banner__script', {
    y: -8,
    duration: 2.8,
    repeat: -1,
    yoyo: true,
    ease: 'sine.inOut'
  });

  // 12. MAGNETIC BUTTONS (Micro-interactions for luxury feel)
  document.querySelectorAll('.btn, .btn-outline-box, .site-header__cta, .stories__arrow').forEach(btn => {
    btn.addEventListener('mousemove', (e) => {
      const rect = btn.getBoundingClientRect();
      const x = e.clientX - rect.left - rect.width / 2;
      const y = e.clientY - rect.top - rect.height / 2;
      gsap.to(btn, {
        x: x * 0.25,
        y: y * 0.25,
        duration: 0.25,
        ease: 'power2.out'
      });
    });
    btn.addEventListener('mouseleave', () => {
      gsap.to(btn, {
        x: 0,
        y: 0,
        duration: 0.5,
        ease: 'elastic.out(1, 0.4)'
      });
    });
  });

  // 13. VERTICAL TEXT SUBTLE FLOAT
  gsap.utils.toArray('.vertical-text').forEach(vt => {
    gsap.to(vt, {
      y: -6,
      duration: 3.5,
      repeat: -1,
      yoyo: true,
      ease: 'sine.inOut'
    });
  });
});

