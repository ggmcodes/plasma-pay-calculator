#!/usr/bin/env python3
"""
Batch update script to reposition Browse Cities sections on state pages.
"""

import re
from pathlib import Path

# List of states to process (excluding already done: Alabama, Alaska, Arizona, West Virginia)
STATES = [
    "arkansas", "california", "colorado", "connecticut", "delaware", "florida",
    "georgia", "hawaii", "idaho", "illinois", "indiana", "iowa", "kansas",
    "kentucky", "louisiana", "maine", "maryland", "massachusetts", "michigan",
    "minnesota", "mississippi", "missouri", "montana", "nebraska", "nevada",
    "new-hampshire", "new-jersey", "new-mexico", "new-york", "north-carolina",
    "north-dakota", "ohio", "oklahoma", "oregon", "pennsylvania", "rhode-island",
    "south-carolina", "south-dakota", "tennessee", "texas", "utah", "vermont",
    "virginia", "washington", "wisconsin", "wyoming"
]

BASE_DIR = Path("/Users/glengomezmeade/Projects/plasma-pay-calculator/calculators")

def update_state(state_name):
    """Update a single state file."""
    file_path = BASE_DIR / state_name / "index.html"

    if not file_path.exists():
        return False, f"File not found: {file_path}"

    try:
        # Read file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find and extract Browse Cities section from footer area
        browse_pattern = r'(    <!-- Browse Cities Section -->.*?    </section>)\s*(?=    </footer>|</footer>)'
        browse_match = re.search(browse_pattern, content, re.DOTALL)

        if not browse_match:
            return False, "Browse Cities section not found"

        browse_section = browse_match.group(1)

        # Find insertion point (after Plasma Centers by City section)
        insertion_pattern = r'(                </div>\s*</div>\s*</section>)\s*(        <!-- .* Plasma Donation Benefits -->)'

        if not re.search(insertion_pattern, content):
            return False, "Insertion point not found"

        # Remove from old location
        content_cleaned = re.sub(browse_pattern + r'\s*', '', content, count=1, flags=re.DOTALL)

        # Insert at new location
        content_updated = re.sub(
            insertion_pattern,
            r'\1\n\n' + browse_section + r'\n\n\2',
            content_cleaned
        )

        # Write updated content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content_updated)

        return True, "Success"

    except Exception as e:
        return False, str(e)

def main():
    """Main function."""
    print("Batch updating Browse Cities sections...")
    print("=" * 60)

    results = []
    for state in STATES:
        success, message = update_state(state)
        status = "✓" if success else "✗"
        results.append((state, success, message))
        print(f"{status} {state:20s} {message}")

    print("=" * 60)
    success_count = sum(1 for _, success, _ in results if success)
    print(f"Summary: {success_count}/{len(STATES)} states updated successfully")

    if success_count < len(STATES):
        print("\nFailed states:")
        for state, success, message in results:
            if not success:
                print(f"  - {state}: {message}")

if __name__ == "__main__":
    main()
