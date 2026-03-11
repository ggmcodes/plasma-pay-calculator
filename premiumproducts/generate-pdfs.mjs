import puppeteer from 'puppeteer';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const OUT = path.join(__dirname, 'pdfs');

const STYLE = `
  body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; color: #1e293b; line-height: 1.6; padding: 40px; max-width: 800px; margin: 0 auto; }
  h1 { color: #0d9488; font-size: 28px; margin-bottom: 4px; border-bottom: 3px solid #0d9488; padding-bottom: 10px; }
  h2 { color: #0d9488; font-size: 20px; margin-top: 28px; }
  h3 { color: #f97316; font-size: 16px; margin-top: 20px; }
  .brand { color: #64748b; font-size: 12px; margin-bottom: 20px; }
  table { width: 100%; border-collapse: collapse; margin: 14px 0; font-size: 13px; }
  th { background: #0d9488; color: white; padding: 8px 10px; text-align: left; font-size: 12px; }
  td { padding: 7px 10px; border-bottom: 1px solid #e2e8f0; }
  tr:nth-child(even) td { background: #f0fdfa; }
  ul, ol { padding-left: 22px; }
  li { margin-bottom: 6px; font-size: 14px; }
  .tip { background: #fefce8; border-left: 4px solid #f97316; padding: 12px 16px; margin: 16px 0; border-radius: 0 8px 8px 0; }
  .tip strong { color: #f97316; }
  .check { color: #0d9488; font-weight: bold; }
  .footer { margin-top: 40px; padding-top: 16px; border-top: 2px solid #e2e8f0; font-size: 11px; color: #94a3b8; text-align: center; }
  p { font-size: 14px; }
`;

