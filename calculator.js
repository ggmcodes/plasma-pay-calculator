// Plasma Pay Calculator Logic

// Payment rates by center and donor status
const paymentRates = {
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
    },
    other: {
        new: { week1: 110, week2: 90, week3: 80, week4: 75 },
        returning: { first: 20, second: 40 },
        lapsed: { week1: 90, week2: 80, week3: 75, week4: 70 }
    }
};

// State multipliers based on cost of living
const stateMultipliers = {
    'CA': 1.15,
    'NY': 1.12,
    'IL': 1.10,
    'TX': 1.08,
    'PA': 1.07,
    'FL': 1.05,
    'MI': 1.05,
    'GA': 1.03,
    'NC': 1.02,
    'OH': 1.00,
    'other': 1.00
};

// Weight multipliers
function getWeightMultiplier(weightRange) {
    const multipliers = {
        '110-149': 1.0,
        '150-174': 1.1,
        '175-200': 1.2,
        '200+': 1.25
    };
    return multipliers[weightRange] || 1.0;
}

// Referral bonuses
function getReferralBonus(referrals) {
    const bonuses = {
        '0': 0,
        '1': 75,
        '2': 150,
        '3': 225,
        '4': 300
    };
    return bonuses[referrals] || 0;
}

// Main calculation function
function calculateEarnings() {
    // Get form values
    const donorType = document.getElementById('donorType').value;
    const weightRange = document.getElementById('weight').value;
    const center = document.getElementById('center').value || 'average';
    const state = document.getElementById('state').value;
    const frequency = parseFloat(document.getElementById('frequency').value);
    const miles = parseFloat(document.getElementById('miles').value) || 5;
    const mpg = parseFloat(document.getElementById('mpg').value) || 25;
    const gasPrice = parseFloat(document.getElementById('gasPrice').value) || 3.50;
    const referrals = document.getElementById('referrals').value;
    
    // Validate inputs
    if (!donorType || !weightRange || !state || !frequency) {
        alert('Please fill in all required fields');
        return;
    }
    
    // Get rates and multipliers
    const rates = paymentRates[center];
    const weightMult = getWeightMultiplier(weightRange);
    const stateMult = stateMultipliers[state] || 1.0;
    const referralBonus = getReferralBonus(referrals);
    
    let monthlyGross = 0;
    let weeklyAvg = 0;
    let baseRate = 0;
    
    if (donorType === 'new') {
        // Calculate first month for new donors
        const totalFirstMonth = (rates.new.week1 * 2 + rates.new.week2 * 2 + 
                               rates.new.week3 * 2 + rates.new.week4 * 2);
        monthlyGross = totalFirstMonth * weightMult * stateMult;
        weeklyAvg = monthlyGross / 4;
        baseRate = rates.new.week1;
    } else if (donorType === 'lapsed') {
        // Lapsed donors get special rates
        const totalFirstMonth = (rates.lapsed.week1 * 2 + rates.lapsed.week2 * 2 + 
                               rates.lapsed.week3 * 2 + rates.lapsed.week4 * 2);
        monthlyGross = totalFirstMonth * weightMult * stateMult;
        weeklyAvg = monthlyGross / 4;
        baseRate = rates.lapsed.week1;
    } else {
        // Returning donors
        weeklyAvg = (rates.returning.first + rates.returning.second) * frequency * weightMult * stateMult;
        monthlyGross = weeklyAvg * 4.33;
        baseRate = (rates.returning.first + rates.returning.second) / 2;
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
    const monthlyTax = monthlyGross * 0.20;
    
    // Net calculations
    const monthlyNet = monthlyGross - monthlyGas - monthlyTax;
    const weeklyNet = monthlyNet / 4.33;
    const yearlyNet = monthlyNet * 12;
    
    // Update display
    document.getElementById('weeklyNet').textContent = Math.round(weeklyNet);
    document.getElementById('monthlyNet').textContent = Math.round(monthlyNet);
    document.getElementById('yearlyNet').textContent = Math.round(yearlyNet).toLocaleString();
    
    // Detailed breakdown
    document.getElementById('baseRate').textContent = Math.round(baseRate);
    document.getElementById('weightBonus').textContent = Math.round((weightMult - 1) * 100);
    document.getElementById('stateBonus').textContent = Math.round((stateMult - 1) * 100);
    document.getElementById('monthlyDonations').textContent = Math.round(donationsPerMonth);
    document.getElementById('grossMonthly').textContent = Math.round(monthlyGross);
    document.getElementById('referralBonus').textContent = referralBonus;
    document.getElementById('gasMonthly').textContent = Math.round(monthlyGas);
    document.getElementById('taxMonthly').textContent = Math.round(monthlyTax);
    document.getElementById('totalMiles').textContent = Math.round(monthlyMiles);
    document.getElementById('finalMonthly').textContent = Math.round(monthlyNet);
    
    // Earning analysis message
    const earningAnalysis = document.getElementById('earningAnalysis');
    if (monthlyNet > 800) {
        earningAnalysis.textContent = "WOW! You're in the TOP 5% of plasma earners! Your optimized strategy puts you way ahead of average donors.";
    } else if (monthlyNet > 600) {
        earningAnalysis.textContent = "Excellent! You're earning more than 85% of plasma donors. Your frequency and location give you a major advantage.";
    } else if (monthlyNet > 400) {
        earningAnalysis.textContent = "Great job! You're earning more than 70% of plasma donors. Consider increasing frequency or finding a closer center to earn even more.";
    } else {
        earningAnalysis.textContent = "You're on track to earn steady supplemental income. Try donating more frequently or checking for referral bonuses to maximize earnings.";
    }
    
    // Show results section
    document.getElementById('results').classList.add('show');
    document.getElementById('results').scrollIntoView({ behavior: 'smooth' });
}

// Quiz functions
function nextQuestion(currentQ, eligible) {
    document.getElementById('q' + currentQ).style.display = 'none';
    if (currentQ < 5) {
        document.getElementById('q' + (currentQ + 1)).style.display = 'block';
    }
}

function showEligible() {
    document.getElementById('q5').style.display = 'none';
    document.getElementById('quiz-result').innerHTML = `
        <div style="background: #e8f5e9; padding: 20px; border-radius: 8px; border: 2px solid #27ae60;">
            <h3 style="color: #155724; margin-bottom: 10px;">✅ Great News - You Can Donate!</h3>
            <p style="margin-bottom: 15px;">You meet the basic requirements. Bring these documents to your first visit:</p>
            <ul style="text-align: left; margin: 0 auto; max-width: 300px;">
                <li>Valid photo ID</li>
                <li>Proof of address (utility bill, bank statement)</li>
                <li>Social Security card</li>
            </ul>
            <button onclick="resetQuiz()" style="margin-top: 15px; padding: 10px 20px; background: #27ae60; color: white; border: none; border-radius: 6px; cursor: pointer;">Take Quiz Again</button>
        </div>
    `;
    document.getElementById('quiz-result').style.display = 'block';
}

function showNotEligible(reason) {
    document.querySelectorAll('.quiz-question').forEach(q => q.style.display = 'none');
    document.getElementById('quiz-result').innerHTML = `
        <div style="background: #f8d7da; padding: 20px; border-radius: 8px; border: 2px solid #e74c3c;">
            <h3 style="color: #721c24; margin-bottom: 10px;">❌ Sorry, You Can't Donate Right Now</h3>
            <p style="margin-bottom: 15px;">${reason}</p>
            <p>Check back later or look into other ways to make quick money.</p>
            <button onclick="resetQuiz()" style="margin-top: 15px; padding: 10px 20px; background: #e74c3c; color: white; border: none; border-radius: 6px; cursor: pointer;">Take Quiz Again</button>
        </div>
    `;
    document.getElementById('quiz-result').style.display = 'block';
}

function showMaybe(message) {
    document.querySelectorAll('.quiz-question').forEach(q => q.style.display = 'none');
    document.getElementById('quiz-result').innerHTML = `
        <div style="background: #fff3cd; padding: 20px; border-radius: 8px; border: 2px solid #f39c12;">
            <h3 style="color: #856404; margin-bottom: 10px;">⚠️ You Might Be Eligible</h3>
            <p style="margin-bottom: 15px;">${message}</p>
            <p>Contact your local center to check - they can give specific guidance.</p>
            <button onclick="resetQuiz()" style="margin-top: 15px; padding: 10px 20px; background: #f39c12; color: white; border: none; border-radius: 6px; cursor: pointer;">Take Quiz Again</button>
        </div>
    `;
    document.getElementById('quiz-result').style.display = 'block';
}

function resetQuiz() {
    document.getElementById('quiz-result').style.display = 'none';
    document.getElementById('quiz-result').innerHTML = '';
    document.querySelectorAll('.quiz-question').forEach(q => q.style.display = 'none');
    document.getElementById('q1').style.display = 'block';
}

// Initialize when page loads
document.addEventListener('DOMContentLoaded', function() {
    // Register Service Worker for PWA functionality
    if ('serviceWorker' in navigator) {
        navigator.serviceWorker.register('sw.js')
            .then(reg => console.log('Service Worker registered'))
            .catch(err => console.log('Service Worker registration failed'));
    }
    
    // Prevent pull-to-refresh on mobile for better UX
    document.body.addEventListener('touchmove', (e) => {
        if (e.touches.length > 1) {
            e.preventDefault();
        }
    }, { passive: false });
});