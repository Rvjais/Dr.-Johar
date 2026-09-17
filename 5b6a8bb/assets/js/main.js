/* Dr. Johar's Plastic Surgery Group — site scripts */
(function () {
  'use strict';

  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => Array.from(c.querySelectorAll(s));
  const WA_NUMBER = '918527778462';
  document.documentElement.classList.add('js-ready');

  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  let motionPaused = false;
  try { motionPaused = sessionStorage.getItem('kratam-motion-paused') === 'true'; } catch (_) {}
  const motionEnabled = () => !reducedMotion.matches && !motionPaused;
  const scrollBehavior = () => motionEnabled() ? 'smooth' : 'instant';
  const main = $('main');
  if (main) {
    if (!main.id) main.id = 'main-content';
    main.tabIndex = -1;
    const skip = document.createElement('a');
    skip.className = 'skip-link';
    skip.href = '#' + main.id;
    skip.textContent = 'Skip to content';
    document.body.prepend(skip);
  }
  const motionButton = document.createElement('button');
  motionButton.type = 'button';
  motionButton.className = 'motion-toggle';
  const syncMotion = () => {
    const paused = !motionEnabled();
    document.body.classList.toggle('motion-paused', paused);
    document.documentElement.classList.toggle('motion-paused', paused);
    motionButton.textContent = paused ? 'Motion off' : 'Motion on';
    motionButton.setAttribute('aria-label', paused ? 'Resume animations' : 'Pause animations');
    motionButton.setAttribute('aria-pressed', String(paused));
    if (paused) $$('.reveal, .reveal-stagger').forEach(el => el.classList.add('is-visible'));
    document.dispatchEvent(new Event('kratam:motionchange'));
  };
  motionButton.addEventListener('click', () => {
    motionPaused = !motionPaused;
    try { sessionStorage.setItem('kratam-motion-paused', String(motionPaused)); } catch (_) {}
    syncMotion();
  });
  document.body.appendChild(motionButton);
  reducedMotion.addEventListener('change', syncMotion);
  syncMotion();

  /* ---------- Header: scrolled state ---------- */
  const header = $('.header');
  const toTop = $('.to-top');
  const progress = document.createElement('div');
  progress.className = 'scroll-progress';
  progress.setAttribute('aria-hidden', 'true');
  document.body.appendChild(progress);
  let scrollPending = false;
  const onScroll = () => {
    const y = window.scrollY || document.documentElement.scrollTop;
    if (header) header.classList.toggle('is-scrolled', y > 10);
    if (toTop) toTop.classList.toggle('is-visible', y > 600);
    const distance = document.documentElement.scrollHeight - window.innerHeight;
    progress.style.transform = 'scaleX(' + (distance > 0 ? Math.min(1, Math.max(0, y / distance)) : 0) + ')';
    scrollPending = false;
  };
  window.addEventListener('scroll', () => {
    if (!scrollPending) { scrollPending = true; requestAnimationFrame(onScroll); }
  }, { passive: true });
  window.addEventListener('resize', onScroll, { passive: true });
  onScroll();
  if (toTop) toTop.addEventListener('click', () => window.scrollTo({ top: 0, behavior: scrollBehavior() }));

  /* ---------- Desktop nav: click-to-toggle (touch/keyboard) ---------- */
  const navButtons = $$('.nav > li > button');
  const setMenu = (btn, open) => {
    btn.parentElement.classList.toggle('is-open', open);
    btn.setAttribute('aria-expanded', String(open));
  };
  const closeMenus = () => navButtons.forEach(btn => setMenu(btn, false));
  navButtons.forEach((btn, index) => {
    const panel = $('.dropdown, .mega', btn.parentElement);
    if (panel) { panel.id = 'desktop-menu-' + index; btn.setAttribute('aria-controls', panel.id); }
    btn.setAttribute('aria-expanded', 'false');
    let hoverTimer;
    btn.addEventListener('click', e => {
      e.stopPropagation();
      const open = btn.parentElement.classList.contains('is-open');
      closeMenus();
      setMenu(btn, !open);
    });
    btn.parentElement.addEventListener('pointerenter', e => {
      if (e.pointerType !== 'mouse') return;
      clearTimeout(hoverTimer); closeMenus(); setMenu(btn, true);
    });
    btn.parentElement.addEventListener('pointerleave', () => {
      hoverTimer = setTimeout(() => {
        if (!btn.parentElement.contains(document.activeElement)) setMenu(btn, false);
      }, 160);
    });
    btn.parentElement.addEventListener('focusout', e => {
      if (!btn.parentElement.contains(e.relatedTarget)) setMenu(btn, false);
    });
  });
  document.addEventListener('click', e => {
    if (!e.target.closest('.nav')) closeMenus();
  });
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape') {
      const menu = $('.nav > li.is-open > button');
      closeMenus();
      if (menu) menu.focus();
      closeDrawer();
      closeLightbox();
    }
  });

  /* ---------- Mobile drawer ---------- */
  const drawer = $('.drawer');
  const navToggle = $('.nav-toggle');
  let drawerReturnFocus;
  let previousOverflow = '';
  if (drawer) {
    drawer.id = 'mobile-navigation';
    drawer.inert = true;
    const panel = $('.drawer__panel', drawer);
    panel.setAttribute('role', 'dialog');
    panel.setAttribute('aria-modal', 'true');
    panel.setAttribute('aria-label', 'Main navigation');
  }
  if (navToggle) {
    navToggle.setAttribute('aria-controls', 'mobile-navigation');
    navToggle.setAttribute('aria-expanded', 'false');
  }
  const openDrawer = () => {
    if (!drawer || drawer.classList.contains('is-open')) return;
    drawerReturnFocus = document.activeElement;
    previousOverflow = document.body.style.overflow;
    drawer.inert = false;
    drawer.classList.add('is-open');
    drawer.setAttribute('aria-hidden', 'false');
    if (navToggle) navToggle.setAttribute('aria-expanded', 'true');
    document.body.style.overflow = 'hidden';
    $('.drawer__close', drawer).focus();
  };
  const closeDrawer = () => {
    if (!drawer || !drawer.classList.contains('is-open')) return;
    drawer.classList.remove('is-open');
    document.body.style.overflow = previousOverflow;
    if (navToggle) navToggle.setAttribute('aria-expanded', 'false');
    if (drawerReturnFocus) drawerReturnFocus.focus();
    drawer.inert = true;
    drawer.setAttribute('aria-hidden', 'true');
  };
  if (navToggle) navToggle.addEventListener('click', openDrawer);
  $$('.drawer__close, .drawer__scrim').forEach(el => el.addEventListener('click', closeDrawer));
  $$('.drawer a').forEach(a => a.addEventListener('click', closeDrawer));
  if (drawer) drawer.addEventListener('keydown', e => {
    if (e.key !== 'Tab') return;
    const focusable = $$('a[href], button:not([disabled])', drawer).filter(el => el.getClientRects().length);
    const first = focusable[0], last = focusable[focusable.length - 1];
    if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
    else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
  });
  window.addEventListener('resize', () => { if (window.innerWidth > 1100) closeDrawer(); });
  $$('.drawer__nav > li > button').forEach((btn, index) => {
    btn.setAttribute('aria-expanded', 'false');
    const sub = $('.drawer__sub', btn.parentElement);
    if (sub) { sub.id = 'mobile-submenu-' + index; btn.setAttribute('aria-controls', sub.id); }
    btn.addEventListener('click', () => {
      const li = btn.parentElement;
      const open = li.classList.contains('is-open');
      $$('.drawer__nav > li.is-open').forEach(x => {
        x.classList.remove('is-open');
        $('button', x).setAttribute('aria-expanded', 'false');
      });
      if (!open) li.classList.add('is-open');
      btn.setAttribute('aria-expanded', String(!open));
    });
  });

  /* ---------- Active nav link ---------- */
  (function markActive() {
    const path = location.pathname.replace(/\/index\.html$/, '/');
    $$('.nav a, .drawer__nav a').forEach(a => {
      const href = new URL(a.href, location.href).pathname.replace(/\/index\.html$/, '/');
      if (href === path) { a.classList.add('is-active'); a.setAttribute('aria-current', 'page'); }
    });
  })();

  /* ---------- Reveal on scroll ---------- */
  $$('.section-head, .detail__content > section').forEach(el => {
    if (!el.closest('.reveal')) el.classList.add('reveal');
  });
  $$('.reveal-stagger').forEach(group => {
    group.classList.add('is-visible');
    Array.from(group.children).forEach((el, index) => {
      el.classList.add('reveal');
      el.style.setProperty('--reveal-delay', Math.min(index % 5, 3) * 65 + 'ms');
    });
  });
  const revealEls = $$('.reveal');
  if ('IntersectionObserver' in window && revealEls.length && motionEnabled()) {
    const io = new IntersectionObserver(entries => {
      entries.forEach(en => {
        if (en.isIntersecting) { en.target.classList.add('is-visible'); io.unobserve(en.target); }
      });
    }, { threshold: 0, rootMargin: '0px 0px -24px 0px' });
    revealEls.forEach(el => io.observe(el));
    document.body.classList.add('motion-ready');
  } else {
    revealEls.forEach(el => el.classList.add('is-visible'));
  }

  /* ---------- Counters ---------- */
  const counters = $$('[data-count]');
  if (typeof gsap === 'undefined' && counters.length && 'IntersectionObserver' in window && motionEnabled()) {
    const cio = new IntersectionObserver(entries => {
      entries.forEach(en => {
        if (!en.isIntersecting) return;
        const el = en.target;
        const raw = el.dataset.count;
        if (!raw) return;
        const target = parseFloat(raw);
        if (isNaN(target)) return;
        const suffix = el.dataset.suffix || '';
        const dur = 1400;
        const start = performance.now();
        const step = now => {
          const p = motionEnabled() ? Math.min(1, (now - start) / dur) : 1;
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
    items.forEach(item => {
      const btn = $('.acc__btn', item);
      const panel = $('.acc__panel', item);
      if (!btn || !panel) return;
      const panelId = 'accordion-panel-' + $$('.acc__panel').indexOf(panel);
      panel.id = panelId;
      btn.setAttribute('aria-controls', panelId);
      const setOpen = open => {
        item.classList.toggle('is-open', open);
        btn.setAttribute('aria-expanded', open ? 'true' : 'false');
        panel.style.maxHeight = open ? panel.scrollHeight + 'px' : '0px';
      };
      btn.addEventListener('click', () => {
        const isOpen = item.classList.contains('is-open');
        if (acc.dataset.single !== 'false') items.forEach(x => { if (x !== item) { x.classList.remove('is-open'); $('.acc__btn', x).setAttribute('aria-expanded', 'false'); $('.acc__panel', x).style.maxHeight = '0px'; } });
        setOpen(!isOpen);
      });
      setOpen(item.classList.contains('is-open'));
    });
    window.addEventListener('resize', () => items.forEach(x => { if (x.classList.contains('is-open')) $('.acc__panel', x).style.maxHeight = $('.acc__panel', x).scrollHeight + 'px'; }));
  });

  /* ---------- Sliders (testimonials etc.) ---------- */
  $$('[data-slider]').forEach(wrap => {
    const track = $('.testi-track, [data-track]', wrap);
    if (!track) return;
    const prev = $('[data-prev]', wrap);
    const next = $('[data-next]', wrap);
    const step = () => (track.firstElementChild ? track.firstElementChild.getBoundingClientRect().width + (parseFloat(getComputedStyle(track).columnGap) || 24) : 300);
    if (prev) prev.addEventListener('click', () => track.scrollBy({ left: -step(), behavior: scrollBehavior() }));
    if (next) next.addEventListener('click', () => track.scrollBy({ left: step(), behavior: scrollBehavior() }));
    let timer;
    const auto = wrap.dataset.auto !== 'false';
    let hovered = false;
    let touched = false;
    const start = () => { stop(); if (!auto || !motionEnabled() || document.hidden || hovered || touched || wrap.contains(document.activeElement)) return; timer = setInterval(() => {
      const max = track.scrollWidth - track.clientWidth - 2;
      if (max <= 0) return;
      if (track.scrollLeft >= max) track.scrollTo({ left: 0, behavior: scrollBehavior() });
      else track.scrollBy({ left: step(), behavior: scrollBehavior() });
    }, 6500); };
    const stop = () => clearInterval(timer);
    wrap.addEventListener('mouseenter', () => { hovered = true; stop(); });
    wrap.addEventListener('mouseleave', () => { hovered = false; start(); });
    wrap.addEventListener('touchstart', () => { touched = true; stop(); }, { passive: true });
    wrap.addEventListener('focusin', stop);
    wrap.addEventListener('focusout', () => setTimeout(start, 0));
    document.addEventListener('visibilitychange', start);
    document.addEventListener('kratam:motionchange', start);
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
  $$('.marquee__track').forEach(t => {
    if (t.dataset.dup) return;
    Array.from(t.children).forEach(child => {
      const copy = child.cloneNode(true);
      copy.setAttribute('aria-hidden', 'true');
      copy.inert = true;
      t.appendChild(copy);
    });
    t.dataset.dup = '1';
  });

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

  /* ---------- Pointer light: no image displacement or scroll hijacking ---------- */
  if (window.matchMedia('(hover: hover) and (pointer: fine)').matches) {
    const cards = $$('.card, .post-card, .loc-card, .tcard');
    cards.forEach(card => {
      let frame = 0;
      let clientX = 0, clientY = 0;
      card.addEventListener('pointermove', e => {
        if (!motionEnabled()) return;
        clientX = e.clientX; clientY = e.clientY;
        if (frame) return;
        frame = requestAnimationFrame(() => {
          const rect = card.getBoundingClientRect();
          card.style.setProperty('--glow-x', clientX - rect.left + 'px');
          card.style.setProperty('--glow-y', clientY - rect.top + 'px');
          frame = 0;
        });
      });
      card.addEventListener('pointerleave', () => {
        cancelAnimationFrame(frame); frame = 0;
        card.style.removeProperty('--glow-x');
        card.style.removeProperty('--glow-y');
      });
    });
  }
})();
