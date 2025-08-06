#!/usr/bin/env python3
"""
Selectively remove only the specific deleted files from sitemap
"""

import re

# Only remove URLs for files we actually deleted (exact matches)
exact_deleted_files = [
    'plasma-donation-requirements-2025.html',
    'csl-biolife-octapharma-comparison-guide.html', 
    'first-time-plasma-donation-bonus.html',
    'california-cities.html',
    'plasma-donation-complete-beginners-guide.html',
    'plasma-donation-side-effects-safety-guide.html'
]

# Remove directory URLs that we deleted
deleted_directories = [
    'centers/',
    'health/'
]

# Read the current sitemap
with open('/Users/glengomezmeade/Projects/plasma-pay-calculator/sitemap.xml', 'r') as f:
    content = f.read()

original_url_count = content.count('<url>')

# Remove only exact file matches
for filename in exact_deleted_files:
    pattern = rf'  <url>\s*<loc>https://plasmapaycalculator\.com/{re.escape(filename)}.*?</url>\n'
    content = re.sub(pattern, '', content, flags=re.DOTALL)

# Remove directory URLs  
for directory in deleted_directories:
    pattern = rf'  <url>\s*<loc>https://plasmapaycalculator\.com/{re.escape(directory)}.*?</url>\n'
    content = re.sub(pattern, '', content, flags=re.DOTALL)

# Write the cleaned sitemap
with open('/Users/glengomezmeade/Projects/plasma-pay-calculator/sitemap.xml', 'w') as f:
    f.write(content)

final_url_count = content.count('<url>')
removed_count = original_url_count - final_url_count

print(f"Sitemap cleaned: {removed_count} URLs removed")
print(f"Original: {original_url_count} URLs → Final: {final_url_count} URLs")