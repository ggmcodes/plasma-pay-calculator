#!/usr/bin/env python3
"""
Add topic cluster pages to sitemap
"""

import os
import re
from datetime import datetime

def add_topic_clusters_to_sitemap():
    """Add topic cluster pages to sitemap"""
    
    sitemap_path = "/Users/glengomezmeade/Projects/plasma-pay-calculator/sitemap.xml"
    
    # Topic cluster pages to add
    topic_pages = [
        {
            'url': 'https://plasmapaycalculator.com/topics/earning-strategies/',
            'priority': '0.8',
            'changefreq': 'weekly'
        },
        {
            'url': 'https://plasmapaycalculator.com/topics/center-comparisons/',
            'priority': '0.8',
            'changefreq': 'weekly'
        },
        {
            'url': 'https://plasmapaycalculator.com/topics/requirements-eligibility/',
            'priority': '0.8',
            'changefreq': 'weekly'
        },
        {
            'url': 'https://plasmapaycalculator.com/topics/tax-legal/',
            'priority': '0.8',
            'changefreq': 'weekly'
        }
    ]
    
    try:
        with open(sitemap_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check which URLs are already in sitemap
        existing_urls = set(re.findall(r'<loc>(https://[^<]+)</loc>', content))
        new_urls_to_add = [page for page in topic_pages if page['url'] not in existing_urls]
        
        if not new_urls_to_add:
            print("ℹ️ All topic cluster pages already in sitemap")
            return False
        
        # Create new URL entries
        current_date = datetime.now().strftime('%Y-%m-%d')
        new_entries = []
        
        for page in new_urls_to_add:
            new_entry = f'''  <url>
    <loc>{page['url']}</loc>
    <lastmod>{current_date}</lastmod>
    <changefreq>{page['changefreq']}</changefreq>
    <priority>{page['priority']}</priority>
  </url>'''
            new_entries.append(new_entry)
        
        # Insert new entries before closing </urlset> tag
        new_content = content.replace(
            '</urlset>',
            '\n' + '\n\n'.join(new_entries) + '\n\n</urlset>'
        )
        
        # Write updated sitemap
        with open(sitemap_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✅ Added {len(new_urls_to_add)} topic cluster pages to sitemap")
        return True
        
    except Exception as e:
        print(f"❌ Error updating sitemap: {str(e)}")
        return False

def main():
    """Main function"""
    print("📝 Adding topic cluster pages to sitemap...")
    add_topic_clusters_to_sitemap()

if __name__ == "__main__":
    main()