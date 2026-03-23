/**
 * SideQuestHustle Newsletter Injection Script
 * Auto-injects: footer CTA, mid-content inline CTA, sticky bottom bar
 * Site: plasmapaycalculator.com
 *
 * Uses DOM methods (createElement, textContent, addEventListener) only.
 */
(function() {
  'use strict';

  var BEEHIIV_SRC = 'https://subscribe-forms.beehiiv.com/4311c479-112f-4a48-bd7f-b6fc98488ed6?utm_source=plasmapaycalculator&utm_medium=embed&utm_campaign=sidequesthustle';
  var DISMISSED_KEY = 'sqh_bar_dismissed';

  function isBarDismissed() {
    var dismissed = localStorage.getItem(DISMISSED_KEY);
    if (!dismissed) return false;
    return (Date.now() - parseInt(dismissed)) < 7 * 24 * 60 * 60 * 1000;
  }

  function createIframe() {
    var iframe = document.createElement('iframe');
    iframe.src = BEEHIIV_SRC;
    iframe.className = 'beehiiv-embed';
    iframe.setAttribute('data-test-id', 'beehiiv-embed');
    iframe.setAttribute('width', '429');
    iframe.setAttribute('height', '230');
    iframe.setAttribute('frameborder', '0');
    iframe.setAttribute('scrolling', 'no');
    iframe.style.cssText = 'width:429px;height:230px;margin:0;border-radius:0px!important;background-color:transparent;box-shadow:0 0 #0000;max-width:100%;border:none;';
    return iframe;
  }

  // ============================================
  // 1. FOOTER CTA (compact, above footer)
  // ============================================
  function injectFooterCTA() {
    var footer = document.querySelector('footer') || document.querySelector('[class*="footer"]');
    if (!footer) return;
    if (document.getElementById('sqh-footer-cta')) return;

    var section = document.createElement('div');
    section.id = 'sqh-footer-cta';

    var wrapper = document.createElement('div');
    wrapper.style.cssText = 'background:#ffffff;border:2px solid #0d9488;padding:32px 20px;text-align:center;font-family:system-ui,sans-serif;';

    var inner = document.createElement('div');
    inner.style.cssText = 'max-width:600px;margin:0 auto;';

    var badgeRow = document.createElement('div');
    badgeRow.style.cssText = 'display:inline-flex;align-items:center;gap:8px;margin-bottom:12px;';

    var badge = document.createElement('span');
    badge.style.cssText = 'background:#0d9488;color:#fff;font-weight:700;font-size:10px;letter-spacing:1px;text-transform:uppercase;padding:3px 10px;border-radius:100px;';
    badge.textContent = 'Free Newsletter';

    var sunday = document.createElement('span');
    sunday.style.cssText = 'color:#0d9488;font-size:11px;font-weight:600;';
    sunday.textContent = 'Every Sunday';

    badgeRow.appendChild(badge);
    badgeRow.appendChild(sunday);

    var heading = document.createElement('h3');
    heading.style.cssText = 'color:#111;font-weight:800;font-size:20px;margin:0 0 6px;line-height:1.3;';
    heading.textContent = 'Get the Side Hustle Blueprint 2026 ';
    var headingSpan = document.createElement('span');
    headingSpan.style.color = '#0d9488';
    headingSpan.textContent = 'FREE';
    heading.appendChild(headingSpan);

    var desc = document.createElement('p');
    desc.style.cssText = 'color:#6b7280;font-size:13px;margin:0 0 14px;line-height:1.5;';
    desc.textContent = '150+ side income strategies beyond plasma donations. New issue every Sunday.';

    var iframeWrap = document.createElement('div');
    iframeWrap.style.cssText = 'display:flex;justify-content:center;';
    iframeWrap.appendChild(createIframe());

    inner.appendChild(badgeRow);
    inner.appendChild(heading);
    inner.appendChild(desc);
    inner.appendChild(iframeWrap);
    wrapper.appendChild(inner);
    section.appendChild(wrapper);

    footer.parentNode.insertBefore(section, footer);
  }

  // ============================================
  // 2. MID-CONTENT INLINE CTA
  // ============================================
  function injectInlineCTA() {
    var article = document.querySelector('article') || document.querySelector('main') || document.querySelector('[class*="content"]');
    if (!article) return;
    if (window.location.pathname === '/' || window.location.pathname === '/index.html') return;
    if (document.getElementById('sqh-inline-cta')) return;

    var headings = article.querySelectorAll('h2');
    if (headings.length < 3) return;

    var targetHeading = headings[2];
    var cta = document.createElement('div');
    cta.id = 'sqh-inline-cta';

    var card = document.createElement('div');
    card.style.cssText = 'background:linear-gradient(135deg,#FF6F61,#FF8A7A);border-radius:12px;padding:24px 20px;text-align:center;margin:32px 0;font-family:system-ui,sans-serif;';

    var title = document.createElement('p');
    title.style.cssText = 'color:#fff;font-weight:800;font-size:16px;margin:0 0 6px;line-height:1.3;';
    title.textContent = '\uD83C\uDF81 Free: Side Hustle Blueprint 2026';

    var sub = document.createElement('p');
    sub.style.cssText = 'color:rgba(255,255,255,0.9);font-size:13px;margin:0 0 12px;line-height:1.4;';
    sub.textContent = '150+ strategies in 14 chapters \u2014 delivered to your inbox every Sunday.';

    var iframeWrap = document.createElement('div');
    iframeWrap.style.cssText = 'display:flex;justify-content:center;';
    iframeWrap.appendChild(createIframe());

    card.appendChild(title);
    card.appendChild(sub);
    card.appendChild(iframeWrap);
    cta.appendChild(card);

    var parent = targetHeading.parentElement;
    if (parent && parent !== article) {
      parent.parentNode.insertBefore(cta, parent.nextSibling);
    } else {
      targetHeading.parentNode.insertBefore(cta, targetHeading.nextSibling);
    }
  }

  // ============================================
  // 4. STICKY BOTTOM BAR
  // ============================================
  function injectStickyBar() {
    if (isBarDismissed()) return;
    if (document.getElementById('sqh-sticky-bar')) return;

    var bar = document.createElement('div');
    bar.id = 'sqh-sticky-bar';

    var barInner = document.createElement('div');
    barInner.style.cssText = 'position:fixed;bottom:0;left:0;right:0;background:#030712;border-top:2px solid #0d9488;padding:12px 20px;z-index:9999;font-family:system-ui,sans-serif;display:flex;align-items:center;justify-content:center;gap:12px;flex-wrap:wrap;';

    var content = document.createElement('div');
    content.style.cssText = 'display:flex;align-items:center;gap:10px;flex-wrap:wrap;justify-content:center;';

    var gift = document.createElement('span');
    gift.style.cssText = 'color:#0d9488;font-size:18px;';
    gift.textContent = '\uD83C\uDF81';

    var text = document.createElement('span');
    text.style.cssText = 'color:#fff;font-weight:700;font-size:14px;';
    text.textContent = 'Get 150+ Side Hustle Strategies FREE';

    var btn = document.createElement('a');
    btn.href = '#sqh-footer-cta';
    btn.style.cssText = 'background:#0d9488;color:#fff;font-weight:700;font-size:12px;padding:6px 16px;border-radius:6px;text-decoration:none;white-space:nowrap;';
    btn.textContent = 'Subscribe Free';
    btn.addEventListener('click', function(e) {
      e.preventDefault();
      var target = document.getElementById('sqh-footer-cta');
      if (target) target.scrollIntoView({behavior: 'smooth'});
    });

    var close = document.createElement('button');
    close.style.cssText = 'background:none;border:none;color:#6b7280;font-size:18px;cursor:pointer;padding:4px 8px;line-height:1;';
    close.textContent = '\u00D7';
    close.setAttribute('aria-label', 'Dismiss');
    close.addEventListener('click', function() {
      bar.remove();
      document.body.style.paddingBottom = '';
      localStorage.setItem(DISMISSED_KEY, Date.now().toString());
    });

    content.appendChild(gift);
    content.appendChild(text);
    content.appendChild(btn);
    barInner.appendChild(content);
    barInner.appendChild(close);
    bar.appendChild(barInner);
    document.body.appendChild(bar);
    document.body.style.paddingBottom = '60px';
  }

  // ============================================
  // INIT
  // ============================================
  function init() {
    injectFooterCTA();
    injectInlineCTA();
    setTimeout(injectStickyBar, 5000);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
