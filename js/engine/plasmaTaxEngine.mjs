/**
 * Plasma Tax Calculator Engine
 * Pure functions for calculating tax liability on plasma donation income
 * Works in both Node.js (build time) and browser (runtime)
 */

// 2024/2025 Federal Tax Brackets (simplified)
export const taxBrackets = {
  single: [
    { min: 0, max: 11600, rate: 0.10 },
    { min: 11600, max: 47150, rate: 0.12 },
    { min: 47150, max: 100525, rate: 0.22 },
    { min: 100525, max: 191950, rate: 0.24 },
    { min: 191950, max: 243725, rate: 0.32 },
    { min: 243725, max: 609350, rate: 0.35 },
    { min: 609350, max: Infinity, rate: 0.37 }
  ],
  married: [
    { min: 0, max: 23200, rate: 0.10 },
    { min: 23200, max: 94300, rate: 0.12 },
    { min: 94300, max: 201050, rate: 0.22 },
    { min: 201050, max: 383900, rate: 0.24 },
    { min: 383900, max: 487450, rate: 0.32 },
    { min: 487450, max: 731200, rate: 0.35 },
    { min: 731200, max: Infinity, rate: 0.37 }
  ],
  head_of_household: [
    { min: 0, max: 16550, rate: 0.10 },
    { min: 16550, max: 63100, rate: 0.12 },
    { min: 63100, max: 100500, rate: 0.22 },
    { min: 100500, max: 191950, rate: 0.24 },
    { min: 191950, max: 243700, rate: 0.32 },
    { min: 243700, max: 609350, rate: 0.35 },
    { min: 609350, max: Infinity, rate: 0.37 }
  ]
};

// Self-employment tax rate (Social Security + Medicare)
export const SELF_EMPLOYMENT_TAX_RATE = 0.153; // 15.3%
export const SE_DEDUCTION_RATE = 0.5; // 50% of SE tax is deductible

// Standard deductions
export const standardDeductions = {
  single: 14600,
  married: 29200,
  head_of_household: 21900
};

// Filing status display names
export const filingStatusNames = {
  single: 'Single',
  married: 'Married Filing Jointly',
  head_of_household: 'Head of Household'
};

/**
 * Validate inputs for tax calculation
 * @param {Object} inputs - Input parameters
 * @returns {Object} { valid: boolean, reason?: string }
 */
export function validateTaxInputs(inputs) {
  const { plasmaIncome, filingStatus, otherIncome = 0 } = inputs;

  if (typeof plasmaIncome !== 'number' || plasmaIncome < 0) {
    return { valid: false, reason: 'Invalid plasma income' };
  }

  // Skip if income is too low to be meaningful (under $100)
  if (plasmaIncome < 100) {
    return { valid: false, reason: 'Plasma income too low for meaningful calculation' };
  }

  if (!filingStatus || !taxBrackets[filingStatus]) {
    return { valid: false, reason: 'Invalid filing status' };
  }

  if (typeof otherIncome !== 'number' || otherIncome < 0) {
    return { valid: false, reason: 'Invalid other income' };
  }

  return { valid: true };
}

/**
 * Calculate self-employment tax
 * @param {number} netSelfEmploymentIncome - Net self-employment income
 * @returns {Object} Self-employment tax breakdown
 */
export function calculateSelfEmploymentTax(netSelfEmploymentIncome) {
  // SE tax is only on 92.35% of net SE income
  const taxableAmount = netSelfEmploymentIncome * 0.9235;
  const seTax = taxableAmount * SELF_EMPLOYMENT_TAX_RATE;
  const seDeduction = seTax * SE_DEDUCTION_RATE;

  return {
    taxableAmount: Math.round(taxableAmount),
    seTax: Math.round(seTax),
    seDeduction: Math.round(seDeduction),
    socialSecurityPortion: Math.round(taxableAmount * 0.124),
    medicarePortion: Math.round(taxableAmount * 0.029)
  };
}

/**
 * Calculate federal income tax using progressive brackets
 * @param {number} taxableIncome - Taxable income after deductions
 * @param {string} filingStatus - Filing status
 * @returns {Object} Tax calculation breakdown
 */
export function calculateFederalTax(taxableIncome, filingStatus) {
  const brackets = taxBrackets[filingStatus];
  let totalTax = 0;
  let remainingIncome = taxableIncome;
  const bracketBreakdown = [];

  for (const bracket of brackets) {
    if (remainingIncome <= 0) break;

    const incomeInBracket = Math.min(
      remainingIncome,
      bracket.max - bracket.min
    );

    if (incomeInBracket > 0) {
      const taxInBracket = incomeInBracket * bracket.rate;
      totalTax += taxInBracket;
      bracketBreakdown.push({
        rate: bracket.rate * 100,
        income: Math.round(incomeInBracket),
        tax: Math.round(taxInBracket)
      });
      remainingIncome -= incomeInBracket;
    }
  }

  // Find effective and marginal rates
  const effectiveRate = taxableIncome > 0 ? (totalTax / taxableIncome) * 100 : 0;
  const marginalBracket = brackets.find(b => taxableIncome <= b.max) || brackets[brackets.length - 1];

  return {
    totalTax: Math.round(totalTax),
    effectiveRate: Math.round(effectiveRate * 10) / 10,
    marginalRate: marginalBracket.rate * 100,
    bracketBreakdown
  };
}

