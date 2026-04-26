#!/usr/bin/env python3
"""
AI Citation Optimization for PlasmaPayCalculator.com
Adds Article + FAQPage schemas and refreshes dateModified sitewide.
"""

import os
import re
import json

SITE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATE_MODIFIED = "2026-04-26"
PUBLISHER = {
    "@type": "Organization",
    "name": "PlasmaPayCalculator.com",
    "logo": {"@type": "ImageObject", "url": "https://plasmapaycalculator.com/images/logo.png"},
}

# --------------------------------------------------------------------------
# Category-specific FAQ data
# --------------------------------------------------------------------------
CATEGORY_FAQS = {
    "city": [
        (
            "How much can I earn donating plasma per month?",
            "Most plasma donors earn $400–$1,000 per month donating twice weekly at the maximum allowed frequency. New donors typically earn $700–$1,200 in their first month due to promotional bonuses offered at CSL Plasma, BioLife, Octapharma, and Grifols. Returning donor rates average $50–$100 per visit depending on weight and the center's current promotions. Rates vary significantly by location — urban markets tend to offer higher bonuses to compete for donors.",
        ),
        (
            "What do I need to bring to my first plasma donation?",
            "First-time donors must bring: (1) a valid government-issued photo ID (driver's license or passport); (2) proof of Social Security number (Social Security card, W-2, or tax document showing the full number); (3) proof of current address (utility bill, bank statement, or lease dated within the last 60 days — most centers require it to be dated within 30–45 days). Some centers also require your vaccination records for certain diseases. Call ahead to confirm the specific center's documentation requirements before your visit.",
        ),
        (
            "How long does a plasma donation take?",
            "Your first plasma donation takes 2–3 hours including a medical screening, physical exam, and the donation itself. Repeat donations typically take 60–90 minutes total — about 35–50 minutes for the actual plasmapheresis process, plus check-in and post-donation observation. Plasmapheresis is a machine process where blood is drawn, plasma is separated, and red cells are returned to your body — this cycle repeats 4–6 times during a session. Staying well-hydrated before your appointment significantly speeds up the process.",
        ),
    ],
    "pay": [
        (
            "How much does plasma donation pay per visit in 2026?",
            "Repeat donor pay rates in 2026 range from $45–$130 per visit depending on your weight class and the plasma center chain. Weight tiers: under 150 lbs pays the lowest rate, 150–174 lbs earns mid-tier rates, and donors over 175 lbs earn the highest rates because heavier donors can safely donate a larger volume of plasma. New donor promotions dramatically increase first-month earnings: CSL Plasma, BioLife, Octapharma, and Grifols all offer $700–$1,200 in the first 8 donations via promotional bonus structures.",
        ),
        (
            "Which plasma center pays the most in 2026?",
            "Pay rates vary by location more than by chain — the same center brand may pay differently in Chicago versus a rural market. In general, Octapharma Plasma and CSL Plasma tend to offer the highest new donor promotions ($900–$1,200 for the first month). For repeat donors, rates are more uniform across chains at $50–$100 per visit. The best strategy: check all centers within driving distance using their current promotions, then return to the highest-paying center as a new donor before switching to optimize the next new-donor bonus.",
        ),
        (
            "Can I donate plasma at two different centers to earn more?",
            "Technically yes — you can be registered at multiple plasma donation centers. However, there is an industry-shared database (IQPP/National Donor Deferral Registry) that tracks donation frequency. Donating at two centers to exceed the FDA-allowed maximum of 2 donations per 7-day period is prohibited and dangerous. The safe approach: donate at one center, earn the new donor bonus, then switch centers after the promotional period ends to earn the next center's new donor bonus — this is fully within the rules.",
        ),
    ],
    "eligibility": [
        (
            "What medical conditions disqualify you from donating plasma?",
            "Permanent disqualifications include: HIV/AIDS, hepatitis B or C, certain cancers (leukemia, lymphoma), Creutzfeldt-Jakob disease (CJD), and a history of IV drug use. Temporary deferrals (typically 30–365 days) may apply for: recent tattoos or piercings (3–12 months depending on state regulations and center policy), certain medications, recent surgery, pregnancy and postpartum recovery (usually 6 weeks to 6 months after delivery), recent illness or fever, and travel to malaria-endemic countries. Each center conducts its own screening — call ahead if you have a specific condition.",
        ),
        (
            "Can I donate plasma if I take prescription medication?",
            "Many medications are acceptable for plasma donation. Generally acceptable: most blood pressure medications, antidepressants (SSRIs, SNRIs), antihistamines, thyroid medication, and most common maintenance medications. Generally disqualifying: blood thinners (warfarin, Eliquis, Xarelto), immunosuppressants, certain acne medications (isotretinoin/Accutane), some antibiotics within 14–30 days of completion, and medications derived from human pituitary hormones. Plasma centers maintain their own medication deferral lists — bring a list of all medications to your screening for an accurate assessment.",
        ),
        (
            "What are the weight and age requirements for plasma donation?",
            "Minimum weight: 110 lbs (50 kg) — this is an FDA safety requirement, not a center preference. Age: 18–69 at most plasma centers; some centers accept donors up to age 70 with medical clearance. Maximum weight: there is no upper weight limit, but weight determines your donation volume tier, which affects pay rates. Blood pressure and pulse must be within normal ranges at time of donation. Hematocrit (iron in red blood cells) must be above a minimum threshold, which is why iron supplementation and adequate protein intake are important for regular donors.",
        ),
    ],
    "preparation": [
        (
            "What should I eat before donating plasma?",
            "Eat a high-protein, low-fat meal 2–3 hours before donation. Good pre-donation meals: eggs with toast, chicken with rice, turkey sandwich, Greek yogurt with fruit, or oatmeal with protein. Avoid fatty or fried foods for 24 hours before donation — high fat content (lipemia) can make your plasma appear cloudy and cause your donation to be rejected. Drink 64–80 oz of water in the 24 hours before donation — dehydration is the most common reason for slow donations and post-donation side effects. On donation day, eat within 2–3 hours of your appointment; never donate fasted.",
        ),
        (
            "How do I prepare for plasma donation to avoid side effects?",
            "Pre-donation checklist: (1) Drink 6–8 glasses of water the day before and the day of donation; (2) Eat a high-protein, low-fat meal 2–3 hours before; (3) Avoid alcohol for at least 24 hours (48 hours is better); (4) Avoid caffeine on donation day — it causes dehydration; (5) Get adequate sleep the night before; (6) Avoid strenuous exercise for 12 hours before donation. Post-donation: keep the bandage on for 30–60 minutes, avoid heavy lifting with the donation arm for 4–6 hours, continue drinking fluids for the rest of the day, and eat a protein-rich snack within 1–2 hours of donating.",
        ),
        (
            "How can I increase my iron levels for plasma donation?",
            "Iron-rich foods to eat regularly: red meat (beef, lamb), chicken liver, fortified cereals, spinach, lentils, tofu, and pumpkin seeds. Take iron supplements 2–3 times per week (daily supplementation can cause constipation) — ferrous sulfate 325mg or a chelated iron form for easier digestion. Pair iron-rich foods or supplements with vitamin C (orange juice, bell peppers) to increase iron absorption by up to 3x. Avoid coffee or tea within 1 hour of iron-rich meals — tannins block iron absorption. Getting deferrals for low hematocrit is common among regular donors; addressing iron proactively prevents the 4-week wait between deferrals.",
        ),
    ],
    "side_effects": [
        (
            "What are the most common plasma donation side effects?",
            "Most common (mild, resolve within hours): fatigue and weakness immediately after donation, lightheadedness or dizziness when standing quickly, bruising at the needle site, tingling or numbness around the mouth or fingers (from citrate anticoagulant affecting calcium — temporary and harmless), and arm soreness. Uncommon but possible: nausea, low blood pressure causing fainting (more common in dehydrated or first-time donors), and hematoma (blood pooling under skin) from needle insertion. Serious reactions (rare): allergic reaction to citrate, nerve damage from improper needle placement. If you experience chest pain, severe shortness of breath, or prolonged weakness, contact the center or seek medical care.",
        ),
        (
            "Why do I feel tired after donating plasma?",
            "Fatigue after plasma donation is caused primarily by fluid loss — plasma is about 90% water, and donating removes 690–880ml of fluid from your circulatory system. This temporarily reduces blood volume, which reduces oxygen delivery to muscles and brain, causing tiredness. Second cause: your body immediately begins replacing the donated plasma proteins, which is a metabolically demanding process. Most fatigue resolves within 4–12 hours with adequate fluid and protein intake. If fatigue persists beyond 24 hours or is severe, you may need to increase your pre-donation hydration, reduce donation frequency, or consult a doctor about iron or protein levels.",
        ),
        (
            "How long after plasma donation can I exercise?",
            "Avoid strenuous exercise for 24 hours after plasma donation. Light activity (walking, gentle stretching) is fine after a few hours. Avoid heavy lifting with the donation arm for 4–6 hours. The rest period matters because your blood volume is temporarily reduced, increasing risk of dizziness or poor exercise performance. Regular donors who exercise: schedule donations on rest days, not before workouts. If you consistently feel severely fatigued after donations, consider reducing to once per week instead of twice, and focus on protein intake (1g per pound of bodyweight daily) to support faster plasma regeneration.",
        ),
    ],
    "blood_type": [
        (
            "Does blood type affect how much plasma donation pays?",
            "Standard cash pay rates at most plasma centers are the same regardless of blood type — compensation is based on weight and donation frequency, not blood type. However, blood type does affect the medical value of your plasma and may influence special programs: AB blood type donors have universal plasma (can be transfused to any patient regardless of recipient blood type) and are highly sought by blood banks and hospitals, but most commercial plasma donation centers compensate equally. Some specialty plasma programs seek specific antibodies (hyperimmune plasma) that pay premium rates — these are separate programs from standard compensation.",
        ),
        (
            "What blood type is most valuable for plasma donation?",
            "For commercial plasma centers paying cash: all blood types are equally compensated. For medical/therapeutic purposes: AB plasma is most valuable because it is universal (any recipient can receive AB plasma regardless of their blood type). O negative is the universal donor for red blood cells, but not for plasma — O negative plasma can only be given to O negative recipients. For special programs like hyperimmune plasma (anti-rabies, anti-tetanus, anti-Rh), any blood type can participate if the donor has the required antibody titers. For regular plasma donation income, blood type has no effect on pay.",
        ),
        (
            "Do I need to know my blood type before donating plasma?",
            "No — you do not need to know your blood type to donate plasma. The plasma center will test your blood during your initial screening, which includes blood typing along with protein levels, hematocrit, blood pressure, pulse, weight, and infectious disease screening. You will receive your blood type results, which is a useful byproduct of the process. What matters more for eligibility is your hematocrit level (iron), total protein level, blood pressure within normal range, and weight above 110 lbs.",
        ),
    ],
    "center": [
        (
            "What is the difference between CSL Plasma, BioLife, and Octapharma?",
            "CSL Plasma: largest plasma collection network in the US with 300+ centers, known for iGive rewards program, typically pays $50–$90 per repeat visit, strong new donor bonuses. BioLife Plasma Services (owned by Takeda): 200+ centers, known for the BioLife app and promotional coupon system, pays $50–$90 per repeat visit, offers $900–$1,100 first-month promotions. Octapharma Plasma: 150+ centers, pays $60–$100+ for higher weight donors, OctaRewards loyalty program, often slightly higher per-visit rates than CSL. All three are FDA-licensed, use the same plasmapheresis process, and follow the same 2-donations-per-7-days safety limit. Choice should be based on which center is closest and which currently has the best new donor promotion.",
        ),
        (
            "How do plasma center new donor bonuses work?",
            "New donor promotions work by paying elevated rates on your first 6–10 donations rather than the standard repeat donor rate. Example structure: donations 1–2 may pay $100 each, donations 3–6 may pay $80 each, donations 7–8 may pay $70 each. The 'bonus' is the difference between these promotional rates and the standard $50–$70 repeat donor rate. After the promotional period ends, your pay drops to the standard repeat donor rate. The strategy most donors use: maximize donations during the promotional window (donate twice per week), then potentially switch to another center to take advantage of their new donor promotion.",
        ),
        (
            "Can I switch plasma centers and get the new donor bonus again?",
            "Yes — you can donate at multiple plasma centers and receive new donor promotions at each one, as long as you follow the FDA safety rule of no more than 2 donations per 7-day period. The centers share a national deferral database for safety, but they do not prevent you from registering as a 'new donor' elsewhere after completing one center's promotional period. The industry calls this 'center hopping.' Practical approach: finish a full promotional cycle at one center (4–8 weeks), then register at a competing center to earn their new donor bonus. Many experienced donors rotate between 2–3 centers annually.",
        ),
    ],
    "tax": [
        (
            "Is plasma donation money taxable income?",
            "Yes — plasma donation payments are taxable income according to IRS guidelines. Plasma centers pay you for your time and the discomfort of the process, not technically for the plasma itself (which would make it a sale of body tissue with different tax treatment). Most plasma centers will issue a 1099-NEC if you earn over $600 in a calendar year from their center. However, even if you earn less than $600 — or don't receive a 1099 — you are still legally required to report all plasma income on your federal tax return as 'Other Income.' Many donors fail to report this income, which can result in IRS notices and penalties.",
        ),
        (
            "Do plasma centers report donations to the IRS?",
            "Plasma centers are legally required to issue IRS Form 1099-NEC for any donor who earns $600 or more in a calendar year from their center. If you donate at multiple centers, each issues its own 1099 if you clear the $600 threshold at that center. The IRS also receives copies of all 1099s issued — the agency cross-references 1099 income against your filed return. As of 2023–2026, the IRS has been increasing enforcement of unreported gig and alternative income including plasma payments. The safest approach: track all plasma income across all centers and report it, even for amounts under $600.",
        ),
        (
            "What tax deductions can plasma donors claim?",
            "Legitimate deductions related to plasma donation (if you itemize): mileage driven to and from the plasma center (at the 2026 standard IRS mileage rate of 67 cents per mile); costs of required supplies the center requires you to purchase; parking fees. These are treated as unreimbursed business expenses if you treat plasma donation as self-employment income — which requires paying self-employment tax (15.3%) on top of regular income tax. Most casual donors earn less than would make itemization worthwhile — the standard deduction is simpler. If plasma income exceeds $5,000/year, consult a tax professional.",
        ),
    ],
    "first_time": [
        (
            "What happens during your first plasma donation?",
            "First visit timeline: (1) Registration (15–20 min): photo ID, SSN card, proof of address, sign consent forms; (2) Medical screening (30–45 min): nurse reviews medical history, checks vitals (blood pressure, pulse, temperature), tests blood for hematocrit and total protein, and may do a physical exam; (3) Donation (35–50 min): seated in a reclining chair, needle inserted into arm vein, blood drawn through plasmapheresis machine that separates plasma and returns red blood cells — cycle repeats 4–6 times; (4) Recovery (5–10 min): observation, bandage applied, receive payment loaded to a prepaid debit card. Total time: 2–3 hours on first visit, 60–90 minutes on subsequent visits.",
        ),
        (
            "Is plasma donation safe for regular donors?",
            "Plasma donation is safe at the FDA-allowed maximum frequency of twice per week (every 48 hours, no more than 110 donations per year). Long-term studies of regular donors show no significant negative health effects when the frequency limits are followed. The primary considerations for regular donors: maintain adequate protein intake (plasma proteins are rebuilt from dietary protein), stay well-hydrated, and maintain healthy iron levels to prevent hematocrit deferrals. The needle stick itself carries minimal infection risk — plasma centers use sterile, single-use equipment. Donors with certain conditions (anemia, very low body weight, active infections) should not donate.",
        ),
        (
            "How soon after my first donation can I donate again?",
            "The FDA requires at least 48 hours between plasma donations — this is the minimum interval, not a recommendation. The maximum is twice per 7-day calendar period. After your first donation, you can donate as soon as 48 hours later if you feel fully recovered and meet all health criteria at the screening. Most centers track your donation dates and will not allow you to donate too soon. New donors often feel more side effects (fatigue, dizziness) than regular donors — wait until you feel fully recovered before returning, even if 48 hours has passed.",
        ),
    ],
    "generic": [
        (
            "How often can you donate plasma legally?",
            "The FDA allows plasma donation up to twice per 7-day period, with at least 48 hours between donations. This equals a maximum of about 104 donations per year, though the FDA caps the annual total at 110 liters of plasma. Most regular donors donate 6–8 times per month. The 48-hour minimum exists because your body needs time to replenish plasma proteins (primarily albumin, immunoglobulins, and clotting factors). Donating more frequently than twice per week has been linked to protein deficiency and increased side effect rates — the limit exists to protect donor health, not just to regulate supply.",
        ),
        (
            "What is plasma used for after donation?",
            "Donated plasma is used to manufacture plasma-derived medicines (PDMs) that treat life-threatening conditions: immunoglobulin therapy for immune deficiencies, hemophilia A and B treatment (clotting factors VIII and IX), alpha-1 antitrypsin therapy for hereditary lung/liver disease, albumin for trauma and burn patients, and rabies/tetanus hyperimmune globulins. The US supplies approximately 70% of the world's plasma-derived medicines, largely because the US is one of the few countries that compensates plasma donors — higher compensation drives higher donation volume. Your plasma donation directly contributes to treatment of patients with rare, chronic diseases.",
        ),
        (
            "What disqualifies you from donating plasma?",
            "Permanent disqualifications: HIV/AIDS, hepatitis B or C, human T-cell lymphotropic virus (HTLV), certain cancers, Creutzfeldt-Jakob disease (CJD), history of IV drug use, and a history of receiving money for sex. Temporary deferrals vary by center and condition: recent tattoos or piercings (3–12 months), pregnancy and postpartum (6 months), recent illness or fever (recover fully first), active antibiotic treatment, recent travel to malaria zones (12 months), and some medications. Low hematocrit (iron) is the most common deferral reason for regular donors — addressable through diet and supplementation.",
        ),
    ],
}


