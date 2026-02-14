#!/usr/bin/env python3
"""
Generate Round 2 Batch 1: Medical Condition Plasma Donation Eligibility Pages
15 pages covering specific medical conditions and medication interactions
"""

import os
from generate_batch1_centers import make_en_page, make_faq, AFFILIATE_BLOCK, PRO_TOOLKIT, related_reading, footer_related

BLOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'blog')

# Ensure blog directory exists
os.makedirs(BLOG_DIR, exist_ok=True)

# Page configurations
PAGES = [
    {
        'slug': 'can-you-donate-plasma-with-uti-2026',
        'title': 'Can You Donate Plasma With a UTI? [2026 Eligibility Guide]',
        'meta': 'Active UTI = automatic deferral. Learn waiting periods, antibiotic restrictions, and when you can safely donate plasma after urinary tract infection treatment.',
        'category': 'Medical Eligibility',
        'read_time': 7,
        'toc': [
            ('quick-answer', 'Quick Answer'),
            ('eligibility', 'UTI and Plasma Donation Eligibility'),
            ('antibiotics', 'Antibiotic Medications and Deferral'),
            ('screening', 'What to Tell Screening Staff'),
            ('waiting-period', 'How Long to Wait After UTI'),
            ('prevention', 'UTI Prevention Tips for Donors'),
        ],
        'content': f'''
<div class="quick-answer">
<h3>Quick Answer: Can You Donate Plasma With a UTI?</h3>
<p><strong>No, you cannot donate plasma with an active urinary tract infection.</strong> All plasma donation centers defer donors with active infections to protect both the donor and plasma recipients. You must complete antibiotic treatment and be symptom-free for at least 14 days before donating.</p>
</div>

<h2 id="eligibility">UTI and Plasma Donation Eligibility</h2>

<p>Urinary tract infections create an automatic deferral from plasma donation for several important medical reasons:</p>

<h3>Why UTIs Disqualify You</h3>

<ul>
<li><strong>Active infection risk:</strong> Bacteria from UTIs can enter the bloodstream during the donation process</li>
<li><strong>Weakened immune response:</strong> Your body is fighting the infection and needs its full plasma volume</li>
<li><strong>Medication complications:</strong> Antibiotics used to treat UTIs have deferral periods</li>
<li><strong>Protein levels:</strong> Infections can temporarily alter plasma protein composition</li>
</ul>

<h3>When You're Deferred</h3>

<p>You cannot donate if you have:</p>

<ul>
<li>Current UTI symptoms (burning, frequent urination, pelvic pain)</li>
<li>Active antibiotic treatment for UTI</li>
<li>Completed antibiotics less than 14 days ago</li>
<li>Fever or chills related to the infection</li>
<li>Blood in urine (hematuria)</li>
<li>Kidney involvement (pyelonephritis)</li>
</ul>

{AFFILIATE_BLOCK}

<h2 id="antibiotics">Antibiotic Medications and Deferral</h2>

<p>Common UTI antibiotics and their typical deferral periods:</p>

<table>
<thead>
<tr>
<th>Antibiotic</th>
<th>Common Brand Names</th>
<th>Minimum Wait After Last Dose</th>
</tr>
</thead>
<tbody>
<tr>
<td>Trimethoprim-sulfamethoxazole</td>
<td>Bactrim, Septra</td>
<td>14 days</td>
</tr>
<tr>
<td>Nitrofurantoin</td>
<td>Macrobid, Macrodantin</td>
<td>14 days</td>
</tr>
<tr>
<td>Ciprofloxacin</td>
<td>Cipro</td>
<td>14 days</td>
</tr>
<tr>
<td>Levofloxacin</td>
<td>Levaquin</td>
<td>14 days</td>
</tr>
<tr>
<td>Cephalexin</td>
<td>Keflex</td>
<td>14 days</td>
</tr>
<tr>
<td>Amoxicillin</td>
<td>Amoxil</td>
<td>14 days</td>
</tr>
</tbody>
</table>

<p><strong>Important:</strong> The 14-day waiting period starts from your <em>last dose</em> of antibiotics, not from when symptoms began.</p>

<h3>Why Antibiotics Matter</h3>

<ul>
<li><strong>Drug contamination:</strong> Antibiotics in your plasma could affect recipients</li>
<li><strong>Incomplete treatment:</strong> Ensures infection is fully cleared before donation</li>
<li><strong>Side effects:</strong> Donation could worsen antibiotic-related dehydration or dizziness</li>
</ul>

<h2 id="screening">What to Tell Screening Staff</h2>

<p>Be completely honest during your screening interview. Staff needs to know:</p>

<h3>Information to Provide</h3>

<ol>
<li><strong>Infection history:</strong> When did UTI symptoms start?</li>
<li><strong>Treatment details:</strong> What antibiotic were you prescribed?</li>
<li><strong>Last dose date:</strong> When did you finish the medication?</li>
<li><strong>Current symptoms:</strong> Are you completely symptom-free?</li>
<li><strong>Recurrent UTIs:</strong> How often do you get infections?</li>
<li><strong>Kidney involvement:</strong> Did the infection spread to kidneys?</li>
</ol>

{PRO_TOOLKIT}

<h3>Questions Staff Will Ask</h3>

<ul>
<li>"Have you had any infections in the past 30 days?"</li>
<li>"Are you currently taking or have you recently taken antibiotics?"</li>
<li>"When was your last dose of medication?"</li>
<li>"Do you have any urinary symptoms today?"</li>
</ul>

<p><strong>Pro tip:</strong> Bring documentation of your antibiotic prescription and completion date to speed up the screening process.</p>

<h2 id="waiting-period">How Long to Wait After UTI</h2>

<p>The standard waiting period depends on your treatment and recovery:</p>

<h3>Standard Timeline</h3>

<ul>
<li><strong>Simple UTI, oral antibiotics:</strong> 14 days after last antibiotic dose</li>
<li><strong>Complicated UTI:</strong> 14-30 days depending on severity</li>
<li><strong>Kidney infection (pyelonephritis):</strong> 30 days minimum, may require doctor clearance</li>
<li><strong>Recurrent UTIs (3+ per year):</strong> May need medical evaluation before donating</li>
<li><strong>Untreated UTI that resolved:</strong> Still 14 days after symptoms cleared</li>
</ul>

<h3>What Happens at Your Return Visit</h3>

<p>When you return after a UTI deferral:</p>

<ol>
<li><strong>Medical history review:</strong> Staff confirms infection has cleared</li>
<li><strong>Urinalysis:</strong> Some centers may check urine protein/blood</li>
<li><strong>Vital signs check:</strong> Ensures normal temperature and blood pressure</li>
<li><strong>Physical exam:</strong> Quick assessment of overall health</li>
<li><strong>Protein screening:</strong> Finger stick test to check plasma protein levels</li>
</ol>

<h2 id="prevention">UTI Prevention Tips for Donors</h2>

<p>Frequent plasma donors should take extra precautions to prevent UTIs:</p>

<h3>Before Donation</h3>

<ul>
<li><strong>Hydrate thoroughly:</strong> Drink 16-20 oz water 2-3 hours before donating</li>
<li><strong>Urinate before donation:</strong> Empty bladder completely</li>
<li><strong>Avoid caffeine:</strong> Can irritate the bladder</li>
<li><strong>Proper hygiene:</strong> Shower before your appointment</li>
</ul>

<h3>After Donation</h3>

<ul>
<li><strong>Drink extra fluids:</strong> 8-10 glasses of water over next 24 hours</li>
<li><strong>Urinate frequently:</strong> Don't hold urine for long periods</li>
<li><strong>Cranberry juice:</strong> May help prevent bacterial adhesion (unsweetened)</li>
<li><strong>Avoid irritants:</strong> Skip alcohol and spicy foods for 24 hours</li>
</ul>

<h3>Long-Term Prevention</h3>

<ul>
<li>Maintain 2-week spacing between donations when possible</li>
<li>Take probiotics to support urinary tract health</li>
<li>Wipe front to back (women)</li>
<li>Urinate after sexual activity</li>
<li>Wear breathable cotton underwear</li>
<li>Avoid harsh soaps in genital area</li>
</ul>

{related_reading([
    ('/blog/can-you-donate-plasma-with-kidney-disease-2026', 'Plasma Donation With Kidney Disease'),
    ('/blog/can-you-donate-plasma-on-antibiotics-full-guide', 'Complete Antibiotic Medication Guide'),
    ('/blog/plasma-donation-health-screening-what-to-expect', 'Health Screening Process Explained')
])}

{footer_related()}
''',
        'faqs': [
            make_faq(
                "Can I donate plasma if I get frequent UTIs?",
                "Yes, you can donate between infections as long as you're symptom-free and have completed the 14-day waiting period after each antibiotic treatment. However, if you have 3+ UTIs per year, some centers may require a doctor's note confirming you're healthy to donate. Frequent UTIs don't permanently disqualify you, but each infection creates a temporary deferral."
            ),
            make_faq(
                "What if I had a UTI but didn't take antibiotics?",
                "You still need to wait at least 14 days after symptoms completely resolve. Even without antibiotics, the infection and immune response affect your plasma quality. Some centers may require a urinalysis to confirm the infection has cleared. Never donate while experiencing any UTI symptoms, even mild ones."
            ),
            make_faq(
                "Will the plasma center test my urine for infection?",
                "Most centers don't routinely test urine unless you report recent UTI symptoms. However, they may perform a urinalysis if you mention recent infections, recurrent UTIs, or if your medical screening raises concerns. The standard finger-stick protein test can sometimes indicate kidney issues related to severe UTIs."
            ),
            make_faq(
                "Can dehydration from plasma donation cause a UTI?",
                "Dehydration itself doesn't cause UTIs, but it can increase your risk by concentrating urine and reducing how often you urinate. This is why hydration is critical for plasma donors. Drink at least 64 oz of water daily, with extra fluids on donation days. Proper hydration helps flush bacteria from your urinary tract."
            ),
            make_faq(
                "What if I develop UTI symptoms after donating plasma?",
                "Contact the plasma center immediately to report the infection. You'll be temporarily deferred from future donations until the UTI is treated and the waiting period passes. This doesn't affect the plasma you already donated (it goes through extensive testing and processing), but it helps the center track donor health patterns and may prompt them to check for other issues."
            ),
        ]
    },
    {
        'slug': 'can-you-donate-plasma-with-multiple-sclerosis-2026',
        'title': 'Can You Donate Plasma With Multiple Sclerosis (MS)? [2026 Rules]',
        'meta': 'MS diagnosis typically disqualifies plasma donation due to autoimmune factors and disease-modifying therapies. Complete eligibility guide for multiple sclerosis patients.',
        'category': 'Medical Eligibility',
        'read_time': 9,
        'toc': [
            ('quick-answer', 'Quick Answer'),
            ('why-deferred', 'Why MS Usually Disqualifies You'),
            ('medications', 'Disease-Modifying Therapies and Deferral'),
            ('exceptions', 'Rare Exceptions and Special Cases'),
            ('alternatives', 'Alternative Ways to Help'),
            ('research', 'MS Plasma Research Programs'),
        ],
        'content': f'''
<div class="quick-answer">
<h3>Quick Answer: Can You Donate Plasma With MS?</h3>
<p><strong>No, multiple sclerosis is a permanent deferral at most commercial plasma centers.</strong> The autoimmune nature of MS, along with the immunosuppressive and disease-modifying medications used to treat it, make plasma donation unsafe for both donors and recipients. However, some research programs specifically collect plasma from MS patients for antibody studies.</p>
</div>

<h2 id="why-deferred">Why MS Usually Disqualifies You</h2>

<p>Multiple sclerosis creates several medical barriers to plasma donation:</p>

<h3>Autoimmune Disease Concerns</h3>

<ul>
<li><strong>Abnormal antibodies:</strong> MS plasma contains autoantibodies that attack myelin proteins</li>
<li><strong>Immune dysregulation:</strong> Altered immune markers could affect plasma recipients</li>
<li><strong>Inflammatory proteins:</strong> Elevated cytokines and inflammatory factors in plasma</li>
<li><strong>Safety uncertainty:</strong> Long-term effects of MS antibodies on recipients unknown</li>
</ul>

<h3>Donor Safety Concerns</h3>

<p>Plasma donation could worsen MS symptoms through:</p>

<ul>
<li><strong>Immune stress:</strong> Donation temporarily reduces immune factors needed for disease management</li>
<li><strong>Fatigue exacerbation:</strong> MS-related fatigue severely worsened by plasma loss</li>
<li><strong>Heat sensitivity:</strong> Donation can raise body temperature, triggering MS symptoms (Uhthoff's phenomenon)</li>
<li><strong>Dehydration risk:</strong> Fluid loss may worsen MS-related bladder control issues</li>
<li><strong>Medication complications:</strong> DMTs interact with the donation process</li>
</ul>

{AFFILIATE_BLOCK}

<h2 id="medications">Disease-Modifying Therapies and Deferral</h2>

<p>All disease-modifying therapies (DMTs) for MS are disqualifying medications for plasma donation:</p>

<h3>Injectable DMTs (Permanent Deferral)</h3>

<table>
<thead>
<tr>
<th>Medication</th>
<th>Brand Name</th>
<th>Why It Disqualifies</th>
</tr>
</thead>
<tbody>
<tr>
<td>Interferon beta-1a</td>
<td>Avonex, Rebif</td>
<td>Immunomodulator, alters plasma proteins</td>
</tr>
<tr>
<td>Interferon beta-1b</td>
<td>Betaseron, Extavia</td>
<td>Immunomodulator, affects cytokine levels</td>
</tr>
<tr>
<td>Glatiramer acetate</td>
<td>Copaxone, Glatopa</td>
<td>Immune modulation, myelin effects</td>
</tr>
<tr>
<td>Peginterferon beta-1a</td>
<td>Plegridy</td>
<td>Long-acting immunomodulator</td>
</tr>
</tbody>
</table>

<h3>Oral DMTs (Permanent Deferral)</h3>

<table>
<thead>
<tr>
<th>Medication</th>
<th>Brand Name</th>
<th>Why It Disqualifies</th>
</tr>
</thead>
<tbody>
<tr>
<td>Fingolimod</td>
<td>Gilenya</td>
<td>Immunosuppressant, lymphocyte sequestration</td>
</tr>
<tr>
<td>Dimethyl fumarate</td>
<td>Tecfidera</td>
<td>Immune modulation, lymphocyte reduction</td>
</tr>
<tr>
<td>Teriflunomide</td>
<td>Aubagio</td>
<td>Immunosuppressant, teratogenic metabolites</td>
</tr>
<tr>
<td>Siponimod</td>
<td>Mayzent</td>
<td>Lymphocyte sequestration</td>
</tr>
<tr>
<td>Ozanimod</td>
<td>Zeposia</td>
<td>Immunosuppressant effects</td>
</tr>
<tr>
<td>Ponesimod</td>
<td>Ponvory</td>
<td>S1P receptor modulator</td>
</tr>
<tr>
<td>Diroximel fumarate</td>
<td>Vumerity</td>
<td>Immune modulation</td>
</tr>
</tbody>
</table>

<h3>Infusion DMTs (Permanent Deferral)</h3>

<table>
<thead>
<tr>
<th>Medication</th>
<th>Brand Name</th>
<th>Why It Disqualifies</th>
</tr>
</thead>
<tbody>
<tr>
<td>Natalizumab</td>
<td>Tysabri</td>
<td>Monoclonal antibody, PML risk</td>
</tr>
<tr>
<td>Ocrelizumab</td>
<td>Ocrevus</td>
<td>B-cell depleting antibody</td>
</tr>
<tr>
<td>Alemtuzumab</td>
<td>Lemtrada</td>
<td>Severe immunosuppression</td>
</tr>
<tr>
<td>Mitoxantrone</td>
<td>Novantrone</td>
<td>Chemotherapy agent, cardiotoxic</td>
</tr>
<tr>
<td>Ofatumumab</td>
<td>Kesimpta</td>
<td>B-cell depleting antibody</td>
</tr>
</tbody>
</table>

{PRO_TOOLKIT}

<h3>Symptom Management Medications</h3>

<p>Some MS symptom treatments are also disqualifying:</p>

<ul>
<li><strong>Corticosteroids (during active use):</strong> Prednisone, methylprednisolone for relapses</li>
<li><strong>Muscle relaxants:</strong> Some formulations may cause deferral</li>
<li><strong>Immunosuppressants:</strong> Azathioprine, methotrexate (off-label MS use)</li>
</ul>

<h2 id="exceptions">Rare Exceptions and Special Cases</h2>

<h3>Theoretical Donation Scenarios (Highly Unlikely)</h3>

<p>In extremely rare cases, you might be considered if:</p>

<ul>
<li><strong>Clinically isolated syndrome (CIS):</strong> Single demyelinating episode, no MS diagnosis, not on DMTs</li>
<li><strong>Radiologically isolated syndrome (RIS):</strong> MRI findings without clinical symptoms or diagnosis</li>
<li><strong>Long-term remission off all medications:</strong> Some centers might consider after 5+ years medication-free with neurologist clearance (very rare)</li>
</ul>

<p><strong>Reality check:</strong> Even in these scenarios, most commercial plasma centers maintain permanent deferral policies for anyone with MS on their medical record due to liability and recipient safety concerns.</p>

<h3>What Screening Staff Will Do</h3>

<ol>
<li><strong>Medical history:</strong> Ask about autoimmune diseases</li>
<li><strong>Medication review:</strong> Screen for all DMTs and immunosuppressants</li>
<li><strong>Diagnosis confirmation:</strong> Verify MS diagnosis and treatment history</li>
<li><strong>Permanent deferral:</strong> Enter into database to prevent future donation attempts</li>
</ol>

<h2 id="alternatives">Alternative Ways to Help</h2>

<p>If you can't donate plasma due to MS, consider these alternatives:</p>

<h3>Direct Support Options</h3>

<ul>
<li><strong>Volunteer time:</strong> Help at plasma centers with administrative tasks or donor support</li>
<li><strong>Awareness campaigns:</strong> Encourage eligible friends and family to donate</li>
<li><strong>Financial donations:</strong> Support plasma-dependent patient organizations</li>
<li><strong>Social media advocacy:</strong> Share information about plasma donation importance</li>
</ul>

<h3>MS-Specific Contributions</h3>

<ul>
<li><strong>Research participation:</strong> Join MS clinical trials and observational studies</li>
<li><strong>Biobank donation:</strong> Contribute blood/plasma to MS research biorepositories</li>
<li><strong>Survey participation:</strong> Help researchers understand MS patient experiences</li>
<li><strong>Genetic studies:</strong> Contribute DNA samples for MS genetics research</li>
</ul>

<h2 id="research">MS Plasma Research Programs</h2>

<p>While you can't donate commercially, your MS plasma is valuable for research:</p>

<h3>Research Organizations Collecting MS Plasma</h3>

<ul>
<li><strong>National MS Society Biorepository:</strong> Collects samples for approved research projects</li>
<li><strong>NMSS EPIC (Epitope-spreading in MS) Study:</strong> Antibody profiling research</li>
<li><strong>iConquerMS:</strong> Patient-powered research network with biobanking</li>
<li><strong>University MS Centers:</strong> Many academic centers collect samples for specific studies</li>
</ul>

<h3>What Research Programs Study</h3>

<ul>
<li>Autoantibody profiles and disease progression markers</li>
<li>Biomarkers for treatment response prediction</li>
<li>Differences between relapsing-remitting and progressive MS</li>
<li>Genetic factors combined with antibody studies</li>
<li>Development of new diagnostic tests</li>
</ul>

<h3>How to Participate</h3>

<ol>
<li><strong>Ask your neurologist:</strong> Many MS specialists partner with research programs</li>
<li><strong>Contact MS Society:</strong> Call 1-800-344-4867 for research opportunities</li>
<li><strong>Check ClinicalTrials.gov:</strong> Search "multiple sclerosis biobank" or "MS plasma study"</li>
<li><strong>University MS centers:</strong> Contact academic medical centers in your area</li>
</ol>

<p><strong>Benefits of research donation:</strong> You contribute to MS treatment advancement while receiving no compensation (research studies don't pay for samples, unlike commercial plasma donation).</p>

{related_reading([
    ('/blog/can-you-donate-plasma-with-lupus-2026', 'Plasma Donation With Lupus (SLE)'),
    ('/blog/can-you-donate-plasma-with-arthritis-2026', 'Rheumatoid Arthritis and Plasma Donation'),
    ('/blog/autoimmune-disease-plasma-donation-guide', 'Complete Autoimmune Disease Guide')
])}

{footer_related()}
''',
        'faqs': [
            make_faq(
                "Can I donate plasma if I only had one MS episode years ago?",
                "It depends on your formal diagnosis and current treatment. If you were diagnosed with MS and are on any disease-modifying therapy, you cannot donate. If you had clinically isolated syndrome (CIS) without progressing to MS diagnosis and are medication-free, some centers might consider you—but this is rare. Most centers apply permanent deferral to anyone with MS-related diagnoses due to recipient safety concerns."
            ),
            make_faq(
                "What if I stopped my MS medication to donate plasma?",
                "Never stop MS medication to donate plasma. This is medically dangerous and still wouldn't qualify you—most centers permanently defer anyone with an MS diagnosis regardless of current treatment status. Disease-modifying therapies prevent relapses and slow progression; stopping them risks serious neurological damage. The small compensation from plasma donation isn't worth risking your long-term health."
            ),
            make_faq(
                "Will my MS be detected during plasma screening if I don't mention it?",
                "Possibly. While standard screening doesn't include neurological exams, the medical history questionnaire asks about autoimmune diseases and chronic neurological conditions. Lying on screening forms is fraudulent and dangerous—MS antibodies and medication markers in your plasma could harm recipients. All plasma undergoes extensive testing that may detect abnormalities. Centers permanently ban donors who provide false medical information."
            ),
            make_faq(
                "Can someone with MS donate blood instead of plasma?",
                "No, the same restrictions apply to whole blood donation. The American Red Cross and other blood banks defer people with MS due to autoimmune factors and immunosuppressive medications. However, you may be able to donate to MS-specific research biobanks, which collect blood samples specifically for multiple sclerosis studies rather than therapeutic use."
            ),
            make_faq(
                "Are there any countries where MS patients can donate plasma?",
                "Plasma donation eligibility criteria are fairly consistent across developed nations due to international safety standards. The United States, Canada, European Union countries, and Australia all defer donors with autoimmune diseases including MS. This isn't discrimination—it's based on recipient safety and the unknown effects of autoimmune antibodies in plasma-derived medications."
            ),
        ]
    },
    {
        'slug': 'can-you-donate-plasma-with-psoriasis-2026',
        'title': 'Can You Donate Plasma With Psoriasis? [2026 Medication Guide]',
        'meta': 'Psoriasis alone doesn\'t disqualify you, but many treatments do. Complete guide to biologics, immunosuppressants, and when you can donate with psoriatic disease.',
        'category': 'Medical Eligibility',
        'read_time': 8,
        'toc': [
            ('quick-answer', 'Quick Answer'),
            ('mild-psoriasis', 'Mild Psoriasis and Topical Treatments'),
            ('biologics', 'Biologic Medications (Disqualifying)'),
            ('systemics', 'Oral Systemic Medications'),
            ('screening', 'What Screening Staff Will Check'),
            ('tips', 'Donation Tips for Psoriasis Patients'),
        ],
        'content': f'''
<div class="quick-answer">
<h3>Quick Answer: Can You Donate Plasma With Psoriasis?</h3>
<p><strong>It depends on your treatment.</strong> Psoriasis itself doesn't disqualify you, but most systemic medications do—especially biologics and immunosuppressants. If you manage your psoriasis with only topical creams and phototherapy, you can usually donate. Anyone on Humira, Enbrel, Stelara, or other biologics is permanently deferred.</p>
</div>

<h2 id="mild-psoriasis">Mild Psoriasis and Topical Treatments</h2>

<p>Good news: Mild to moderate psoriasis managed with topical treatments generally doesn't prevent plasma donation.</p>

<h3>Acceptable Treatments (You CAN Donate)</h3>

<table>
<thead>
<tr>
<th>Treatment Type</th>
<th>Examples</th>
<th>Donation Status</th>
</tr>
</thead>
<tbody>
<tr>
<td>Topical corticosteroids</td>
<td>Clobetasol, betamethasone, triamcinolone</td>
<td>✓ Allowed</td>
</tr>
<tr>
<td>Vitamin D analogs</td>
<td>Calcipotriene (Dovonex), calcitriol</td>
<td>✓ Allowed</td>
</tr>
<tr>
<td>Topical retinoids</td>
<td>Tazarotene (Tazorac)</td>
<td>✓ Allowed</td>
</tr>
<tr>
<td>Moisturizers/emollients</td>
<td>CeraVe, Cetaphil, petroleum jelly</td>
<td>✓ Allowed</td>
</tr>
<tr>
<td>Coal tar products</td>
<td>MG217, Neutrogena T/Gel</td>
<td>✓ Allowed</td>
</tr>
<tr>
<td>Salicylic acid</td>
<td>Over-the-counter scale removers</td>
<td>✓ Allowed</td>
</tr>
<tr>
<td>Phototherapy (UVB)</td>
<td>Narrowband UVB, PUVA</td>
<td>✓ Usually allowed</td>
</tr>
</tbody>
</table>

<h3>Skin Condition Requirements</h3>

<p>Your skin lesions must meet these criteria on donation day:</p>

<ul>
<li><strong>No active bleeding:</strong> Plaques must be dry and intact</li>
<li><strong>Minimal on arms:</strong> Venipuncture site area should be clear of lesions</li>
<li><strong>No infection:</strong> No signs of secondary bacterial infection</li>
<li><strong>Stable condition:</strong> Not experiencing a major flare-up</li>
</ul>

{AFFILIATE_BLOCK}

<h2 id="biologics">Biologic Medications (Disqualifying)</h2>

<p>All biologic medications for psoriasis create a <strong>permanent deferral</strong> from plasma donation:</p>

<h3>TNF-Alpha Inhibitors (Permanent Deferral)</h3>

<table>
<thead>
<tr>
<th>Medication</th>
<th>Brand Name</th>
<th>Administration</th>
</tr>
</thead>
<tbody>
<tr>
<td>Adalimumab</td>
<td>Humira</td>
<td>Injection every 2 weeks</td>
</tr>
<tr>
<td>Etanercept</td>
<td>Enbrel</td>
<td>Injection weekly or twice weekly</td>
</tr>
<tr>
<td>Infliximab</td>
<td>Remicade</td>
<td>IV infusion every 8 weeks</td>
</tr>
<tr>
<td>Certolizumab pegol</td>
<td>Cimzia</td>
<td>Injection every 2-4 weeks</td>
</tr>
</tbody>
</table>

<h3>IL-17 Inhibitors (Permanent Deferral)</h3>

<table>
<thead>
<tr>
<th>Medication</th>
<th>Brand Name</th>
<th>Administration</th>
</tr>
</thead>
<tbody>
<tr>
<td>Secukinumab</td>
<td>Cosentyx</td>
<td>Injection monthly</td>
</tr>
<tr>
<td>Ixekizumab</td>
<td>Taltz</td>
<td>Injection every 4 weeks</td>
</tr>
<tr>
<td>Brodalumab</td>
<td>Siliq</td>
<td>Injection every 2 weeks</td>
</tr>
</tbody>
</table>

<h3>IL-12/23 and IL-23 Inhibitors (Permanent Deferral)</h3>

<table>
<thead>
<tr>
<th>Medication</th>
<th>Brand Name</th>
<th>Administration</th>
</tr>
</thead>
<tbody>
<tr>
<td>Ustekinumab</td>
<td>Stelara</td>
<td>Injection every 12 weeks</td>
</tr>
<tr>
<td>Guselkumab</td>
<td>Tremfya</td>
<td>Injection every 8 weeks</td>
</tr>
<tr>
<td>Risankizumab</td>
<td>Skyrizi</td>
<td>Injection every 12 weeks</td>
</tr>
<tr>
<td>Tildrakizumab</td>
<td>Ilumya</td>
<td>Injection every 12 weeks</td>
</tr>
</tbody>
</table>

<h3>Why Biologics Disqualify You</h3>

<ul>
<li><strong>Immunosuppression:</strong> Biologics suppress specific immune pathways, affecting plasma quality</li>
<li><strong>Long half-life:</strong> Remain in bloodstream for weeks to months</li>
<li><strong>Antibody contamination:</strong> Monoclonal antibodies in your plasma could affect recipients</li>
<li><strong>Unknown recipient effects:</strong> Long-term safety of biologic-containing plasma not established</li>
</ul>

{PRO_TOOLKIT}

<h2 id="systemics">Oral Systemic Medications</h2>

<p>Most oral systemic psoriasis medications are disqualifying:</p>

<h3>Immunosuppressants (Permanent Deferral)</h3>

<table>
<thead>
<tr>
<th>Medication</th>
<th>Brand Name</th>
<th>Why Disqualifying</th>
</tr>
</thead>
<tbody>
<tr>
<td>Methotrexate</td>
<td>Trexall, Rheumatrex</td>
<td>Immunosuppressant, chemotherapy agent</td>
</tr>
<tr>
<td>Cyclosporine</td>
<td>Neoral, Sandimmune</td>
<td>Strong immunosuppressant</td>
</tr>
<tr>
<td>Apremilast</td>
<td>Otezla</td>
<td>PDE4 inhibitor, immune modulation</td>
</tr>
</tbody>
</table>

<h3>Oral Retinoids (Check Center Policy)</h3>

<table>
<thead>
<tr>
<th>Medication</th>
<th>Brand Name</th>
<th>Typical Policy</th>
</tr>
</thead>
<tbody>
<tr>
<td>Acitretin</td>
<td>Soriatane</td>
<td>Usually permanent deferral (teratogenic)</td>
</tr>
</tbody>
</table>

<h3>JAK Inhibitors (Permanent Deferral)</h3>

<table>
<thead>
<tr>
<th>Medication</th>
<th>Brand Name</th>
<th>Indication</th>
</tr>
</thead>
<tbody>
<tr>
<td>Deucravacitinib</td>
<td>Sotyktu</td>
<td>Plaque psoriasis</td>
</tr>
</tbody>
</table>

<h2 id="screening">What Screening Staff Will Check</h2>

<p>When you disclose psoriasis, staff will need specific information:</p>

<h3>Questions to Expect</h3>

<ol>
<li><strong>"What medications do you currently use for psoriasis?"</strong></li>
<li><strong>"Are any of these injections or infusions?"</strong></li>
<li><strong>"When was your last dose of [medication name]?"</strong></li>
<li><strong>"Do you have psoriatic arthritis?"</strong> (may be on additional medications)</li>
<li><strong>"Is your psoriasis currently flaring?"</strong></li>
<li><strong>"Do you have lesions on your arms near the elbow?"</strong></li>
</ol>

<h3>Physical Exam Considerations</h3>

<p>Staff will examine your arm before insertion:</p>

<ul>
<li><strong>Venipuncture site inspection:</strong> Must be free of active lesions</li>
<li><strong>Skin integrity check:</strong> No open wounds or bleeding plaques</li>
<li><strong>Infection assessment:</strong> Ensure no signs of secondary bacterial infection</li>
<li><strong>Bruising risk:</strong> Psoriatic skin may bruise more easily</li>
</ul>

<h3>Information to Bring</h3>

<ul>
<li>Complete list of all psoriasis medications (topical and systemic)</li>
<li>Recent prescription details or pharmacy printout</li>
<li>Doctor's note if you recently stopped a biologic (though still likely deferred)</li>
</ul>

<h2 id="tips">Donation Tips for Psoriasis Patients</h2>

<p>If you're approved to donate with topical-only psoriasis treatment:</p>

<h3>Before Donation</h3>

<ul>
<li><strong>Moisturize well:</strong> Apply emollients 1-2 hours before (not immediately before venipuncture)</li>
<li><strong>Avoid new topicals:</strong> Don't try new treatments within 24 hours of donation</li>
<li><strong>Hydrate extra:</strong> Psoriasis can affect fluid balance; drink 20+ oz water</li>
<li><strong>Choose clear arms:</strong> Wear short sleeves so staff can assess both arms for best vein</li>
<li><strong>Skip phototherapy:</strong> Avoid UV treatment on donation day (can cause fatigue)</li>
</ul>

<h3>During Donation</h3>

<ul>
<li><strong>Communicate discomfort:</strong> Tell staff if needle site stings more than expected</li>
<li><strong>Protect skin:</strong> Request extra care with tape removal (psoriatic skin can tear)</li>
<li><strong>Stay warm:</strong> Bring layers (cold can trigger psoriasis flares in some people)</li>
</ul>

<h3>After Donation</h3>

<ul>
<li><strong>Gentle bandage removal:</strong> Soak adhesive with oil if needed to prevent skin damage</li>
<li><strong>Monitor puncture site:</strong> Watch for delayed bleeding or plaque formation</li>
<li><strong>Extra moisturizing:</strong> Donation can be dehydrating; increase topical care</li>
<li><strong>Avoid stress:</strong> Rest well to prevent stress-triggered flares</li>
<li><strong>Continue medications:</strong> Maintain your regular topical treatment schedule</li>
</ul>

<h3>Long-Term Donation Considerations</h3>

<ul>
<li><strong>Vein health:</strong> Frequent donations may cause vein scarring; rotate arms</li>
<li><strong>Flare management:</strong> If you need to start systemic meds, you'll become ineligible</li>
<li><strong>Arthritis development:</strong> Up to 30% of psoriasis patients develop psoriatic arthritis, which may require biologics</li>
</ul>

<h3>When to Skip Donation</h3>

<p>Don't donate if you're experiencing:</p>

<ul>
<li>Active psoriasis flare with widespread new lesions</li>
<li>Guttate psoriasis triggered by strep throat (wait until cleared)</li>
<li>Secondary skin infection requiring antibiotics</li>
<li>Recent start of new systemic medication</li>
<li>Psoriatic arthritis joint pain or swelling</li>
</ul>

{related_reading([
    ('/blog/can-you-donate-plasma-with-lupus-2026', 'Lupus and Plasma Donation'),
    ('/blog/can-you-donate-plasma-with-arthritis-2026', 'Arthritis Medication Guide'),
    ('/blog/can-you-donate-plasma-on-biologics-complete-guide', 'Complete Biologic Medications Guide')
])}

{footer_related()}
''',
        'faqs': [
            make_faq(
                "Can I donate if I stopped my biologic medication?",
                "Most centers maintain permanent deferral even after stopping biologics because you have a chronic autoimmune condition that required immunosuppressive therapy. Some centers might consider you after 12+ months off biologics with dermatologist clearance, but this is rare. Never stop prescribed medication just to donate plasma—biologics prevent disease progression and stopping them risks severe flares."
            ),
            make_faq(
                "Will plasma donation make my psoriasis worse?",
                "Donation shouldn't directly worsen psoriasis, but dehydration and stress from the process could potentially trigger flares in some people. If you're approved to donate (topical treatments only), stay well-hydrated, get adequate rest, and maintain your regular skincare routine. Some donors report no impact on their psoriasis, while others notice temporary flare-ups after donation."
            ),
            make_faq(
                "What if I only use my biologic during bad flares?",
                "Even intermittent biologic use disqualifies you from plasma donation. The medications remain in your system for weeks to months after each dose, and centers can't accommodate on-and-off treatment schedules. If you're prescribed a biologic, you should be using it regularly as directed—intermittent use is generally not recommended by dermatologists and won't clear you for donation."
            ),
            make_faq(
                "Can I donate if I have psoriatic arthritis but no skin symptoms?",
                "It depends entirely on your medication. Psoriatic arthritis is typically treated with the same biologics and DMARDs that disqualify you from donation. If you manage PsA with only NSAIDs (ibuprofen, naproxen) and don't have active joint inflammation, you might be eligible, but this is uncommon—most PsA patients need stronger medications that create permanent deferral."
            ),
            make_faq(
                "Do I need a doctor's note to donate with psoriasis?",
                "Generally no, if you're only using topical treatments and your skin is stable. However, some centers may request a note from your dermatologist if you have extensive psoriasis coverage, recent flares, or if you recently stopped a systemic medication. Call ahead to ask about specific documentation requirements for autoimmune skin conditions."
            ),
        ]
    },
    {
        'slug': 'can-you-donate-plasma-with-lupus-2026',
        'title': 'Can You Donate Plasma With Lupus (SLE)? [2026 Complete Guide]',
        'meta': 'Lupus diagnosis creates permanent deferral at plasma centers due to autoimmune antibodies and immunosuppressive treatments. Full eligibility guide for SLE patients.',
        'category': 'Medical Eligibility',
        'read_time': 9,
        'toc': [
            ('quick-answer', 'Quick Answer'),
            ('why-deferred', 'Why Lupus Disqualifies You'),
            ('medications', 'Lupus Medications and Deferral'),
            ('antiphospholipid', 'Antiphospholipid Syndrome Concerns'),
            ('research', 'Donating Plasma for Lupus Research'),
            ('alternatives', 'Alternative Ways to Contribute'),
        ],
        'content': f'''
<div class="quick-answer">
<h3>Quick Answer: Can You Donate Plasma With Lupus?</h3>
<p><strong>No, systemic lupus erythematosus (SLE) is a permanent deferral at all commercial plasma donation centers.</strong> Lupus is an autoimmune disease that produces abnormal antibodies, including anti-nuclear antibodies (ANA) and potentially anti-phospholipid antibodies, which make donated plasma unsuitable for therapeutic use. Additionally, all lupus medications—from hydroxychloroquine to immunosuppressants—are disqualifying.</p>
</div>

<h2 id="why-deferred">Why Lupus Disqualifies You</h2>

<p>Systemic lupus erythematosus creates multiple barriers to safe plasma donation:</p>

<h3>Autoantibody Concerns</h3>

<p>Lupus plasma contains pathogenic antibodies that could harm recipients:</p>

<ul>
<li><strong>Anti-nuclear antibodies (ANA):</strong> Present in 95%+ of SLE patients, attack cell nuclei</li>
<li><strong>Anti-dsDNA antibodies:</strong> Correlate with disease activity and kidney involvement</li>
<li><strong>Anti-Smith antibodies:</strong> Specific to lupus, affect RNA processing</li>
<li><strong>Anti-Ro/SSA and Anti-La/SSB:</strong> Can cross placenta and affect fetus (neonatal lupus risk)</li>
<li><strong>Antiphospholipid antibodies:</strong> Increase blood clot risk in recipients</li>
<li><strong>Anti-histone antibodies:</strong> Common in drug-induced lupus</li>
</ul>

<h3>Recipient Safety Risks</h3>

<p>Transfusing lupus plasma could theoretically:</p>

<ul>
<li>Transfer autoantibodies to immunocompromised recipients</li>
<li>Trigger clotting in patients receiving immunoglobulin products</li>
<li>Interfere with immune reconstitution therapies</li>
<li>Contaminate plasma pools used for manufacturing medications</li>
</ul>

<h3>Donor Safety Concerns</h3>

<p>Plasma donation poses risks to lupus patients:</p>

<ul>
<li><strong>Disease flare trigger:</strong> Physical stress can activate lupus</li>
<li><strong>Immune depletion:</strong> Removing plasma temporarily reduces immune factors</li>
<li><strong>Kidney stress:</strong> Many lupus patients have subclinical kidney involvement</li>
<li><strong>Infection risk:</strong> Immunosuppressed donors more vulnerable to needle-site infections</li>
<li><strong>Fatigue exacerbation:</strong> Lupus fatigue worsened by plasma loss</li>
<li><strong>Photosensitivity:</strong> Travel to/from center increases sun exposure</li>
</ul>

{AFFILIATE_BLOCK}

<h2 id="medications">Lupus Medications and Deferral</h2>

<p>All lupus medications are disqualifying for plasma donation:</p>

<h3>Antimalarial Drugs (Permanent Deferral)</h3>

<table>
<thead>
<tr>
<th>Medication</th>
<th>Brand Name</th>
<th>Why Disqualifying</th>
</tr>
</thead>
<tbody>
<tr>
<td>Hydroxychloroquine</td>
<td>Plaquenil</td>
<td>Immune modulation, long half-life (40-50 days)</td>
</tr>
<tr>
<td>Chloroquine</td>
<td>Aralen</td>
<td>Antimalarial with immunosuppressive effects</td>
</tr>
</tbody>
</table>

<h3>Immunosuppressants (Permanent Deferral)</h3>

<table>
<thead>
<tr>
<th>Medication</th>
<th>Brand Name</th>
<th>Why Disqualifying</th>
</tr>
</thead>
<tbody>
<tr>
<td>Azathioprine</td>
<td>Imuran</td>
<td>Strong immunosuppressant, cancer risk</td>
</tr>
<tr>
<td>Mycophenolate</td>
<td>CellCept, Myfortic</td>
<td>Immunosuppressant, teratogenic</td>
</tr>
<tr>
<td>Methotrexate</td>
<td>Trexall, Rheumatrex</td>
<td>Chemotherapy agent, immunosuppressant</td>
</tr>
<tr>
<td>Cyclophosphamide</td>
<td>Cytoxan</td>
<td>Chemotherapy, severe immunosuppression</td>
</tr>
<tr>
<td>Cyclosporine</td>
<td>Neoral, Sandimmune</td>
<td>Calcineurin inhibitor, transplant drug</td>
</tr>
<tr>
<td>Tacrolimus</td>
<td>Prograf</td>
<td>Strong immunosuppressant</td>
</tr>
</tbody>
</table>

<h3>Biologic Medications (Permanent Deferral)</h3>

<table>
<thead>
<tr>
<th>Medication</th>
<th>Brand Name</th>
<th>Why Disqualifying</th>
</tr>
</thead>
<tbody>
<tr>
<td>Belimumab</td>
<td>Benlysta</td>
<td>B-cell inhibitor monoclonal antibody</td>
</tr>
<tr>
<td>Rituximab</td>
<td>Rituxan</td>
<td>B-cell depleting antibody</td>
</tr>
<tr>
<td>Anifrolumab</td>
<td>Saphnelo</td>
<td>Type I interferon receptor antagonist</td>
</tr>
</tbody>
</table>

<h3>Corticosteroids (Deferral During Use)</h3>

<table>
<thead>
<tr>
<th>Medication</th>
<th>Common Doses</th>
<th>Deferral Status</th>
</tr>
</thead>
<tbody>
<tr>
<td>Prednisone</td>
<td>5-60 mg daily</td>
<td>Deferred while taking any dose</td>
</tr>
<tr>
<td>Methylprednisolone</td>
<td>IV pulse therapy</td>
<td>Deferred during and 30 days after</td>
</tr>
</tbody>
</table>

{PRO_TOOLKIT}

<h3>Other Medications</h3>

<ul>
<li><strong>NSAIDs:</strong> Generally allowed if used alone (rare in lupus)</li>
<li><strong>Anticoagulants:</strong> Warfarin, apixaban, rivaroxaban all disqualifying</li>
<li><strong>Antiplatelet drugs:</strong> Aspirin usually allowed; Plavix disqualifies</li>
</ul>

<p><strong>Reality check:</strong> It's extremely rare for lupus patients to be on zero disqualifying medications. Even mild lupus typically requires hydroxychloroquine at minimum.</p>

<h2 id="antiphospholipid">Antiphospholipid Syndrome Concerns</h2>

<p>Up to 40% of lupus patients have antiphospholipid antibodies, creating additional concerns:</p>

<h3>What Is Antiphospholipid Syndrome (APS)?</h3>

<p>APS is characterized by:</p>

<ul>
<li><strong>Antiphospholipid antibodies:</strong> Anticardiolipin, anti-β2 glycoprotein I, lupus anticoagulant</li>
<li><strong>Blood clot risk:</strong> Venous thrombosis (DVT, PE) and arterial clots (stroke)</li>
<li><strong>Pregnancy complications:</strong> Recurrent miscarriage, pre-eclampsia</li>
<li><strong>Treatment requirement:</strong> Long-term anticoagulation with warfarin or heparin</li>
</ul>

<h3>Why APS Disqualifies Donation</h3>

<ul>
<li><strong>Clotting risk:</strong> Transferring prothrombotic antibodies to recipients could cause clots</li>
<li><strong>Anticoagulation:</strong> All blood thinners disqualify donation</li>
<li><strong>Catastrophic APS risk:</strong> Stress of donation could trigger widespread clotting in donor</li>
</ul>

<h3>Screening Questions</h3>

<p>Staff will ask about:</p>

<ul>
<li>History of blood clots (DVT, PE, stroke)</li>
<li>Recurrent miscarriages</li>
<li>Use of blood thinners</li>
<li>Diagnosis of antiphospholipid syndrome</li>
</ul>

<h2 id="research">Donating Plasma for Lupus Research</h2>

<p>While you can't donate commercially, your lupus plasma is valuable for research:</p>

<h3>Why Researchers Want Lupus Plasma</h3>

<ul>
<li><strong>Biomarker discovery:</strong> Identify new antibodies and disease markers</li>
<li><strong>Treatment response studies:</strong> Track how biologics affect antibody levels</li>
<li><strong>Genetic research:</strong> Combine plasma with genetic data</li>
<li><strong>Flare prediction:</strong> Find early warning signs in plasma composition</li>
<li><strong>New diagnostics:</strong> Develop better lupus detection tests</li>
</ul>

<h3>Major Lupus Research Programs</h3>

<table>
<thead>
<tr>
<th>Program</th>
<th>Organization</th>
<th>How to Participate</th>
</tr>
</thead>
<tbody>
<tr>
<td>LORE Registry</td>
<td>Lupus Foundation of America</td>
<td>Register at lupus.org/research</td>
</tr>
<tr>
<td>SPARE Study</td>
<td>NIH/NIAMS</td>
<td>Contact through ClinicalTrials.gov</td>
</tr>
<tr>
<td>Alliance for Lupus Research</td>
<td>Various academic centers</td>
<td>lupusresearch.org</td>
</tr>
<tr>
<td>University biobanks</td>
<td>Johns Hopkins, NYU, UCSF, others</td>
<td>Contact local rheumatology research</td>
</tr>
</tbody>
</table>

<h3>What Research Participation Involves</h3>

<ol>
<li><strong>Enrollment:</strong> Complete health questionnaires and consent forms</li>
<li><strong>Blood draw:</strong> Usually 20-40 mL (much less than plasma donation)</li>
<li><strong>Medical records:</strong> Share diagnosis and treatment history</li>
<li><strong>Follow-up:</strong> Some studies request samples during flares vs. remission</li>
<li><strong>No compensation:</strong> Research studies don't pay for samples (unlike commercial donation)</li>
</ol>

<h3>Benefits of Research Donation</h3>

<ul>
<li>Contribute to lupus treatment advancement</li>
<li>Help develop better diagnostic tests</li>
<li>Potentially access results of your antibody profile</li>
<li>Support research for rare lupus subtypes</li>
<li>Create legacy contribution to science</li>
</ul>

<h2 id="alternatives">Alternative Ways to Contribute</h2>

<p>If commercial plasma donation isn't possible, consider these alternatives:</p>

<h3>Direct Support</h3>

<ul>
<li><strong>Volunteer at centers:</strong> Help with administrative tasks and donor support</li>
<li><strong>Organize drives:</strong> Coordinate plasma donation events in your community</li>
<li><strong>Awareness campaigns:</strong> Educate others about plasma donation importance</li>
<li><strong>Financial donations:</strong> Support organizations serving immunocompromised patients</li>
</ul>

<h3>Lupus-Specific Advocacy</h3>

<ul>
<li><strong>Join support groups:</strong> Share your experience to help newly diagnosed patients</li>
<li><strong>Participate in trials:</strong> Help test new lupus treatments</li>
<li><strong>Raise awareness:</strong> Combat stigma and misconceptions about lupus</li>
<li><strong>Support legislation:</strong> Advocate for lupus research funding</li>
</ul>

<h3>Health Optimization</h3>

<p>Focus on managing your own health:</p>

<ul>
<li>Strict medication adherence to prevent flares</li>
<li>Regular rheumatologist visits and monitoring</li>
<li>Sun protection to avoid photosensitivity triggers</li>
<li>Healthy lifestyle to reduce cardiovascular risk</li>
<li>Mental health support for chronic illness</li>
</ul>

{related_reading([
    ('/blog/can-you-donate-plasma-with-multiple-sclerosis-2026', 'MS and Plasma Donation'),
    ('/blog/can-you-donate-plasma-with-arthritis-2026', 'Rheumatoid Arthritis Guide'),
    ('/blog/autoimmune-disease-plasma-donation-complete-guide', 'Complete Autoimmune Disease Guide')
])}

{footer_related()}
''',
        'faqs': [
            make_faq(
                "Can I donate if my lupus is in remission?",
                "No, even lupus in remission is a permanent deferral. Remission doesn't eliminate the autoantibodies in your plasma—ANA and other lupus antibodies typically remain detectable even when disease is inactive. Additionally, most patients maintain at least hydroxychloroquine during remission, which is disqualifying. The diagnosis itself, not disease activity, determines eligibility."
            ),
            make_faq(
                "What if I only have cutaneous lupus, not systemic lupus?",
                "Cutaneous lupus (discoid lupus, subacute cutaneous lupus) may be handled differently depending on medications. If you're on only topical treatments and have no systemic involvement or autoantibodies, some centers might consider you. However, most cutaneous lupus patients take hydroxychloroquine or other systemic medications that disqualify donation. You'd need to discuss your specific case with the center."
            ),
            make_faq(
                "Will plasma donation detect lupus I don't know I have?",
                "Standard plasma donation screening doesn't include ANA tests or lupus-specific antibody panels. However, if you have unexplained symptoms (joint pain, rashes, fatigue, recurrent fevers), you should see a rheumatologist for evaluation before attempting to donate. Don't rely on plasma screening to diagnose autoimmune diseases—it's not designed for that purpose."
            ),
            make_faq(
                "Can family members of lupus patients donate plasma?",
                "Yes, having a family member with lupus doesn't disqualify you from donation. While lupus has genetic risk factors, family members without symptoms or diagnosis can donate normally. However, if you have lupus symptoms or positive autoimmune testing, you should be evaluated by a doctor before donating. First-degree relatives have slightly higher lupus risk but can still donate if healthy."
            ),
            make_faq(
                "What if I had drug-induced lupus that resolved?",
                "Drug-induced lupus (from medications like hydralazine, procainamide, or TNF inhibitors) typically resolves within weeks to months after stopping the trigger medication. If your symptoms completely resolved, antibodies normalized, and you're off all lupus medications, some centers might consider you after 12+ months—but this requires center director approval and medical documentation. Most centers still maintain permanent deferral for any lupus diagnosis."
            ),
        ]
    },
    {
        'slug': 'can-you-donate-plasma-with-schizophrenia-2026',
        'title': 'Can You Donate Plasma With Schizophrenia? [2026 Medication Guide]',
        'meta': 'Schizophrenia diagnosis doesn\'t automatically disqualify you, but antipsychotic medications and symptom stability determine eligibility. Complete guide for 2026.',
        'category': 'Medical Eligibility',
        'read_time': 8,
        'toc': [
            ('quick-answer', 'Quick Answer'),
            ('eligibility', 'Schizophrenia and Donation Eligibility'),
            ('antipsychotics', 'Antipsychotic Medications'),
            ('screening', 'Mental Health Screening Process'),
            ('safety', 'Safety Considerations'),
            ('tips', 'Donation Tips for Stable Patients'),
        ],
        'content': f'''
<div class="quick-answer">
<h3>Quick Answer: Can You Donate Plasma With Schizophrenia?</h3>
<p><strong>It depends on your symptom stability and medications.</strong> Most plasma centers accept donors with well-controlled schizophrenia on stable medication regimens, as long as you can understand the donation process and consent. However, certain antipsychotics, recent hospitalizations, or active psychotic symptoms will disqualify you temporarily or permanently.</p>
</div>

<h2 id="eligibility">Schizophrenia and Donation Eligibility</h2>

<p>Plasma donation eligibility with schizophrenia focuses on three factors:</p>

<h3>When You CAN Donate</h3>

<ul>
<li><strong>Stable symptoms:</strong> No active hallucinations, delusions, or disorganized thinking</li>
<li><strong>Medication compliance:</strong> Taking prescribed antipsychotics regularly</li>
<li><strong>Capacity to consent:</strong> Able to understand risks and benefits of donation</li>
<li><strong>No recent crises:</strong> No hospitalizations or medication changes in past 6 months</li>
<li><strong>Approved medications:</strong> On antipsychotics that don't disqualify donation</li>
<li><strong>Independent functioning:</strong> Able to attend appointments and follow instructions</li>
</ul>

<h3>When You're Deferred</h3>

<ul>
<li><strong>Active psychosis:</strong> Current hallucinations, delusions, or paranoia</li>
<li><strong>Recent hospitalization:</strong> Psychiatric admission within 6-12 months</li>
<li><strong>Medication changes:</strong> New antipsychotic or dose adjustments within 3-6 months</li>
<li><strong>Clozapine use:</strong> This medication creates permanent deferral (blood monitoring required)</li>
<li><strong>Inability to consent:</strong> Cognitive symptoms prevent understanding donation process</li>
<li><strong>Substance use:</strong> Co-occurring drug or alcohol use disorders</li>
<li><strong>Suicidal ideation:</strong> Active thoughts of self-harm</li>
</ul>

{AFFILIATE_BLOCK}

<h2 id="antipsychotics">Antipsychotic Medications</h2>

<p>Most antipsychotics are acceptable, but some require special consideration:</p>

<h3>First-Generation (Typical) Antipsychotics</h3>

<table>
<thead>
<tr>
<th>Medication</th>
<th>Brand Name</th>
<th>Donation Status</th>
</tr>
</thead>
<tbody>
<tr>
<td>Haloperidol</td>
<td>Haldol</td>
<td>✓ Usually allowed</td>
</tr>
<tr>
<td>Chlorpromazine</td>
<td>Thorazine</td>
<td>✓ Usually allowed</td>
</tr>
<tr>
<td>Fluphenazine</td>
<td>Prolixin</td>
<td>✓ Usually allowed</td>
</tr>
<tr>
<td>Perphenazine</td>
<td>Trilafon</td>
<td>✓ Usually allowed</td>
</tr>
</tbody>
</table>

<h3>Second-Generation (Atypical) Antipsychotics</h3>

<table>
<thead>
<tr>
<th>Medication</th>
<th>Brand Name</th>
<th>Donation Status</th>
</tr>
</thead>
<tbody>
<tr>
<td>Risperidone</td>
<td>Risperdal</td>
<td>✓ Usually allowed</td>
</tr>
<tr>
<td>Olanzapine</td>
<td>Zyprexa</td>
<td>✓ Usually allowed</td>
</tr>
<tr>
<td>Quetiapine</td>
<td>Seroquel</td>
<td>✓ Usually allowed</td>
</tr>
<tr>
<td>Aripiprazole</td>
<td>Abilify</td>
<td>✓ Usually allowed</td>
</tr>
<tr>
<td>Ziprasidone</td>
<td>Geodon</td>
<td>✓ Usually allowed</td>
</tr>
<tr>
<td>Paliperidone</td>
<td>Invega</td>
<td>✓ Usually allowed</td>
</tr>
<tr>
<td>Lurasidone</td>
<td>Latuda</td>
<td>✓ Usually allowed</td>
</tr>
<tr>
<td>Brexpiprazole</td>
<td>Rexulti</td>
<td>✓ Usually allowed</td>
</tr>
<tr>
<td>Cariprazine</td>
<td>Vraylar</td>
<td>✓ Usually allowed</td>
</tr>
<tr>
<td>Lumateperone</td>
<td>Caplyta</td>
<td>✓ Usually allowed</td>
</tr>
</tbody>
</table>

<h3>Special Case: Clozapine (PERMANENT DEFERRAL)</h3>

<table>
<thead>
<tr>
<th>Medication</th>
<th>Brand Name</th>
<th>Why Disqualifying</th>
</tr>
</thead>
<tbody>
<tr>
<td>Clozapine</td>
<td>Clozaril, Versacloz</td>
<td>Requires weekly/biweekly blood monitoring for agranulocytosis; severe side effect profile makes donation unsafe</td>
</tr>
</tbody>
</table>

{PRO_TOOLKIT}

<h3>Long-Acting Injectable Antipsychotics</h3>

<p>These are generally acceptable if symptoms are stable:</p>

<ul>
<li><strong>Risperidone long-acting (Risperdal Consta):</strong> Usually allowed</li>
<li><strong>Paliperidone palmitate (Invega Sustenna, Invega Trinza):</strong> Usually allowed</li>
<li><strong>Aripiprazole long-acting (Abilify Maintena, Aristada):</strong> Usually allowed</li>
<li><strong>Haloperidol decanoate:</strong> Usually allowed</li>
</ul>

<h2 id="screening">Mental Health Screening Process</h2>

<p>Expect more detailed questioning when you disclose schizophrenia:</p>

<h3>Questions Staff Will Ask</h3>

<ol>
<li><strong>"When were you diagnosed with schizophrenia?"</strong></li>
<li><strong>"What medications are you currently taking?"</strong></li>
<li><strong>"When was your last dose?"</strong></li>
<li><strong>"Have you had any recent hospitalizations?"</strong></li>
<li><strong>"When was your last psychiatrist appointment?"</strong></li>
<li><strong>"Are you experiencing any symptoms today?"</strong></li>
<li><strong>"Do you understand what plasma donation involves?"</strong></li>
<li><strong>"Can you follow instructions during the donation process?"</strong></li>
</ol>

<h3>Capacity Assessment</h3>

<p>Staff will evaluate your ability to:</p>

<ul>
<li>Understand the donation process and risks</li>
<li>Make an informed decision to participate</li>
<li>Communicate clearly with staff</li>
<li>Follow multi-step instructions</li>
<li>Recognize and report adverse reactions</li>
</ul>

<h3>Documentation Requirements</h3>

<p>Some centers may request:</p>

<ul>
<li>Letter from psychiatrist confirming stability</li>
<li>List of current medications and dosages</li>
<li>Recent psychiatric evaluation (within 6-12 months)</li>
<li>Emergency contact information</li>
</ul>

<h2 id="safety">Safety Considerations</h2>

<h3>Why Some Centers Are Cautious</h3>

<ul>
<li><strong>Consent validity:</strong> Ensuring decision-making capacity is intact</li>
<li><strong>Medication side effects:</strong> Some antipsychotics cause dizziness or blood pressure changes</li>
<li><strong>Stress response:</strong> Donation stress could potentially trigger symptoms</li>
<li><strong>Compliance concerns:</strong> Ability to follow pre- and post-donation instructions</li>
</ul>

<h3>Risks for Donors With Schizophrenia</h3>

<ul>
<li><strong>Orthostatic hypotension:</strong> Many antipsychotics lower blood pressure; donation compounds this</li>
<li><strong>Dehydration sensitivity:</strong> Some medications affect fluid regulation</li>
<li><strong>Sedation:</strong> Antipsychotics may cause drowsiness worsened by donation</li>
<li><strong>Metabolic effects:</strong> Weight gain and diabetes risk with some medications</li>
</ul>

<h2 id="tips">Donation Tips for Stable Patients</h2>

<h3>Before Your First Donation</h3>

<ul>
<li><strong>Discuss with psychiatrist:</strong> Confirm they approve of plasma donation</li>
<li><strong>Gather documentation:</strong> Bring medication list and doctor contact info</li>
<li><strong>Choose stable periods:</strong> Don't attempt during medication changes or stress</li>
<li><strong>Bring support person:</strong> Consider having someone accompany you first time</li>
<li><strong>Time medications:</strong> Take morning doses as usual; bring afternoon doses if needed</li>
</ul>

<h3>Day of Donation</h3>

<ul>
<li><strong>Take medications as prescribed:</strong> Don't skip doses</li>
<li><strong>Eat substantial meal:</strong> Prevents low blood sugar and dizziness</li>
<li><strong>Hydrate well:</strong> 16-20 oz water 2-3 hours before</li>
<li><strong>Avoid caffeine:</strong> Can interact with some antipsychotics</li>
<li><strong>Wear comfortable clothes:</strong> Donation takes 1-2 hours</li>
<li><strong>Bring entertainment:</strong> Book, headphones, or stress ball</li>
</ul>

<h3>During Donation</h3>

<ul>
<li><strong>Communicate clearly:</strong> Tell staff immediately if you feel unwell</li>
<li><strong>Stay still:</strong> Movement can affect donation quality</li>
<li><strong>Ask questions:</strong> Don't hesitate to seek clarification</li>
<li><strong>Report symptoms:</strong> Dizziness, tingling, anxiety, or disorientation</li>
</ul>

<h3>After Donation</h3>

<ul>
<li><strong>Rest 15+ minutes:</strong> Don't rush to stand up</li>
<li><strong>Drink extra fluids:</strong> 8-10 glasses over next 24 hours</li>
<li><strong>Eat protein:</strong> Helps replace plasma proteins</li>
<li><strong>Avoid strenuous activity:</strong> Take it easy for 24 hours</li>
<li><strong>Monitor mood:</strong> Watch for any symptom changes</li>
<li><strong>Continue medications:</strong> Maintain your regular schedule</li>
</ul>

<h3>Long-Term Donation Considerations</h3>

<ul>
<li><strong>Stick to safe frequency:</strong> Don't exceed twice weekly maximum</li>
<li><strong>Track how you feel:</strong> Note any pattern of symptoms after donation</li>
<li><strong>Maintain stability:</strong> If symptoms worsen, pause donations and see psychiatrist</li>
<li><strong>Update medical info:</strong> Report any medication or diagnosis changes</li>
</ul>

<h3>When to Stop Donating</h3>

<p>Discontinue plasma donation if you experience:</p>

<ul>
<li>Return of psychotic symptoms</li>
<li>Medication changes or new prescriptions</li>
<li>Psychiatric hospitalization</li>
<li>Increased anxiety or paranoia around donation</li>
<li>Difficulty following donation instructions</li>
<li>Clozapine prescription (permanent deferral)</li>
</ul>

{related_reading([
    ('/blog/can-you-donate-plasma-on-antidepressants-2026', 'Antidepressants and Plasma Donation'),
    ('/blog/can-you-donate-plasma-with-anxiety-bipolar-guide', 'Anxiety and Bipolar Disorder Guide'),
    ('/blog/mental-health-medications-plasma-donation', 'Mental Health Medications Complete Guide')
])}

{footer_related()}
''',
        'faqs': [
            make_faq(
                "Will the plasma center discriminate against me for having schizophrenia?",
                "Legitimate plasma centers follow medical guidelines, not discrimination. They defer based on safety factors (medication types, symptom stability, capacity to consent), not diagnosis alone. If you're stable on acceptable medications and can understand the process, most centers will accept you. However, center staff must ensure both donor and recipient safety, which requires honest assessment of your current mental health status."
            ),
            make_faq(
                "Can I donate if I'm on clozapine?",
                "No, clozapine (Clozaril) creates a permanent deferral from plasma donation. This medication requires regular blood monitoring because it can cause agranulocytosis (severe white blood cell depletion). The plasma donation process could interfere with this necessary monitoring and poses additional risks. If you're on clozapine, your treatment-resistant schizophrenia likely requires this specific medication—don't switch medications just to donate plasma."
            ),
            make_faq(
                "What if I haven't told my psychiatrist I'm donating plasma?",
                "You should always inform your psychiatrist about plasma donation. They can assess whether donation is safe given your specific medication regimen and symptom profile. Some antipsychotics have side effects (low blood pressure, sedation, metabolic changes) that make frequent plasma donation risky. Your psychiatrist may also provide documentation that helps speed up center approval."
            ),
            make_faq(
                "Will donating plasma affect my antipsychotic medication levels?",
                "Plasma donation shouldn't significantly affect medication levels for most antipsychotics, as these drugs distribute into tissues and cells, not just plasma. However, proper hydration is important to maintain consistent blood volume. If you notice any change in symptom control after starting plasma donation, contact your psychiatrist—it may be coincidental, but they should evaluate."
            ),
            make_faq(
                "Can I donate during a medication transition?",
                "No, wait until you've been stable on your new medication for at least 3-6 months before attempting plasma donation. Medication transitions in schizophrenia can be delicate, with risk of symptom breakthrough or side effects. Adding the physical stress of plasma donation during this time isn't advisable. Focus on stabilizing your mental health first, then consider donation."
            ),
        ]
    },
    {
        'slug': 'can-you-donate-plasma-with-narcolepsy-2026',
        'title': 'Can You Donate Plasma With Narcolepsy? [2026 Medication Guide]',
        'meta': 'Narcolepsy doesn\'t automatically disqualify plasma donation, but stimulant medications and cataplexy severity determine eligibility. Complete 2026 guide.',
        'category': 'Medical Eligibility',
        'read_time': 7,
        'toc': [
            ('quick-answer', 'Quick Answer'),
            ('eligibility', 'Narcolepsy and Donation Eligibility'),
            ('medications', 'Narcolepsy Medications'),
            ('cataplexy', 'Cataplexy and Safety Concerns'),
            ('screening', 'What to Tell Screening Staff'),
            ('tips', 'Safe Donation Tips'),
        ],
        'content': f'''
<div class="quick-answer">
<h3>Quick Answer: Can You Donate Plasma With Narcolepsy?</h3>
<p><strong>It depends on your medications and symptom severity.</strong> Many people with narcolepsy can donate if they're stable on acceptable medications (most stimulants are allowed), don't have severe cataplexy, and can stay awake during the 1-2 hour donation process. However, sodium oxybate (Xyrem/Xywav) and some other medications may disqualify you.</p>
</div>

<h2 id="eligibility">Narcolepsy and Donation Eligibility</h2>

<h3>When You CAN Donate</h3>

<ul>
<li><strong>Well-controlled symptoms:</strong> Able to stay awake for 1-2 hours comfortably</li>
<li><strong>Acceptable medications:</strong> Most stimulants and wake-promoting agents are allowed</li>
<li><strong>Mild or no cataplexy:</strong> No risk of sudden muscle weakness during donation</li>
<li><strong>Stable regimen:</strong> No recent medication changes</li>
<li><strong>Can time medications:</strong> Able to take doses to maintain alertness during donation</li>
</ul>

<h3>When You're Deferred</h3>

<ul>
<li><strong>Sodium oxybate use:</strong> Xyrem or Xywav (permanent or long-term deferral)</li>
<li><strong>Severe cataplexy:</strong> Frequent or emotionally-triggered muscle weakness</li>
<li><strong>Uncontrolled symptoms:</strong> Falling asleep unpredictably</li>
<li><strong>Recent diagnosis:</strong> Still adjusting medications (wait for stability)</li>
<li><strong>Safety concerns:</strong> Risk of sleep attacks during donation</li>
</ul>

{AFFILIATE_BLOCK}

<h2 id="medications">Narcolepsy Medications</h2>

<h3>Wake-Promoting Agents (Usually Allowed)</h3>

<table>
<thead>
<tr>
<th>Medication</th>
<th>Brand Name</th>
<th>Donation Status</th>
</tr>
</thead>
<tbody>
<tr>
<td>Modafinil</td>
<td>Provigil</td>
<td>✓ Usually allowed</td>
</tr>
<tr>
<td>Armodafinil</td>
<td>Nuvigil</td>
<td>✓ Usually allowed</td>
</tr>
<tr>
<td>Solriamfetol</td>
<td>Sunosi</td>
<td>✓ Usually allowed</td>
</tr>
<tr>
<td>Pitolisant</td>
<td>Wakix</td>
<td>✓ Usually allowed</td>
</tr>
</tbody>
</table>

<h3>Stimulants (Usually Allowed, Check Center Policy)</h3>

<table>
<thead>
<tr>
<th>Medication</th>
<th>Brand Name</th>
<th>Donation Status</th>
</tr>
</thead>
<tbody>
<tr>
<td>Methylphenidate</td>
<td>Ritalin, Concerta</td>
<td>✓ Usually allowed with prescription</td>
</tr>
<tr>
<td>Dexmethylphenidate</td>
<td>Focalin</td>
<td>✓ Usually allowed with prescription</td>
</tr>
<tr>
<td>Amphetamine/dextroamphetamine</td>
<td>Adderall</td>
<td>✓ Usually allowed with prescription</td>
</tr>
<tr>
<td>Lisdexamfetamine</td>
<td>Vyvanse</td>
<td>✓ Usually allowed with prescription</td>
</tr>
<tr>
<td>Dextroamphetamine</td>
<td>Dexedrine</td>
<td>✓ Usually allowed with prescription</td>
</tr>
</tbody>
</table>

<h3>Sodium Oxybate (DISQUALIFYING)</h3>

<table>
<thead>
<tr>
<th>Medication</th>
<th>Brand Name</th>
<th>Why Disqualifying</th>
</tr>
</thead>
<tbody>
<tr>
<td>Sodium oxybate</td>
<td>Xyrem</td>
<td>CNS depressant, GHB derivative, strict REMS program, safety concerns</td>
</tr>
<tr>
<td>Mixed salts oxybate</td>
<td>Xywav</td>
<td>CNS depressant, same safety concerns as Xyrem</td>
</tr>
</tbody>
</table>

{PRO_TOOLKIT}

<h3>Cataplexy Medications</h3>

<table>
<thead>
<tr>
<th>Medication Class</th>
<th>Examples</th>
<th>Donation Status</th>
</tr>
</thead>
<tbody>
<tr>
<td>SSRIs</td>
<td>Fluoxetine (Prozac)</td>
<td>✓ Usually allowed</td>
</tr>
<tr>
<td>SNRIs</td>
<td>Venlafaxine (Effexor)</td>
<td>✓ Usually allowed</td>
</tr>
<tr>
<td>Tricyclic antidepressants</td>
<td>Clomipramine, Imipramine</td>
<td>Check center policy</td>
</tr>
</tbody>
</table>

<h2 id="cataplexy">Cataplexy and Safety Concerns</h2>

<h3>What Is Cataplexy?</h3>

<p>Cataplexy is sudden muscle weakness triggered by strong emotions (laughter, surprise, anger), affecting about 70% of narcolepsy type 1 patients.</p>

<h3>Cataplexy Severity and Donation</h3>

<table>
<thead>
<tr>
<th>Severity</th>
<th>Description</th>
<th>Donation Safety</th>
</tr>
</thead>
<tbody>
<tr>
<td>Mild</td>
<td>Rare episodes, slight facial drooping or knee buckling, brief duration</td>
<td>✓ Usually safe to donate</td>
</tr>
<tr>
<td>Moderate</td>
<td>Weekly episodes, partial muscle weakness, need to sit/lean</td>
<td>⚠ Case-by-case evaluation</td>
</tr>
<tr>
<td>Severe</td>
<td>Daily episodes, complete muscle weakness, falls</td>
<td>✗ Likely deferred (safety risk)</td>
</tr>
</tbody>
</table>

<h3>Why Severe Cataplexy Is Concerning</h3>

<ul>
<li><strong>Needle in arm:</strong> Sudden muscle weakness could cause injury during venipuncture</li>
<li><strong>Equipment damage:</strong> Falls could disrupt donation equipment</li>
<li><strong>Staff availability:</strong> Centers may not be equipped to handle cataplexy episodes</li>
<li><strong>Liability:</strong> Risk of injury during episode on center premises</li>
</ul>

<h3>How to Discuss Cataplexy With Staff</h3>

<p>Be honest about:</p>

<ul>
<li>Frequency of episodes (per day, week, month)</li>
<li>Typical triggers (laughter, stress, surprise)</li>
<li>Severity (facial only, partial weakness, full collapse)</li>
<li>Warning signs (do you feel it coming?)</li>
<li>How well controlled with medication</li>
<li>Last episode date</li>
</ul>

<h2 id="screening">What to Tell Screening Staff</h2>

<h3>Questions to Expect</h3>

<ol>
<li><strong>"What type of narcolepsy do you have?"</strong> (Type 1 with cataplexy, Type 2 without, or unsure)</li>
<li><strong>"What medications do you take for narcolepsy?"</strong></li>
<li><strong>"When do you take your doses?"</strong></li>
<li><strong>"Can you stay awake for 1-2 hours without falling asleep?"</strong></li>
<li><strong>"Do you experience cataplexy?"</strong></li>
<li><strong>"Have you ever fallen asleep unexpectedly?"</strong></li>
<li><strong>"Can you recognize when you're about to fall asleep?"</strong></li>
</ol>

<h3>Documentation to Bring</h3>

<ul>
<li><strong>Prescription information:</strong> All narcolepsy medications with dosages</li>
<li><strong>Doctor's note:</strong> Some centers may request clearance from neurologist/sleep specialist</li>
<li><strong>Diagnosis confirmation:</strong> Sleep study results or formal diagnosis letter</li>
<li><strong>Emergency contact:</strong> Someone who can pick you up if needed</li>
</ul>

<h2 id="tips">Safe Donation Tips</h2>

<h3>Timing Your Donation</h3>

<ul>
<li><strong>Peak medication times:</strong> Schedule during peak alertness (1-2 hours after stimulant dose)</li>
<li><strong>Avoid sleep attacks:</strong> Not during known sleepy periods</li>
<li><strong>Morning vs afternoon:</strong> Choose when you're naturally most alert</li>
<li><strong>After good sleep:</strong> Donate on days you're well-rested</li>
</ul>

<h3>Before Donation</h3>

<ul>
<li><strong>Take medications as prescribed:</strong> Don't skip doses</li>
<li><strong>Get adequate sleep:</strong> Follow your sleep schedule strictly night before</li>
<li><strong>Eat protein-rich meal:</strong> Helps maintain alertness</li>
<li><strong>Hydrate well:</strong> 16-20 oz water 2-3 hours before</li>
<li><strong>Avoid heavy foods:</strong> Can increase sleepiness</li>
<li><strong>Skip alcohol:</strong> Never mix with narcolepsy meds or donation</li>
</ul>

<h3>During Donation</h3>

<ul>
<li><strong>Stay engaged:</strong> Listen to stimulating podcast, music, or audiobook</li>
<li><strong>Keep eyes open:</strong> Don't close eyes even if resting</li>
<li><strong>Alert staff:</strong> Tell them immediately if you feel sleepy</li>
<li><strong>Avoid emotional content:</strong> If you have cataplexy, skip comedy or sad stories</li>
<li><strong>Communicate continuously:</strong> Talk to staff periodically to stay alert</li>
</ul>

<h3>After Donation</h3>

<ul>
<li><strong>Don't drive immediately:</strong> Rest 15-30 minutes first</li>
<li><strong>Have backup transport:</strong> Arrange ride home if needed</li>
<li><strong>Eat and drink:</strong> Snacks and fluids help with alertness</li>
<li><strong>Monitor sleepiness:</strong> Donation can increase fatigue</li>
<li><strong>Rest as needed:</strong> Don't fight excessive sleepiness after donation</li>
</ul>

<h3>Signs You Should Stop Donating</h3>

<ul>
<li>Falling asleep during donation process</li>
<li>Cataplexy episodes at donation center</li>
<li>Excessive fatigue after donations</li>
<li>Medication changes affecting alertness</li>
<li>Symptoms worsening with donation frequency</li>
</ul>

{related_reading([
    ('/blog/can-you-donate-plasma-on-adderall-adhd-2026', 'ADHD Medications and Plasma Donation'),
    ('/blog/can-you-donate-plasma-with-sleep-apnea-2026', 'Sleep Apnea and CPAP Users'),
    ('/blog/stimulant-medications-plasma-donation-guide', 'Complete Stimulant Medication Guide')
])}

{footer_related()}
''',
        'faqs': [
            make_faq(
                "Can I donate if I'm on Xyrem or Xywav?",
                "No, sodium oxybate (Xyrem, Xywav) is disqualifying for plasma donation. These are controlled substances (GHB derivatives) with CNS depressant effects, enrolled in strict REMS programs. The safety profile and controlled nature of these medications make plasma donation inappropriate. If you're on Xyrem/Xywav, you likely have narcolepsy type 1 with severe symptoms that make donation risky anyway."
            ),
            make_faq(
                "Will I fall asleep during plasma donation?",
                "If your narcolepsy is well-controlled with medication and you time your donation during peak alertness, you should be able to stay awake. The donation takes 1-2 hours and involves a needle in your arm, which provides enough stimulation for most people. However, if you have frequent uncontrollable sleep attacks even on medication, plasma donation may not be safe for you. Discuss this honestly with screening staff."
            ),
            make_faq(
                "Do I need a doctor's note to donate with narcolepsy?",
                "Most centers don't automatically require a doctor's note, but it's helpful to bring one—especially if you have cataplexy or are on multiple medications. A note from your neurologist or sleep specialist confirming your diagnosis is stable and medications are optimized can speed up the approval process. Some centers may request this if they're unfamiliar with narcolepsy."
            ),
            make_faq(
                "Can donation make my narcolepsy worse?",
                "Donation shouldn't directly worsen narcolepsy, but it can cause temporary fatigue that compounds your existing sleepiness. The fluid and protein loss from donation may leave you more tired for 24-48 hours. If you notice excessive sleepiness or worsening symptoms after donation, consider reducing donation frequency or stopping. Proper hydration and rest between donations are critical for narcolepsy patients."
            ),
            make_faq(
                "What if I have a cataplexy episode at the donation center?",
                "Alert the staff immediately and let your body go through the episode safely. The phlebotomist should stop the donation if needed and ensure you don't fall or injure yourself. After recovering, staff will assess whether to continue or defer you. If you have frequent cataplexy, you should discuss the realistic risks with the center medical director before attempting donation—your safety is paramount."
            ),
        ]
    },
    {
        'slug': 'can-you-donate-plasma-on-adderall-adhd-2026',
        'title': 'Can You Donate Plasma on Adderall or With ADHD? [2026 Guide]',
        'meta': 'ADHD diagnosis doesn\'t disqualify you, and most stimulant medications including Adderall are allowed with valid prescription. Complete 2026 eligibility guide.',
        'category': 'Medical Eligibility',
        'read_time': 8,
        'toc': [
            ('quick-answer', 'Quick Answer'),
            ('adhd-diagnosis', 'ADHD Diagnosis and Eligibility'),
            ('stimulants', 'Stimulant Medications (Allowed)'),
            ('non-stimulants', 'Non-Stimulant ADHD Medications'),
            ('screening', 'Prescription Verification Process'),
            ('tips', 'Donation Tips for ADHD Patients'),
        ],
        'content': f'''
<div class="quick-answer">
<h3>Quick Answer: Can You Donate Plasma on Adderall?</h3>
<p><strong>Yes, you can donate plasma while taking Adderall or other ADHD stimulant medications.</strong> ADHD diagnosis alone doesn't disqualify you, and most centers accept donors on prescribed stimulants (amphetamines, methylphenidate) as long as you have a valid prescription and are stable on your medication. You'll need to bring proof of prescription at your first visit.</p>
</div>

<h2 id="adhd-diagnosis">ADHD Diagnosis and Eligibility</h2>

<p>Good news: ADHD is one of the few mental health conditions that rarely disqualifies plasma donation.</p>

<h3>Why ADHD Doesn't Disqualify You</h3>

<ul>
<li><strong>Not immunosuppressive:</strong> ADHD medications don't affect immune function</li>
<li><strong>Doesn't affect plasma quality:</strong> Stimulants don't create problematic antibodies or proteins</li>
<li><strong>Common condition:</strong> Up to 10% of adults have ADHD; excluding them would severely limit donor pool</li>
<li><strong>Stable medications:</strong> Most ADHD patients are on consistent regimens</li>
</ul>

<h3>When You CAN Donate</h3>

<ul>
<li><strong>Valid prescription:</strong> Legally prescribed ADHD medication from licensed physician</li>
<li><strong>Stable regimen:</strong> On current medication for at least 30 days</li>
<li><strong>No substance abuse:</strong> Taking medication as prescribed, not misusing it</li>
<li><strong>Can focus:</strong> Able to sit still and follow instructions for 1-2 hours</li>
<li><strong>Cardiovascular health:</strong> No heart problems exacerbated by stimulants</li>
</ul>

<h3>When You're Deferred</h3>

<ul>
<li><strong>No prescription:</strong> Using stimulants recreationally or without doctor supervision</li>
<li><strong>Recent medication change:</strong> Started new ADHD med within past 30 days</li>
<li><strong>Cardiovascular issues:</strong> High blood pressure not controlled, heart arrhythmia, recent cardiac event</li>
<li><strong>Substance abuse history:</strong> Active drug or alcohol use disorder</li>
<li><strong>Misuse concerns:</strong> Taking more than prescribed or using non-prescribed stimulants</li>
</ul>

{AFFILIATE_BLOCK}

<h2 id="stimulants">Stimulant Medications (Allowed)</h2>

<h3>Amphetamine-Based Stimulants</h3>

<table>
<thead>
<tr>
<th>Medication</th>
<th>Brand Name</th>
<th>Donation Status</th>
</tr>
</thead>
<tbody>
<tr>
<td>Amphetamine/dextroamphetamine</td>
<td>Adderall, Adderall XR</td>
<td>✓ Allowed with prescription</td>
</tr>
<tr>
<td>Lisdexamfetamine</td>
<td>Vyvanse</td>
<td>✓ Allowed with prescription</td>
</tr>
<tr>
<td>Dextroamphetamine</td>
<td>Dexedrine, ProCentra</td>
<td>✓ Allowed with prescription</td>
</tr>
<tr>
<td>Amphetamine sulfate</td>
<td>Evekeo, Dyanavel XR</td>
<td>✓ Allowed with prescription</td>
</tr>
</tbody>
</table>

<h3>Methylphenidate-Based Stimulants</h3>

<table>
<thead>
<tr>
<th>Medication</th>
<th>Brand Name</th>
<th>Donation Status</th>
</tr>
</thead>
<tbody>
<tr>
<td>Methylphenidate</td>
<td>Ritalin, Ritalin LA</td>
<td>✓ Allowed with prescription</td>
</tr>
<tr>
<td>Methylphenidate ER</td>
<td>Concerta, Metadate CD</td>
<td>✓ Allowed with prescription</td>
</tr>
<tr>
<td>Dexmethylphenidate</td>
<td>Focalin, Focalin XR</td>
<td>✓ Allowed with prescription</td>
</tr>
<tr>
<td>Methylphenidate patch</td>
<td>Daytrana</td>
<td>✓ Allowed with prescription</td>
</tr>
</tbody>
</table>

{PRO_TOOLKIT}

<h2 id="non-stimulants">Non-Stimulant ADHD Medications</h2>

<h3>Non-Stimulant Options (All Allowed)</h3>

<table>
<thead>
<tr>
<th>Medication</th>
<th>Brand Name</th>
<th>Donation Status</th>
</tr>
</thead>
<tbody>
<tr>
<td>Atomoxetine</td>
<td>Strattera</td>
<td>✓ Allowed</td>
</tr>
<tr>
<td>Viloxazine</td>
<td>Qelbree</td>
<td>✓ Allowed</td>
</tr>
<tr>
<td>Clonidine ER</td>
<td>Kapvay</td>
<td>✓ Usually allowed (check blood pressure)</td>
</tr>
<tr>
<td>Guanfacine ER</td>
<td>Intuniv</td>
<td>✓ Usually allowed (check blood pressure)</td>
</tr>
<tr>
<td>Bupropion</td>
<td>Wellbutrin (off-label for ADHD)</td>
<td>✓ Allowed</td>
</tr>
</tbody>
</table>

<h3>Why Non-Stimulants Are Easier</h3>

<ul>
<li>No controlled substance tracking required</li>
<li>Less cardiovascular impact</li>
<li>No misuse potential concerns</li>
<li>More straightforward screening process</li>
</ul>

<h2 id="screening">Prescription Verification Process</h2>

<h3>What Documentation You Need</h3>

<p>At your first donation appointment, bring:</p>

<ul>
<li><strong>Prescription bottle:</strong> With your name, medication, dose, and prescribing doctor</li>
<li><strong>Pharmacy printout:</strong> Recent fill history showing ongoing prescription</li>
<li><strong>Doctor's contact info:</strong> Name and phone number of prescribing physician</li>
<li><strong>Photo ID:</strong> Matches name on prescription</li>
</ul>

<h3>Questions Staff Will Ask</h3>

<ol>
<li><strong>"What medication do you take for ADHD?"</strong></li>
<li><strong>"What dose and how often?"</strong></li>
<li><strong>"How long have you been on this medication?"</strong></li>
<li><strong>"Who prescribed it?"</strong></li>
<li><strong>"Have you had any recent dose changes?"</strong></li>
<li><strong>"Do you have any heart problems?"</strong></li>
<li><strong>"Have you ever been treated for substance abuse?"</strong></li>
</ol>

<h3>Controlled Substance Database Check</h3>

<p>Most states maintain prescription drug monitoring programs (PDMP):</p>

<ul>
<li>Center may verify your prescription through state database</li>
<li>Checks for multiple prescribers (potential "doctor shopping")</li>
<li>Confirms prescription dates and refill pattern</li>
<li>Ensures you're not obtaining stimulants from multiple sources</li>
</ul>

<h3>Center Policies Vary</h3>

<p>Some centers are stricter than others:</p>

<ul>
<li><strong>Liberal policy:</strong> Accept prescription bottle, quick verification</li>
<li><strong>Moderate policy:</strong> Call prescribing doctor to confirm</li>
<li><strong>Strict policy:</strong> Require written doctor's note for controlled substances</li>
</ul>

<p><strong>Pro tip:</strong> Call ahead to ask what documentation your specific center requires for ADHD medication.</p>

<h2 id="tips">Donation Tips for ADHD Patients</h2>

<h3>Managing Hyperactivity During Donation</h3>

<p>Sitting still for 1-2 hours can be challenging with ADHD:</p>

<ul>
<li><strong>Time donation:</strong> Schedule 1-2 hours after taking medication (peak effectiveness)</li>
<li><strong>Bring distractions:</strong> Audiobook, podcast, phone games, fidget toy for free hand</li>
<li><strong>Use leg movement:</strong> Subtle foot tapping or leg shifts (doesn't affect arm donation)</li>
<li><strong>Request specific seating:</strong> Position where you can see activity (less boring)</li>
<li><strong>Take breaks:</strong> If you need to adjust position, alert staff first</li>
</ul>

<h3>Before Donation</h3>

<ul>
<li><strong>Take medication as usual:</strong> Don't skip your dose</li>
<li><strong>Eat protein breakfast:</strong> Helps maintain blood sugar and focus</li>
<li><strong>Hydrate well:</strong> 16-20 oz water 2-3 hours before (helps veins, too)</li>
<li><strong>Avoid extra caffeine:</strong> Can increase jitteriness with stimulants</li>
<li><strong>Plan timing:</strong> Not right after medication wears off (increased restlessness)</li>
</ul>

<h3>During Donation</h3>

<ul>
<li><strong>Tell staff about ADHD:</strong> They can provide extra reminders and check-ins</li>
<li><strong>Set phone alarms:</strong> Remind yourself not to move donation arm</li>
<li><strong>Use noise-cancelling headphones:</strong> Blocks distracting center noise</li>
<li><strong>Engage staff in conversation:</strong> Helps time pass faster</li>
<li><strong>Track progress:</strong> Ask for time updates to stay motivated</li>
</ul>

<h3>After Donation</h3>

<ul>
<li><strong>Don't rush:</strong> Take full recommended rest time (15 minutes)</li>
<li><strong>Eat snacks:</strong> Protein and complex carbs help recovery</li>
<li><strong>Hydrate more:</strong> 8-10 glasses water over next 24 hours</li>
<li><strong>Avoid intense exercise:</strong> Wait 4-6 hours</li>
<li><strong>Continue medications:</strong> Maintain regular schedule</li>
</ul>

<h3>Managing Impulsivity and Appointments</h3>

<ul>
<li><strong>Set multiple reminders:</strong> Phone alerts for appointment</li>
<li><strong>Schedule regularly:</strong> Same day/time each week (creates routine)</li>
<li><strong>Calendar blocking:</strong> Block 3 hours (travel, donation, recovery)</li>
<li><strong>Pair with routine:</strong> Always go after work/class</li>
<li><strong>Accountability partner:</strong> Text friend when heading to appointment</li>
</ul>

<h3>Cardiovascular Monitoring</h3>

<p>Stimulant medications and plasma donation both stress the cardiovascular system:</p>

<ul>
<li><strong>Blood pressure checks:</strong> Monitor at each donation (stimulants can raise BP)</li>
<li><strong>Heart rate monitoring:</strong> Tell staff if you notice irregular heartbeat</li>
<li><strong>Stay hydrated:</strong> Reduces cardiovascular stress</li>
<li><strong>Report symptoms:</strong> Chest tightness, palpitations, dizziness</li>
<li><strong>Annual physical:</strong> Maintain regular checkups with prescribing doctor</li>
</ul>

<h3>When to Pause Donations</h3>

<ul>
<li>Starting new ADHD medication (wait 30 days for stability)</li>
<li>Dose increase or decrease (wait 2 weeks)</li>
<li>Blood pressure consistently elevated (>140/90)</li>
<li>Heart palpitations or arrhythmia</li>
<li>Difficulty sitting still even with medication</li>
</ul>

{related_reading([
    ('/blog/can-you-donate-plasma-with-narcolepsy-2026', 'Narcolepsy and Stimulant Medications'),
    ('/blog/can-you-donate-plasma-on-antidepressants-2026', 'Antidepressants and Plasma Donation'),
    ('/blog/prescription-medications-plasma-donation-guide', 'Complete Prescription Medication Guide')
])}

{footer_related()}
''',
        'faqs': [
            make_faq(
                "Do I need to bring my prescription bottle every time I donate?",
                "Usually only at your first visit or when your prescription changes. After initial verification, the center will have your medication information on file. However, if you switch doses, change to a different ADHD medication, or change pharmacies, bring updated documentation. Some centers do periodic re-verification (every 6-12 months) for controlled substances."
            ),
            make_faq(
                "Will my Adderall levels in plasma affect the recipients?",
                "No. The amount of medication in your plasma is minimal, and all plasma undergoes extensive processing and testing before use. Therapeutic plasma products are manufactured from pooled plasma from thousands of donors, further diluting any trace medication amounts. The screening is more about ensuring you have a legitimate prescription and aren't misusing controlled substances."
            ),
            make_faq(
                "Can I donate if I take Adderall recreationally without a prescription?",
                "Absolutely not. Using stimulants without a prescription is illegal and will permanently disqualify you from plasma donation. Centers verify prescriptions through databases and doctor contacts. If caught lying about prescription status, you'll be banned and could face legal consequences. If you need ADHD treatment, see a psychiatrist for proper evaluation and prescription."
            ),
            make_faq(
                "What if I'm on Adderall for narcolepsy instead of ADHD?",
                "That's fine—Adderall and other stimulants are FDA-approved for narcolepsy. Just provide your prescription documentation showing narcolepsy as the indication. The screening process is the same. If you're also on sodium oxybate (Xyrem/Xywav) for narcolepsy, that medication would disqualify you regardless of the Adderall."
            ),
            make_faq(
                "Can donation affect my ADHD symptoms or medication effectiveness?",
                "Plasma donation shouldn't significantly affect ADHD medication levels since stimulants primarily bind to tissues and cells, not plasma proteins. However, dehydration from donation could potentially make you feel more scatterbrained or fatigued. Drink plenty of water before and after donating, and if you notice any change in symptom control, consult your prescribing doctor."
            ),
        ]
    },
    {
        'slug': 'can-you-donate-plasma-with-concussion-2026',
        'title': 'Can You Donate Plasma With a Concussion or Whiplash? [2026 Guide]',
        'meta': 'Recent concussion or head injury = temporary deferral. Learn waiting periods, symptom requirements, and when you can safely donate after TBI or whiplash.',
        'category': 'Medical Eligibility',
        'read_time': 7,
        'toc': [
            ('quick-answer', 'Quick Answer'),
            ('concussion-deferral', 'Concussion and TBI Deferral Periods'),
            ('symptoms', 'Post-Concussion Symptoms'),
            ('whiplash', 'Whiplash and Neck Injuries'),
            ('screening', 'What Screening Staff Will Check'),
            ('returning', 'Safe Return to Donation'),
        ],
        'content': f'''
<div class="quick-answer">
<h3>Quick Answer: Can You Donate With a Concussion?</h3>
<p><strong>Not immediately—you must wait until fully recovered.</strong> Plasma centers defer donors with recent concussions (typically 3-6 months) until all symptoms resolve. Minor whiplash without head injury may clear faster (1-3 months). You'll need medical clearance if symptoms lasted more than a few weeks or if you had severe head trauma.</p>
</div>

<h2 id="concussion-deferral">Concussion and TBI Deferral Periods</h2>

<h3>Why Concussions Disqualify You</h3>

<ul>
<li><strong>Blood pressure fluctuations:</strong> Plasma donation can lower BP, worsening concussion symptoms</li>
<li><strong>Increased bleed risk:</strong> Brain may still be healing from microhemorrhages</li>
<li><strong>Syncope risk:</strong> Post-concussion patients more prone to fainting</li>
<li><strong>Cognitive impairment:</strong> May not be able to recognize or report adverse reactions</li>
<li><strong>Hydration stress:</strong> Fluid shifts from donation can worsen headaches and dizziness</li>
</ul>

<h3>Standard Waiting Periods</h3>

<table>
<thead>
<tr>
<th>Injury Severity</th>
<th>Description</th>
<th>Typical Deferral</th>
</tr>
</thead>
<tbody>
<tr>
<td>Mild concussion</td>
<td>Brief LOC (<1 min), no imaging abnormalities, symptoms resolved in 1-2 weeks</td>
<td>3 months symptom-free</td>
</tr>
<tr>
<td>Moderate concussion</td>
<td>LOC 1-30 min, post-traumatic amnesia, symptoms lasted weeks</td>
<td>6 months symptom-free</td>
</tr>
<tr>
<td>Severe TBI</td>
<td>LOC >30 min, brain imaging abnormalities, hospitalization</td>
<td>12 months + doctor clearance</td>
</tr>
<tr>
<td>Repeat concussion</td>
<td>Second concussion within 12 months</td>
<td>6-12 months + neurology clearance</td>
</tr>
<tr>
<td>Post-concussion syndrome</td>
<td>Symptoms persisting >3 months</td>
<td>Until resolved + 6 months</td>
</tr>
</tbody>
</table>

<p><strong>Note:</strong> "Symptom-free" means WITHOUT medication. If you need pain medication for post-concussion headaches, the clock hasn't started yet.</p>

{AFFILIATE_BLOCK}

<h2 id="symptoms">Post-Concussion Symptoms</h2>

<p>You cannot donate if experiencing ANY of these symptoms:</p>

<h3>Physical Symptoms</h3>

<ul>
<li><strong>Headaches:</strong> Any frequency or severity</li>
<li><strong>Dizziness or balance problems</strong></li>
<li><strong>Nausea or vomiting</strong></li>
<li><strong>Vision changes:</strong> Blurry vision, double vision, light sensitivity</li>
<li><strong>Hearing changes:</strong> Ringing in ears (tinnitus), sound sensitivity</li>
<li><strong>Fatigue or drowsiness:</strong> More than baseline</li>
<li><strong>Sleep disturbances:</strong> Insomnia or sleeping more than usual</li>
</ul>

<h3>Cognitive Symptoms</h3>

<ul>
<li><strong>Difficulty concentrating or focusing</strong></li>
<li><strong>Memory problems:</strong> Short-term memory issues</li>
<li><strong>Confusion or feeling "foggy"</strong></li>
<li><strong>Slowed thinking or processing</strong></li>
<li><strong>Difficulty with decision-making</strong></li>
</ul>

<h3>Emotional/Behavioral Symptoms</h3>

<ul>
<li><strong>Irritability or mood swings</strong></li>
<li><strong>Anxiety or nervousness</strong></li>
<li><strong>Depression or sadness</strong></li>
<li><strong>Personality changes</strong></li>
</ul>

<h3>Red Flags for Extended Deferral</h3>

<p>If you experienced any of these, you'll need neurology clearance:</p>

<ul>
<li>Loss of consciousness >5 minutes</li>
<li>Seizure after injury</li>
<li>Repeated vomiting</li>
<li>Severe or worsening headache</li>
<li>Unequal pupils</li>
<li>Clear fluid draining from nose/ears</li>
<li>Weakness or numbness in limbs</li>
<li>Slurred speech</li>
<li>Blood-thinning medication prescribed after injury</li>
</ul>

{PRO_TOOLKIT}

<h2 id="whiplash">Whiplash and Neck Injuries</h2>

<h3>Whiplash Without Head Impact</h3>

<p>Pure whiplash (neck strain without head injury) has shorter deferral:</p>

<table>
<thead>
<tr>
<th>Severity</th>
<th>Symptoms</th>
<th>Typical Deferral</th>
</tr>
</thead>
<tbody>
<tr>
<td>Grade 1 (Mild)</td>
<td>Neck pain/stiffness only, no physical findings</td>
<td>2-4 weeks symptom-free</td>
</tr>
<tr>
<td>Grade 2 (Moderate)</td>
<td>Neck pain + musculoskeletal findings (reduced range of motion)</td>
<td>4-8 weeks symptom-free</td>
</tr>
<tr>
<td>Grade 3 (Severe)</td>
<td>Neck pain + neurological signs (numbness, weakness)</td>
<td>3 months + doctor clearance</td>
</tr>
</tbody>
</table>

<h3>When Whiplash Becomes Concussion Deferral</h3>

<p>If whiplash included any of these, use concussion waiting periods:</p>

<ul>
<li>Head struck dashboard, window, or headrest</li>
<li>Any loss of consciousness (even brief)</li>
<li>Post-traumatic amnesia (can't remember accident)</li>
<li>Headache, dizziness, or cognitive symptoms</li>
<li>Diagnosed with "mild traumatic brain injury"</li>
</ul>

<h2 id="screening">What Screening Staff Will Check</h2>

<h3>Questions About Head Injury History</h3>

<ol>
<li><strong>"Have you had a head injury in the past year?"</strong></li>
<li><strong>"Did you lose consciousness? For how long?"</strong></li>
<li><strong>"Did you seek medical treatment?"</strong></li>
<li><strong>"Were you hospitalized?"</strong></li>
<li><strong>"Did you have a CT scan or MRI?"</strong></li>
<li><strong>"When did your symptoms completely resolve?"</strong></li>
<li><strong>"Are you taking any medication for concussion symptoms?"</strong></li>
<li><strong>"Have you been cleared by a doctor to resume normal activities?"</strong></li>
</ol>

<h3>Physical Assessment</h3>

<p>Staff may perform:</p>

<ul>
<li><strong>Pupil check:</strong> Equal size and reactivity</li>
<li><strong>Balance assessment:</strong> Observe walking to donation chair</li>
<li><strong>Alertness evaluation:</strong> Appropriate responses and orientation</li>
<li><strong>Blood pressure check:</strong> Ensure stable vitals</li>
</ul>

<h3>Documentation Requirements</h3>

<p>For moderate to severe concussions, bring:</p>

<ul>
<li><strong>Medical records:</strong> ER visit summary or neurologist notes</li>
<li><strong>Imaging reports:</strong> CT/MRI results showing resolution</li>
<li><strong>Clearance letter:</strong> Doctor's note stating full recovery</li>
<li><strong>Return-to-work/activity clearance:</strong> Shows you're back to normal function</li>
</ul>

<h2 id="returning">Safe Return to Donation</h2>

<h3>Before You Return</h3>

<p>Ensure you meet ALL these criteria:</p>

<ul>
<li><strong>Zero symptoms:</strong> Completely symptom-free without medication</li>
<li><strong>Passed waiting period:</strong> Appropriate time since injury based on severity</li>
<li><strong>Medical clearance:</strong> Doctor approved return to normal activities</li>
<li><strong>Back to baseline:</strong> Able to work, exercise, and function normally</li>
<li><strong>No medications:</strong> Off all pain relievers, anti-nausea meds, sleep aids</li>
</ul>

<h3>Your First Donation Back</h3>

<ul>
<li><strong>Hydrate extra:</strong> 20+ oz water 2-3 hours before (prevents dizziness)</li>
<li><strong>Eat substantial meal:</strong> Helps maintain blood pressure</li>
<li><strong>Report history:</strong> Tell staff about previous concussion and recovery</li>
<li><strong>Monitor closely:</strong> Alert staff to any headache, dizziness, or nausea</li>
<li><strong>Extended rest:</strong> Take 20-30 minutes in recovery area</li>
<li><strong>Arrange backup transport:</strong> Have someone on standby to pick you up if needed</li>
</ul>

<h3>Warning Signs to Stop</h3>

<p>If you experience these after returning to donation, stop and see a doctor:</p>

<ul>
<li>Return of headaches (especially severe or persistent)</li>
<li>Dizziness or balance problems</li>
<li>Cognitive symptoms (brain fog, memory issues)</li>
<li>Unusual fatigue lasting days after donation</li>
<li>Mood changes or irritability</li>
<li>Sleep disturbances</li>
</ul>

<h3>Long-Term Considerations</h3>

<ul>
<li><strong>Monitor for cumulative effects:</strong> Multiple concussions increase long-term risk</li>
<li><strong>Consider reduced frequency:</strong> Once weekly instead of twice weekly</li>
<li><strong>Track symptoms:</strong> Keep log of how you feel after donations</li>
<li><strong>Annual neurological check:</strong> If you have history of multiple concussions</li>
</ul>

{related_reading([
    ('/blog/plasma-donation-after-surgery-complete-guide', 'Post-Surgery Donation Guidelines'),
    ('/blog/can-you-donate-plasma-after-accident-injury', 'Accident and Injury Deferral Periods'),
    ('/blog/plasma-donation-health-screening-process', 'Complete Health Screening Guide')
])}

{footer_related()}
''',
        'faqs': [
            make_faq(
                "Can I donate if my concussion was years ago and I'm completely fine now?",
                "Yes, as long as you fully recovered and have had no lingering symptoms. If your concussion was more than a year ago, you're symptom-free, and back to all normal activities, most centers will accept you. Be honest about the history during screening—staff may ask additional questions but shouldn't defer you for a fully resolved old injury."
            ),
            make_faq(
                "What if I get headaches after donating—could it be from my old concussion?",
                "Post-donation headaches are common in all donors (usually dehydration-related), but if you have concussion history and develop unusual headaches after donation, take it seriously. Stop donating and consult your doctor. Post-concussion syndrome can sometimes be triggered by physical stressors like plasma donation, even years after the initial injury."
            ),
            make_faq(
                "Do I need to report minor head bumps that didn't cause symptoms?",
                "If you had no loss of consciousness, no symptoms, and didn't seek medical care for a minor bump, it's generally not considered a concussion and doesn't need extensive disclosure. However, if asked specifically about head injuries, err on the side of honesty—let screening staff determine significance rather than self-editing your medical history."
            ),
            make_faq(
                "Can I donate if I have chronic headaches from an old concussion?",
                "No, ongoing symptoms from a previous concussion disqualify you from donation. Chronic post-concussion syndrome means your brain hasn't fully healed. Plasma donation could worsen symptoms and is contraindicated. Focus on working with a neurologist to manage your symptoms rather than attempting to donate."
            ),
            make_faq(
                "What if I got whiplash from a car accident but didn't hit my head?",
                "Pure whiplash without head impact has shorter deferral periods than concussion—typically just until neck pain and stiffness completely resolve (2-8 weeks depending on severity). However, be thorough in assessing whether you truly had no head symptoms. Many people with whiplash have minor concussions they don't realize because symptoms are mild. If you had any dizziness, headache, or cognitive symptoms after the accident, use concussion deferral guidelines."
            ),
        ]
    },
    {
        'slug': 'can-you-donate-plasma-with-kidney-disease-2026',
        'title': 'Can You Donate Plasma With Kidney Disease or CKD? [2026 Guide]',
        'meta': 'Chronic kidney disease usually disqualifies plasma donation due to protein loss and electrolyte stress. Complete CKD, kidney stones, and GFR eligibility guide.',
        'category': 'Medical Eligibility',
        'read_time': 9,
        'toc': [
            ('quick-answer', 'Quick Answer'),
            ('why-disqualified', 'Why Kidney Disease Disqualifies You'),
            ('ckd-stages', 'CKD Stages and Eligibility'),
            ('kidney-stones', 'Kidney Stones and Donation'),
            ('screening', 'Kidney Function Screening'),
            ('dialysis', 'Dialysis Patients'),
        ],
        'content': f'''
<div class="quick-answer">
<h3>Quick Answer: Can You Donate Plasma With Kidney Disease?</h3>
<p><strong>No, chronic kidney disease (CKD) is a permanent deferral from plasma donation.</strong> The process removes plasma proteins that kidneys must work hard to replace, creating dangerous stress on already compromised kidney function. Even early-stage CKD (stage 2) usually disqualifies you. However, history of kidney stones may be acceptable after full recovery.</p>
</div>

<h2 id="why-disqualified">Why Kidney Disease Disqualifies You</h2>

<h3>The Kidney-Plasma Connection</h3>

<p>Kidneys play a critical role in maintaining the proteins removed during plasma donation:</p>

<ul>
<li><strong>Protein conservation:</strong> Healthy kidneys retain plasma proteins (albumin, immunoglobulins)</li>
<li><strong>Protein synthesis regulation:</strong> Kidneys signal liver to produce more protein after plasma loss</li>
<li><strong>Fluid/electrolyte balance:</strong> Plasma donation creates fluid shifts that stress kidney function</li>
<li><strong>Toxin filtering:</strong> Diseased kidneys can't handle additional metabolic stress</li>
</ul>

<h3>Dangers of Donation With Kidney Disease</h3>

<ul>
<li><strong>Proteinuria worsening:</strong> Protein loss from donation exacerbates protein in urine</li>
<li><strong>GFR decline acceleration:</strong> Physical stress can speed kidney function deterioration</li>
<li><strong>Electrolyte imbalance:</strong> Citrate anticoagulant affects calcium/potassium balance</li>
<li><strong>Volume depletion:</strong> Fluid loss dangerous for patients with impaired kidney regulation</li>
<li><strong>Uremia risk:</strong> Advanced CKD patients accumulate toxins donation could worsen</li>
<li><strong>Anemia worsening:</strong> CKD causes anemia; plasma donation compounds this</li>
</ul>

{AFFILIATE_BLOCK}

<h2 id="ckd-stages">CKD Stages and Eligibility</h2>

<h3>Understanding CKD Stages</h3>

<table>
<thead>
<tr>
<th>CKD Stage</th>
<th>GFR (mL/min/1.73m²)</th>
<th>Description</th>
<th>Donation Eligibility</th>
</tr>
</thead>
<tbody>
<tr>
<td>Stage 1</td>
<td>≥90</td>
<td>Normal GFR with kidney damage (proteinuria, structural abnormality)</td>
<td>❌ Deferred (kidney damage present)</td>
</tr>
<tr>
<td>Stage 2</td>
<td>60-89</td>
<td>Mild GFR reduction with kidney damage</td>
<td>❌ Deferred</td>
</tr>
<tr>
<td>Stage 3a</td>
<td>45-59</td>
<td>Mild to moderate GFR reduction</td>
<td>❌ Deferred</td>
</tr>
<tr>
<td>Stage 3b</td>
<td>30-44</td>
<td>Moderate to severe GFR reduction</td>
<td>❌ Deferred</td>
</tr>
<tr>
<td>Stage 4</td>
<td>15-29</td>
<td>Severe GFR reduction</td>
<td>❌ Deferred</td>
</tr>
<tr>
<td>Stage 5</td>
<td><15 or dialysis</td>
<td>Kidney failure</td>
<td>❌ Permanent deferral</td>
</tr>
</tbody>
</table>

<p><strong>Important:</strong> ANY stage of CKD disqualifies you, even with normal GFR, if there's evidence of kidney damage (protein in urine, imaging abnormalities, etc.).</p>

<h3>Related Kidney Conditions That Disqualify</h3>

<ul>
<li><strong>Polycystic kidney disease (PKD):</strong> Permanent deferral</li>
<li><strong>Glomerulonephritis:</strong> Permanent deferral (autoimmune kidney inflammation)</li>
<li><strong>Diabetic nephropathy:</strong> Permanent deferral</li>
<li><strong>Hypertensive nephropathy:</strong> Permanent deferral</li>
<li><strong>IgA nephropathy:</strong> Permanent deferral (even if GFR normal)</li>
<li><strong>Kidney transplant recipient:</strong> Permanent deferral (immunosuppression)</li>
<li><strong>Kidney donor:</strong> Usually permanent deferral (single kidney more vulnerable)</li>
</ul>

{PRO_TOOLKIT}

<h3>How Centers Detect Kidney Disease</h3>

<p>Standard plasma donation screening includes:</p>

<ul>
<li><strong>Protein screening:</strong> Finger-stick test measures total protein (can indicate kidney issues)</li>
<li><strong>Medical history:</strong> Questions about kidney disease, high blood pressure, diabetes</li>
<li><strong>Urinalysis:</strong> Some centers check for protein in urine</li>
<li><strong>Vital signs:</strong> High blood pressure may prompt kidney function questions</li>
</ul>

<p><strong>Note:</strong> Standard screening doesn't include GFR calculation—but medical history disclosure should prevent donation if you know you have CKD.</p>

<h2 id="kidney-stones">Kidney Stones and Donation</h2>

<p>Unlike chronic kidney disease, kidney stone history may be acceptable after recovery:</p>

<h3>When You CAN Donate (Kidney Stones)</h3>

<table>
<thead>
<tr>
<th>Situation</th>
<th>Waiting Period</th>
<th>Requirements</th>
</tr>
</thead>
<tbody>
<tr>
<td>Single kidney stone, passed naturally</td>
<td>30 days after passing</td>
<td>Completely pain-free, no complications</td>
</tr>
<tr>
<td>Kidney stone, removed surgically</td>
<td>3-6 months after surgery</td>
<td>Full recovery, no complications, doctor clearance</td>
</tr>
<tr>
<td>Lithotripsy (shock wave)</td>
<td>6-8 weeks after procedure</td>
<td>Stone fragments passed, no pain</td>
</tr>
<tr>
<td>Single stone 5+ years ago</td>
<td>No waiting (if no recurrence)</td>
<td>No current symptoms or kidney damage</td>
</tr>
</tbody>
</table>

<h3>When You're Deferred (Kidney Stones)</h3>

<ul>
<li><strong>Active stone:</strong> Currently have stone causing symptoms</li>
<li><strong>Recurrent stones:</strong> 3+ stones in past 5 years (may indicate chronic issue)</li>
<li><strong>Ongoing pain:</strong> Any kidney/flank pain</li>
<li><strong>Kidney damage:</strong> Stones caused hydronephrosis, infection, or GFR reduction</li>
<li><strong>Metabolic disorder:</strong> Cystinuria, hyperoxaluria, or other stone-forming conditions</li>
</ul>

<h3>What to Tell Screening Staff</h3>

<p>If you have kidney stone history:</p>

<ol>
<li><strong>How many stones:</strong> Total number and timeframe</li>
<li><strong>When last stone occurred:</strong> Exact date stone passed or was removed</li>
<li><strong>Stone composition:</strong> Calcium oxalate, uric acid, struvite, etc. (if known)</li>
<li><strong>Treatment required:</strong> Passed naturally, surgery, lithotripsy</li>
<li><strong>Complications:</strong> Any infections, blockages, or kidney damage</li>
<li><strong>Current symptoms:</strong> Any ongoing pain or urinary issues</li>
<li><strong>Prevention measures:</strong> Diet changes, medications (potassium citrate, etc.)</li>
</ol>

<h2 id="screening">Kidney Function Screening</h2>

<h3>Standard Tests</h3>

<p>If you're concerned about kidney function, get these tests before attempting donation:</p>

<ul>
<li><strong>Serum creatinine:</strong> Elevated levels indicate reduced kidney function</li>
<li><strong>eGFR calculation:</strong> Estimated glomerular filtration rate (should be >90)</li>
<li><strong>Blood urea nitrogen (BUN):</strong> Waste product filtered by kidneys</li>
<li><strong>Urinalysis:</strong> Checks for protein, blood, glucose in urine</li>
<li><strong>Urine albumin-to-creatinine ratio (UACR):</strong> Detects early kidney damage</li>
</ul>

<h3>Risk Factors for Kidney Disease</h3>

<p>If you have these risk factors, get kidney function tested before donating:</p>

<ul>
<li><strong>Diabetes:</strong> Type 1 or type 2 (leading cause of kidney disease)</li>
<li><strong>High blood pressure:</strong> Uncontrolled hypertension damages kidneys</li>
<li><strong>Family history:</strong> Parent or sibling with kidney disease</li>
<li><strong>Age over 60:</strong> GFR naturally declines with age</li>
<li><strong>Obesity:</strong> BMI >30 increases kidney disease risk</li>
<li><strong>Heart disease:</strong> Cardiovascular and kidney health linked</li>
<li><strong>Smoking:</strong> Accelerates kidney function decline</li>
<li><strong>Frequent NSAIDs:</strong> Regular ibuprofen/naproxen use can damage kidneys</li>
</ul>

<h2 id="dialysis">Dialysis Patients</h2>

<h3>Can Dialysis Patients Donate Plasma?</h3>

<p><strong>Absolutely not.</strong> This is a permanent, non-negotiable deferral for multiple reasons:</p>

<h3>Why Dialysis Patients Cannot Donate</h3>

<ul>
<li><strong>End-stage renal disease:</strong> Complete kidney failure</li>
<li><strong>Vascular access preservation:</strong> Dialysis fistulas/grafts must be protected</li>
<li><strong>Severe anemia:</strong> Dialysis patients already have low blood counts</li>
<li><strong>Protein needs:</strong> Already struggle to maintain adequate protein levels</li>
<li><strong>Fluid balance:</strong> Strict fluid restrictions incompatible with plasma donation</li>
<li><strong>Immunosuppression:</strong> Increased infection risk</li>
<li><strong>Anticoagulation:</strong> Many dialysis patients on blood thinners</li>
<li><strong>Electrolyte instability:</strong> Citrate anticoagulant dangerous for ESRD patients</li>
</ul>

<h3>Can You Receive Plasma Products if You Can't Donate?</h3>

<p>Yes—this is an important distinction:</p>

<ul>
<li>Dialysis patients can RECEIVE plasma-derived medications (albumin, immunoglobulins)</li>
<li>They cannot DONATE plasma to help manufacture these products</li>
<li>Your contribution can be encouraging others to donate</li>
</ul>

{related_reading([
    ('/blog/can-you-donate-plasma-with-diabetes-complete-guide', 'Diabetes and Plasma Donation'),
    ('/blog/can-you-donate-plasma-with-high-blood-pressure', 'Hypertension Eligibility Guide'),
    ('/blog/can-you-donate-plasma-with-uti-2026', 'UTI and Urinary Issues')
])}

{footer_related()}
''',
        'faqs': [
            make_faq(
                "Can I donate if I have only one kidney?",
                "Most plasma centers permanently defer people with solitary kidneys (whether from birth, donation, or surgical removal). A single kidney must work twice as hard and can't afford the additional stress of plasma donation's protein loss. Some centers might consider you with exceptional kidney function and nephrologist clearance, but this is very rare. Your single kidney is too precious to risk."
            ),
            make_faq(
                "What if my kidney disease is very mild and well-controlled?",
                "Even early-stage CKD with normal or near-normal GFR creates permanent deferral because ANY kidney damage means reduced reserve capacity. The kidneys can't handle the repeated stress of replacing lost plasma proteins twice weekly. Centers can't make exceptions—the policy protects your long-term kidney health. Focus on preserving your remaining function rather than attempting to donate."
            ),
            make_faq(
                "Will plasma donation show if I have kidney disease I don't know about?",
                "Not reliably. Standard screening includes a protein test that might indicate kidney issues if significantly abnormal, but it's not designed to diagnose kidney disease. If you have risk factors (diabetes, hypertension, family history), get proper kidney function testing (GFR, urinalysis) through your doctor before attempting donation. Don't use plasma screening as a substitute for medical care."
            ),
            make_faq(
                "Can I donate if I had a kidney infection (pyelonephritis)?",
                "If you had a single kidney infection that completely resolved with antibiotics and caused no lasting kidney damage, you can donate after the standard 14-day post-antibiotic waiting period. However, if you have recurrent kidney infections (3+ per year), reduced GFR, or kidney scarring from infection, you'll likely be deferred. Bring medical records showing complete recovery."
            ),
            make_faq(
                "What if I'm a living kidney donor—can I donate plasma?",
                "Living kidney donors are usually permanently deferred from plasma donation. While your remaining kidney compensates well for normal life activities, the repeated protein loss from plasma donation creates unnecessary risk. Some centers might reconsider after 2+ years with perfect kidney function and nephrologist clearance, but most maintain permanent deferral. You've already made an incredible donation by giving a kidney."
            ),
        ]
    },
    {
        'slug': 'can-you-donate-plasma-on-antidepressants-2026',
        'title': 'Can You Donate Plasma on Antidepressants? [2026 Medication Guide]',
        'meta': 'SSRIs, SNRIs, and most antidepressants are allowed for plasma donation if symptoms are stable. Complete guide to depression medications and eligibility.',
        'category': 'Medical Eligibility',
        'read_time': 8,
        'toc': [
            ('quick-answer', 'Quick Answer'),
            ('allowed-medications', 'Antidepressants That Are Allowed'),
            ('disqualifying', 'Medications That May Disqualify'),
            ('symptom-stability', 'Mental Health Stability Requirements'),
            ('screening', 'What Screening Staff Will Ask'),
            ('tips', 'Safe Donation Tips'),
        ],
        'content': f'''
<div class="quick-answer">
<h3>Quick Answer: Can You Donate on Antidepressants?</h3>
<p><strong>Yes, most antidepressants are allowed for plasma donation.</strong> SSRIs (Prozac, Zoloft, Lexapro), SNRIs (Effexor, Cymbalta), Wellbutrin, and many others are acceptable as long as your depression is stable and well-controlled. The focus is on your mental health stability, not the medication itself.</p>
</div>

<h2 id="allowed-medications">Antidepressants That Are Allowed</h2>

<h3>SSRIs (Selective Serotonin Reuptake Inhibitors)</h3>

<table>
<thead>
<tr>
<th>Medication</th>
<th>Brand Name</th>
<th>Donation Status</th>
</tr>
</thead>
<tbody>
<tr>
<td>Fluoxetine</td>
<td>Prozac</td>
<td>✓ Allowed</td>
</tr>
<tr>
<td>Sertraline</td>
<td>Zoloft</td>
<td>✓ Allowed</td>
</tr>
<tr>
<td>Escitalopram</td>
<td>Lexapro</td>
<td>✓ Allowed</td>
</tr>
<tr>
<td>Citalopram</td>
<td>Celexa</td>
<td>✓ Allowed</td>
</tr>
<tr>
<td>Paroxetine</td>
<td>Paxil</td>
<td>✓ Allowed</td>
</tr>
<tr>
<td>Fluvoxamine</td>
<td>Luvox</td>
<td>✓ Allowed</td>
</tr>
</tbody>
</table>

<h3>SNRIs (Serotonin-Norepinephrine Reuptake Inhibitors)</h3>

<table>
<thead>
<tr>
<th>Medication</th>
<th>Brand Name</th>
<th>Donation Status</th>
</tr>
</thead>
<tbody>
<tr>
<td>Venlafaxine</td>
<td>Effexor, Effexor XR</td>
<td>✓ Allowed</td>
</tr>
<tr>
<td>Duloxetine</td>
<td>Cymbalta</td>
<td>✓ Allowed</td>
</tr>
<tr>
<td>Desvenlafaxine</td>
<td>Pristiq</td>
<td>✓ Allowed</td>
</tr>
<tr>
<td>Levomilnacipran</td>
<td>Fetzima</td>
<td>✓ Allowed</td>
</tr>
</tbody>
</table>

<h3>Atypical Antidepressants</h3>

<table>
<thead>
<tr>
<th>Medication</th>
<th>Brand Name</th>
<th>Donation Status</th>
</tr>
</thead>
<tbody>
<tr>
<td>Bupropion</td>
<td>Wellbutrin, Wellbutrin XL</td>
<td>✓ Allowed</td>
</tr>
<tr>
<td>Mirtazapine</td>
<td>Remeron</td>
<td>✓ Allowed</td>
</tr>
<tr>
<td>Trazodone</td>
<td>Desyrel</td>
<td>✓ Allowed</td>
</tr>
<tr>
<td>Vilazodone</td>
<td>Viibryd</td>
<td>✓ Allowed</td>
</tr>
<tr>
<td>Vortioxetine</td>
<td>Trintellix</td>
<td>✓ Allowed</td>
</tr>
</tbody>
</table>

{AFFILIATE_BLOCK}

<h2 id="disqualifying">Medications That May Disqualify</h2>

<h3>MAO Inhibitors (Often Restricted)</h3>

<table>
<thead>
<tr>
<th>Medication</th>
<th>Brand Name</th>
<th>Status</th>
</tr>
</thead>
<tbody>
<tr>
<td>Phenelzine</td>
<td>Nardil</td>
<td>⚠ Check center policy (some defer)</td>
</tr>
<tr>
<td>Tranylcypromine</td>
<td>Parnate</td>
<td>⚠ Check center policy (some defer)</td>
</tr>
<tr>
<td>Isocarboxazid</td>
<td>Marplan</td>
<td>⚠ Check center policy (some defer)</td>
</tr>
<tr>
<td>Selegiline</td>
<td>Emsam (patch)</td>
<td>⚠ Check center policy</td>
</tr>
</tbody>
</table>

<p><strong>Why MAOIs are problematic:</strong> MAO inhibitors have serious drug interactions and dietary restrictions. Some centers defer due to concerns about blood pressure changes during donation. Centers that accept MAO inhibitor users require careful monitoring.</p>

<h3>Tricyclic Antidepressants (Usually Allowed but Monitored)</h3>

<table>
<thead>
<tr>
<th>Medication</th>
<th>Brand Name</th>
<th>Status</th>
</tr>
</thead>
<tbody>
<tr>
<td>Amitriptyline</td>
<td>Elavil</td>
<td>✓ Usually allowed (monitor BP/HR)</td>
</tr>
<tr>
<td>Nortriptyline</td>
<td>Pamelor</td>
<td>✓ Usually allowed</td>
</tr>
<tr>
<td>Imipramine</td>
<td>Tofranil</td>
<td>✓ Usually allowed</td>
</tr>
<tr>
<td>Doxepin</td>
<td>Sinequan</td>
<td>✓ Usually allowed</td>
</tr>
</tbody>
</table>

<p><strong>Monitoring needed:</strong> Tricyclics can affect heart rhythm and blood pressure, so vital signs are checked carefully.</p>

{PRO_TOOLKIT}

<h3>Medications for Treatment-Resistant Depression</h3>

<table>
<thead>
<tr>
<th>Medication</th>
<th>Brand Name</th>
<th>Status</th>
</tr>
</thead>
<tbody>
<tr>
<td>Esketamine nasal spray</td>
<td>Spravato</td>
<td>❌ Likely deferred (requires supervised use, REMS program)</td>
</tr>
<tr>
<td>Lithium</td>
<td>Lithobid, Eskalith</td>
<td>❌ Usually deferred (narrow therapeutic window, electrolyte sensitive)</td>
</tr>
</tbody>
</table>

<h2 id="symptom-stability">Mental Health Stability Requirements</h2>

<h3>When You CAN Donate</h3>

<ul>
<li><strong>Stable symptoms:</strong> Depression well-controlled on current medication</li>
<li><strong>No recent crises:</strong> No suicidal ideation, psychiatric hospitalization, or emergency visits</li>
<li><strong>Medication compliance:</strong> Taking antidepressants as prescribed</li>
<li><strong>Stable regimen:</strong> On current medication/dose for at least 30 days</li>
<li><strong>Functional status:</strong> Able to work, manage daily activities, attend appointments</li>
<li><strong>Capacity to consent:</strong> Can understand donation process and risks</li>
</ul>

<h3>When You're Deferred</h3>

<ul>
<li><strong>Active suicidal ideation:</strong> Current thoughts of self-harm</li>
<li><strong>Recent hospitalization:</strong> Psychiatric admission within past 6-12 months</li>
<li><strong>Medication adjustments:</strong> Recent dose changes or new medication trials within 30 days</li>
<li><strong>Severe symptoms:</strong> Unable to function in daily life</li>
<li><strong>Treatment non-compliance:</strong> Not taking prescribed medications</li>
<li><strong>Co-occurring substance abuse:</strong> Active drug or alcohol use disorder</li>
</ul>

<h3>Why Stability Matters</h3>

<ul>
<li><strong>Stress response:</strong> Donation can be physically stressful; must be emotionally equipped to handle it</li>
<li><strong>Decision-making capacity:</strong> Need clear judgment to consent and recognize adverse reactions</li>
<li><strong>Appointment reliability:</strong> Donation requires consistent attendance</li>
<li><strong>Self-care ability:</strong> Must follow pre/post-donation instructions</li>
</ul>

<h2 id="screening">What Screening Staff Will Ask</h2>

<h3>Mental Health Questions</h3>

<ol>
<li><strong>"Are you currently being treated for depression or anxiety?"</strong></li>
<li><strong>"What medications are you taking?"</strong></li>
<li><strong>"How long have you been on this medication?"</strong></li>
<li><strong>"When was your last dose change?"</strong></li>
<li><strong>"Have you been hospitalized for mental health reasons?"</strong></li>
<li><strong>"Are you experiencing any suicidal thoughts?"</strong></li>
<li><strong>"Are you able to care for yourself and attend appointments reliably?"</strong></li>
</ol>

<h3>What Staff Is Assessing</h3>

<ul>
<li><strong>Symptom control:</strong> Is treatment effectively managing depression?</li>
<li><strong>Medication stability:</strong> Recent changes indicate instability</li>
<li><strong>Safety:</strong> Risk of self-harm or crisis during/after donation</li>
<li><strong>Capacity:</strong> Ability to understand process and give informed consent</li>
<li><strong>Reliability:</strong> Can you commit to donation schedule?</li>
</ul>

<h3>Privacy Considerations</h3>

<ul>
<li>Mental health information is protected under HIPAA</li>
<li>Staff will conduct screening privately</li>
<li>Your depression diagnosis won't be publicly disclosed</li>
<li>Information used only for donation eligibility determination</li>
</ul>

<h2 id="tips">Safe Donation Tips</h2>

<h3>Before Donation</h3>

<ul>
<li><strong>Take medication as prescribed:</strong> Don't skip morning dose</li>
<li><strong>Eat balanced meal:</strong> Low blood sugar can worsen mood</li>
<li><strong>Sleep adequately:</strong> Depression + poor sleep + donation = bad combination</li>
<li><strong>Stay hydrated:</strong> 16-20 oz water 2-3 hours before</li>
<li><strong>Avoid alcohol:</strong> Never mix with antidepressants or donation</li>
</ul>

<h3>During Donation</h3>

<ul>
<li><strong>Bring comfort items:</strong> Music, audiobook, stress ball</li>
<li><strong>Communicate needs:</strong> Tell staff if you're feeling anxious or unwell</li>
<li><strong>Practice relaxation:</strong> Deep breathing, meditation apps</li>
<li><strong>Stay engaged:</strong> Conversation with staff can help time pass</li>
</ul>

<h3>After Donation</h3>

<ul>
<li><strong>Rest adequately:</strong> Don't skip recommended recovery time</li>
<li><strong>Eat protein-rich snacks:</strong> Helps mood and energy</li>
<li><strong>Hydrate well:</strong> 8-10 glasses water over next 24 hours</li>
<li><strong>Monitor mood:</strong> Note any changes in depression symptoms</li>
<li><strong>Self-care:</strong> Prioritize rest and healthy activities</li>
</ul>

<h3>Long-Term Considerations</h3>

<ul>
<li><strong>Track patterns:</strong> Does donation affect your mood? Keep log</li>
<li><strong>Limit frequency if needed:</strong> Weekly instead of twice weekly</li>
<li><strong>Maintain treatment:</strong> Keep all psychiatrist/therapist appointments</li>
<li><strong>Communicate changes:</strong> Tell donation center if medications change</li>
</ul>

<h3>When to Stop Donating</h3>

<ul>
<li>Depression symptoms worsen</li>
<li>Suicidal thoughts emerge</li>
<li>Medication changes or additions</li>
<li>Psychiatric hospitalization</li>
<li>Donation becomes source of stress or anxiety</li>
<li>Unable to maintain donation schedule</li>
</ul>

{related_reading([
    ('/blog/can-you-donate-plasma-with-anxiety-disorder-2026', 'Anxiety Disorders and Plasma Donation'),
    ('/blog/can-you-donate-plasma-with-schizophrenia-2026', 'Antipsychotic Medications Guide'),
    ('/blog/mental-health-medications-plasma-donation-guide', 'Complete Mental Health Medication Guide')
])}

{footer_related()}
''',
        'faqs': [
            make_faq(
                "Will donating plasma affect my antidepressant medication levels?",
                "Plasma donation shouldn't significantly impact antidepressant levels for most medications. These drugs primarily bind to tissues and cells, not just plasma proteins. However, stay well-hydrated to maintain consistent blood volume. If you notice any change in depression symptoms or medication effectiveness after starting donation, consult your prescribing doctor."
            ),
            make_faq(
                "Can I donate if I just started taking antidepressants?",
                "Most centers prefer you wait 30 days after starting a new antidepressant or changing doses before donating. This allows time for the medication to stabilize, side effects to resolve, and ensures your depression is improving. Starting antidepressants can cause initial worsening or activation symptoms—add the stress of donation during this adjustment period isn't advisable."
            ),
            make_faq(
                "Do I need a doctor's note to donate while on antidepressants?",
                "Generally no, as long as your depression is stable and you're on acceptable medications. However, if you have recent psychiatric hospitalization, are on multiple psychiatric medications, or have treatment-resistant depression, some centers may request a clearance letter from your psychiatrist. Call ahead to ask about specific requirements."
            ),
            make_faq(
                "What if I'm tapering off my antidepressant?",
                "Wait until you've completely tapered off and have been medication-free and stable for at least 30 days before donating. Tapering periods can involve withdrawal symptoms, mood fluctuations, and return of depression—all contraindications for plasma donation. Focus on safely discontinuing the medication first, then consider donation later if appropriate."
            ),
            make_faq(
                "Can I donate if I have depression but I'm not on medication?",
                "It depends on symptom severity and stability. If you have mild depression managed with therapy alone and are fully functional with no suicidal ideation, most centers will accept you. However, if you have moderate to severe depression that really should be medicated but isn't, centers may defer you for your own safety. Be honest during screening about symptom severity."
            ),
        ]
    },
    {
        'slug': 'can-you-donate-plasma-with-ibs-crohns-2026',
        'title': 'Can You Donate Plasma With IBS, Crohn\'s, or Ulcerative Colitis? [2026]',
        'meta': 'IBS usually allowed, but Crohn\'s and UC depend on severity and medications. Complete IBD and IBS eligibility guide including biologic deferral rules.',
        'category': 'Medical Eligibility',
        'read_time': 9,
        'toc': [
            ('quick-answer', 'Quick Answer'),
            ('ibs-eligibility', 'IBS (Irritable Bowel Syndrome)'),
            ('ibd-overview', 'IBD: Crohn\'s and Ulcerative Colitis'),
            ('medications', 'IBD Medications and Deferral'),
            ('screening', 'What to Tell Screening Staff'),
            ('tips', 'Managing Donation With GI Issues'),
        ],
        'content': f'''
<div class="quick-answer">
<h3>Quick Answer: Can You Donate With IBS or IBD?</h3>
<p><strong>IBS: Yes, usually allowed if symptoms are controlled.</strong> IBS doesn't affect plasma quality or safety. <strong>Crohn's/UC: It depends on medications.</strong> Mild IBD on only aminosalicylates may be acceptable, but biologics (Humira, Remicade, etc.) create permanent deferral. Active flares always defer you temporarily.</p>
</div>

<h2 id="ibs-eligibility">IBS (Irritable Bowel Syndrome)</h2>

<h3>Why IBS Is Usually Acceptable</h3>

<ul>
<li><strong>Functional disorder:</strong> IBS doesn't cause inflammation or alter plasma composition</li>
<li><strong>No immunosuppression:</strong> IBS medications don't compromise immune function</li>
<li><strong>Not autoimmune:</strong> No antibodies or immune factors that affect plasma</li>
<li><strong>Common condition:</strong> Up to 15% of adults have IBS</li>
</ul>

<h3>When You CAN Donate (IBS)</h3>

<ul>
<li><strong>Stable symptoms:</strong> Managed with diet, lifestyle, or medication</li>
<li><strong>No active flare:</strong> Not experiencing severe diarrhea, cramping, or pain</li>
<li><strong>Acceptable medications:</strong> Antispasmodics, laxatives, antidiarrheals all allowed</li>
<li><strong>Good nutrition:</strong> Able to eat and absorb nutrients adequately</li>
<li><strong>Well-hydrated:</strong> Not chronically dehydrated from diarrhea</li>
</ul>

<h3>When You're Deferred (IBS)</h3>

<ul>
<li><strong>Active severe symptoms:</strong> Frequent diarrhea (risk of dehydration during donation)</li>
<li><strong>Recent weight loss:</strong> Malnutrition affects plasma protein levels</li>
<li><strong>Severe abdominal pain:</strong> Sitting for 1-2 hours may be intolerable</li>
<li><strong>Dehydration:</strong> From persistent diarrhea</li>
</ul>

<h3>IBS Medications (All Allowed)</h3>

<table>
<thead>
<tr>
<th>Medication Type</th>
<th>Examples</th>
<th>Status</th>
</tr>
</thead>
<tbody>
<tr>
<td>Antispasmodics</td>
<td>Dicyclomine (Bentyl), Hyoscyamine (Levsin)</td>
<td>✓ Allowed</td>
</tr>
<tr>
<td>Antidiarrheals</td>
<td>Loperamide (Imodium), Diphenoxylate (Lomotil)</td>
<td>✓ Allowed</td>
</tr>
<tr>
<td>Fiber supplements</td>
<td>Psyllium (Metamucil), methylcellulose</td>
<td>✓ Allowed</td>
</tr>
<tr>
<td>Laxatives</td>
<td>Polyethylene glycol (Miralax), senna</td>
<td>✓ Allowed</td>
</tr>
<tr>
<td>IBS-specific meds</td>
<td>Alosetron (Lotronex), Eluxadoline (Viberzi)</td>
<td>✓ Usually allowed</td>
</tr>
<tr>
<td>Rifaximin</td>
<td>Xifaxan</td>
<td>✓ Allowed (after completing course)</td>
</tr>
</tbody>
</table>

{AFFILIATE_BLOCK}

<h2 id="ibd-overview">IBD: Crohn's and Ulcerative Colitis</h2>

<h3>Why IBD Is More Complicated</h3>

<ul>
<li><strong>Autoimmune component:</strong> Inflammatory bowel diseases involve immune dysregulation</li>
<li><strong>Medication requirements:</strong> Most IBD patients need immunosuppressive therapy</li>
<li><strong>Malabsorption:</strong> Active disease affects protein and nutrient absorption</li>
<li><strong>Systemic inflammation:</strong> May alter plasma protein composition</li>
<li><strong>Anemia common:</strong> GI bleeding and chronic inflammation cause low iron</li>
</ul>

<h3>IBD Severity and Eligibility</h3>

<table>
<thead>
<tr>
<th>Disease Status</th>
<th>Description</th>
<th>Typical Eligibility</th>
</tr>
</thead>
<tbody>
<tr>
<td>Mild, controlled</td>
<td>On aminosalicylates only, no flares, no systemic symptoms</td>
<td>✓ May be allowed</td>
</tr>
<tr>
<td>Moderate</td>
<td>On immunosuppressants or corticosteroids</td>
<td>❌ Usually deferred</td>
</tr>
<tr>
<td>Severe</td>
<td>On biologics, frequent flares, malnutrition</td>
<td>❌ Permanent deferral</td>
</tr>
<tr>
<td>Active flare</td>
<td>Current symptoms, bloody stool, pain</td>
<td>❌ Deferred until remission</td>
</tr>
<tr>
<td>Post-surgery</td>
<td>Colectomy, ileostomy, resection</td>
<td>⚠ Case-by-case (see below)</td>
</tr>
</tbody>
</table>

{PRO_TOOLKIT}

<h2 id="medications">IBD Medications and Deferral</h2>

<h3>Aminosalicylates (Usually Allowed)</h3>

<table>
<thead>
<tr>
<th>Medication</th>
<th>Brand Name</th>
<th>Status</th>
</tr>
</thead>
<tbody>
<tr>
<td>Mesalamine</td>
<td>Asacol, Pentasa, Lialda, Apriso</td>
<td>✓ Usually allowed</td>
</tr>
<tr>
<td>Sulfasalazine</td>
<td>Azulfidine</td>
<td>✓ Usually allowed</td>
</tr>
<tr>
<td>Balsalazide</td>
<td>Colazal</td>
<td>✓ Usually allowed</td>
</tr>
<tr>
<td>Olsalazine</td>
<td>Dipentum</td>
<td>✓ Usually allowed</td>
</tr>
</tbody>
</table>

<h3>Immunosuppressants (DISQUALIFYING)</h3>

<table>
<thead>
<tr>
<th>Medication</th>
<th>Brand Name</th>
<th>Status</th>
</tr>
</thead>
<tbody>
<tr>
<td>Azathioprine</td>
<td>Imuran</td>
<td>❌ Permanent deferral</td>
</tr>
<tr>
<td>6-Mercaptopurine</td>
<td>Purinethol</td>
<td>❌ Permanent deferral</td>
</tr>
<tr>
<td>Methotrexate</td>
<td>Trexall</td>
<td>❌ Permanent deferral</td>
</tr>
<tr>
<td>Cyclosporine</td>
<td>Neoral, Sandimmune</td>
<td>❌ Permanent deferral</td>
</tr>
<tr>
<td>Tacrolimus</td>
<td>Prograf</td>
<td>❌ Permanent deferral</td>
</tr>
</tbody>
</table>

<h3>Biologic Medications (PERMANENT DEFERRAL)</h3>

<table>
<thead>
<tr>
<th>Medication</th>
<th>Brand Name</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>Infliximab</td>
<td>Remicade</td>
<td>TNF-alpha inhibitor</td>
</tr>
<tr>
<td>Adalimumab</td>
<td>Humira</td>
<td>TNF-alpha inhibitor</td>
</tr>
<tr>
<td>Certolizumab</td>
<td>Cimzia</td>
<td>TNF-alpha inhibitor</td>
</tr>
<tr>
<td>Golimumab</td>
<td>Simponi</td>
<td>TNF-alpha inhibitor</td>
</tr>
<tr>
<td>Vedolizumab</td>
<td>Entyvio</td>
<td>Integrin inhibitor</td>
</tr>
<tr>
<td>Ustekinumab</td>
<td>Stelara</td>
<td>IL-12/23 inhibitor</td>
</tr>
<tr>
<td>Natalizumab</td>
<td>Tysabri</td>
<td>Integrin inhibitor</td>
</tr>
<tr>
<td>Risankizumab</td>
<td>Skyrizi</td>
<td>IL-23 inhibitor</td>
</tr>
</tbody>
</table>

<h3>JAK Inhibitors (PERMANENT DEFERRAL)</h3>

<table>
<thead>
<tr>
<th>Medication</th>
<th>Brand Name</th>
<th>Status</th>
</tr>
</thead>
<tbody>
<tr>
<td>Tofacitinib</td>
<td>Xeljanz</td>
<td>❌ Permanent deferral</td>
</tr>
<tr>
<td>Upadacitinib</td>
<td>Rinvoq</td>
<td>❌ Permanent deferral</td>
</tr>
</tbody>
</table>

<h3>Corticosteroids (Deferral During Use)</h3>

<table>
<thead>
<tr>
<th>Medication</th>
<th>Common Use</th>
<th>Status</th>
</tr>
</thead>
<tbody>
<tr>
<td>Prednisone</td>
<td>Oral, systemic</td>
<td>❌ Deferred while taking</td>
</tr>
<tr>
<td>Budesonide</td>
<td>Entocort EC, Uceris (oral)</td>
<td>⚠ May be allowed (lower systemic absorption)</td>
</tr>
<tr>
<td>Hydrocortisone enema</td>
<td>Cortenema (topical)</td>
<td>✓ Usually allowed (minimal systemic absorption)</td>
</tr>
</tbody>
</table>

<h2 id="screening">What to Tell Screening Staff</h2>

<h3>Information to Provide</h3>

<ol>
<li><strong>Specific diagnosis:</strong> IBS, Crohn's disease, or ulcerative colitis?</li>
<li><strong>Disease location:</strong> (For IBD) Small intestine, colon, or both?</li>
<li><strong>Current medications:</strong> Complete list with doses</li>
<li><strong>Disease activity:</strong> In remission or active flare?</li>
<li><strong>Last flare:</strong> When was most recent symptom exacerbation?</li>
<li><strong>Surgeries:</strong> Any bowel resection, ostomy, or other procedures?</li>
<li><strong>Complications:</strong> Fistulas, strictures, abscesses?</li>
<li><strong>Nutrition status:</strong> Any recent weight loss or malabsorption?</li>
</ol>

<h3>Questions Staff Will Ask</h3>

<ul>
<li>"Do you have irritable bowel syndrome or inflammatory bowel disease?"</li>
<li>"What medications do you take for your condition?"</li>
<li>"Are you currently having symptoms?"</li>
<li>"Have you had any GI bleeding?"</li>
<li>"Do you have an ostomy or ileostomy?"</li>
<li>"When was your last colonoscopy?"</li>
</ul>

<h3>Red Flags for Deferral</h3>

<ul>
<li>Any biologic medication use (even if stopped recently)</li>
<li>Current systemic corticosteroid use</li>
<li>Active flare with bloody stool</li>
<li>Recent hospitalization for IBD</li>
<li>Significant weight loss or malnutrition</li>
<li>Anemia from GI bleeding</li>
</ul>

<h2 id="tips">Managing Donation With GI Issues</h2>

<h3>For IBS Patients</h3>

<ul>
<li><strong>Time donations carefully:</strong> Schedule when symptoms typically better (morning vs evening)</li>
<li><strong>Manage triggers:</strong> Avoid trigger foods 24 hours before donation</li>
<li><strong>Pre-donate bathroom visit:</strong> Empty bowels before starting process</li>
<li><strong>Bring antispasmodics:</strong> Have medication available if cramping starts</li>
<li><strong>Know bathroom location:</strong> Ask staff where restrooms are before starting</li>
<li><strong>Hydration balance:</strong> Drink enough for donation but not so much you trigger IBS-D</li>
</ul>

<h3>For Mild IBD (If Eligible)</h3>

<ul>
<li><strong>Only donate in remission:</strong> Never during active flare</li>
<li><strong>Consult gastroenterologist:</strong> Get approval before starting donation</li>
<li><strong>Monitor protein levels:</strong> Ensure adequate nutrition and absorption</li>
<li><strong>Watch for flare triggers:</strong> Donation stress could potentially trigger symptoms</li>
<li><strong>Extra hydration:</strong> 20+ oz water before donation</li>
<li><strong>Continue medications:</strong> Take all prescribed medications on schedule</li>
</ul>

<h3>Post-Donation Care</h3>

<ul>
<li><strong>Gentle foods:</strong> Stick to low-FODMAP or easy-to-digest foods for 24 hours</li>
<li><strong>Adequate protein:</strong> Replace plasma proteins with lean protein sources</li>
<li><strong>Hydration:</strong> 8-10 glasses water (more if prone to diarrhea)</li>
<li><strong>Monitor stools:</strong> Watch for blood, increased diarrhea, or symptom changes</li>
<li><strong>Rest:</strong> Allow body to recover, especially if you have IBD</li>
</ul>

<h3>Ostomy Considerations</h3>

<p>If you have an ileostomy or colostomy:</p>

<ul>
<li><strong>Output monitoring:</strong> Track ostomy output to ensure adequate hydration</li>
<li><strong>Electrolyte awareness:</strong> Ileostomy patients lose more electrolytes</li>
<li><strong>Bag management:</strong> Empty before donation; bring supplies in case needed</li>
<li><strong>Staff notification:</strong> Tell phlebotomist about ostomy (affects positioning, bathroom access)</li>
<li><strong>Increased hydration:</strong> Ostomy patients need extra fluids before and after</li>
</ul>

<h3>When to Stop Donating</h3>

<ul>
<li>IBD flare begins</li>
<li>Need to start biologics or immunosuppressants</li>
<li>GI bleeding or anemia develops</li>
<li>Unintended weight loss</li>
<li>Donation seems to trigger IBS/IBD symptoms</li>
<li>Surgery scheduled</li>
</ul>

{related_reading([
    ('/blog/can-you-donate-plasma-with-celiac-disease-2026', 'Celiac Disease and Plasma Donation'),
    ('/blog/can-you-donate-plasma-on-biologics-complete-guide', 'Complete Biologic Medications Guide'),
    ('/blog/digestive-disorders-plasma-donation-eligibility', 'Other Digestive Disorders')
])}

{footer_related()}
''',
        'faqs': [
            make_faq(
                "Can I donate if I have Crohn's disease in remission on Humira?",
                "No, Humira (adalimumab) is a biologic TNF-alpha inhibitor that creates permanent deferral from plasma donation, regardless of whether your Crohn's is in remission. The medication itself disqualifies you due to its immunosuppressive effects and the monoclonal antibodies it introduces to your plasma. This policy protects both you and plasma recipients."
            ),
            make_faq(
                "What if I only take Lialda for ulcerative colitis—can I donate?",
                "Possibly. Lialda (mesalamine) is an aminosalicylate that's generally allowed for plasma donation. If your UC is mild, well-controlled on mesalamine alone, you're in remission, and you have no anemia or malnutrition, many centers will accept you. However, you'll need to disclose your diagnosis and medication—they may request documentation from your gastroenterologist."
            ),
            make_faq(
                "Does having an ileostomy disqualify me from donating?",
                "Not necessarily, but it depends on why you have the ostomy and your current health status. If you had ileostomy for UC or Crohn's and you're on biologics/immunosuppressants, you're deferred due to medications. If you're stable, well-nourished, maintaining good ostomy output and hydration, and not on disqualifying medications, some centers may accept you. Discuss with center medical staff."
            ),
            make_faq(
                "Can I donate with IBS if I have frequent diarrhea?",
                "If your diarrhea is frequent enough to cause chronic dehydration or electrolyte imbalances, you may be deferred. However, if you have IBS-D that's reasonably controlled (maybe 2-3 loose stools daily but manageable with medication), you're well-hydrated, and lab values are normal, most centers will accept you. The key is adequate hydration status and ability to sit for 1-2 hours without urgent bathroom needs."
            ),
            make_faq(
                "What if I stopped my biologic for Crohn's disease—can I donate now?",
                "Most centers maintain permanent deferral even after stopping biologics because you have an autoimmune/inflammatory condition that required immunosuppressive therapy. Some centers might consider you after 12+ months off biologics with documented stable remission and gastroenterologist clearance, but this is rare and requires medical director approval. Never stop prescribed medications just to donate plasma."
            ),
        ]
    },
    {
        'slug': 'can-you-donate-plasma-with-pcos-2026',
        'title': 'Can You Donate Plasma With PCOS? [2026 Medication & Eligibility Guide]',
        'meta': 'PCOS alone doesn\'t disqualify plasma donation. Learn about metformin, birth control, and other PCOS medication eligibility for 2026 donation.',
        'category': 'Medical Eligibility',
        'read_time': 7,
        'toc': [
            ('quick-answer', 'Quick Answer'),
            ('pcos-eligibility', 'PCOS and Plasma Donation'),
            ('medications', 'PCOS Medications (All Allowed)'),
            ('complications', 'PCOS-Related Complications'),
            ('screening', 'What Screening Staff Will Ask'),
            ('tips', 'Donation Tips for PCOS Patients'),
        ],
        'content': f'''
<div class="quick-answer">
<h3>Quick Answer: Can You Donate Plasma With PCOS?</h3>
<p><strong>Yes, PCOS (polycystic ovary syndrome) doesn't disqualify you from plasma donation.</strong> All standard PCOS medications—including metformin, birth control pills, and spironolactone—are acceptable. However, PCOS-related complications like diabetes, high blood pressure, or obesity may require additional screening or could affect eligibility.</p>
</div>

<h2 id="pcos-eligibility">PCOS and Plasma Donation</h2>

<h3>Why PCOS Is Acceptable</h3>

<ul>
<li><strong>Not autoimmune:</strong> PCOS is an endocrine/metabolic disorder, not an immune condition</li>
<li><strong>Doesn't affect plasma quality:</strong> No abnormal antibodies or plasma proteins</li>
<li><strong>Common condition:</strong> Affects 6-12% of women; excluding them would significantly reduce donor pool</li>
<li><strong>Medications allowed:</strong> All standard PCOS treatments are acceptable</li>
</ul>

<h3>When You CAN Donate</h3>

<ul>
<li><strong>Diagnosis of PCOS:</strong> With or without symptoms</li>
<li><strong>Taking PCOS medications:</strong> Metformin, birth control, anti-androgens all allowed</li>
<li><strong>Stable weight:</strong> Not experiencing rapid weight changes</li>
<li><strong>Normal blood pressure:</strong> <140/90 at donation screening</li>
<li><strong>No diabetes:</strong> Or well-controlled diabetes with A1C <6.5%</li>
<li><strong>Regular periods:</strong> Or amenorrhea that doesn't affect health</li>
</ul>

<h3>When You're Deferred</h3>

<ul>
<li><strong>Uncontrolled diabetes:</strong> A1C >6.5% or on insulin (see diabetes policies)</li>
<li><strong>High blood pressure:</strong> >140/90 consistently</li>
<li><strong>Severe obesity:</strong> BMI may affect venous access (center-specific policies)</li>
<li><strong>Active infection:</strong> Ovarian cyst rupture, pelvic infection</li>
<li><strong>Recent hospitalization:</strong> For PCOS-related complications</li>
</ul>

{AFFILIATE_BLOCK}

<h2 id="medications">PCOS Medications (All Allowed)</h2>

<h3>Insulin Sensitizers</h3>

<table>
<thead>
<tr>
<th>Medication</th>
<th>Brand Name</th>
<th>Donation Status</th>
</tr>
</thead>
<tbody>
<tr>
<td>Metformin</td>
<td>Glucophage, Glucophage XR</td>
<td>✓ Allowed</td>
</tr>
<tr>
<td>Metformin ER</td>
<td>Fortamet, Glumetza</td>
<td>✓ Allowed</td>
</tr>
<tr>
<td>Pioglitazone</td>
<td>Actos</td>
<td>✓ Usually allowed</td>
</tr>
</tbody>
</table>

<h3>Hormonal Birth Control (All Allowed)</h3>

<table>
<thead>
<tr>
<th>Type</th>
<th>Examples</th>
<th>Donation Status</th>
</tr>
</thead>
<tbody>
<tr>
<td>Combined oral contraceptives</td>
<td>Yaz, Yasmin, Ortho Tri-Cyclen, Lo Loestrin</td>
<td>✓ Allowed</td>
</tr>
<tr>
<td>Progestin-only pills</td>
<td>Nor QD, Camila, Errin</td>
<td>✓ Allowed</td>
</tr>
<tr>
<td>Vaginal ring</td>
<td>NuvaRing, Annovera</td>
<td>✓ Allowed</td>
</tr>
<tr>
<td>Birth control patch</td>
<td>Xulane, Twirla</td>
<td>✓ Allowed</td>
</tr>
<tr>
<td>Hormonal IUD</td>
<td>Mirena, Kyleena, Skyla, Liletta</td>
<td>✓ Allowed</td>
</tr>
<tr>
<td>Implant</td>
<td>Nexplanon</td>
<td>✓ Allowed</td>
</tr>
<tr>
<td>Injection</td>
<td>Depo-Provera</td>
<td>✓ Allowed</td>
</tr>
</tbody>
</table>

<h3>Anti-Androgens</h3>

<table>
<thead>
<tr>
<th>Medication</th>
<th>Brand Name</th>
<th>Donation Status</th>
</tr>
</thead>
<tbody>
<tr>
<td>Spironolactone</td>
<td>Aldactone</td>
<td>✓ Allowed (monitor blood pressure)</td>
</tr>
<tr>
<td>Finasteride</td>
<td>Propecia (off-label for PCOS)</td>
<td>✓ Usually allowed</td>
</tr>
</tbody>
</table>

{PRO_TOOLKIT}

<h3>Ovulation Induction (for Fertility)</h3>

<table>
<thead>
<tr>
<th>Medication</th>
<th>Brand Name</th>
<th>Donation Status</th>
</tr>
</thead>
<tbody>
<tr>
<td>Clomiphene</td>
<td>Clomid</td>
<td>✓ Allowed (but defer if pregnant)</td>
</tr>
<tr>
<td>Letrozole</td>
<td>Femara (off-label)</td>
<td>✓ Allowed (but defer if pregnant)</td>
</tr>
</tbody>
</table>

<p><strong>Pregnancy note:</strong> If you become pregnant while taking fertility medications, you cannot donate during pregnancy or for 6-9 months postpartum.</p>

<h3>Other PCOS Treatments</h3>

<ul>
<li><strong>Inositol supplements:</strong> Allowed</li>
<li><strong>Vitamin D:</strong> Allowed</li>
<li><strong>NAC (N-acetylcysteine):</strong> Allowed</li>
<li><strong>Omega-3 supplements:</strong> Allowed</li>
</ul>

<h2 id="complications">PCOS-Related Complications</h2>

<h3>Diabetes and Pre-Diabetes</h3>

<p>Women with PCOS have higher diabetes risk:</p>

<table>
<thead>
<tr>
<th>Status</th>
<th>A1C Level</th>
<th>Donation Eligibility</th>
</tr>
</thead>
<tbody>
<tr>
<td>Normal</td>
<td><5.7%</td>
<td>✓ Allowed</td>
</tr>
<tr>
<td>Pre-diabetes</td>
<td>5.7-6.4%</td>
<td>✓ Usually allowed (may require monitoring)</td>
</tr>
<tr>
<td>Well-controlled diabetes</td>
<td><6.5%, no insulin</td>
<td>✓ May be allowed (center-specific)</td>
</tr>
<tr>
<td>Poorly controlled diabetes</td>
<td>>6.5% or on insulin</td>
<td>❌ Usually deferred</td>
</tr>
</tbody>
</table>

<h3>Hypertension</h3>

<p>PCOS increases high blood pressure risk:</p>

<ul>
<li><strong>Normal (<120/80):</strong> No issues</li>
<li><strong>Elevated (120-129/<80):</strong> Acceptable</li>
<li><strong>Stage 1 (130-139/80-89):</strong> May donate if on medication and controlled</li>
<li><strong>Stage 2 (≥140/90):</strong> Deferred until controlled</li>
</ul>

<h3>Obesity</h3>

<p>PCOS often involves weight struggles:</p>

<ul>
<li><strong>BMI eligibility:</strong> Most centers accept up to BMI 40-45 (varies by center)</li>
<li><strong>Venous access:</strong> Higher BMI may make vein location harder but doesn't automatically disqualify</li>
<li><strong>Comfort:</strong> Donation chairs have weight limits (usually 350-400 lbs)</li>
<li><strong>Health screening:</strong> Higher BMI prompts careful BP and diabetes screening</li>
</ul>

<h3>Ovarian Cysts</h3>

<ul>
<li><strong>Asymptomatic cysts:</strong> Normal with PCOS, no deferral needed</li>
<li><strong>Recent rupture:</strong> Wait 30 days after resolution</li>
<li><strong>Surgery:</strong> Standard post-surgical waiting periods apply</li>
<li><strong>Ongoing pain:</strong> May interfere with ability to sit comfortably for donation</li>
</ul>

<h2 id="screening">What Screening Staff Will Ask</h2>

<h3>PCOS-Specific Questions</h3>

<ol>
<li><strong>"Do you have PCOS or polycystic ovary syndrome?"</strong></li>
<li><strong>"What medications do you take for PCOS?"</strong></li>
<li><strong>"Do you have diabetes or pre-diabetes?"</strong></li>
<li><strong>"Are you trying to get pregnant or currently pregnant?"</strong></li>
<li><strong>"Do you take metformin or other diabetes medications?"</strong></li>
<li><strong>"When was your last menstrual period?"</strong> (pregnancy screening)</li>
</ol>

<h3>Vital Signs Monitoring</h3>

<p>PCOS patients get extra attention to:</p>

<ul>
<li><strong>Blood pressure:</strong> Checked each visit (PCOS increases hypertension risk)</li>
<li><strong>Weight:</strong> Tracked to monitor stability</li>
<li><strong>Protein levels:</strong> Finger-stick test (can be affected by insulin resistance)</li>
<li><strong>Pulse:</strong> Some PCOS medications affect heart rate</li>
</ul>

<h3>Information to Provide</h3>

<ul>
<li>Complete medication list (including supplements)</li>
<li>Last A1C result if you have diabetes/pre-diabetes</li>
<li>Blood pressure readings if you monitor at home</li>
<li>Any recent PCOS-related hospitalizations or procedures</li>
<li>Fertility treatment status (if applicable)</li>
</ul>

<h2 id="tips">Donation Tips for PCOS Patients</h2>

<h3>Managing Metformin Side Effects</h3>

<p>Metformin can cause GI issues that complicate donation:</p>

<ul>
<li><strong>Timing:</strong> Take metformin after donation, not before (reduces nausea risk)</li>
<li><strong>Food intake:</strong> Eat protein-rich meal 2-3 hours before donation</li>
<li><strong>GI symptoms:</strong> If metformin causes diarrhea, ensure well-hydrated before donating</li>
<li><strong>Extended release:</strong> Metformin ER has fewer GI side effects if you can switch</li>
</ul>

<h3>Blood Sugar Management</h3>

<ul>
<li><strong>Pre-donation meal:</strong> Balanced with protein, complex carbs, healthy fats</li>
<li><strong>Avoid simple sugars:</strong> Don't load up on candy/juice before donation (insulin spike then crash)</li>
<li><strong>Snack availability:</strong> Bring protein bar in case of low blood sugar during/after</li>
<li><strong>Monitor symptoms:</strong> Dizziness, shakiness, confusion could indicate hypoglycemia</li>
</ul>

<h3>Hydration Considerations</h3>

<ul>
<li><strong>Extra water needed:</strong> PCOS patients may have subtle dehydration from insulin resistance</li>
<li><strong>20+ oz before donation:</strong> Drink 2-3 hours prior</li>
<li><strong>Avoid caffeine excess:</strong> Can affect blood pressure and hydration</li>
<li><strong>Post-donation fluids:</strong> 8-10 glasses water over next 24 hours</li>
</ul>

<h3>Weight Management While Donating</h3>

<ul>
<li><strong>Protein replacement:</strong> Donation removes 50-70g protein; replace with lean protein</li>
<li><strong>Not a weight-loss tool:</strong> Don't use plasma donation to burn calories (unhealthy approach)</li>
<li><strong>Stable weight best:</strong> Rapid weight changes affect protein levels and eligibility</li>
<li><strong>Nutrient-dense foods:</strong> Focus on quality nutrition to support both PCOS and donation recovery</li>
</ul>

<h3>Fertility Considerations</h3>

<ul>
<li><strong>If trying to conceive:</strong> Inform staff (pregnancy creates 6-9 month deferral)</li>
<li><strong>Pregnancy tests:</strong> Some centers test before each donation</li>
<li><strong>First trimester risk:</strong> Unknown pregnancy could be harmed by donation stress</li>
<li><strong>Document LMP:</strong> Keep track of last menstrual period for screening questions</li>
</ul>

<h3>When to Pause Donations</h3>

<ul>
<li>Pregnancy confirmed</li>
<li>Starting insulin for diabetes</li>
<li>Blood pressure becomes uncontrolled</li>
<li>Significant weight gain affecting venous access</li>
<li>PCOS medication changes causing instability</li>
<li>Ovarian cyst complications</li>
</ul>

{related_reading([
    ('/blog/can-you-donate-plasma-with-diabetes-complete-guide', 'Diabetes and Metformin Guide'),
    ('/blog/can-you-donate-plasma-on-birth-control-2026', 'Birth Control and Plasma Donation'),
    ('/blog/can-you-donate-plasma-while-pregnant-postpartum', 'Pregnancy and Postpartum Deferral')
])}

{footer_related()}
''',
        'faqs': [
            make_faq(
                "Does metformin in my plasma affect the recipients?",
                "No. The trace amounts of metformin in donated plasma are negligible, and all plasma undergoes extensive processing before manufacture into therapeutic products. Plasma from thousands of donors is pooled, further diluting any medication traces. The screening for metformin is more about ensuring you're healthy enough to donate, not about drug contamination concerns."
            ),
            make_faq(
                "Can I donate if I have PCOS but I'm not on any medication?",
                "Yes, absolutely. PCOS diagnosis alone doesn't disqualify you, whether you're managing it with lifestyle alone or with medication. As long as you don't have uncontrolled diabetes, high blood pressure, or other complications that would independently disqualify you, you can donate. Many women with mild PCOS don't require medication."
            ),
            make_faq(
                "Will donating plasma affect my PCOS symptoms or hormones?",
                "Plasma donation shouldn't directly affect your PCOS symptoms or hormone levels. However, if you're not adequately replacing protein and nutrients after donation, the stress on your body could potentially worsen some symptoms. Maintain good nutrition, adequate protein intake, and proper hydration to support both PCOS management and donation recovery."
            ),
            make_faq(
                "Can I donate if I'm doing IVF or fertility treatments for PCOS?",
                "It depends on the timing and medications. During active IVF cycles with injectable hormones (gonadotropins), you should pause donation. If you're taking only oral medications like Clomid or letrozole, you can likely continue donating—but stop immediately if pregnancy is confirmed. Discuss your specific fertility treatment plan with both your reproductive endocrinologist and the plasma center."
            ),
            make_faq(
                "What if my PCOS causes irregular periods—will that disqualify me?",
                "No, irregular periods from PCOS don't disqualify you. However, irregular cycles make pregnancy detection harder, so centers may be more careful with pregnancy screening. Some centers test for pregnancy more frequently in women with amenorrhea or very irregular cycles. The concern is unknowingly donating while pregnant, which could harm the fetus."
            ),
        ]
    },
    {
        'slug': 'can-you-donate-plasma-with-arthritis-2026',
        'title': 'Can You Donate Plasma With Arthritis? [2026 RA & Medication Guide]',
        'meta': 'Osteoarthritis usually OK, but rheumatoid arthritis depends on medications. Complete guide to biologics, DMARDs, and arthritis eligibility for 2026.',
        'category': 'Medical Eligibility',
        'read_time': 9,
        'toc': [
            ('quick-answer', 'Quick Answer'),
            ('osteoarthritis', 'Osteoarthritis (OA) Eligibility'),
            ('rheumatoid', 'Rheumatoid Arthritis (RA) Eligibility'),
            ('medications', 'Arthritis Medications and Deferral'),
            ('screening', 'What Screening Staff Will Check'),
            ('tips', 'Donation Tips for Arthritis Patients'),
        ],
        'content': f'''
<div class="quick-answer">
<h3>Quick Answer: Can You Donate With Arthritis?</h3>
<p><strong>Osteoarthritis: Yes, usually allowed.</strong> OA is degenerative, not autoimmune, and most OA medications (NSAIDs, acetaminophen) are acceptable. <strong>Rheumatoid arthritis: It depends on medications.</strong> RA patients on biologics (Humira, Enbrel, etc.) or DMARDs (methotrexate) are permanently deferred. Those on only NSAIDs or low-dose prednisone may be eligible.</p>
</div>

<h2 id="osteoarthritis">Osteoarthritis (OA) Eligibility</h2>

<h3>Why Osteoarthritis Is Generally Acceptable</h3>

<ul>
<li><strong>Degenerative, not autoimmune:</strong> OA is "wear and tear" arthritis without immune dysfunction</li>
<li><strong>No abnormal antibodies:</strong> Doesn't produce autoantibodies that affect plasma</li>
<li><strong>Simple medications:</strong> Most OA treatments are allowed for donation</li>
<li><strong>Very common:</strong> Over 32 million US adults have OA</li>
</ul>

<h3>When You CAN Donate (OA)</h3>

<ul>
<li><strong>Diagnosis of osteoarthritis:</strong> Any joints affected</li>
<li><strong>On allowed medications:</strong> NSAIDs, acetaminophen, topical treatments</li>
<li><strong>Mobile and functional:</strong> Able to get to donation center and sit for 1-2 hours</li>
<li><strong>No recent joint injections:</strong> Or completed waiting period</li>
<li><strong>Adequate arm mobility:</strong> Can extend arm for venipuncture</li>
</ul>

<h3>When You're Deferred (OA)</h3>

<ul>
<li><strong>Recent joint injection:</strong> Wait 24-48 hours after corticosteroid injection</li>
<li><strong>Viscosupplement injection:</strong> Wait 48-72 hours after hyaluronic acid injection</li>
<li><strong>Active joint infection:</strong> Septic arthritis requires treatment and waiting period</li>
<li><strong>Recent surgery:</strong> Joint replacement or arthroscopy (standard surgical waiting periods)</li>
<li><strong>Unable to extend arm:</strong> Severe elbow or shoulder OA preventing proper positioning</li>
</ul>

<h3>OA Medications (All Allowed)</h3>

<table>
<thead>
<tr>
<th>Medication Type</th>
<th>Examples</th>
<th>Donation Status</th>
</tr>
</thead>
<tbody>
<tr>
<td>Acetaminophen</td>
<td>Tylenol</td>
<td>✓ Allowed</td>
</tr>
<tr>
<td>NSAIDs (oral)</td>
<td>Ibuprofen, naproxen, diclofenac, meloxicam</td>
<td>✓ Allowed</td>
</tr>
<tr>
<td>Topical NSAIDs</td>
<td>Voltaren gel, diclofenac gel</td>
<td>✓ Allowed</td>
</tr>
<tr>
<td>Topical capsaicin</td>
<td>Zostrix, Capzasin</td>
<td>✓ Allowed</td>
</tr>
<tr>
<td>Topical menthol</td>
<td>Biofreeze, Bengay</td>
<td>✓ Allowed</td>
</tr>
<tr>
<td>Tramadol</td>
<td>Ultram</td>
<td>✓ Usually allowed</td>
</tr>
<tr>
<td>Supplements</td>
<td>Glucosamine, chondroitin</td>
<td>✓ Allowed</td>
</tr>
</tbody>
</table>

{AFFILIATE_BLOCK}

<h2 id="rheumatoid">Rheumatoid Arthritis (RA) Eligibility</h2>

<h3>Why RA Is More Complicated</h3>

<ul>
<li><strong>Autoimmune disease:</strong> RA produces autoantibodies (RF, anti-CCP)</li>
<li><strong>Systemic inflammation:</strong> Affects plasma protein composition</li>
<li><strong>Immunosuppressive treatment:</strong> Most RA patients require DMARDs or biologics</li>
<li><strong>Recipient safety concerns:</strong> Autoantibodies could affect plasma product recipients</li>
</ul>

<h3>RA Severity and Eligibility</h3>

<table>
<thead>
<tr>
<th>RA Status</th>
<th>Description</th>
<th>Typical Eligibility</th>
</tr>
</thead>
<tbody>
<tr>
<td>Very mild RA</td>
<td>On NSAIDs only, no DMARDs/biologics</td>
<td>⚠ Possibly allowed (very rare)</td>
</tr>
<tr>
<td>Mild-moderate RA</td>
<td>On methotrexate or other DMARDs</td>
<td>❌ Permanent deferral</td>
</tr>
<tr>
<td>Moderate-severe RA</td>
<td>On biologic medications</td>
<td>❌ Permanent deferral</td>
</tr>
<tr>
<td>Active flare</td>
<td>Current joint swelling, pain, systemic symptoms</td>
<td>❌ Permanent deferral</td>
</tr>
</tbody>
</table>

<p><strong>Reality check:</strong> Over 90% of RA patients take medications that disqualify donation. It's extremely rare to have RA managed with only NSAIDs.</p>

{PRO_TOOLKIT}

<h2 id="medications">Arthritis Medications and Deferral</h2>

<h3>DMARDs - Disease-Modifying Anti-Rheumatic Drugs (ALL DISQUALIFYING)</h3>

<table>
<thead>
<tr>
<th>Medication</th>
<th>Brand Name</th>
<th>Why Disqualifying</th>
</tr>
</thead>
<tbody>
<tr>
<td>Methotrexate</td>
<td>Trexall, Rheumatrex, Otrexup</td>
<td>Immunosuppressant, chemotherapy agent</td>
</tr>
<tr>
<td>Leflunomide</td>
<td>Arava</td>
<td>Immunosuppressant, teratogenic metabolites</td>
</tr>
<tr>
<td>Sulfasalazine</td>
<td>Azulfidine</td>
<td>Immunomodulator (when used for RA)</td>
</tr>
<tr>
<td>Hydroxychloroquine</td>
<td>Plaquenil</td>
<td>Antimalarial, long half-life, immune modulation</td>
</tr>
<tr>
<td>Azathioprine</td>
<td>Imuran</td>
<td>Strong immunosuppressant</td>
</tr>
<tr>
<td>Cyclosporine</td>
<td>Neoral, Sandimmune</td>
<td>Transplant-level immunosuppression</td>
</tr>
</tbody>
</table>

<h3>Biologic DMARDs (PERMANENT DEFERRAL)</h3>

<h4>TNF-Alpha Inhibitors</h4>

<table>
<thead>
<tr>
<th>Medication</th>
<th>Brand Name</th>
<th>Administration</th>
</tr>
</thead>
<tbody>
<tr>
<td>Adalimumab</td>
<td>Humira</td>
<td>Injection every 2 weeks</td>
</tr>
<tr>
<td>Etanercept</td>
<td>Enbrel</td>
<td>Injection weekly</td>
</tr>
<tr>
<td>Infliximab</td>
<td>Remicade</td>
<td>IV infusion every 8 weeks</td>
</tr>
<tr>
<td>Certolizumab</td>
<td>Cimzia</td>
<td>Injection every 2-4 weeks</td>
</tr>
<tr>
<td>Golimumab</td>
<td>Simponi, Simponi Aria</td>
<td>Injection monthly or IV every 8 weeks</td>
</tr>
</tbody>
</table>

<h4>Other Biologics</h4>

<table>
<thead>
<tr>
<th>Medication</th>
<th>Brand Name</th>
<th>Mechanism</th>
</tr>
</thead>
<tbody>
<tr>
<td>Abatacept</td>
<td>Orencia</td>
<td>T-cell co-stimulation inhibitor</td>
</tr>
<tr>
<td>Rituximab</td>
<td>Rituxan</td>
<td>B-cell depleting antibody</td>
</tr>
<tr>
<td>Tocilizumab</td>
<td>Actemra</td>
<td>IL-6 receptor inhibitor</td>
</tr>
<tr>
<td>Sarilumab</td>
<td>Kevzara</td>
<td>IL-6 receptor inhibitor</td>
</tr>
<tr>
<td>Anakinra</td>
<td>Kineret</td>
<td>IL-1 receptor antagonist</td>
</tr>
</tbody>
</table>

<h3>JAK Inhibitors (PERMANENT DEFERRAL)</h3>

<table>
<thead>
<tr>
<th>Medication</th>
<th>Brand Name</th>
<th>Status</th>
</tr>
</thead>
<tbody>
<tr>
<td>Tofacitinib</td>
<td>Xeljanz</td>
<td>❌ Permanent deferral</td>
</tr>
<tr>
<td>Baricitinib</td>
<td>Olumiant</td>
<td>❌ Permanent deferral</td>
</tr>
<tr>
<td>Upadacitinib</td>
<td>Rinvoq</td>
<td>❌ Permanent deferral</td>
</tr>
</tbody>
</table>

<h3>Corticosteroids (Deferral During Certain Uses)</h3>

<table>
<thead>
<tr>
<th>Type</th>
<th>Examples</th>
<th>Status</th>
</tr>
</thead>
<tbody>
<tr>
<td>Low-dose oral</td>
<td>Prednisone ≤5mg daily</td>
<td>⚠ May be allowed (center-specific)</td>
</tr>
<tr>
<td>Moderate-high dose oral</td>
<td>Prednisone >5mg daily</td>
<td>❌ Deferred while taking</td>
</tr>
<tr>
<td>Joint injection</td>
<td>Cortisone, triamcinolone injection</td>
<td>✓ Allowed after 24-48 hours</td>
</tr>
<tr>
<td>Topical steroids</td>
<td>Hydrocortisone cream</td>
<td>✓ Allowed</td>
</tr>
</tbody>
</table>

<h2 id="screening">What Screening Staff Will Check</h2>

<h3>Questions About Arthritis</h3>

<ol>
<li><strong>"Do you have arthritis? What type?"</strong></li>
<li><strong>"What medications do you take for arthritis?"</strong></li>
<li><strong>"When was your last dose of medication?"</strong></li>
<li><strong>"Have you had any recent joint injections?"</strong></li>
<li><strong>"Have you had any joint replacement surgeries?"</strong></li>
<li><strong>"Are you experiencing any joint swelling or active inflammation?"</strong></li>
</ol>

<h3>Physical Considerations</h3>

<p>Staff will assess:</p>

<ul>
<li><strong>Arm mobility:</strong> Can you fully extend your arm for venipuncture?</li>
<li><strong>Hand function:</strong> Can you squeeze stress ball during donation?</li>
<li><strong>Sitting tolerance:</strong> Can you remain seated for 1-2 hours comfortably?</li>
<li><strong>Joint swelling:</strong> Active inflammation in arm affects donation site</li>
</ul>

<h3>Documentation Requirements</h3>

<p>For RA patients, bring:</p>

<ul>
<li>Complete medication list with dosages</li>
<li>Rheumatologist contact information</li>
<li>Recent lab work (if claiming you're on no DMARDs, may need to verify)</li>
<li>Doctor's note if requesting exception (very rare)</li>
</ul>

<h2 id="tips">Donation Tips for Arthritis Patients</h2>

<h3>For Osteoarthritis Patients</h3>

<h4>Joint Comfort During Donation</h4>

<ul>
<li><strong>Request positioning help:</strong> Ask staff for pillows or arm support</li>
<li><strong>Choose best arm:</strong> Donate from arm with less OA involvement</li>
<li><strong>Pre-medicate if needed:</strong> Take acetaminophen or NSAID 30-60 minutes before</li>
<li><strong>Gentle stretching:</strong> Light movement before donation to reduce stiffness</li>
<li><strong>Heat therapy beforehand:</strong> Warm compress on joints before leaving for appointment</li>
</ul>

<h4>Managing Post-Donation Stiffness</h4>

<ul>
<li><strong>Move arm gently:</strong> Don't completely immobilize donation arm</li>
<li><strong>Ice if needed:</strong> Apply ice to elbow if sore from needle</li>
<li><strong>Continue medications:</strong> Take usual OA medications on schedule</li>
<li><strong>Stay active:</strong> Light walking helps prevent stiffness</li>
</ul>

<h3>For RA Patients (If Eligible - Rare)</h3>

<h4>Managing Fatigue</h4>

<ul>
<li><strong>Schedule wisely:</strong> Donate when you have energy, not during flares</li>
<li><strong>Rest after donation:</strong> Plan low-activity day following donation</li>
<li><strong>Adequate sleep:</strong> Night before donation, prioritize 8+ hours sleep</li>
<li><strong>Limit frequency:</strong> Weekly instead of twice weekly if fatigue is significant</li>
</ul>

<h4>Infection Risk Awareness</h4>

<p>If you're on mild RA medications that allow donation (very rare):</p>

<ul>
<li><strong>Monitor injection site:</strong> RA patients may have slightly higher infection risk</li>
<li><strong>Report fever:</strong> Any post-donation fever should prompt medical evaluation</li>
<li><strong>Keep site clean:</strong> Follow bandage care instructions carefully</li>
<li><strong>Watch for redness:</strong> Increased redness, warmth, or swelling at needle site</li>
</ul>

<h3>Joint Injection Timing</h3>

<p>If you receive regular joint injections for arthritis:</p>

<ul>
<li><strong>Corticosteroid injections:</strong> Wait 24-48 hours before donating</li>
<li><strong>Hyaluronic acid (Synvisc, Orthovisc):</strong> Wait 48-72 hours</li>
<li><strong>PRP (platelet-rich plasma) injections:</strong> Check center policy (may be longer deferral)</li>
<li><strong>Don't inject donation arm:</strong> Use opposite arm for injection when possible</li>
</ul>

<h3>Hand Arthritis Considerations</h3>

<p>If you have hand/finger OA or RA:</p>

<ul>
<li><strong>Stress ball alternative:</strong> Ask if you can use something softer or larger</li>
<li><strong>Assisted squeezing:</strong> Staff can sometimes help with gentle pressure</li>
<li><strong>Warm hands first:</strong> Wear gloves to donation center, remove before screening</li>
<li><strong>Communication:</strong> Tell phlebotomist about hand arthritis before starting</li>
</ul>

<h3>When to Stop Donating</h3>

<ul>
<li>RA progresses requiring DMARDs or biologics</li>
<li>Joint pain worsens significantly after donations</li>
<li>Unable to extend arm adequately for venipuncture</li>
<li>Joint replacement surgery scheduled</li>
<li>Active arthritis flare with systemic symptoms</li>
</ul>

{related_reading([
    ('/blog/can-you-donate-plasma-with-lupus-2026', 'Lupus and Autoimmune Arthritis'),
    ('/blog/can-you-donate-plasma-with-psoriasis-2026', 'Psoriatic Arthritis Guide'),
    ('/blog/can-you-donate-plasma-on-biologics-complete-guide', 'Complete Biologic Medications Guide')
])}

{footer_related()}
''',
        'faqs': [
            make_faq(
                "Can I donate if I have rheumatoid arthritis but I'm in remission?",
                "It depends entirely on what medications you're taking, not your disease activity. If you achieved remission with biologics or DMARDs like methotrexate, you're permanently deferred regardless of symptom status. The extremely rare RA patient who maintains remission on only NSAIDs might be eligible, but this is unusual—most people require immunosuppressive therapy to achieve and maintain RA remission."
            ),
            make_faq(
                "What if I stopped taking my biologic medication for RA?",
                "Most centers maintain permanent deferral even after stopping biologics because you have an autoimmune disease that required immunosuppressive therapy. Stopping RA medications typically leads to disease flares and is medically inadvisable. Never discontinue prescribed RA treatment just to donate plasma—the long-term joint damage from uncontrolled RA far outweighs any plasma donation compensation."
            ),
            make_faq(
                "Can I donate if I only have arthritis in my knees, not my arms?",
                "Yes, if it's osteoarthritis and you're on only allowed medications (NSAIDs, acetaminophen). The location of your arthritis doesn't matter as long as you can extend your arm for venipuncture and sit comfortably during donation. Knee OA is very common and doesn't affect plasma quality or donation safety."
            ),
            make_faq(
                "Will donating plasma make my arthritis worse?",
                "Plasma donation shouldn't directly worsen osteoarthritis or rheumatoid arthritis. However, sitting for 1-2 hours may cause temporary stiffness, and arm positioning could cause mild joint discomfort. If you notice increased pain or swelling after donations, consider reducing frequency or using pre-medication with NSAIDs. Adequate hydration and gentle movement after donation help minimize stiffness."
            ),
            make_faq(
                "Can I donate if I take Plaquenil (hydroxychloroquine) for arthritis?",
                "No, hydroxychloroquine (Plaquenil) creates permanent deferral from plasma donation. This antimalarial drug used for RA and lupus has a very long half-life (40-50 days) and immune-modulating effects that make donation inappropriate. Even if you stopped Plaquenil, centers typically maintain deferral because you have a condition that required immunosuppressive therapy."
            ),
        ]
    },
    {
        'slug': 'can-you-donate-plasma-with-sleep-apnea-2026',
        'title': 'Can You Donate Plasma With Sleep Apnea or CPAP? [2026 Guide]',
        'meta': 'Sleep apnea doesn\'t disqualify plasma donation if well-controlled with CPAP/BiPAP. Complete guide to OSA, CSA, and untreated sleep apnea eligibility.',
        'category': 'Medical Eligibility',
        'read_time': 7,
        'toc': [
            ('quick-answer', 'Quick Answer'),
            ('controlled-apnea', 'Well-Controlled Sleep Apnea'),
            ('untreated', 'Untreated Sleep Apnea Risks'),
            ('screening', 'What Screening Staff Will Check'),
            ('cpap-users', 'Tips for CPAP/BiPAP Users'),
            ('other-treatments', 'Other Sleep Apnea Treatments'),
        ],
        'content': f'''
<div class="quick-answer">
<h3>Quick Answer: Can You Donate With Sleep Apnea?</h3>
<p><strong>Yes, if your sleep apnea is well-controlled with CPAP, BiPAP, or other treatment.</strong> Sleep apnea alone doesn't disqualify you from plasma donation as long as you're compliant with therapy, well-rested, and don't have related complications like uncontrolled hypertension or heart problems. Untreated severe sleep apnea may result in deferral due to safety concerns.</p>
</div>

<h2 id="controlled-apnea">Well-Controlled Sleep Apnea</h2>

<h3>Why Controlled Sleep Apnea Is Acceptable</h3>

<ul>
<li><strong>Not an immune disorder:</strong> Sleep apnea doesn't affect plasma quality or composition</li>
<li><strong>Treatment normalizes breathing:</strong> CPAP/BiPAP restores normal oxygen levels during sleep</li>
<li><strong>Common condition:</strong> 22 million Americans have sleep apnea</li>
<li><strong>No disqualifying medications:</strong> CPAP is device therapy, not medication</li>
</ul>

<h3>When You CAN Donate</h3>

<ul>
<li><strong>Diagnosed sleep apnea:</strong> Obstructive (OSA) or central (CSA)</li>
<li><strong>Using CPAP/BiPAP:</strong> Compliant with therapy (using 4+ hours per night)</li>
<li><strong>Well-rested:</strong> Getting adequate quality sleep with treatment</li>
<li><strong>No severe complications:</strong> Blood pressure controlled, no heart failure</li>
<li><strong>Alert and oriented:</strong> Not excessively sleepy during day</li>
<li><strong>Successful surgery:</strong> If treated with surgery (UPPP, etc.), fully recovered</li>
</ul>

<h3>When You're Deferred</h3>

<ul>
<li><strong>Untreated severe sleep apnea:</strong> Diagnosed but not using prescribed treatment</li>
<li><strong>Recent diagnosis:</strong> Still titrating CPAP settings (wait for stable therapy)</li>
<li><strong>Non-compliant with CPAP:</strong> Not using device regularly</li>
<li><strong>Excessive daytime sleepiness:</strong> Risk of falling asleep during donation</li>
<li><strong>Uncontrolled hypertension:</strong> Blood pressure >140/90 despite medication</li>
<li><strong>Heart failure:</strong> Sleep apnea-related cardiac complications</li>
<li><strong>Recent sleep apnea surgery:</strong> Standard post-surgical waiting periods</li>
</ul>

{AFFILIATE_BLOCK}

<h2 id="untreated">Untreated Sleep Apnea Risks</h2>

<h3>Why Untreated Sleep Apnea Is Concerning</h3>

<ul>
<li><strong>Oxygen deprivation:</strong> Repeated breathing pauses during sleep cause low oxygen</li>
<li><strong>Cardiovascular stress:</strong> Untreated OSA increases heart attack and stroke risk</li>
<li><strong>Blood pressure issues:</strong> OSA commonly causes hypertension</li>
<li><strong>Excessive sleepiness:</strong> Risk of falling asleep during donation</li>
<li><strong>Cognitive impairment:</strong> Sleep deprivation affects judgment and reaction time</li>
</ul>

<h3>Sleep Apnea Severity</h3>

<table>
<thead>
<tr>
<th>Severity</th>
<th>AHI (Apnea-Hypopnea Index)</th>
<th>Donation Eligibility</th>
</tr>
</thead>
<tbody>
<tr>
<td>None/Minimal</td>
<td><5 events/hour</td>
<td>✓ No issues</td>
</tr>
<tr>
<td>Mild</td>
<td>5-14 events/hour</td>
<td>✓ If treated or monitored</td>
</tr>
<tr>
<td>Moderate</td>
<td>15-29 events/hour</td>
<td>⚠ Only if well-controlled with treatment</td>
</tr>
<tr>
<td>Severe</td>
<td>≥30 events/hour</td>
<td>❌ Must be treated; untreated = deferral</td>
</tr>
</tbody>
</table>

<h3>Related Conditions That May Affect Eligibility</h3>

<ul>
<li><strong>Obesity hypoventilation syndrome:</strong> May require additional screening</li>
<li><strong>Pulmonary hypertension:</strong> From chronic sleep apnea (often disqualifying)</li>
<li><strong>Heart failure:</strong> Sleep apnea-induced cardiac dysfunction (disqualifying)</li>
<li><strong>Atrial fibrillation:</strong> May disqualify depending on treatment</li>
<li><strong>Type 2 diabetes:</strong> Common with sleep apnea; see diabetes policies</li>
</ul>

{PRO_TOOLKIT}

<h2 id="screening">What Screening Staff Will Check</h2>

<h3>Sleep Apnea Questions</h3>

<ol>
<li><strong>"Do you have sleep apnea?"</strong></li>
<li><strong>"Do you use a CPAP or BiPAP machine?"</strong></li>
<li><strong>"How many hours per night do you use it?"</strong></li>
<li><strong>"How long have you had sleep apnea?"</strong></li>
<li><strong>"Did you get adequate sleep last night?"</strong></li>
<li><strong>"Do you feel excessively sleepy today?"</strong></li>
<li><strong>"Do you have high blood pressure related to sleep apnea?"</strong></li>
</ol>

<h3>What Staff Is Assessing</h3>

<ul>
<li><strong>Treatment compliance:</strong> Are you using prescribed therapy?</li>
<li><strong>Sleep quality:</strong> Did you get restful sleep before donation?</li>
<li><strong>Alertness:</strong> Are you awake and oriented enough to donate safely?</li>
<li><strong>Cardiovascular stability:</strong> Is blood pressure controlled?</li>
<li><strong>Safety:</strong> Risk of falling asleep during 1-2 hour donation process</li>
</ul>

<h3>CPAP Compliance Documentation</h3>

<p>Some centers may request:</p>

<ul>
<li><strong>CPAP machine data:</strong> Download showing usage hours</li>
<li><strong>Doctor's note:</strong> Confirming diagnosis and treatment compliance</li>
<li><strong>Recent sleep study:</strong> Showing effectiveness of current CPAP settings</li>
<li><strong>AHI on treatment:</strong> Proving sleep apnea is controlled with therapy</li>
</ul>

<p><strong>Note:</strong> Most centers don't routinely require this documentation unless you have other concerning factors (severe sleepiness, uncontrolled BP, recent diagnosis).</p>

<h2 id="cpap-users">Tips for CPAP/BiPAP Users</h2>

<h3>Before Donation</h3>

<ul>
<li><strong>Use CPAP night before:</strong> Essential to get adequate rest</li>
<li><strong>Check equipment:</strong> Ensure mask isn't leaking, machine working properly</li>
<li><strong>Full night's sleep:</strong> Aim for 7-9 hours with CPAP on</li>
<li><strong>Morning assessment:</strong> Honestly evaluate if you feel rested enough</li>
<li><strong>Avoid sleep deprivation:</strong> Don't donate if you had poor sleep quality</li>
</ul>

<h3>Day of Donation</h3>

<ul>
<li><strong>Eat substantial breakfast:</strong> Helps maintain alertness</li>
<li><strong>Moderate caffeine OK:</strong> Coffee or tea can help if slightly tired (don't overdo it)</li>
<li><strong>Avoid heavy meals:</strong> Can increase drowsiness</li>
<li><strong>Stay hydrated:</strong> 16-20 oz water 2-3 hours before</li>
<li><strong>Schedule wisely:</strong> Donate during your most alert time of day</li>
</ul>

<h3>During Donation</h3>

<ul>
<li><strong>Stay engaged:</strong> Listen to stimulating podcast, music, or audiobook</li>
<li><strong>Keep eyes open:</strong> Don't close eyes even if resting</li>
<li><strong>Alert staff if drowsy:</strong> Tell them immediately if you feel sleepy</li>
<li><strong>Avoid relaxation content:</strong> Skip meditation apps or calming music that might make you drowsy</li>
<li><strong>Talk to staff:</strong> Conversation helps maintain alertness</li>
</ul>

<h3>After Donation</h3>

<ul>
<li><strong>Don't drive if drowsy:</strong> Have backup transportation plan</li>
<li><strong>Rest 15-30 minutes:</strong> Allow time to ensure alertness before leaving</li>
<li><strong>Eat and hydrate:</strong> Helps maintain energy</li>
<li><strong>Monitor fatigue:</strong> Donation can be tiring; don't fight severe sleepiness</li>
<li><strong>Continue CPAP:</strong> Don't skip treatment after donation</li>
</ul>

<h3>Long-Term Donation Considerations</h3>

<ul>
<li><strong>Track sleep quality:</strong> Note if donations affect your sleep</li>
<li><strong>Maintain CPAP compliance:</strong> Continue using 4+ hours nightly</li>
<li><strong>Regular follow-ups:</strong> Keep appointments with sleep doctor</li>
<li><strong>Monitor blood pressure:</strong> Check at each donation</li>
<li><strong>Weight management:</strong> Weight loss often improves sleep apnea</li>
</ul>

<h2 id="other-treatments">Other Sleep Apnea Treatments</h2>

<h3>Oral Appliances</h3>

<p>Mandibular advancement devices (MADs):</p>

<ul>
<li><strong>Donation status:</strong> Allowed if sleep apnea well-controlled</li>
<li><strong>Compliance:</strong> Must be using device nightly</li>
<li><strong>Effectiveness check:</strong> Should have follow-up sleep study confirming improvement</li>
</ul>

<h3>Surgical Treatments</h3>

<table>
<thead>
<tr>
<th>Surgery Type</th>
<th>Waiting Period</th>
<th>Requirements</th>
</tr>
</thead>
<tbody>
<tr>
<td>UPPP (uvulopalatopharyngoplasty)</td>
<td>6-8 weeks</td>
<td>Full healing, normal eating, no pain</td>
</tr>
<tr>
<td>Tonsillectomy/adenoidectomy</td>
<td>4-6 weeks</td>
<td>Complete healing</td>
</tr>
<tr>
<td>Septoplasty/turbinate reduction</td>
<td>4-6 weeks</td>
<td>No bleeding, full recovery</td>
</tr>
<tr>
<td>Hypoglossal nerve stimulation (Inspire)</td>
<td>3-6 months</td>
<td>Device fully healed, settings optimized</td>
</tr>
<tr>
<td>Maxillomandibular advancement (MMA)</td>
<td>6 months+</td>
<td>Complete healing, medical clearance</td>
</tr>
</tbody>
</table>

<h3>Positional Therapy and Lifestyle</h3>

<ul>
<li><strong>Positional devices:</strong> (Sleep on side) - Allowed</li>
<li><strong>Weight loss:</strong> Often improves sleep apnea; allowed</li>
<li><strong>Alcohol avoidance:</strong> Good practice for both sleep apnea and donation</li>
</ul>

<h3>Medications</h3>

<p>Some people with central sleep apnea take medications:</p>

<ul>
<li><strong>Acetazolamide (Diamox):</strong> Usually allowed</li>
<li><strong>Theophylline:</strong> Check center policy</li>
<li><strong>Modafinil/armodafinil:</strong> For excessive sleepiness - usually allowed</li>
</ul>

<h3>When to Stop Donating</h3>

<ul>
<li>Unable to use CPAP regularly</li>
<li>Sleep apnea worsens despite treatment</li>
<li>Develop excessive daytime sleepiness</li>
<li>Blood pressure becomes uncontrolled</li>
<li>Fall asleep during donation process</li>
<li>Develop sleep apnea-related heart problems</li>
</ul>

{related_reading([
    ('/blog/can-you-donate-plasma-with-narcolepsy-2026', 'Narcolepsy and Sleep Disorders'),
    ('/blog/can-you-donate-plasma-with-high-blood-pressure', 'Hypertension Eligibility'),
    ('/blog/plasma-donation-health-screening-complete-guide', 'Complete Health Screening Guide')
])}

{footer_related()}
''',
        'faqs': [
            make_faq(
                "Do I need to bring proof of my CPAP usage to donate?",
                "Not usually. Most centers accept your verbal confirmation that you use CPAP regularly. However, if you have other concerning factors (very high blood pressure, excessive sleepiness, severe sleep apnea), they may request documentation from your sleep doctor or CPAP compliance data from your machine. Call ahead if you're uncertain about specific requirements."
            ),
            make_faq(
                "Can I donate if I was diagnosed with sleep apnea but don't use my CPAP?",
                "This depends on severity. If you have mild sleep apnea that your doctor said could be managed with weight loss and lifestyle changes, you might be eligible. However, if you were prescribed CPAP for moderate to severe sleep apnea and aren't using it, centers may defer you due to safety concerns—untreated sleep apnea causes excessive sleepiness, high blood pressure, and cardiovascular risks."
            ),
            make_faq(
                "What if I fall asleep during the plasma donation?",
                "This would be unsafe and could cause injury if you move suddenly or the needle dislodges. If you have significant trouble staying awake during the day despite CPAP use, you should not donate plasma. Discuss the excessive sleepiness with your sleep doctor—you may need CPAP settings adjusted, a different treatment, or evaluation for other sleep disorders."
            ),
            make_faq(
                "Will donating plasma make my sleep apnea worse?",
                "No, plasma donation doesn't directly worsen sleep apnea. However, if donation causes fatigue that leads you to skip CPAP use or if dehydration affects your sleep quality, there could be indirect effects. Maintain good hydration, continue CPAP compliance, and get adequate sleep between donations. If you notice worsening sleep quality after starting donation, consider reducing frequency."
            ),
            make_faq(
                "Can I donate if I have sleep apnea from being overweight?",
                "Yes, as long as your sleep apnea is well-controlled with CPAP or other treatment and you meet other eligibility criteria. Obesity-related sleep apnea is very common. However, some centers have BMI limits (typically 40-45) for practical reasons (venous access, equipment weight limits). Weight-related sleep apnea that's untreated or causing complications like heart failure would disqualify you."
            ),
        ]
    },
    {
        'slug': 'can-you-donate-plasma-with-fibromyalgia-2026',
        'title': 'Can You Donate Plasma With Fibromyalgia? [2026 Medication Guide]',
        'meta': 'Fibromyalgia doesn\'t disqualify plasma donation, and most fibromyalgia medications are allowed. Complete guide to chronic pain and eligibility for 2026.',
        'category': 'Medical Eligibility',
        'read_time': 8,
        'toc': [
            ('quick-answer', 'Quick Answer'),
            ('fibromyalgia-eligibility', 'Fibromyalgia and Donation Eligibility'),
            ('medications', 'Fibromyalgia Medications (Most Allowed)'),
            ('pain-management', 'Chronic Pain Considerations'),
            ('screening', 'What Screening Staff Will Ask'),
            ('tips', 'Managing Donation With Fibromyalgia'),
        ],
        'content': f'''
<div class="quick-answer">
<h3>Quick Answer: Can You Donate With Fibromyalgia?</h3>
<p><strong>Yes, fibromyalgia doesn't disqualify you from plasma donation.</strong> Most fibromyalgia medications—including Lyrica, Cymbalta, gabapentin, and muscle relaxers—are acceptable. The key factors are your symptom stability, ability to sit comfortably for 1-2 hours, and whether your chronic pain is managed well enough to tolerate the donation process.</p>
</div>

<h2 id="fibromyalgia-eligibility">Fibromyalgia and Donation Eligibility</h2>

<h3>Why Fibromyalgia Is Acceptable</h3>

<ul>
<li><strong>Not autoimmune:</strong> Fibromyalgia is a chronic pain syndrome, not an immune disorder</li>
<li><strong>Doesn't affect plasma:</strong> No abnormal antibodies or plasma protein changes</li>
<li><strong>Medications allowed:</strong> Most fibromyalgia treatments are acceptable</li>
<li><strong>Common condition:</strong> Affects about 4 million US adults</li>
</ul>

<h3>When You CAN Donate</h3>

<ul>
<li><strong>Stable symptoms:</strong> Pain and fatigue managed with treatment</li>
<li><strong>Acceptable medications:</strong> On allowed fibromyalgia medications</li>
<li><strong>Can sit comfortably:</strong> Able to remain in donation chair for 1-2 hours</li>
<li><strong>Adequate energy:</strong> Not experiencing severe fatigue flare</li>
<li><strong>Good pain day:</strong> Pain level tolerable for donation process</li>
<li><strong>No recent hospitalizations:</strong> For fibromyalgia-related issues</li>
</ul>

<h3>When You're Deferred</h3>

<ul>
<li><strong>Severe pain flare:</strong> Acute exacerbation preventing comfortable sitting</li>
<li><strong>Extreme fatigue:</strong> Too exhausted to safely donate</li>
<li><strong>Recent medication changes:</strong> Still adjusting to new fibromyalgia treatment</li>
<li><strong>Disqualifying pain medications:</strong> On certain opioids or controlled substances (center-specific)</li>
<li><strong>Unable to position arm:</strong> Pain preventing proper venipuncture positioning</li>
<li><strong>Co-occurring conditions:</strong> Fibromyalgia plus autoimmune disease that disqualifies</li>
</ul>

{AFFILIATE_BLOCK}

<h2 id="medications">Fibromyalgia Medications (Most Allowed)</h2>

<h3>FDA-Approved Fibromyalgia Medications</h3>

<table>
<thead>
<tr>
<th>Medication</th>
<th>Brand Name</th>
<th>Drug Class</th>
<th>Donation Status</th>
</tr>
</thead>
<tbody>
<tr>
<td>Pregabalin</td>
<td>Lyrica</td>
<td>Anticonvulsant</td>
<td>✓ Allowed</td>
</tr>
<tr>
<td>Duloxetine</td>
<td>Cymbalta</td>
<td>SNRI antidepressant</td>
<td>✓ Allowed</td>
</tr>
<tr>
<td>Milnacipran</td>
<td>Savella</td>
<td>SNRI</td>
<td>✓ Allowed</td>
</tr>
</tbody>
</table>

<h3>Off-Label Medications Commonly Used</h3>

<table>
<thead>
<tr>
<th>Medication</th>
<th>Brand Name</th>
<th>Drug Class</th>
<th>Donation Status</th>
</tr>
</thead>
<tbody>
<tr>
<td>Gabapentin</td>
<td>Neurontin</td>
<td>Anticonvulsant</td>
<td>✓ Allowed</td>
</tr>
<tr>
<td>Amitriptyline</td>
<td>Elavil</td>
<td>Tricyclic antidepressant</td>
<td>✓ Allowed</td>
</tr>
<tr>
<td>Cyclobenzaprine</td>
<td>Flexeril</td>
<td>Muscle relaxant</td>
<td>✓ Allowed</td>
</tr>
<tr>
<td>Tizanidine</td>
<td>Zanaflex</td>
<td>Muscle relaxant</td>
<td>✓ Allowed</td>
</tr>
<tr>
<td>Venlafaxine</td>
<td>Effexor</td>
<td>SNRI antidepressant</td>
<td>✓ Allowed</td>
</tr>
<tr>
<td>Tramadol</td>
<td>Ultram</td>
<td>Atypical opioid</td>
<td>✓ Usually allowed with prescription</td>
</tr>
</tbody>
</table>

{PRO_TOOLKIT}

<h3>Pain Medications</h3>

<table>
<thead>
<tr>
<th>Medication Type</th>
<th>Examples</th>
<th>Donation Status</th>
</tr>
</thead>
<tbody>
<tr>
<td>NSAIDs</td>
<td>Ibuprofen, naproxen, meloxicam</td>
<td>✓ Allowed</td>
</tr>
<tr>
<td>Acetaminophen</td>
<td>Tylenol</td>
<td>✓ Allowed</td>
</tr>
<tr>
<td>Topical analgesics</td>
<td>Lidocaine patches, capsaicin cream</td>
<td>✓ Allowed</td>
</tr>
<tr>
<td>Tramadol</td>
<td>Ultram</td>
<td>✓ Usually allowed with valid prescription</td>
</tr>
<tr>
<td>Weak opioids</td>
<td>Codeine (in Tylenol #3)</td>
<td>⚠ Check center policy, need prescription</td>
</tr>
<tr>
<td>Strong opioids</td>
<td>Oxycodone, hydrocodone, morphine</td>
<td>❌ Often disqualifying (center-specific)</td>
</tr>
</tbody>
</table>

<h3>Sleep Medications</h3>

<p>Many fibromyalgia patients take sleep aids:</p>

<table>
<thead>
<tr>
<th>Medication</th>
<th>Brand Name</th>
<th>Status</th>
</tr>
</thead>
<tbody>
<tr>
<td>Trazodone</td>
<td>Desyrel</td>
<td>✓ Allowed</td>
</tr>
<tr>
<td>Melatonin</td>
<td>Various</td>
<td>✓ Allowed</td>
</tr>
<tr>
<td>Zolpidem</td>
<td>Ambien</td>
<td>✓ Allowed (if well-rested at donation)</td>
</tr>
<tr>
<td>Eszopiclone</td>
<td>Lunesta</td>
<td>✓ Allowed (if well-rested at donation)</td>
</tr>
</tbody>
</table>

<h3>Medications That May Disqualify</h3>

<ul>
<li><strong>Immunosuppressants:</strong> If you have overlapping autoimmune disease (lupus, RA)</li>
<li><strong>Strong opioids:</strong> Some centers defer patients on chronic opioid therapy</li>
<li><strong>Medical marijuana:</strong> THC products (check state and center policies)</li>
<li><strong>Muscle relaxants causing severe sedation:</strong> If you can't stay alert during donation</li>
</ul>

<h2 id="pain-management">Chronic Pain Considerations</h2>

<h3>Assessing If You're Well Enough to Donate</h3>

<p>Before scheduling donation, honestly evaluate:</p>

<ul>
<li><strong>Pain level:</strong> Can you sit still for 1-2 hours without severe discomfort?</li>
<li><strong>Fatigue:</strong> Do you have enough energy for donation and recovery?</li>
<li><strong>Fibro fog:</strong> Is your cognitive function clear enough to understand process and consent?</li>
<li><strong>Positioning:</strong> Can you keep arm extended without significant pain?</li>
<li><strong>Recovery capacity:</strong> Can you afford the physical toll donation may take?</li>
</ul>

<h3>Fibromyalgia Trigger Points</h3>

<p>Consider how donation positioning affects tender points:</p>

<ul>
<li><strong>Neck and shoulders:</strong> Donation chair angle may strain these areas</li>
<li><strong>Upper back:</strong> Prolonged sitting could trigger pain</li>
<li><strong>Arm position:</strong> Extended arm may affect shoulder/elbow tender points</li>
<li><strong>Lower back:</strong> Chair support important for lumbar tender points</li>
</ul>

<h3>Post-Exertional Malaise</h3>

<p>Many fibromyalgia patients experience symptom flares after physical stress:</p>

<ul>
<li><strong>Plan recovery time:</strong> Clear schedule for 24-48 hours after donation</li>
<li><strong>Track patterns:</strong> Note if donation consistently triggers flares</li>
<li><strong>Reduce frequency if needed:</strong> Weekly instead of twice weekly</li>
<li><strong>Listen to your body:</strong> Skip donations during bad symptom periods</li>
</ul>

<h2 id="screening">What Screening Staff Will Ask</h2>

<h3>Fibromyalgia Questions</h3>

<ol>
<li><strong>"Do you have fibromyalgia or chronic pain syndrome?"</strong></li>
<li><strong>"What medications do you take for fibromyalgia?"</strong></li>
<li><strong>"Are you experiencing a pain flare today?"</strong></li>
<li><strong>"Can you sit comfortably for 1-2 hours?"</strong></li>
<li><strong>"Do you take any narcotic pain medications?"</strong></li>
<li><strong>"How is your energy level today?"</strong></li>
<li><strong>"Do you have any other autoimmune or chronic illnesses?"</strong></li>
</ol>

<h3>What Staff Is Assessing</h3>

<ul>
<li><strong>Medication eligibility:</strong> Are you on allowed fibromyalgia medications?</li>
<li><strong>Physical capability:</strong> Can you tolerate donation positioning and duration?</li>
<li><strong>Alertness:</strong> Are pain medications causing excessive sedation?</li>
<li><strong>Safety:</strong> Is your pain managed well enough for safe donation?</li>
<li><strong>Overall health:</strong> Any fibromyalgia-related complications affecting eligibility?</li>
</ul>

<h3>Information to Provide</h3>

<ul>
<li>Complete medication list including dosages</li>
<li>Any controlled substance prescriptions (opioids)</li>
<li>Other diagnoses (fibromyalgia often coexists with autoimmune conditions)</li>
<li>Recent medication changes or adjustments</li>
<li>Typical pain patterns and current status</li>
</ul>

<h2 id="tips">Managing Donation With Fibromyalgia</h2>

<h3>Before Donation</h3>

<ul>
<li><strong>Take medications as prescribed:</strong> Don't skip doses before donation</li>
<li><strong>Pain management timing:</strong> Take pain meds 30-60 min before appointment</li>
<li><strong>Gentle stretching:</strong> Light movement to reduce stiffness</li>
<li><strong>Warm shower:</strong> Helps relax muscles before leaving home</li>
<li><strong>Eat balanced meal:</strong> Helps with energy and blood sugar stability</li>
<li><strong>Dress comfortably:</strong> Soft, non-restrictive clothing</li>
<li><strong>Adequate sleep:</strong> Priority night before donation</li>
</ul>

<h3>During Donation</h3>

<ul>
<li><strong>Request positioning help:</strong> Ask for pillows or arm support</li>
<li><strong>Communicate pain:</strong> Tell staff immediately if positioning causes significant pain</li>
<li><strong>Bring comfort items:</strong> Small pillow for lumbar support, stress ball alternative if hand pain</li>
<li><strong>Distraction techniques:</strong> Music, audiobook, or podcast to manage discomfort</li>
<li><strong>Gentle movement:</strong> Shift weight slightly if comfortable (don't move donation arm)</li>
<li><strong>Temperature control:</strong> Request blanket if cold worsens pain</li>
</ul>

<h3>After Donation</h3>

<ul>
<li><strong>Extended rest period:</strong> Take 20-30 minutes in recovery area</li>
<li><strong>Gentle movement:</strong> Slow, careful movements when standing</li>
<li><strong>Hydration:</strong> 8-10 glasses water over next 24 hours</li>
<li><strong>Protein intake:</strong> Replace lost plasma proteins with lean protein</li>
<li><strong>Pain management:</strong> Continue regular medications, use heat/ice as needed</li>
<li><strong>Rest day:</strong> Plan low-activity schedule for 24 hours post-donation</li>
<li><strong>Gentle stretching:</strong> Light movement to prevent stiffness</li>
</ul>

<h3>Managing Post-Donation Flares</h3>

<p>If donation triggers fibromyalgia symptoms:</p>

<ul>
<li><strong>Track patterns:</strong> Keep log of how you feel after each donation</li>
<li><strong>Reduce frequency:</strong> Try once weekly or every 10 days instead of twice weekly</li>
<li><strong>Optimize timing:</strong> Donate on your "best" days when symptoms are mild</li>
<li><strong>Extra self-care:</strong> Increase rest, gentle exercise, stress management</li>
<li><strong>Consider stopping:</strong> If flares are severe or prolonged, donation may not be worth it</li>
</ul>

<h3>Cognitive Function ("Fibro Fog")</h3>

<ul>
<li><strong>Donate when mental clarity is best:</strong> Morning vs afternoon depends on your pattern</li>
<li><strong>Bring notes:</strong> Write down questions or concerns beforehand</li>
<li><strong>Ask for repetition:</strong> Don't hesitate to ask staff to repeat instructions</li>
<li><strong>Check understanding:</strong> Confirm you understand post-donation care instructions</li>
</ul>

<h3>When to Skip or Stop Donating</h3>

<ul>
<li>Severe pain flare making sitting intolerable</li>
<li>Extreme fatigue or fibromyalgia crash</li>
<li>Medication changes causing instability</li>
<li>Consistent post-donation flares lasting days</li>
<li>Unable to maintain adequate nutrition/hydration for recovery</li>
<li>Worsening overall fibromyalgia symptoms</li>
</ul>

{related_reading([
    ('/blog/can-you-donate-plasma-on-antidepressants-2026', 'Antidepressants and Plasma Donation'),
    ('/blog/can-you-donate-plasma-with-chronic-fatigue-syndrome', 'Chronic Fatigue Syndrome Guide'),
    ('/blog/pain-medications-plasma-donation-eligibility', 'Complete Pain Medication Guide')
])}

{footer_related()}
''',
        'faqs': [
            make_faq(
                "Will donating plasma make my fibromyalgia worse?",
                "Plasma donation could potentially trigger a fibromyalgia flare in some people due to physical stress, dehydration, or prolonged positioning. However, many fibromyalgia patients donate successfully without worsening symptoms. Key factors are good hydration, adequate rest, pain management, and limiting donation frequency. Start with once weekly and see how your body responds before increasing frequency."
            ),
            make_faq(
                "Can I donate if I take Lyrica or gabapentin for fibromyalgia?",
                "Yes, both pregabalin (Lyrica) and gabapentin (Neurontin) are allowed for plasma donation. These anticonvulsant medications used for neuropathic pain don't disqualify you. Just make sure you take your medication as prescribed and aren't experiencing excessive sedation or dizziness that would make donation unsafe."
            ),
            make_faq(
                "What if I'm too tired from fibromyalgia to donate?",
                "Severe fatigue is a valid reason to skip donation. If you're experiencing a fatigue flare, your body needs rest and energy conservation, not the additional stress of plasma donation. Only donate on days when your energy level is adequate to tolerate the 1-2 hour process plus recovery. Pushing through severe fatigue could worsen your fibromyalgia."
            ),
            make_faq(
                "Can I donate if I take opioids for fibromyalgia pain?",
                "This depends on the specific opioid and center policy. Tramadol is usually allowed with a valid prescription. Stronger opioids (oxycodone, hydrocodone, morphine) may disqualify you at some centers due to concerns about impaired judgment, sedation, or medication misuse. Check with your specific donation center about their policy on opioid medications."
            ),
            make_faq(
                "Does fibromyalgia cause any abnormalities in plasma that would disqualify me?",
                "No, fibromyalgia doesn't produce abnormal antibodies or alter plasma protein composition in ways that would disqualify donation. It's a chronic pain syndrome, not an autoimmune or immune disorder. Your plasma quality should be normal. However, if you have fibromyalgia plus an autoimmune condition (like lupus or RA), the autoimmune diagnosis might disqualify you regardless of fibromyalgia."
            ),
        ]
    },
]

def main():
    """Generate all pages"""
    print(f"Generating {len(PAGES)} medical condition pages...")

    for i, page in enumerate(PAGES, 1):
        output_path = os.path.join(BLOG_DIR, f"{page['slug']}.html")

        html = make_en_page(
            slug=page['slug'],
            title=page['title'],
            meta_desc=page['meta'],
            category=page['category'],
            read_time=page['read_time'],
            toc_items=page['toc'],
            content_html=page['content'],
            faq_schema=page['faqs']
        )

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)

        print(f"  [{i}/{len(PAGES)}] ✓ {page['slug']}.html")

    print(f"\n✓ Successfully generated {len(PAGES)} pages in {BLOG_DIR}/")

if __name__ == '__main__':
    main()