const pdfs = [
  {
    name: '90-Day-Earning-Playbook',
    html: `<h1>Your First 90 Days: The $2,000+ Roadmap</h1>
<div class="brand">Plasma Pay Calculator &mdash; plasmapaycalculator.com</div>
<h2>Week 0: Prep Week (Before Your First Visit)</h2>
<ul>
<li><strong>Research centers</strong> within 30 miles &mdash; compare BioLife, CSL, Grifols, Octapharma</li>
<li><strong>Check new donor bonuses</strong> &mdash; most offer $700-$1,000 for first month</li>
<li><strong>Get your documents ready:</strong> Valid photo ID, proof of address, Social Security card</li>
<li><strong>Hydrate aggressively</strong> for 3 days before &mdash; 80+ oz water daily</li>
<li><strong>Eat iron-rich foods</strong> &mdash; red meat, spinach, beans, fortified cereal</li>
<li><strong>Download the center's app</strong> &mdash; BioLife, CSL, etc. for scheduling</li>
</ul>

<h2>Ideal Weekly Donation Schedule</h2>
<table>
<tr><th>Day</th><th>Activity</th><th>Expected Pay</th></tr>
<tr><td>Monday</td><td>Donation #1</td><td>$50-75</td></tr>
<tr><td>Tuesday</td><td>Recovery Day</td><td>&mdash;</td></tr>
<tr><td>Wednesday</td><td>Recovery / Hydrate</td><td>&mdash;</td></tr>
<tr><td>Thursday</td><td>Donation #2</td><td>$50-75</td></tr>
<tr><td>Friday-Sunday</td><td>Recovery &amp; Meal Prep</td><td>&mdash;</td></tr>
</table>

<h2>Week-by-Week Plan</h2>
<h3>Weeks 1-2: Foundation ($200-400)</h3>
<ul>
<li>Complete first 4 donations at your primary center</li>
<li>Start tracking every visit in the Donation Tracker spreadsheet</li>
<li>Note wait times, staff quality, overall experience</li>
<li>Take the new donor bonus &mdash; typically highest payout</li>
</ul>

<h3>Weeks 3-4: Optimize ($400-700 cumulative)</h3>
<ul>
<li>Dial in your pre-donation routine (hydration, iron, protein)</li>
<li>Visit a 2nd center for their new donor bonus</li>
<li>Start tracking mileage for tax deductions</li>
<li>Ask about referral bonuses &mdash; bring a friend for $50-100 bonus</li>
</ul>

<h3>Weeks 5-8: Scale ($800-1,400 cumulative)</h3>
<ul>
<li>Lock in a consistent schedule at your highest-paying center</li>
<li>Stack loyalty bonuses on top of base pay</li>
<li>Check the Center Pay Rate Bible for better rates nearby</li>
<li>Optimize for weight tier (higher weight = higher pay)</li>
</ul>

<h3>Weeks 9-12: Maximize ($1,400-2,000+ cumulative)</h3>
<ul>
<li>You're now a regular &mdash; faster process, shorter waits</li>
<li>Stack monthly bonuses + referral bonuses</li>
<li>File quarterly estimated taxes with your tax deductions</li>
<li>Consider rotating centers for overlapping promotions</li>
</ul>

<div class="tip"><strong>Pro Tip:</strong> New donor bonuses are the single biggest income boost. Some donors visit 3-4 different centers in their first 90 days, stacking $2,000-3,000 in bonuses alone.</div>

<h2>What to Bring Every Visit</h2>
<ul>
<li>Photo ID (must match center records)</li>
<li>Water bottle (32 oz minimum)</li>
<li>High-protein snack for after</li>
<li>Phone with charger or headphones</li>
<li>Warm layers (donation rooms are cold)</li>
<li>Stress ball (helps speed up donation)</li>
</ul>
<div class="footer">PlasmaPayCalculator.com &mdash; Plasma Donor Pro Toolkit</div>`
  },
  {
    name: 'Bonus-Stacking-Strategy',
    html: `<h1>Bonus Stacking Cheat Sheet</h1>
<div class="brand">Plasma Pay Calculator &mdash; plasmapaycalculator.com</div>
<h2>New Donor Bonus Comparison (2026)</h2>
<table>
<tr><th>Center</th><th>Bonus Amount</th><th>Requirement</th><th>Timeframe</th></tr>
<tr><td>BioLife</td><td>$800-900</td><td>8 donations</td><td>45 days</td></tr>
<tr><td>CSL Plasma</td><td>$900-1,100</td><td>10 donations</td><td>60 days</td></tr>
<tr><td>Grifols / Biomat</td><td>$700-800</td><td>6-8 donations</td><td>30 days</td></tr>
<tr><td>Octapharma</td><td>$600-750</td><td>6 donations</td><td>30 days</td></tr>
<tr><td>KEDPLASMA</td><td>$500-700</td><td>8 donations</td><td>45 days</td></tr>
</table>

<h2>The Bonus Stacking Strategy</h2>
<ol>
<li><strong>Start at the center with the HIGHEST new donor bonus</strong> (usually CSL at $900-1,100)</li>
<li><strong>Complete their required donations</strong> within the deadline</li>
<li><strong>Immediately switch to Center #2</strong> for their new donor bonus</li>
<li><strong>While donating, refer friends</strong> for referral bonuses ($50-100 each)</li>
<li><strong>After exhausting new donor bonuses, settle at the highest-paying center</strong> for regular donations</li>
</ol>

<h2>Optimal Stacking Order by Region</h2>
<h3>If you have CSL + BioLife nearby:</h3>
<ol>
<li>CSL Plasma first ($1,000 in 60 days)</li>
<li>BioLife second ($900 in 45 days)</li>
<li>Settle at whichever pays more regularly</li>
<li><strong>Total: $1,900+ in first 3 months</strong></li>
</ol>

<h3>If you have Grifols + Octapharma nearby:</h3>
<ol>
<li>Grifols first ($800 in 30 days)</li>
<li>Octapharma second ($700 in 30 days)</li>
<li>Settle at the better-paying center</li>
<li><strong>Total: $1,500+ in first 2 months</strong></li>
</ol>

<h2>Referral Bonus Programs</h2>
<table>
<tr><th>Center</th><th>You Earn</th><th>Friend Earns</th><th>Requirement</th></tr>
<tr><td>BioLife</td><td>$50-100</td><td>$50</td><td>Friend completes 2 donations</td></tr>
<tr><td>CSL Plasma</td><td>$50-75</td><td>$50</td><td>Friend completes 1 donation</td></tr>
<tr><td>Grifols</td><td>$25-50</td><td>$25</td><td>Friend completes 2 donations</td></tr>
<tr><td>Octapharma</td><td>$50</td><td>$50</td><td>Friend completes 1 donation</td></tr>
</table>

<div class="tip"><strong>Pro Tip:</strong> Some centers let you refer unlimited friends. If you refer 5 people at CSL ($75 each), that's an extra $375 on top of your donation income.</div>

<h2>Monthly Loyalty Bonuses</h2>
<ul>
<li><strong>BioLife:</strong> Bonus for 8 donations/month ($20-50 extra)</li>
<li><strong>CSL:</strong> Tiered loyalty rewards &mdash; donate more, earn more per visit</li>
<li><strong>Grifols:</strong> Loyalty points system for gift cards and bonuses</li>
</ul>
<div class="footer">PlasmaPayCalculator.com &mdash; Plasma Donor Pro Toolkit</div>`
  },
  {
    name: 'Nutrition-Plan',
    html: `<h1>Pre & Post Donation Nutrition Plan</h1>
<div class="brand">Plasma Pay Calculator &mdash; plasmapaycalculator.com</div>
<h2>24 Hours Before Donating</h2>
<ul>
<li><strong>Drink 80+ oz of water</strong> &mdash; hydration is the #1 factor for fast donations</li>
<li><strong>Eat 60-80g protein</strong> &mdash; chicken, eggs, fish, beans, or protein shake</li>
<li><strong>Iron-rich dinner:</strong> Red meat or spinach + vitamin C (helps iron absorption)</li>
<li><strong>Avoid:</strong> Alcohol, fatty foods, excessive caffeine, high-sodium meals</li>
<li><strong>Avoid:</strong> NSAIDs (ibuprofen, aspirin) &mdash; can affect platelet function</li>
</ul>

<h2>Morning of Donation</h2>
<ul>
<li><strong>16-20 oz water</strong> first thing when you wake up</li>
<li><strong>High-protein breakfast:</strong> Eggs + toast, oatmeal + peanut butter, Greek yogurt</li>
<li><strong>Iron supplement</strong> with vitamin C (orange juice) if you tend to have low levels</li>
<li><strong>Light cardio</strong> (10-min walk) to get blood flowing</li>
<li><strong>Another 16 oz water</strong> 30 minutes before your appointment</li>
</ul>

<h2>Post-Donation Recovery</h2>
<ul>
<li><strong>Drink 32+ oz water</strong> in the first 2 hours after donating</li>
<li><strong>Eat within 30 minutes:</strong> Protein bar, sandwich, or the center's free snacks</li>
<li><strong>Recovery meal:</strong> Chicken, rice, vegetables &mdash; balanced protein + carbs</li>
<li><strong>Rest:</strong> No heavy lifting or intense exercise for 4-6 hours</li>
<li><strong>Take iron supplement</strong> with dinner (vitamin C helps absorption)</li>
</ul>

<h2>Weekly Meal Prep Template (Donation Days)</h2>
<table>
<tr><th>Meal</th><th>Option A</th><th>Option B</th><th>Option C</th></tr>
<tr><td>Breakfast</td><td>3 eggs + toast + OJ</td><td>Greek yogurt + granola + berries</td><td>Oatmeal + PB + banana</td></tr>
<tr><td>Pre-Donation Snack</td><td>Protein bar + water</td><td>Trail mix + water</td><td>Apple + PB + water</td></tr>
<tr><td>Post-Donation</td><td>Chicken sandwich</td><td>Turkey wrap + fruit</td><td>Protein shake + crackers</td></tr>
<tr><td>Dinner</td><td>Steak + spinach + rice</td><td>Salmon + broccoli + quinoa</td><td>Bean chili + cornbread</td></tr>
</table>

<h2>Top Iron-Rich Foods</h2>
<table>
<tr><th>Food</th><th>Iron (mg per serving)</th><th>Tips</th></tr>
<tr><td>Beef liver (3 oz)</td><td>5.2 mg</td><td>Highest iron food</td></tr>
<tr><td>Ground beef (3 oz)</td><td>2.2 mg</td><td>Easy to meal prep</td></tr>
<tr><td>Spinach (1 cup cooked)</td><td>6.4 mg</td><td>Pair with vitamin C</td></tr>
<tr><td>Fortified cereal</td><td>18 mg</td><td>Easy breakfast option</td></tr>
<tr><td>Lentils (1 cup)</td><td>6.6 mg</td><td>Great for vegetarians</td></tr>
<tr><td>Kidney beans (1 cup)</td><td>3.9 mg</td><td>Add to chili or salads</td></tr>
<tr><td>Dark chocolate (1 oz)</td><td>3.4 mg</td><td>Healthy snack option</td></tr>
</table>

<div class="tip"><strong>Pro Tip:</strong> The #1 reason donors get deferred is low hematocrit/iron levels. Consistent hydration and iron-rich meals prevent 90% of deferrals.</div>
<div class="footer">PlasmaPayCalculator.com &mdash; Plasma Donor Pro Toolkit</div>`
  },
  {
    name: 'Tax-Guide-2026',
    html: `<h1>The Complete Plasma Donation Tax Guide 2026</h1>
<div class="brand">Plasma Pay Calculator &mdash; plasmapaycalculator.com</div>
<h2>How Plasma Income Is Taxed</h2>
<p>Plasma donation income is <strong>taxable income</strong> reported on your federal return. While you may not receive a 1099, you are legally required to report all plasma earnings.</p>
<ul>
<li><strong>Self-employment income</strong> &mdash; reported on Schedule C</li>
<li><strong>Subject to self-employment tax</strong> (15.3% for Social Security + Medicare)</li>
<li><strong>Subject to federal income tax</strong> at your bracket rate</li>
<li><strong>Subject to state income tax</strong> (varies by state, 0-13%)</li>
</ul>
<div class="tip"><strong>Key Insight:</strong> The good news is you can deduct mileage, supplies, and other expenses to significantly reduce what you owe.</div>

<h2>Reporting Step-by-Step</h2>
<ol>
<li>Track all plasma income throughout the year (use the Donation Tracker spreadsheet)</li>
<li>Track all deductions (mileage, supplies, etc.)</li>
<li>File Schedule C (Profit or Loss from Business) with your 1040</li>
<li>File Schedule SE (Self-Employment Tax)</li>
<li>Pay quarterly estimated taxes if you owe $1,000+ for the year</li>
</ol>

<h2>Tax Bracket Quick Reference (2026)</h2>
<table>
<tr><th>Taxable Income (Single)</th><th>Rate</th><th>Plasma Income Example</th></tr>
<tr><td>$0 - $11,925</td><td>10%</td><td>$3,000 plasma = $300 federal tax</td></tr>
<tr><td>$11,926 - $48,475</td><td>12%</td><td>$3,000 plasma = $360 federal tax</td></tr>
<tr><td>$48,476 - $103,350</td><td>22%</td><td>$3,000 plasma = $660 federal tax</td></tr>
<tr><td>$103,351 - $197,300</td><td>24%</td><td>$3,000 plasma = $720 federal tax</td></tr>
</table>

<h2>Quarterly Estimated Taxes</h2>
<table>
<tr><th>Quarter</th><th>Period</th><th>Due Date</th></tr>
<tr><td>Q1</td><td>January - March</td><td>April 15, 2026</td></tr>
<tr><td>Q2</td><td>April - June</td><td>June 15, 2026</td></tr>
<tr><td>Q3</td><td>July - September</td><td>September 15, 2026</td></tr>
<tr><td>Q4</td><td>October - December</td><td>January 15, 2027</td></tr>
</table>
<p>Use the Quarterly Tax Estimator tab in the Mileage & Tax Log spreadsheet to calculate your payments.</p>

<h2>State-Specific Notes</h2>
<ul>
<li><strong>No state tax:</strong> TX, FL, NV, WA, WY, TN, SD, NH, AK</li>
<li><strong>Low tax states:</strong> AZ (2.5%), CO (4.4%), IN (3.05%), NC (4.5%)</li>
<li><strong>High tax states:</strong> CA (up to 13.3%), NY (up to 10.9%), NJ (up to 10.75%)</li>
</ul>

<div class="tip"><strong>Pro Tip:</strong> If you earn $3,000/year from plasma and drive 2,000 miles to centers, your mileage deduction alone ($1,400) cuts your taxable income nearly in half.</div>
<div class="footer">PlasmaPayCalculator.com &mdash; Plasma Donor Pro Toolkit</div>`
  },
  {
    name: 'Deduction-Checklist',
    html: `<h1>Plasma Donor Deduction Checklist</h1>
<div class="brand">Plasma Pay Calculator &mdash; plasmapaycalculator.com</div>
<h2>Mileage & Transportation (Biggest Deduction)</h2>
<table>
<tr><th>Item</th><th>How to Track</th><th>Estimated Annual Value</th></tr>
<tr><td>IRS Standard Mileage Rate ($0.70/mile)</td><td>Mileage log (use the spreadsheet)</td><td>$700 - $2,000+</td></tr>
<tr><td>Parking at center</td><td>Receipts or bank statements</td><td>$0 - $200</td></tr>
<tr><td>Tolls</td><td>E-ZPass or toll receipts</td><td>$0 - $300</td></tr>
<tr><td>Public transit fares</td><td>Transit card statements</td><td>$0 - $500</td></tr>
</table>
<div class="tip"><strong>Example:</strong> If your center is 10 miles away, each round trip is 20 miles. At 100 visits/year: 2,000 miles &times; $0.70 = <strong>$1,400 deduction</strong>.</div>

<h2>Full Deduction Checklist</h2>
<table>
<tr><th>&#10003;</th><th>Deduction</th><th>Category</th><th>Notes</th></tr>
<tr><td>&#9744;</td><td>Mileage to/from center</td><td>Transportation</td><td>Use IRS standard rate</td></tr>
<tr><td>&#9744;</td><td>Parking fees at center</td><td>Transportation</td><td>Keep receipts</td></tr>
<tr><td>&#9744;</td><td>Tolls on route to center</td><td>Transportation</td><td>E-ZPass records work</td></tr>
<tr><td>&#9744;</td><td>Iron supplements</td><td>Health</td><td>Required for eligibility</td></tr>
<tr><td>&#9744;</td><td>Vitamin C supplements</td><td>Health</td><td>Aids iron absorption</td></tr>
<tr><td>&#9744;</td><td>B12 supplements</td><td>Health</td><td>Recovery support</td></tr>
<tr><td>&#9744;</td><td>Protein supplements/shakes</td><td>Health</td><td>Pre/post donation</td></tr>
<tr><td>&#9744;</td><td>Pre-donation meals</td><td>Health</td><td>Directly related to donation</td></tr>
<tr><td>&#9744;</td><td>Water bottles/hydration</td><td>Supplies</td><td>Business necessity</td></tr>
<tr><td>&#9744;</td><td>Vein care cream/supplies</td><td>Medical</td><td>Arm care products</td></tr>
<tr><td>&#9744;</td><td>Bandages, compression wraps</td><td>Medical</td><td>Post-donation care</td></tr>
<tr><td>&#9744;</td><td>Warm clothing for center</td><td>Supplies</td><td>If bought specifically</td></tr>
<tr><td>&#9744;</td><td>Phone usage (scheduling %)</td><td>Administrative</td><td>Business % of phone bill</td></tr>
<tr><td>&#9744;</td><td>Tax preparation fees</td><td>Administrative</td><td>Plasma-related portion</td></tr>
<tr><td>&#9744;</td><td>Record-keeping supplies</td><td>Administrative</td><td>Notebooks, folders</td></tr>
<tr><td>&#9744;</td><td>Insulated bag (snacks)</td><td>Supplies</td><td>For post-donation nutrition</td></tr>
</table>

<h2>Sample Schedule C Summary</h2>
<table>
<tr><th>Line</th><th>Item</th><th>Amount</th></tr>
<tr><td>Line 1</td><td>Gross Plasma Income</td><td>$4,800</td></tr>
<tr><td>Line 9</td><td>Car/Truck Expenses (mileage)</td><td>($1,400)</td></tr>
<tr><td>Line 22</td><td>Supplies</td><td>($300)</td></tr>
<tr><td>Line 27</td><td>Other Expenses (health/admin)</td><td>($400)</td></tr>
<tr><td>Line 31</td><td><strong>Net Profit</strong></td><td><strong>$2,700</strong></td></tr>
</table>
<p>In this example, deductions saved you <strong>$2,100 off your taxable income</strong>, which at a 12% tax rate saves <strong>$252+ in federal taxes</strong>.</p>
<div class="footer">PlasmaPayCalculator.com &mdash; Plasma Donor Pro Toolkit</div>`
  },
  {
    name: 'Center-Pay-Rate-Bible',
    html: `<h1>2026 Center Pay Rate Bible</h1>
<div class="brand">Plasma Pay Calculator &mdash; plasmapaycalculator.com</div>
<h2>Regular Donor Pay Rates (Per Visit)</h2>
<table>
<tr><th>Center</th><th>1st Visit/Week</th><th>2nd Visit/Week</th><th>Monthly (8 visits)</th></tr>
<tr><td>BioLife</td><td>$40-50</td><td>$50-70</td><td>$360-480</td></tr>
<tr><td>CSL Plasma</td><td>$35-55</td><td>$55-75</td><td>$360-520</td></tr>
<tr><td>Grifols / Biomat</td><td>$30-45</td><td>$45-65</td><td>$300-440</td></tr>
<tr><td>Octapharma</td><td>$30-50</td><td>$40-60</td><td>$280-440</td></tr>
<tr><td>KEDPLASMA</td><td>$30-40</td><td>$40-55</td><td>$280-380</td></tr>
<tr><td>Interstate Blood Bank</td><td>$25-40</td><td>$35-50</td><td>$240-360</td></tr>
</table>

<h2>New Donor Bonus Programs (2026)</h2>
<table>
<tr><th>Center</th><th>Bonus</th><th>Visits Required</th><th>Effective $/Visit</th></tr>
<tr><td>CSL Plasma</td><td>$900-1,100</td><td>10 in 60 days</td><td>$90-110</td></tr>
<tr><td>BioLife</td><td>$800-900</td><td>8 in 45 days</td><td>$100-112</td></tr>
<tr><td>Grifols</td><td>$700-800</td><td>6-8 in 30 days</td><td>$87-133</td></tr>
<tr><td>Octapharma</td><td>$600-750</td><td>6 in 30 days</td><td>$100-125</td></tr>
<tr><td>KEDPLASMA</td><td>$500-700</td><td>8 in 45 days</td><td>$62-87</td></tr>
</table>

<h2>Pay by Weight Tier (All Centers)</h2>
<table>
<tr><th>Weight</th><th>Plasma Collected</th><th>Base Pay Range</th><th>Annual Difference</th></tr>
<tr><td>110-149 lbs</td><td>690 mL</td><td>$30-45/visit</td><td>Baseline</td></tr>
<tr><td>150-174 lbs</td><td>825 mL</td><td>$40-55/visit</td><td>+$800-1,000/year</td></tr>
<tr><td>175-399 lbs</td><td>880 mL</td><td>$50-75/visit</td><td>+$1,600-2,400/year</td></tr>
</table>

<h2>Loyalty & Referral Programs</h2>
<table>
<tr><th>Center</th><th>Loyalty Perk</th><th>Referral Bonus</th></tr>
<tr><td>BioLife</td><td>Bonus for 8 donations/month</td><td>$50-100 per referral</td></tr>
<tr><td>CSL Plasma</td><td>iGive Rewards loyalty tiers</td><td>$50-75 per referral</td></tr>
<tr><td>Grifols</td><td>Loyalty points for gift cards</td><td>$25-50 per referral</td></tr>
<tr><td>Octapharma</td><td>Monthly bonus promotions</td><td>$50 per referral</td></tr>
</table>

<div class="tip"><strong>Pro Tip:</strong> Pay rates vary significantly by location. Urban centers often pay $10-20 more per visit than rural ones. Check multiple centers within driving distance.</div>
<div class="footer">PlasmaPayCalculator.com &mdash; Plasma Donor Pro Toolkit</div>`
  },
  {
    name: 'Weight-Optimization-Guide',
    html: `<h1>Weight Optimization: Earn $10-$25 More Per Visit</h1>
<div class="brand">Plasma Pay Calculator &mdash; plasmapaycalculator.com</div>
<h2>How Weight Affects Your Pay</h2>
<p>Plasma centers pay based on how much plasma they can collect, which is determined by your weight. There are typically 3 tiers:</p>
<table>
<tr><th>Tier</th><th>Weight Range</th><th>Plasma Volume</th><th>Typical Pay</th></tr>
<tr><td>Tier 1</td><td>110-149 lbs</td><td>690 mL</td><td>$30-45</td></tr>
<tr><td>Tier 2</td><td>150-174 lbs</td><td>825 mL</td><td>$40-55</td></tr>
<tr><td>Tier 3</td><td>175+ lbs</td><td>880 mL</td><td>$50-75</td></tr>
</table>

<h2>The Math: Why 1 Tier Makes a Big Difference</h2>
<table>
<tr><th></th><th>Tier 1 (130 lbs)</th><th>Tier 2 (155 lbs)</th><th>Tier 3 (180 lbs)</th></tr>
<tr><td>Per Visit</td><td>$40</td><td>$50</td><td>$65</td></tr>
<tr><td>Per Month (8 visits)</td><td>$320</td><td>$400</td><td>$520</td></tr>
<tr><td>Per Year (100 visits)</td><td>$4,000</td><td>$5,000</td><td>$6,500</td></tr>
<tr><td><strong>Annual Difference</strong></td><td>Baseline</td><td><strong>+$1,000</strong></td><td><strong>+$2,500</strong></td></tr>
</table>

<h2>How to Move Up a Tier (Safely)</h2>
<ul>
<li><strong>If you're 145-149 lbs:</strong> Gaining 1-5 lbs moves you to Tier 2 (+$1,000/year)</li>
<li><strong>Healthy weight gain:</strong> Increase protein intake, add strength training</li>
<li><strong>Weigh-in tips:</strong> Wear heavier clothes, hydrate well (water adds weight)</li>
<li><strong>Don't:</strong> Unhealthily gain weight just for plasma pay &mdash; focus on muscle</li>
<li><strong>Track:</strong> Know your weight before each visit to stay in the optimal tier</li>
</ul>

<h2>Weight Tier Strategy by Center</h2>
<table>
<tr><th>Center</th><th>Weigh-in Timing</th><th>Clothing Policy</th><th>Notes</th></tr>
<tr><td>BioLife</td><td>Every visit</td><td>Can wear clothes/shoes</td><td>Consistent scales</td></tr>
<tr><td>CSL Plasma</td><td>Every visit</td><td>Shoes on at most locations</td><td>May vary by location</td></tr>
<tr><td>Grifols</td><td>Every visit</td><td>Varies by location</td><td>Ask your center</td></tr>
<tr><td>Octapharma</td><td>Every visit</td><td>Standard clothing OK</td><td>Check with staff</td></tr>
</table>

<div class="tip"><strong>Pro Tip:</strong> If you're right at a tier boundary, weighing in with shoes and a hoodie can add 2-3 lbs. Over 100 visits/year, that's an extra $1,000+.</div>
<div class="footer">PlasmaPayCalculator.com &mdash; Plasma Donor Pro Toolkit</div>`
  },
  {
    name: 'Deferral-Recovery-Plan',
    html: `<h1>Deferral Recovery Plan: Get Back In Fast</h1>
<div class="brand">Plasma Pay Calculator &mdash; plasmapaycalculator.com</div>
<p>Getting deferred means lost income. Here's how to fix the most common deferrals and get back to donating ASAP.</p>

<h2>Low Hematocrit / Low Iron (Most Common)</h2>
<p><strong>Threshold:</strong> Hematocrit must be 38%+ (women) or 39%+ (men)</p>
<h3>Recovery Plan (3-7 days):</h3>
<ul>
<li>Take iron supplement (65mg elemental iron) with vitamin C daily</li>
<li>Eat iron-rich foods: red meat, spinach, fortified cereal, lentils</li>
<li>Avoid calcium, coffee, and tea within 2 hours of iron supplement</li>
<li>Cook in cast iron cookware (leaches iron into food)</li>
<li>Hydrate well &mdash; dehydration concentrates blood but can worsen hematocrit reading</li>
</ul>

<h2>Low Protein (Total Protein < 6.0 g/dL)</h2>
<h3>Recovery Plan (3-5 days):</h3>
<ul>
<li>Increase protein to 80-100g/day (chicken, eggs, fish, whey protein)</li>
<li>Eat protein with every meal and snack</li>
<li>Avoid alcohol (depletes protein levels)</li>
<li>Stay hydrated but don't over-hydrate (dilutes protein levels)</li>
</ul>

<h2>High Blood Pressure (>180/100)</h2>
<h3>Recovery Plan:</h3>
<ul>
<li>Deep breathing exercises for 10 minutes before your appointment</li>
<li>Arrive early and sit calmly for 15 minutes</li>
<li>Reduce sodium intake for 48 hours before</li>
<li>Avoid caffeine the morning of your appointment</li>
<li>If persistent, see your doctor &mdash; may indicate a health issue</li>
</ul>

<h2>High Pulse (>100 bpm)</h2>
<h3>Recovery Plan:</h3>
<ul>
<li>Skip caffeine on donation day</li>
<li>Practice slow breathing (4 seconds in, 6 seconds out)</li>
<li>Arrive 15 minutes early and sit quietly</li>
<li>Avoid rushing to the center</li>
<li>Stay calm during the screening &mdash; white coat syndrome is real</li>
</ul>

<h2>Medication-Related Deferral</h2>
<ul>
<li><strong>Antibiotics:</strong> Wait until course is complete + 24-72 hours</li>
<li><strong>Blood thinners:</strong> Permanent deferral at most centers</li>
<li><strong>Accutane:</strong> 30-day deferral after last dose</li>
<li><strong>Vaccines:</strong> Varies &mdash; COVID (no deferral), flu (no deferral), live vaccines (2-8 weeks)</li>
<li><strong>Always:</strong> Bring a list of all medications to your screening</li>
</ul>

<h2>Quick Reference: Deferral Recovery Cheat Sheet</h2>
<table>
<tr><th>Deferral Type</th><th>Recovery Time</th><th>#1 Fix</th></tr>
<tr><td>Low Iron/Hematocrit</td><td>3-7 days</td><td>Iron supplement + vitamin C</td></tr>
<tr><td>Low Protein</td><td>3-5 days</td><td>80g+ protein daily</td></tr>
<tr><td>High BP</td><td>Same day possible</td><td>Arrive early, breathe deeply</td></tr>
<tr><td>High Pulse</td><td>Same day possible</td><td>Skip caffeine, sit calmly</td></tr>
<tr><td>Antibiotics</td><td>1-3 days post-course</td><td>Complete full course first</td></tr>
<tr><td>Tattoo/Piercing</td><td>3-12 months</td><td>Wait it out (state dependent)</td></tr>
<tr><td>Travel</td><td>Varies</td><td>Check center's travel policy</td></tr>
</table>

<div class="tip"><strong>Pro Tip:</strong> Every deferral costs you $50-75 in lost income. Consistent iron supplementation and hydration prevent the vast majority of deferrals.</div>
<div class="footer">PlasmaPayCalculator.com &mdash; Plasma Donor Pro Toolkit</div>`
  },
  {
    name: 'Emergency-Cash-Playbook',
    html: `<h1>Emergency Cash Playbook: $200-$400 in 7 Days</h1>
<div class="brand">Plasma Pay Calculator &mdash; plasmapaycalculator.com</div>
<p>Need cash fast? Here's a day-by-day plan to earn $200-400 in your first week of plasma donation.</p>

<h2>Day-by-Day Emergency Plan</h2>
<table>
<tr><th>Day</th><th>Action</th><th>Expected Earnings</th></tr>
<tr><td>Day 1</td><td>Sign up at center with highest new donor bonus + donate</td><td>$75-125</td></tr>
<tr><td>Day 2</td><td>Recovery day &mdash; hydrate, eat protein</td><td>$0</td></tr>
<tr><td>Day 3</td><td>Second donation at same center</td><td>$50-100</td></tr>
<tr><td>Day 4</td><td>Recovery day + sign up at Center #2</td><td>$0</td></tr>
<tr><td>Day 5</td><td>First donation at Center #2</td><td>$75-125</td></tr>
<tr><td>Day 6</td><td>Recovery day</td><td>$0</td></tr>
<tr><td>Day 7</td><td>Second donation at Center #2</td><td>$50-100</td></tr>
<tr><td colspan="2"><strong>TOTAL WEEK 1</strong></td><td><strong>$250-450</strong></td></tr>
</table>

<h2>Maximize Your First Visit Pay</h2>
<ul>
<li><strong>Choose the center with the biggest new donor bonus</strong> (CSL often pays $100+ for first visit)</li>
<li><strong>Bring all documents:</strong> Photo ID, proof of address, Social Security card</li>
<li><strong>Arrive early:</strong> First visit takes 2-3 hours (includes physical and screening)</li>
<li><strong>Hydrate heavily</strong> the day before &mdash; faster donation = faster payment</li>
</ul>

<h2>Same-Day Payment Centers</h2>
<table>
<tr><th>Center</th><th>Payment Method</th><th>How Fast</th></tr>
<tr><td>BioLife</td><td>Prepaid debit card</td><td>Loaded immediately after donation</td></tr>
<tr><td>CSL Plasma</td><td>Prepaid debit card</td><td>Loaded immediately after donation</td></tr>
<tr><td>Grifols/Biomat</td><td>Prepaid debit card</td><td>Loaded immediately after donation</td></tr>
<tr><td>Octapharma</td><td>Prepaid debit card</td><td>Loaded immediately after donation</td></tr>
</table>
<p>All major centers pay via prepaid debit card loaded immediately. You can use it at any store or ATM that same day.</p>

<h2>If You Need More Than $400</h2>
<ul>
<li><strong>Week 2-4:</strong> Continue donating 2x/week while stacking new donor bonuses</li>
<li><strong>Refer friends:</strong> Earn $50-100 per friend who donates</li>
<li><strong>Stack center bonuses:</strong> See the Bonus Stacking Cheat Sheet</li>
<li><strong>Month 1 realistic total:</strong> $600-1,200+ across 2 centers</li>
</ul>

<div class="tip"><strong>Pro Tip:</strong> Your first 30 days are the highest-earning period because of new donor bonuses. Take advantage of every promotion available.</div>
<div class="footer">PlasmaPayCalculator.com &mdash; Plasma Donor Pro Toolkit</div>`
  },
  {
    name: 'Donor-Essentials-Checklist',
    html: `<h1>Donor Essentials Checklist</h1>
<div class="brand">Plasma Pay Calculator &mdash; plasmapaycalculator.com</div>
<h2>The Starter Kit &mdash; Before Your First Visit (~$45-55)</h2>
<table>
<tr><th>&#10003;</th><th>Item</th><th>Why</th><th>Est. Cost</th></tr>
<tr><td>&#9744;</td><td>32 oz water bottle</td><td>Stay hydrated before/during/after</td><td>$10-15</td></tr>
<tr><td>&#9744;</td><td>Iron supplement (65mg)</td><td>Prevent low iron deferrals</td><td>$8-12</td></tr>
<tr><td>&#9744;</td><td>Vitamin C supplement</td><td>Boosts iron absorption</td><td>$5-8</td></tr>
<tr><td>&#9744;</td><td>Protein bars (box)</td><td>Pre/post donation nutrition</td><td>$12-18</td></tr>
<tr><td>&#9744;</td><td>Stress ball / grip ball</td><td>Speeds up donation 20-30%</td><td>$3-5</td></tr>
<tr><td>&#9744;</td><td>Phone charger (portable)</td><td>Entertainment during 45-60 min donation</td><td>$10-15</td></tr>
</table>

<h2>The Recovery Kit &mdash; For Regular Donors (~$35-50)</h2>
<table>
<tr><th>&#10003;</th><th>Item</th><th>Why</th><th>Est. Cost</th></tr>
<tr><td>&#9744;</td><td>Arnica gel or cream</td><td>Reduces bruising at needle site</td><td>$8-12</td></tr>
<tr><td>&#9744;</td><td>Self-adhesive bandage wrap</td><td>Better than center bandages</td><td>$5-8</td></tr>
<tr><td>&#9744;</td><td>Vitamin B12 supplement</td><td>Supports red blood cell production</td><td>$6-10</td></tr>
<tr><td>&#9744;</td><td>Electrolyte packets</td><td>Faster hydration recovery</td><td>$10-15</td></tr>
<tr><td>&#9744;</td><td>Heating pad</td><td>Warms veins before donation (faster flow)</td><td>$8-12</td></tr>
</table>

<h2>The Tracking Kit &mdash; Stay Organized (~$20-30)</h2>
<table>
<tr><th>&#10003;</th><th>Item</th><th>Why</th><th>Est. Cost</th></tr>
<tr><td>&#9744;</td><td>Small notebook / mileage log</td><td>Track visits and deductions</td><td>$3-5</td></tr>
<tr><td>&#9744;</td><td>Folder for tax documents</td><td>Keep 1099s and receipts organized</td><td>$2-3</td></tr>
<tr><td>&#9744;</td><td>Donation Tracker Spreadsheet</td><td>Digital tracking (included in toolkit)</td><td>Included</td></tr>
<tr><td>&#9744;</td><td>Mileage tracking app</td><td>Automate mileage deduction tracking</td><td>Free-$5/mo</td></tr>
</table>

<div class="tip"><strong>Pro Tip:</strong> The stress ball alone can cut your donation time from 60 to 40 minutes. That's 20 hours saved per year for regular donors.</div>
<div class="footer">PlasmaPayCalculator.com &mdash; Plasma Donor Pro Toolkit</div>`
  },
  {
    name: 'Eligibility-Self-Assessment',
    html: `<h1>Eligibility Self-Assessment Checklist</h1>
<div class="brand">Plasma Pay Calculator &mdash; plasmapaycalculator.com</div>
<p>Before visiting a center, make sure you meet the basic requirements. This checklist covers what every center checks.</p>

<h2>Basic Requirements</h2>
<table>
<tr><th>&#10003;</th><th>Requirement</th><th>Details</th></tr>
<tr><td>&#9744;</td><td>Age: 18-69 years old</td><td>Some centers accept 16-17 with parental consent</td></tr>
<tr><td>&#9744;</td><td>Weight: 110 lbs minimum</td><td>Higher weight = higher pay</td></tr>
<tr><td>&#9744;</td><td>Valid photo ID</td><td>Driver's license, passport, or state ID</td></tr>
<tr><td>&#9744;</td><td>Proof of address</td><td>Utility bill, bank statement, or lease</td></tr>
<tr><td>&#9744;</td><td>Social Security card or number</td><td>Required for tax reporting</td></tr>
<tr><td>&#9744;</td><td>Generally good health</td><td>No acute illness on donation day</td></tr>
</table>

<h2>Health Screening (You Should Pass If...)</h2>
<table>
<tr><th>&#10003;</th><th>Screening Item</th><th>Passing Range</th></tr>
<tr><td>&#9744;</td><td>Temperature</td><td>Below 99.5&deg;F</td></tr>
<tr><td>&#9744;</td><td>Blood pressure</td><td>Below 180/100</td></tr>
<tr><td>&#9744;</td><td>Pulse</td><td>50-100 bpm</td></tr>
<tr><td>&#9744;</td><td>Hematocrit (iron)</td><td>38%+ (women) / 39%+ (men)</td></tr>
<tr><td>&#9744;</td><td>Total protein</td><td>6.0 g/dL or higher</td></tr>
<tr><td>&#9744;</td><td>No visible track marks</td><td>Clean arm veins</td></tr>
</table>

<h2>Common Disqualifiers (Temporary)</h2>
<table>
<tr><th>Condition</th><th>Wait Period</th><th>Notes</th></tr>
<tr><td>Cold or flu</td><td>Until symptoms resolve</td><td>Must be symptom-free</td></tr>
<tr><td>Antibiotics</td><td>Until course complete + 24-72 hrs</td><td>Depends on the medication</td></tr>
<tr><td>Tattoo or piercing</td><td>3-12 months</td><td>State dependent</td></tr>
<tr><td>Surgery</td><td>6-12 months</td><td>Depends on type</td></tr>
<tr><td>Pregnancy</td><td>6 months postpartum</td><td>Standard deferral</td></tr>
<tr><td>Travel to malaria areas</td><td>12 months</td><td>Check CDC list</td></tr>
<tr><td>Recent vaccination</td><td>0-8 weeks</td><td>Varies by vaccine type</td></tr>
</table>

<h2>Permanent Disqualifiers</h2>
<ul>
<li>HIV/AIDS positive</li>
<li>Hepatitis B or C positive</li>
<li>Certain autoimmune conditions</li>
<li>History of IV drug use</li>
<li>Organ transplant recipient</li>
</ul>

<div class="tip"><strong>Note:</strong> When in doubt, visit the center &mdash; they'll do a free physical exam on your first visit and tell you definitively if you qualify. The screening is free with no obligation.</div>
<div class="footer">PlasmaPayCalculator.com &mdash; Plasma Donor Pro Toolkit</div>`
  }
];

(async () => {
  const browser = await puppeteer.launch({ headless: true });

  for (const pdf of pdfs) {
    const page = await browser.newPage();
    const fullHtml = `<!DOCTYPE html><html><head><style>${STYLE}</style></head><body>${pdf.html}</body></html>`;
    await page.setContent(fullHtml, { waitUntil: 'domcontentloaded' });
    const fp = path.join(OUT, `${pdf.name}.pdf`);
    await page.pdf({
      path: fp,
      format: 'Letter',
      margin: { top: '0.5in', right: '0.5in', bottom: '0.5in', left: '0.5in' },
      printBackground: true,
    });
    await page.close();
    console.log('Created:', pdf.name + '.pdf');
  }

  await browser.close();
  console.log('All plasma PDFs generated!');
})();
