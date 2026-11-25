(() => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const fine = matchMedia('(hover:hover) and (pointer:fine)').matches;
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const body = document.body;

  /* ---------- split headings into words ---------- */
  $$('[data-split]').forEach(el => {
    const walk = (node) => {
      [...node.childNodes].forEach(n => {
        if (n.nodeType === 3) {
          const frag = document.createDocumentFragment();
          n.textContent.split(/(\s+)/).forEach(t => {
            if (!t) return;
            if (/^\s+$/.test(t)) { frag.appendChild(document.createTextNode(' ')); return; }
            const o = document.createElement('span'); o.className = 'split-l'; o.style.display = 'inline-block';
            const i = document.createElement('span'); i.textContent = t; o.appendChild(i); frag.appendChild(o);
          });
          n.replaceWith(frag);
        } else if (n.nodeType === 1 && !n.classList.contains('split-l')) walk(n);
      });
    };
    walk(el);
    $$('.split-l>span', el).forEach((s, i) => s.style.transitionDelay = (i * 0.05) + 's');
    el.classList.add('rv-split');
  });

  /* ---------- big footer name letters ---------- */
  $$('.big-name').forEach(el => {
    const t = el.textContent.trim(); el.textContent = '';
    [...t].forEach((c, i) => { const s = document.createElement('span'); s.textContent = c === ' ' ? ' ' : c; s.style.setProperty('--i', i); el.appendChild(s); });
  });

  /* ---------- preloader (first visit per session) ---------- */
  const loader = $('.loader');
  const start = () => { body.classList.remove('loading'); requestAnimationFrame(() => body.classList.add('is-in')); };
  let seen = false;
  try { seen = sessionStorage.getItem('sa-seen') === '1'; sessionStorage.setItem('sa-seen', '1'); } catch (e) {}
  if (loader && !reduce && !seen) {
    body.classList.add('loading');
    const c = $('.l-count', loader), bar = $('.l-bar', loader);
    let v = 0; const t0 = performance.now(), dur = 1500;
    const tick = (t) => {
      const p = Math.min(1, (t - t0) / dur); v = Math.round(100 * (1 - Math.pow(1 - p, 3)));
      c.textContent = String(v).padStart(3, '0'); bar.style.width = v + '%';
      if (p < 1) requestAnimationFrame(tick);
      else setTimeout(() => { loader.classList.add('done'); setTimeout(start, 250); setTimeout(() => loader.remove(), 1200); }, 200);
    };
    requestAnimationFrame(tick);
  } else { loader && loader.remove(); start(); }

  /* ---------- nav ---------- */
  const nav = $('.nav'); let lastY = scrollY;
  const prog = $('.progress');
  const onScroll = () => {
    const y = scrollY;
    nav && nav.classList.toggle('scrolled', y > 10);
    if (nav && !body.classList.contains('menu-open')) nav.classList.toggle('hide', y > lastY && y > 400);
    lastY = y;
    if (prog) { const h = document.documentElement.scrollHeight - innerHeight; prog.style.transform = `scaleX(${h > 0 ? y / h : 0})`; }
  };
  addEventListener('scroll', onScroll, { passive: true }); onScroll();
  const burger = $('.burger');
  burger && burger.addEventListener('click', () => {
    const open = body.classList.toggle('menu-open');
    burger.setAttribute('aria-expanded', open);
  });

  /* ---------- reveal on scroll ---------- */
  const io = new IntersectionObserver((es) => es.forEach(e => {
    if (e.isIntersecting) { e.target.classList.add('in'); $$('.split-l', e.target).forEach(s => s.classList.add('in')); io.unobserve(e.target); }
  }), { threshold: 0.12, rootMargin: '0px 0px -60px 0px' });
  $$('.rv, .rv-split, .reveal-img, .tl-item, .big-name').forEach(el => io.observe(el));

  /* ---------- counters ---------- */
  const cio = new IntersectionObserver((es) => es.forEach(e => {
    if (!e.isIntersecting) return;
    const el = e.target, to = parseFloat(el.dataset.to), dec = (el.dataset.to.split('.')[1] || '').length;
    cio.unobserve(el);
    if (reduce) { el.textContent = to.toFixed(dec); return; }
    const t0 = performance.now(), dur = 1800;
    const tick = (t) => {
      const p = Math.min(1, (t - t0) / dur), v = to * (1 - Math.pow(1 - p, 4));
      el.textContent = v.toFixed(dec);
      if (p < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  }), { threshold: 0.5 });
  $$('[data-to]').forEach(el => cio.observe(el));

  /* ---------- custom cursor ---------- */
  const cur = $('.cursor'), dot = $('.cursor-dot');
  if (cur && fine && !reduce) {
    let mx = innerWidth / 2, my = innerHeight / 2, cx = mx, cy = my;
    addEventListener('pointermove', (e) => { mx = e.clientX; my = e.clientY; dot.style.transform = `translate(${mx}px,${my}px)`; }, { passive: true });
    const loop = () => { cx += (mx - cx) * .18; cy += (my - cy) * .18; cur.style.transform = `translate(${cx}px,${cy}px)`; requestAnimationFrame(loop); };
    loop();
    document.addEventListener('pointerover', (e) => {
      const v = e.target.closest('[data-cursor]');
      const a = e.target.closest('a,button,summary,label,.layer,input,select,textarea');
      cur.classList.toggle('view', !!v);
      cur.classList.toggle('hover', !v && !!a);
      const sp = $('span', cur); if (sp) sp.textContent = v ? v.dataset.cursor : '';
    });
    document.addEventListener('mouseleave', () => body.classList.add('no-cursor'));
    document.addEventListener('mouseenter', () => body.classList.remove('no-cursor'));
  }

  /* ---------- magnetic ---------- */
  if (fine && !reduce) $$('.btn, .magnetic, .to-top, .logo-mark').forEach(el => {
    el.addEventListener('pointermove', (e) => {
      const r = el.getBoundingClientRect();
      const x = (e.clientX - r.left - r.width / 2) * .25, y = (e.clientY - r.top - r.height / 2) * .35;
      el.style.transform = `translate(${x}px,${y}px)`;
    });
    el.addEventListener('pointerleave', () => el.style.transform = '');
  });

  /* ---------- card spotlight + tilt ---------- */
  $$('.card').forEach(c => {
    c.addEventListener('pointermove', (e) => {
      const r = c.getBoundingClientRect(), x = e.clientX - r.left, y = e.clientY - r.top;
      c.style.setProperty('--mx', x + 'px'); c.style.setProperty('--my', y + 'px');
      if (fine && !reduce && c.hasAttribute('data-tilt')) c.style.transform = `perspective(900px) rotateX(${(y / r.height - .5) * -6}deg) rotateY(${(x / r.width - .5) * 6}deg)`;
    });
    c.addEventListener('pointerleave', () => { c.style.transform = ''; });
  });

  /* ---------- AI Growth Stack ---------- */
  const layers = $$('.layer'), slabs = $$('.slab');
  const activate = (i) => {
    layers.forEach((l, j) => { l.classList.toggle('active', j === i); l.setAttribute('aria-expanded', j === i); });
    slabs.forEach((s, j) => s.classList.toggle('on', j <= i));
  };
  layers.forEach((l, i) => {
    l.setAttribute('role', 'button');
    l.addEventListener('click', () => activate(i));
    l.addEventListener('keydown', (e) => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); activate(i); } });
    l.addEventListener('mouseenter', () => fine && activate(i));
  });
  if (layers.length) activate(0);

  /* ---------- scroll-lit statement ---------- */
  $$('[data-lit]').forEach(stmt => {
    stmt.innerHTML = stmt.textContent.trim().split(/\s+/).map(w => `<span class="word">${w}</span>`).join(' ');
    const words = $$('.word', stmt);
    const lit = () => {
      const r = stmt.getBoundingClientRect(), vh = innerHeight;
      const p = Math.min(1, Math.max(0, (vh * 0.85 - r.top) / (r.height + vh * 0.3)));
      const n = Math.round(p * words.length);
      words.forEach((w, i) => w.classList.toggle('lit', reduce || i < n));
    };
    addEventListener('scroll', lit, { passive: true }); lit();
  });

  /* ---------- marquees (scroll-velocity aware) ---------- */
  const tracks = $$('.marquee-track');
  if (tracks.length && !reduce) {
    let vel = 0, prevY = scrollY;
    const state = tracks.map(t => ({ t, x: 0, dir: t.dataset.dir === 'right' ? 1 : -1, w: 0 }));
    const measure = () => state.forEach(s => s.w = s.t.scrollWidth / 2);
    measure(); addEventListener('resize', measure);
    const loop = () => {
      const y = scrollY; vel = vel * .9 + (y - prevY) * .1; prevY = y;
      state.forEach(s => {
        const speed = (s.t.closest('.big-marquee') ? .6 : .45) + Math.min(6, Math.abs(vel) * .25);
        s.x += speed * s.dir;
        if (s.w) { if (s.x <= -s.w) s.x += s.w; if (s.x >= 0 && s.dir > 0) s.x -= s.w; }
        s.t.style.transform = `translate3d(${s.x}px,0,0)`;
      });
      requestAnimationFrame(loop);
    };
    state.forEach(s => { if (s.dir > 0) s.x = -s.t.scrollWidth / 4; });
    loop();
  }

  /* ---------- parallax ---------- */
  const par = $$('[data-speed]');
  if (par.length && !reduce) {
    const run = () => {
      par.forEach(el => {
        const r = el.parentElement.getBoundingClientRect();
        const p = (r.top + r.height / 2 - innerHeight / 2) / innerHeight;
        el.style.transform = `translate3d(0,${p * parseFloat(el.dataset.speed) * -100}px,0)`;
      });
      requestAnimationFrame(run);
    };
    run();
  }

  /* ---------- hero portrait mouse drift ---------- */
  const pr = $('.portrait');
  if (pr && fine && !reduce) {
    const img = $('img', pr);
    pr.addEventListener('pointermove', (e) => {
      const r = pr.getBoundingClientRect();
      const x = (e.clientX - r.left) / r.width - .5, y = (e.clientY - r.top) / r.height - .5;
      img.style.translate = `${x * -14}px ${y * -10}px`;
    });
    pr.addEventListener('pointerleave', () => img.style.translate = '');
  }

  /* ---------- timeline fill ---------- */
  $$('.tl').forEach(tl => {
    const fill = document.createElement('span'); fill.className = 'tl-fill'; tl.prepend(fill);
    const run = () => {
      const r = tl.getBoundingClientRect();
      const p = Math.min(1, Math.max(0, (innerHeight * .7 - r.top) / r.height));
      fill.style.height = (p * (r.height - 16)) + 'px';
    };
    addEventListener('scroll', run, { passive: true }); run();
  });

  /* ---------- Dubai clock ---------- */
  const clocks = $$('.clock');
  if (clocks.length) {
    const f = () => {
      let s; try { s = new Date().toLocaleTimeString('en-GB', { timeZone: 'Asia/Dubai', hour: '2-digit', minute: '2-digit' }); } catch (e) { s = ''; }
      clocks.forEach(c => c.textContent = s);
    };
    f(); setInterval(f, 15000);
  }

  /* ---------- to top ---------- */
  $$('.to-top').forEach(b => b.addEventListener('click', () => scrollTo({ top: 0, behavior: reduce ? 'auto' : 'smooth' })));

  /* ---------- page transitions ---------- */
  const pt = $('.pt');
  if (pt && !reduce) {
    document.addEventListener('click', (e) => {
      const a = e.target.closest('a');
      if (!a || e.metaKey || e.ctrlKey || e.shiftKey || a.target === '_blank') return;
      const href = a.getAttribute('href') || '';
      if (!/\.html(#.*)?$/.test(href) || href.startsWith('http')) return;
      const url = new URL(href, location.href);
      if (url.pathname === location.pathname) return;
      e.preventDefault(); pt.classList.add('out');
      setTimeout(() => { location.href = href; }, 550);
    });
    addEventListener('pageshow', (e) => { if (e.persisted) pt.classList.remove('out'); });
  }

  /* ---------- contact form -> mailto ---------- */
  const form = $('#contact-form');
  form && form.addEventListener('submit', (e) => {
    e.preventDefault();
    const d = new FormData(form);
    const focus = d.getAll('focus').join(', ') || '—';
    const body = `Name: ${d.get('name')}\nCompany: ${d.get('company') || '—'}\nWebsite: ${d.get('site') || '—'}\nFocus: ${focus}\nMonthly marketing budget: ${d.get('budget') || '—'}\n\n${d.get('msg')}`;
    location.href = `mailto:hello@saqibameer.com?subject=${encodeURIComponent('Growth enquiry from ' + d.get('name'))}&body=${encodeURIComponent(body)}`;
  });

  $$('[data-year]').forEach(y => y.textContent = new Date().getFullYear());
})();
