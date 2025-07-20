#!/usr/bin/env python3
"""
Add new blog pages to sitemap.xml
"""

import os
import re
from datetime import datetime

def add_new_pages_to_sitemap():
    """Add newly created blog pages to sitemap"""
    
    sitemap_path = "/Users/glengomezmeade/Projects/plasma-pay-calculator/sitemap.xml"
    
    # New pages to add
    new_pages = [
        {
            'url': 'https://plasmapaycalculator.com/blog/how-much-do-you-get-for-donating-plasma-in-iowa.html',
            'priority': '0.8',
            'changefreq': 'weekly'
        },
        {
            'url': 'https://plasmapaycalculator.com/blog/plasma-donation-anchorage-alaska-earnings.html',
            'priority': '0.8',
            'changefreq': 'weekly'
        },
        {
            'url': 'https://plasmapaycalculator.com/blog/plasma-donation-fort-collins-colorado-earnings.html',
            'priority': '0.8',
            'changefreq': 'weekly'
        },
        {
            'url': 'https://plasmapaycalculator.com/blog/make-1200-week-donating-plasma-calculator.html',
            'priority': '0.9',
            'changefreq': 'weekly'
        },
        {
            'url': 'https://plasmapaycalculator.com/blog/plasma-donation-rockville-maryland-earnings.html',
            'priority': '0.8',
            'changefreq': 'weekly'
        }
    ]
    
    try:
        with open(sitemap_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check which URLs are already in sitemap
        existing_urls = set(re.findall(r'<loc>(https://[^<]+)</loc>', content))
        new_urls_to_add = [page for page in new_pages if page['url'] not in existing_urls]
        
        if not new_urls_to_add:
            print("ℹ️ All new pages already in sitemap")
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
        
        print(f"✅ Added {len(new_urls_to_add)} new pages to sitemap")
        for page in new_urls_to_add:
            print(f"   📄 {page['url'].split('/')[-1]}")
        return True
        
    except Exception as e:
        print(f"❌ Error updating sitemap: {str(e)}")
        return False

def main():
    """Main function"""
    print("📄 Adding new blog pages to sitemap...")
    add_new_pages_to_sitemap()

if __name__ == "__main__":
    main()