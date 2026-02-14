#!/usr/bin/env python3
"""Generate Round 2 Batch 2 Part 2: Process/Science Deep-Dive Pages 20-30 (11 pages)"""
import os
from generate_batch1_centers import make_en_page, make_faq, AFFILIATE_BLOCK, PRO_TOOLKIT, related_reading, footer_related

BLOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'blog')

# Note: Pages 16-19 are in generate_round2_batch2_science.py
# This file contains pages 20-30

# ============ PAGE 20: Volume Calculation by Weight ============
def generate_page_20():
    slug = 'how-plasma-donation-volume-calculated-by-weight-2026'
    title = 'How Plasma Donation Volume Is Calculated by Weight: FDA Tiers Explained (2026)'
    meta_desc = 'Complete guide to FDA weight tiers for plasma donation: 110-149, 150-174, 175+ lbs. Volume collected (690/825/880 mL), why weight matters, safety thresholds.'
    category = 'Donation Process'
    read_time = 10

    toc_items = [
        ('quick-answer', 'Quick Answer'),
        ('fda-tiers', 'FDA Weight Tiers & Volume'),
        ('why-weight-matters', 'Why Weight Determines Volume'),
        ('safety-ratios', 'Safety: Plasma-to-Body Ratio'),
        ('volume-calculation', 'How Centers Calculate Your Volume'),
        ('faq', 'FAQ')
    ]

    content_html = f'''
<div class="quick-answer" style="background: #f0fdf4; border-left: 4px solid #10b981; padding: 1.5rem; margin: 2rem 0; border-radius: 8px;">
    <h2 style="margin-top: 0; color: #065f46; font-size: 1.3rem;">Quick Answer</h2>
    <p style="margin: 0; font-size: 1.05rem; line-height: 1.6;"><strong>FDA regulations set maximum plasma volumes based on donor weight tiers:</strong> 110-149 lbs can donate up to 690 mL, 150-174 lbs up to 825 mL, and 175+ lbs up to 880 mL. This ensures no more than 12-15% of your total blood volume is removed per donation, maintaining safety and allowing your body to regenerate plasma within 48 hours.</p>
</div>

<h2 id="fda-tiers">FDA Weight Tiers & Volume Limits</h2>

<p>The FDA Code of Federal Regulations (21 CFR 640.65) establishes strict volume limits based on body weight:</p>

<table style="width: 100%; border-collapse: collapse; margin: 1.5rem 0;">
    <thead>
        <tr style="background: #f3f4f6;">
            <th style="padding: 12px; text-align: left; border: 1px solid #e5e7eb;">Weight Range (lbs)</th>
            <th style="padding: 12px; text-align: left; border: 1px solid #e5e7eb;">Weight Range (kg)</th>
            <th style="padding: 12px; text-align: left; border: 1px solid #e5e7eb;">Max Plasma Volume</th>
            <th style="padding: 12px; text-align: left; border: 1px solid #e5e7eb;">% of Blood Volume</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="padding: 12px; border: 1px solid #e5e7eb;"><strong>110-149 lbs</strong></td>
            <td style="padding: 12px; border: 1px solid #e5e7eb;">50-67 kg</td>
            <td style="padding: 12px; border: 1px solid #e5e7eb;">690 mL</td>
            <td style="padding: 12px; border: 1px solid #e5e7eb;">~12-15%</td>
        </tr>
        <tr style="background: #f9fafb;">
            <td style="padding: 12px; border: 1px solid #e5e7eb;"><strong>150-174 lbs</strong></td>
            <td style="padding: 12px; border: 1px solid #e5e7eb;">68-79 kg</td>
            <td style="padding: 12px; border: 1px solid #e5e7eb;">825 mL</td>
            <td style="padding: 12px; border: 1px solid #e5e7eb;">~13-16%</td>
        </tr>
        <tr>
            <td style="padding: 12px; border: 1px solid #e5e7eb;"><strong>175+ lbs</strong></td>
            <td style="padding: 12px; border: 1px solid #e5e7eb;">80+ kg</td>
            <td style="padding: 12px; border: 1px solid #e5e7eb;">880 mL</td>
            <td style="padding: 12px; border: 1px solid #e5e7eb;">~12-14%</td>
        </tr>
    </tbody>
</table>

<p><strong>Important Notes:</strong></p>
<ul>
    <li><strong>Minimum weight:</strong> You must weigh at least 110 lbs (50 kg) to donate plasma in the U.S.</li>
    <li><strong>Weight verification:</strong> You're weighed at every donation (shoes off, after emptying pockets).</li>
    <li><strong>Machine settings:</strong> Apheresis machines are programmed with your weight to stop collection at the appropriate volume.</li>
    <li><strong>No overrides:</strong> Staff cannot manually increase your volume beyond FDA limits, even if you request it.</li>
</ul>

<h2 id="why-weight-matters">Why Weight Determines Donation Volume</h2>

<h3>Total Blood Volume Formula</h3>

<p>Your total blood volume is proportional to your body weight:</p>

<ul>
    <li><strong>Men:</strong> ~75 mL of blood per kg of body weight</li>
    <li><strong>Women:</strong> ~65 mL of blood per kg of body weight (slightly less due to higher body fat percentage)</li>
</ul>

<p><strong>Example Calculation (150 lb woman):</strong></p>
<ul>
    <li>150 lbs ÷ 2.2 = 68 kg</li>
    <li>68 kg × 65 mL/kg = 4,420 mL total blood volume</li>
    <li>Plasma portion (~55% of blood) = 2,431 mL</li>
    <li>FDA limit (825 mL) = 34% of total plasma, 19% of total blood volume</li>
</ul>

<h3>Why the 12-15% Threshold?</h3>

<p>Removing more than 15% of blood volume at once can cause:</p>
<ul>
    <li><strong>Hypotension:</strong> Drop in blood pressure leading to dizziness, fainting</li>
    <li><strong>Hypovolemic shock:</strong> Inadequate oxygen delivery to organs (rare but dangerous)</li>
    <li><strong>Prolonged recovery:</strong> Body takes longer than 48 hours to replace plasma, risking protein depletion with twice-weekly donations</li>
</ul>

{AFFILIATE_BLOCK}

<h2 id="safety-ratios">Safety: Plasma-to-Body Weight Ratio</h2>

<p>The FDA volume limits maintain a safe plasma-to-body weight ratio across all donors:</p>

<table style="width: 100%; border-collapse: collapse; margin: 1.5rem 0;">
    <thead>
        <tr style="background: #f3f4f6;">
            <th style="padding: 12px; text-align: left; border: 1px solid #e5e7eb;">Donor Profile</th>
            <th style="padding: 12px; text-align: left; border: 1px solid #e5e7eb;">Weight</th>
            <th style="padding: 12px; text-align: left; border: 1px solid #e5e7eb;">Volume Collected</th>
            <th style="padding: 12px; text-align: left; border: 1px solid #e5e7eb;">mL per kg Body Weight</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="padding: 12px; border: 1px solid #e5e7eb;">Small donor</td>
            <td style="padding: 12px; border: 1px solid #e5e7eb;">110 lbs (50 kg)</td>
            <td style="padding: 12px; border: 1px solid #e5e7eb;">690 mL</td>
            <td style="padding: 12px; border: 1px solid #e5e7eb;">13.8 mL/kg</td>
        </tr>
        <tr style="background: #f9fafb;">
            <td style="padding: 12px; border: 1px solid #e5e7eb;">Medium donor</td>
            <td style="padding: 12px; border: 1px solid #e5e7eb;">160 lbs (73 kg)</td>
            <td style="padding: 12px; border: 1px solid #e5e7eb;">825 mL</td>
            <td style="padding: 12px; border: 1px solid #e5e7eb;">11.3 mL/kg</td>
        </tr>
        <tr>
            <td style="padding: 12px; border: 1px solid #e5e7eb;">Large donor</td>
            <td style="padding: 12px; border: 1px solid #e5e7eb;">200 lbs (91 kg)</td>
            <td style="padding: 12px; border: 1px solid #e5e7eb;">880 mL</td>
            <td style="padding: 12px; border: 1px solid #e5e7eb;">9.7 mL/kg</td>
        </tr>
    </tbody>
</table>

<p><strong>Key Insight:</strong> Heavier donors give proportionally less plasma per kg of body weight, which is why they tolerate donations better and recover faster.</p>

{PRO_TOOLKIT}

<h2 id="volume-calculation">How Plasma Centers Calculate Your Exact Volume</h2>

<p>When you check in for donation, here's what happens:</p>

<h3>Step 1: Weight Verification</h3>
<ul>
    <li>You remove shoes and empty pockets</li>
    <li>Staff weighs you on a certified medical scale</li>
    <li>Weight is entered into the donor management system</li>
</ul>

<h3>Step 2: FDA Tier Assignment</h3>
<ul>
    <li>System automatically assigns you to tier 1, 2, or 3 based on weight</li>
    <li>If you're on a tier boundary (e.g., 149.5 lbs), you may be placed in the lower tier for safety</li>
</ul>

<h3>Step 3: Machine Programming</h3>
<ul>
    <li>Phlebotomist enters your weight into the apheresis machine</li>
    <li>Machine calculates the exact volume to collect (often slightly less than the FDA maximum)</li>
    <li>Machine stops automatically when target volume is reached</li>
</ul>

<h3>Step 4: Real-Time Monitoring</h3>
<ul>
    <li>Machine displays volume collected on screen (you can usually see it)</li>
    <li>If you experience adverse reaction, staff can stop donation early (you're still compensated for partial donation)</li>
</ul>

<h3>Actual Volumes Collected (May Be Less Than Maximum)</h3>

<p>Many centers program machines to collect 10-50 mL less than the FDA limit to account for:</p>
<ul>
    <li><strong>Anticoagulant volume:</strong> Citrate solution added to plasma</li>
    <li><strong>System residual:</strong> Small amount of plasma left in tubing</li>
    <li><strong>Safety margin:</strong> Ensures they don't accidentally exceed FDA limit</li>
</ul>

<p><strong>Example:</strong> A 180-lb donor's machine may be set to collect 850 mL instead of the full 880 mL maximum.</p>

{related_reading([
    ('/blog/why-plasma-centers-pay-more-for-heavier-donors-2026', 'Why Heavier Donors Earn More Money'),
    ('/blog/first-plasma-donation-what-to-expect-2026', 'First Plasma Donation Guide'),
    ('/blog/plasma-donation-day-before-checklist-2026', 'Day-Before Checklist for Faster Donation')
])}

<h2 id="faq">Frequently Asked Questions</h2>

<div class="faq-item" style="margin-bottom: 1.5rem;">
    <h3 style="color: #0c4a6e; font-size: 1.15rem;">What happens if my weight drops below 110 lbs?</h3>
    <p>You'll be deferred from donating until your weight reaches at least 110 lbs. This is a non-negotiable FDA requirement. If you're consistently close to this threshold, consider weighing yourself at home before going to the center to avoid wasted trips.</p>
</div>

<div class="faq-item" style="margin-bottom: 1.5rem;">
    <h3 style="color: #0c4a6e; font-size: 1.15rem;">If I lose or gain weight, does my donation volume change?</h3>
    <p>Yes, immediately. Since you're weighed at every donation, any weight change is reflected in your FDA tier and collection volume that same day. Gaining 25+ lbs can move you to a higher tier, increasing both volume collected and compensation.</p>
</div>

<div class="faq-item" style="margin-bottom: 1.5rem;">
    <h3 style="color: #0c4a6e; font-size: 1.15rem;">Can I wear heavy clothes to weigh more and donate more plasma?</h3>
    <p>Technically yes, but it's not recommended. Some donors wear jeans and a hoodie to add 2-5 lbs, which might push them over a tier threshold (e.g., from 148 lbs to 151 lbs). However, staff may ask you to remove heavy items if they suspect you're gaming the system. Focus on healthy weight gain (muscle/hydration) if you want to increase volume long-term.</p>
</div>

<div class="faq-item" style="margin-bottom: 1.5rem;">
    <h3 style="color: #0c4a6e; font-size: 1.15rem;">Why is the 175+ tier volume (880 mL) not much higher than 150-174 tier (825 mL)?</h3>
    <p>The FDA sets conservative limits to protect all donors. While a 250-lb donor could theoretically safely donate 1,000+ mL, the FDA uses a one-size-fits-most approach. The 880 mL limit balances safety (works for a 175-lb donor) with collection efficiency (sufficient volume for pharmaceutical processing).</p>
</div>

{footer_related()}
'''

    faq_schema = [
        make_faq(
            "What happens if my weight drops below 110 lbs?",
            "You'll be deferred from donating until your weight reaches at least 110 lbs. This is a non-negotiable FDA requirement."
        ),
        make_faq(
            "If I lose or gain weight, does my donation volume change?",
            "Yes, immediately. Since you're weighed at every donation, any weight change is reflected in your FDA tier and collection volume that same day."
        ),
        make_faq(
            "Can I wear heavy clothes to weigh more and donate more plasma?",
            "Technically yes, but staff may ask you to remove heavy items if they suspect gaming. Focus on healthy weight gain if you want to increase volume long-term."
        ),
        make_faq(
            "Why is the 175+ tier volume not much higher than 150-174 tier?",
            "The FDA sets conservative limits to protect all donors. The 880 mL limit balances safety with collection efficiency."
        ),
    ]

    html = make_en_page(slug, title, meta_desc, category, read_time, toc_items, content_html, faq_schema)

    with open(os.path.join(BLOG_DIR, f'{slug}.html'), 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✓ Generated {slug}.html")

# ============ RUN ALL ============
if __name__ == '__main__':
    os.makedirs(BLOG_DIR, exist_ok=True)
    print("Generating Round 2 Batch 2 Part 2: Pages 20-30...")
    generate_page_20()
    print("\n✓ Part 2 started: 1 page generated so far")
