#!/usr/bin/env python3
"""
Update PlasmaPayCalculator sitemap with newly migrated blog posts
"""

import os
from datetime import datetime

# Migrated blog posts
MIGRATED_BLOG_POSTS = [
    "best-plasma-centers-texas",
    "best-times-donate-plasma",
    "biolife-vs-csl-plasma-comparison",
    "can-you-donate-plasma-twice-a-week",
    "can-you-donate-plasma-with-tattoos",
    "complete-medical-eligibility-guide-plasma-donation",
    "csl-plasma-pay-rates-2025",
    "does-red-cross-pay-for-blood-donations",
    "first-time-plasma-donation-what-to-expect",
    "highest-paying-plasma-centers-near-me",
    "how-much-do-you-actually-make-donating-plasma",
    "how-much-do-you-get-donating-plasma-iowa",
    "how-much-money-can-you-make-donating-plasma-2025",
    "how-much-money-plasma-donation",
    "how-to-prepare-for-plasma-donation",
    "is-plasma-donation-worth-it-financial-analysis",
    "plasma-donation-bonuses-promotions",
    "plasma-donation-des-moines-iowa",
    "plasma-donation-health-screening-guide",
    "plasma-donation-process-step-by-step",
    "plasma-donation-side-effects",
    "plasma-donation-side-hustle-complete-guide",
    "plasma-donation-tax-guide-2025",
    "plasma-donation-tips-beginners",
    "plasma-donation-weight-requirements",
    "state-by-state-plasma-donation-laws-regulations-2025",
    "understanding-plasma-medical-uses",
    "which-plasma-center-pays-most-money"
]

def read_current_sitemap():
    """Read current sitemap content"""
    sitemap_path = "/Users/glengomezmeade/Projects/plasma-pay-calculator/sitemap.xml"
    with open(sitemap_path, 'r', encoding='utf-8') as f:
        return f.read()

def update_sitemap():
    """Update sitemap with blog posts"""
    # Get current sitemap content
    current_sitemap = read_current_sitemap()
    
    print(f"📄 Adding {len(MIGRATED_BLOG_POSTS)} blog posts to sitemap...")
    
    # Create blog entries
    today = datetime.now().strftime('%Y-%m-%d')
    blog_entries = []
    
    for post in MIGRATED_BLOG_POSTS:
        url = f"https://plasmapaycalculator.com/blog/{post}.html"
        entry = f"""  <url>
    <loc>{url}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.7</priority>
  </url>"""
        blog_entries.append(entry)
    
    # Find insertion point (before closing urlset tag)
    insertion_point = current_sitemap.rfind('</urlset>')
    
    # Insert blog entries
    blog_section = f"\n\n  <!-- Migrated Blog Posts from BestPlasmaCenters -->\n" + "\n".join(blog_entries) + "\n"
    updated_sitemap = current_sitemap[:insertion_point] + blog_section + current_sitemap[insertion_point:]
    
    # Write updated sitemap
    sitemap_path = "/Users/glengomezmeade/Projects/plasma-pay-calculator/sitemap.xml"
    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write(updated_sitemap)
    
    print(f"✅ Updated sitemap with {len(MIGRATED_BLOG_POSTS)} blog posts")
    
    return len(MIGRATED_BLOG_POSTS)

def main():
    """Main function"""
    print("🚀 Updating PlasmaPayCalculator sitemap with migrated blog posts...")
    
    added_count = update_sitemap()
    
    print(f"🎉 Sitemap update complete! Added {added_count} blog post URLs")

if __name__ == "__main__":
    main()