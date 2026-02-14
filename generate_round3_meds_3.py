#!/usr/bin/env python3
"""Generate Round 3 Meds Batch 3: 4 medication-specific plasma donation eligibility pages."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_batch1_centers import make_en_page, make_faq, AFFILIATE_BLOCK, PRO_TOOLKIT, related_reading, footer_related
BLOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'blog')

os.makedirs(BLOG_DIR, exist_ok=True)

# ============================================================
# Shared helpers
# ============================================================

TOC_ITEMS = [
    ('quick-answer', 'Quick Answer'),
    ('eligibility', 'Eligibility'),
    ('how-it-works', 'How It Works'),
    ('center-policies', 'Center Policies'),
    ('screening-tips', 'Screening Tips'),
    ('timing', 'Timing'),
    ('faq', 'FAQ'),
]

# ============================================================
# PAGE 1 — Lithium
# ============================================================

lithium_slug = 'can-you-donate-plasma-on-lithium-2026'
lithium_title = 'Can You Donate Plasma on Lithium? Bipolar Medication Guide (2026)'
lithium_meta = 'Can you donate plasma while taking lithium? It depends — some centers defer due to the narrow therapeutic window and dehydration risk. Full 2026 eligibility breakdown inside.'
lithium_content = f'''
<div class="highlight-box" id="quick-answer">
<h3>Quick Answer: Can You Donate Plasma on Lithium?</h3>
<p><strong>It depends.</strong> Lithium sits in a gray area for plasma donation eligibility. Some centers will allow you to donate if your lithium levels are stable and you are well-hydrated, while others issue a blanket deferral because of lithium\'s narrow therapeutic window. Dehydration during the donation process can push lithium concentrations into the toxic range, which is the primary safety concern. Always call your specific center before visiting.</p>
</div>

<h2 id="eligibility">Lithium and Plasma Donation Eligibility</h2>

<p>Lithium carbonate is one of the oldest and most effective mood stabilizers, widely prescribed for bipolar I disorder, bipolar II, and schizoaffective disorder. Its eligibility status for plasma donation is more nuanced than most medications.</p>

<h3>Why Lithium Is Complicated</h3>

<ul>
<li><strong>Narrow therapeutic window:</strong> Therapeutic blood levels are 0.6 - 1.2 mEq/L; toxicity begins above 1.5 mEq/L — a very small margin</li>
<li><strong>Dehydration sensitivity:</strong> Plasma donation removes approximately 600 - 880 mL of fluid, which can concentrate lithium in the blood</li>
<li><strong>Renal clearance:</strong> Lithium is cleared exclusively by the kidneys; any fluid shift affects excretion rate</li>
<li><strong>Side-effect overlap:</strong> Common lithium side effects (tremor, nausea, dizziness) mimic donation reactions, making monitoring harder</li>
</ul>

<h3>When You CAN Donate</h3>

<ul>
<li>Lithium levels are stable and recently verified (within 30 - 60 days)</li>
<li>You are on a consistent dose for at least 3 months</li>
<li>No recent episodes of lithium toxicity</li>
<li>You are well-hydrated before and after the visit</li>
<li>The center\'s medical director approves your case</li>
</ul>

<h3>When You\'re Deferred</h3>

<ul>
<li>Lithium levels are outside the therapeutic range</li>
<li>Recent dosage adjustment (within the last 4 - 6 weeks)</li>
<li>History of lithium toxicity episodes</li>
<li>Concurrent kidney impairment or renal issues</li>
<li>Signs of dehydration at the pre-donation screening</li>
<li>The center has a blanket lithium deferral policy</li>
</ul>

<h2 id="how-it-works">How Lithium Affects the Donation Process</h2>

<p>Understanding the pharmacology helps explain why centers are cautious.</p>

<h3>Lithium and Fluid Balance</h3>

<p>Lithium is a small ion that distributes in total body water and is excreted almost entirely by the kidneys. Unlike most drugs that bind to plasma proteins, lithium is freely dissolved in serum. When plasma volume drops during donation:</p>

<ul>
<li><strong>Concentration increases:</strong> Removing 600 - 880 mL of plasma temporarily raises lithium blood levels</li>
<li><strong>Kidney compensation takes time:</strong> The kidneys need hours to rebalance sodium and lithium levels</li>
<li><strong>Dehydration risk compounds:</strong> If you arrive under-hydrated, the effect is magnified</li>
</ul>

<h3>Lithium Toxicity Symptoms to Watch For</h3>

<table>
<thead>
<tr><th>Severity</th><th>Lithium Level</th><th>Symptoms</th></tr>
</thead>
<tbody>
<tr><td>Mild Toxicity</td><td>1.5 - 2.0 mEq/L</td><td>Nausea, tremor, diarrhea, drowsiness</td></tr>
<tr><td>Moderate Toxicity</td><td>2.0 - 2.5 mEq/L</td><td>Confusion, slurred speech, muscle twitching, vomiting</td></tr>
<tr><td>Severe Toxicity</td><td>&gt; 2.5 mEq/L</td><td>Seizures, kidney failure, cardiac arrhythmias</td></tr>
</tbody>
</table>

<p><strong>Important:</strong> Some of these symptoms (nausea, dizziness, drowsiness) also occur normally after plasma donation, making it difficult to distinguish routine post-donation effects from early toxicity.</p>

{AFFILIATE_BLOCK}

<h2 id="center-policies">Center-by-Center Lithium Policies</h2>

<p>Policies vary significantly. Here is a general overview of what to expect:</p>

<table>
<thead>
<tr><th>Center</th><th>Typical Lithium Policy</th><th>Notes</th></tr>
</thead>
<tbody>
<tr><td>CSL Plasma</td><td>Case-by-case review</td><td>Medical director approval; recent lab work may be required</td></tr>
<tr><td>BioLife</td><td>Case-by-case review</td><td>Stable levels and documented prescription needed</td></tr>
<tr><td>Octapharma</td><td>May defer</td><td>Tends to be more conservative on mood stabilizers</td></tr>
<tr><td>Grifols / Biomat</td><td>Case-by-case review</td><td>Some locations defer; call ahead</td></tr>
<tr><td>KEDPlasma</td><td>May defer</td><td>Varies by location; ask the medical team</td></tr>
</tbody>
</table>

<p><strong>Pro tip:</strong> Always call the center before your visit and specifically mention lithium. Ask to speak with the medical staff or center nurse if the front desk is unsure.</p>

<h2 id="screening-tips">Screening Tips for Lithium Users</h2>

<ol>
<li><strong>Bring recent lab work:</strong> A lithium level drawn within the last 30 - 60 days shows you are in the therapeutic range</li>
<li><strong>Bring your prescription bottle:</strong> Verifying the medication, dosage, and prescriber helps the screening nurse</li>
<li><strong>Disclose everything:</strong> Mention lithium upfront — do not wait for the screener to ask about it</li>
<li><strong>Note your diagnosis:</strong> Some centers are more flexible if the underlying condition (e.g., bipolar disorder) is well-controlled</li>
<li><strong>Stay hydrated:</strong> Drink at least 64 oz of water the day before and 16 - 24 oz in the hour before your appointment</li>
</ol>

{PRO_TOOLKIT}

<h2 id="timing">Timing Your Donation Around Lithium</h2>

<p>If your center does allow lithium donors, timing matters:</p>

<ul>
<li><strong>Donate at trough:</strong> Schedule your appointment right before your next lithium dose, when blood levels are at their lowest</li>
<li><strong>Hydrate aggressively:</strong> Aim for 80 - 100 oz of water in the 24 hours before donation</li>
<li><strong>Eat a salty snack:</strong> Sodium intake helps maintain lithium clearance</li>
<li><strong>Avoid alcohol and caffeine:</strong> Both are dehydrating and can exacerbate fluid loss</li>
<li><strong>Monitor after donation:</strong> Watch for signs of toxicity (tremor, nausea, confusion) for 12 - 24 hours post-donation</li>
<li><strong>Take your next dose on schedule:</strong> Do not skip or delay lithium doses around donation</li>
</ul>

{related_reading([
    ('/blog/can-you-donate-plasma-on-antidepressants-2026.html', 'Can You Donate Plasma on Antidepressants?'),
    ('/blog/can-you-donate-plasma-on-adderall-adhd-2026.html', 'Plasma Donation on Adderall / ADHD Meds'),
    ('/blog/how-to-avoid-plasma-deferral-2026.html', 'How to Avoid Plasma Deferral'),
    ('/blog/plasma-donation-day-before-checklist-2026.html', 'Day-Before Checklist'),
])}

<h2 id="faq">Frequently Asked Questions</h2>

<h3>Will plasma donation change my lithium levels?</h3>
<p>Yes, temporarily. Removing 600 - 880 mL of plasma reduces your total fluid volume, which can temporarily increase lithium concentration in your blood. The effect is usually mild and resolves within hours as your body replaces the lost fluid, but it is the main reason some centers defer lithium users.</p>

<h3>Do I need to bring lab work showing my lithium levels?</h3>
<p>Most centers that allow lithium donors will want to see recent lab results. A comprehensive metabolic panel (CMP) and lithium level drawn within the last 30 - 60 days is ideal. Some centers may require it; others will accept verbal confirmation that you are being monitored regularly.</p>

<h3>Can I donate if I take lithium for something other than bipolar disorder?</h3>
<p>Lithium is sometimes prescribed off-label for depression augmentation, cluster headaches, or other conditions. The eligibility depends on the medication itself, not the diagnosis, so the same rules apply regardless of why you take lithium.</p>

<h3>What should I do if I feel strange after donating while on lithium?</h3>
<p>If you experience worsening tremor, confusion, severe nausea, or slurred speech after donating, seek medical attention immediately. These could be signs of lithium toxicity. Mild dizziness and fatigue are normal after any plasma donation, but any symptom that goes beyond what you typically feel after donating should be evaluated.</p>

<h3>Are other bipolar medications easier for plasma donation?</h3>
<p>Yes. Valproic acid (Depakote), lamotrigine (Lamictal), and carbamazepine (Tegretol) are generally accepted at most centers because they do not carry the same dehydration-toxicity risk as lithium. If you are considering switching medications, discuss it with your psychiatrist — but never change medications solely to qualify for plasma donation.</p>

{footer_related()}
'''

lithium_faqs = [
    make_faq("Will plasma donation change my lithium levels?",
             "Yes, temporarily. Removing plasma reduces fluid volume, which can briefly increase lithium concentration. The effect resolves within hours as the body replaces lost fluid."),
    make_faq("Do I need to bring lab work showing my lithium levels?",
             "Most centers that allow lithium donors will want recent lab results. A lithium level drawn within the last 30-60 days is ideal."),
    make_faq("Can I donate if I take lithium for something other than bipolar disorder?",
             "The eligibility depends on the medication itself, not the diagnosis. The same lithium rules apply regardless of indication."),
    make_faq("What should I do if I feel strange after donating while on lithium?",
             "If you experience worsening tremor, confusion, severe nausea, or slurred speech, seek medical attention immediately as these could indicate lithium toxicity."),
    make_faq("Are other bipolar medications easier for plasma donation?",
             "Yes. Valproic acid (Depakote), lamotrigine (Lamictal), and carbamazepine (Tegretol) are generally accepted at most centers because they don't carry the same dehydration-toxicity risk as lithium."),
]

# ============================================================
# PAGE 2 — Warfarin / Blood Thinners
# ============================================================

warfarin_slug = 'can-you-donate-plasma-on-warfarin-blood-thinners-2026'
warfarin_title = 'Can You Donate Plasma on Warfarin (Coumadin) or Blood Thinners? 2026 Guide'
warfarin_meta = 'Warfarin and most blood thinners are a permanent deferral for plasma donation — anticoagulants affect the clotting factors plasma centers collect. Full 2026 guide to blood thinner eligibility.'
warfarin_content = f'''
<div class="highlight-box" id="quick-answer">
<h3>Quick Answer: Can You Donate Plasma on Warfarin or Blood Thinners?</h3>
<p><strong>Generally, no.</strong> Warfarin (Coumadin) and most anticoagulant medications result in a permanent deferral at the vast majority of plasma centers. The reason is straightforward: blood thinners directly affect the clotting factors in plasma, which are the exact proteins that centers are collecting. Aspirin and NSAIDs are a different story — those affect platelets, not clotting factors, and may be allowed.</p>
</div>

<h2 id="eligibility">Blood Thinner Eligibility Breakdown</h2>

<p>Not all "blood thinners" are treated the same. Eligibility depends on the specific medication and its mechanism of action.</p>

<h3>Anticoagulants — Generally NOT Allowed</h3>

<table>
<thead>
<tr><th>Medication</th><th>Brand Name(s)</th><th>Mechanism</th><th>Plasma Donation Status</th></tr>
</thead>
<tbody>
<tr><td>Warfarin</td><td>Coumadin, Jantoven</td><td>Vitamin K antagonist — blocks factors II, VII, IX, X</td><td>Permanent deferral</td></tr>
<tr><td>Heparin (unfractionated)</td><td>Heparin sodium</td><td>Activates antithrombin III</td><td>Permanent deferral</td></tr>
<tr><td>Enoxaparin</td><td>Lovenox</td><td>Low-molecular-weight heparin</td><td>Permanent deferral</td></tr>
<tr><td>Rivaroxaban</td><td>Xarelto</td><td>Direct Factor Xa inhibitor</td><td>Permanent deferral</td></tr>
<tr><td>Apixaban</td><td>Eliquis</td><td>Direct Factor Xa inhibitor</td><td>Permanent deferral</td></tr>
<tr><td>Dabigatran</td><td>Pradaxa</td><td>Direct thrombin inhibitor</td><td>Permanent deferral</td></tr>
<tr><td>Edoxaban</td><td>Savaysa</td><td>Direct Factor Xa inhibitor</td><td>Permanent deferral</td></tr>
</tbody>
</table>

<h3>Antiplatelet Agents — Sometimes Allowed</h3>

<table>
<thead>
<tr><th>Medication</th><th>Brand Name(s)</th><th>Mechanism</th><th>Plasma Donation Status</th></tr>
</thead>
<tbody>
<tr><td>Low-dose aspirin (81 mg)</td><td>Baby aspirin</td><td>Irreversible COX-1 inhibitor — affects platelets only</td><td>Often allowed</td></tr>
<tr><td>Ibuprofen, naproxen</td><td>Advil, Aleve</td><td>Reversible COX inhibitor</td><td>Usually allowed</td></tr>
<tr><td>Clopidogrel</td><td>Plavix</td><td>P2Y12 platelet inhibitor</td><td>Usually deferred</td></tr>
<tr><td>Prasugrel</td><td>Effient</td><td>P2Y12 platelet inhibitor</td><td>Usually deferred</td></tr>
<tr><td>Ticagrelor</td><td>Brilinta</td><td>P2Y12 platelet inhibitor</td><td>Usually deferred</td></tr>
</tbody>
</table>

<h2 id="how-it-works">Why Blood Thinners Disqualify You</h2>

<p>Understanding the science clarifies why this deferral exists and why it is different from most medication deferrals.</p>

<h3>What Plasma Centers Actually Collect</h3>

<p>Plasma is the liquid portion of blood containing hundreds of proteins. The primary therapeutic products manufactured from donated plasma include:</p>

<ul>
<li><strong>Clotting factor concentrates:</strong> Used to treat hemophilia A (Factor VIII) and hemophilia B (Factor IX)</li>
<li><strong>Immunoglobulins (IVIG):</strong> Used for immune deficiencies and autoimmune conditions</li>
<li><strong>Albumin:</strong> Used for burn patients, liver disease, and surgical recovery</li>
</ul>

<p>Warfarin and other anticoagulants directly inhibit or destroy the clotting factors that are the primary reason plasma is collected. Plasma from a donor on warfarin would contain non-functional or depleted clotting factors, making it unsuitable for manufacturing life-saving clotting factor concentrates.</p>

<h3>Aspirin and NSAIDs: Why They Are Different</h3>

<p>Aspirin and NSAIDs work on <strong>platelets</strong>, not on the clotting factors dissolved in plasma. During plasmapheresis, platelets are returned to you along with red blood cells. Because the platelets stay with the donor and do not end up in the collected plasma, aspirin and NSAID use does not affect the quality of the donated plasma product.</p>

<ul>
<li><strong>Low-dose aspirin (81 mg):</strong> Most centers allow this — it only affects platelet function</li>
<li><strong>Full-strength aspirin (325 mg):</strong> Some centers allow it; others defer for 48 hours after last dose</li>
<li><strong>Ibuprofen / naproxen:</strong> Reversible platelet inhibition; usually allowed after 24 hours</li>
</ul>

{AFFILIATE_BLOCK}

<h2 id="center-policies">Center-by-Center Blood Thinner Policies</h2>

<table>
<thead>
<tr><th>Center</th><th>Warfarin / Anticoagulants</th><th>Low-Dose Aspirin (81 mg)</th><th>Notes</th></tr>
</thead>
<tbody>
<tr><td>CSL Plasma</td><td>Permanent deferral</td><td>Usually allowed</td><td>Anticoagulants in any form are disqualifying</td></tr>
<tr><td>BioLife</td><td>Permanent deferral</td><td>Usually allowed</td><td>Must be stable; underlying condition reviewed</td></tr>
<tr><td>Octapharma</td><td>Permanent deferral</td><td>Usually allowed</td><td>DOACs (Eliquis, Xarelto) also disqualifying</td></tr>
<tr><td>Grifols / Biomat</td><td>Permanent deferral</td><td>Case by case</td><td>Ask medical staff directly</td></tr>
<tr><td>KEDPlasma</td><td>Permanent deferral</td><td>Usually allowed</td><td>All prescription anticoagulants excluded</td></tr>
</tbody>
</table>

<h2 id="screening-tips">Screening Tips for Blood Thinner Users</h2>

<ol>
<li><strong>Be upfront about your medication:</strong> Blood thinners will show in your medical history and failing to disclose them can result in a permanent ban</li>
<li><strong>Know the difference:</strong> If you take aspirin only, emphasize that it is an antiplatelet agent, not an anticoagulant</li>
<li><strong>Bring your medication list:</strong> A printed list from your pharmacy or doctor\'s office helps the screener quickly verify what you take</li>
<li><strong>Ask about the underlying condition:</strong> Even if the blood thinner disqualifies you, ask whether you would be eligible if the medication were discontinued (some conditions themselves are deferring)</li>
<li><strong>Do not stop your medication to donate:</strong> Stopping warfarin or other anticoagulants without physician supervision is medically dangerous and could lead to stroke, pulmonary embolism, or DVT</li>
</ol>

<div style="background: #fef2f2; border-left: 4px solid #ef4444; padding: 1rem 1.5rem; border-radius: 8px; margin: 1.5rem 0;">
<p style="margin: 0; color: #991b1b; font-weight: 600;">Safety Warning</p>
<p style="margin: 0.5rem 0 0; color: #7f1d1d;">Never stop or reduce your anticoagulant medication to qualify for plasma donation. The risk of blood clots, stroke, or heart attack far outweighs any donation compensation. Your medication was prescribed for a serious medical reason.</p>
</div>

{PRO_TOOLKIT}

<h2 id="timing">Timing and Alternative Options</h2>

<p>For most people on anticoagulants, plasma donation is not an option. However, there are some scenarios to consider:</p>

<h3>If You Are Temporarily on Blood Thinners</h3>

<ul>
<li><strong>Post-surgical heparin or Lovenox:</strong> Once discontinued and cleared by your doctor (typically 7 - 30 days), you may become eligible</li>
<li><strong>Short-term warfarin after DVT:</strong> Some centers will allow donation after 3 - 12 months off warfarin if the underlying clotting event is fully resolved</li>
<li><strong>Wait period:</strong> Even after stopping an anticoagulant, most centers require a 7 - 30 day waiting period for the medication to fully clear</li>
</ul>

<h3>Alternative Ways to Earn</h3>

<p>If blood thinners permanently disqualify you from plasma donation, consider:</p>

<ul>
<li><strong>Clinical trial participation:</strong> Some studies specifically recruit people on anticoagulants</li>
<li><strong>Blood donation:</strong> Some blood banks accept donors on certain anticoagulants (Red Cross allows warfarin donors for whole blood)</li>
<li><strong>Refer others:</strong> Most plasma centers pay $50 - $100 per successful referral</li>
</ul>

{related_reading([
    ('/blog/can-you-donate-plasma-on-antibiotics-2026.html', 'Can You Donate Plasma on Antibiotics?'),
    ('/blog/how-to-avoid-plasma-deferral-2026.html', 'How to Avoid Plasma Deferral'),
    ('/blog/can-you-donate-plasma-on-blood-thinners-2026.html', 'Blood Thinners and Plasma Donation Overview'),
    ('/blog/plasma-donation-day-before-checklist-2026.html', 'Day-Before Checklist'),
])}

<h2 id="faq">Frequently Asked Questions</h2>

<h3>Can I donate plasma if I only take baby aspirin (81 mg)?</h3>
<p>In most cases, yes. Low-dose aspirin affects platelets, not the clotting factors in plasma. Since platelets are returned to you during plasmapheresis, aspirin does not affect the quality of collected plasma. Most major centers (CSL, BioLife, Octapharma) allow donors on low-dose aspirin. Always confirm with your specific location.</p>

<h3>What if I stopped taking warfarin — how long until I can donate?</h3>
<p>Most centers require at least 7 - 30 days after your last warfarin dose, plus medical clearance from your physician confirming it is safe for you to be off the medication. The underlying condition (such as atrial fibrillation or prior DVT) may also need to be reviewed for eligibility.</p>

<h3>Can I switch from warfarin to aspirin so I can donate plasma?</h3>
<p>Never change your anticoagulant therapy for plasma donation purposes. Warfarin and aspirin treat fundamentally different conditions. If your doctor prescribed warfarin, it is because aspirin alone is not sufficient to prevent life-threatening blood clots. Discuss any medication changes with your prescribing physician.</p>

<h3>Does Eliquis (apixaban) disqualify me from donating plasma?</h3>
<p>Yes. Eliquis is a direct Factor Xa inhibitor, meaning it directly blocks one of the key clotting factors that plasma centers collect. Like warfarin, Eliquis results in a permanent deferral at virtually all commercial plasma centers.</p>

<h3>Why does the Red Cross accept warfarin donors but plasma centers do not?</h3>
<p>The Red Cross collects whole blood primarily for transfusions, where the recipient needs red blood cells. Commercial plasma centers collect plasma specifically for manufacturing clotting factor concentrates and other protein therapies. Because warfarin depletes functional clotting factors in plasma, it renders the donation unsuitable for that manufacturing purpose.</p>

{footer_related()}
'''

warfarin_faqs = [
    make_faq("Can I donate plasma if I only take baby aspirin (81 mg)?",
             "In most cases, yes. Low-dose aspirin affects platelets, not clotting factors. Since platelets are returned to you during plasmapheresis, aspirin does not affect collected plasma quality."),
    make_faq("What if I stopped taking warfarin — how long until I can donate?",
             "Most centers require 7-30 days after your last dose plus medical clearance. The underlying condition may also need review for eligibility."),
    make_faq("Can I switch from warfarin to aspirin so I can donate plasma?",
             "Never change your anticoagulant therapy for plasma donation. Warfarin and aspirin treat different conditions. Discuss any changes with your prescribing physician."),
    make_faq("Does Eliquis (apixaban) disqualify me from donating plasma?",
             "Yes. Eliquis is a direct Factor Xa inhibitor that blocks key clotting factors plasma centers collect, resulting in permanent deferral."),
    make_faq("Why does the Red Cross accept warfarin donors but plasma centers do not?",
             "The Red Cross collects whole blood for transfusions. Commercial plasma centers collect plasma for manufacturing clotting factor concentrates, which warfarin depletes."),
]

# ============================================================
# PAGE 3 — Muscle Relaxers
# ============================================================

muscle_slug = 'can-you-donate-plasma-on-muscle-relaxers-2026'
muscle_title = 'Can You Donate Plasma on Muscle Relaxers? 2026 Guide'
muscle_meta = 'Most muscle relaxants like Flexeril, Robaxin, and baclofen are allowed for plasma donation. Carisoprodol (Soma) may be flagged. Full 2026 eligibility guide.'
muscle_content = f'''
<div class="highlight-box" id="quick-answer">
<h3>Quick Answer: Can You Donate Plasma on Muscle Relaxers?</h3>
<p><strong>Generally, yes.</strong> Most muscle relaxant medications are allowed for plasma donation because they do not affect plasma proteins, clotting factors, or immune function. Cyclobenzaprine (Flexeril), methocarbamol (Robaxin), baclofen, and tizanidine (Zanaflex) are accepted at most centers. The main concern is drowsiness — you need to be alert enough to donate safely. Carisoprodol (Soma) may be flagged due to its abuse potential and Schedule IV controlled substance classification.</p>
</div>

<h2 id="eligibility">Muscle Relaxer Eligibility by Medication</h2>

<p>Here is a breakdown of common muscle relaxants and their plasma donation eligibility status:</p>

<table>
<thead>
<tr><th>Medication</th><th>Brand Name</th><th>DEA Schedule</th><th>Plasma Donation Status</th></tr>
</thead>
<tbody>
<tr><td>Cyclobenzaprine</td><td>Flexeril, Amrix</td><td>Not scheduled</td><td>Generally allowed</td></tr>
<tr><td>Methocarbamol</td><td>Robaxin</td><td>Not scheduled</td><td>Generally allowed</td></tr>
<tr><td>Baclofen</td><td>Lioresal, Gablofen</td><td>Not scheduled</td><td>Generally allowed</td></tr>
<tr><td>Tizanidine</td><td>Zanaflex</td><td>Not scheduled</td><td>Generally allowed</td></tr>
<tr><td>Metaxalone</td><td>Skelaxin</td><td>Not scheduled</td><td>Generally allowed</td></tr>
<tr><td>Orphenadrine</td><td>Norflex</td><td>Not scheduled</td><td>Generally allowed</td></tr>
<tr><td>Carisoprodol</td><td>Soma</td><td>Schedule IV</td><td>May be flagged / deferred</td></tr>
<tr><td>Dantrolene</td><td>Dantrium</td><td>Not scheduled</td><td>Case by case (liver concerns)</td></tr>
</tbody>
</table>

<h3>Why Most Muscle Relaxers Are Accepted</h3>

<ul>
<li><strong>No effect on clotting factors:</strong> Muscle relaxants do not alter the proteins collected during plasmapheresis</li>
<li><strong>No immune suppression:</strong> These medications target the central nervous system or skeletal muscle, not the immune system</li>
<li><strong>No contamination risk:</strong> Trace amounts in plasma do not affect manufacturing processes or end-product safety</li>
<li><strong>Common prescriptions:</strong> Millions of Americans take muscle relaxers; excluding them would significantly reduce the donor pool</li>
</ul>

<h3>The Carisoprodol (Soma) Exception</h3>

<p>Carisoprodol is the one muscle relaxant that may cause issues at screening. Here is why:</p>

<ul>
<li><strong>Schedule IV controlled substance:</strong> Higher abuse potential than other muscle relaxants</li>
<li><strong>Metabolizes to meprobamate:</strong> Soma\'s active metabolite is a barbiturate-like compound that raises red flags</li>
<li><strong>Sedation risk:</strong> Stronger sedative effect than other muscle relaxers, increasing donation safety concerns</li>
<li><strong>Prescription scrutiny:</strong> Centers may verify your prescription more closely and require documentation</li>
</ul>

<h2 id="how-it-works">How Muscle Relaxers Affect the Donation Process</h2>

<p>While muscle relaxants do not affect plasma quality, they can affect your experience during donation.</p>

<h3>Drowsiness During Donation</h3>

<p>The most common side effect of all muscle relaxants is drowsiness. During a 45 - 90 minute plasma donation session:</p>

<ul>
<li><strong>You must remain conscious:</strong> Staff need you alert enough to respond if there is a problem</li>
<li><strong>You must grip periodically:</strong> Many centers ask you to squeeze a stress ball to maintain blood flow</li>
<li><strong>You need to communicate:</strong> Alert staff to tingling, numbness, or discomfort in the needle arm</li>
<li><strong>You must drive home safely:</strong> Post-donation fatigue combined with medication drowsiness is a concern</li>
</ul>

<h3>Timing Around Peak Sedation</h3>

<table>
<thead>
<tr><th>Medication</th><th>Time to Peak Effect</th><th>Duration of Drowsiness</th><th>Suggested Donation Window</th></tr>
</thead>
<tbody>
<tr><td>Cyclobenzaprine (Flexeril)</td><td>1 - 2 hours</td><td>4 - 6 hours</td><td>Donate before morning dose or 6+ hours after dose</td></tr>
<tr><td>Methocarbamol (Robaxin)</td><td>1 - 2 hours</td><td>4 - 6 hours</td><td>Donate before morning dose or 6+ hours after dose</td></tr>
<tr><td>Baclofen</td><td>1 - 2 hours</td><td>6 - 8 hours</td><td>Donate before morning dose or 8+ hours after dose</td></tr>
<tr><td>Tizanidine (Zanaflex)</td><td>1 - 2 hours</td><td>3 - 6 hours</td><td>Donate before morning dose or 6+ hours after dose</td></tr>
<tr><td>Carisoprodol (Soma)</td><td>1 - 2 hours</td><td>4 - 6 hours</td><td>Donate before morning dose or 6+ hours after dose</td></tr>
</tbody>
</table>

{AFFILIATE_BLOCK}

<h2 id="center-policies">Center-by-Center Muscle Relaxer Policies</h2>

<table>
<thead>
<tr><th>Center</th><th>Standard Muscle Relaxers</th><th>Carisoprodol (Soma)</th><th>Notes</th></tr>
</thead>
<tbody>
<tr><td>CSL Plasma</td><td>Allowed</td><td>May require prescription verification</td><td>Must be alert and responsive during screening</td></tr>
<tr><td>BioLife</td><td>Allowed</td><td>Case by case</td><td>Disclose during health history questionnaire</td></tr>
<tr><td>Octapharma</td><td>Allowed</td><td>Case by case</td><td>May ask about underlying condition</td></tr>
<tr><td>Grifols / Biomat</td><td>Allowed</td><td>May defer</td><td>Varies by location; call ahead</td></tr>
<tr><td>KEDPlasma</td><td>Allowed</td><td>May defer</td><td>Schedule IV status may trigger review</td></tr>
</tbody>
</table>

<h2 id="screening-tips">Screening Tips for Muscle Relaxer Users</h2>

<ol>
<li><strong>Disclose all muscle relaxants:</strong> List every medication on the health questionnaire, including OTC options</li>
<li><strong>Bring your prescription bottle:</strong> Especially important for carisoprodol (Soma) since it is a controlled substance</li>
<li><strong>Mention the underlying condition:</strong> Whether it is back pain, fibromyalgia, or a sports injury, the reason you take the medication matters</li>
<li><strong>Be honest about drowsiness:</strong> If you feel too drowsy to drive, the center will likely defer you for the day</li>
<li><strong>Time your dose wisely:</strong> Take your muscle relaxer after your donation appointment, not before, to minimize sedation during the visit</li>
</ol>

{PRO_TOOLKIT}

<h2 id="timing">Timing Your Donation Around Muscle Relaxers</h2>

<p>Strategic timing can make your donation experience much smoother:</p>

<h3>Best Approach</h3>

<ul>
<li><strong>Morning appointment, evening dose:</strong> If you take your muscle relaxer at bedtime, schedule your donation for the morning when the medication has largely worn off</li>
<li><strong>Donate before your dose:</strong> Take your next dose after you finish donating and are safely home</li>
<li><strong>Avoid peak sedation:</strong> Do not donate within 2 hours of taking any muscle relaxant</li>
<li><strong>Plan transportation:</strong> If your muscle relaxer causes significant drowsiness, consider having someone drive you to and from the center</li>
</ul>

<h3>Post-Donation Considerations</h3>

<ul>
<li><strong>Increased drowsiness:</strong> Plasma donation itself can cause fatigue; combined with muscle relaxer sedation, you may feel more drowsy than usual</li>
<li><strong>Stay hydrated:</strong> Dehydration can worsen both post-donation fatigue and muscle relaxer side effects</li>
<li><strong>Eat a meal:</strong> A protein-rich meal after donation helps counteract fatigue</li>
<li><strong>Rest at the center:</strong> Take a few extra minutes in the refreshment area before driving</li>
</ul>

{related_reading([
    ('/blog/can-you-donate-plasma-on-antibiotics-2026.html', 'Can You Donate Plasma on Antibiotics?'),
    ('/blog/can-you-donate-plasma-on-adderall-adhd-2026.html', 'Plasma Donation on Adderall / ADHD Meds'),
    ('/blog/how-to-avoid-plasma-deferral-2026.html', 'How to Avoid Plasma Deferral'),
    ('/blog/first-plasma-donation-what-to-expect-2026.html', 'First Plasma Donation Guide'),
])}

<h2 id="faq">Frequently Asked Questions</h2>

<h3>Can I donate plasma if I take Flexeril (cyclobenzaprine)?</h3>
<p>Yes. Cyclobenzaprine (Flexeril) is one of the most commonly prescribed muscle relaxants and is accepted at virtually all plasma centers. It does not affect clotting factors or plasma proteins. Just make sure you are not overly drowsy at the time of your appointment.</p>

<h3>Will taking Soma (carisoprodol) disqualify me from donating?</h3>
<p>Not necessarily, but it may require extra verification. Carisoprodol is a Schedule IV controlled substance, so some centers will want to see your prescription and may ask additional questions. A few centers may defer carisoprodol users entirely due to its abuse potential and stronger sedative effects.</p>

<h3>Should I skip my muscle relaxer before donating?</h3>
<p>You should never stop a prescribed medication without consulting your doctor. However, if your doctor approves and you typically take your muscle relaxer on an as-needed basis (PRN), you can time your dose so you take it after your donation rather than before. This minimizes drowsiness during the visit.</p>

<h3>Can I donate plasma if I take baclofen for spasticity?</h3>
<p>Yes, baclofen is generally accepted. The key consideration is the underlying condition causing the spasticity. If baclofen is prescribed for multiple sclerosis, spinal cord injury, or another neurological condition, the center will evaluate whether the condition itself affects eligibility, separate from the medication.</p>

<h3>What if I feel too drowsy during the donation?</h3>
<p>Tell the staff immediately. They can slow the machine, give you fluids, or stop the donation early if needed. Your safety always comes first. If drowsiness is a recurring issue, reschedule your donation for a time when your medication effects have worn off, or discuss timing adjustments with your prescribing doctor.</p>

{footer_related()}
'''

muscle_faqs = [
    make_faq("Can I donate plasma if I take Flexeril (cyclobenzaprine)?",
             "Yes. Cyclobenzaprine is accepted at virtually all plasma centers. It does not affect clotting factors or plasma proteins. Just ensure you are not overly drowsy."),
    make_faq("Will taking Soma (carisoprodol) disqualify me from donating?",
             "Not necessarily, but it may require extra verification. Carisoprodol is a Schedule IV controlled substance, so some centers want to see your prescription and may defer."),
    make_faq("Should I skip my muscle relaxer before donating?",
             "Never stop prescribed medication without consulting your doctor. If you take it as-needed, you can time your dose after donation rather than before to minimize drowsiness."),
    make_faq("Can I donate plasma if I take baclofen for spasticity?",
             "Yes, baclofen is generally accepted. The center will evaluate whether the underlying condition itself affects eligibility, separate from the medication."),
    make_faq("What if I feel too drowsy during the donation?",
             "Tell staff immediately. They can slow the machine, give fluids, or stop early. Reschedule for a time when medication effects have worn off."),
]

# ============================================================
# PAGE 4 — Hydroxychloroquine (Plaquenil)
# ============================================================

hcq_slug = 'can-you-donate-plasma-on-hydroxychloroquine-2026'
hcq_title = 'Can You Donate Plasma on Hydroxychloroquine (Plaquenil)? 2026 Guide'
hcq_meta = 'Hydroxychloroquine (Plaquenil) itself usually does not disqualify you from plasma donation, but the underlying autoimmune condition often does. Full 2026 eligibility guide by indication.'
hcq_content = f'''
<div class="highlight-box" id="quick-answer">
<h3>Quick Answer: Can You Donate Plasma on Hydroxychloroquine?</h3>
<p><strong>It depends on why you take it.</strong> Hydroxychloroquine (Plaquenil) as a medication is generally not disqualifying for plasma donation. However, the underlying condition being treated — lupus, rheumatoid arthritis, or malaria prophylaxis — often determines eligibility. Lupus and active autoimmune conditions typically result in deferral. Malaria prophylaxis requires a waiting period after returning from endemic areas. Each indication has different eligibility rules.</p>
</div>

<h2 id="eligibility">Eligibility by Indication</h2>

<p>Hydroxychloroquine is prescribed for several very different conditions. Your eligibility depends primarily on the diagnosis, not the medication itself.</p>

<table>
<thead>
<tr><th>Indication</th><th>Common Diagnosis</th><th>Plasma Donation Status</th><th>Key Factor</th></tr>
</thead>
<tbody>
<tr><td>Systemic Lupus Erythematosus (SLE)</td><td>Lupus</td><td>Usually deferred</td><td>Autoimmune antibodies in plasma</td></tr>
<tr><td>Rheumatoid Arthritis (RA)</td><td>RA</td><td>Depends on disease activity</td><td>Varies by center; mild RA may be accepted</td></tr>
<tr><td>Discoid Lupus</td><td>Skin-only lupus</td><td>Case by case</td><td>Less systemic involvement than SLE</td></tr>
<tr><td>Malaria Prophylaxis</td><td>Travel prevention</td><td>Deferred during + after travel</td><td>Deferral period for malaria-endemic travel</td></tr>
<tr><td>Sjogren\'s Syndrome</td><td>Sjogren\'s</td><td>Usually deferred</td><td>Autoimmune condition</td></tr>
<tr><td>Dermatomyositis</td><td>Inflammatory myopathy</td><td>Usually deferred</td><td>Autoimmune condition</td></tr>
</tbody>
</table>

<h3>Lupus (SLE) — Usually Deferred</h3>

<p>Systemic lupus erythematosus is the most common reason for hydroxychloroquine prescriptions and the most likely to result in deferral.</p>

<ul>
<li><strong>Autoimmune antibodies:</strong> Lupus produces anti-nuclear antibodies (ANA), anti-dsDNA, and other autoantibodies that are present in plasma</li>
<li><strong>Plasma quality concern:</strong> These antibodies could theoretically transfer to plasma recipients</li>
<li><strong>Flare risk:</strong> Plasma donation could potentially trigger a lupus flare by stressing the immune system</li>
<li><strong>Most centers defer:</strong> CSL Plasma, BioLife, and Octapharma generally defer SLE patients</li>
</ul>

<h3>Rheumatoid Arthritis — Depends</h3>

<p>RA eligibility varies more than lupus because the spectrum of disease severity is broader:</p>

<ul>
<li><strong>Mild, well-controlled RA:</strong> Some centers accept donors on hydroxychloroquine alone for mild RA</li>
<li><strong>Moderate to severe RA:</strong> More likely to be deferred, especially if on additional immunosuppressants</li>
<li><strong>Combination therapy:</strong> If you take hydroxychloroquine plus methotrexate, biologics, or JAK inhibitors, the immunosuppressive medications will likely defer you</li>
<li><strong>Disease activity matters:</strong> Centers assess current symptoms, not just diagnosis</li>
</ul>

<h3>Malaria Prophylaxis — Deferral Period</h3>

<p>If you take hydroxychloroquine for malaria prevention while traveling, the deferral is not about the medication — it is about potential malaria exposure:</p>

<ul>
<li><strong>During travel:</strong> Cannot donate while in a malaria-endemic area</li>
<li><strong>After return:</strong> Most centers require a 3-year deferral after returning from a malaria-endemic area</li>
<li><strong>No malaria symptoms:</strong> You must remain symptom-free throughout the deferral period</li>
<li><strong>Documentation:</strong> Some centers may ask about travel dates and destinations</li>
</ul>

<h2 id="how-it-works">How Hydroxychloroquine Affects Plasma</h2>

<p>Understanding the pharmacology helps explain why the medication itself is not the problem.</p>

<h3>What Hydroxychloroquine Does</h3>

<ul>
<li><strong>Immunomodulator, not immunosuppressant:</strong> Hydroxychloroquine modulates the immune response rather than suppressing it outright</li>
<li><strong>Does not deplete clotting factors:</strong> Unlike blood thinners, HCQ does not affect coagulation proteins</li>
<li><strong>Long half-life:</strong> HCQ has a half-life of 40 - 50 days, so it is always present in your plasma if you take it regularly</li>
<li><strong>Trace amounts in plasma:</strong> The drug concentration in donated plasma is minimal and does not affect manufacturing processes</li>
</ul>

<h3>Why the Underlying Condition Matters More</h3>

<p>The reason centers focus on the diagnosis rather than the medication:</p>

<ul>
<li><strong>Autoimmune antibodies:</strong> Lupus and other autoimmune conditions produce pathological antibodies that are dissolved in plasma</li>
<li><strong>Plasma product safety:</strong> Autoantibodies in donated plasma could theoretically affect the safety of manufactured immunoglobulin (IVIG) products</li>
<li><strong>Donor safety:</strong> Autoimmune patients may have compromised immune systems that make donation riskier</li>
<li><strong>Flare prevention:</strong> The physical stress of donation could trigger disease flares</li>
</ul>

{AFFILIATE_BLOCK}

<h2 id="center-policies">Center-by-Center Hydroxychloroquine Policies</h2>

<table>
<thead>
<tr><th>Center</th><th>Lupus (SLE)</th><th>Rheumatoid Arthritis</th><th>Malaria Prophylaxis</th></tr>
</thead>
<tbody>
<tr><td>CSL Plasma</td><td>Deferred</td><td>Case by case</td><td>3-year deferral post-travel</td></tr>
<tr><td>BioLife</td><td>Deferred</td><td>Case by case</td><td>3-year deferral post-travel</td></tr>
<tr><td>Octapharma</td><td>Deferred</td><td>May defer</td><td>3-year deferral post-travel</td></tr>
<tr><td>Grifols / Biomat</td><td>Deferred</td><td>Case by case</td><td>3-year deferral post-travel</td></tr>
<tr><td>KEDPlasma</td><td>Deferred</td><td>Case by case</td><td>3-year deferral post-travel</td></tr>
</tbody>
</table>

<h2 id="screening-tips">Screening Tips for Hydroxychloroquine Users</h2>

<ol>
<li><strong>Know your diagnosis:</strong> Be prepared to clearly state why you take hydroxychloroquine — the indication is what matters most</li>
<li><strong>Bring documentation:</strong> A letter from your rheumatologist or primary care physician stating your diagnosis and disease status helps</li>
<li><strong>List all medications:</strong> If you take hydroxychloroquine in combination with other medications (methotrexate, prednisone, biologics), list them all — the combination may be more deferring than HCQ alone</li>
<li><strong>Describe disease activity:</strong> "Mild RA, well-controlled" is very different from "active lupus with flares" in terms of eligibility</li>
<li><strong>For malaria prophylaxis:</strong> Be ready to provide travel dates and destinations; the deferral clock starts when you return</li>
</ol>

{PRO_TOOLKIT}

<h2 id="timing">Timing and Special Considerations</h2>

<h3>If You Have Rheumatoid Arthritis</h3>

<ul>
<li><strong>Donate during remission:</strong> If your RA is in remission or very well-controlled, you have the best chance of acceptance</li>
<li><strong>Avoid flare periods:</strong> Do not attempt to donate during an active flare — you will be deferred and the physical stress could worsen your symptoms</li>
<li><strong>Monotherapy advantage:</strong> If hydroxychloroquine is your only RA medication, you are more likely to be accepted than if you are on combination therapy</li>
</ul>

<h3>If You Take HCQ for Malaria Prevention</h3>

<ul>
<li><strong>Donate before travel:</strong> You can donate normally before your trip if you have not yet traveled to an endemic area</li>
<li><strong>3-year waiting period:</strong> After returning from a malaria-endemic area, you must wait 3 years before donating plasma</li>
<li><strong>Keep travel records:</strong> Documentation of when and where you traveled helps the center determine your eligibility date</li>
</ul>

<h3>If You Have Lupus (SLE)</h3>

<p>Unfortunately, most lupus patients are permanently deferred from plasma donation regardless of disease activity or medication regimen. This is due to the persistent autoantibodies (ANA, anti-dsDNA) that remain in your plasma even during remission. Alternative options include:</p>

<ul>
<li><strong>Whole blood donation:</strong> Some blood banks may accept lupus patients during remission</li>
<li><strong>Clinical trials:</strong> Research studies sometimes specifically recruit autoimmune patients</li>
<li><strong>Referral bonuses:</strong> Most plasma centers pay $50 - $100 per successful referral</li>
</ul>

{related_reading([
    ('/blog/can-you-donate-plasma-on-antibiotics-2026.html', 'Can You Donate Plasma on Antibiotics?'),
    ('/blog/can-you-donate-plasma-on-antidepressants-2026.html', 'Can You Donate Plasma on Antidepressants?'),
    ('/blog/how-to-avoid-plasma-deferral-2026.html', 'How to Avoid Plasma Deferral'),
    ('/blog/plasma-donation-day-before-checklist-2026.html', 'Day-Before Checklist'),
])}

<h2 id="faq">Frequently Asked Questions</h2>

<h3>Can I donate plasma if I have lupus but it is in remission?</h3>
<p>Most centers still defer lupus patients even during remission. The concern is not disease activity but the autoantibodies (ANA, anti-dsDNA) that persist in your plasma regardless of symptom status. These antibodies could affect manufactured plasma products. Some centers may make exceptions for long-term remission, but this is rare.</p>

<h3>Is hydroxychloroquine considered an immunosuppressant for plasma donation purposes?</h3>
<p>No. Hydroxychloroquine is classified as an immunomodulator, not an immunosuppressant. It modifies how the immune system functions without broadly suppressing it. This is why the medication itself is typically not disqualifying — it is the underlying autoimmune condition that usually causes the deferral.</p>

<h3>I take Plaquenil for rheumatoid arthritis — can I donate?</h3>
<p>Possibly. RA eligibility depends on disease severity, current activity level, and whether you take additional medications. If your RA is mild and well-controlled on hydroxychloroquine alone, many centers will consider you. If you are on combination therapy with methotrexate or biologics, you are more likely to be deferred.</p>

<h3>How long after returning from a malaria zone can I donate plasma?</h3>
<p>Most plasma centers require a 3-year deferral after returning from a malaria-endemic area, regardless of whether you took prophylaxis. This is an FDA-aligned guideline based on the potential for asymptomatic malaria parasitemia. The clock starts from your last day in the endemic region.</p>

<h3>What if I took hydroxychloroquine during COVID and no longer take it?</h3>
<p>If you took hydroxychloroquine temporarily and no longer take it, you are not deferred for the medication. The key question is why you took it. If it was prescribed for COVID treatment (not an autoimmune condition), and you have fully recovered with no ongoing complications, most centers will accept you after a standard post-illness recovery period (typically 14 - 28 days after symptom resolution).</p>

{footer_related()}
'''

hcq_faqs = [
    make_faq("Can I donate plasma if I have lupus but it is in remission?",
             "Most centers still defer lupus patients even during remission because autoantibodies persist in plasma regardless of symptom status."),
    make_faq("Is hydroxychloroquine considered an immunosuppressant for plasma donation purposes?",
             "No. Hydroxychloroquine is an immunomodulator, not an immunosuppressant. The medication itself is typically not disqualifying — the underlying condition usually causes the deferral."),
    make_faq("I take Plaquenil for rheumatoid arthritis — can I donate?",
             "Possibly. If your RA is mild and well-controlled on hydroxychloroquine alone, many centers will consider you. Combination therapy with methotrexate or biologics makes deferral more likely."),
    make_faq("How long after returning from a malaria zone can I donate plasma?",
             "Most centers require a 3-year deferral after returning from a malaria-endemic area, regardless of whether you took prophylaxis."),
    make_faq("What if I took hydroxychloroquine during COVID and no longer take it?",
             "If you no longer take it and have fully recovered, most centers accept you after a standard post-illness recovery period (14-28 days after symptom resolution)."),
]

# ============================================================
# Generate all 4 pages
# ============================================================

PAGES = [
    {
        'slug': lithium_slug,
        'title': lithium_title,
        'meta': lithium_meta,
        'category': 'Medical Eligibility',
        'read_time': 10,
        'toc': TOC_ITEMS,
        'content': lithium_content,
        'faqs': lithium_faqs,
    },
    {
        'slug': warfarin_slug,
        'title': warfarin_title,
        'meta': warfarin_meta,
        'category': 'Medical Eligibility',
        'read_time': 11,
        'toc': TOC_ITEMS,
        'content': warfarin_content,
        'faqs': warfarin_faqs,
    },
    {
        'slug': muscle_slug,
        'title': muscle_title,
        'meta': muscle_meta,
        'category': 'Medical Eligibility',
        'read_time': 10,
        'toc': TOC_ITEMS,
        'content': muscle_content,
        'faqs': muscle_faqs,
    },
    {
        'slug': hcq_slug,
        'title': hcq_title,
        'meta': hcq_meta,
        'category': 'Medical Eligibility',
        'read_time': 11,
        'toc': TOC_ITEMS,
        'content': hcq_content,
        'faqs': hcq_faqs,
    },
]

if __name__ == '__main__':
    print(f"Generating Round 3 Meds Batch 3: {len(PAGES)} medication eligibility pages...")
    for p in PAGES:
        html = make_en_page(
            p['slug'], p['title'], p['meta'], p['category'],
            p['read_time'], p['toc'], p['content'], p['faqs'],
        )
        filepath = os.path.join(BLOG_DIR, f"{p['slug']}.html")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"  Created: blog/{p['slug']}.html")
    print(f"Done! Generated {len(PAGES)} pages.")
