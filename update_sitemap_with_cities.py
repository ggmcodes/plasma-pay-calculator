#!/usr/bin/env python3
"""
Update PlasmaPayCalculator sitemap with all migrated city pages
"""

import os
from pathlib import Path
from datetime import datetime

# Base URL
BASE_URL = "https://plasmapaycalculator.com"
CALCULATORS_DIR = "/Users/glengomezmeade/Projects/plasma-pay-calculator/calculators"

def generate_city_urls():
    """Generate all city page URLs"""
    city_urls = []
    
    # Find all city pages
    for state_dir in os.listdir(CALCULATORS_DIR):
        state_path = os.path.join(CALCULATORS_DIR, state_dir)
        if os.path.isdir(state_path):
            for city_dir in os.listdir(state_path):
                city_path = os.path.join(state_path, city_dir)
                if os.path.isdir(city_path) and os.path.exists(os.path.join(city_path, 'index.html')):
                    city_urls.append(f"{BASE_URL}/calculators/{state_dir}/{city_dir}/")
    
    return sorted(city_urls)

def read_current_sitemap():
    """Read current sitemap content"""
    sitemap_path = "/Users/glengomezmeade/Projects/plasma-pay-calculator/sitemap.xml"
    with open(sitemap_path, 'r', encoding='utf-8') as f:
        return f.read()

def update_sitemap():
    """Update sitemap with city pages"""
    # Get current sitemap content
    current_sitemap = read_current_sitemap()
    
    # Generate city URLs
    city_urls = generate_city_urls()
    print(f"Found {len(city_urls)} city pages to add to sitemap")
    
    # Create city entries
    today = datetime.now().strftime('%Y-%m-%d')
    city_entries = []
    
    for url in city_urls:
        entry = f"""  <url>
    <loc>{url}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>"""
        city_entries.append(entry)
    
    # Find insertion point (before closing urlset tag)
    insertion_point = current_sitemap.rfind('</urlset>')
    
    # Insert city entries
    city_section = f"\n\n  <!-- City Calculator Pages -->\n" + "\n".join(city_entries) + "\n"
    updated_sitemap = current_sitemap[:insertion_point] + city_section + current_sitemap[insertion_point:]
    
    # Write updated sitemap
    sitemap_path = "/Users/glengomezmeade/Projects/plasma-pay-calculator/sitemap.xml"
    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write(updated_sitemap)
    
    print(f"✅ Updated sitemap with {len(city_urls)} city pages")

def main():
    """Main function"""
    print("🚀 Updating PlasmaPayCalculator sitemap with city pages...")
    update_sitemap()
    print("🎉 Sitemap update complete!")

if __name__ == "__main__":
    main()