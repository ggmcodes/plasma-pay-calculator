#!/usr/bin/env python3
"""
Clean sitemap by removing URLs for deleted content
"""

import re

# URLs to remove (content we deleted)
removed_urls = [
    'plasma-donation-requirements-2025',
    'centers/',
    'csl-biolife-octapharma-comparison',
    'first-time-plasma-donation-bonus',
    'california-cities',
    'health/'
]

# Read the current sitemap
with open('/Users/glengomezmeade/Projects/plasma-pay-calculator/sitemap.xml', 'r') as f:
    content = f.read()

# Remove URL blocks for deleted content
for url in removed_urls:
    # Remove the entire URL block (url tag and its contents)
    pattern = rf'  <url>.*?{re.escape(url)}.*?</url>\n'
    content = re.sub(pattern, '', content, flags=re.DOTALL)

# Write the cleaned sitemap
with open('/Users/glengomezmeade/Projects/plasma-pay-calculator/sitemap.xml', 'w') as f:
    f.write(content)

print("Sitemap cleaned successfully!")