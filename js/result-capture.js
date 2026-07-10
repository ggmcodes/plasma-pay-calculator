/**
 * Result-moment email capture (portfolio standard, July 2026)
 * Reveals the #result-capture block when the calculator's #results div
 * gets the 'show' class, and submits email signups via the Beehiiv
 * magic link (same list as sqh-newsletter.js).
 */
(function () {
  'use strict';

  var MAGIC = 'https://magic.beehiiv.com/v1/3b13f050-475f-42fa-b944-76bf00acb3eb';

  function init() {
    var block = document.getElementById('result-capture');
    var results = document.getElementById('results');
    if (!block) return;

    var source = block.getAttribute('data-source') || 'plasmapaycalculator.com (result)';
    var utmContent = block.getAttribute('data-utm-content') || '';

    function reveal() {
      block.hidden = false;
    }

    if (results) {
      // Main calculators reveal #results with .show; programmatic state
      // calculators reveal it by removing .hidden.
      var startedHidden = results.classList.contains('hidden');
      if (results.classList.contains('show')) {
        reveal();
      } else {
        var observer = new MutationObserver(function () {
          if (
            results.classList.contains('show') ||
            (startedHidden && !results.classList.contains('hidden'))
          ) {
            reveal();
            observer.disconnect();
          }
        });
        observer.observe(results, { attributes: true, attributeFilter: ['class'] });
      }
    }

    // Programmatic pages without a hidden #results update an always-visible
    // panel from an inline onclick handler: reveal on that click instead.
    var calcButtons = document.querySelectorAll(
      '[onclick^="calculateEarnings"], [onclick^="calculateCityEarnings"]'
    );
    for (var i = 0; i < calcButtons.length; i++) {
      calcButtons[i].addEventListener('click', reveal);
    }

    var form = block.querySelector('form');
    if (!form) return;

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var honeypot = form.querySelector('[name="company_website"]');
      var emailInput = form.querySelector('[name="email"]');
      var email = emailInput ? emailInput.value.trim() : '';

      if ((!honeypot || !honeypot.value) && email) {
        var url = MAGIC + '?email=' + encodeURIComponent(email) +
          '&utm_source=plasmapaycalculator&utm_medium=result_block';
        if (utmContent) {
          url += '&utm_content=' + encodeURIComponent(utmContent);
        }
        window.open(url, '_blank');
        if (window.gtag) {
          gtag('event', 'email_capture', { method: 'result_block', source: source });
        }
      }

      // Static success state only. Never interpolate user input into markup.
      var lead = block.querySelector('.rc-lead');
      var success = block.querySelector('.rc-success');
      if (lead) lead.hidden = true;
      if (success) success.hidden = false;
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
