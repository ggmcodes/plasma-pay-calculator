#!/usr/bin/env python3
import os
import re
from pathlib import Path

blog_dir = Path('/Users/glengomezmeade/Projects/plasma-pay-calculator/blog')
files_with_true_empties = {}

for html_file in blog_dir.glob('*.html'):
    with open(html_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    empty_sections = []
    for i in range(len(lines) - 2):
        # Check for pattern: h2 header, then div opening, then immediate div closing
        if '<h2' in lines[i] and '</h2>' in lines[i]:
            if 'bg-white rounded-xl shadow-md p-6">' in lines[i+1]:
                # Check if next line is just whitespace and closing div
                if lines[i+2].strip() == '</div>':
                    # Extract the title
                    title = re.sub(r'<[^>]+>', '', lines[i]).strip()
                    empty_sections.append({
                        'title': title,
                        'line': i+1
                    })
    
    if empty_sections:
        files_with_true_empties[html_file.name] = empty_sections

print(f"=== TRULY EMPTY SECTIONS ===\n")
print(f"Files with truly empty sections: {len(files_with_true_empties)}")
print(f"Total empty sections: {sum(len(sections) for sections in files_with_true_empties.values())}\n")

# List files that need fixing
priority_files = ['biolife-plasma-pay-chart-2025.html', 'csl-plasma-pay-chart-2025-complete-rates-guide.html', 
                  'kedplasma-pay-chart-2025.html', 'octapharma-vs-competitors-payment-calculator.html',
                  'which-plasma-center-pays-most-money.html', 'biolife-vs-csl-plasma-comparison.html']

print("Priority files to fix:")
for filename in priority_files:
    if filename in files_with_true_empties:
        print(f"\n{filename}:")
        for section in files_with_true_empties[filename]:
            print(f"  - Line {section['line']}: {section['title']}")

print("\n\nAll files with empty sections:")
for filename, sections in list(files_with_true_empties.items())[:10]:
    print(f"\n{filename}:")
    for section in sections:
        print(f"  - {section['title']}")