def get_faq_category(slug: str) -> str:
    s = slug.lower().replace(".html", "")
    if any(x in s for x in ["what-to-eat", "breakfast", "hydration", "best-meal", "food-", "iron-supplement",
                              "protein-rich", "protein-food", "what-to-wear", "comfort-item", "prepare",
                              "best-drink", "vegan", "plant-based"]):
        return "preparation"
    if any(x in s for x in ["side-effect", "tired", "fatigue", "faint", "what-happens-to-your-body",
                              "hematocrit", "protein-level", "vein-health", "cold-weather", "winter-tip",
                              "after-donation", "pain", "bruise", "dehydr", "exercise-after"]):
        return "side_effects"
    if any(x in s for x in ["tax", "irs", "1099", "income-tax", "deduction", "social-security", "track-",
                              "shocking-irs", "texas-irs"]):
        return "tax"
    if any(x in s for x in ["can-you-donate", "eligib", "disqualif", "medical", "condition", "anxiety",
                              "depression", "autoimmune", "thyroid", "diabetes", "medication", "pregnancy",
                              "breastfeed", "low-iron", "deferral", "blood-test", "what-they-test",
                              "tattoo", "piercing", "temporarily", "permanent"]):
        return "eligibility"
    if any(x in s for x in ["-negative-", "-positive-", "ab-plasma", "ab-negative", "ab plasma",
                              "blood-type", "abo-plasma", "universal-donor", "universal-plasma"]):
        return "blood_type"
    if any(x in s for x in ["csl-", "biolife", "octapharma", "grifols", "adma-", "talecris", "thplasma",
                              "vitalant", "kedplasma", "immunotek", "bpl-plasma", "interstate-blood",
                              "plasma-center-comparison", "compare-plasma"]):
        return "center"
    if any(x in s for x in ["pay-rate", "pay-chart", "how-much", "calculator", "earn", "income", "bonus",
                              "make-money", "make-1000", "weekly-earn", "annual-plasma", "realistic",
                              "same-day", "emergency-cash", "highest-paying", "most-money", "maximize"]):
        return "pay"
    if any(x in s for x in ["first-time", "tips-for", "ultimate-", "step-by-step", "what-not-to-do",
                              "what-to-bring", "walk-in", "appointment", "how-long", "process",
                              "beginner", "new-to"]):
        return "first_time"
    if any(x in s for x in ["plasma-donation-", "best-plasma-center"]):
        return "city"
    return "generic"


