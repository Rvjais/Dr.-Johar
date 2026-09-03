/* Dr. Johar's Plastic Surgery Group — site scripts */
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
    if (header) header.classList.toggle('is-scrolled', y > 10);
    if (toTop) toTop.classList.toggle('is-visible', y > 600);
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
  if (toTop) toTop.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));

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

  /* ---------- Reveal on scroll ---------- */
  const revealEls = $$('.reveal, .reveal-stagger');
  if ('IntersectionObserver' in window && revealEls.length) {
    const io = new IntersectionObserver(entries => {
      entries.forEach(en => {
        if (en.isIntersecting) { en.target.classList.add('is-visible'); io.unobserve(en.target); }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    revealEls.forEach(el => io.observe(el));
  } else {
    revealEls.forEach(el => el.classList.add('is-visible'));
  }

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
    items.forEach((item, i) => {
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
        if (acc.dataset.single !== 'false') items.forEach(x => { if (x !== item) { x.classList.remove('is-open'); $('.acc__panel', x).style.maxHeight = '0px'; } });
        setOpen(!isOpen);
      });
      if (item.classList.contains('is-open')) setOpen(true);
    });
    window.addEventListener('resize', () => items.forEach(x => { if (x.classList.contains('is-open')) $('.acc__panel', x).style.maxHeight = $('.acc__panel', x).scrollHeight + 'px'; }));
  });

  /* ---------- Sliders (testimonials etc.) ---------- */
  $$('[data-slider]').forEach(wrap => {
    const track = $('.testi-track, [data-track]', wrap);
    if (!track) return;
    const prev = $('[data-prev]', wrap);
    const next = $('[data-next]', wrap);
    const step = () => (track.firstElementChild ? track.firstElementChild.getBoundingClientRect().width + 24 : 300);
    if (prev) prev.addEventListener('click', () => track.scrollBy({ left: -step(), behavior: 'smooth' }));
    if (next) next.addEventListener('click', () => track.scrollBy({ left: step(), behavior: 'smooth' }));
    let timer;
    const auto = wrap.dataset.auto !== 'false';
    const start = () => { if (!auto) return; stop(); timer = setInterval(() => {
      const max = track.scrollWidth - track.clientWidth - 2;
      if (track.scrollLeft >= max) track.scrollTo({ left: 0, behavior: 'smooth' });
      else track.scrollBy({ left: step(), behavior: 'smooth' });
    }, 5000); };
    const stop = () => clearInterval(timer);
    wrap.addEventListener('mouseenter', stop);
    wrap.addEventListener('mouseleave', start);
    wrap.addEventListener('touchstart', stop, { passive: true });
    start();
  });

  /* ---------- Tabs ---------- */
  $$('[data-tabs]').forEach(tabs => {
    const btns = $$('button[data-tab]', tabs);
    const panels = $$('.tab-panel', tabs.parentElement);
    btns.forEach(b => b.addEventListener('click', () => {
      btns.forEach(x => x.classList.remove('is-active'));
      b.classList.add('is-active');
      panels.forEach(p => p.classList.toggle('is-active', p.dataset.panel === b.dataset.tab));
    }));
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

  /* ---------- Forms → WhatsApp / mail ---------- */
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

      const title = form.dataset.form || 'Website Enquiry';
      const lines = ['*' + title + '* — theaesthetic.in'];
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

  /* ---------- Newsletter (demo) ---------- */
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

  /* ---------- Marquee duplicate for seamless loop ---------- */
  $$('.marquee__track').forEach(t => { if (!t.dataset.dup) { t.innerHTML += t.innerHTML; t.dataset.dup = '1'; } });

  /* ---------- Treatment search / filter ---------- */
  const search = $('[data-treatment-search]');
  if (search) {
    const items = $$('[data-treatment-item]');
    const empty = $('[data-treatment-empty]');
    search.addEventListener('input', () => {
      const q = search.value.trim().toLowerCase();
      let n = 0;
      items.forEach(it => { const show = !q || it.dataset.treatmentItem.includes(q); it.style.display = show ? '' : 'none'; if (show) n++; });
      if (empty) empty.style.display = n ? 'none' : 'block';
    });
  }

  /* ---------- Interactive Animated Cards: 3D Tilt & Micro-interactions ---------- */
  const cards = $$('.post-card, .loc-card, .cat-tile, .tcard');
  cards.forEach(card => {
    card.addEventListener('mousemove', e => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      const cx = rect.width / 2;
      const cy = rect.height / 2;
      const rx = ((y - cy) / cy) * -3.5;
      const ry = ((x - cx) / cx) * 3.5;
      card.style.transform = `perspective(800px) rotateX(${rx.toFixed(2)}deg) rotateY(${ry.toFixed(2)}deg) translateY(-8px) scale(1.015)`;
    });
    card.addEventListener('mouseleave', () => {
      card.style.transform = '';
    });
  });
})();
