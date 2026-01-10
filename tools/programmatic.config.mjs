/**
 * Programmatic SEO Configuration
 *
 * This file defines all calculators for programmatic page generation.
 * Each calculator includes curated input grids designed to create
 * high-intent, meaningful pages without thin/duplicate content.
 *
 * SAFETY LIMITS:
 * - DEFAULT_MAX_PAGES: 800 (conservative limit)
 * - All combinations are validated before generation
 * - Deduplication is performed based on output buckets
 */

import {
  calculatePlasmaEarnings,
  validateInputs,
  getEarningsTier,
  compareCenters,
  centerNames,
  stateNames,
  weightRangeNames,
  donorTypeNames,
  paymentRates
} from '../js/engine/plasmaPayEngine.mjs';

import {
  calculatePlasmaTax,
  validateTaxInputs,
  getTaxScenario,
  filingStatusNames,
  getDeductibleExpenses
} from '../js/engine/plasmaTaxEngine.mjs';

import {
  formatCurrency,
  formatNumber,
  formatPercent,
  slugify,
  getSiteUrl,
  getCurrentYear
} from './lib/utils.mjs';

import {
  renderFaq,
  renderRelatedLinks,
  generateFaqSchema,
  generateAppSchema,
  generateBreadcrumbSchema
} from './lib/render.mjs';

// ============================================================================
// GLOBAL CONFIGURATION
// ============================================================================

export const DEFAULT_MAX_PAGES = 800;
export const SITE_URL = getSiteUrl();

// ============================================================================
// PLASMA PAY CALCULATOR CONFIG
// ============================================================================