def build_faq_schema(faqs: list) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a},
            }
            for q, a in faqs
        ],
    }


def build_article_schema(title: str, description: str, slug_url: str) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title[:110],
        "description": description,
        "image": "https://plasmapaycalculator.com/images/plasma-donation-guide.jpg",
        "datePublished": "2025-01-01",
        "dateModified": DATE_MODIFIED,
        "author": {"@type": "Organization", "name": "PlasmaPayCalculator.com"},
        "publisher": PUBLISHER,
        "mainEntityOfPage": {"@type": "WebPage", "@id": slug_url},
    }


def get_title(content: str) -> str:
    m = re.search(r"<title[^>]*>([^<]+)</title>", content, re.IGNORECASE)
    return m.group(1).strip() if m else "Plasma Pay Calculator"


def get_description(content: str) -> str:
    m = re.search(r'<meta\s+name=["\']description["\']\s+content=["\']([^"\']+)["\']', content, re.IGNORECASE)
    if not m:
        m = re.search(r'<meta\s+content=["\']([^"\']+)["\']\s+name=["\']description["\']', content, re.IGNORECASE)
    return m.group(1).strip() if m else ""


def inject_schemas(content: str, schemas: list, inject_after: str = "</title>") -> str:
    blocks = "\n".join(
        f'<script type="application/ld+json">\n{json.dumps(s, indent=2)}\n</script>'
        for s in schemas
    )
    idx = content.find(inject_after)
    if idx == -1:
        idx = content.find("</head>")
        if idx == -1:
            return content + "\n" + blocks
        return content[:idx] + blocks + "\n" + content[idx:]
    insert_at = idx + len(inject_after)
    return content[:insert_at] + "\n" + blocks + content[insert_at:]


