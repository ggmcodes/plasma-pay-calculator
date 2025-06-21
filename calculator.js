// Plasma Pay Calculator Logic

// Payment rates by center and donor status
const paymentRates = {
    average: {
        new: { week1: 125, week2: 110, week3: 95, week4: 90 },
        returning: { first: 25, second: 45 }
    },
    csl: {
        new: { week1: 135, week2: 115, week3: 100, week4: 95 },
        returning: { first: 25, second: 50 }
    },
    biolife: {
        new: { week1: 120, week2: 100, week3: 90, week4: 85 },
        returning: { first: 30, second: 55 }
    },
    octapharma: {
        new: { week1: 130, week2: 110, week3: 95, week4: 90 },
        returning: { first: 30, second: 60 }
    },
    grifols: {
        new: { week1: 115, week2: 95, week3: 85, week4: 80 },
        returning: { first: 20, second: 45 }
    },
    kedplasma: {
        new: { week1: 125, week2: 105, week3: 90, week4: 85 },
        returning: { first: 25, second: 45 }
    },
    immunotek: {
        new: { week1: 120, week2: 100, week3: 85, week4: 80 },
        returning: { first: 25, second: 45 }
    },
    gcam: {
        new: { week1: 115, week2: 95, week3: 85, week4: 80 },
        returning: { first: 25, second: 40 }
    },
    other: {
        new: { week1: 110, week2: 90, week3: 80, week4: 75 },
        returning: { first: 20, second: 40 }
    }
};

// Weight multipliers
function getWeightMultiplier(weightRange) {
    if (weightRange === '110-149') return 1.0;
    if (weightRange === '150-174') return 1.1;
    if (weightRange === '175+') return 1.2;
    return 1.0; // default
}

// Main calculation function
function calculateEarnings() {
    // Get form values
    const donorType = document.getElementById('donorType').value;
    const weightRange = document.getElementById('weight').value;
    const miles = parseFloat(document.getElementById('miles').value);
    const center = document.getElementById('center').value || 'average';
    
    // Validate inputs
    if (!donorType) {
        alert('Please select if you are a new or returning donor');
        return;
    }
    
    if (!weightRange) {
        alert('Please select your weight range');
        return;
    }
    
    // Get rates for selected center
    const rates = paymentRates[center];
    const weightMult = getWeightMultiplier(weightRange);
    
    let monthlyGross = 0;
    let weeklyAvg = 0;
    
    if (donorType === 'new') {
        // Calculate first month for new donors (2x per week)
        monthlyGross = (rates.new.week1 * 2 + rates.new.week2 * 2 + 
                       rates.new.week3 * 2 + rates.new.week4 * 2) * weightMult;
        weeklyAvg = monthlyGross / 4;
    } else {
        // Returning donors
        weeklyAvg = (rates.returning.first + rates.returning.second) * weightMult;
        monthlyGross = weeklyAvg * 4.33;
    }
    
    // Gas calculation (27 MPG at $3.00/gallon = $0.111/mile)
    const milesPerDonation = miles * 2; // round trip
    const donationsPerMonth = 8; // 2x per week for 4 weeks
    const monthlyMiles = milesPerDonation * donationsPerMonth;
    const monthlyGas = monthlyMiles * 0.111;
    const weeklyGas = monthlyGas / 4;
    
    // Net calculations
    const monthlyNet = monthlyGross - monthlyGas;
    const weeklyNet = weeklyAvg - weeklyGas;
    
    // Tax estimate (20% for self-employment + state average)
    const monthlyTax = monthlyGross * 0.20;
    
    // Update display
    document.getElementById('weeklyNet').textContent = Math.round(weeklyNet);
    document.getElementById('monthlyNet').textContent = Math.round(monthlyNet);
    document.getElementById('taxMonthly').textContent = Math.round(monthlyTax);
    document.getElementById('grossMonthly').textContent = Math.round(monthlyGross);
    document.getElementById('gasMonthly').textContent = Math.round(monthlyGas);
    document.getElementById('totalMiles').textContent = Math.round(monthlyMiles);
    document.getElementById('finalMonthly').textContent = Math.round(monthlyNet);
    
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