/**
 * Calculate complete tax liability for plasma income
 * @param {Object} inputs - Input parameters
 * @returns {Object} Complete tax calculation
 */
export function calculatePlasmaTax(inputs) {
  const {
    plasmaIncome,
    filingStatus,
    otherIncome = 0,
    deductions = 0, // Additional itemized deductions
    quarterlyPayments = 0 // Already paid quarterly
  } = inputs;

  // Calculate self-employment tax on plasma income
  const seTax = calculateSelfEmploymentTax(plasmaIncome);

  // Total gross income
  const totalGrossIncome = plasmaIncome + otherIncome;

  // Adjusted Gross Income (AGI) - deduct half of SE tax
  const agi = totalGrossIncome - seTax.seDeduction;

  // Determine deduction (standard vs itemized)
  const standardDeduction = standardDeductions[filingStatus];
  const totalDeduction = Math.max(standardDeduction, deductions);
  const usedStandardDeduction = totalDeduction === standardDeduction;

  // Taxable income
  const taxableIncome = Math.max(0, agi - totalDeduction);

  // Federal income tax
  const federalTax = calculateFederalTax(taxableIncome, filingStatus);

  // Total tax liability
  const totalTax = federalTax.totalTax + seTax.seTax;

  // Amount still owed (minus quarterly payments)
  const amountOwed = Math.max(0, totalTax - quarterlyPayments);

  // Tax on just the plasma income (for comparison)
  const taxOnPlasmaOnly = Math.round(plasmaIncome * (federalTax.effectiveRate / 100)) + seTax.seTax;

  // Effective tax rate on plasma income
  const effectivePlasmaRate = plasmaIncome > 0 ? (taxOnPlasmaOnly / plasmaIncome) * 100 : 0;

  // After-tax plasma income
  const afterTaxPlasmaIncome = plasmaIncome - taxOnPlasmaOnly;

  // Quarterly payment recommendation
  const recommendedQuarterly = Math.ceil(totalTax / 4);

  return {
    // Income summary
    plasmaIncome,
    otherIncome,
    totalGrossIncome,
    agi: Math.round(agi),
    taxableIncome: Math.round(taxableIncome),

    // Deductions
    standardDeduction,
    totalDeduction,
    usedStandardDeduction,

    // Self-employment tax
    selfEmploymentTax: seTax,

    // Federal income tax
    federalIncomeTax: federalTax.totalTax,
    effectiveRate: federalTax.effectiveRate,
    marginalRate: federalTax.marginalRate,
    bracketBreakdown: federalTax.bracketBreakdown,

    // Total tax
    totalTax,
    quarterlyPayments,
    amountOwed,
    recommendedQuarterly,

    // Plasma-specific
    taxOnPlasmaOnly,
    effectivePlasmaRate: Math.round(effectivePlasmaRate * 10) / 10,
    afterTaxPlasmaIncome: Math.round(afterTaxPlasmaIncome),

    // 1099 threshold info
    will1099BeIssued: plasmaIncome >= 600,
    amountOver1099Threshold: Math.max(0, plasmaIncome - 600),

    // Input echo
    inputs: {
      plasmaIncome,
      filingStatus,
      otherIncome,
      deductions,
      quarterlyPayments
    }
  };
}

/**
 * Get tax scenario description based on income level
 * @param {number} plasmaIncome - Annual plasma income
 * @returns {Object} Scenario info
 */
export function getTaxScenario(plasmaIncome) {
  if (plasmaIncome < 600) {
    return {
      level: 'minimal',
      label: 'Under 1099 Threshold',
      description: 'No 1099 form issued, but income is still technically taxable.',
      reportingRequired: false
    };
  } else if (plasmaIncome < 2500) {
    return {
      level: 'low',
      label: 'Casual Donor',
      description: 'Light donation schedule, modest tax impact.',
      reportingRequired: true
    };
  } else if (plasmaIncome < 5000) {
    return {
      level: 'moderate',
      label: 'Regular Donor',
      description: 'Consistent donation routine, notable tax consideration.',
      reportingRequired: true
    };
  } else if (plasmaIncome < 7500) {
    return {
      level: 'high',
      label: 'Dedicated Donor',
      description: 'Near-maximum donation frequency, significant tax planning recommended.',
      reportingRequired: true
    };
  } else {
    return {
      level: 'maximum',
      label: 'Maximum Frequency Donor',
      description: 'Donating at FDA-allowed maximum, quarterly tax payments strongly recommended.',
      reportingRequired: true
    };
  }
}

/**
 * Get deductible expenses info for plasma donors
 * @returns {Array} List of potentially deductible expenses
 */
export function getDeductibleExpenses() {
  return [
    {
      category: 'Transportation',
      items: [
        'Mileage to/from plasma center (67 cents/mile in 2024)',
        'Parking fees at plasma center',
        'Tolls on route to center'
      ]
    },
    {
      category: 'Health-Related',
      items: [
        'Iron supplements recommended by center',
        'Protein supplements for donation prep',
        'Hydration products (electrolyte drinks)'
      ]
    },
    {
      category: 'Documentation',
      items: [
        'Cost of required documentation (IDs, address verification)',
        'Physical exam fees if required by center'
      ]
    }
  ];
}
