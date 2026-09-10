/* Kratam Studio — page-specific interactions */
(function () {
  'use strict';

  const $ = (selector, context = document) => context.querySelector(selector);
  const $$ = (selector, context = document) => Array.from(context.querySelectorAll(selector));
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');

  /* Accessible editorial tabs used by treatment discovery and locations. */
  $$('[data-studio-tabs]').forEach((tabs, groupIndex) => {
    const buttons = $$('[data-studio-tab]', tabs);
    const scope = tabs.closest('section') || tabs.parentElement;
    const panels = $$('[data-studio-panel]', scope);
    if (!buttons.length || !panels.length) return;

    tabs.setAttribute('role', 'tablist');

    const activate = (button, focusPanel) => {
      const target = button.dataset.studioTab;
      buttons.forEach((item) => {
        const active = item === button;
        item.classList.toggle('is-active', active);
        item.setAttribute('aria-selected', String(active));
        item.tabIndex = active ? 0 : -1;
      });
      panels.forEach((panel) => {
        const active = panel.dataset.studioPanel === target;
        panel.classList.toggle('is-active', active);
        panel.hidden = !active;
        if (active && focusPanel) panel.focus({ preventScroll: true });
      });
    };

    buttons.forEach((button, index) => {
      const panel = panels.find((item) => item.dataset.studioPanel === button.dataset.studioTab);
      const tabId = `studio-tab-${groupIndex}-${index}`;
      button.id = button.id || tabId;
      button.setAttribute('role', 'tab');
      if (panel) {
        panel.id = panel.id || `studio-panel-${groupIndex}-${index}`;
        panel.setAttribute('role', 'tabpanel');
        panel.setAttribute('aria-labelledby', button.id);
        panel.tabIndex = -1;
        button.setAttribute('aria-controls', panel.id);
      }
      button.addEventListener('click', () => activate(button, false));
      button.addEventListener('keydown', (event) => {
        const keys = ['ArrowLeft', 'ArrowRight', 'Home', 'End'];
        if (!keys.includes(event.key)) return;
        event.preventDefault();
        let next = index;
        if (event.key === 'ArrowLeft') next = (index - 1 + buttons.length) % buttons.length;
        if (event.key === 'ArrowRight') next = (index + 1) % buttons.length;
        if (event.key === 'Home') next = 0;
        if (event.key === 'End') next = buttons.length - 1;
        buttons[next].focus();
        activate(buttons[next], false);
      });
    });

    activate(buttons.find((button) => button.classList.contains('is-active')) || buttons[0], false);
  });

  /* Keep native FAQ controls simple, exclusive and keyboard-friendly. */
  $$('.native-faq').forEach((faq) => {
    $$('details', faq).forEach((item) => {
      item.addEventListener('toggle', () => {
        if (!item.open) return;
        $$('details[open]', faq).forEach((other) => {
          if (other !== item) other.open = false;
        });
      });
    });
  });

  /* Upgrade the treatment directory with useful category filters. */
  const treatmentSearch = $('[data-treatment-search]');
  if (treatmentSearch) {
    const section = treatmentSearch.closest('section');
    const cards = $$('[data-treatment-item]', section || document);
    const grid = cards[0] && cards[0].parentElement;
    const searchWrap = treatmentSearch.closest('.search') || treatmentSearch.parentElement;

    if (cards.length && grid && searchWrap) {
      const controls = document.createElement('div');
      controls.className = 'treatment-filters';
      controls.setAttribute('aria-label', 'Filter treatment type');
      const count = document.createElement('span');
      count.className = 'treatment-count';
      controls.insertAdjacentHTML('beforeend', [
        '<button type="button" data-kind="all" aria-pressed="true">All treatments</button>',
        '<button type="button" data-kind="surgical" aria-pressed="false">Surgical</button>',
        '<button type="button" data-kind="non-surgical" aria-pressed="false">Non-surgical</button>'
      ].join(''));
      controls.appendChild(count);
      searchWrap.insertAdjacentElement('afterend', controls);

      let activeKind = 'all';
      const render = () => {
        const query = treatmentSearch.value.trim().toLowerCase();
        let visible = 0;
        cards.forEach((card) => {
          const text = card.dataset.treatmentItem.toLowerCase();
          const kindMatches = activeKind === 'all' || (
            activeKind === 'non-surgical'
              ? text.includes('non-surgical')
              : text.includes('surgical') && !text.includes('non-surgical')
          );
          const show = kindMatches && (!query || text.includes(query));
          card.hidden = !show;
          card.style.display = show ? '' : 'none';
          if (show) visible += 1;
        });
        count.textContent = `${visible} ${visible === 1 ? 'treatment' : 'treatments'}`;
        const empty = $('[data-treatment-empty]');
        if (empty) empty.style.display = visible ? 'none' : 'block';
      };

      $$('button[data-kind]', controls).forEach((button) => {
        button.addEventListener('click', () => {
          activeKind = button.dataset.kind;
          $$('button[data-kind]', controls).forEach((item) => {
            item.setAttribute('aria-pressed', String(item === button));
          });
          render();
        });
      });
      treatmentSearch.addEventListener('input', render);
      render();
    }
  }

  /* Add context to request forms without altering their submitted fields. */
  $$('form[data-form]').forEach((form) => {
    const panel = form.closest('.form-panel');
    if (!panel || $('.booking-intro', panel)) return;
    const intro = document.createElement('div');
    intro.className = 'booking-intro';
    intro.innerHTML = '<span class="eyebrow">Private enquiry</span><h2>Start with a conversation.</h2><p>Share what you are considering. A member of the care team will respond personally to guide the next step.</p>';
    panel.insertBefore(intro, form);
  });

  /* Subtle depth on the opening photograph; movement never blocks scrolling. */
  const hero = $('.studio-hero');
  const heroPhoto = $('.hero-photograph', hero || document);
  if (hero && heroPhoto && window.matchMedia('(hover: hover) and (pointer: fine)').matches) {
    let frame = 0;
    hero.addEventListener('pointermove', (event) => {
      if (reducedMotion.matches || document.documentElement.classList.contains('motion-paused')) return;
      if (frame) cancelAnimationFrame(frame);
      frame = requestAnimationFrame(() => {
        const rect = hero.getBoundingClientRect();
        const x = ((event.clientX - rect.left) / rect.width - 0.5) * 8;
        const y = ((event.clientY - rect.top) / rect.height - 0.5) * 5;
        heroPhoto.style.setProperty('--photo-x', `${x}px`);
        heroPhoto.style.setProperty('--photo-y', `${y}px`);
      });
    });
    hero.addEventListener('pointerleave', () => {
      heroPhoto.style.removeProperty('--photo-x');
      heroPhoto.style.removeProperty('--photo-y');
    });
  }
})();
