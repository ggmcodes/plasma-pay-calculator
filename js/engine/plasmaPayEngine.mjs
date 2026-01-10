/**
 * Plasma Pay Calculator Engine
 * Pure functions for calculating plasma donation earnings
 * Works in both Node.js (build time) and browser (runtime)
 */

// Payment rates by center and donor status
export const paymentRates = {
  average: {
    new: { week1: 125, week2: 110, week3: 95, week4: 90 },
    returning: { first: 25, second: 45 },
    lapsed: { week1: 100, week2: 90, week3: 85, week4: 80 }
  },
  csl: {
    new: { week1: 135, week2: 115, week3: 100, week4: 95 },
    returning: { first: 25, second: 50 },
    lapsed: { week1: 110, week2: 95, week3: 90, week4: 85 }
  },
  biolife: {
    new: { week1: 120, week2: 100, week3: 90, week4: 85 },
    returning: { first: 30, second: 55 },
    lapsed: { week1: 105, week2: 90, week3: 85, week4: 80 }
  },
  octapharma: {
    new: { week1: 130, week2: 110, week3: 95, week4: 90 },
    returning: { first: 30, second: 60 },
    lapsed: { week1: 110, week2: 95, week3: 90, week4: 85 }
  },
  grifols: {
    new: { week1: 115, week2: 95, week3: 85, week4: 80 },
    returning: { first: 20, second: 45 },
    lapsed: { week1: 95, week2: 85, week3: 80, week4: 75 }
  },
  kedplasma: {
    new: { week1: 125, week2: 105, week3: 90, week4: 85 },
    returning: { first: 25, second: 45 },
    lapsed: { week1: 100, week2: 90, week3: 85, week4: 80 }
  },
  bpl: {
    new: { week1: 140, week2: 120, week3: 100, week4: 95 },
    returning: { first: 35, second: 65 },
    lapsed: { week1: 115, week2: 100, week3: 90, week4: 85 }
  },
  interstate: {
    new: { week1: 115, week2: 95, week3: 85, week4: 80 },
    returning: { first: 25, second: 40 },
    lapsed: { week1: 95, week2: 85, week3: 80, week4: 75 }
  }
};

// State multipliers based on cost of living
export const stateMultipliers = {
  CA: 1.15,
  NY: 1.12,
  IL: 1.10,
  TX: 1.08,
  PA: 1.07,
  FL: 1.05,
  MI: 1.05,
  GA: 1.03,
  NC: 1.02,
  OH: 1.00,
  AZ: 1.02,
  WA: 1.08,
  CO: 1.06,
  NV: 1.04,
  NJ: 1.10,
  MA: 1.12,
  other: 1.00
};

// State display names
export const stateNames = {
  CA: 'California',
  NY: 'New York',
  IL: 'Illinois',
  TX: 'Texas',
  PA: 'Pennsylvania',
  FL: 'Florida',
  MI: 'Michigan',
  GA: 'Georgia',
  NC: 'North Carolina',
  OH: 'Ohio',
  AZ: 'Arizona',
  WA: 'Washington',
  CO: 'Colorado',
  NV: 'Nevada',
  NJ: 'New Jersey',
  MA: 'Massachusetts'
};

// Center display names
export const centerNames = {
  csl: 'CSL Plasma',
  biolife: 'BioLife Plasma',
  octapharma: 'Octapharma Plasma',
  grifols: 'Grifols',
  kedplasma: 'KEDPLASMA',
  bpl: 'BPL Plasma'
};

// Weight range display names
export const weightRangeNames = {
  '110-149': '110-149 lbs',
  '150-174': '150-174 lbs',
  '175-200': '175-200 lbs',
  '200+': '200+ lbs'
};

// Donor type display names
export const donorTypeNames = {
  new: 'New Donor',
  returning: 'Returning Donor',
  lapsed: 'Lapsed Donor'
};

