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
        },
        {
            'url': 'https://plasmapaycalculator.com/blog/shocking-irs-tracks-plasma-income-2025.html',
            'priority': '0.9',
            'changefreq': 'monthly'
        },
        {
            'url': 'https://plasmapaycalculator.com/blog/plasma-income-tax-deductions-guide-2025.html',
            'priority': '0.9',
            'changefreq': 'monthly'
        },
        {
            'url': 'https://plasmapaycalculator.com/blog/social-security-plasma-income-impact-2025.html',
            'priority': '0.9',
            'changefreq': 'monthly'
        },
        {
            'url': 'https://plasmapaycalculator.com/blog/insurance-companies-hate-plasma-donors-2025.html',
            'priority': '0.9',
            'changefreq': 'monthly'
        },
        {
            'url': 'https://plasmapaycalculator.com/blog/student-loan-crisis-plasma-solution-2025.html',
            'priority': '0.9',
            'changefreq': 'weekly'
        },
        {
            'url': 'https://plasmapaycalculator.com/blog/realistic-plasma-income-budget-calculator-2025.html',
            'priority': '0.8',
            'changefreq': 'weekly'
        },
        {
            'url': 'https://plasmapaycalculator.com/blog/can-you-donate-plasma-with-medical-conditions-2025.html',
            'priority': '0.9',
            'changefreq': 'monthly'
        },
        {
            'url': 'https://plasmapaycalculator.com/blog/emergency-same-day-plasma-donation-cash-2025.html',
            'priority': '0.9',
            'changefreq': 'weekly'
        },
        {
            'url': 'https://plasmapaycalculator.com/blog/plasma-donation-after-covid-vaccine-timing-2025.html',
            'priority': '0.9',
            'changefreq': 'monthly'
        },
        {
            'url': 'https://plasmapaycalculator.com/blog/advanced-plasma-donation-optimization-hacks-2025.html',
            'priority': '0.8',
            'changefreq': 'weekly'
        },
        {
            'url': 'https://plasmapaycalculator.com/blog/pregnancy-plasma-donation-complete-guide-2025.html',
            'priority': '0.9',
            'changefreq': 'monthly'
        },
        {
            'url': 'https://plasmapaycalculator.com/blog/24-hour-plasma-centers-complete-locator-guide-2025.html',
            'priority': '0.8',
            'changefreq': 'weekly'
        },
        {
            'url': 'https://plasmapaycalculator.com/blog/fastest-plasma-qualification-speed-guide-2025.html',
            'priority': '0.8',
            'changefreq': 'weekly'
        },
        {
            'url': 'https://plasmapaycalculator.com/blog/csl-plasma-pay-chart-2025-complete-rates-guide.html',
            'priority': '0.9',
            'changefreq': 'monthly'
        },
        {
            'url': 'https://plasmapaycalculator.com/blog/how-to-improve-veins-for-plasma-donation-complete-guide.html',
            'priority': '0.8',
            'changefreq': 'monthly'
        },
        {
            'url': 'https://plasmapaycalculator.com/blog/make-1000-month-plasma-donation-realistic-guide-2025.html',
            'priority': '0.9',
            'changefreq': 'weekly'
        },
        {
            'url': 'https://plasmapaycalculator.com/blog/california-plasma-donation-pay-rates-complete-guide-2025.html',
            'priority': '0.8',
            'changefreq': 'weekly'
        },
        {
            'url': 'https://plasmapaycalculator.com/blog/biolife-vs-csl-plasma-pay-chart-comparison-2025.html',
            'priority': '0.9',
            'changefreq': 'weekly'
        },
        {
            'url': 'https://plasmapaycalculator.com/blog/cuanto-pagan-por-donar-plasma-guia-completa-2025.html',
            'priority': '0.8',
            'changefreq': 'weekly'
        },
        {
            'url': 'https://plasmapaycalculator.com/blog/annual-plasma-income-calculator-guide-2025.html',
            'priority': '0.8',
            'changefreq': 'weekly'
        },
        {
            'url': 'https://plasmapaycalculator.com/blog/highest-paying-plasma-centers-by-state-location-guide-2025.html',
            'priority': '0.9',
            'changefreq': 'weekly'
        },
        {
            'url': 'https://plasmapaycalculator.com/blog/new-jersey-plasma-donation-earnings-guide-2025.html',
            'priority': '0.8',
            'changefreq': 'weekly'
        },
        {
            'url': 'https://plasmapaycalculator.com/blog/find-highest-paying-plasma-centers-near-me-2025.html',
            'priority': '0.9',
            'changefreq': 'weekly'
        },
        {
            'url': 'https://plasmapaycalculator.com/blog/earn-800-month-plasma-donation-complete-strategy-guide-2025.html',
            'priority': '0.9',
            'changefreq': 'weekly'
        },
        {
            'url': 'https://plasmapaycalculator.com/blog/advanced-plasma-donation-optimization-techniques-2025.html',
            'priority': '0.8',
            'changefreq': 'weekly'
        },
        {
            'url': 'https://plasmapaycalculator.com/blog/better-ways-earn-money-than-plasma-donation-2025.html',
            'priority': '0.8',
            'changefreq': 'weekly'
        },
        {
            'url': 'https://plasmapaycalculator.com/blog/plasma-donation-side-effects-red-veins-medical-guide-2025.html',
            'priority': '0.9',
            'changefreq': 'monthly'
        },
        {
            'url': 'https://plasmapaycalculator.com/blog/complete-cost-breakdown-plasma-donation-2025.html',
            'priority': '0.8',
            'changefreq': 'monthly'
        },
        {
            'url': 'https://plasmapaycalculator.com/blog/plasma-donation-referral-income-maximization-2025.html',
            'priority': '0.8',
            'changefreq': 'weekly'
        },
        {
            'url': 'https://plasmapaycalculator.com/blog/plasma-donation-health-risks-medical-analysis-2025.html',
            'priority': '0.9',
            'changefreq': 'monthly'
        },
        {
            'url': 'https://plasmapaycalculator.com/blog/new-york-city-plasma-donation-earnings-guide-2025.html',
            'priority': '0.9',
            'changefreq': 'weekly'
        },
        {
            'url': 'https://plasmapaycalculator.com/blog/seasonal-plasma-donation-income-optimization-2025.html',
            'priority': '0.8',
            'changefreq': 'weekly'
        },
        {
            'url': 'https://plasmapaycalculator.com/blog/plasma-donation-calculators-income-tools-2025.html',
            'priority': '0.9',
            'changefreq': 'weekly'
        },
        {
            'url': 'https://plasmapaycalculator.com/blog/plasma-donation-taxes-irs-legal-guide-2025.html',
            'priority': '0.9',
            'changefreq': 'monthly'
        },
        {
            'url': 'https://plasmapaycalculator.com/blog/emergency-plasma-donation-cash-crisis-guide-2025.html',
            'priority': '0.9',
            'changefreq': 'weekly'
        },
        {
            'url': 'https://plasmapaycalculator.com/blog/pregnancy-plasma-donation-medical-guide-2025.html',
            'priority': '0.9',
            'changefreq': 'monthly'
        },
        {
            'url': 'https://plasmapaycalculator.com/blog/college-student-plasma-income-optimization-2025.html',
            'priority': '0.8',
            'changefreq': 'weekly'
        },
        {
            'url': 'https://plasmapaycalculator.com/blog/plasma-donation-weight-requirements-bmi-guide-2025.html',
            'priority': '0.9',
            'changefreq': 'monthly'
        },
        {
            'url': 'https://plasmapaycalculator.com/blog/plasma-donation-near-me-locator-guide-2025.html',
            'priority': '0.9',
            'changefreq': 'weekly'
        },
        {
            'url': 'https://plasmapaycalculator.com/blog/plasma-donation-frequency-schedule-optimization-2025.html',
            'priority': '0.8',
            'changefreq': 'monthly'
        },
        {
            'url': 'https://plasmapaycalculator.com/blog/plasma-donation-eligibility-requirements-comprehensive-guide-2025.html',
            'priority': '0.9',
            'changefreq': 'monthly'
        },
        {
            'url': 'https://plasmapaycalculator.com/blog/plasma-donation-recovery-tips-complete-guide-2025.html',
            'priority': '0.8',
            'changefreq': 'monthly'
        },
        {
            'url': 'https://plasmapaycalculator.com/blog/plasma-donation-bonus-maximization-strategies-2025.html',
            'priority': '0.9',
            'changefreq': 'weekly'
        },
        {
            'url': 'https://plasmapaycalculator.com/blog/plasma-donation-safety-medical-concerns-2025.html',
            'priority': '0.9',
            'changefreq': 'monthly'
        },
        {
            'url': 'https://plasmapaycalculator.com/blog/plasma-donation-first-time-complete-guide-2025.html',
            'priority': '0.9',
            'changefreq': 'monthly'
        },
        {
            'url': 'https://plasmapaycalculator.com/blog/plasma-donation-nutrition-diet-optimization-2025.html',
            'priority': '0.8',
            'changefreq': 'monthly'
        },
        {
            'url': 'https://plasmapaycalculator.com/blog/plasma-donation-tax-implications-irs-guide-2025.html',
            'priority': '0.9',
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