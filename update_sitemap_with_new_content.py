#!/usr/bin/env python3
"""
Update sitemap to include new SEO expansion content
"""

import os
import re
from datetime import datetime

def add_new_pages_to_sitemap():
    """Add new metro, tools, and seasonal pages to sitemap"""
    
    sitemap_path = "/Users/glengomezmeade/Projects/plasma-pay-calculator/sitemap.xml"
    
    # New pages to add
    new_pages = [
        # Metro hub pages
        {
            'url': 'https://plasmapaycalculator.com/metro/new-york-metro/',
            'priority': '0.8',
            'changefreq': 'weekly'
        },
        {
            'url': 'https://plasmapaycalculator.com/metro/los-angeles-metro/',
            'priority': '0.8',
            'changefreq': 'weekly'
        },
        {
            'url': 'https://plasmapaycalculator.com/metro/chicago-metro/',
            'priority': '0.8',
            'changefreq': 'weekly'
        },
        {
            'url': 'https://plasmapaycalculator.com/metro/dallas-metro/',
            'priority': '0.8',
            'changefreq': 'weekly'
        },
        {
            'url': 'https://plasmapaycalculator.com/metro/houston-metro/',
            'priority': '0.8',
            'changefreq': 'weekly'
        },
        
        # Comparison calculator tools
        {
            'url': 'https://plasmapaycalculator.com/tools/csl-vs-biolife-calculator.html',
            'priority': '0.9',
            'changefreq': 'weekly'
        },
        {
            'url': 'https://plasmapaycalculator.com/tools/octapharma-vs-grifols-calculator.html',
            'priority': '0.9',
            'changefreq': 'weekly'
        },
        {
            'url': 'https://plasmapaycalculator.com/tools/all-plasma-centers-comparison.html',
            'priority': '0.9',
            'changefreq': 'weekly'
        },
        
        # Seasonal content
        {
            'url': 'https://plasmapaycalculator.com/seasonal/tax-season-plasma-guide.html',
            'priority': '0.7',
            'changefreq': 'monthly'
        },
        {
            'url': 'https://plasmapaycalculator.com/seasonal/back-to-school-plasma-earnings.html',
            'priority': '0.7',
            'changefreq': 'monthly'
        },
        {
            'url': 'https://plasmapaycalculator.com/seasonal/holiday-plasma-bonus-guide.html',
            'priority': '0.7',
            'changefreq': 'monthly'
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
        
        # Log added pages
        for page in new_urls_to_add:
            page_name = page['url'].split('/')[-2] if page['url'].endswith('.html') else page['url'].split('/')[-2]
            print(f"  • {page_name}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error updating sitemap: {str(e)}")
        return False

def validate_new_sitemap():
    """Validate the updated sitemap"""
    
    sitemap_path = "/Users/glengomezmeade/Projects/plasma-pay-calculator/sitemap.xml"
    
    try:
        with open(sitemap_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Count total URLs
        url_count = len(re.findall(r'<loc>', content))
        
        # Check for new content types
        metro_count = len(re.findall(r'/metro/', content))
        tools_count = len(re.findall(r'/tools/', content))
        seasonal_count = len(re.findall(r'/seasonal/', content))
        
        print(f"📊 Sitemap validation results:")
        print(f"  • Total URLs: {url_count}")
        print(f"  • Metro pages: {metro_count}")
        print(f"  • Tool pages: {tools_count}")
        print(f"  • Seasonal pages: {seasonal_count}")
        
        # Check XML structure
        if content.startswith('<?xml') and '</urlset>' in content:
            print("✅ XML structure is valid")
            return True
        else:
            print("❌ XML structure is invalid")
            return False
            
    except Exception as e:
        print(f"❌ Error validating sitemap: {str(e)}")
        return False

def main():
    """Main function to update sitemap with new content"""
    print("📝 Updating sitemap with new SEO content...")
    
    # Add new pages
    if add_new_pages_to_sitemap():
        print("✅ Sitemap updated with new content")
    
    # Validate updated sitemap
    print("\n🔍 Validating updated sitemap...")
    if validate_new_sitemap():
        print("✅ Sitemap validation passed")
    else:
        print("❌ Sitemap validation failed")

if __name__ == "__main__":
    main()