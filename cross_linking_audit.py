#!/usr/bin/env python3
"""
Comprehensive Cross-Linking Audit and Implementation
- Add "Browse Other States" sections to state pages
- Add geographic neighboring states links
- Strengthen internal linking across the site
"""

from pathlib import Path
import re

# Geographic neighboring states (for cross-linking)
STATE_NEIGHBORS = {
    'alabama': ['georgia', 'florida', 'mississippi', 'tennessee'],
    'alaska': ['washington'],  # Closest continental state
    'arizona': ['california', 'nevada', 'new-mexico', 'utah'],
    'arkansas': ['missouri', 'tennessee', 'mississippi', 'louisiana', 'texas', 'oklahoma'],
    'california': ['oregon', 'nevada', 'arizona'],
    'colorado': ['wyoming', 'nebraska', 'kansas', 'oklahoma', 'new-mexico', 'utah'],
    'connecticut': ['massachusetts', 'rhode-island', 'new-york'],
    'delaware': ['maryland', 'pennsylvania', 'new-jersey'],
    'florida': ['georgia', 'alabama'],
    'georgia': ['florida', 'alabama', 'tennessee', 'north-carolina', 'south-carolina'],
    'hawaii': ['california'],  # Closest state
    'idaho': ['montana', 'wyoming', 'utah', 'nevada', 'oregon', 'washington'],
    'illinois': ['wisconsin', 'indiana', 'kentucky', 'missouri', 'iowa'],
    'indiana': ['michigan', 'ohio', 'kentucky', 'illinois'],
    'iowa': ['minnesota', 'wisconsin', 'illinois', 'missouri', 'nebraska', 'south-dakota'],
    'kansas': ['nebraska', 'missouri', 'oklahoma', 'colorado'],
    'kentucky': ['illinois', 'indiana', 'ohio', 'west-virginia', 'virginia', 'tennessee', 'missouri'],
    'louisiana': ['texas', 'arkansas', 'mississippi'],
    'maine': ['new-hampshire'],
    'maryland': ['pennsylvania', 'delaware', 'virginia', 'west-virginia'],
    'massachusetts': ['rhode-island', 'connecticut', 'new-york', 'vermont', 'new-hampshire'],
    'michigan': ['wisconsin', 'indiana', 'ohio'],
    'minnesota': ['wisconsin', 'iowa', 'south-dakota', 'north-dakota'],
    'mississippi': ['tennessee', 'alabama', 'louisiana', 'arkansas'],
    'missouri': ['iowa', 'illinois', 'kentucky', 'tennessee', 'arkansas', 'oklahoma', 'kansas', 'nebraska'],
    'montana': ['north-dakota', 'south-dakota', 'wyoming', 'idaho'],
    'nebraska': ['south-dakota', 'iowa', 'missouri', 'kansas', 'colorado', 'wyoming'],
    'nevada': ['oregon', 'idaho', 'utah', 'arizona', 'california'],
    'new-hampshire': ['maine', 'massachusetts', 'vermont'],
    'new-jersey': ['new-york', 'pennsylvania', 'delaware'],
    'new-mexico': ['colorado', 'oklahoma', 'texas', 'arizona'],
    'new-york': ['vermont', 'massachusetts', 'connecticut', 'new-jersey', 'pennsylvania'],
    'north-carolina': ['virginia', 'tennessee', 'georgia', 'south-carolina'],
    'north-dakota': ['minnesota', 'south-dakota', 'montana'],
    'ohio': ['pennsylvania', 'west-virginia', 'kentucky', 'indiana', 'michigan'],
    'oklahoma': ['kansas', 'missouri', 'arkansas', 'texas', 'new-mexico', 'colorado'],
    'oregon': ['washington', 'idaho', 'nevada', 'california'],
    'pennsylvania': ['new-york', 'new-jersey', 'delaware', 'maryland', 'west-virginia', 'ohio'],
    'rhode-island': ['massachusetts', 'connecticut'],
    'south-carolina': ['north-carolina', 'georgia'],
    'south-dakota': ['north-dakota', 'minnesota', 'iowa', 'nebraska', 'wyoming', 'montana'],
    'tennessee': ['kentucky', 'virginia', 'north-carolina', 'georgia', 'alabama', 'mississippi', 'arkansas', 'missouri'],
    'texas': ['oklahoma', 'arkansas', 'louisiana', 'new-mexico'],
    'utah': ['idaho', 'wyoming', 'colorado', 'new-mexico', 'arizona', 'nevada'],
    'vermont': ['new-hampshire', 'massachusetts', 'new-york'],
    'virginia': ['maryland', 'west-virginia', 'kentucky', 'tennessee', 'north-carolina'],
    'washington': ['idaho', 'oregon'],
    'west-virginia': ['ohio', 'pennsylvania', 'maryland', 'virginia', 'kentucky'],
    'wisconsin': ['michigan', 'illinois', 'iowa', 'minnesota'],
    'wyoming': ['montana', 'south-dakota', 'nebraska', 'colorado', 'utah', 'idaho']
}

