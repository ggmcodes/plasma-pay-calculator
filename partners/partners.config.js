/**
 * Partners Configuration System
 * Central configuration for all partner placements with feature flags
 *
 * To disable ALL placements: Set enabled to false
 * To disable individual placements: Set specific placement.enabled to false
 */

window.PartnersConfig = {
  // MASTER SWITCH - Set to false to disable ALL partner placements instantly
  enabled: true,

  // Individual partner configurations
  partners: {
    olgam: {
      // Partner-level toggle
      enabled: true,

      // Partner details
      name: 'Olgam Life',

      // Logo configuration
      logo: {
        url: '/partners/assets/olgam-logo.png',
        alt: 'Olgam Life logo'
      },

      // Olgam brand colors
      colors: {
        primary: '#5BC4F0',    // Blue
        secondary: '#FFE81F',  // Yellow
        tertiary: '#3B2654'    // Purple
      },

      // Copy/messaging
      copy: {
        badge: 'Featured Partner',
        headline: 'Earn $500+/month at Olgam Life NYC locations',
        subtext: 'Multiple convenient NYC locations • Competitive rates • Fast payouts',
        cta: 'Find Locations'
      },

      // Base URL for partner links
      baseUrl: 'https://olgam.com/our-locations/',

      // Page-specific placement configurations
      placements: {
        homepage: {
          enabled: true,
          utmCampaign: 'homepage-featured',
          gaLabel: 'olgam_homepage'
        },
        centersDirectory: {
          enabled: true,
          utmCampaign: 'centers-directory',
          gaLabel: 'olgam_centers'
        },
        nyState: {
          enabled: true,
          utmCampaign: 'ny-state-page',
          gaLabel: 'olgam_nypage'
        },
        nycCity: {
          enabled: true,
          utmCampaign: 'nyc-page',
          gaLabel: 'olgam_nycpage'
        },
        njState: {
          enabled: true,
          utmCampaign: 'nj-state-page',
          gaLabel: 'olgam_njpage'
        },
        newark: {
          enabled: true,
          utmCampaign: 'newark-page',
          gaLabel: 'olgam_newark'
        },
        jerseyCity: {
          enabled: true,
          utmCampaign: 'jersey-city-page',
          gaLabel: 'olgam_jerseycity'
        },
        elizabeth: {
          enabled: true,
          utmCampaign: 'elizabeth-page',
          gaLabel: 'olgam_elizabeth'
        },
        paterson: {
          enabled: true,
          utmCampaign: 'paterson-page',
          gaLabel: 'olgam_paterson'
        },
        edison: {
          enabled: true,
          utmCampaign: 'edison-page',
          gaLabel: 'olgam_edison'
        },
        manhattan: {
          enabled: true,
          utmCampaign: 'manhattan-page',
          gaLabel: 'olgam_manhattan'
        },
        brooklyn: {
          enabled: true,
          utmCampaign: 'brooklyn-page',
          gaLabel: 'olgam_brooklyn'
        },
        queens: {
          enabled: true,
          utmCampaign: 'queens-page',
          gaLabel: 'olgam_queens'
        },
        bronx: {
          enabled: true,
          utmCampaign: 'bronx-page',
          gaLabel: 'olgam_bronx'
        },
        statenIsland: {
          enabled: true,
          utmCampaign: 'staten-island-page',
          gaLabel: 'olgam_statenisland'
        }
      }
    }
  },

  // UTM parameter configuration
  utm: {
    source: 'plasmapaycalculator',
    medium: 'referral'
  },

  /**
   * Build tracking URL with UTM parameters
   * @param {string} partner - Partner key (e.g., 'olgam')
   * @param {string} placement - Placement key (e.g., 'homepage')
   * @returns {string} Full URL with UTM parameters
   */
  buildTrackingUrl: function(partner, placement) {
    const config = this.partners[partner];
    if (!config) return '';

    const placementConfig = config.placements[placement];
    if (!placementConfig) return config.baseUrl;

    const params = new URLSearchParams({
      utm_source: this.utm.source,
      utm_medium: this.utm.medium,
      utm_campaign: placementConfig.utmCampaign
    });

    return `${config.baseUrl}?${params.toString()}`;
  }
};
