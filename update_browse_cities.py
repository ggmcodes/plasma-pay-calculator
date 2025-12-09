#!/usr/bin/env python3
"""
Script to reposition "Browse Cities" sections on state pages.
Moves the section from footer area to immediately after "{State} Plasma Centers by City" section.
"""

import os
import re
from pathlib import Path

# Define all 50 states (excluding the 3 already done: Alabama, Alaska, West Virginia)
STATES = [
    "arizona", "arkansas", "california", "colorado", "connecticut", "delaware",
    "florida", "georgia", "hawaii", "idaho", "illinois", "indiana", "iowa",
    "kansas", "kentucky", "louisiana", "maine", "maryland", "massachusetts",
    "michigan", "minnesota", "mississippi", "missouri", "montana", "nebraska",
    "nevada", "new-hampshire", "new-jersey", "new-mexico", "new-york",
    "north-carolina", "north-dakota", "ohio", "oklahoma", "oregon",
    "pennsylvania", "rhode-island", "south-carolina", "south-dakota",
    "tennessee", "texas", "utah", "vermont", "virginia", "washington",
    "wisconsin", "wyoming"
]

BASE_DIR = Path("/Users/glengomezmeade/Projects/plasma-pay-calculator/calculators")

def update_state_file(state_name):
    """Update a single state file to reposition Browse Cities section."""
    file_path = BASE_DIR / state_name / "index.html"

    if not file_path.exists():
        print(f"  ⚠️  File not found: {file_path}")
        return False

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find the Browse Cities section
        browse_pattern = r'(    <!-- Browse Cities Section -->.*?</section>)\s*(?:</footer>|<footer)'
        browse_match = re.search(browse_pattern, content, re.DOTALL)

        if not browse_match:
            print(f"  ⚠️  Browse Cities section not found in {state_name}")
            return False

        browse_section = browse_match.group(1)

        # Find the Plasma Centers by City section closing
        state_title = state_name.replace('-', ' ').title().replace('New ', 'New-').replace('North ', 'North-').replace('South ', 'South-').replace('West ', 'West-').replace('Rhode ', 'Rhode-')
        state_title = state_title.replace('-', ' ')

        # Pattern to find where "{State} Plasma Centers by City" section closes
        centers_pattern = rf'(                </div>\s*</div>\s*</section>)\s*(        <!-- .*? Plasma Donation Benefits -->)'

        centers_match = re.search(centers_pattern, content)

        if not centers_match:
            print(f"  ⚠️  Plasma Centers by City section end not found in {state_name}")
            return False

        # Remove Browse Cities from old location (near footer)
        content_without_browse = re.sub(
            r'    <!-- Browse Cities Section -->.*?</section>\s*',
            '',
            content,
            count=1,
            flags=re.DOTALL
        )

        # Insert Browse Cities after Plasma Centers by City section
        content_updated = re.sub(
            centers_pattern,
            r'\1\n\n        ' + browse_section + r'\n\n\2',
            content_without_browse
        )

        # Write back the updated content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content_updated)

        print(f"  ✓ Updated {state_name}")
        return True

    except Exception as e:
        print(f"  ✗ Error updating {state_name}: {e}")
        return False

def main():
    """Main function to update all state files."""
    print("Repositioning Browse Cities sections on state pages...\n")

    success_count = 0
    fail_count = 0

    for state in STATES:
        print(f"Processing {state}...")
        if update_state_file(state):
            success_count += 1
        else:
            fail_count += 1

    print(f"\n{'='*60}")
    print(f"Summary: {success_count} successful, {fail_count} failed")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
