#!/usr/bin/env python3
"""
Rebuild sitemap with conservative, guaranteed-valid values
"""

import os
import re
from datetime import datetime
from pathlib import Path

def rebuild_sitemap_conservative():
    """Rebuild sitemap with only the most common, safe values"""
    
    base_dir = "/Users/glengomezmeade/Projects/plasma-pay-calculator"
    sitemap_path = os.path.join(base_dir, "sitemap.xml")
    
    # Read current sitemap to get all URLs
    with open(sitemap_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract all URL entries
    url_pattern = r'<url>.*?</url>'
    urls = re.findall(url_pattern, content, re.DOTALL)
    
    # Start new sitemap
    new_sitemap = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
'''
    
    for url_block in urls:
        # Extract components
        loc_match = re.search(r'<loc>(.*?)</loc>', url_block)
        if not loc_match:
            continue
        
        loc = loc_match.group(1)
        
        # Determine priority and changefreq based on URL patterns
        if loc.endswith('/'):
            if 'blog/' in loc:
                priority = '0.8'
                changefreq = 'weekly'
            elif 'metro/' in loc or 'centers/' in loc:
                priority = '0.8'
                changefreq = 'weekly'
            elif 'calculators/' in loc:
                if loc.count('/') > 4:  # City pages
                    priority = '0.7'
                    changefreq = 'monthly'
                else:  # State pages
                    priority = '0.8'
                    changefreq = 'monthly'
            else:
                priority = '0.9'
                changefreq = 'weekly'
        else:
            # HTML files
            if 'blog/' in loc:
                priority = '0.6'
                changefreq = 'monthly'
            elif 'tools/' in loc:
                priority = '0.9'
                changefreq = 'weekly'
            elif 'seasonal/' in loc:
                priority = '0.7'
                changefreq = 'monthly'
            elif loc == 'https://plasmapaycalculator.com/index.html':
                priority = '1.0'
                changefreq = 'daily'
            else:
                priority = '0.5'
                changefreq = 'monthly'
        
        # Build clean URL entry with only core elements
        new_sitemap += f'''  <url>
    <loc>{loc}</loc>
    <lastmod>2025-01-20</lastmod>
    <changefreq>{changefreq}</changefreq>
    <priority>{priority}</priority>
  </url>
'''
    
    new_sitemap += '</urlset>'
    
    # Write new sitemap
    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write(new_sitemap)
    
    print("✅ Rebuilt sitemap with conservative values")
    
    # Count URLs
    url_count = len(urls)
    print(f"📊 Total URLs: {url_count}")
    
    return True

def validate_new_sitemap():
    """Validate the rebuilt sitemap"""
    
    sitemap_path = "/Users/glengomezmeade/Projects/plasma-pay-calculator/sitemap.xml"
    
    with open(sitemap_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for valid changefreq values
    changefreq_values = re.findall(r'<changefreq>([^<]+)</changefreq>', content)
    unique_values = set(changefreq_values)
    
    print(f"📋 Changefreq values used: {unique_values}")
    
    # Check for valid priority values
    priority_values = re.findall(r'<priority>([^<]+)</priority>', content)
    invalid_priorities = [p for p in priority_values if not (0.0 <= float(p) <= 1.0)]
    
    if invalid_priorities:
        print(f"❌ Invalid priorities found: {invalid_priorities}")
        return False
    
    print("✅ All priorities are valid (0.0-1.0)")
    
    # Check structure
    if content.count('<url>') == content.count('</url>'):
        print("✅ URL tags are balanced")
    else:
        print("❌ URL tags are not balanced")
        return False
    
    return True

def main():
    """Main function"""
    print("🔧 Rebuilding sitemap with conservative, guaranteed-valid values...")
    
    if rebuild_sitemap_conservative():
        print("\n🔍 Validating rebuilt sitemap...")
        if validate_new_sitemap():
            print("\n✅ Sitemap successfully rebuilt and validated!")
        else:
            print("\n❌ Validation failed")

if __name__ == "__main__":
    main()