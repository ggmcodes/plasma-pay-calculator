#!/bin/bash

# Script to move Browse Cities sections on remaining state pages
# Usage: ./move_browse_sections.sh

CALCULATORS_DIR="/Users/glengomezmeade/Projects/plasma-pay-calculator/calculators"

# States to process (excluding Alabama, Alaska, West Virginia which are already done)
STATES=(
    "arizona" "arkansas" "california" "colorado" "connecticut" "delaware"
    "florida" "georgia" "hawaii" "idaho" "illinois" "indiana" "iowa"
    "kansas" "kentucky" "louisiana" "maine" "maryland" "massachusetts"
    "michigan" "minnesota" "mississippi" "missouri" "montana" "nebraska"
    "nevada" "new-hampshire" "new-jersey" "new-mexico" "new-york"
    "north-carolina" "north-dakota" "ohio" "oklahoma" "oregon"
    "pennsylvania" "rhode-island" "south-carolina" "south-dakota"
    "tennessee" "texas" "utah" "vermont" "virginia" "washington"
    "wisconsin" "wyoming"
)

process_state() {
    local state=$1
    local file="${CALCULATORS_DIR}/${state}/index.html"

    if [ ! -f "$file" ]; then
        echo "  ⚠️  File not found: $file"
        return 1
    fi

    # Create backup
    cp "$file" "${file}.backup"

    # Use Python for complex regex operations
    python3 << 'PYTHON_SCRIPT' "$file" "$state"
import sys
import re

file_path = sys.argv[1]
state = sys.argv[2]

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract the Browse Cities section from near footer
browse_pattern = r'(    <!-- Browse Cities Section -->.*?    </section>)\s*(?=    </footer>|</footer>|<footer)'
browse_match = re.search(browse_pattern, content, re.DOTALL)

if not browse_match:
    print(f"⚠️  Browse Cities section not found in {state}", file=sys.stderr)
    sys.exit(1)

browse_section = browse_match.group(1)

# Find where to insert (after Plasma Centers by City section closes)
insertion_pattern = r'(                </div>\s*</div>\s*</section>)\s*(        <!-- .* Plasma Donation Benefits -->)'
insertion_match = re.search(insertion_pattern, content)

if not insertion_match:
    print(f"⚠️  Insertion point not found in {state}", file=sys.stderr)
    sys.exit(1)

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

print(f"✓ Updated {state}")
PYTHON_SCRIPT

    if [ $? -eq 0 ]; then
        # Remove backup on success
        rm "${file}.backup"
        return 0
    else
        # Restore backup on failure
        mv "${file}.backup" "$file"
        return 1
    fi
}

echo "Moving Browse Cities sections..."
echo "================================"

success=0
failed=0

for state in "${STATES[@]}"; do
    echo -n "Processing $state..."
    if process_state "$state"; then
        ((success++))
    else
        ((failed++))
    fi
done

echo ""
echo "================================"
echo "Summary: $success successful, $failed failed"
echo "================================"
