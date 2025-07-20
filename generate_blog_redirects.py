#!/usr/bin/env python3
"""
Generate 301 redirects for all blog posts
"""

import os

# Migrated blog posts (excluding index.html which already exists on PPC)
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

def generate_blog_redirects():
    """Generate redirect rules for all blog posts"""
    redirects = []
    
    print(f"Generating redirects for {len(MIGRATED_BLOG_POSTS)} blog posts...")
    
    for post in MIGRATED_BLOG_POSTS:
        # Generate redirect with .html
        old_url_html = f"/blog/{post}.html"
        new_url = f"https://plasmapaycalculator.com/blog/{post}.html"
        redirects.append(f"{old_url_html} {new_url} 301")
        
        # Generate redirect without .html
        old_url_no_html = f"/blog/{post}"
        redirects.append(f"{old_url_no_html} {new_url} 301")
    
    return redirects

def generate_additional_redirects():
    """Generate redirects for other pages"""
    additional_redirects = [
        "# Calculator and core pages",
        "/calculator.html https://plasmapaycalculator.com/calculator/ 301",
        "/calculator https://plasmapaycalculator.com/calculator/ 301",
        "/states.html https://plasmapaycalculator.com/states.html 301",
        "/states https://plasmapaycalculator.com/states.html 301",
        "/center.html https://plasmapaycalculator.com/centers/ 301",
        "/center https://plasmapaycalculator.com/centers/ 301",
        "",
        "# Location-specific pages",
        "/frederick-md-plasma-donation.html https://plasmapaycalculator.com/calculators/maryland/frederick/ 301",
        "/frederick-md-plasma-donation https://plasmapaycalculator.com/calculators/maryland/frederick/ 301",
        "/iowa-plasma-donation-earnings.html https://plasmapaycalculator.com/calculators/iowa/ 301",
        "/iowa-plasma-donation-earnings https://plasmapaycalculator.com/calculators/iowa/ 301",
        "/lowell-ma-plasma-donation.html https://plasmapaycalculator.com/calculators/massachusetts/lowell/ 301",
        "/lowell-ma-plasma-donation https://plasmapaycalculator.com/calculators/massachusetts/lowell/ 301",
        "/how-much-do-you-get-for-donating-plasma.html https://plasmapaycalculator.com/blog/maximize-plasma-earnings.html 301",
        "/how-much-do-you-get-for-donating-plasma https://plasmapaycalculator.com/blog/maximize-plasma-earnings.html 301"
    ]
    
    return additional_redirects

def main():
    """Generate and display all redirects"""
    blog_redirects = generate_blog_redirects()
    additional_redirects = generate_additional_redirects()
    
    all_redirects = []
    all_redirects.append("# Blog post redirects - Migration to PlasmaPayCalculator.com")
    all_redirects.extend(blog_redirects)
    all_redirects.append("")
    all_redirects.extend(additional_redirects)
    
    print("\n" + "="*60)
    print("NEW REDIRECTS TO ADD TO _redirects FILE:")
    print("="*60)
    for redirect in all_redirects:
        print(redirect)
    
    print(f"\nTotal blog redirects generated: {len(blog_redirects)}")
    print(f"Total additional redirects: {len([r for r in additional_redirects if r and not r.startswith('#')])}")
    
    # Write to file
    with open('/tmp/new_redirects.txt', 'w') as f:
        for redirect in all_redirects:
            f.write(redirect + "\n")
    
    print(f"\nAll redirects written to /tmp/new_redirects.txt")

if __name__ == "__main__":
    main()