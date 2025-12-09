#!/usr/bin/env python3
"""
Remove the "Nearby States" sections that were just added.
Keep focus on local geographic intent - cities within same state only.
"""

import re
from pathlib import Path

def remove_nearby_states_section(file_path):
    """Remove 'Nearby States' section from a state page"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Remove the Nearby States section
        pattern = r'\n        <!-- Nearby States Section -->[\s\S]*?        </section>\n'
        content = re.sub(pattern, '\n', content)

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
    print("Removing 'Nearby States' sections to maintain local geographic focus...\n")

    # Process all state pages
    calculators_dir = Path('calculators')
    state_pages = []

    for state_dir in calculators_dir.iterdir():
        if state_dir.is_dir():
            state_index = state_dir / 'index.html'
            if state_index.exists():
                state_pages.append((state_index, state_dir.name))

    print(f"Found {len(state_pages)} state pages")

    # Remove nearby states sections
    updated_count = 0
    for state_page, state_slug in state_pages:
        if remove_nearby_states_section(state_page):
            updated_count += 1
            print(f"  ✓ Removed nearby states from {state_slug}")

    print(f"\nRemoved nearby states sections from {updated_count}/{len(state_pages)} state pages")
    print("\nFocus: Keeping users within their local geographic area")
    print("- State pages → Link to cities within that state")
    print("- City pages → Link to other cities in same state")

if __name__ == '__main__':
    main()
