#!/usr/bin/env python3
"""Quick verification script"""

from pathlib import Path

STATES = [
    "alabama", "alaska", "arizona", "arkansas", "california", "colorado", "connecticut",
    "delaware", "florida", "georgia", "hawaii", "idaho", "illinois", "indiana", "iowa",
    "kansas", "kentucky", "louisiana", "maine", "maryland", "massachusetts", "michigan",
    "minnesota", "mississippi", "missouri", "montana", "nebraska", "nevada",
    "new-hampshire", "new-jersey", "new-mexico", "new-york", "north-carolina",
    "north-dakota", "ohio", "oklahoma", "oregon", "pennsylvania", "rhode-island",
    "south-carolina", "south-dakota", "tennessee", "texas", "utah", "vermont",
    "virginia", "washington", "west-virginia", "wisconsin", "wyoming"
]

BASE = Path("/Users/glengomezmeade/Projects/plasma-pay-calculator/calculators")

correct = 0
incorrect = []

for state in STATES:
    file_path = BASE / state / "index.html"
    if not file_path.exists():
        incorrect.append(f"{state}: File not found")
        continue

    with open(file_path, 'r') as f:
        content = f.read()

    count = content.count("<!-- Browse Cities Section -->")

    if count == 1:
        correct += 1
    else:
        incorrect.append(f"{state}: {count} occurrences")

print(f"✓ Correct: {correct}/50")
if incorrect:
    print(f"✗ Incorrect: {len(incorrect)}")
    for issue in incorrect:
        print(f"  - {issue}")
else:
    print("✓ All 50 states verified successfully!")
