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
    if (!block || !results) return;

    var source = block.getAttribute('data-source') || 'plasmapaycalculator.com (result)';

    function reveal() {
      block.hidden = false;
    }

    if (results.classList.contains('show')) {
      reveal();
    } else {
      var observer = new MutationObserver(function () {
        if (results.classList.contains('show')) {
          reveal();
          observer.disconnect();
        }
      });
      observer.observe(results, { attributes: true, attributeFilter: ['class'] });
    }

    var form = block.querySelector('form');
    if (!form) return;

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var honeypot = form.querySelector('[name="company_website"]');
      var emailInput = form.querySelector('[name="email"]');
      var email = emailInput ? emailInput.value.trim() : '';

      if ((!honeypot || !honeypot.value) && email) {
        window.open(
          MAGIC + '?email=' + encodeURIComponent(email) +
          '&utm_source=plasmapaycalculator&utm_medium=result_block',
          '_blank'
        );
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
