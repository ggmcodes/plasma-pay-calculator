/**
 * Surveoo slim banner bar - MaxBounty offer 31078
 * Replaces the expired Rakuten $50 promo slot (ended 2026-06-30).
 *
 * Deliberately low-key: single thin bar, clearly labeled "Ad",
 * dismissible with a 7-day localStorage TTL, hides on scroll down /
 * returns on scroll up, and skips pages that already show the
 * Pro Toolkit sticky banner (#stickyBanner) so bars never stack.
 *
 * Spanish copy is served automatically on /es/ paths.
 * Clicks are tracked by /assets/js/affiliate-tracker.js via the
 * data-affiliate-* attributes on the link.
 */
(function () {
  'use strict';

  var DISMISSED_KEY = 'freecash_banner_dismissed';
  var DISMISS_TTL_MS = 7 * 24 * 60 * 60 * 1000;
  var EXCLUDE_PATHS = ['/premium', '/success', '/privacy', '/terms', '/contact'];

  var BASE_URL = 'https://afflat3c2.com/trk/lnk/30D695DC-75C6-40FA-82F7-BDD4AA37AB19/?o=31078&c=918277&a=798537&k=2DB34ACB9DEC3CABBD0FBA55039DEC62&l=36077';

  var isSpanish = window.location.pathname.indexOf('/es/') === 0;

  var COPY = isSpanish
    ? {
        ad: 'Anuncio',
        msg: 'Gana dinero extra en tus días libres:',
        brand: 'Surveoo',
        detail: 'te paga en efectivo y tarjetas de regalo por encuestas pagadas (solo nuevos usuarios)',
        cta: 'Gana dinero ahora',
        sub: 'plasma_banner_es'
      }
    : {
        ad: 'Ad',
        msg: 'Off-day from donating?',
        brand: 'Surveoo',
        detail: 'pays cash & gift cards for quick paid surveys (new users only)',
        cta: 'Earn money now',
        sub: 'plasma_banner'
      };

  function isExcluded() {
    var p = window.location.pathname;
    for (var i = 0; i < EXCLUDE_PATHS.length; i++) {
      if (p.indexOf(EXCLUDE_PATHS[i]) !== -1) return true;
    }
    return false;
  }

  function isDismissed() {
    var ts = null;
    try { ts = localStorage.getItem(DISMISSED_KEY); } catch (_) {}
    if (!ts) return false;
    return (Date.now() - parseInt(ts, 10)) < DISMISS_TTL_MS;
  }

  function injectStyles() {
    var css = [
      '#fc-banner{position:fixed;top:0;left:0;right:0;z-index:9998;',
      'background:#fdf2f8;border-bottom:1px solid #f9a8d4;',
      'font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;',
      'transition:transform .25s ease;}',
      '#fc-banner.fc-hidden{transform:translateY(-100%);}',
      '.fc-inner{max-width:1100px;margin:0 auto;display:flex;align-items:center;',
      'gap:.6rem;padding:.45rem 2.4rem .45rem .9rem;position:relative;}',
      '.fc-ad{flex:none;font-size:.6rem;font-weight:700;letter-spacing:.08em;',
      'text-transform:uppercase;color:#9d174d;border:1px solid #f9a8d4;',
      'border-radius:4px;padding:.1rem .3rem;background:#fff;}',
      '.fc-link{display:flex;align-items:center;gap:.6rem;flex:1;min-width:0;',
      'text-decoration:none;color:#374151;font-size:.85rem;line-height:1.3;}',
      '.fc-text{overflow:hidden;text-overflow:ellipsis;white-space:nowrap;}',
      '.fc-text strong{color:#831843;}',
      '.fc-cta{flex:none;background:#ec4899;color:#fff;font-weight:700;',
      'font-size:.78rem;padding:.3rem .8rem;border-radius:999px;white-space:nowrap;}',
      '.fc-close{position:absolute;right:.5rem;top:50%;transform:translateY(-50%);',
      'border:none;background:none;color:#9d174d;font-size:1.15rem;line-height:1;',
      'padding:.2rem .4rem;cursor:pointer;}',
      '@media(max-width:640px){.fc-detail{display:none;}',
      '.fc-inner{padding-left:.6rem;gap:.45rem;}.fc-link{font-size:.8rem;}}'
    ].join('');
    var style = document.createElement('style');
    style.textContent = css;
    document.head.appendChild(style);
  }

  function createBanner() {
    var banner = document.createElement('div');
    banner.id = 'fc-banner';

    var inner = document.createElement('div');
    inner.className = 'fc-inner';

    var ad = document.createElement('span');
    ad.className = 'fc-ad';
    ad.textContent = COPY.ad;

    var link = document.createElement('a');
    link.className = 'fc-link';
    link.href = BASE_URL + '&s1=' + COPY.sub;
    link.target = '_blank';
    link.rel = 'nofollow noopener sponsored';
    link.setAttribute('data-affiliate-network', 'maxbounty');
    link.setAttribute('data-offer-id', '31078');
    link.setAttribute('data-link-text', 'Surveoo Banner');

    var text = document.createElement('span');
    text.className = 'fc-text';
    text.appendChild(document.createTextNode(COPY.msg + ' '));
    var b = document.createElement('strong');
    b.textContent = COPY.brand;
    text.appendChild(b);
    var detail = document.createElement('span');
    detail.className = 'fc-detail';
    detail.textContent = ' ' + COPY.detail;
    text.appendChild(detail);

    var cta = document.createElement('span');
    cta.className = 'fc-cta';
    cta.textContent = COPY.cta + ' →';

    link.appendChild(text);
    link.appendChild(cta);

    var close = document.createElement('button');
    close.className = 'fc-close';
    close.setAttribute('aria-label', isSpanish ? 'Cerrar' : 'Dismiss');
    close.textContent = '×';

    inner.appendChild(ad);
    inner.appendChild(link);
    inner.appendChild(close);
    banner.appendChild(inner);
    return banner;
  }

  function adjustPadding(banner) {
    document.body.style.paddingTop = banner.offsetHeight + 'px';
  }

  function removeBanner() {
    var banner = document.getElementById('fc-banner');
    if (banner) {
      banner.remove();
      document.body.style.paddingTop = '';
      try { localStorage.setItem(DISMISSED_KEY, String(Date.now())); } catch (_) {}
    }
  }

  function init() {
    if (isDismissed() || isExcluded()) return;
    // Never stack under the Pro Toolkit sticky banner
    if (document.getElementById('stickyBanner')) return;

    injectStyles();
    var banner = createBanner();
    document.body.insertBefore(banner, document.body.firstChild);
    adjustPadding(banner);

    window.addEventListener('resize', function () {
      var b = document.getElementById('fc-banner');
      if (b && !b.classList.contains('fc-hidden')) adjustPadding(b);
    });

    banner.querySelector('.fc-close').addEventListener('click', function (e) {
      e.preventDefault();
      removeBanner();
    });

    var lastY = window.pageYOffset || 0;
    window.addEventListener('scroll', function () {
      var y = window.pageYOffset || document.documentElement.scrollTop;
      var b = document.getElementById('fc-banner');
      if (!b) return;
      if (y > lastY && y > 120) {
        b.classList.add('fc-hidden');
      } else if (y < lastY) {
        b.classList.remove('fc-hidden');
      }
      lastY = y;
    }, { passive: true });
  }

  // Wait for DOMContentLoaded even when loaded via defer (readyState
  // 'interactive'): the Pro Toolkit sticky-banner registers its
  // DOMContentLoaded handler during parse, so it inserts #stickyBanner
  // before we check for it.
  if (document.readyState === 'complete') {
    init();
  } else {
    document.addEventListener('DOMContentLoaded', init);
  }
})();
