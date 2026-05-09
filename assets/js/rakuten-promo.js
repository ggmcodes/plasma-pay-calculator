/**
 * Rakuten $50 Referral Promo - Floating bottom-right card
 * Site: sidequesthustle.com
 *
 * Time-sensitive: Rakuten is ending the $50/$50 referral bonus June 30, 2026.
 *
 * Pattern: self-contained, inline styles, 7-day localStorage dismiss,
 *          UTM-tagged outbound, gtag tracking, mobile responsive.
 *
 * Configure via window.RAKUTEN_PROMO_CONFIG before loading:
 * window.RAKUTEN_PROMO_CONFIG = {
 *   site: 'sidequesthustle',          // utm_source
 *   campaign: 'rakuten50',            // utm_campaign
 *   accentColor: '#FF6F61',           // matches site brand
 *   delayMs: 4000,
 *   excludePaths: ['/privacy','/terms','/disclaimer','/contact','/about']
 * };
 */
(function() {
  'use strict';

  var DEFAULTS = {
    site: 'sidequesthustle',
    campaign: 'rakuten50',
    accentColor: '#FF6F61',
    delayMs: 4000,
    excludePaths: ['/privacy', '/terms', '/disclaimer', '/contact', '/success'],
    deadline: '2026-06-30T23:59:59-07:00',
    style: 'banner'   // 'banner' (sticky top) | 'card' (bottom-right corner) | 'both'
  };
  var cfg = Object.assign({}, DEFAULTS, window.RAKUTEN_PROMO_CONFIG || {});

  var BASE_URL = 'https://www.rakuten.com/r/4PJYY4?eeid=44971';
  var DISMISSED_KEY = 'rakuten_promo_dismissed';        // localStorage, 7-day TTL (only set by pill ×)
  var SHOWN_THIS_SESSION_KEY = 'rakuten_promo_shown';   // sessionStorage, card per-session gate
  var MINIMIZED_KEY = 'rakuten_promo_minimized';        // sessionStorage, banner minimized state
  var DISMISS_TTL_MS = 7 * 24 * 60 * 60 * 1000;

  function buildUrl(placement) {
    return BASE_URL +
      '&utm_source=' + encodeURIComponent(cfg.site) +
      '&utm_medium=' + encodeURIComponent(placement) +
      '&utm_campaign=' + encodeURIComponent(cfg.campaign);
  }

  function isExcluded() {
    var p = window.location.pathname;
    for (var i = 0; i < cfg.excludePaths.length; i++) {
      if (p.indexOf(cfg.excludePaths[i]) !== -1) return true;
    }
    return false;
  }

  function isDismissed() {
    var ts = null;
    try { ts = localStorage.getItem(DISMISSED_KEY); } catch (_) {}
    if (!ts) return false;
    return (Date.now() - parseInt(ts, 10)) < DISMISS_TTL_MS;
  }

  function markDismissed() {
    try { localStorage.setItem(DISMISSED_KEY, String(Date.now())); } catch (_) {}
  }

  function shownThisSession() {
    try { return sessionStorage.getItem(SHOWN_THIS_SESSION_KEY) === '1'; } catch (_) { return false; }
  }

  function markShownThisSession() {
    try { sessionStorage.setItem(SHOWN_THIS_SESSION_KEY, '1'); } catch (_) {}
  }

  function isMinimized() {
    try { return sessionStorage.getItem(MINIMIZED_KEY) === '1'; } catch (_) { return false; }
  }

  function setMinimized(v) {
    try {
      if (v) sessionStorage.setItem(MINIMIZED_KEY, '1');
      else sessionStorage.removeItem(MINIMIZED_KEY);
    } catch (_) {}
  }

  function isExpired() {
    return Date.now() > new Date(cfg.deadline).getTime();
  }

  function daysLeft() {
    var ms = new Date(cfg.deadline).getTime() - Date.now();
    return Math.max(0, Math.ceil(ms / (24 * 60 * 60 * 1000)));
  }

  function trackClick(placement) {
    if (window.gtag) {
      try {
        window.gtag('event', 'rakuten_promo_click', {
          placement: placement,
          campaign: cfg.campaign
        });
      } catch (_) {}
    }
  }

  function el(tag, styleStr, textValue) {
    var n = document.createElement(tag);
    if (styleStr) n.style.cssText = styleStr;
    if (textValue != null) n.textContent = textValue;
    return n;
  }

  function buildCard() {
    var accent = cfg.accentColor;
    var days = daysLeft();
    var deadlineStr = new Date(cfg.deadline).toLocaleDateString('en-US', {
      month: 'long', day: 'numeric'
    });

    var wrap = document.createElement('div');
    wrap.id = 'rakuten-promo-card';
    wrap.setAttribute('role', 'complementary');
    wrap.setAttribute('aria-label', 'Rakuten $50 cash bonus offer ending ' + deadlineStr);
    wrap.style.cssText = [
      'position:fixed', 'right:20px', 'bottom:20px', 'z-index:9998',
      'width:320px', 'max-width:calc(100vw - 32px)',
      'background:#fff',
      'border:2px solid ' + accent,
      'border-radius:14px',
      'box-shadow:0 16px 40px rgba(0,0,0,0.18),0 4px 10px rgba(0,0,0,0.08)',
      'font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif',
      'overflow:hidden',
      'transform:translateY(20px)', 'opacity:0',
      'transition:transform .35s ease,opacity .35s ease'
    ].join(';');

    // Top urgency bar
    var bar = el('div',
      'background:' + accent + ';color:#fff;padding:9px 14px;font-size:11px;font-weight:800;letter-spacing:0.14em;text-transform:uppercase;display:flex;align-items:center;justify-content:space-between;');

    var barText = el('span', null,
      days <= 1 ? 'Last chance · Ends today' :
      days <= 7 ? days + ' days left · Ends ' + deadlineStr :
                  'Ending ' + deadlineStr);
    bar.appendChild(barText);

    var close = el('button', 'background:transparent;border:0;color:#fff;font-size:22px;line-height:1;cursor:pointer;padding:0 0 0 8px;font-weight:700;', '×');
    close.type = 'button';
    close.setAttribute('aria-label', 'Dismiss offer');
    close.addEventListener('click', function() {
      markDismissed();
      remove();
    });
    bar.appendChild(close);

    // Body
    var body = el('div', 'padding:18px 18px 16px;');

    var eyebrow = el('div',
      'display:inline-block;background:#FFF3F1;color:' + accent + ';font-size:10px;font-weight:900;letter-spacing:0.16em;text-transform:uppercase;padding:4px 8px;border-radius:4px;margin-bottom:8px;',
      'Biggest Rakuten Bonus Ever');

    var headline = el('div', 'display:flex;align-items:baseline;gap:8px;margin-bottom:6px;');
    headline.appendChild(el('span',
      'font-size:42px;font-weight:900;color:#0F0F10;line-height:1;letter-spacing:-0.02em;', '$50'));
    headline.appendChild(el('span',
      'font-size:15px;font-weight:800;color:#0F0F10;', 'cash · no catch'));

    var sub = el('p', 'margin:0 0 12px;font-size:13px;line-height:1.5;color:#3A3A3D;');
    sub.appendChild(document.createTextNode('The '));
    sub.appendChild(el('strong', null, '$50 sign-up bonus is the best Rakuten has ever run'));
    sub.appendChild(document.createTextNode('. The historical norm is $30. '));
    var endsStrong = el('strong', 'color:' + accent + ';', 'Expires ' + deadlineStr + '.');
    sub.appendChild(endsStrong);
    sub.appendChild(document.createTextNode(' Spend $50, get $50.'));

    var ctaUrl = buildUrl('floating-card');
    var cta = el('a',
      'display:block;background:' + accent + ';color:#fff;text-align:center;padding:14px 16px;border-radius:10px;font-size:15px;font-weight:800;text-decoration:none;letter-spacing:0.01em;cursor:pointer;',
      'Claim my $50 →');
    cta.href = ctaUrl;
    cta.target = '_blank';
    cta.rel = 'noopener sponsored';
    cta.addEventListener('click', function(e) {
      trackClick('floating-card');
      // Explicit window.open with same-tab fallback for reliability
      // (defends against popup blockers eating target="_blank" clicks).
      var opened = null;
      try { opened = window.open(ctaUrl, '_blank', 'noopener'); } catch (_) {}
      if (!opened) {
        e.preventDefault();
        window.location.href = ctaUrl;
      } else {
        e.preventDefault();
      }
    });

    var disclosure = el('p',
      'margin:10px 0 0;font-size:11px;color:#7A7A80;text-align:center;line-height:1.4;',
      'Referral link · Both of us earn · No purchase required to sign up');

    body.appendChild(eyebrow);
    body.appendChild(headline);
    body.appendChild(sub);
    body.appendChild(cta);
    body.appendChild(disclosure);

    // Make the body area clickable (except cta which has its own handler)
    body.style.cursor = 'pointer';
    body.addEventListener('click', function(e) {
      // ignore clicks that originated on the cta (it has its own handler)
      if (cta.contains(e.target) || e.target === cta) return;
      trackClick('card-body');
      var opened = null;
      try { opened = window.open(ctaUrl, '_blank', 'noopener'); } catch (_) {}
      if (!opened) window.location.href = ctaUrl;
    });

    wrap.appendChild(bar);
    wrap.appendChild(body);

    return wrap;
  }

  // ============================================
  // TOP BANNER (sticky, full-width)
  // ============================================
  function buildBanner() {
    var accent = cfg.accentColor;
    var days = daysLeft();
    var deadlineStr = new Date(cfg.deadline).toLocaleDateString('en-US', {
      month: 'long', day: 'numeric'
    });
    var bannerUrl = buildUrl('top-banner');

    var bar = document.createElement('div');
    bar.id = 'rakuten-promo-banner';
    bar.setAttribute('role', 'complementary');
    bar.setAttribute('aria-label', 'Rakuten $50 cash bonus offer ending ' + deadlineStr);
    bar.style.cssText = [
      'position:sticky', 'top:0', 'left:0', 'right:0', 'z-index:9999',
      'background:linear-gradient(90deg,' + accent + ' 0%,#E04B3D 100%)',
      'color:#fff',
      'font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif',
      'box-shadow:0 2px 10px rgba(0,0,0,0.10)',
      'cursor:pointer',
      'transform:translateY(-100%)', 'opacity:0',
      'transition:transform .35s ease,opacity .35s ease'
    ].join(';');

    var inner = el('div',
      'max-width:1200px;margin:0 auto;padding:10px 16px;display:flex;align-items:center;gap:12px;justify-content:center;flex-wrap:wrap;');

    // Mobile: shorter text. Desktop: full pitch.
    var msg = el('span', 'font-size:14px;font-weight:700;line-height:1.4;text-align:center;');
    msg.appendChild(document.createTextNode('💰 '));
    msg.appendChild(el('strong',
      'font-weight:900;letter-spacing:0.01em;',
      'Rakuten\'s biggest bonus EVER:'));
    msg.appendChild(document.createTextNode(' Get $50 free cash when you spend $50. '));
    var endsSpan = el('span', 'background:rgba(0,0,0,0.18);padding:2px 8px;border-radius:4px;margin:0 6px;white-space:nowrap;font-weight:800;',
      days <= 1 ? 'Ends today' :
      days <= 7 ? days + ' days left' :
                  'Ends ' + deadlineStr);
    msg.appendChild(endsSpan);

    var ctaBtn = el('a',
      'background:#fff;color:' + accent + ';font-weight:900;font-size:13px;padding:7px 14px;border-radius:6px;text-decoration:none;white-space:nowrap;letter-spacing:0.02em;text-transform:uppercase;',
      'Claim $50 →');
    ctaBtn.href = bannerUrl;
    ctaBtn.target = '_blank';
    ctaBtn.rel = 'noopener sponsored';
    ctaBtn.addEventListener('click', function(e) {
      trackClick('top-banner');
      var opened = null;
      try { opened = window.open(bannerUrl, '_blank', 'noopener'); } catch (_) {}
      e.preventDefault();
      if (!opened) window.location.href = bannerUrl;
    });

    var close = el('button',
      'background:transparent;border:0;color:#fff;font-size:22px;line-height:1;cursor:pointer;padding:0 4px;font-weight:700;opacity:0.8;',
      '×');
    close.type = 'button';
    close.setAttribute('aria-label', 'Minimize offer');
    close.title = 'Minimize';
    close.addEventListener('click', function(e) {
      e.stopPropagation();
      // Minimize — don't permanently dismiss. Show reopener pill.
      setMinimized(true);
      removeBanner();
      showPill();
    });

    inner.appendChild(msg);
    inner.appendChild(ctaBtn);
    inner.appendChild(close);
    bar.appendChild(inner);

    // Make whole banner clickable (except × button)
    bar.addEventListener('click', function(e) {
      if (close.contains(e.target) || e.target === close) return;
      if (ctaBtn.contains(e.target) || e.target === ctaBtn) return;
      trackClick('top-banner');
      var opened = null;
      try { opened = window.open(bannerUrl, '_blank', 'noopener'); } catch (_) {}
      if (!opened) window.location.href = bannerUrl;
    });

    return bar;
  }

  function showBanner() {
    if (document.getElementById('rakuten-promo-banner')) return;
    var b = buildBanner();
    // Insert at top of body so it sits above page content
    document.body.insertBefore(b, document.body.firstChild);
    requestAnimationFrame(function() {
      b.style.transform = 'translateY(0)';
      b.style.opacity = '1';
    });
  }

  function removeBanner() {
    var b = document.getElementById('rakuten-promo-banner');
    if (!b) return;
    b.style.transform = 'translateY(-100%)';
    b.style.opacity = '0';
    setTimeout(function() { if (b.parentNode) b.parentNode.removeChild(b); }, 350);
  }

  // ============================================
  // REOPENER PILL (small floating bubble shown after minimize)
  // ============================================
  function buildPill() {
    var accent = cfg.accentColor;
    var days = daysLeft();

    var pill = document.createElement('button');
    pill.id = 'rakuten-promo-pill';
    pill.type = 'button';
    pill.setAttribute('aria-label', 'Reopen Rakuten $50 offer');
    pill.title = 'Reopen $50 offer';
    pill.style.cssText = [
      'position:fixed', 'right:16px', 'bottom:16px', 'z-index:9997',
      'background:linear-gradient(135deg,' + accent + ' 0%,#E04B3D 100%)',
      'color:#fff',
      'border:0',
      'border-radius:999px',
      'padding:10px 14px 10px 12px',
      'font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif',
      'font-size:13px', 'font-weight:800',
      'cursor:pointer',
      'box-shadow:0 8px 22px rgba(224,75,61,0.35),0 2px 6px rgba(0,0,0,0.10)',
      'display:flex', 'align-items:center', 'gap:6px',
      'transform:scale(0.6)', 'opacity:0',
      'transition:transform .25s ease,opacity .25s ease,box-shadow .2s ease'
    ].join(';');

    pill.appendChild(document.createTextNode('💰 '));
    pill.appendChild(el('span',
      'font-weight:900;font-size:14px;letter-spacing:-0.01em;', '$50'));
    pill.appendChild(el('span',
      'font-weight:700;font-size:12px;opacity:0.95;',
      days <= 1 ? 'today only' : days + 'd left'));

    // Hover effect
    pill.addEventListener('mouseenter', function() {
      pill.style.transform = 'scale(1.05)';
      pill.style.boxShadow = '0 12px 28px rgba(224,75,61,0.45),0 3px 8px rgba(0,0,0,0.12)';
    });
    pill.addEventListener('mouseleave', function() {
      pill.style.transform = 'scale(1)';
      pill.style.boxShadow = '0 8px 22px rgba(224,75,61,0.35),0 2px 6px rgba(0,0,0,0.10)';
    });

    pill.addEventListener('click', function() {
      setMinimized(false);
      removePill();
      showBanner();
    });

    return pill;
  }

  function showPill() {
    if (document.getElementById('rakuten-promo-pill')) return;
    var pill = buildPill();
    document.body.appendChild(pill);
    requestAnimationFrame(function() {
      pill.style.transform = 'scale(1)';
      pill.style.opacity = '1';
    });
  }

  function removePill() {
    var pill = document.getElementById('rakuten-promo-pill');
    if (!pill) return;
    pill.style.transform = 'scale(0.6)';
    pill.style.opacity = '0';
    setTimeout(function() { if (pill.parentNode) pill.parentNode.removeChild(pill); }, 250);
  }

  function show() {
    if (document.getElementById('rakuten-promo-card')) return;
    var card = buildCard();
    document.body.appendChild(card);
    markShownThisSession();
    requestAnimationFrame(function() {
      card.style.transform = 'translateY(0)';
      card.style.opacity = '1';
    });
  }

  function remove() {
    var card = document.getElementById('rakuten-promo-card');
    if (!card) return;
    card.style.transform = 'translateY(20px)';
    card.style.opacity = '0';
    setTimeout(function() { if (card.parentNode) card.parentNode.removeChild(card); }, 350);
  }

  function init() {
    if (isExpired()) return;
    if (isExcluded()) return;
    if (isDismissed()) return;

    if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      cfg.delayMs = Math.min(cfg.delayMs, 1500);
    }

    var style = cfg.style || 'banner';
    var doBanner = style === 'banner' || style === 'both';
    var doCard = style === 'card' || style === 'both';

    if (doBanner) {
      // If user minimized in this session, show the small pill instead of the banner.
      var bannerFn = isMinimized() ? showPill : showBanner;
      if (document.body) {
        bannerFn();
      } else {
        document.addEventListener('DOMContentLoaded', bannerFn);
      }
    }
    if (doCard) {
      if (shownThisSession()) return;   // card respects per-session limit
      setTimeout(show, cfg.delayMs);
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
