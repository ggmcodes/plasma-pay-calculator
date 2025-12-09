/**
 * Partners Rendering Engine
 * Injects partner cards into pages based on configuration
 *
 * Usage: Partners.init('pageType')
 * Example: Partners.init('homepage')
 */

(function() {
  'use strict';

  // Check if partners system is enabled globally
  if (!window.PartnersConfig || !window.PartnersConfig.enabled) {
    return;
  }

  const Partners = {
    /**
     * Render partner card HTML
     * @param {string} partnerKey - Partner identifier (e.g., 'olgam')
     * @param {string} placementKey - Placement identifier (e.g., 'homepage')
     * @returns {string|null} HTML string or null if disabled
     */
    renderCard: function(partnerKey, placementKey) {
      const config = window.PartnersConfig.partners[partnerKey];
      if (!config) return null;

      const placement = config.placements[placementKey];
      if (!placement) return null;

      // Check if this specific placement is enabled
      if (!config.enabled || !placement.enabled) {
        return null;
      }

      const trackingUrl = window.PartnersConfig.buildTrackingUrl(partnerKey, placementKey);

      // Build card HTML using Tailwind CSS classes
      return `
        <section class="bg-gradient-to-r from-[${config.colors.tertiary}] to-[${config.colors.primary}] py-8 md:py-12 border-y border-gray-200">
          <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="bg-white rounded-xl shadow-xl overflow-hidden">
              <div class="grid md:grid-cols-3 gap-6 md:gap-8 items-center p-6 md:p-8">

                <!-- Badge + Logo Column -->
                <div class="flex flex-col items-center md:items-start space-y-3">
                  <div class="bg-[${config.colors.secondary}] text-[${config.colors.tertiary}] px-3 py-1 rounded-full text-xs font-bold uppercase tracking-wide">
                    ${config.copy.badge}
                  </div>
                  <div class="w-32 h-32 md:w-40 md:h-40 flex items-center justify-center">
                    <img src="${config.logo.url}" alt="${config.logo.alt}" class="max-w-full max-h-full object-contain" />
                  </div>
                </div>

                <!-- Headline Column -->
                <div class="text-center md:text-left md:col-span-1">
                  <h3 class="text-2xl md:text-3xl font-bold text-gray-900 mb-2">
                    ${config.copy.headline}
                  </h3>
                  <p class="text-gray-600 text-sm">
                    ${config.copy.subtext}
                  </p>
                </div>

                <!-- CTA Column -->
                <div class="flex justify-center md:justify-end">
                  <a href="${trackingUrl}"
                     target="_blank"
                     rel="noopener noreferrer"
                     onclick="Partners.trackClick('${partnerKey}', '${placementKey}'); return true;"
                     class="bg-gradient-to-r from-[${config.colors.primary}] to-[${config.colors.tertiary}] hover:from-[${config.colors.tertiary}] hover:to-[${config.colors.primary}] text-white px-8 py-4 rounded-lg font-bold text-lg shadow-lg hover:shadow-xl transform hover:-translate-y-1 transition-all duration-300 inline-flex items-center gap-2">
                    ${config.copy.cta}
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
                    </svg>
                  </a>
                </div>

              </div>
            </div>
          </div>
        </section>
      `;
    },

    /**
     * Track partner click event via GA4
     * @param {string} partnerKey - Partner identifier
     * @param {string} placementKey - Placement identifier
     */
    trackClick: function(partnerKey, placementKey) {
      const config = window.PartnersConfig.partners[partnerKey];
      if (!config) return;

      const placement = config.placements[placementKey];
      if (!placement) return;

      // Check if gtag exists (GA4)
      if (typeof gtag === 'function') {
        gtag('event', 'click', {
          event_category: 'partner_click',
          event_label: placement.gaLabel,
          partner: partnerKey,
          placement: placementKey,
          value: 1
        });

        // Optional: Console log for debugging
        if (console && console.log) {
          console.log('Partner click tracked:', {
            category: 'partner_click',
            label: placement.gaLabel,
            partner: partnerKey,
            placement: placementKey
          });
        }
      }
    },

    /**
     * Inject partner card into page at specified position
     * @param {string} partnerKey - Partner identifier
     * @param {string} placementKey - Placement identifier
     * @param {string} targetSelector - CSS selector for target element
     * @param {string} position - Position relative to target ('afterend', 'beforebegin', etc.)
     */
    inject: function(partnerKey, placementKey, targetSelector, position) {
      position = position || 'afterend';

      const cardHtml = this.renderCard(partnerKey, placementKey);
      if (!cardHtml) return;

      const target = document.querySelector(targetSelector);
      if (target) {
        target.insertAdjacentHTML(position, cardHtml);
      } else {
        // Log warning if target not found (for debugging)
        if (console && console.warn) {
          console.warn('Partner injection failed: Target not found', {
            selector: targetSelector,
            partner: partnerKey,
            placement: placementKey
          });
        }
      }
    },

    /**
     * Initialize partner placements for current page
     * @param {string} pageType - Type of page (homepage, centersDirectory, nyState, etc.)
     */
    init: function(pageType) {
      // Wait for DOM to be ready
      if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', () => this.init(pageType));
        return;
      }

      // Page-specific injection logic
      const injections = {
        homepage: () => {
          // After hero section, before calculator
          // Try multiple selectors to find the hero
          const heroSelectors = [
            '.header',
            'div.header',
            'main .container .header'
          ];

          for (const selector of heroSelectors) {
            const hero = document.querySelector(selector);
            if (hero) {
              this.inject('olgam', 'homepage', selector, 'afterend');
              break;
            }
          }
        },

        centersDirectory: () => {
          // After hero section, before center listings
          const heroSelectors = [
            'section.relative.min-h-\\[100vh\\]',
            'section.bg-gray-800',
            'section.text-center.bg-gray-800'
          ];

          for (const selector of heroSelectors) {
            const hero = document.querySelector(selector);
            if (hero) {
              this.inject('olgam', 'centersDirectory', selector, 'afterend');
              break;
            }
          }
        },

        nyState: () => {
          // After hero section
          const heroSelectors = [
            'section.relative.min-h-\\[60vh\\]',
            'section.relative.min-h-\\[50vh\\]',
            'section[class*="min-h"]'
          ];

          for (const selector of heroSelectors) {
            const hero = document.querySelector(selector);
            if (hero) {
              this.inject('olgam', 'nyState', selector, 'afterend');
              break;
            }
          }
        },

        nycCity: () => {
          // After hero section, before Quick Action CTA
          const heroSelectors = [
            'section.relative.min-h-\\[50vh\\]',
            'section.relative.min-h-\\[60vh\\]',
            'section[class*="min-h"]'
          ];

          for (const selector of heroSelectors) {
            const hero = document.querySelector(selector);
            if (hero) {
              this.inject('olgam', 'nycCity', selector, 'afterend');
              break;
            }
          }
        },

        njState: () => {
          // After hero section
          const heroSelectors = [
            'section.relative.min-h-\\[60vh\\]',
            'section.relative.min-h-\\[50vh\\]',
            'section[class*="min-h"]'
          ];

          for (const selector of heroSelectors) {
            const hero = document.querySelector(selector);
            if (hero) {
              this.inject('olgam', 'njState', selector, 'afterend');
              break;
            }
          }
        },

        newark: () => {
          const heroSelectors = [
            'section.relative.min-h-\\[50vh\\]',
            'section.relative.min-h-\\[60vh\\]',
            'section[class*="min-h"]'
          ];

          for (const selector of heroSelectors) {
            const hero = document.querySelector(selector);
            if (hero) {
              this.inject('olgam', 'newark', selector, 'afterend');
              break;
            }
          }
        },

        jerseyCity: () => {
          const heroSelectors = [
            'section.relative.min-h-\\[50vh\\]',
            'section.relative.min-h-\\[60vh\\]',
            'section[class*="min-h"]'
          ];

          for (const selector of heroSelectors) {
            const hero = document.querySelector(selector);
            if (hero) {
              this.inject('olgam', 'jerseyCity', selector, 'afterend');
              break;
            }
          }
        },

        elizabeth: () => {
          const heroSelectors = [
            'section.relative.min-h-\\[50vh\\]',
            'section.relative.min-h-\\[60vh\\]',
            'section[class*="min-h"]'
          ];

          for (const selector of heroSelectors) {
            const hero = document.querySelector(selector);
            if (hero) {
              this.inject('olgam', 'elizabeth', selector, 'afterend');
              break;
            }
          }
        },

        paterson: () => {
          const heroSelectors = [
            'section.relative.min-h-\\[50vh\\]',
            'section.relative.min-h-\\[60vh\\]',
            'section[class*="min-h"]'
          ];

          for (const selector of heroSelectors) {
            const hero = document.querySelector(selector);
            if (hero) {
              this.inject('olgam', 'paterson', selector, 'afterend');
              break;
            }
          }
        },

        edison: () => {
          const heroSelectors = [
            'section.relative.min-h-\\[50vh\\]',
            'section.relative.min-h-\\[60vh\\]',
            'section[class*="min-h"]'
          ];

          for (const selector of heroSelectors) {
            const hero = document.querySelector(selector);
            if (hero) {
              this.inject('olgam', 'edison', selector, 'afterend');
              break;
            }
          }
        },

        manhattan: () => {
          const heroSelectors = [
            'section.relative.min-h-\\[50vh\\]',
            'section.relative.min-h-\\[60vh\\]',
            'section[class*="min-h"]'
          ];

          for (const selector of heroSelectors) {
            const hero = document.querySelector(selector);
            if (hero) {
              this.inject('olgam', 'manhattan', selector, 'afterend');
              break;
            }
          }
        },

        brooklyn: () => {
          const heroSelectors = [
            'section.relative.min-h-\\[50vh\\]',
            'section.relative.min-h-\\[60vh\\]',
            'section[class*="min-h"]'
          ];

          for (const selector of heroSelectors) {
            const hero = document.querySelector(selector);
            if (hero) {
              this.inject('olgam', 'brooklyn', selector, 'afterend');
              break;
            }
          }
        },

        queens: () => {
          const heroSelectors = [
            'section.relative.min-h-\\[50vh\\]',
            'section.relative.min-h-\\[60vh\\]',
            'section[class*="min-h"]'
          ];

          for (const selector of heroSelectors) {
            const hero = document.querySelector(selector);
            if (hero) {
              this.inject('olgam', 'queens', selector, 'afterend');
              break;
            }
          }
        },

        bronx: () => {
          const heroSelectors = [
            'section.relative.min-h-\\[50vh\\]',
            'section.relative.min-h-\\[60vh\\]',
            'section[class*="min-h"]'
          ];

          for (const selector of heroSelectors) {
            const hero = document.querySelector(selector);
            if (hero) {
              this.inject('olgam', 'bronx', selector, 'afterend');
              break;
            }
          }
        },

        statenIsland: () => {
          const heroSelectors = [
            'section.relative.min-h-\\[50vh\\]',
            'section.relative.min-h-\\[60vh\\]',
            'section[class*="min-h"]'
          ];

          for (const selector of heroSelectors) {
            const hero = document.querySelector(selector);
            if (hero) {
              this.inject('olgam', 'statenIsland', selector, 'afterend');
              break;
            }
          }
        }
      };

      // Execute injection for this page type
      if (injections[pageType]) {
        injections[pageType]();
      }
    }
  };

  // Expose Partners object globally
  window.Partners = Partners;

})();