def has_schema_type(content: str, schema_type: str) -> bool:
    # Match both pretty-printed and minified JSON variants
    return (
        f'"@type": "{schema_type}"' in content
        or f'"@type":"{schema_type}"' in content
        or f"'@type': '{schema_type}'" in content
    )


def refresh_date_modified(content: str) -> str:
    updated = re.sub(
        r'("dateModified"\s*:\s*")[^"]+(")',
        rf'\g<1>{DATE_MODIFIED}\2',
        content,
    )
    return updated


def process_blog_page(filepath: str) -> str:
    fname = os.path.basename(filepath)
    slug = fname.replace(".html", "")
    slug_url = f"https://plasmapaycalculator.com/blog/{slug}/"

    with open(filepath, encoding="utf-8") as f:
        content = f.read()

    schemas_to_inject = []
    changed = False

    # Article schema
    if not has_schema_type(content, "Article"):
        title = get_title(content)
        desc = get_description(content)
        schemas_to_inject.append(build_article_schema(title, desc, slug_url))

    # FAQPage schema
    if not has_schema_type(content, "FAQPage"):
        cat = get_faq_category(slug)
        faqs = CATEGORY_FAQS[cat]
        schemas_to_inject.append(build_faq_schema(faqs))

    if schemas_to_inject:
        content = inject_schemas(content, schemas_to_inject)
        changed = True

    # Always refresh dateModified
    new_content = refresh_date_modified(content)
    if new_content == content and not re.search(r'"dateModified"', content):
        # No existing dateModified — add it inside Article block if present
        pass  # Article schema added above already has the correct date
    if new_content != content:
        content = new_content
        changed = True

    if changed:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

    return "changed" if changed else "skip"