/**
 * Get weight multiplier based on weight range
 * @param {string} weightRange - Weight range key
 * @returns {number} Multiplier value
 */
export function getWeightMultiplier(weightRange) {
  const multipliers = {
    '110-149': 1.0,
    '150-174': 1.1,
    '175-200': 1.2,
    '200+': 1.25
  };
  return multipliers[weightRange] || 1.0;
}

/**
 * Get referral bonus amount
 * @param {number|string} referrals - Number of referrals
 * @returns {number} Bonus amount
 */
export function getReferralBonus(referrals) {
  const bonuses = {
    0: 0,
    1: 75,
    2: 150,
    3: 225,
    4: 300
  };
  return bonuses[Number(referrals)] || 0;
}

/**
 * Validate inputs for plasma pay calculation
 * @param {Object} inputs - Input parameters
 * @returns {Object} { valid: boolean, reason?: string }
 */
export function validateInputs(inputs) {
  const { center, donorType, weightRange, state, frequency } = inputs;

  // Check required fields
  if (!center || !paymentRates[center]) {
    return { valid: false, reason: 'Invalid or missing center' };
  }
  if (!donorType || !['new', 'returning', 'lapsed'].includes(donorType)) {
    return { valid: false, reason: 'Invalid or missing donor type' };
  }
  if (!weightRange || !['110-149', '150-174', '175-200', '200+'].includes(weightRange)) {
    return { valid: false, reason: 'Invalid or missing weight range' };
  }
  if (!state) {
    return { valid: false, reason: 'Missing state' };
  }

  // Frequency validation for returning donors
  if (donorType === 'returning') {
    const freq = Number(frequency);
    if (!freq || freq < 1 || freq > 2) {
      return { valid: false, reason: 'Returning donors need valid frequency (1-2)' };
    }
  }

  return { valid: true };
}

/**
 * Calculate plasma donation earnings
 * @param {Object} inputs - Input parameters
 * @returns {Object} Calculated earnings breakdown
 */