const plasmaPayConfig = {
  id: 'plasma-pay',
  interactivePath: '/',
  outBase: 'p/plasma-pay',

  // Curated input grid - focused on high-intent combinations
  // Centers: 6 major centers with distinct rates
  // States: 5 high-volume states with meaningful multiplier differences
  // Weights: All 4 ranges (significant pay differences)
  // Donor types: Focus on new (highest intent) and returning (ongoing value)
  inputGrid: {
    center: ['csl', 'biolife', 'octapharma', 'grifols', 'kedplasma', 'bpl'],
    donorType: ['new', 'returning'],
    weightRange: ['110-149', '150-174', '175-200', '200+'],
    state: ['CA', 'TX', 'FL', 'NY', 'OH'], // High volume + varied multipliers
    frequency: [2] // Default to max frequency for returning donors
  },

  /**
   * Validate input combination
   * Skip invalid or low-quality combinations
   */
  validate(inputs) {
    const result = validateInputs(inputs);
    if (!result.valid) return false;

    // All curated combinations are valid
    return true;
  },

  /**
   * Compute earnings for inputs
   */
  compute(inputs) {
    return calculatePlasmaEarnings(inputs);
  },

  /**
   * Generate canonical key for deduplication
   * Based on output buckets, not exact values
   */
  canonicalKey(inputs, outputs) {
    // Bucket monthly net into ranges for dedup
    const monthlyBucket = Math.floor(outputs.monthlyNet / 50) * 50; // $50 buckets
    return `${inputs.center}-${inputs.donorType}-${inputs.weightRange}-${monthlyBucket}`;
  },

  /**
   * Generate URL slug
   */
  slug(inputs, outputs) {
    const { center, donorType, weightRange, state } = inputs;
    const centerSlug = centerNames[center]?.toLowerCase().replace(/\s+/g, '-') || center;
    const stateSlug = stateNames[state]?.toLowerCase().replace(/\s+/g, '-') || state.toLowerCase();
    const weightSlug = weightRange.replace('+', '-plus').replace(/\s+/g, '');
    const typeSlug = donorType === 'new' ? 'new-donor' : 'returning-donor';

    return `${centerSlug}-${typeSlug}-${weightSlug}-${stateSlug}`;
  },

  /**
   * Generate page title
   */
  pageTitle(inputs, outputs) {
    const { center, donorType, weightRange, state } = inputs;
    const year = getCurrentYear();
    const centerName = centerNames[center] || center;
    const stateName = stateNames[state] || state;
    const typeLabel = donorType === 'new' ? 'New Donor' : 'Returning Donor';

    return `${centerName} ${typeLabel} Pay ${year}: ${weightRangeNames[weightRange]} in ${stateName} | Earn ${formatCurrency(outputs.monthlyNet)}/Month`;
  },

  /**
   * Generate meta description
   */
  metaDescription(inputs, outputs) {
    const { center, donorType, weightRange, state } = inputs;
    const centerName = centerNames[center] || center;
    const stateName = stateNames[state] || state;
    const typeLabel = donorType === 'new' ? 'new donor' : 'returning donor';

    return `Calculate ${centerName} plasma donation pay for ${typeLabel}s weighing ${weightRangeNames[weightRange]} in ${stateName}. Earn ${formatCurrency(outputs.monthlyNet)}/month (${formatCurrency(outputs.yearlyNet)}/year) after taxes.`;
  },

  /**
   * Generate hero HTML
   */
  heroHtml(inputs, outputs) {
    const { center, donorType, weightRange, state } = inputs;
    const centerName = centerNames[center] || center;
    const stateName = stateNames[state] || state;
    const typeLabel = donorTypeNames[donorType] || donorType;
    const year = getCurrentYear();

    return `
      <h1>${centerName} Pay Calculator ${year}: ${typeLabel} in ${stateName}</h1>
      <p>Accurate earnings estimate for donors weighing ${weightRangeNames[weightRange]} donating at ${centerName} locations in ${stateName}.</p>
    `;
  },

  /**
   * Generate summary HTML with computed values
   */
  summaryHtml(inputs, outputs) {
    const { center, donorType, weightRange, state } = inputs;
    const centerName = centerNames[center] || center;
    const stateName = stateNames[state] || state;
    const tier = getEarningsTier(outputs.monthlyNet);

    const bonusNote = donorType === 'new' && outputs.firstMonthBonus > 0
      ? `<p style="margin-top: 1rem; padding: 1rem; background: #fef3c7; border-radius: 8px;"><strong>New Donor Bonus:</strong> First-month earnings include approximately ${formatCurrency(outputs.firstMonthBonus)} in new donor promotional rates!</p>`
      : '';

    return `
      <h2 class="card-title">Your Estimated Earnings at ${centerName}</h2>
      <div class="result-box">
        <div class="label">Monthly Net Earnings (After Taxes)</div>
        <div class="amount">${formatCurrency(outputs.monthlyNet)}</div>
      </div>

      <div class="results-grid">
        <div class="result-item">
          <div class="value">${formatCurrency(outputs.weeklyNet)}</div>
          <div class="label">Weekly Net</div>
        </div>
        <div class="result-item">
          <div class="value">${formatCurrency(outputs.yearlyNet)}</div>
          <div class="label">Yearly Net</div>
        </div>
        <div class="result-item">
          <div class="value">${formatCurrency(outputs.perVisitGross)}</div>
          <div class="label">Per Visit (Gross)</div>
        </div>
        <div class="result-item">
          <div class="value">${outputs.donationsPerMonth}</div>
          <div class="label">Donations/Month</div>
        </div>
      </div>

      <p style="margin-top: 1rem;">
        As a <strong>${donorTypeNames[donorType]?.toLowerCase() || donorType}</strong> weighing <strong>${weightRangeNames[weightRange]}</strong> donating at <strong>${centerName}</strong> in <strong>${stateName}</strong>, you can expect to earn approximately <strong>${formatCurrency(outputs.monthlyGross)}</strong> gross per month. After estimated taxes (${formatPercent(outputs.taxRate)}) and travel costs, your net take-home is around <strong>${formatCurrency(outputs.monthlyNet)}</strong> monthly.
      </p>

      ${bonusNote}

      <p style="margin-top: 1rem; padding: 1rem; background: #f0fdfa; border-radius: 8px;">
        <strong>${tier.label}:</strong> ${tier.description}
      </p>
    `;
  },

  /**
   * Generate comparison table HTML
   */
  tableHtml(inputs, outputs) {
    const { center, donorType, weightRange, state } = inputs;

    // Compare across centers for same donor profile
    const comparisons = compareCenters({
      donorType,
      weightRange,
      state,
      frequency: 2
    });

    const rows = comparisons.map(c => {
      const isCurrent = c.center === center;
      return `
        <tr class="${isCurrent ? 'current' : ''}">
          <td>${c.centerName}</td>
          <td style="font-family: 'Space Mono', monospace;">${formatCurrency(c.perVisitGross)}</td>
          <td style="font-family: 'Space Mono', monospace;">${formatCurrency(c.monthlyNet)}</td>
          <td style="font-family: 'Space Mono', monospace;">${formatCurrency(c.yearlyNet)}</td>
        </tr>
      `;
    }).join('');

    return `
      <h2 class="card-title">Compare Centers for ${weightRangeNames[weightRange]} ${donorTypeNames[donorType]}s in ${stateNames[state]}</h2>
      <p style="margin-bottom: 1rem; color: var(--slate);">Based on donating twice weekly. Your current selection is highlighted.</p>
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Center</th>
            <th>Per Visit</th>
            <th>Monthly Net</th>
            <th>Yearly Net</th>
          </tr>
        </thead>
        <tbody>
          ${rows}
        </tbody>
      </table>
    `;
  },

  /**
   * Generate FAQ items specific to this scenario
   */
  faqItems(inputs, outputs) {
    const { center, donorType, weightRange, state } = inputs;
    const centerName = centerNames[center] || center;
    const stateName = stateNames[state] || state;
    const year = getCurrentYear();

    return [
      {
        q: `How much does ${centerName} pay per donation in ${stateName}?`,
        a: `${centerName} pays approximately <strong>${formatCurrency(outputs.perVisitGross)}</strong> per visit for donors weighing ${weightRangeNames[weightRange]} in ${stateName}. This varies based on promotional periods and donation frequency.`
      },
      {
        q: `How much can I make monthly donating plasma at ${centerName}?`,
        a: `Donating twice weekly at ${centerName} in ${stateName}, donors weighing ${weightRangeNames[weightRange]} can earn approximately <strong>${formatCurrency(outputs.monthlyGross)}</strong> gross or <strong>${formatCurrency(outputs.monthlyNet)}</strong> after estimated taxes and travel costs.`
      },
      {
        q: `What are the weight requirements for plasma donation at ${centerName}?`,
        a: `You must weigh at least 110 lbs to donate plasma. Higher weight donors (${weightRangeNames[weightRange]}) often receive higher compensation because they can donate more plasma volume per session.`
      },
      {
        q: `How often can I donate plasma at ${centerName}?`,
        a: `You can donate plasma up to <strong>twice per week</strong> with at least 48 hours between donations. This means approximately ${outputs.donationsPerMonth} donations per month for maximum earnings.`
      },
      {
        q: `Is plasma donation income taxable in ${stateName}?`,
        a: `Yes, plasma donation income is considered taxable self-employment income. We've estimated ${formatPercent(outputs.taxRate)} for taxes in our calculations. Centers issue 1099 forms for earnings over $600/year.`
      },
      {
        q: `${donorType === 'new' ? 'What bonuses do new donors get at ' + centerName + '?' : 'Do returning donors get bonuses at ' + centerName + '?'}`,
        a: donorType === 'new'
          ? `New donors at ${centerName} typically receive enhanced rates during their first month, potentially earning ${formatCurrency(outputs.firstMonthBonus)} more than regular rates. Contact your local center for current promotions.`
          : `Returning donors at ${centerName} can earn bonuses through referral programs (${formatCurrency(75)} per referral), loyalty promotions, and special weekly/monthly incentives.`
      },
      {
        q: `How long does a plasma donation take at ${centerName}?`,
        a: `First-time donations take 2-3 hours including screening and physical. Subsequent donations typically take 45-90 minutes. The donation itself is about 35-45 minutes depending on your plasma volume.`
      },
      {
        q: `What do I need to bring to ${centerName} for my first donation?`,
        a: `Bring a valid photo ID, proof of address (utility bill or bank statement from last 30 days), and your Social Security card. Make sure you're well-hydrated and have eaten protein before your visit.`
      }
    ];
  },

  /**
   * Generate CTA HTML
   */
  ctaHtml(inputs, outputs) {
    const { center, donorType, weightRange, state } = inputs;
    const params = new URLSearchParams({
      center,
      donorType,
      weight: weightRange,
      state
    }).toString();

    return `
      <h3 style="margin-bottom: 1rem;">Calculate Your Exact Earnings</h3>
      <p style="margin-bottom: 1.5rem; color: var(--slate);">Use our interactive calculator with your specific details for a personalized estimate.</p>
      <a href="/?${params}" class="cta-button">Open Interactive Calculator</a>
    `;
  },

  /**
   * Generate related links
   */
  relatedLinks(inputs, outputs) {
    const { center, state, donorType } = inputs;
    const links = [
      { href: '/', label: 'Main Calculator' },
      { href: '/faq.html', label: 'Plasma Donation FAQ' }
    ];

    // Add center-specific links
    if (center === 'csl') {
      links.push({ href: '/csl-plasma-pay-chart-2026.html', label: 'CSL Pay Chart' });
    } else if (center === 'octapharma') {
      links.push({ href: '/octapharma-payment-calculator.html', label: 'Octapharma Calculator' });
    }

    // Add state calculator if exists
    const stateSlug = stateNames[state]?.toLowerCase().replace(/\s+/g, '-');
    if (stateSlug) {
      links.push({ href: `/calculators/${stateSlug}/`, label: `${stateNames[state]} Calculator` });
    }

    // Add comparison tools
    links.push({ href: '/tools/all-plasma-centers-comparison.html', label: 'Compare All Centers' });

    return links;
  },

  /**
   * Generate JSON-LD schema
   */
  schemaJsonLd(inputs, outputs, canonicalUrl) {
    const { center, donorType, weightRange, state } = inputs;
    const centerName = centerNames[center] || center;
    const stateName = stateNames[state] || state;
    const year = getCurrentYear();

    const faqItems = this.faqItems(inputs, outputs);

    return [
      generateAppSchema({
        name: `${centerName} Plasma Pay Calculator - ${stateName}`,
        description: this.metaDescription(inputs, outputs),
        url: canonicalUrl
      }),
      generateFaqSchema(faqItems),
      generateBreadcrumbSchema([
        { label: 'Home', url: '/' },
        { label: 'Calculators', url: '/calculators/' },
        { label: centerName, url: canonicalUrl }
      ], SITE_URL)
    ];
  }
};