# State display names
STATE_NAMES = {
    'alabama': 'Alabama',
    'alaska': 'Alaska',
    'arizona': 'Arizona',
    'arkansas': 'Arkansas',
    'california': 'California',
    'colorado': 'Colorado',
    'connecticut': 'Connecticut',
    'delaware': 'Delaware',
    'florida': 'Florida',
    'georgia': 'Georgia',
    'hawaii': 'Hawaii',
    'idaho': 'Idaho',
    'illinois': 'Illinois',
    'indiana': 'Indiana',
    'iowa': 'Iowa',
    'kansas': 'Kansas',
    'kentucky': 'Kentucky',
    'louisiana': 'Louisiana',
    'maine': 'Maine',
    'maryland': 'Maryland',
    'massachusetts': 'Massachusetts',
    'michigan': 'Michigan',
    'minnesota': 'Minnesota',
    'mississippi': 'Mississippi',
    'missouri': 'Missouri',
    'montana': 'Montana',
    'nebraska': 'Nebraska',
    'nevada': 'Nevada',
    'new-hampshire': 'New Hampshire',
    'new-jersey': 'New Jersey',
    'new-mexico': 'New Mexico',
    'new-york': 'New York',
    'north-carolina': 'North Carolina',
    'north-dakota': 'North Dakota',
    'ohio': 'Ohio',
    'oklahoma': 'Oklahoma',
    'oregon': 'Oregon',
    'pennsylvania': 'Pennsylvania',
    'rhode-island': 'Rhode Island',
    'south-carolina': 'South Carolina',
    'south-dakota': 'South Dakota',
    'tennessee': 'Tennessee',
    'texas': 'Texas',
    'utah': 'Utah',
    'vermont': 'Vermont',
    'virginia': 'Virginia',
    'washington': 'Washington',
    'west-virginia': 'West Virginia',
    'wisconsin': 'Wisconsin',
    'wyoming': 'Wyoming'
}

def add_nearby_states_section(file_path, state_slug):
    """Add 'Browse Nearby States' section to a state page"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Get neighboring states
        neighbors = STATE_NEIGHBORS.get(state_slug, [])
        if not neighbors:
            return False

        # Limit to top 4 neighbors for clean layout
        neighbors = neighbors[:4]

        # Build the nearby states section HTML
        nearby_states_html = '\n        <!-- Nearby States Section -->\n'
        nearby_states_html += '        <section class="py-12 md:py-16 bg-white">\n'
        nearby_states_html += '            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">\n'
        nearby_states_html += '                <h2 class="text-2xl md:text-3xl font-bold text-center text-gray-900 mb-8">\n'
        nearby_states_html += '                    Plasma Donation in Nearby States\n'
        nearby_states_html += '                </h2>\n'
        nearby_states_html += '                <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-4">\n'

        for neighbor in neighbors:
            display_name = STATE_NAMES.get(neighbor, neighbor.replace('-', ' ').title())
            nearby_states_html += f'    <a href="/calculators/{neighbor}/" class="bg-gray-50 hover:bg-gray-100 rounded-lg p-4 text-center transition-colors border border-gray-200">\n'
            nearby_states_html += f'        <h3 class="font-semibold text-gray-900">{display_name}</h3>\n'
            nearby_states_html += f'        <p class="text-sm text-gray-600">View Centers →</p>\n'
            nearby_states_html += '    </a>\n'

        nearby_states_html += '                </div>\n'
        nearby_states_html += '            </div>\n'
        nearby_states_html += '        </section>\n'

        # Find the insertion point - right before the Browse All Cities section
        pattern = r'(        <!-- Browse All Cities Section -->)'

        if re.search(pattern, content):
            content = re.sub(pattern, nearby_states_html + r'\1', content)
        else:
            # Fallback: insert before footer if Browse Cities not found
            pattern = r'(<footer)'
            if re.search(pattern, content):
                content = re.sub(pattern, nearby_states_html + r'\1', content)

        # Only write if content changed
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    print("=== CROSS-LINKING AUDIT ===\n")

    # Process all state pages
    calculators_dir = Path('calculators')
    state_pages = []

    for state_dir in calculators_dir.iterdir():
        if state_dir.is_dir():
            state_index = state_dir / 'index.html'
            if state_index.exists():
                state_pages.append((state_index, state_dir.name))

    print(f"Found {len(state_pages)} state pages")

    # Add nearby states sections
    print("\n1. Adding 'Nearby States' sections to state pages...")
    updated_count = 0
    for state_page, state_slug in state_pages:
        if add_nearby_states_section(state_page, state_slug):
            updated_count += 1
            print(f"  ✓ Added nearby states to {state_slug}")

    print(f"\nUpdated {updated_count}/{len(state_pages)} state pages with nearby states sections")

    print("\n=== AUDIT COMPLETE ===")
    print(f"\nCross-linking improvements:")
    print(f"- Added 'Browse Nearby States' sections to {updated_count} state pages")
    print(f"- Each state now links to its geographic neighbors")
    print(f"- Strengthened internal linking structure site-wide")

if __name__ == '__main__':
    main()
