#!/usr/bin/env python3
"""Generate Round 3 City Pages: 100 NEW English city pages for US cities."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_round2_cities import gen_en_city

BLOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'blog')

# ============ 100 NEW ENGLISH CITY PAGES ============
en_cities = [
    # --- Arizona / Nevada (10) ---
    ('plasma-donation-mesa-az-2026', 'Mesa', 'AZ', 'Arizona', 'East Valley of the Phoenix metro area'),
    ('plasma-donation-chandler-az-2026', 'Chandler', 'AZ', 'Arizona', 'Southeast Valley of metro Phoenix'),
    ('plasma-donation-glendale-az-2026', 'Glendale', 'AZ', 'Arizona', 'West Valley of the Phoenix metro area'),
    ('plasma-donation-scottsdale-az-2026', 'Scottsdale', 'AZ', 'Arizona', 'Northeast Phoenix metro area'),
    ('plasma-donation-gilbert-az-2026', 'Gilbert', 'AZ', 'Arizona', 'Southeast Valley of metro Phoenix'),
    ('plasma-donation-surprise-az-2026', 'Surprise', 'AZ', 'Arizona', 'Northwest Valley of metro Phoenix'),
    ('plasma-donation-flagstaff-az-2026', 'Flagstaff', 'AZ', 'Arizona', 'Northern Arizona near the Grand Canyon'),
    ('plasma-donation-henderson-nv-2026', 'Henderson', 'NV', 'Nevada', 'Southern Nevada in the Las Vegas metro area'),
    ('plasma-donation-north-las-vegas-nv-2026', 'North Las Vegas', 'NV', 'Nevada', 'Northern Las Vegas metro area'),
    ('plasma-donation-sparks-nv-2026', 'Sparks', 'NV', 'Nevada', 'Western Nevada adjacent to Reno'),

    # --- California (23) ---
    ('plasma-donation-anaheim-ca-2026', 'Anaheim', 'CA', 'California', 'Orange County in Southern California'),
    ('plasma-donation-santa-ana-ca-2026', 'Santa Ana', 'CA', 'California', 'Central Orange County'),
    ('plasma-donation-irvine-ca-2026', 'Irvine', 'CA', 'California', 'South Orange County'),
    ('plasma-donation-chula-vista-ca-2026', 'Chula Vista', 'CA', 'California', 'South San Diego County near the Mexican border'),
    ('plasma-donation-san-bernardino-ca-2026', 'San Bernardino', 'CA', 'California', 'Inland Empire of Southern California'),
    ('plasma-donation-fontana-ca-2026', 'Fontana', 'CA', 'California', 'Western San Bernardino County in the Inland Empire'),
    ('plasma-donation-moreno-valley-ca-2026', 'Moreno Valley', 'CA', 'California', 'Western Riverside County in the Inland Empire'),
    ('plasma-donation-oxnard-ca-2026', 'Oxnard', 'CA', 'California', 'Ventura County on the Central Coast'),
    ('plasma-donation-ontario-ca-2026', 'Ontario', 'CA', 'California', 'Western San Bernardino County in the Inland Empire'),
    ('plasma-donation-rancho-cucamonga-ca-2026', 'Rancho Cucamonga', 'CA', 'California', 'Inland Empire at the base of the San Gabriel Mountains'),
    ('plasma-donation-elk-grove-ca-2026', 'Elk Grove', 'CA', 'California', 'Sacramento metro area in Northern California'),
    ('plasma-donation-pomona-ca-2026', 'Pomona', 'CA', 'California', 'Eastern Los Angeles County'),
    ('plasma-donation-pasadena-ca-2026', 'Pasadena', 'CA', 'California', 'San Gabriel Valley in Los Angeles County'),
    ('plasma-donation-torrance-ca-2026', 'Torrance', 'CA', 'California', 'South Bay area of Los Angeles County'),
    ('plasma-donation-escondido-ca-2026', 'Escondido', 'CA', 'California', 'North San Diego County'),
    ('plasma-donation-roseville-ca-2026', 'Roseville', 'CA', 'California', 'Placer County in the greater Sacramento area'),
    ('plasma-donation-hayward-ca-2026', 'Hayward', 'CA', 'California', 'East Bay of the San Francisco Bay Area'),
    ('plasma-donation-clovis-ca-2026', 'Clovis', 'CA', 'California', 'Fresno metro area in the Central Valley'),
    ('plasma-donation-victorville-ca-2026', 'Victorville', 'CA', 'California', 'High Desert region of San Bernardino County'),
    ('plasma-donation-palmdale-ca-2026', 'Palmdale', 'CA', 'California', 'Antelope Valley in northern Los Angeles County'),
    ('plasma-donation-lancaster-ca-2026', 'Lancaster', 'CA', 'California', 'Antelope Valley in northern Los Angeles County'),
    ('plasma-donation-vallejo-ca-2026', 'Vallejo', 'CA', 'California', 'North Bay of the San Francisco Bay Area'),
    ('plasma-donation-concord-ca-2026', 'Concord', 'CA', 'California', 'East Bay of the San Francisco Bay Area'),

    # --- Texas (14) ---
    ('plasma-donation-irving-tx-2026', 'Irving', 'TX', 'Texas', 'Dallas-Fort Worth metro area'),
    ('plasma-donation-garland-tx-2026', 'Garland', 'TX', 'Texas', 'Northeast Dallas-Fort Worth metro area'),
    ('plasma-donation-frisco-tx-2026', 'Frisco', 'TX', 'Texas', 'Northern Dallas-Fort Worth metro area'),
    ('plasma-donation-mckinney-tx-2026', 'McKinney', 'TX', 'Texas', 'Collin County in the northern DFW metro'),
    ('plasma-donation-killeen-tx-2026', 'Killeen', 'TX', 'Texas', 'Central Texas near Fort Cavazos (formerly Fort Hood)'),
    ('plasma-donation-midland-tx-2026', 'Midland', 'TX', 'Texas', 'Permian Basin of West Texas'),
    ('plasma-donation-odessa-tx-2026', 'Odessa', 'TX', 'Texas', 'Permian Basin of West Texas'),
    ('plasma-donation-beaumont-tx-2026', 'Beaumont', 'TX', 'Texas', 'Southeast Texas near the Louisiana border'),
    ('plasma-donation-abilene-tx-2026', 'Abilene', 'TX', 'Texas', 'West-Central Texas'),
    ('plasma-donation-round-rock-tx-2026', 'Round Rock', 'TX', 'Texas', 'Austin metro area in Central Texas'),
    ('plasma-donation-denton-tx-2026', 'Denton', 'TX', 'Texas', 'North Texas, home to UNT and TWU'),
    ('plasma-donation-tyler-tx-2026', 'Tyler', 'TX', 'Texas', 'East Texas Piney Woods region'),
    ('plasma-donation-brownsville-tx-2026', 'Brownsville', 'TX', 'Texas', 'Rio Grande Valley at the southern tip of Texas'),
    ('plasma-donation-mcallen-tx-2026', 'McAllen', 'TX', 'Texas', 'Rio Grande Valley in South Texas'),

    # --- Florida (11) ---
    ('plasma-donation-pembroke-pines-fl-2026', 'Pembroke Pines', 'FL', 'Florida', 'Broward County in the Miami metro area'),
    ('plasma-donation-cape-coral-fl-2026', 'Cape Coral', 'FL', 'Florida', 'Southwest Florida on the Gulf Coast'),
    ('plasma-donation-port-st-lucie-fl-2026', 'Port St Lucie', 'FL', 'Florida', 'Treasure Coast of Southeast Florida'),
    ('plasma-donation-lakeland-fl-2026', 'Lakeland', 'FL', 'Florida', 'Central Florida between Tampa and Orlando'),
    ('plasma-donation-clearwater-fl-2026', 'Clearwater', 'FL', 'Florida', 'Tampa Bay area on the Gulf Coast'),
    ('plasma-donation-kissimmee-fl-2026', 'Kissimmee', 'FL', 'Florida', 'Osceola County in the greater Orlando area'),
    ('plasma-donation-ocala-fl-2026', 'Ocala', 'FL', 'Florida', 'North-Central Florida'),
    ('plasma-donation-daytona-beach-fl-2026', 'Daytona Beach', 'FL', 'Florida', 'East-Central Florida on the Atlantic Coast'),
    ('plasma-donation-melbourne-fl-2026', 'Melbourne', 'FL', 'Florida', 'Brevard County on Florida\'s Space Coast'),
    ('plasma-donation-pensacola-fl-2026', 'Pensacola', 'FL', 'Florida', 'Northwest Florida Panhandle on the Gulf Coast'),
    ('plasma-donation-palm-bay-fl-2026', 'Palm Bay', 'FL', 'Florida', 'Brevard County on Florida\'s Space Coast'),

    # --- Southeast (13) ---
    ('plasma-donation-macon-ga-2026', 'Macon', 'GA', 'Georgia', 'Central Georgia'),
    ('plasma-donation-valdosta-ga-2026', 'Valdosta', 'GA', 'Georgia', 'South Georgia near the Florida border'),
    ('plasma-donation-warner-robins-ga-2026', 'Warner Robins', 'GA', 'Georgia', 'Central Georgia near Robins Air Force Base'),
    ('plasma-donation-murfreesboro-tn-2026', 'Murfreesboro', 'TN', 'Tennessee', 'Middle Tennessee in the Nashville metro area'),
    ('plasma-donation-jackson-tn-2026', 'Jackson', 'TN', 'Tennessee', 'West Tennessee between Nashville and Memphis'),
    ('plasma-donation-wilmington-nc-2026', 'Wilmington', 'NC', 'North Carolina', 'Southeastern North Carolina on the Cape Fear Coast'),
    ('plasma-donation-high-point-nc-2026', 'High Point', 'NC', 'North Carolina', 'Piedmont Triad of Central North Carolina'),
    ('plasma-donation-asheville-nc-2026', 'Asheville', 'NC', 'North Carolina', 'Western North Carolina in the Blue Ridge Mountains'),
    ('plasma-donation-gastonia-nc-2026', 'Gastonia', 'NC', 'North Carolina', 'Gaston County west of Charlotte'),
    ('plasma-donation-chesapeake-va-2026', 'Chesapeake', 'VA', 'Virginia', 'Hampton Roads region of Southeastern Virginia'),
    ('plasma-donation-hampton-va-2026', 'Hampton', 'VA', 'Virginia', 'Hampton Roads region on the Virginia Peninsula'),
    ('plasma-donation-roanoke-va-2026', 'Roanoke', 'VA', 'Virginia', 'Roanoke Valley in the Blue Ridge Mountains of Western Virginia'),
    ('plasma-donation-lynchburg-va-2026', 'Lynchburg', 'VA', 'Virginia', 'Central Virginia in the foothills of the Blue Ridge Mountains'),

    # --- Midwest (18) ---
    ('plasma-donation-aurora-il-2026', 'Aurora', 'IL', 'Illinois', 'Fox Valley area west of Chicago'),
    ('plasma-donation-rockford-il-2026', 'Rockford', 'IL', 'Illinois', 'Northern Illinois near the Wisconsin border'),
    ('plasma-donation-joliet-il-2026', 'Joliet', 'IL', 'Illinois', 'Will County southwest of Chicago'),
    ('plasma-donation-naperville-il-2026', 'Naperville', 'IL', 'Illinois', 'DuPage County in the western Chicago suburbs'),
    ('plasma-donation-flint-mi-2026', 'Flint', 'MI', 'Michigan', 'Genesee County in Mid-Michigan'),
    ('plasma-donation-kalamazoo-mi-2026', 'Kalamazoo', 'MI', 'Michigan', 'Southwest Michigan'),
    ('plasma-donation-warren-mi-2026', 'Warren', 'MI', 'Michigan', 'Macomb County in the northern Detroit metro area'),
    ('plasma-donation-saginaw-mi-2026', 'Saginaw', 'MI', 'Michigan', 'Saginaw Valley in Mid-Michigan'),
    ('plasma-donation-overland-park-ks-2026', 'Overland Park', 'KS', 'Kansas', 'Johnson County in the Kansas City metro area'),
    ('plasma-donation-olathe-ks-2026', 'Olathe', 'KS', 'Kansas', 'Johnson County in the Kansas City metro area'),
    ('plasma-donation-rochester-mn-2026', 'Rochester', 'MN', 'Minnesota', 'Southeastern Minnesota, home of the Mayo Clinic'),
    ('plasma-donation-duluth-mn-2026', 'Duluth', 'MN', 'Minnesota', 'Northeastern Minnesota on Lake Superior'),
    ('plasma-donation-youngstown-oh-2026', 'Youngstown', 'OH', 'Ohio', 'Mahoning Valley in Northeastern Ohio'),
    ('plasma-donation-canton-oh-2026', 'Canton', 'OH', 'Ohio', 'Stark County in Northeast Ohio'),
    ('plasma-donation-south-bend-in-2026', 'South Bend', 'IN', 'Indiana', 'Northern Indiana, home of the University of Notre Dame'),
    ('plasma-donation-muncie-in-2026', 'Muncie', 'IN', 'Indiana', 'East-Central Indiana, home of Ball State University'),
    ('plasma-donation-terre-haute-in-2026', 'Terre Haute', 'IN', 'Indiana', 'Western Indiana on the Wabash River near the Illinois border'),

    # --- Mountain / West (11) ---
    ('plasma-donation-pueblo-co-2026', 'Pueblo', 'CO', 'Colorado', 'Southern Colorado along the Arkansas River'),
    ('plasma-donation-greeley-co-2026', 'Greeley', 'CO', 'Colorado', 'Weld County in Northern Colorado'),
    ('plasma-donation-lakewood-co-2026', 'Lakewood', 'CO', 'Colorado', 'Jefferson County in the Denver metro area'),
    ('plasma-donation-ogden-ut-2026', 'Ogden', 'UT', 'Utah', 'Weber County in Northern Utah along the Wasatch Front'),
    ('plasma-donation-layton-ut-2026', 'Layton', 'UT', 'Utah', 'Davis County between Salt Lake City and Ogden'),
    ('plasma-donation-orem-ut-2026', 'Orem', 'UT', 'Utah', 'Utah County in the Provo-Orem metro area'),
    ('plasma-donation-bend-or-2026', 'Bend', 'OR', 'Oregon', 'Central Oregon east of the Cascade Range'),
    ('plasma-donation-medford-or-2026', 'Medford', 'OR', 'Oregon', 'Rogue Valley of Southern Oregon'),
    ('plasma-donation-kent-wa-2026', 'Kent', 'WA', 'Washington', 'South King County in the Seattle metro area'),
    ('plasma-donation-bellevue-wa-2026', 'Bellevue', 'WA', 'Washington', 'East side of the Seattle metro area'),
    ('plasma-donation-everett-wa-2026', 'Everett', 'WA', 'Washington', 'Snohomish County north of Seattle'),
    ('plasma-donation-yakima-wa-2026', 'Yakima', 'WA', 'Washington', 'Yakima Valley in Central Washington'),
]

if __name__ == '__main__':
    print(f"Generating Round 3 City Pages ({len(en_cities)} cities)...")

    # Safety check: verify no duplicates in our list
    slugs = [c[0] for c in en_cities]
    if len(slugs) != len(set(slugs)):
        print("ERROR: Duplicate slugs found!")
        from collections import Counter
        dupes = [s for s, cnt in Counter(slugs).items() if cnt > 1]
        for d in dupes:
            print(f"  DUPLICATE: {d}")
        sys.exit(1)

    # Safety check: verify none of these files already exist
    existing = []
    for slug, *_ in en_cities:
        path = os.path.join(BLOG_DIR, f"{slug}.html")
        if os.path.exists(path):
            existing.append(slug)
    if existing:
        print(f"WARNING: {len(existing)} files already exist (will be overwritten):")
        for e in existing:
            print(f"  {e}")

    count = 0
    for slug, city, state_abbr, state_full, region in en_cities:
        html = gen_en_city(slug, city, state_abbr, state_full, region)
        path = os.path.join(BLOG_DIR, f"{slug}.html")
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"  Created: blog/{slug}.html")
        count += 1

    print(f"\nDone! Generated {count} new English city pages.")