// ============================================================================
// PLASMA TAX CALCULATOR CONFIG
// ============================================================================

const plasmaTaxConfig = {
  id: 'plasma-tax',
  interactivePath: '/csl-plasma-tax-calculator.html',
  outBase: 'p/plasma-tax',

  // Curated input grid for tax scenarios
  // Income levels: Key thresholds that affect tax reporting
  // Filing status: All three common statuses
  inputGrid: {
    plasmaIncome: [600, 1200, 2500, 5000, 7500, 9000], // 1099 threshold + common earning levels
    filingStatus: ['single', 'married', 'head_of_household'],
    otherIncome: [0, 25000, 50000] // No other income, modest, median
  },

  /**
   * Validate input combination
   */
  validate(inputs) {
    const result = validateTaxInputs(inputs);
    if (!result.valid) return false;

    // Skip very low plasma income (not meaningful)
    if (inputs.plasmaIncome < 600) return false;

    return true;
  },

  /**
   * Compute tax liability
   */
  compute(inputs) {
    return calculatePlasmaTax(inputs);
  },

  /**
   * Generate canonical key for deduplication
   */
  canonicalKey(inputs, outputs) {
    // Bucket by tax amount in $50 increments
    const taxBucket = Math.floor(outputs.totalTax / 50) * 50;
    return `${inputs.filingStatus}-plasma${inputs.plasmaIncome}-tax${taxBucket}`;
  },

  /**
   * Generate URL slug
   */
  slug(inputs, outputs) {
    const { plasmaIncome, filingStatus, otherIncome } = inputs;
    const incomeSlug = plasmaIncome >= 1000 ? `${plasmaIncome / 1000}k` : plasmaIncome;
    const statusSlug = filingStatus.replace(/_/g, '-');
    const otherSlug = otherIncome > 0 ? `-${otherIncome / 1000}k-income` : '';

    return `${incomeSlug}-plasma-income-${statusSlug}${otherSlug}`;
  },

  /**
   * Generate page title
   */
  pageTitle(inputs, outputs) {
    const { plasmaIncome, filingStatus } = inputs;
    const year = getCurrentYear();
    const statusName = filingStatusNames[filingStatus];

    return `Plasma Donation Tax Calculator ${year}: ${formatCurrency(plasmaIncome)} Income (${statusName}) | Owe ${formatCurrency(outputs.totalTax)}`;
  },

  /**
   * Generate meta description
   */
  metaDescription(inputs, outputs) {
    const { plasmaIncome, filingStatus, otherIncome } = inputs;
    const statusName = filingStatusNames[filingStatus];
    const otherNote = otherIncome > 0 ? ` with ${formatCurrency(otherIncome)} other income` : '';

    return `Calculate taxes on ${formatCurrency(plasmaIncome)} plasma donation income for ${statusName} filers${otherNote}. Total tax: ${formatCurrency(outputs.totalTax)}. Quarterly payment: ${formatCurrency(outputs.recommendedQuarterly)}.`;
  },

  /**
   * Generate hero HTML
   */
  heroHtml(inputs, outputs) {
    const { plasmaIncome, filingStatus } = inputs;
    const statusName = filingStatusNames[filingStatus];
    const year = getCurrentYear();
    const scenario = getTaxScenario(plasmaIncome);

    return `
      <h1>Plasma Income Tax Calculator ${year}: ${formatCurrency(plasmaIncome)} (${statusName})</h1>
      <p>${scenario.description} Calculate your exact tax liability and recommended quarterly payments.</p>
    `;
  },

  /**
   * Generate summary HTML
   */
  summaryHtml(inputs, outputs) {
    const { plasmaIncome, filingStatus, otherIncome } = inputs;
    const statusName = filingStatusNames[filingStatus];
    const scenario = getTaxScenario(plasmaIncome);

    const otherIncomeNote = otherIncome > 0
      ? `<p style="margin-top: 1rem;">Combined with your ${formatCurrency(otherIncome)} other income, your total gross income is ${formatCurrency(outputs.totalGrossIncome)}.</p>`
      : '';

    return `
      <h2 class="card-title">Tax Summary for ${formatCurrency(plasmaIncome)} Plasma Income</h2>

      <div class="result-box">
        <div class="label">Total Estimated Tax Liability</div>
        <div class="amount">${formatCurrency(outputs.totalTax)}</div>
      </div>

      <div class="results-grid">
        <div class="result-item">
          <div class="value">${formatCurrency(outputs.selfEmploymentTax.seTax)}</div>
          <div class="label">Self-Employment Tax</div>
        </div>
        <div class="result-item">
          <div class="value">${formatCurrency(outputs.federalIncomeTax)}</div>
          <div class="label">Federal Income Tax</div>
        </div>
        <div class="result-item">
          <div class="value">${formatPercent(outputs.effectivePlasmaRate)}</div>
          <div class="label">Effective Tax Rate</div>
        </div>
        <div class="result-item">
          <div class="value">${formatCurrency(outputs.recommendedQuarterly)}</div>
          <div class="label">Quarterly Payment</div>
        </div>
      </div>

      <p style="margin-top: 1rem;">
        Filing as <strong>${statusName}</strong> with ${formatCurrency(plasmaIncome)} in plasma donation income, you'll owe approximately <strong>${formatCurrency(outputs.totalTax)}</strong> in federal taxes. This includes ${formatCurrency(outputs.selfEmploymentTax.seTax)} in self-employment tax (Social Security + Medicare).
      </p>

      ${otherIncomeNote}

      <p style="margin-top: 1rem; padding: 1rem; background: ${outputs.will1099BeIssued ? '#fef3c7' : '#f0fdfa'}; border-radius: 8px;">
        <strong>${outputs.will1099BeIssued ? '1099 Form Required:' : 'No 1099 Required:'}</strong>
        ${outputs.will1099BeIssued
          ? `Your plasma center will send you a 1099-MISC form since your earnings exceed $600. Report this income on Schedule C.`
          : `You won't receive a 1099 form, but this income is still technically taxable.`}
      </p>

      <p style="margin-top: 1rem; padding: 1rem; background: #f0fdfa; border-radius: 8px;">
        <strong>After-Tax Income:</strong> After paying ${formatCurrency(outputs.totalTax)} in taxes, your take-home from plasma donations is <strong>${formatCurrency(outputs.afterTaxPlasmaIncome)}</strong>.
      </p>
    `;
  },

  /**
   * Generate tax breakdown table
   */
  tableHtml(inputs, outputs) {
    const { plasmaIncome } = inputs;

    // Show comparison across income levels
    const incomes = [600, 1200, 2500, 5000, 7500, 9000];
    const rows = incomes.map(income => {
      const result = calculatePlasmaTax({ ...inputs, plasmaIncome: income });
      const isCurrent = income === plasmaIncome;
      return `
        <tr class="${isCurrent ? 'current' : ''}">
          <td style="font-family: 'Space Mono', monospace;">${formatCurrency(income)}</td>
          <td style="font-family: 'Space Mono', monospace;">${formatCurrency(result.selfEmploymentTax.seTax)}</td>
          <td style="font-family: 'Space Mono', monospace;">${formatCurrency(result.federalIncomeTax)}</td>
          <td style="font-family: 'Space Mono', monospace;">${formatCurrency(result.totalTax)}</td>
          <td style="font-family: 'Space Mono', monospace;">${formatPercent(result.effectivePlasmaRate)}</td>
        </tr>
      `;
    }).join('');

    return `
      <h2 class="card-title">Tax Comparison by Plasma Income Level</h2>
      <p style="margin-bottom: 1rem; color: var(--slate);">See how taxes scale with different plasma donation income levels. Your scenario is highlighted.</p>
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Plasma Income</th>
            <th>SE Tax</th>
            <th>Income Tax</th>
            <th>Total Tax</th>
            <th>Eff. Rate</th>
          </tr>
        </thead>
        <tbody>
          ${rows}
        </tbody>
      </table>
    `;
  },

  /**
   * Generate FAQ items
   */
  faqItems(inputs, outputs) {
    const { plasmaIncome, filingStatus } = inputs;
    const statusName = filingStatusNames[filingStatus];
    const year = getCurrentYear();
    const scenario = getTaxScenario(plasmaIncome);

    return [
      {
        q: `How much tax do I owe on ${formatCurrency(plasmaIncome)} plasma income?`,
        a: `Filing as ${statusName} with ${formatCurrency(plasmaIncome)} in plasma income, you'll owe approximately <strong>${formatCurrency(outputs.totalTax)}</strong>. This includes ${formatCurrency(outputs.selfEmploymentTax.seTax)} in self-employment tax and ${formatCurrency(outputs.federalIncomeTax)} in federal income tax.`
      },
      {
        q: 'Is plasma donation income taxable?',
        a: `Yes, plasma donation income is considered <strong>taxable self-employment income</strong>. You must report it on Schedule C of your tax return and pay both income tax and self-employment tax (15.3% for Social Security and Medicare).`
      },
      {
        q: 'Do I need to make quarterly tax payments on plasma income?',
        a: `If you expect to owe more than $1,000 in taxes, the IRS recommends making quarterly estimated payments. For ${formatCurrency(plasmaIncome)} in plasma income, we recommend quarterly payments of <strong>${formatCurrency(outputs.recommendedQuarterly)}</strong> to avoid penalties.`
      },
      {
        q: `Will I receive a 1099 form for my plasma donations?`,
        a: outputs.will1099BeIssued
          ? `Yes, plasma centers issue 1099-MISC forms for earnings over $600. With ${formatCurrency(plasmaIncome)} in donations, you'll receive a 1099 that must be reported on your tax return.`
          : `Plasma centers only issue 1099 forms for earnings over $600. However, even without a 1099, this income is technically taxable and should be reported.`
      },
      {
        q: 'What expenses can I deduct from plasma donation income?',
        a: `You can deduct legitimate business expenses including: <strong>mileage</strong> to/from the plasma center (67 cents/mile in ${year}), parking fees, iron supplements, and other health-related costs recommended by your center.`
      },
      {
        q: 'How do I report plasma income on my taxes?',
        a: `Report plasma income on <strong>Schedule C</strong> (Profit or Loss from Business) as self-employment income. You'll also need to complete <strong>Schedule SE</strong> to calculate self-employment tax. The total flows to your Form 1040.`
      },
      {
        q: 'What is the self-employment tax rate for plasma income?',
        a: `The self-employment tax rate is <strong>15.3%</strong> (12.4% for Social Security and 2.9% for Medicare). This is applied to 92.35% of your net self-employment income. You can deduct half of this tax from your adjusted gross income.`
      },
      {
        q: `How does filing status affect my plasma income taxes?`,
        a: `Your filing status affects your tax brackets and standard deduction. As a ${statusName}, your standard deduction is ${formatCurrency(outputs.standardDeduction)}. This reduces your taxable income and lowers your income tax (though not your self-employment tax).`
      }
    ];
  },

  /**
   * Generate CTA HTML
   */
  ctaHtml(inputs, outputs) {
    const params = new URLSearchParams({
      income: inputs.plasmaIncome,
      status: inputs.filingStatus
    }).toString();

    return `
      <h3 style="margin-bottom: 1rem;">Calculate Your Exact Tax Liability</h3>
      <p style="margin-bottom: 1.5rem; color: var(--slate);">Use our interactive calculator with your specific income and deductions.</p>
      <a href="/csl-plasma-tax-calculator.html?${params}" class="cta-button">Open Tax Calculator</a>
    `;
  },

  /**
   * Generate related links
   */
  relatedLinks(inputs, outputs) {
    return [
      { href: '/csl-plasma-tax-calculator.html', label: 'Tax Calculator' },
      { href: '/', label: 'Pay Calculator' },
      { href: '/comprehensive-plasma-tax-guide-2026.html', label: 'Tax Guide' },
      { href: '/blog/', label: 'Tax Tips Blog' }
    ];
  },

  /**
   * Generate JSON-LD schema
   */
  schemaJsonLd(inputs, outputs, canonicalUrl) {
    const { plasmaIncome, filingStatus } = inputs;
    const statusName = filingStatusNames[filingStatus];

    const faqItems = this.faqItems(inputs, outputs);

    return [
      generateAppSchema({
        name: `Plasma Tax Calculator - ${formatCurrency(plasmaIncome)} (${statusName})`,
        description: this.metaDescription(inputs, outputs),
        url: canonicalUrl
      }),
      generateFaqSchema(faqItems),
      generateBreadcrumbSchema([
        { label: 'Home', url: '/' },
        { label: 'Tax Calculator', url: '/csl-plasma-tax-calculator.html' },
        { label: `${formatCurrency(plasmaIncome)} ${statusName}`, url: canonicalUrl }
      ], SITE_URL)
    ];
  }
};

// ============================================================================
// EXPORT ALL CALCULATORS
// ============================================================================

export const calculators = [
  plasmaPayConfig,
  plasmaTaxConfig
];

// Helper to get calculator by ID
export function getCalculatorById(id) {
  return calculators.find(c => c.id === id);
}
