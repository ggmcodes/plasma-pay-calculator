#!/usr/bin/env python3
"""
Fix ALL remaining broken links to achieve 100% site integrity
"""

import os
import re
from pathlib import Path

def fix_all_remaining_links(file_path):
    """Fix all remaining broken links in an HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Fix FAQ link (missing .html)
        content = re.sub(r'href="/faq"', 'href="/faq.html"', content)
        
        # Fix health directory (doesn't exist, redirect to topics)
        content = re.sub(r'href="/health/"', 'href="/topics/requirements-eligibility/"', content)
        
        # Fix topics directory (missing index.html)
        content = re.sub(r'href="/topics/"', 'href="/topics/requirements-eligibility/"', content)
        
        # Fix plasma donation eligibility calculator (doesn't exist as separate page)
        content = re.sub(r'href="/blog/plasma-donation-eligibility-calculator\.html"', 
                        'href="/blog/plasma-donation-eligibility-quiz-viral.html"', content)
        
        # Fix relative blog links that are missing /blog/ prefix
        if '/blog/' in file_path:
            # Fix blog posts that are referenced without path
            content = re.sub(r'href="make-1000-month-plasma-donation-realistic-guide-2025\.html"',
                            'href="/blog/make-1000-month-plasma-donation-realistic-guide-2025.html"', content)
            content = re.sub(r'href="csl-plasma-pay-chart-2025-complete-rates-guide\.html"',
                            'href="/blog/csl-plasma-pay-chart-2025-complete-rates-guide.html"', content)
            content = re.sub(r'href="emergency-money-plasma-donation-broke\.html"',
                            'href="/blog/emergency-money-plasma-donation-broke.html"', content)
            content = re.sub(r'href="emergency-plasma-donation-cash-crisis-guide-2025\.html"',
                            'href="/blog/emergency-plasma-donation-cash-crisis-guide-2025.html"', content)
            content = re.sub(r'href="find-highest-paying-plasma-centers-near-me-2025\.html"',
                            'href="/blog/find-highest-paying-plasma-centers-near-me-2025.html"', content)
            content = re.sub(r'href="biolife-vs-csl-plasma-pay-chart-comparison-2025\.html"',
                            'href="/blog/biolife-vs-csl-plasma-pay-chart-comparison-2025.html"', content)
            
            # Fix Texas-specific blog links
            content = re.sub(r'href="texas-irs-plasma-income-tracking\.html"',
                            'href="/blog/plasma-donation-tax-guide-2025.html"', content)
            content = re.sub(r'href="texas-plasma-1099-tax-forms\.html"',
                            'href="/blog/plasma-donation-tax-guide-2025.html"', content)
            content = re.sub(r'href="texas-vein-health-plasma-donation\.html"',
                            'href="/blog/plasma-donation-requirements.html"', content)
            content = re.sub(r'href="texas-plasma-social-security-reporting\.html"',
                            'href="/blog/plasma-donation-tax-guide-2025.html"', content)
            
            # Fix generic blog references
            content = re.sub(r'href="plasma-center-comparison\.html"',
                            'href="/blog/biolife-vs-csl-plasma-comparison-2025.html"', content)
            content = re.sub(r'href="first-time-plasma-donation\.html"',
                            'href="/blog/first-time-plasma-donation-what-to-expect.html"', content)
            content = re.sub(r'href="plasma-donation-requirements\.html"',
                            'href="/blog/plasma-donation-requirements.html"', content)
            content = re.sub(r'href="plasma-donation-schedule\.html"',
                            'href="/blog/plasma-donation-frequency-guidelines.html"', content)
            content = re.sub(r'href="maximize-plasma-earnings\.html"',
                            'href="/blog/highest-paying-plasma-centers-near-me.html"', content)
            
            # Fix favicon reference
            content = re.sub(r'href="favicon\.svg"', 'href="/favicon.svg"', content)
        
        # Fix CSL plasma pay chart variations
        content = re.sub(r'href="/blog/csl-plasma-pay-chart-2025\.html"',
                        'href="/blog/csl-plasma-pay-chart-2025-complete-rates-guide.html"', content)
        
        # Fix malformed link tags
        content = re.sub(r'href=",\s*"', 'href="/"', content)
        content = re.sub(r'href=","', 'href="/"', content)
        content = re.sub(r'href=">\s*<link rel="', 'href="/"><link rel="', content)
        
        # Fix manifest.json reference (create it if needed)
        content = re.sub(r'href="manifest\.json"', 'href="/manifest.json"', content)
        
        # Remove all Spanish (/es/) links - redirect to main pages
        content = re.sub(r'href="/es/calculators/[^"]*"', 'href="/calculators/"', content)
        content = re.sub(r'href="/es/blog/[^"]*"', 'href="/blog/"', content)
        content = re.sub(r'href="/es/[^"]*"', 'href="/"', content)
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False
    
    return False

def create_manifest_json():
    """Create a basic manifest.json file"""
    manifest = {
        "name": "Plasma Pay Calculator",
        "short_name": "PPC",
        "description": "Calculate your plasma donation earnings across all 50 states",
        "start_url": "/",
        "display": "standalone",
        "background_color": "#ffffff",
        "theme_color": "#27ae60",
        "icons": [
            {
                "src": "/favicon.svg",
                "sizes": "any",
                "type": "image/svg+xml"
            }
        ]
    }
    
    import json
    manifest_path = '/Users/glengomezmeade/Projects/plasma-pay-calculator/manifest.json'
    with open(manifest_path, 'w') as f:
        json.dump(manifest, f, indent=2)
    print(f"✅ Created manifest.json")

def main():
    root_dir = '/Users/glengomezmeade/Projects/plasma-pay-calculator'
    
    # Create manifest.json if it doesn't exist
    if not os.path.exists(os.path.join(root_dir, 'manifest.json')):
        create_manifest_json()
    
    # Find all HTML files
    html_files = []
    for root, dirs, files in os.walk(root_dir):
        # Skip hidden directories and node_modules
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'node_modules']
        
        for file in files:
            if file.endswith('.html'):
                full_path = os.path.join(root, file)
                html_files.append(full_path)
    
    print(f"Processing {len(html_files)} HTML files...")
    
    fixed_count = 0
    for html_file in html_files:
        if fix_all_remaining_links(html_file):
            fixed_count += 1
            if fixed_count % 100 == 0:
                print(f"  Fixed {fixed_count} files...")
    
    print(f"✅ Fixed links in {fixed_count} files")

if __name__ == '__main__':
    main()