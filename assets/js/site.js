/* Aces Haven — small progressive enhancements. Everything works without JS. */
(function () {
  const root = document.documentElement;
  root.classList.add('js');
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  window.addEventListener('load', () => root.classList.add('loaded'));
  setTimeout(() => root.classList.add('loaded'), 1200); // never wait on slow images

  /* Header background once scrolled */
  const header = document.querySelector('.site-header');
  const onScroll = () => header && header.classList.toggle('scrolled', window.scrollY > 20);
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  /* Mobile menu */
  const menuBtn = document.querySelector('.menu-btn');
  if (menuBtn) {
    const setMenu = (open) => {
      root.classList.toggle('menu-open', open);
      menuBtn.setAttribute('aria-expanded', String(open));
      menuBtn.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    };
    menuBtn.addEventListener('click', () => setMenu(!root.classList.contains('menu-open')));
    document.addEventListener('keydown', (e) => { if (e.key === 'Escape') setMenu(false); });
    document.querySelectorAll('.mobile-menu a').forEach((a) => a.addEventListener('click', () => setMenu(false)));
  }

  /* Reveal on scroll */
  const reveals = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && !reduce) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((en) => { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    reveals.forEach((el) => io.observe(el));
  } else {
    reveals.forEach((el) => el.classList.add('in'));
  }

  /* Stay filters */
  const chips = document.querySelectorAll('[data-filter]');
  chips.forEach((chip) => chip.addEventListener('click', () => {
    const f = chip.dataset.filter;
    chips.forEach((c) => c.setAttribute('aria-pressed', String(c === chip)));
    const grid = document.querySelector('.stays');
    if (grid) grid.classList.toggle('featured', f === 'all');
    document.querySelectorAll('.stay[data-beds]').forEach((card) => {
      card.hidden = !(f === 'all' || card.dataset.beds === f);
    });
  }));

  /* Review rotator */
  const reviews = document.querySelectorAll('.review');
  const dots = document.querySelectorAll('.review-dots button');
  if (reviews.length > 1) {
    let i = 0, timer;
    const show = (n) => {
      i = (n + reviews.length) % reviews.length;
      reviews.forEach((r, k) => { r.classList.toggle('active', k === i); r.setAttribute('aria-hidden', String(k !== i)); });
      dots.forEach((d, k) => {
        d.removeAttribute('aria-current');
        if (k === i) { void d.offsetWidth; d.setAttribute('aria-current', 'true'); }
      });
      clearTimeout(timer);
      if (!reduce) timer = setTimeout(() => show(i + 1), 7000);
    };
    dots.forEach((d, k) => d.addEventListener('click', () => show(k)));
    const stage = document.querySelector('.review-stage');
    if (stage) {
      stage.addEventListener('mouseenter', () => clearTimeout(timer));
      stage.addEventListener('mouseleave', () => show(i));
    }
    show(0);
  }

  /* Gallery lightbox */
  const lb = document.querySelector('.lightbox');
  const shots = Array.from(document.querySelectorAll('[data-full]'));
  if (lb && shots.length && typeof lb.showModal === 'function') {
    const img = lb.querySelector('.lb-stage img');
    const count = lb.querySelector('.lb-count');
    let cur = 0;
    const open = (n) => {
      cur = (n + shots.length) % shots.length;
      const s = shots[cur];
      img.src = s.dataset.full;
      img.alt = s.querySelector('img').alt;
      count.textContent = (cur + 1) + ' / ' + shots.length;
      if (!lb.open) lb.showModal();
    };
    shots.forEach((s, k) => s.addEventListener('click', () => open(k)));
    lb.querySelector('[data-lb="prev"]').addEventListener('click', () => open(cur - 1));
    lb.querySelector('[data-lb="next"]').addEventListener('click', () => open(cur + 1));
    lb.querySelector('[data-lb="close"]').addEventListener('click', () => lb.close());
    lb.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowLeft') open(cur - 1);
      if (e.key === 'ArrowRight') open(cur + 1);
    });
    lb.addEventListener('click', (e) => { if (e.target === lb || e.target.classList.contains('lb-stage')) lb.close(); });
    let x0 = null;
    lb.addEventListener('touchstart', (e) => { x0 = e.touches[0].clientX; }, { passive: true });
    lb.addEventListener('touchend', (e) => {
      if (x0 === null) return;
      const dx = e.changedTouches[0].clientX - x0;
      if (Math.abs(dx) > 50) open(cur + (dx < 0 ? 1 : -1));
      x0 = null;
    });
  }

  /* Sticky mobile booking bar on property pages */
  const bar = document.querySelector('.book-bar');
  const card = document.querySelector('.book-card');
  if (bar && card && 'IntersectionObserver' in window) {
    const gallery = document.querySelector('.gallery');
    let pastGallery = false, cardVisible = false;
    const update = () => bar.classList.toggle('show', pastGallery && !cardVisible);
    new IntersectionObserver(([en]) => { pastGallery = !en.isIntersecting && en.boundingClientRect.top < 0; update(); }).observe(gallery);
    new IntersectionObserver(([en]) => { cardVisible = en.isIntersecting; update(); }).observe(card);
  }

  /* Explore page: highlight the section in view */
  const navLinks = document.querySelectorAll('.explore-nav a');
  if (navLinks.length && 'IntersectionObserver' in window) {
    const map = new Map();
    navLinks.forEach((a) => { const t = document.querySelector(a.getAttribute('href')); if (t) map.set(t, a); });
    const io = new IntersectionObserver((entries) => {
      entries.forEach((en) => {
        if (en.isIntersecting) {
          navLinks.forEach((a) => a.classList.remove('active'));
          const a = map.get(en.target);
          a.classList.add('active');
          a.scrollIntoView({ block: 'nearest', inline: 'center', behavior: reduce ? 'auto' : 'smooth' });
        }
      });
    }, { rootMargin: '-45% 0px -50% 0px' });
    map.forEach((_, sec) => io.observe(sec));
  }

  /* Contact form: compose an email in the visitor's mail app (no server needed) */
  const form = document.querySelector('#enquiry');
  if (form) {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const d = new FormData(form);
      const lines = [
        'Name: ' + d.get('name'),
        'Email: ' + d.get('email'),
        d.get('phone') ? 'Phone: ' + d.get('phone') : '',
        'Haven: ' + d.get('haven'),
        d.get('checkin') ? 'Dates: ' + d.get('checkin') + ' to ' + (d.get('checkout') || '?') : '',
        d.get('guests') ? 'Guests: ' + d.get('guests') : '',
        '',
        d.get('message') || ''
      ].filter((l, k) => l !== '' || k === 6);
      const subject = 'Enquiry: ' + d.get('haven');
      window.location.href = 'mailto:' + form.dataset.to +
        '?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(lines.join('\n'));
    });
  }
})();
