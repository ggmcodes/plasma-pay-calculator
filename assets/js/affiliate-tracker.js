/**
 * Affiliate Click Tracker (canonical)
 *
 * Delegated, capture-phase click listener that fires a GA4 `affiliate_click`
 * event for affiliate links. Uses transport_type:'beacon' so the event
 * survives the navigation away (sendBeacon is not dropped when the page
 * unloads). Reuses the page's existing gtag/GA4 tag; does NOT load a second one.
 *
 * Matches:
 *   - Amazon links (amazon.* / amzn.to)
 *   - MaxBounty links (afflat3c*.com / mb0*.com) and ANY link tagged with
 *     data-affiliate-network (e.g. data-affiliate-network="maxbounty"
 *     data-offer-id="31078").
 *
 * In GA4 Admin -> Events, mark `affiliate_click` as a Key Event for conversions.
 */
(function () {
  "use strict";

  var MAXBOUNTY_RE = /afflat3c\d?\.com|mb0\d\.com|maxbounty/i;
  var AMAZON_RE = /(^|\/\/|\.)amazon\.|amzn\.to/i;

  function findAffiliateLink(el) {
    while (el && el !== document) {
      if (el.tagName === "A" && el.href &&
          (el.hasAttribute("data-affiliate-network") ||
           AMAZON_RE.test(el.href) || MAXBOUNTY_RE.test(el.href))) {
        return el;
      }
      el = el.parentNode;
    }
    return null;
  }

  function extractAsin(url) {
    var m = url.match(/\/(?:dp|gp\/product)\/([A-Z0-9]{10})/i);
    return m ? m[1] : "";
  }

  function fire(a) {
    if (!a || typeof window.gtag !== "function") return;
    var network = a.getAttribute("data-affiliate-network") ||
      (MAXBOUNTY_RE.test(a.href) ? "maxbounty" :
       AMAZON_RE.test(a.href) ? "amazon" : "other");
    var text = (a.getAttribute("data-link-text") || a.textContent || "")
      .trim().replace(/\s+/g, " ").slice(0, 100);
    var params = {
      transport_type: "beacon",
      link_url: a.href,
      affiliate_network: network,
      link_text: text,
      page_path: location.pathname
    };
    var offer = a.getAttribute("data-offer-id");
    if (offer) params.offer_id = offer;
    if (network === "amazon") {
      params.link_domain = "amazon.com";
      params.product_asin = extractAsin(a.href);
    }
    window.gtag("event", "affiliate_click", params);
  }

  document.addEventListener("click", function (e) {
    fire(findAffiliateLink(e.target));
  }, true);

  // Middle-click / cmd-click opens in a new tab (auxclick).
  document.addEventListener("auxclick", function (e) {
    if (e.button === 1) fire(findAffiliateLink(e.target));
  }, true);
})();
