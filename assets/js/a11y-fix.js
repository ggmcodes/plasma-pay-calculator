/**
 * Universal Accessibility Fix Script
 * Auto-fixes common a11y issues on page load:
 * - Inputs/selects/textareas without associated labels
 * - Buttons without accessible text
 * - Links with generic text
 * - Beehiiv newsletter iframes without labels
 *
 * Idempotent: safe to run multiple times without duplicating attributes.
 */
(function () {
  'use strict';

  /** Generic link text patterns (case-insensitive). */
  var GENERIC_LINK_RE = /^(click here|read more|learn more|here|more|go|see more|view more|details|link|info)\.?$/i;

  /**
   * Derive a human-readable label from an element's attributes.
   * Priority: placeholder > name > id > type.
   */
  function deriveLabel(el) {
    if (el.placeholder) {
      return el.placeholder;
    }
    if (el.name) {
      return formatName(el.name);
    }
    if (el.id) {
      return formatName(el.id);
    }
    var tag = el.tagName.toLowerCase();
    if (tag === 'select') return 'Selection';
    if (tag === 'textarea') return 'Text input';
    if (el.type === 'email') return 'Email address';
    if (el.type === 'search') return 'Search';
    if (el.type === 'tel') return 'Phone number';
    if (el.type === 'url') return 'URL';
    if (el.type === 'number') return 'Number input';
    if (el.type === 'password') return 'Password';
    if (el.type === 'date') return 'Date';
    if (el.type === 'range') return 'Range slider';
    if (el.type === 'checkbox') return 'Checkbox';
    if (el.type === 'radio') return 'Radio option';
    return 'Input';
  }

  /**
   * Turn a camelCase / kebab-case / snake_case name into words.
   */
  function formatName(str) {
    return str
      .replace(/([a-z])([A-Z])/g, '$1 $2')
      .replace(/[-_]+/g, ' ')
      .replace(/\b\w/g, function (c) { return c.toUpperCase(); })
      .trim();
  }

  /**
   * Check whether an element already has an accessible name via
   * <label>, aria-label, or aria-labelledby.
   */
  function hasAccessibleName(el) {
    if (el.getAttribute('aria-label')) return true;
    if (el.getAttribute('aria-labelledby')) return true;
    if (el.id && document.querySelector('label[for="' + CSS.escape(el.id) + '"]')) return true;
    // Check if wrapped inside a <label>
    var parent = el.parentElement;
    while (parent) {
      if (parent.tagName === 'LABEL') return true;
      parent = parent.parentElement;
    }
    return false;
  }

  /**
   * Find the nearest heading or meaningful text near an anchor for context.
   */
  function getContextForLink(el) {
    // Walk up to find a heading sibling or parent heading
    var parent = el.parentElement;
    for (var i = 0; i < 5 && parent; i++) {
      var heading = parent.querySelector('h1, h2, h3, h4, h5, h6');
      if (heading && heading.textContent.trim()) {
        return heading.textContent.trim();
      }
      parent = parent.parentElement;
    }
    // Try title attribute
    if (el.title) return el.title;
    // Try href for last resort context
    if (el.href) {
      var path = el.pathname || '';
      var slug = path.split('/').filter(Boolean).pop();
      if (slug) {
        return formatName(slug.replace(/\.\w+$/, ''));
      }
    }
    return '';
  }

  function fixFormControls() {
    var controls = document.querySelectorAll('input, select, textarea');
    for (var i = 0; i < controls.length; i++) {
      var el = controls[i];
      // Skip hidden and submit/button inputs
      if (el.type === 'hidden' || el.type === 'submit' || el.type === 'button') continue;
      if (hasAccessibleName(el)) continue;
      el.setAttribute('aria-label', deriveLabel(el));
    }
  }

  function fixButtons() {
    var buttons = document.querySelectorAll('button');
    for (var i = 0; i < buttons.length; i++) {
      var btn = buttons[i];
      if (btn.getAttribute('aria-label')) continue;
      if (btn.getAttribute('aria-labelledby')) continue;
      var text = btn.textContent.trim();
      if (text) continue; // Has visible text already
      // Try title
      if (btn.title) {
        btn.setAttribute('aria-label', btn.title);
        continue;
      }
      // Try img alt inside button
      var img = btn.querySelector('img');
      if (img && img.alt) {
        btn.setAttribute('aria-label', img.alt);
        continue;
      }
      // Try SVG title
      var svgTitle = btn.querySelector('svg title');
      if (svgTitle && svgTitle.textContent.trim()) {
        btn.setAttribute('aria-label', svgTitle.textContent.trim());
        continue;
      }
      // Generic fallback
      btn.setAttribute('aria-label', 'Button');
    }
  }

  function fixGenericLinks() {
    var links = document.querySelectorAll('a');
    for (var i = 0; i < links.length; i++) {
      var a = links[i];
      if (a.getAttribute('aria-label')) continue;
      var text = a.textContent.trim();
      if (!GENERIC_LINK_RE.test(text)) continue;
      var context = getContextForLink(a);
      if (context) {
        a.setAttribute('aria-label', text + ' - ' + context);
      }
    }
  }

  function fixBeehiivIframes() {
    var iframes = document.querySelectorAll('iframe');
    for (var i = 0; i < iframes.length; i++) {
      var iframe = iframes[i];
      if (iframe.getAttribute('aria-label')) continue;
      if (iframe.getAttribute('title')) continue;
      var src = iframe.getAttribute('src') || '';
      if (src.indexOf('beehiiv') !== -1) {
        iframe.setAttribute('aria-label', 'Newsletter signup form');
        iframe.setAttribute('title', 'Newsletter signup form');
      }
    }
  }

  function run() {
    fixFormControls();
    fixButtons();
    fixGenericLinks();
    fixBeehiivIframes();
  }

  // Run when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', run);
  } else {
    run();
  }
})();
