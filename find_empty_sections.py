#!/usr/bin/env python3
import os
import re
from pathlib import Path
from collections import Counter

blog_dir = Path('/Users/glengomezmeade/Projects/plasma-pay-calculator/blog')
empty_section_titles = []
files_with_empties = {}

for html_file in blog_dir.glob('*.html'):
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find empty sections with their titles
    pattern = r'<h2[^>]*>(.*?)</h2>\s*<div class="bg-white rounded-xl shadow-md p-6">\s*\n\s*</div>'
    matches = re.findall(pattern, content, re.DOTALL)
    
    if matches:
        for match in matches:
            # Clean up the title
            title = re.sub(r'<[^>]+>', '', match).strip()
            empty_section_titles.append(title)
            
            if html_file.name not in files_with_empties:
                files_with_empties[html_file.name] = []
            files_with_empties[html_file.name].append(title)

# Count most common empty sections
title_counts = Counter(empty_section_titles)

print("=== EMPTY SECTION ANALYSIS ===\n")
print(f"Total empty sections found: {len(empty_section_titles)}")
print(f"Files with empty sections: {len(files_with_empties)}\n")

print("Most common empty sections:")
for title, count in title_counts.most_common(10):
    print(f"  - '{title}': {count} occurrences")

print("\n\nSample files with empty sections:")
for i, (filename, sections) in enumerate(list(files_with_empties.items())[:5]):
    print(f"\n{filename}:")
    for section in sections:
        print(f"  - {section}")