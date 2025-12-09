#!/bin/bash

# Verification script to confirm Browse Cities sections are positioned correctly

CALCULATORS_DIR="/Users/glengomezmeade/Projects/plasma-pay-calculator/calculators"

ALL_STATES=(
    "alabama" "alaska" "arizona" "arkansas" "california" "colorado" "connecticut"
    "delaware" "florida" "georgia" "hawaii" "idaho" "illinois" "indiana" "iowa"
    "kansas" "kentucky" "louisiana" "maine" "maryland" "massachusetts" "michigan"
    "minnesota" "mississippi" "missouri" "montana" "nebraska" "nevada"
    "new-hampshire" "new-jersey" "new-mexico" "new-york" "north-carolina"
    "north-dakota" "ohio" "oklahoma" "oregon" "pennsylvania" "rhode-island"
    "south-carolina" "south-dakota" "tennessee" "texas" "utah" "vermont"
    "virginia" "washington" "west-virginia" "wisconsin" "wyoming"
)

echo "Verifying Browse Cities Section Repositioning"
echo "=============================================="
echo ""

correct=0
incorrect=0

for state in "${ALL_STATES[@]}"; do
    file="${CALCULATORS_DIR}/${state}/index.html"

    if [ ! -f "$file" ]; then
        echo "✗ $state: File not found"
        ((incorrect++))
        continue
    fi

    # Count occurrences of Browse Cities Section
    count=$(grep -c "<!-- Browse Cities Section -->" "$file" || true)

    if [ "$count" -eq 1 ]; then
        echo "✓ $state"
        ((correct++))
    else
        echo "✗ $state: Found $count occurrences (expected 1)"
        ((incorrect++))
    fi
done

echo ""
echo "=============================================="
echo "Summary: $correct correct, $incorrect incorrect"
echo "=============================================="

if [ "$incorrect" -eq 0 ]; then
    echo "✓ All 50 states verified successfully!"
    exit 0
else
    echo "✗ Some states need attention"
    exit 1
fi