def process_root_pages(site_root: str):
    """Process important root-level pages missing Article schema."""
    ROOT_FAQS = {
        "index.html": CATEGORY_FAQS["pay"],
        "how-much-money-can-you-make-donating-plasma.html": CATEGORY_FAQS["pay"],
        "make-1000-month-plasma-donation.html": CATEGORY_FAQS["pay"],
        "faq.html": CATEGORY_FAQS["generic"],
        "ultimate-plasma-donation-guide.html": CATEGORY_FAQS["first_time"],
        "tips-for-first-time-plasma-donation.html": CATEGORY_FAQS["first_time"],
        "what-disqualifies-you-from-donating-plasma.html": CATEGORY_FAQS["eligibility"],
        "plasma-side-effects.html": CATEGORY_FAQS["side_effects"],
        "plasma-donation-tax-guide.html": CATEGORY_FAQS["tax"],
    }

    changed = 0
    for fname in os.listdir(site_root):
        if not fname.endswith(".html"):
            continue
        path = os.path.join(site_root, fname)
        with open(path, encoding="utf-8") as f:
            content = f.read()

        schemas_to_inject = []

        if not has_schema_type(content, "Article"):
            title = get_title(content)
            desc = get_description(content)
            slug_url = f"https://plasmapaycalculator.com/{fname.replace('.html', '')}/"
            schemas_to_inject.append(build_article_schema(title, desc, slug_url))

        if not has_schema_type(content, "FAQPage"):
            cat = get_faq_category(fname)
            faqs = CATEGORY_FAQS[cat]
            schemas_to_inject.append(build_faq_schema(faqs))

        new_content = refresh_date_modified(content)
        if new_content != content:
            content = new_content

        if schemas_to_inject:
            content = inject_schemas(content, schemas_to_inject)

        # Write if anything changed
        original = open(path, encoding="utf-8").read()
        if content != original:
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            changed += 1

    return changed


if __name__ == "__main__":
    # Fix the ROOT_FAQS bug above (typo in walrus)
    blog_dir = os.path.join(SITE_ROOT, "blog")
    blog_files = sorted(f for f in os.listdir(blog_dir) if f.endswith(".html"))

    print("=== BLOG PAGES ===")
    changed_count = 0
    skip_count = 0
    for fname in blog_files:
        result = process_blog_page(os.path.join(blog_dir, fname))
        if result == "changed":
            changed_count += 1
        else:
            skip_count += 1

    print(f"  Changed: {changed_count}, Already complete: {skip_count}")
    print(f"  Total blog: {len(blog_files)}")

    print()
    print("=== ROOT PAGES ===")
    root_changed = process_root_pages(SITE_ROOT)
    print(f"  Changed: {root_changed}")

    print()
    print("Done.")