export function calculatePlasmaEarnings(inputs) {
  const {
    center,
    donorType,
    weightRange,
    state,
    frequency = 2,
    miles = 5,
    mpg = 25,
    gasPrice = 3.50,
    referrals = 0
  } = inputs;

  // Get rates and multipliers
  const rates = paymentRates[center];
  const weightMult = getWeightMultiplier(weightRange);
  const stateMult = stateMultipliers[state] || stateMultipliers.other;
  const referralBonus = getReferralBonus(referrals);

  let monthlyGross = 0;
  let weeklyAvg = 0;
  let baseRate = 0;
  let firstMonthBonus = 0;

  if (donorType === 'new') {
    // Calculate first month for new donors
    const totalFirstMonth = (rates.new.week1 * 2 + rates.new.week2 * 2 +
      rates.new.week3 * 2 + rates.new.week4 * 2);
    monthlyGross = totalFirstMonth * weightMult * stateMult;
    weeklyAvg = monthlyGross / 4;
    baseRate = rates.new.week1;
    firstMonthBonus = Math.round((rates.new.week1 - rates.returning.first) * 8 * weightMult * stateMult);
  } else if (donorType === 'lapsed') {
    // Lapsed donors get special rates
    const totalFirstMonth = (rates.lapsed.week1 * 2 + rates.lapsed.week2 * 2 +
      rates.lapsed.week3 * 2 + rates.lapsed.week4 * 2);
    monthlyGross = totalFirstMonth * weightMult * stateMult;
    weeklyAvg = monthlyGross / 4;
    baseRate = rates.lapsed.week1;
  } else {
    // Returning donors
    const freq = Number(frequency);
    weeklyAvg = (rates.returning.first + rates.returning.second) * freq * weightMult * stateMult;
    monthlyGross = weeklyAvg * 4.33;
    baseRate = Math.round((rates.returning.first + rates.returning.second) / 2);
  }

  // Add referral bonuses
  monthlyGross += referralBonus;

  // Gas calculation
  const milesPerDonation = miles * 2; // round trip
  const donationsPerMonth = frequency * 4.33;
  const monthlyMiles = milesPerDonation * donationsPerMonth;
  const monthlyGas = (monthlyMiles / mpg) * gasPrice;
  const weeklyGas = monthlyGas / 4.33;

  // Tax estimate (20% for self-employment)
  const taxRate = 0.20;
  const monthlyTax = monthlyGross * taxRate;

  // Net calculations
  const monthlyNet = monthlyGross - monthlyGas - monthlyTax;
  const weeklyNet = monthlyNet / 4.33;
  const yearlyNet = monthlyNet * 12;
  const yearlyGross = monthlyGross * 12;

  // Per-visit earnings
  const perVisitGross = Math.round(monthlyGross / donationsPerMonth);
  const perVisitNet = Math.round(monthlyNet / donationsPerMonth);

  return {
    // Gross earnings
    weeklyGross: Math.round(weeklyAvg),
    monthlyGross: Math.round(monthlyGross),
    yearlyGross: Math.round(yearlyGross),

    // Net earnings (after gas and estimated tax)
    weeklyNet: Math.round(weeklyNet),
    monthlyNet: Math.round(monthlyNet),
    yearlyNet: Math.round(yearlyNet),

    // Per visit
    perVisitGross,
    perVisitNet,

    // Breakdown details
    baseRate: Math.round(baseRate),
    weightBonus: Math.round((weightMult - 1) * 100),
    stateBonus: Math.round((stateMult - 1) * 100),
    weightMultiplier: weightMult,
    stateMultiplier: stateMult,
    donationsPerMonth: Math.round(donationsPerMonth),
    referralBonus,
    firstMonthBonus,

    // Expenses
    monthlyGas: Math.round(monthlyGas),
    monthlyMiles: Math.round(monthlyMiles),
    monthlyTax: Math.round(monthlyTax),
    taxRate: taxRate * 100,

    // Input echo (for display)
    inputs: {
      center,
      donorType,
      weightRange,
      state,
      frequency: Number(frequency),
      miles,
      mpg,
      gasPrice,
      referrals: Number(referrals)
    }
  };
}

/**
 * Get earnings tier label based on monthly net
 * @param {number} monthlyNet - Monthly net earnings
 * @returns {Object} { tier, label, description }
 */
export function getEarningsTier(monthlyNet) {
  if (monthlyNet >= 800) {
    return {
      tier: 'top',
      label: 'Top 5% Earner',
      description: 'Your optimized strategy puts you way ahead of average donors.'
    };
  } else if (monthlyNet >= 600) {
    return {
      tier: 'excellent',
      label: 'Top 15% Earner',
      description: 'You\'re earning more than 85% of plasma donors.'
    };
  } else if (monthlyNet >= 400) {
    return {
      tier: 'good',
      label: 'Above Average',
      description: 'You\'re earning more than 70% of plasma donors.'
    };
  } else {
    return {
      tier: 'standard',
      label: 'Standard Earner',
      description: 'You\'re on track for steady supplemental income.'
    };
  }
}

/**
 * Compare earnings across centers for given inputs
 * @param {Object} baseInputs - Base input parameters (without center)
 * @returns {Array} Sorted array of earnings by center
 */
export function compareCenters(baseInputs) {
  const centers = Object.keys(paymentRates).filter(c => c !== 'average');
  const comparisons = centers.map(center => {
    const inputs = { ...baseInputs, center };
    const validation = validateInputs(inputs);
    if (!validation.valid) return null;

    const earnings = calculatePlasmaEarnings(inputs);
    return {
      center,
      centerName: centerNames[center] || center,
      ...earnings
    };
  }).filter(Boolean);

  return comparisons.sort((a, b) => b.monthlyNet - a.monthlyNet);
}
