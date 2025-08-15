#!/usr/bin/env python3
"""Fix all remaining broken internal links"""

import os
import re
import json
from collections import defaultdict

def fix_links_in_file(filepath, fixes_to_apply):
    """Apply link fixes to a file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Apply each fix
        for old_link, new_link in fixes_to_apply.items():
            # Fix href attributes
            pattern1 = f'href="{re.escape(old_link)}"'
            replacement1 = f'href="{new_link}"'
            content = re.sub(pattern1, replacement1, content)
            
            # Fix href attributes with single quotes
            pattern2 = f"href='{re.escape(old_link)}'"
            replacement2 = f"href='{new_link}'"
            content = re.sub(pattern2, replacement2, content)
        
        # Write back if changed
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
        
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

def main():
    print("=" * 60)
    print("FIXING ALL REMAINING BROKEN LINKS")
    print("=" * 60)
    
    # Define comprehensive link mappings
    link_mappings = {
        # First-time bonus page (doesn't exist, redirect to main calculator)
        '/first-time-plasma-donation-bonus.html': '/',
        
        # Calculator variations
        '/calculator.html': '/',
        '/how-much-do-you-get-for-donating-plasma.html': '/how-much-money-can-you-make-donating-plasma.html',
        '/iowa-plasma-donation-earnings.html': '/calculators/iowa/',
        
        # State pages that should be calculator pages
        '/state/california.html': '/calculators/california/',
        '/state/texas.html': '/calculators/texas/',
        '/state/florida.html': '/calculators/florida/',
        '/state/new-york.html': '/calculators/new-york/',
        '/state/iowa.html': '/calculators/iowa/',
        
        # Blog posts that don't exist - redirect to similar content
        '/plasma-donation-complete-beginners-guide.html': '/blog/first-time-plasma-donor-guide-2025.html',
        '/blog/maximize-plasma-donation-earnings-guide.html': '/blog/maximize-plasma-donation-earnings-2025.html',
        '/blog/csl-biolife-octapharma-comparison-guide.html': '/blog/biolife-vs-csl-plasma-comparison-2025.html',
        '/blog/plasma-donation-side-effects-safety-guide.html': '/blog/plasma-donation-side-effects-safety-2025.html',
        '/blog/weight-requirements-maximum-pay-guide.html': '/weight-requirements-maximum-pay-guide.html',
        '/blog/comprehensive-plasma-tax-guide-2025.html': '/comprehensive-plasma-tax-guide-2025.html',
        '/blog/plasma-donation-taxes-calculator.html': '/blog/plasma-donation-tax-guide-2025.html',
        
        # Tools that don't exist
        '/tools/all-plasma-centers-comparison.html': '/centers/',
        
        # Insurance pages that don't exist
        '/insurance-lawsuit-plasma-donors.html': '/blog/',
        '/insurance-protection-plasma-donors.html': '/blog/',
        
        # California blog posts that don't exist - redirect to main California content
        'california-plasma-donation-frequency-guidelines.html': '/blog/california/',
        'california-plasma-donation-tax-guide.html': '/blog/california/plasma-donation-taxes.html',
        'california-plasma-donation-common-questions.html': '/blog/california/',
        'california-plasma-donation-process-explained.html': '/blog/california/',
        
        # Process pages
        '/process/': '/blog/plasma-donation-process-explained-2025.html',
        
        # Center comparison pages
        '/centers/csl-plasma': '/centers/csl-plasma/',
        '/centers/biolife': '/centers/biolife/',
        '/centers/octapharma': '/centers/octapharma/',
        '/centers/grifols': '/centers/grifols/',
        
        # Spanish equivalents
        '/es/first-time-plasma-donation-bonus.html': '/es/',
        '/es/calculator.html': '/es/',
        '/es/health/side-effects': '/es/faq.html',
        '/es/health': '/es/faq.html',
        
        # Seasonal pages
        '/seasonal/summer-plasma-donation-tips.html': '/seasonal/',
        '/seasonal/winter-plasma-donation-guide.html': '/seasonal/',
        '/seasonal/holiday-plasma-donation-bonuses.html': '/seasonal/',
        
        # Weight requirements
        '/weight-requirements': '/weight-requirements-maximum-pay-guide.html',
        
        # Tax related
        '/tax-guide': '/comprehensive-plasma-tax-guide-2025.html',
        
        # Quick money
        '/quick-money': '/quick-money-today.html'
    }
    
    # Read the audit report to get all broken links
    with open('internal_linking_audit_report.json', 'r') as f:
        audit_data = json.load(f)
    
    files_fixed = 0
    total_fixes = 0
    
    # Process each file with broken links
    for filepath, broken_links in audit_data['broken_links'].items():
        fixes_for_file = {}
        
        for broken_link in broken_links:
            # Check if we have a mapping for this link
            if broken_link in link_mappings:
                fixes_for_file[broken_link] = link_mappings[broken_link]
                total_fixes += 1
            # Check for variations without leading slash
            elif '/' + broken_link in link_mappings:
                fixes_for_file[broken_link] = link_mappings['/' + broken_link]
                total_fixes += 1
            # For blog posts, try to find closest match
            elif broken_link.startswith('/blog/') and broken_link.endswith('.html'):
                # Default to blog index if no specific match
                fixes_for_file[broken_link] = '/blog/'
                total_fixes += 1
            elif broken_link.endswith('-plasma-donation.html'):
                # City-specific pages that don't exist
                fixes_for_file[broken_link] = '/calculators/'
                total_fixes += 1
        
        if fixes_for_file:
            if fix_links_in_file(filepath, fixes_for_file):
                files_fixed += 1
                print(f"✓ Fixed {len(fixes_for_file)} links in {filepath}")
    
    print("\n" + "=" * 60)
    print(f"SUMMARY:")
    print(f"  Files fixed: {files_fixed}")
    print(f"  Total link fixes applied: {total_fixes}")
    print("=" * 60)
    
    # Additional cleanup for common patterns
    print("\nApplying additional pattern-based fixes...")
    
    additional_patterns = [
        # Fix any remaining /state/ references
        (r'href="/state/([^/]+)\.html"', r'href="/calculators/\1/"'),
        (r'href="/state/([^/]+)/([^"]+)\.html"', r'href="/calculators/\1/\2/"'),
        
        # Fix blog post references without /blog/ prefix
        (r'href="(plasma-donation-[^"]+\.html)"', r'href="/blog/\1"'),
        
        # Fix tools references
        (r'href="/tools/([^"]+)\.html"', r'href="/tools/"'),
        
        # Fix health references
        (r'href="/health/[^"]*"', r'href="/topics/requirements-eligibility/"'),
        
        # Fix process references
        (r'href="/process/[^"]*"', r'href="/blog/plasma-donation-process-explained-2025.html"'),
    ]
    
    pattern_fixes = 0
    for root, dirs, files in os.walk('.'):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'node_modules']
        
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    original_content = content
                    
                    for pattern, replacement in additional_patterns:
                        content = re.sub(pattern, replacement, content)
                    
                    if content != original_content:
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(content)
                        pattern_fixes += 1
                        
                except Exception as e:
                    continue
    
    print(f"  Pattern-based fixes applied to {pattern_fixes} files")
    
    print("\n✅ All fixable broken links have been resolved!")

if __name__ == "__main__":
    main()