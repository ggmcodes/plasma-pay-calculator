/* HETAL_RETAIL_START_2026_05 */
/**
 * Hetal Retail sponsor injection — Cozy River Studios paid placement
 * Campaign: hetal_retail_trial_2026_05  (2026-05-12 → 2026-06-11)
 *
 * Behaviour:
 *  - On every page: inject a sticky top sponsor banner (sitewide placement)
 *  - On plasmapaycalculator 10 target city pages: ALSO inject a hero sponsor block above the calculator
 *  - All outbound URLs include UTM tags scoped to the placement
 *
 * KILLSWITCH: when the trial ends and Hetal does not renew, delete this folder
 *  (/assets/sponsors/hetal-retail/) and the single <script> include in the site
 *  header — that is the entire removal. No other dependencies.
 */
(function () {
  'use strict';

  var CAMPAIGN = 'hetal_retail_trial_2026_05';
  var BASE_URL = 'https://hetalretail.onelink.me/sfUI/f8wk75ms';
  var ASSET_BASE = '/assets/sponsors/hetal-retail/';
  var STORAGE_KEY = 'hetalSponsorDismissed_2026_05';
  var SVG_NS = 'http://www.w3.org/2000/svg';

  function detectSite() {
    if (window.HETAL_SITE) return window.HETAL_SITE;
    var h = window.location.hostname;
    if (h.indexOf('sidequesthustle') !== -1) return 'sqh';
    if (h.indexOf('plasmapaycalculator') !== -1) return 'plasma';
    if (h.indexOf('donorpaycalculator') !== -1) return 'dpc';
    if (h.indexOf('flexdriverguide') !== -1) return 'fdg';
    if (h.indexOf('localhost') !== -1 || h.indexOf('127.0.0.1') !== -1) return 'local';
    return 'unknown';
  }

  var SITE = detectSite();

  var PLASMA_CITY_MAP = {
    'california/los-angeles': 'los_angeles',
    'texas/dallas': 'dallas',
    'illinois/chicago': 'chicago',
    'massachusetts/boston': 'boston',
    'new-jersey/newark': 'newark',
    'district-of-columbia/washington': 'dc',
    'connecticut/hartford': 'hartford',
    'pennsylvania/philadelphia': 'philadelphia',
    'pennsylvania/pittsburgh': 'pittsburgh',
    'maryland/baltimore': 'baltimore'
  };

  function detectCity() {
    if (SITE !== 'plasma') return null;
    var path = window.location.pathname.replace(/\/+$/, '');
    var m = path.match(/^\/calculators\/([^\/]+)\/([^\/]+)$/);
    if (!m) return null;
    var key = m[1] + '/' + m[2];
    return PLASMA_CITY_MAP[key] || null;
  }

  function buildUrl(medium, content) {
    var p = [
      'utm_source=' + encodeURIComponent(SITE),
      'utm_medium=' + encodeURIComponent(medium),
      'utm_campaign=' + encodeURIComponent(CAMPAIGN),
      'utm_content=' + encodeURIComponent(content)
    ];
    return BASE_URL + '?' + p.join('&');
  }

  function isDismissed() {
    try { return localStorage.getItem(STORAGE_KEY) === '1'; } catch (e) { return false; }
  }
  function setDismissed() {
    try { localStorage.setItem(STORAGE_KEY, '1'); } catch (e) {}
  }

  function el(tag, opts) {
    var n = document.createElement(tag);
    if (!opts) return n;
    if (opts.className) n.className = opts.className;
    if (opts.id) n.id = opts.id;
    if (opts.text) n.textContent = opts.text;
    if (opts.attrs) {
      for (var k in opts.attrs) if (Object.prototype.hasOwnProperty.call(opts.attrs, k)) {
        n.setAttribute(k, opts.attrs[k]);
      }
    }
    return n;
  }

  function img(src, alt, className) {
    var n = document.createElement('img');
    n.src = src;
    n.alt = alt;
    if (className) n.className = className;
    return n;
  }

  function arrowSvg(size) {
    var s = document.createElementNS(SVG_NS, 'svg');
    s.setAttribute('width', String(size));
    s.setAttribute('height', String(size));
    s.setAttribute('viewBox', '0 0 24 24');
    s.setAttribute('fill', 'none');
    s.setAttribute('stroke', 'currentColor');
    s.setAttribute('stroke-width', '2.5');
    s.setAttribute('stroke-linecap', 'round');
    s.setAttribute('stroke-linejoin', 'round');
    s.setAttribute('aria-hidden', 'true');
    var path = document.createElementNS(SVG_NS, 'path');
    path.setAttribute('d', 'M9 5l7 7-7 7');
    s.appendChild(path);
    return s;
  }

  function createStickyBanner() {
    var city = detectCity();
    var medium = city ? 'city_banner_sticky' : 'banner';
    var content = city ? 'city_' + city + '_sticky' : 'sitewide_sticky_' + SITE;

    var wrap = el('div', { className: 'hr-sticky', id: 'hetalStickyBanner', attrs: { 'data-hetal-campaign': CAMPAIGN } });

    var a = document.createElement('a');
    a.href = buildUrl(medium, content);
    a.target = '_blank';
    a.rel = 'noopener sponsored';
    a.className = 'hr-sticky-link';

    a.appendChild(img(ASSET_BASE + 'logo.png', 'Hetal Retail', 'hr-sticky-logo'));
    a.appendChild(el('span', { className: 'hr-sticky-badge', text: 'Get Paid to Shop' }));
    a.appendChild(el('span', { className: 'hr-sticky-headline', text: 'Record the aisles we list. It’s that easy.' }));

    var cta = el('span', { className: 'hr-sticky-cta', text: 'Download App' });
    cta.appendChild(arrowSvg(14));
    a.appendChild(cta);

    var dismiss = el('button', { className: 'hr-sticky-dismiss', text: '×', attrs: { type: 'button', 'aria-label': 'Dismiss sponsor banner' } });
    dismiss.addEventListener('click', function (e) {
      e.preventDefault();
      e.stopPropagation();
      var b = document.getElementById('hetalStickyBanner');
      if (b && b.parentNode) b.parentNode.removeChild(b);
      document.body.classList.remove('hr-sticky-padded');
      setDismissed();
    });

    wrap.appendChild(a);
    wrap.appendChild(dismiss);
    return wrap;
  }

  function injectSticky() {
    if (isDismissed()) return;
    if (document.getElementById('hetalStickyBanner')) return;
    var banner = createStickyBanner();
    document.body.insertBefore(banner, document.body.firstChild);
    document.body.classList.add('hr-sticky-padded');
  }

  function createCityHero(city) {
    var content = 'city_' + city + '_hero';

    var section = el('section', { className: 'hr-city-hero', id: 'hetalCityHero', attrs: { 'aria-label': 'Sponsored: Hetal Retail' } });
    var inner = el('div', { className: 'hr-city-hero-inner' });

    var media = el('div', { className: 'hr-city-hero-media' });
    var heroImg = img(ASSET_BASE + 'hero-city.png', 'Hetal Retail — Get paid to film store aisles');
    heroImg.loading = 'lazy';
    media.appendChild(heroImg);

    var copy = el('div', { className: 'hr-city-hero-copy' });

    var sponsorLine = el('div', { className: 'hr-city-hero-sponsor' });
    sponsorLine.appendChild(document.createTextNode('SPONSORED • '));
    sponsorLine.appendChild(img(ASSET_BASE + 'logo.png', 'Hetal Retail'));
    copy.appendChild(sponsorLine);

    copy.appendChild(el('div', { className: 'hr-city-hero-badge', text: 'Get Paid to Shop' }));
    copy.appendChild(el('h2', { className: 'hr-city-hero-headline', text: 'Record the aisles we list. It’s that easy.' }));
    copy.appendChild(el('p', { className: 'hr-city-hero-sub', text: 'Unlike other gig apps, there’s no shopping or delivery required. Walmart, Target, Sprouts, Whole Foods & more.' }));

    var ctaLink = document.createElement('a');
    ctaLink.className = 'hr-city-hero-cta';
    ctaLink.href = buildUrl('city_hero', content);
    ctaLink.target = '_blank';
    ctaLink.rel = 'noopener sponsored';
    ctaLink.appendChild(document.createTextNode('Download the App'));
    ctaLink.appendChild(arrowSvg(16));
    copy.appendChild(ctaLink);

    copy.appendChild(el('div', { className: 'hr-city-hero-disclosure', text: 'Sponsored content. Cozy River Studios may receive compensation.' }));

    inner.appendChild(media);
    inner.appendChild(copy);
    section.appendChild(inner);
    return section;
  }

  function injectCityHero() {
    var city = detectCity();
    if (!city) return;
    if (document.getElementById('hetalCityHero')) return;

    var hero = createCityHero(city);

    // Final desired order on plasma city pages: sticky → site nav → Hetal hero → page content.
    // Site nav is repositioned in repositionPlasmaNav() to sit right after sticky,
    // so on plasma we anchor the hero to the nav. Elsewhere we anchor to the sticky.
    var nav = document.querySelector('body > nav');
    var sticky = document.getElementById('hetalStickyBanner');
    var anchor = (SITE === 'plasma' && nav) ? nav : sticky;
    if (anchor && anchor.parentNode) {
      anchor.parentNode.insertBefore(hero, anchor.nextSibling);
    } else {
      document.body.insertBefore(hero, document.body.firstChild);
    }
  }

  function injectStyles() {
    if (document.getElementById('hetalSponsorCss')) return;
    var link = document.createElement('link');
    link.id = 'hetalSponsorCss';
    link.rel = 'stylesheet';
    link.href = ASSET_BASE + 'sponsor.css?v=6';
    document.head.appendChild(link);
  }

  function repositionPlasmaNav() {
    // Plasma's homepage nav is `<body><nav>...</nav>`, but plasma city pages
    // have malformed HTML where SEO sections render before the nav. CSS
    // position:static makes the nav fall to the bottom on those pages.
    // Move the nav back to the top in DOM order, right after the Hetal sticky
    // (and city hero if present), so navigation stays accessible and looks
    // intentional regardless of page structure.
    if (SITE !== 'plasma') return;
    var nav = document.querySelector('body > nav');
    if (!nav) return;
    var sticky = document.getElementById('hetalStickyBanner');
    var hero = document.getElementById('hetalCityHero');
    var anchor = hero || sticky;
    if (!anchor || !anchor.parentNode) return;
    anchor.parentNode.insertBefore(nav, anchor.nextSibling);
  }

  function init() {
    injectStyles();
    injectSticky();
    // Order matters on plasma: move nav into top position BEFORE the hero, so the
    // hero anchors against the nav and ends up below it. Result: sticky → nav → hero.
    repositionPlasmaNav();
    injectCityHero();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
/* HETAL_RETAIL_END_2026_05 */
