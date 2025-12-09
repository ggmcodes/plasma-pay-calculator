#!/usr/bin/env python3
"""
Fix borough pages:
1. Make borough neighborhoods clickable links
2. Remove \n\n text before FAQ section
"""

import re
from pathlib import Path

# Map of borough names to their URL paths
BOROUGH_LINKS = {
    'Manhattan': '/calculators/new-york/manhattan/',
    'Brooklyn': '/calculators/new-york/brooklyn/',
    'Queens': '/calculators/new-york/queens/',
    'Bronx': '/calculators/new-york/bronx/',
    'Staten Island': '/calculators/new-york/staten-island/'
}

def fix_borough_page(file_path):
    """Fix a single borough page"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # 1. Remove the literal \n\n text before FAQ section
        content = content.replace('    \\n\\n                <!-- FAQ Section -->', '                <!-- FAQ Section -->')

        # 2. Convert each borough neighborhood card to a clickable link
        # Pattern for non-linkable borough cards
        for borough_name, borough_url in BOROUGH_LINKS.items():
            # Skip if it's the current page (don't link to itself)
            if borough_name.lower().replace(' ', '-') in str(file_path):
                continue

            # Pattern: <div class="bg-gray-50 rounded-lg p-6">
            #              <h3 class="text-lg font-semibold text-gray-900 mb-2">Manhattan</h3>
            pattern = rf'(<div class="bg-gray-50 rounded-lg p-6">)\s*<h3 class="text-lg font-semibold text-gray-900 mb-2">{borough_name}</h3>'

            # Replacement: <a href="/calculators/new-york/manhattan/" class="bg-gray-50 rounded-lg p-6 block hover:bg-gray-100 transition-colors">
            #                  <h3 class="text-lg font-semibold text-gray-900 mb-2">Manhattan</h3>
            replacement = rf'<a href="{borough_url}" class="bg-gray-50 rounded-lg p-6 block hover:bg-gray-100 transition-colors">\n        <h3 class="text-lg font-semibold text-gray-900 mb-2">{borough_name}</h3>'

            content = re.sub(pattern, replacement, content)

        # Also need to change closing </div> to </a> for borough cards
        # This is tricky - we need to be careful to only change the borough card divs
        # Let's do a more targeted approach - find each borough section and replace its closing tag
        for borough_name, borough_url in BOROUGH_LINKS.items():
            if borough_name.lower().replace(' ', '-') in str(file_path):
                continue

            # Find the borough card and replace its closing </div> with </a>
            # Pattern: starts with <a href="[borough_url]" and ends with </div> after the borough content
            pattern = rf'(<a href="{borough_url}"[^>]*>[\s\S]*?<h3[^>]*>{borough_name}</h3>[\s\S]*?</div>\s*)</div>'
            replacement = rf'\1</a>'
            content = re.sub(pattern, replacement, content)

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
    borough_pages = [
        Path('calculators/new-york/manhattan/index.html'),
        Path('calculators/new-york/brooklyn/index.html'),
        Path('calculators/new-york/queens/index.html'),
        Path('calculators/new-york/bronx/index.html'),
        Path('calculators/new-york/staten-island/index.html')
    ]

    print("Fixing borough pages...")
    updated_count = 0
    for page in borough_pages:
        if page.exists():
            if fix_borough_page(page):
                updated_count += 1
                print(f"✓ Fixed {page}")
        else:
            print(f"✗ Not found: {page}")

    print(f"\nComplete! Updated {updated_count} borough pages")

if __name__ == '__main__':
    main()
