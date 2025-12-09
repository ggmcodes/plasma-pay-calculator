#!/usr/bin/env python3
"""
Generate comprehensive redirect rules for all calculator pages.
Prevents redirect chains by creating direct redirects for all URL variants.
"""

from pathlib import Path

def get_all_calculators(lang='en'):
    """Get all calculator pages (state and city)"""
    base_dir = Path('calculators') if lang == 'en' else Path('es/calculators')

    states = []
    cities = []

    for state_dir in sorted(base_dir.iterdir()):
        if state_dir.is_dir():
            state_slug = state_dir.name
            states.append(state_slug)

            # Get cities for this state
            for city_dir in sorted(state_dir.iterdir()):
                if city_dir.is_dir() and (city_dir / 'index.html').exists():
                    city_slug = city_dir.name
                    cities.append((state_slug, city_slug))

    return states, cities

def generate_state_redirects(state_slug, lang='en'):
    """Generate 4 redirect variants for a state page"""
    if lang == 'en':
        target = f'/calculators/{state_slug}'
        return [
            f'/state/{state_slug}.html {target} 301',
            f'/state/{state_slug} {target} 301',
            f'/calculators/{state_slug}.html {target} 301',
            f'/calculators/{state_slug}/ {target} 301',
        ]
    else:  # Spanish
        target = f'/es/calculators/{state_slug}'
        return [
            f'/es/estado/{state_slug}.html {target} 301',
            f'/es/estado/{state_slug} {target} 301',
            f'/es/calculators/{state_slug}.html {target} 301',
            f'/es/calculators/{state_slug}/ {target} 301',
        ]

def generate_city_redirects(state_slug, city_slug, lang='en'):
    """Generate 4 redirect variants for a city page"""
    if lang == 'en':
        target = f'/calculators/{state_slug}/{city_slug}'
        return [
            f'/state/{state_slug}/{city_slug}.html {target} 301',
            f'/state/{state_slug}/{city_slug} {target} 301',
            f'/calculators/{state_slug}/{city_slug}.html {target} 301',
            f'/calculators/{state_slug}/{city_slug}/ {target} 301',
        ]
    else:  # Spanish
        target = f'/es/calculators/{state_slug}/{city_slug}'
        return [
            f'/es/estado/{state_slug}/{city_slug}.html {target} 301',
            f'/es/estado/{state_slug}/{city_slug} {target} 301',
            f'/es/calculators/{state_slug}/{city_slug}.html {target} 301',
            f'/es/calculators/{state_slug}/{city_slug}/ {target} 301',
        ]

def main():
    print("=== GENERATING CALCULATOR REDIRECT RULES ===\n")

    all_redirects = []

    # English redirects
    print("Scanning English calculator pages...")
    all_redirects.append("# ===============================================")
    all_redirects.append("# SPECIFIC CALCULATOR REDIRECTS")
    all_redirects.append("# Generated to prevent redirect chains")
    all_redirects.append("# ===============================================")
    all_redirects.append("")
    all_redirects.append("## English State Pages")

    states_en, cities_en = get_all_calculators('en')
    for state in states_en:
        all_redirects.extend(generate_state_redirects(state, 'en'))

    all_redirects.append("")
    all_redirects.append("## English City Pages")
    for state, city in cities_en:
        all_redirects.extend(generate_city_redirects(state, city, 'en'))

    # Spanish redirects
    print("Scanning Spanish calculator pages...")
    all_redirects.append("")
    all_redirects.append("## Spanish State Pages")

    states_es, cities_es = get_all_calculators('es')
    for state in states_es:
        all_redirects.extend(generate_state_redirects(state, 'es'))

    all_redirects.append("")
    all_redirects.append("## Spanish City Pages")
    for state, city in cities_es:
        all_redirects.extend(generate_city_redirects(state, city, 'es'))

    # Write to file
    output_file = 'calculator_redirects.txt'
    with open(output_file, 'w') as f:
        f.write('\n'.join(all_redirects))

    print(f"\n=== COMPLETE ===")
    print(f"✓ Generated {len([r for r in all_redirects if r and not r.startswith('#')])} redirect rules")
    print(f"✓ Saved to {output_file}\n")
    print(f"English pages:")
    print(f"  • {len(states_en)} states × 4 variants = {len(states_en) * 4} redirects")
    print(f"  • {len(cities_en)} cities × 4 variants = {len(cities_en) * 4} redirects")
    print(f"\nSpanish pages:")
    print(f"  • {len(states_es)} states × 4 variants = {len(states_es) * 4} redirects")
    print(f"  • {len(cities_es)} cities × 4 variants = {len(cities_es) * 4} redirects")
    print(f"\nTotal: {(len(states_en) + len(cities_en) + len(states_es) + len(cities_es)) * 4} redirect rules")
    print(f"\nNext step: Insert these rules into _redirects file after line 20")

if __name__ == '__main__':
    main()
