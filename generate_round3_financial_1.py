#!/usr/bin/env python3
"""Generate Round 3 Financial/Benefits Blog Pages (4 pages):
1. plasma-donation-and-section-8-housing-2026
2. plasma-donation-and-wic-benefits-2026
3. plasma-donation-and-tanf-welfare-2026
4. plasma-donation-1099-tax-form-explained-2026
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_batch1_centers import make_en_page, make_faq, AFFILIATE_BLOCK, PRO_TOOLKIT, related_reading, footer_related
BLOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'blog')


# ============================================================
# Page 1: Plasma Donation and Section 8 Housing
# ============================================================
def gen_section_8():
    slug = "plasma-donation-and-section-8-housing-2026"
    title = "Does Plasma Donation Income Affect Section 8 Housing? 2026 Guide"
    meta_desc = "Find out if plasma donation income affects your Section 8 housing voucher. Learn HUD income reporting rules, recertification tips, and strategies to stay compliant in 2026."
    category = "Benefits & Compliance"
    read_time = 10

    toc = [
        ("quick-answer", "Quick Answer"),
        ("how-section-8-works", "How Section 8 Counts Income"),
        ("plasma-income-reporting", "Reporting Plasma Income"),
        ("income-thresholds", "Income Threshold Table"),
        ("annual-recertification", "Annual Recertification"),
        ("strategies", "Strategies to Stay Compliant"),
        ("faq", "FAQ"),
    ]

    content = f'''
<div class="highlight-box" id="quick-answer">
<h3>Quick Answer</h3>
<p><strong>Yes, plasma donation income MAY need to be reported as "other income" to your local housing authority.</strong> HUD counts virtually all income sources when determining eligibility and voucher amounts for the Section 8 Housing Choice Voucher (HCV) program. However, the practical impact depends on how much you earn and your household's total income. Most plasma donors earning $400-$800/month will see only a modest effect on their rent portion &mdash; if any.</p>
</div>

<h2 id="how-section-8-works">How Section 8 Counts Income</h2>
<p>The Section 8 Housing Choice Voucher (HCV) program uses <strong>Annual Adjusted Income</strong> to calculate your rent portion. HUD requires housing authorities to count all income received by household members, including:</p>
<ul>
<li><strong>Wages and salaries</strong> from employment</li>
<li><strong>Self-employment income</strong> (net)</li>
<li><strong>Social Security, SSI, SSDI</strong> payments</li>
<li><strong>Other recurring income</strong> &mdash; this is where plasma income may fall</li>
<li><strong>Any regular contributions or gifts</strong></li>
</ul>

<p>Your housing authority sets your rent at <strong>30% of your adjusted monthly income</strong> (with some deductions). So any additional income you report could increase your rent portion.</p>

<h3>Does Plasma Income Count as "Earned Income" or "Other Income"?</h3>
<p>Plasma compensation is generally classified by the IRS as <strong>"other income"</strong> (reported on Schedule 1, Line 8z), not wages or self-employment income. For HUD purposes, your housing authority may classify it as:</p>
<ul>
<li><strong>Other recurring income</strong> if you donate regularly</li>
<li><strong>Irregular/sporadic income</strong> if you donate infrequently (may be excluded in some cases)</li>
</ul>

<p>The distinction matters: truly irregular, one-time income may sometimes be excluded from annual income calculations under HUD rules.</p>

<h2 id="plasma-income-reporting">Reporting Plasma Income to Your Housing Authority</h2>
<p>HUD requires tenants to report <strong>all changes in income</strong> between annual recertifications if the change is significant. Here is how plasma income fits in:</p>

<table>
<thead><tr><th>Scenario</th><th>Reporting Obligation</th><th>Likely Impact</th></tr></thead>
<tbody>
<tr><td>Donate 1-2x per month (under $200/mo)</td><td>May not trigger interim reporting</td><td>Minimal &mdash; usually captured at annual recert</td></tr>
<tr><td>Donate regularly, $400-$600/mo</td><td>Should report at next recertification</td><td>Moderate &mdash; could raise rent $120-$180/mo</td></tr>
<tr><td>Donate 2x/week, $700-$1,000/mo</td><td>Report promptly &mdash; significant income change</td><td>Higher &mdash; rent may increase $210-$300/mo</td></tr>
</tbody>
</table>

<p><strong>Important:</strong> Failing to report income can result in <strong>termination of your voucher</strong>, repayment demands, or even fraud charges. Always err on the side of disclosure.</p>

{AFFILIATE_BLOCK}

<h2 id="income-thresholds">When Does Plasma Income Actually Affect Your Voucher?</h2>
<p>Section 8 eligibility is based on Area Median Income (AMI). Here is an approximate table showing 2026 HCV income limits for common household sizes (these vary significantly by metro area):</p>

<table>
<thead><tr><th>Household Size</th><th>Extremely Low (30% AMI)</th><th>Very Low (50% AMI)</th><th>Low (80% AMI)</th></tr></thead>
<tbody>
<tr><td>1 Person</td><td>$16,500 - $24,000</td><td>$27,500 - $40,000</td><td>$44,000 - $64,000</td></tr>
<tr><td>2 Persons</td><td>$18,850 - $27,400</td><td>$31,400 - $45,700</td><td>$50,300 - $73,100</td></tr>
<tr><td>3 Persons</td><td>$21,200 - $30,850</td><td>$35,350 - $51,400</td><td>$56,550 - $82,250</td></tr>
<tr><td>4 Persons</td><td>$23,550 - $34,250</td><td>$39,250 - $57,100</td><td>$62,800 - $91,350</td></tr>
</tbody>
</table>

<p><em>Note: Ranges reflect differences between rural and high-cost metro areas. Check your local PHA for exact limits.</em></p>

<h3>Impact Math Example</h3>
<p>If you earn $600/month from plasma ($7,200/year) and your household income is $20,000/year:</p>
<ul>
<li><strong>Without plasma:</strong> 30% of $20,000 &divide; 12 = <strong>$500/mo rent portion</strong></li>
<li><strong>With plasma:</strong> 30% of $27,200 &divide; 12 = <strong>$680/mo rent portion</strong></li>
<li><strong>Difference: $180/mo more in rent</strong></li>
</ul>
<p>In this example, you would net $420/month from plasma after the rent increase &mdash; still a significant financial gain.</p>

{PRO_TOOLKIT}

<h2 id="annual-recertification">Annual Recertification: When and How to Report</h2>
<p>Every Section 8 household must undergo <strong>annual recertification</strong> where the housing authority reviews all income sources. Here is what to expect:</p>

<h3>Timeline</h3>
<ol>
<li><strong>90 days before anniversary:</strong> Housing authority sends recertification packet</li>
<li><strong>60 days before:</strong> Submit completed paperwork with income documentation</li>
<li><strong>30 days before:</strong> Interview/meeting with housing specialist</li>
<li><strong>Anniversary date:</strong> New rent amount takes effect</li>
</ol>

<h3>Documents to Prepare for Plasma Income</h3>
<ul>
<li>Payment statements from your plasma center (printed from app/website)</li>
<li>1099-NEC forms if you received one (for $600+ from a single center)</li>
<li>Bank or debit card statements showing deposits</li>
<li>A log of donation dates and amounts (recommended)</li>
</ul>

<h3>Interim Reporting</h3>
<p>Many housing authorities also require <strong>interim reporting</strong> if your income increases by a certain threshold (commonly $200+/month or 10%+ of annual income) between annual recertifications. Check your lease and PHA rules.</p>

<h2 id="strategies">Strategies to Stay Compliant While Donating</h2>
<ol>
<li><strong>Keep meticulous records:</strong> Track every donation date, amount paid, and center visited in a spreadsheet or notebook</li>
<li><strong>Use a separate bank account or debit card:</strong> Keep plasma income easily identifiable and separate from other funds</li>
<li><strong>Contact your housing authority proactively:</strong> Ask your caseworker specifically how to report plasma income before your next recertification</li>
<li><strong>Understand your deductions:</strong> HUD allows certain deductions (childcare, medical, disability) that can offset income increases</li>
<li><strong>Calculate the net benefit:</strong> Even with a rent increase, most donors still come out ahead &mdash; do the math for your specific situation</li>
<li><strong>Save documentation:</strong> Keep 1099s, payment histories, and donation logs for at least 3 years</li>
</ol>

<div style="background: #fef3c7; border-left: 4px solid #f59e0b; padding: 1rem 1.5rem; border-radius: 8px; margin: 1.5rem 0;">
<p style="margin: 0; font-weight: 600; color: #92400e;">Disclaimer</p>
<p style="margin: 0.5rem 0 0; color: #78350f;">This article is for informational purposes only and does not constitute legal or financial advice. Section 8 rules vary by housing authority. Always consult your local Public Housing Authority (PHA) or a housing counselor for guidance specific to your situation.</p>
</div>

{related_reading([
    ("/blog/plasma-donation-and-wic-benefits-2026.html", "Does Plasma Donation Affect WIC Benefits?"),
    ("/blog/plasma-donation-and-tanf-welfare-2026.html", "Plasma Donation & TANF/Welfare Benefits"),
    ("/blog/plasma-donation-1099-tax-form-explained-2026.html", "Plasma Donation 1099 Tax Form Explained"),
    ("/blog/plasma-donation-taxes-2026.html", "Complete Plasma Donation Tax Guide 2026"),
])}

<h2 id="faq">Frequently Asked Questions</h2>

<h3>Does HUD count plasma income for Section 8?</h3>
<p>Yes, HUD generally requires housing authorities to count all income sources, including plasma donation income. It is typically classified as "other income." However, truly irregular or one-time income may be treated differently depending on your local PHA's policies.</p>

<h3>Will I lose my Section 8 voucher if I donate plasma?</h3>
<p>Donating plasma alone will not cause you to lose your voucher. However, failing to report the income could result in voucher termination. If your total household income exceeds program limits due to plasma income, you could eventually lose eligibility &mdash; but this is rare since plasma income alone is usually not enough to push families above the income ceiling.</p>

<h3>How much will my rent go up if I report plasma income?</h3>
<p>Your rent portion increases by approximately 30% of any additional income. For example, $600/month in plasma income would increase your rent by about $180/month, leaving you with a net gain of $420/month. The exact calculation depends on your housing authority's deduction policies.</p>

<h3>Do I need to report plasma income between annual recertifications?</h3>
<p>Many housing authorities require interim reporting for significant income changes (typically $200+/month increase). Check your specific PHA's interim reporting policy. At minimum, you must report at your annual recertification.</p>

<h3>Can I use a separate bank account to keep plasma income organized for HUD?</h3>
<p>Yes, using a separate account or keeping your plasma center debit card separate is an excellent strategy. It makes it easy to document your plasma income at recertification time and shows your housing authority clear records of this income source.</p>

{footer_related()}'''

    faqs = [
        make_faq("Does HUD count plasma income for Section 8?",
                 "Yes, HUD generally requires housing authorities to count all income sources, including plasma donation income. It is typically classified as other income. However, truly irregular income may be treated differently by your local PHA."),
        make_faq("Will I lose my Section 8 voucher if I donate plasma?",
                 "Donating plasma alone will not cause you to lose your voucher. Failing to report the income could result in termination. Plasma income alone is usually not enough to push families above the income ceiling."),
        make_faq("How much will my rent go up if I report plasma income?",
                 "Your rent portion increases by approximately 30% of additional income. For example, $600/month in plasma income would increase rent by about $180/month, netting you $420/month."),
        make_faq("Do I need to report plasma income between annual recertifications?",
                 "Many housing authorities require interim reporting for income changes of $200+/month. Check your PHA's policy. At minimum, you must report at annual recertification."),
        make_faq("Can I use a separate bank account to keep plasma income organized for HUD?",
                 "Yes, using a separate account is an excellent strategy for documenting plasma income and making recertification paperwork straightforward."),
    ]

    html = make_en_page(slug, title, meta_desc, category, read_time, toc, content, faqs)
    path = os.path.join(BLOG_DIR, f"{slug}.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  Created: blog/{slug}.html")


# ============================================================
# Page 2: Plasma Donation and WIC Benefits
# ============================================================
def gen_wic():
    slug = "plasma-donation-and-wic-benefits-2026"
    title = "Does Plasma Donation Affect WIC Benefits? 2026 Guide"
    meta_desc = "Does plasma donation income affect your WIC benefits? Learn about WIC income limits, how plasma income is treated, and why most plasma donors keep their WIC eligibility in 2026."
    category = "Benefits & Compliance"
    read_time = 9

    toc = [
        ("quick-answer", "Quick Answer"),
        ("how-wic-income-works", "How WIC Determines Income"),
        ("wic-income-limits", "2026 WIC Income Limits"),
        ("plasma-impact", "Plasma Income Impact on WIC"),
        ("comparison-programs", "Comparison With Other Programs"),
        ("tips", "Tips for WIC Recipients"),
        ("faq", "FAQ"),
    ]

    content = f'''
<div class="highlight-box" id="quick-answer">
<h3>Quick Answer</h3>
<p><strong>Plasma donation income generally does NOT affect WIC benefits.</strong> WIC (Women, Infants, and Children) uses <strong>gross household income</strong> to determine eligibility, and the program's income limits are generous enough that plasma income ($400-$1,000/month) typically does not push families over the threshold. Most WIC recipients can donate plasma without losing their food benefits.</p>
</div>

<h2 id="how-wic-income-works">How WIC Determines Income Eligibility</h2>
<p>WIC eligibility is based on <strong>gross household income</strong> at or below <strong>185% of the Federal Poverty Level (FPL)</strong>. Here is what WIC considers:</p>

<h3>Income WIC Counts</h3>
<ul>
<li><strong>Wages and salaries</strong> (gross, before taxes)</li>
<li><strong>Self-employment income</strong></li>
<li><strong>Social Security, SSI, SSDI</strong></li>
<li><strong>Child support received</strong></li>
<li><strong>Unemployment benefits</strong></li>
<li><strong>Other recurring income</strong> &mdash; plasma income could fall here</li>
</ul>

<h3>Income WIC Does NOT Count</h3>
<ul>
<li>SNAP/food stamp benefits</li>
<li>TANF/welfare payments (in most states)</li>
<li>Housing assistance (Section 8 vouchers)</li>
<li>Loans and one-time gifts</li>
<li>Tax refunds (including EITC)</li>
</ul>

<h3>Adjunctive Eligibility (Automatic Qualification)</h3>
<p>If you or anyone in your household participates in <strong>SNAP, Medicaid, or TANF</strong>, you are <strong>automatically income-eligible</strong> for WIC &mdash; no further income verification needed. This means plasma income is completely irrelevant if you qualify through adjunctive eligibility.</p>

{AFFILIATE_BLOCK}

<h2 id="wic-income-limits">2026 WIC Income Limits by Household Size</h2>
<p>WIC uses 185% of the Federal Poverty Level. Here are the 2026 income limits:</p>

<table>
<thead><tr><th>Household Size</th><th>Annual Income Limit</th><th>Monthly Income Limit</th><th>Weekly Income Limit</th></tr></thead>
<tbody>
<tr><td>1</td><td>$27,861</td><td>$2,322</td><td>$536</td></tr>
<tr><td>2</td><td>$37,814</td><td>$3,152</td><td>$728</td></tr>
<tr><td>3</td><td>$47,767</td><td>$3,981</td><td>$919</td></tr>
<tr><td>4</td><td>$57,720</td><td>$4,810</td><td>$1,110</td></tr>
<tr><td>5</td><td>$67,673</td><td>$5,640</td><td>$1,302</td></tr>
<tr><td>6</td><td>$77,626</td><td>$6,469</td><td>$1,493</td></tr>
<tr><td>7</td><td>$87,579</td><td>$7,299</td><td>$1,685</td></tr>
<tr><td>8</td><td>$97,532</td><td>$8,128</td><td>$1,876</td></tr>
</tbody>
</table>
<p><em>Each additional person: add $9,953/year. Based on 2026 Federal Poverty Guidelines at 185%.</em></p>

<h2 id="plasma-impact">Why Plasma Income Usually Does Not Affect WIC</h2>
<p>For most WIC-eligible families, plasma donation income creates a comfortable buffer below the income limits:</p>

<h3>Example: Family of 3</h3>
<table>
<thead><tr><th>Scenario</th><th>Monthly Income</th><th>Annual Income</th><th>WIC Limit (Family of 3)</th><th>Eligible?</th></tr></thead>
<tbody>
<tr><td>Part-time job only</td><td>$1,800</td><td>$21,600</td><td>$47,767</td><td>Yes &mdash; $26,167 buffer</td></tr>
<tr><td>Part-time + plasma ($500/mo)</td><td>$2,300</td><td>$27,600</td><td>$47,767</td><td>Yes &mdash; $20,167 buffer</td></tr>
<tr><td>Part-time + plasma ($1,000/mo)</td><td>$2,800</td><td>$33,600</td><td>$47,767</td><td>Yes &mdash; $14,167 buffer</td></tr>
<tr><td>Full-time job ($15/hr) + plasma ($800/mo)</td><td>$3,400</td><td>$40,800</td><td>$47,767</td><td>Yes &mdash; $6,967 buffer</td></tr>
</tbody>
</table>

<p>As this table shows, even aggressive plasma donation schedules rarely push WIC-eligible families over the income limit. You would need to be very close to the income ceiling already for plasma income to make a difference.</p>

<h3>When Plasma Income COULD Affect WIC</h3>
<p>Plasma income may matter in these narrow situations:</p>
<ul>
<li>Your household income is <strong>already within $5,000-$10,000 of the WIC limit</strong></li>
<li>You are a <strong>single person</strong> with the lowest income limit ($27,861)</li>
<li>Multiple household members are donating plasma, adding $1,500-$2,000/month combined</li>
</ul>

{PRO_TOOLKIT}

<h2 id="comparison-programs">How WIC Compares to Other Benefit Programs</h2>
<table>
<thead><tr><th>Program</th><th>Plasma Income Impact</th><th>Income Standard</th><th>Notes</th></tr></thead>
<tbody>
<tr><td><strong>WIC</strong></td><td>Minimal</td><td>185% FPL</td><td>Generous limits; adjunctive eligibility bypasses income test</td></tr>
<tr><td><strong>SNAP</strong></td><td>Moderate</td><td>130% FPL (gross)</td><td>Lower limits; plasma income more likely to matter</td></tr>
<tr><td><strong>Medicaid</strong></td><td>Varies</td><td>138% FPL (ACA states)</td><td>Depends on state and category</td></tr>
<tr><td><strong>Section 8</strong></td><td>Moderate</td><td>50% AMI</td><td>Affects rent portion, not just eligibility</td></tr>
<tr><td><strong>TANF</strong></td><td>High</td><td>Varies by state</td><td>Very low income limits; most affected by extra income</td></tr>
</tbody>
</table>

<h2 id="tips">Tips for WIC Recipients Who Donate Plasma</h2>
<ol>
<li><strong>Check your adjunctive eligibility:</strong> If you receive SNAP, Medicaid, or TANF, you are automatically WIC-eligible regardless of income</li>
<li><strong>Know your buffer:</strong> Calculate how far your household income is below the WIC limit before adding plasma income</li>
<li><strong>Keep records:</strong> Save donation payment records in case your WIC office asks about income sources</li>
<li><strong>Be honest at certification:</strong> WIC offices certify eligibility every 6-12 months &mdash; disclose all income sources</li>
<li><strong>Remember WIC is categorical:</strong> You must also be pregnant, breastfeeding, postpartum, or have a child under 5 &mdash; income is only one requirement</li>
</ol>

<div style="background: #fef3c7; border-left: 4px solid #f59e0b; padding: 1rem 1.5rem; border-radius: 8px; margin: 1.5rem 0;">
<p style="margin: 0; font-weight: 600; color: #92400e;">Disclaimer</p>
<p style="margin: 0.5rem 0 0; color: #78350f;">This article is for informational purposes only. WIC policies can vary by state. Contact your local WIC office for guidance specific to your household.</p>
</div>

{related_reading([
    ("/blog/plasma-donation-and-section-8-housing-2026.html", "Plasma Donation & Section 8 Housing"),
    ("/blog/plasma-donation-and-tanf-welfare-2026.html", "Plasma Donation & TANF/Welfare Benefits"),
    ("/blog/plasma-donation-1099-tax-form-explained-2026.html", "Plasma Donation 1099 Tax Form Explained"),
    ("/blog/plasma-donation-taxes-2026.html", "Complete Plasma Donation Tax Guide 2026"),
])}

<h2 id="faq">Frequently Asked Questions</h2>

<h3>Does WIC count plasma donation money as income?</h3>
<p>WIC may count plasma income as "other income" when determining eligibility. However, if you qualify through adjunctive eligibility (receiving SNAP, Medicaid, or TANF), your income is not checked at all. For most families, plasma income is too small to affect WIC eligibility.</p>

<h3>Can I donate plasma while receiving WIC?</h3>
<p>Yes. There is no rule preventing WIC recipients from donating plasma. WIC eligibility is based on income thresholds, and plasma income ($400-$1,000/month) rarely pushes families over the generous 185% FPL limits.</p>

<h3>Will I lose WIC if I earn $800/month from plasma?</h3>
<p>Almost certainly not. For a family of 3, the WIC income limit is roughly $47,767/year. Even $800/month in plasma income ($9,600/year) added to a part-time job would likely keep you well under the limit. Only families already very close to the ceiling would be at risk.</p>

<h3>Do I have to tell my WIC office about plasma income?</h3>
<p>You should report all income sources honestly during your WIC certification appointments (every 6-12 months). However, WIC does not require interim income reporting between certification periods like some other programs do.</p>

<h3>Is plasma income treated differently than a regular job for WIC?</h3>
<p>For WIC purposes, all gross income is added together regardless of the source. Plasma income is not given special treatment &mdash; it is simply added to your total household gross income. The key difference is that plasma income is modest enough that it rarely makes an eligibility difference.</p>

{footer_related()}'''

    faqs = [
        make_faq("Does WIC count plasma donation money as income?",
                 "WIC may count plasma income as other income when determining eligibility. However, if you qualify through adjunctive eligibility (SNAP, Medicaid, or TANF), income is not checked. For most families, plasma income is too small to affect WIC eligibility."),
        make_faq("Can I donate plasma while receiving WIC?",
                 "Yes. There is no rule preventing WIC recipients from donating plasma. Plasma income of $400-$1,000/month rarely pushes families over WIC's generous 185% FPL income limits."),
        make_faq("Will I lose WIC if I earn $800/month from plasma?",
                 "Almost certainly not. For a family of 3, the WIC income limit is about $47,767/year. Even $800/month plasma income added to a part-time job would keep you well under the limit."),
        make_faq("Do I have to tell my WIC office about plasma income?",
                 "You should report all income honestly during WIC certification appointments every 6-12 months. WIC does not require interim reporting between certifications."),
        make_faq("Is plasma income treated differently than a regular job for WIC?",
                 "No. For WIC purposes, all gross income is totaled regardless of source. Plasma income is simply added to household gross income, but it is modest enough that it rarely affects eligibility."),
    ]

    html = make_en_page(slug, title, meta_desc, category, read_time, toc, content, faqs)
    path = os.path.join(BLOG_DIR, f"{slug}.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  Created: blog/{slug}.html")


# ============================================================
# Page 3: Plasma Donation and TANF/Welfare
# ============================================================
def gen_tanf():
    slug = "plasma-donation-and-tanf-welfare-2026"
    title = "Does Plasma Donation Income Affect TANF/Welfare Benefits? 2026 Guide"
    meta_desc = "Learn how plasma donation income affects TANF welfare benefits in 2026. State-by-state differences, asset limits, reporting rules, and strategies to stay compliant."
    category = "Benefits & Compliance"
    read_time = 11

    toc = [
        ("quick-answer", "Quick Answer"),
        ("tanf-overview", "How TANF Counts Income"),
        ("state-differences", "State-by-State Differences"),
        ("asset-limits", "Asset Limits & Prepaid Cards"),
        ("reporting-rules", "Income Reporting Rules"),
        ("strategies", "Strategies to Stay Compliant"),
        ("faq", "FAQ"),
    ]

    content = f'''
<div class="highlight-box" id="quick-answer">
<h3>Quick Answer</h3>
<p><strong>Plasma donation income's impact on TANF varies significantly by state.</strong> Some states count all "other income" including plasma compensation, while others may exclude small amounts of irregular income. TANF has the <strong>lowest income limits</strong> of any major benefit program, so plasma income of $400-$1,000/month can have a meaningful effect. Additionally, the balance on your plasma center's prepaid debit card may count as an <strong>asset</strong> in states with asset limits. Always check with your local TANF office before starting regular plasma donation.</p>
</div>

<h2 id="tanf-overview">How TANF Counts Income</h2>
<p>Temporary Assistance for Needy Families (TANF) is the primary cash welfare program in the United States. Unlike WIC or SNAP, TANF has extremely strict income thresholds and each state runs its own program with different rules.</p>

<h3>General TANF Income Rules</h3>
<ul>
<li><strong>Gross income test:</strong> Total household income must fall below the state's TANF limit (often 50-75% of FPL)</li>
<li><strong>Net income test:</strong> After allowed deductions, income must still be below payment standard</li>
<li><strong>Earned income disregards:</strong> Most states ignore a portion of earned wages (e.g., first $200 + 50% of remainder)</li>
<li><strong>Unearned income:</strong> Usually counted dollar-for-dollar with fewer disregards</li>
</ul>

<h3>Is Plasma Income "Earned" or "Unearned" for TANF?</h3>
<p>This is where it gets complicated. Different states may classify plasma income differently:</p>
<ul>
<li><strong>"Unearned income"</strong> &mdash; Most states treat it this way, meaning it counts dollar-for-dollar against your benefits with no work-related disregards</li>
<li><strong>"Earned income"</strong> &mdash; A few states may treat it as earned income, allowing you to benefit from earned income disregards</li>
<li><strong>"Irregular income"</strong> &mdash; Some states exclude irregular income below a monthly threshold (often $30-$60/month)</li>
</ul>

{AFFILIATE_BLOCK}

<h2 id="state-differences">State-by-State TANF Differences</h2>
<p>TANF rules vary dramatically by state. Here are key examples showing how plasma income treatment differs:</p>

<table>
<thead><tr><th>State</th><th>TANF Max Benefit (Family of 3)</th><th>Asset Limit</th><th>Likely Plasma Income Treatment</th></tr></thead>
<tbody>
<tr><td>California (CalWORKs)</td><td>$963/mo</td><td>$11,231</td><td>Counted as unearned income</td></tr>
<tr><td>Texas</td><td>$308/mo</td><td>$2,000</td><td>Counted as unearned income; low asset limit</td></tr>
<tr><td>New York</td><td>$789/mo</td><td>$2,000</td><td>Counted as other income; may have small disregard</td></tr>
<tr><td>Florida</td><td>$303/mo</td><td>$2,000</td><td>All income counted; very strict</td></tr>
<tr><td>Ohio</td><td>$540/mo</td><td>No limit</td><td>Counted as unearned income; no asset test</td></tr>
<tr><td>Pennsylvania</td><td>$503/mo</td><td>No limit</td><td>Counted as unearned income; no asset test</td></tr>
<tr><td>Illinois</td><td>$532/mo</td><td>No limit</td><td>Counted as unearned income</td></tr>
<tr><td>Georgia</td><td>$280/mo</td><td>$1,000</td><td>All income counted; very low asset limit</td></tr>
<tr><td>Michigan</td><td>$492/mo</td><td>$3,000</td><td>Counted as unearned income</td></tr>
<tr><td>Arizona</td><td>$278/mo</td><td>$2,000</td><td>Counted as unearned income</td></tr>
</tbody>
</table>

<p><em>Note: These figures are approximate for 2026. State rules change frequently. Always verify with your local TANF office.</em></p>

<h3>Impact Example</h3>
<p>In Texas, a family of 3 receives a maximum of $308/month in TANF cash. If plasma income of $600/month is counted as unearned income, it could <strong>completely eliminate the TANF cash benefit</strong> since $600 exceeds the TANF payment standard. However, the family may still receive associated Medicaid and SNAP benefits.</p>

<h2 id="asset-limits">Asset Limits and Prepaid Debit Cards</h2>
<p>Many states impose <strong>asset limits</strong> for TANF eligibility. This is where plasma donation creates an often-overlooked issue:</p>

<h3>The Prepaid Card Problem</h3>
<p>Plasma centers pay via prepaid debit cards. The <strong>balance on that card counts as a countable asset</strong> in most states with asset limits. Here is how it works:</p>

<table>
<thead><tr><th>Scenario</th><th>Prepaid Card Balance</th><th>Other Assets</th><th>Total</th><th>Risk (if $2,000 limit)</th></tr></thead>
<tbody>
<tr><td>Spend immediately</td><td>$0-$50</td><td>$500</td><td>$500-$550</td><td>Safe</td></tr>
<tr><td>Save for 2 weeks</td><td>$200-$400</td><td>$500</td><td>$700-$900</td><td>Safe</td></tr>
<tr><td>Save for a month</td><td>$400-$1,000</td><td>$500</td><td>$900-$1,500</td><td>Getting close</td></tr>
<tr><td>Save for 2+ months</td><td>$800-$2,000</td><td>$500</td><td>$1,300-$2,500</td><td>May exceed limit</td></tr>
</tbody>
</table>

<h3>States Without Asset Limits (2026)</h3>
<p>The following states have eliminated asset tests for TANF, meaning your prepaid card balance does not matter:</p>
<ul>
<li>Alabama, California, Colorado, Connecticut, Delaware, Hawaii, Illinois, Iowa, Louisiana, Maine, Maryland, Massachusetts, Minnesota, Mississippi, Missouri, Nebraska, New Jersey, New Mexico, North Carolina, North Dakota, Ohio, Oregon, Pennsylvania, Vermont, Virginia, Washington, West Virginia, Wisconsin, Wyoming</li>
</ul>

{PRO_TOOLKIT}

<h2 id="reporting-rules">Income Reporting Rules for TANF</h2>
<p>TANF programs typically require more frequent income reporting than other benefit programs:</p>

<h3>Common Reporting Requirements</h3>
<ul>
<li><strong>Monthly reporting:</strong> Many states require monthly income reports (SAR or QR forms)</li>
<li><strong>Change reporting:</strong> Most states require you to report income changes within 10-30 days</li>
<li><strong>Periodic review:</strong> Full eligibility reviews every 6-12 months</li>
</ul>

<h3>What Happens If You Don't Report?</h3>
<ul>
<li><strong>Overpayment recovery:</strong> You may be required to repay benefits received while earning unreported income</li>
<li><strong>Disqualification:</strong> Intentional non-reporting can result in 6-12 month disqualification</li>
<li><strong>Fraud prosecution:</strong> In extreme cases, welfare fraud carries criminal penalties</li>
</ul>

<h2 id="strategies">Strategies to Stay Compliant While Donating</h2>
<ol>
<li><strong>Ask your caseworker first:</strong> Before starting regular plasma donation, ask your TANF caseworker how plasma income will be classified in your state</li>
<li><strong>Calculate the net effect:</strong> If plasma income reduces your TANF check, calculate whether you come out ahead (you usually will &mdash; plasma income often exceeds the lost TANF amount)</li>
<li><strong>Watch your asset balance:</strong> If your state has an asset limit, transfer funds from your prepaid card regularly rather than accumulating a large balance</li>
<li><strong>Keep detailed records:</strong> Document every donation date, amount, and center for your caseworker</li>
<li><strong>Report on time:</strong> Submit required monthly/change reports with plasma income included</li>
<li><strong>Consider the full picture:</strong> Remember that TANF cash is just one benefit &mdash; check whether plasma income affects your Medicaid, SNAP, or childcare subsidies too</li>
</ol>

<div style="background: #fef3c7; border-left: 4px solid #f59e0b; padding: 1rem 1.5rem; border-radius: 8px; margin: 1.5rem 0;">
<p style="margin: 0; font-weight: 600; color: #92400e;">Disclaimer</p>
<p style="margin: 0.5rem 0 0; color: #78350f;">This article is for informational purposes only and does not constitute legal or financial advice. TANF rules vary significantly by state and change frequently. Always consult your local TANF/welfare office or a benefits counselor for guidance specific to your situation.</p>
</div>

{related_reading([
    ("/blog/plasma-donation-and-section-8-housing-2026.html", "Plasma Donation & Section 8 Housing"),
    ("/blog/plasma-donation-and-wic-benefits-2026.html", "Does Plasma Donation Affect WIC Benefits?"),
    ("/blog/plasma-donation-1099-tax-form-explained-2026.html", "Plasma Donation 1099 Tax Form Explained"),
    ("/blog/plasma-donation-taxes-2026.html", "Complete Plasma Donation Tax Guide 2026"),
])}

<h2 id="faq">Frequently Asked Questions</h2>

<h3>Does plasma income count against TANF benefits?</h3>
<p>In most states, yes. Plasma income is typically classified as "unearned income" and counted dollar-for-dollar against your TANF benefit. However, some states have small disregards for irregular income, and a few may treat it as earned income with applicable disregards. Check with your local TANF office.</p>

<h3>Will I lose my TANF if I donate plasma regularly?</h3>
<p>It depends on your state and how much you earn. In states with very low TANF payments ($278-$308/month for a family of 3), plasma income of $400+/month could reduce or eliminate the cash benefit. However, you would likely come out ahead financially since plasma income exceeds the lost TANF amount. Associated benefits like Medicaid and SNAP may be affected differently.</p>

<h3>Does my plasma center prepaid card balance count as an asset for TANF?</h3>
<p>In states with asset limits, yes &mdash; the balance on your prepaid debit card is typically a countable asset. To avoid issues, transfer funds regularly rather than letting a large balance accumulate. Many states (about 29) have eliminated asset tests entirely.</p>

<h3>Do I need to report each plasma donation to TANF?</h3>
<p>You generally do not need to report each individual donation, but you must include plasma income on your monthly income reports or report it as a change in income within your state's required timeframe (usually 10-30 days). Report the total monthly amount rather than each individual payment.</p>

<h3>Is it worth donating plasma if it reduces my TANF?</h3>
<p>In most cases, yes. Even if TANF cash is reduced or eliminated, plasma income of $400-$1,000/month typically exceeds the TANF benefit amount. For example, losing $308/month in TANF but gaining $600/month in plasma income is a net gain of $292/month. However, consider the impact on all your benefits (Medicaid, SNAP, childcare) before deciding.</p>

{footer_related()}'''

    faqs = [
        make_faq("Does plasma income count against TANF benefits?",
                 "In most states, yes. Plasma income is typically classified as unearned income and counted dollar-for-dollar against your TANF benefit. Some states have small disregards for irregular income. Check with your local TANF office."),
        make_faq("Will I lose my TANF if I donate plasma regularly?",
                 "It depends on your state and earnings. In states with low TANF payments, plasma income could reduce or eliminate the cash benefit, but you would likely come out ahead financially since plasma income typically exceeds the lost TANF amount."),
        make_faq("Does my plasma center prepaid card balance count as an asset for TANF?",
                 "In states with asset limits, yes. The prepaid debit card balance is typically a countable asset. Transfer funds regularly to avoid accumulating a balance that exceeds limits. About 29 states have eliminated asset tests."),
        make_faq("Do I need to report each plasma donation to TANF?",
                 "You do not need to report each individual donation, but must include total plasma income on monthly income reports or report it as a change in income within your state's required timeframe."),
        make_faq("Is it worth donating plasma if it reduces my TANF?",
                 "In most cases, yes. Even if TANF is reduced, plasma income of $400-$1,000/month typically exceeds the TANF benefit. For example, losing $308/month TANF but gaining $600/month plasma income is a net gain of $292/month."),
    ]

    html = make_en_page(slug, title, meta_desc, category, read_time, toc, content, faqs)
    path = os.path.join(BLOG_DIR, f"{slug}.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  Created: blog/{slug}.html")


# ============================================================
# Page 4: Plasma Donation 1099 Tax Form Explained
# ============================================================
def gen_1099():
    slug = "plasma-donation-1099-tax-form-explained-2026"
    title = "Plasma Donation 1099 Tax Form: Do You Get One & How to File (2026)"
    meta_desc = "Learn about plasma donation 1099-NEC tax forms in 2026. When centers issue them, how to report plasma income on your tax return, and why plasma is NOT self-employment income."
    category = "Tax Guide"
    read_time = 12

    toc = [
        ("quick-answer", "Quick Answer"),
        ("1099-nec-basics", "1099-NEC Basics"),
        ("when-issued", "When You Get a 1099"),
        ("multi-center", "Multi-Center Strategy"),
        ("how-to-report", "How to Report on Your Tax Return"),
        ("not-self-employment", "Why It's NOT Self-Employment"),
        ("tax-walkthrough", "Tax Form Walkthrough"),
        ("faq", "FAQ"),
    ]

    content = f'''
<div class="highlight-box" id="quick-answer">
<h3>Quick Answer</h3>
<p><strong>Plasma centers issue a 1099-NEC (not 1099-MISC) if you earn $600 or more from a single center in a calendar year.</strong> Even if you earn less than $600 and do NOT receive a 1099, you are still legally required to report the income on your tax return. Plasma income is reported on <strong>Schedule 1, Line 8z</strong> as "Other Income" and is <strong>NOT subject to self-employment tax</strong> &mdash; saving you 15.3% compared to gig work or freelancing.</p>
</div>

<h2 id="1099-nec-basics">Understanding the 1099-NEC for Plasma Donation</h2>
<p>Since 2020, non-employee compensation is reported on Form <strong>1099-NEC</strong> (Nonemployee Compensation), not the older 1099-MISC. Here is what you need to know:</p>

<h3>Key Facts About the 1099-NEC</h3>
<ul>
<li><strong>Form type:</strong> 1099-NEC (replaced 1099-MISC Box 7 for nonemployee compensation)</li>
<li><strong>Threshold:</strong> Centers must issue one if they paid you <strong>$600 or more</strong> during the tax year</li>
<li><strong>Mailing deadline:</strong> Centers must send it by <strong>January 31</strong> for the prior tax year</li>
<li><strong>Your copy:</strong> You receive Copy B for your records</li>
<li><strong>IRS copy:</strong> The center also files a copy with the IRS (they know about it)</li>
</ul>

<h3>What the 1099-NEC Looks Like</h3>
<table>
<thead><tr><th>Box</th><th>Description</th><th>Your Plasma Example</th></tr></thead>
<tbody>
<tr><td>Payer Name</td><td>The plasma center's legal name</td><td>e.g., "CSL Plasma Inc."</td></tr>
<tr><td>Payer TIN</td><td>Center's tax ID number</td><td>XX-XXXXXXX</td></tr>
<tr><td>Recipient Name</td><td>Your legal name</td><td>Your name</td></tr>
<tr><td>Recipient TIN</td><td>Your SSN (partially masked)</td><td>XXX-XX-1234</td></tr>
<tr><td><strong>Box 1</strong></td><td><strong>Nonemployee Compensation</strong></td><td><strong>$2,400.00</strong> (example)</td></tr>
<tr><td>Box 4</td><td>Federal tax withheld</td><td>Usually $0 (no withholding)</td></tr>
</tbody>
</table>

{AFFILIATE_BLOCK}

<h2 id="when-issued">When Do You Get a 1099 from a Plasma Center?</h2>

<h3>You WILL Receive a 1099-NEC If:</h3>
<ul>
<li>You earned <strong>$600 or more</strong> from a single plasma center in one calendar year</li>
<li>Donating twice weekly at $50-$75/visit, you will hit $600 in about <strong>4-6 weeks</strong></li>
<li>Most regular donors will receive a 1099-NEC from every center they visit</li>
</ul>

<h3>You Will NOT Receive a 1099-NEC If:</h3>
<ul>
<li>You earned <strong>less than $600</strong> from a particular center in one year</li>
<li>You donated only a few times before stopping</li>
<li>You split time between multiple centers, earning under $600 at each</li>
</ul>

<h3>Important: No 1099 Does NOT Mean No Tax</h3>
<p><strong>You must report ALL plasma income on your tax return, even without a 1099.</strong> The $600 threshold only determines whether the center must issue a form &mdash; it has nothing to do with whether the income is taxable. All plasma income is taxable regardless of amount.</p>

<h2 id="multi-center">The Multi-Center Strategy &mdash; Tax Implications</h2>
<p>Some donors split donations between multiple centers to take advantage of new donor bonuses. Here is how this affects your 1099 situation:</p>

<table>
<thead><tr><th>Strategy</th><th>1099s Received</th><th>Tax Reporting</th></tr></thead>
<tbody>
<tr><td>One center all year ($4,800)</td><td>1 form (showing $4,800)</td><td>Report $4,800 on Schedule 1</td></tr>
<tr><td>Two centers ($2,400 each)</td><td>2 forms ($2,400 each)</td><td>Report $4,800 total on Schedule 1</td></tr>
<tr><td>Two centers ($500 each)</td><td>0 forms (under $600 each)</td><td>Still report $1,000 on Schedule 1</td></tr>
<tr><td>Four centers ($500 each)</td><td>0 forms (under $600 each)</td><td>Still report $2,000 on Schedule 1</td></tr>
</tbody>
</table>

<p><strong>Bottom line:</strong> Splitting centers does NOT reduce your tax obligation. The IRS expects you to report all income regardless of whether you receive a 1099. Deliberately splitting centers to avoid 1099s is not a legitimate tax strategy and could trigger an audit if the IRS receives conflicting information.</p>

{PRO_TOOLKIT}

<h2 id="how-to-report">How to Report Plasma Income on Your Tax Return</h2>
<p>Plasma donation income is reported as <strong>"Other Income"</strong> on your federal tax return. Here is the path:</p>

<h3>Tax Form Sequence</h3>
<ol>
<li><strong>Form 1040</strong> (your main return) &rarr; Line 8 references Schedule 1</li>
<li><strong>Schedule 1</strong> (Additional Income and Adjustments) &rarr; <strong>Part I, Line 8z</strong> (Other Income)</li>
<li>Write <strong>"Plasma donation income"</strong> as the description</li>
<li>Enter the total amount from all centers combined</li>
<li>This amount flows back to Form 1040, Line 8</li>
</ol>

<h3>What About State Taxes?</h3>
<p>Most states follow the federal treatment &mdash; plasma income is taxable on your state return as well. States with no income tax (Texas, Florida, Nevada, Washington, etc.) do not apply. For other states, the income flows through to your state return automatically when you report it on your federal return.</p>

<h2 id="not-self-employment">Why Plasma Income is NOT Self-Employment Income</h2>
<p>This is one of the most important tax distinctions for plasma donors. Plasma compensation is <strong>not self-employment income</strong>, which saves you a significant amount of money.</p>

<h3>The Key Difference</h3>
<table>
<thead><tr><th>Feature</th><th>Self-Employment Income (Schedule C)</th><th>Plasma "Other Income" (Schedule 1)</th></tr></thead>
<tbody>
<tr><td>Tax form</td><td>Schedule C + Schedule SE</td><td>Schedule 1, Line 8z only</td></tr>
<tr><td>Self-employment tax (15.3%)</td><td>YES &mdash; you pay it</td><td><strong>NO &mdash; you do NOT pay it</strong></td></tr>
<tr><td>Federal income tax</td><td>Yes, at your bracket rate</td><td>Yes, at your bracket rate</td></tr>
<tr><td>Deduct expenses</td><td>Yes (mileage, etc.)</td><td>No (no Schedule C)</td></tr>
<tr><td>Example: $5,000 income at 12% bracket</td><td>$600 income tax + $765 SE tax = <strong>$1,365</strong></td><td>$600 income tax + $0 SE tax = <strong>$600</strong></td></tr>
</tbody>
</table>

<p><strong>You save $765 on $5,000 of plasma income</strong> by correctly reporting it as Other Income instead of self-employment. The IRS has clarified that selling bodily fluids/tissue is not a "trade or business" &mdash; it is compensation for a personal activity.</p>

<h3>What About Mileage Deductions?</h3>
<p>Since plasma income is not reported on Schedule C, you cannot deduct mileage, travel, or other expenses against it. However, the self-employment tax savings (15.3%) almost always far outweigh any potential mileage deduction. For most donors, the math strongly favors the "Other Income" classification.</p>

<h2 id="tax-walkthrough">Sample Tax Form Walkthrough</h2>
<p>Here is a step-by-step example for a donor who earned $4,800 from plasma in 2025 (filing in early 2026):</p>

<h3>Step 1: Gather Your Documents</h3>
<ul>
<li>1099-NEC from CSL Plasma showing $4,800 in Box 1</li>
<li>Any other W-2s or income documents</li>
</ul>

<h3>Step 2: Complete Schedule 1, Part I</h3>
<table>
<thead><tr><th>Line</th><th>Description</th><th>Amount</th></tr></thead>
<tbody>
<tr><td>Line 8z</td><td>Other income &mdash; type: <em>Plasma donation income</em></td><td>$4,800</td></tr>
<tr><td>Line 10</td><td>Total other income (sum of 8a-8z)</td><td>$4,800</td></tr>
</tbody>
</table>

<h3>Step 3: Transfer to Form 1040</h3>
<table>
<thead><tr><th>Line</th><th>Description</th><th>Amount</th></tr></thead>
<tbody>
<tr><td>Line 8</td><td>Other income (from Schedule 1, line 10)</td><td>$4,800</td></tr>
<tr><td>Line 9</td><td>Total income (wages + other income)</td><td>Your total</td></tr>
</tbody>
</table>

<h3>Step 4: Calculate Your Tax</h3>
<p>At the <strong>12% tax bracket</strong>, your federal tax on $4,800 of plasma income is approximately <strong>$576</strong>. If you were in the 10% bracket, it would be $480. Remember: no self-employment tax applies.</p>

<h3>Using Tax Software</h3>
<p>In TurboTax, H&R Block, or FreeTaxUSA:</p>
<ol>
<li>Navigate to <strong>"Other Income"</strong> or <strong>"1099-NEC"</strong> section</li>
<li>Enter the 1099-NEC information</li>
<li>When asked if this is self-employment income, select <strong>"No"</strong></li>
<li>The software will route it to Schedule 1, Line 8z automatically</li>
</ol>

<div style="background: #fef3c7; border-left: 4px solid #f59e0b; padding: 1rem 1.5rem; border-radius: 8px; margin: 1.5rem 0;">
<p style="margin: 0; font-weight: 600; color: #92400e;">Tax Disclaimer</p>
<p style="margin: 0.5rem 0 0; color: #78350f;">This article is for informational purposes only and does not constitute tax advice. Tax laws are subject to change, and individual circumstances vary. Consult a qualified tax professional or CPA for advice specific to your situation.</p>
</div>

{related_reading([
    ("/blog/plasma-donation-taxes-2026.html", "Complete Plasma Donation Tax Guide 2026"),
    ("/blog/plasma-donation-and-section-8-housing-2026.html", "Plasma Donation & Section 8 Housing"),
    ("/blog/plasma-donation-and-tanf-welfare-2026.html", "Plasma Donation & TANF/Welfare Benefits"),
    ("/blog/plasma-donation-and-wic-benefits-2026.html", "Does Plasma Donation Affect WIC Benefits?"),
])}

<h2 id="faq">Frequently Asked Questions</h2>

<h3>Do plasma centers send you a 1099?</h3>
<p>Yes, if you earn $600 or more from a single center in one calendar year, they are required to send you a 1099-NEC by January 31. If you earn less than $600 at a center, they are not required to send one, but the income is still taxable.</p>

<h3>Is a 1099-NEC or 1099-MISC used for plasma income?</h3>
<p>Since 2020, plasma centers use the <strong>1099-NEC</strong> (Nonemployee Compensation), not the 1099-MISC. If you receive a 1099-MISC for plasma income, contact the center to request a corrected form.</p>

<h3>Do I have to pay self-employment tax on plasma income?</h3>
<p>No. Plasma donation income is classified as "Other Income" and reported on Schedule 1, Line 8z. It is NOT self-employment income, so you do NOT pay the 15.3% self-employment tax (Social Security + Medicare). This saves you approximately $765 per $5,000 earned.</p>

<h3>What if I donated at multiple centers and got multiple 1099s?</h3>
<p>Add up the amounts from all 1099-NEC forms and report the total on Schedule 1, Line 8z as a single "Plasma donation income" entry. You do not need to list each center separately on your return, though you should keep all 1099s for your records.</p>

<h3>What happens if I don't report plasma income?</h3>
<p>If a center issued a 1099-NEC to the IRS and you don't report the income, the IRS will likely send you a CP2000 notice proposing additional tax. They may also classify it as self-employment income (which costs more in taxes) and add penalties and interest. Always report all plasma income, even without a 1099.</p>

{footer_related()}'''

    faqs = [
        make_faq("Do plasma centers send you a 1099?",
                 "Yes, if you earn $600 or more from a single center in one calendar year, they send a 1099-NEC by January 31. Income under $600 is still taxable even without a form."),
        make_faq("Is a 1099-NEC or 1099-MISC used for plasma income?",
                 "Since 2020, plasma centers use the 1099-NEC (Nonemployee Compensation). If you receive a 1099-MISC for plasma income, contact the center for a corrected form."),
        make_faq("Do I have to pay self-employment tax on plasma income?",
                 "No. Plasma income is Other Income reported on Schedule 1, Line 8z. It is NOT self-employment income, so you do not pay the 15.3% self-employment tax, saving approximately $765 per $5,000 earned."),
        make_faq("What if I donated at multiple centers and got multiple 1099s?",
                 "Add up all 1099-NEC amounts and report the total on Schedule 1, Line 8z as Plasma donation income. Keep all 1099s for your records."),
        make_faq("What happens if I don't report plasma income?",
                 "The IRS will likely send a CP2000 notice if they received a 1099-NEC. They may classify it as self-employment income, adding SE tax, penalties, and interest. Always report all plasma income."),
    ]

    html = make_en_page(slug, title, meta_desc, category, read_time, toc, content, faqs)
    path = os.path.join(BLOG_DIR, f"{slug}.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  Created: blog/{slug}.html")


# ============================================================
# Main
# ============================================================
if __name__ == "__main__":
    print("Generating Round 3 Financial/Benefits Pages (4 pages)...")
    gen_section_8()
    gen_wic()
    gen_tanf()
    gen_1099()
    print("Done! Generated 4 financial/benefits pages.")
