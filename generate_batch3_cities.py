#!/usr/bin/env python3
"""Generate Batch 3: Uncovered City Pages (23 pages)"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_batch1_centers import make_en_page, make_faq, AFFILIATE_BLOCK, PRO_TOOLKIT, related_reading, footer_related

BLOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'blog')

cities = [
    ('plasma-donation-evansville-in-2026', 'Evansville', 'IN', 'Indiana', 'Evansville metro area'),
    ('plasma-donation-vancouver-wa-2026', 'Vancouver', 'WA', 'Washington', 'Vancouver-Portland metro area'),
    ('plasma-donation-newport-news-va-2026', 'Newport News', 'VA', 'Virginia', 'Hampton Roads region'),
    ('plasma-donation-lake-charles-la-2026', 'Lake Charles', 'LA', 'Louisiana', 'Southwest Louisiana'),
    ('plasma-donation-peoria-il-2026', 'Peoria', 'IL', 'Illinois', 'Central Illinois'),
    ('plasma-donation-cranston-ri-2026', 'Cranston', 'RI', 'Rhode Island', 'Providence metro area'),
    ('plasma-donation-boca-raton-fl-2026', 'Boca Raton', 'FL', 'Florida', 'Palm Beach County'),
    ('plasma-donation-green-bay-wi-2026', 'Green Bay', 'WI', 'Wisconsin', 'Northeast Wisconsin'),
    ('plasma-donation-bowling-green-ky-2026', 'Bowling Green', 'KY', 'Kentucky', 'South-Central Kentucky'),
    ('plasma-donation-rio-rancho-nm-2026', 'Rio Rancho', 'NM', 'New Mexico', 'Albuquerque metro area'),
    ('plasma-donation-lewiston-me-2026', 'Lewiston', 'ME', 'Maine', 'Androscoggin County'),
    ('plasma-donation-pocatello-id-2026', 'Pocatello', 'ID', 'Idaho', 'Southeast Idaho'),
    ('plasma-donation-stamford-ct-2026', 'Stamford', 'CT', 'Connecticut', 'Fairfield County'),
    ('plasma-donation-sioux-city-ia-2026', 'Sioux City', 'IA', 'Iowa', 'Tri-State (IA/NE/SD) area'),
    ('plasma-donation-west-jordan-ut-2026', 'West Jordan', 'UT', 'Utah', 'Salt Lake Valley'),
    ('plasma-donation-van-nuys-ca-2026', 'Van Nuys', 'CA', 'California', 'San Fernando Valley, Los Angeles'),
    ('plasma-donation-frederick-md-2026', 'Frederick', 'MD', 'Maryland', 'Western Maryland'),
    ('plasma-donation-cedar-rapids-ia-2026', 'Cedar Rapids', 'IA', 'Iowa', 'Eastern Iowa'),
    ('plasma-donation-parkersburg-wv-2026', 'Parkersburg', 'WV', 'West Virginia', 'Mid-Ohio Valley'),
    ('plasma-donation-missoula-mt-2026', 'Missoula', 'MT', 'Montana', 'Western Montana'),
    ('plasma-donation-grand-forks-nd-2026', 'Grand Forks', 'ND', 'North Dakota', 'Red River Valley'),
    ('plasma-donation-hattiesburg-ms-2026', 'Hattiesburg', 'MS', 'Mississippi', 'Southeast Mississippi'),
    ('plasma-donation-oahu-hi-2026', 'Oahu', 'HI', 'Hawaii', 'Oahu island including Honolulu suburbs'),
]

def gen_city_page(slug, city, state_abbr, state_full, region):
    title = f"Plasma Donation {city}, {state_abbr} 2026: Best Centers & Pay Rates"
    meta = f"Find the best plasma donation centers in {city}, {state_abbr}. Compare pay rates, new donor bonuses up to $1,200, center locations, and hours in the {region} for 2026."
    category = f"{city} {state_abbr} 2026"

    toc = [
        ('quick-answer', 'Quick Answer'),
        ('overview', f'{city} Overview'),
        ('centers', 'Centers Near You'),
        ('pay-rates', 'Pay Rates'),
        ('new-donor', 'New Donor Bonuses'),
        ('tips', 'Local Tips'),
        ('faq', 'FAQ'),
    ]

    content = f'''
<div class="highlight-box" id="quick-answer"><h3>Quick Answer</h3><p>Plasma donors in <strong>{city}, {state_abbr}</strong> can earn <strong>$50-$100 per donation</strong> at local plasma centers, with new donor bonuses of <strong>$700-$1,200</strong> in the first month. Donating twice weekly yields $400-$1,000/month. Major chains in the {region} include CSL Plasma, BioLife, Octapharma, and Grifols — check below for which centers serve {city}.</p></div>

<h2 id="overview">Plasma Donation in {city}, {state_abbr}</h2>
<p>{city} is located in the {region} and offers several options for plasma donation. Whether you\'re a first-time donor looking to earn extra income or a regular donor seeking the best pay rates, this guide covers everything you need to know about donating plasma in {city} and surrounding areas.</p>

<h3>Key Facts for {city} Donors</h3>
<ul>
<li><strong>Average pay:</strong> $50-$100 per donation depending on center, weight, and promotions</li>
<li><strong>New donor bonuses:</strong> $700-$1,200 at most centers for first-month donors</li>
<li><strong>Donation frequency:</strong> Up to 2 times per week (48 hours between visits)</li>
<li><strong>Monthly potential:</strong> $400-$1,000 with consistent twice-weekly visits</li>
<li><strong>First visit:</strong> Allow 2-3 hours for screening and first donation</li>
</ul>

<h2 id="centers">Plasma Centers Near {city}, {state_abbr}</h2>
<p>Here are the major plasma center chains that serve the {city} area. Availability varies — use our <a href="/centers/" style="color: #0d9488; font-weight: 500;">Center Finder</a> to check exact locations near you.</p>

<table><thead><tr><th>Center</th><th>Pay Per Visit</th><th>New Donor Bonus</th><th>Monthly Potential</th></tr></thead><tbody>
<tr><td><a href="/blog/csl-plasma-pay-rates-2026.html">CSL Plasma</a></td><td>$50-$100</td><td>$700-$1,200</td><td>$400-$1,000</td></tr>
<tr><td><a href="/blog/biolife-plasma-pay-rates-2026.html">BioLife</a></td><td>$60-$100</td><td>$900-$1,100</td><td>$400-$900</td></tr>
<tr><td><a href="/blog/octapharma-plasma-pay-rates-2026.html">Octapharma</a></td><td>$50-$85</td><td>$800-$1,000</td><td>$450-$900</td></tr>
<tr><td><a href="/blog/grifols-plasma-pay-rates-2026.html">Grifols/Biomat</a></td><td>$50-$75</td><td>$700-$1,100</td><td>$400-$900</td></tr>
</tbody></table>

<p><strong>Note:</strong> Not all chains have locations in every city. Use the links above or our <a href="/centers/">Center Finder</a> to verify which centers are currently operating in {city}, {state_abbr}.</p>

{AFFILIATE_BLOCK}

<h2 id="pay-rates">Pay Rates in {city} 2026</h2>
<p>Plasma pay rates in {city} follow national pricing from each chain, with some local variation based on market competition and demand.</p>

<h3>Pay by Weight Category</h3>
<table><thead><tr><th>Weight</th><th>Volume</th><th>Per Visit</th><th>Monthly (8 visits)</th></tr></thead><tbody>
<tr><td>110-149 lbs</td><td>690 mL</td><td>$40-$65</td><td>$320-$520</td></tr>
<tr><td>150-174 lbs</td><td>825 mL</td><td>$50-$80</td><td>$400-$640</td></tr>
<tr><td>175-400 lbs</td><td>880 mL</td><td>$60-$100</td><td>$480-$800</td></tr>
</tbody></table>

<h3>Maximizing Pay in {city}</h3>
<ul>
<li><strong>Compare centers:</strong> Visit each center\'s website or call to check current promotions</li>
<li><strong>New donor shop:</strong> Start at whichever center has the highest new donor bonus right now</li>
<li><strong>Watch for local promotions:</strong> Centers in competitive markets often run extra bonuses</li>
<li><strong>Ask about referral bonuses:</strong> Earn $50-$100 per friend you refer</li>
</ul>

{PRO_TOOLKIT}

<h2 id="new-donor">New Donor Bonuses in {city}</h2>
<p>First-time donors in {city} can earn significantly more during their first month:</p>
<ul>
<li><strong>CSL Plasma:</strong> $700-$1,200 over 6-8 first-month donations</li>
<li><strong>BioLife:</strong> $900-$1,100 with app coupons applied</li>
<li><strong>Octapharma:</strong> $800-$1,000 through graduated bonuses</li>
<li><strong>Grifols:</strong> $700-$1,100 depending on location</li>
</ul>

<h3>What to Bring to Your First Donation</h3>
<ol>
<li>Valid government-issued photo ID (driver\'s license or state ID)</li>
<li>Proof of Social Security number (SSN card, tax form, or W-2)</li>
<li>Proof of current address (utility bill, lease, or bank statement within 30 days)</li>
<li>Water bottle for hydration</li>
</ol>

<h2 id="tips">Local Tips for {city} Donors</h2>
<ul>
<li><strong>Best times:</strong> Visit Tuesday-Thursday between 10am-2pm for shortest waits</li>
<li><strong>Preparation:</strong> Drink 64+ oz of water the day before donating</li>
<li><strong>Food:</strong> Eat a protein-rich meal 2-3 hours before your appointment</li>
<li><strong>Clothing:</strong> Wear short sleeves or a shirt that pushes up easily above the elbow</li>
<li><strong>Entertainment:</strong> Bring your phone, tablet, or book — donations take 45-90 minutes</li>
<li><strong>Nearby centers:</strong> If {city} centers have long waits, check surrounding communities in the {region}</li>
</ul>

{related_reading([
    ('/blog/which-plasma-center-pays-most-money.html', 'Which Center Pays the Most Money?'),
    ('/blog/ultimate-first-time-plasma-donor-guide-2026.html', 'First-Time Donor Guide'),
    ('/calculators/', 'Plasma Pay Calculator'),
    ('/blog/best-times-donate-plasma-2026.html', 'Best Times to Donate Plasma'),
])}

<h2 id="faq">Frequently Asked Questions</h2>

<h3>Where can I donate plasma in {city}, {state_abbr}?</h3>
<p>Plasma donation centers in the {city} area may include CSL Plasma, BioLife, Octapharma, and Grifols locations. Use our <a href="/centers/">Center Finder</a> to see which chains currently operate in {city} and compare their pay rates.</p>

<h3>How much does plasma donation pay in {city}?</h3>
<p>Plasma donation in {city} pays $50-$100 per visit for repeat donors and $700-$1,200 for new donors in their first month. Monthly earnings range from $400-$1,000 with twice-weekly donations. Pay varies by center, weight, and current promotions.</p>

<h3>What do I need to donate plasma in {city}?</h3>
<p>You need a valid photo ID, proof of Social Security number, proof of local address, and to be 18-69 years old weighing at least 110 lbs. Your first visit takes 2-3 hours including a medical screening.</p>

<h3>Which plasma center pays the most in {city}?</h3>
<p>Pay rates vary by location and current promotions. Generally, CSL Plasma and BioLife offer the highest rates ($50-$100/visit). Check current promotions at each center in {city} — new donor bonuses can make a significant difference in your first month.</p>

{footer_related()}'''

    faqs = [
        make_faq(f"Where can I donate plasma in {city}, {state_abbr}?", f"Centers in the {city} area may include CSL Plasma, BioLife, Octapharma, and Grifols. Use our Center Finder to check current locations."),
        make_faq(f"How much does plasma donation pay in {city}?", f"$50-$100 per visit for repeat donors, $700-$1,200 for new donors in the first month. Monthly potential: $400-$1,000."),
        make_faq(f"What do I need to donate plasma in {city}?", "Valid photo ID, SSN proof, proof of address, age 18-69, weight 110+ lbs."),
    ]

    return make_en_page(slug, title, meta, category, 8, toc, content, faqs)


if __name__ == '__main__':
    print("Generating Batch 3: City Pages (23 pages)...")
    for slug, city, state_abbr, state_full, region in cities:
        html = gen_city_page(slug, city, state_abbr, state_full, region)
        path = os.path.join(BLOG_DIR, f"{slug}.html")
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"  Created: blog/{slug}.html")
    print(f"Done! Generated {len(cities)} city pages.")
