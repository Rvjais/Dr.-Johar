/* Dr. Johar's Plastic Surgery Group — Healthcare & Hospital Site Scripts */
(function () {
  'use strict';

  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => Array.from(c.querySelectorAll(s));
  const WA_NUMBER = '918527778462';

  /* ---------- Header: scrolled state ---------- */
  const header = $('.header');
  const toTop = $('.to-top');
  const onScroll = () => {
    const y = window.scrollY || document.documentElement.scrollTop;
    if (header) header.classList.toggle('is-scrolled', y > 15);
    if (toTop) toTop.classList.toggle('is-visible', y > 500);
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
  if (toTop) toTop.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));

  /* ---------- Hero Banner Carousel ---------- */
  const heroSlider = $('.hero-slider');
  if (heroSlider) {
    const slides = $$('.hero-slide', heroSlider);
    const dots = $$('.hero-slider__dot', heroSlider);
    const prevBtn = $('.hero-slider__btn--prev', heroSlider);
    const nextBtn = $('.hero-slider__btn--next', heroSlider);
    let current = 0;
    let timer = null;
    const intervalTime = 6000;

    const showSlide = (index) => {
      if (index < 0) index = slides.length - 1;
      if (index >= slides.length) index = 0;
      current = index;

      slides.forEach((s, i) => s.classList.toggle('is-active', i === current));
      dots.forEach((d, i) => d.classList.toggle('is-active', i === current));
    };

    const nextSlide = () => showSlide(current + 1);
    const prevSlide = () => showSlide(current - 1);

    const startAutoplay = () => {
      stopAutoplay();
      timer = setInterval(nextSlide, intervalTime);
    };

    const stopAutoplay = () => {
      if (timer) clearInterval(timer);
    };

    if (nextBtn) nextBtn.addEventListener('click', () => { nextSlide(); startAutoplay(); });
    if (prevBtn) prevBtn.addEventListener('click', () => { prevSlide(); startAutoplay(); });

    dots.forEach((dot, idx) => {
      dot.addEventListener('click', () => {
        showSlide(idx);
        startAutoplay();
      });
    });

    heroSlider.addEventListener('mouseenter', stopAutoplay);
    heroSlider.addEventListener('mouseleave', startAutoplay);

    // Touch swipe for Hero Banner
    let touchStartX = 0;
    let touchEndX = 0;
    heroSlider.addEventListener('touchstart', (e) => {
      touchStartX = e.changedTouches[0].screenX;
      stopAutoplay();
    }, { passive: true });
    heroSlider.addEventListener('touchend', (e) => {
      touchEndX = e.changedTouches[0].screenX;
      if (touchStartX - touchEndX > 50) nextSlide();
      else if (touchEndX - touchStartX > 50) prevSlide();
      startAutoplay();
    }, { passive: true });

    startAutoplay();
  }

  /* ---------- Desktop nav: click-to-toggle (touch/keyboard) ---------- */
  $$('.nav > li > button').forEach(btn => {
    btn.addEventListener('click', e => {
      e.stopPropagation();
      const li = btn.parentElement;
      const open = li.classList.contains('is-open');
      $$('.nav > li.is-open').forEach(x => x.classList.remove('is-open'));
      if (!open) li.classList.add('is-open');
    });
  });
  document.addEventListener('click', e => {
    if (!e.target.closest('.nav')) $$('.nav > li.is-open').forEach(x => x.classList.remove('is-open'));
  });
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape') {
      $$('.nav > li.is-open').forEach(x => x.classList.remove('is-open'));
      closeDrawer();
      closeLightbox();
    }
  });

  /* ---------- Mobile drawer ---------- */
  const drawer = $('.drawer');
  const openDrawer = () => { if (drawer) { drawer.classList.add('is-open'); document.body.style.overflow = 'hidden'; } };
  const closeDrawer = () => { if (drawer) { drawer.classList.remove('is-open'); document.body.style.overflow = ''; } };
  const navToggle = $('.nav-toggle');
  if (navToggle) navToggle.addEventListener('click', openDrawer);
  $$('.drawer__close, .drawer__scrim').forEach(el => el.addEventListener('click', closeDrawer));
  $$('.drawer__nav > li > button').forEach(btn => {
    btn.addEventListener('click', () => {
      const li = btn.parentElement;
      const open = li.classList.contains('is-open');
      $$('.drawer__nav > li.is-open').forEach(x => x.classList.remove('is-open'));
      if (!open) li.classList.add('is-open');
    });
  });

  /* ---------- Active nav link ---------- */
  (function markActive() {
    const path = location.pathname.replace(/\/index\.html$/, '/').split('/').filter(Boolean);
    const file = path[path.length - 1] || 'index.html';
    $$('.nav > li > a, .drawer__nav > li > a').forEach(a => {
      const href = (a.getAttribute('href') || '').split('/').pop();
      if (href && href === file) a.classList.add('is-active');
    });
  })();

  /* ---------- Counters ---------- */
  const counters = $$('[data-count]');
  if (counters.length && 'IntersectionObserver' in window) {
    const cio = new IntersectionObserver(entries => {
      entries.forEach(en => {
        if (!en.isIntersecting) return;
        const el = en.target;
        const target = parseFloat(el.dataset.count);
        const suffix = el.dataset.suffix || '';
        const dur = 1400;
        const start = performance.now();
        const step = now => {
          const p = Math.min(1, (now - start) / dur);
          const eased = 1 - Math.pow(1 - p, 3);
          el.textContent = Math.round(target * eased).toLocaleString('en-IN') + suffix;
          if (p < 1) requestAnimationFrame(step);
        };
        requestAnimationFrame(step);
        cio.unobserve(el);
      });
    }, { threshold: 0.5 });
    counters.forEach(el => cio.observe(el));
  }

  /* ---------- Accordions ---------- */
  $$('.accordion').forEach(acc => {
    const items = $$('.acc', acc);
    items.forEach((item) => {
      const btn = $('.acc__btn', item);
      const panel = $('.acc__panel', item);
      if (!btn || !panel) return;
      const setOpen = open => {
        item.classList.toggle('is-open', open);
        btn.setAttribute('aria-expanded', open ? 'true' : 'false');
        panel.style.maxHeight = open ? panel.scrollHeight + 'px' : '0px';
      };
      btn.addEventListener('click', () => {
        const isOpen = item.classList.contains('is-open');
        if (acc.dataset.single !== 'false') items.forEach(x => { if (x !== item) { x.classList.remove('is-open'); const p = $('.acc__panel', x); if (p) p.style.maxHeight = '0px'; } });
        setOpen(!isOpen);
      });
      if (item.classList.contains('is-open')) setOpen(true);
    });
    window.addEventListener('resize', () => items.forEach(x => { if (x.classList.contains('is-open')) { const p = $('.acc__panel', x); if (p) p.style.maxHeight = p.scrollHeight + 'px'; } }));
  });

  /* ---------- Sliders (testimonials etc.) ---------- */
  $$('[data-slider]').forEach(wrap => {
    const track = $('.testi-track, [data-track]', wrap);
    if (!track) return;
    const parent = wrap.closest('section') || wrap.parentElement;
    const prev = $('[data-prev]', wrap) || $('[data-prev]', parent);
    const next = $('[data-next]', wrap) || $('[data-next]', parent);
    const step = () => (track.firstElementChild ? track.firstElementChild.getBoundingClientRect().width + 20 : 320);
    if (prev) prev.addEventListener('click', () => track.scrollBy({ left: -step(), behavior: 'smooth' }));
    if (next) next.addEventListener('click', () => track.scrollBy({ left: step(), behavior: 'smooth' }));
    let timer;
    const auto = wrap.dataset.auto !== 'false';
    const start = () => { if (!auto) return; stop(); timer = setInterval(() => {
      const max = track.scrollWidth - track.clientWidth - 2;
      if (track.scrollLeft >= max) track.scrollTo({ left: 0, behavior: 'smooth' });
      else track.scrollBy({ left: step(), behavior: 'smooth' });
    }, 5500); };
    const stop = () => clearInterval(timer);
    wrap.addEventListener('mouseenter', stop);
    wrap.addEventListener('mouseleave', start);
    wrap.addEventListener('touchstart', stop, { passive: true });
    start();
  });

  /* ---------- Lightbox ---------- */
  let lightbox = $('.lightbox');
  const closeLightbox = () => { if (lightbox) lightbox.classList.remove('is-open'); };
  $$('[data-lightbox]').forEach(a => {
    a.addEventListener('click', e => {
      e.preventDefault();
      if (!lightbox) {
        lightbox = document.createElement('div');
        lightbox.className = 'lightbox';
        lightbox.innerHTML = '<button class="lightbox__close" aria-label="Close"><svg class="icon" viewBox="0 0 24 24"><path d="M6 6l12 12M18 6L6 18"/></svg></button><img alt=""><div class="lightbox__cap"></div>';
        document.body.appendChild(lightbox);
        lightbox.addEventListener('click', e2 => { if (e2.target === lightbox || e2.target.closest('.lightbox__close')) closeLightbox(); });
      }
      $('img', lightbox).src = a.getAttribute('href');
      $('.lightbox__cap', lightbox).textContent = a.dataset.caption || '';
      lightbox.classList.add('is-open');
    });
  });

  /* ---------- WhatsApp Consultation Quick Form ---------- */
  $$('form[data-form]').forEach(form => {
    form.addEventListener('submit', e => {
      e.preventDefault();
      let valid = true;
      $$('.field', form).forEach(f => f.classList.remove('is-invalid'));
      $$('[required]', form).forEach(inp => {
        if (!inp.value.trim() || (inp.type === 'email' && !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(inp.value)) || (inp.type === 'tel' && inp.value.replace(/\D/g, '').length < 10)) {
          valid = false;
          const f = inp.closest('.field'); if (f) f.classList.add('is-invalid');
        }
      });
      if (!valid) { const first = $('.is-invalid input, .is-invalid select, .is-invalid textarea', form); if (first) first.focus(); return; }

      const title = form.dataset.form || 'Doctor Consultation Request';
      const lines = ['*' + title + '* — Dr. Johar Plastic Surgery Group (theaesthetic.in)'];
      $$('input, select, textarea', form).forEach(inp => {
        if (!inp.name || inp.type === 'submit' || inp.type === 'file') return;
        if ((inp.type === 'radio' || inp.type === 'checkbox') && !inp.checked) return;
        if (inp.value.trim()) lines.push('*' + (inp.dataset.label || inp.name) + ':* ' + inp.value.trim());
      });
      const msg = encodeURIComponent(lines.join('\n'));
      const success = $('.form-success', form.parentElement) || $('.form-success', form);
      if (success) success.classList.add('is-visible');
      window.open('https://api.whatsapp.com/send?phone=' + WA_NUMBER + '&text=' + msg, '_blank', 'noopener');
      form.reset();
    });
  });

  /* ---------- Newsletter ---------- */
  $$('form.newsletter').forEach(f => f.addEventListener('submit', e => {
    e.preventDefault();
    const inp = $('input', f);
    if (!inp || !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(inp.value)) { inp && inp.focus(); return; }
    const btn = $('button', f);
    if (btn) { btn.textContent = 'Subscribed ✓'; btn.disabled = true; }
    inp.value = '';
  }));

  /* ---------- Current year ---------- */
  $$('[data-year]').forEach(el => el.textContent = new Date().getFullYear());
})();
