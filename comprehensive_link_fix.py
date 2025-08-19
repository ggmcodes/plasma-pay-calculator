#!/usr/bin/env python3
"""
Comprehensive link fix for plasma-pay-calculator website
"""

import os
import re
from pathlib import Path

def fix_all_links_in_file(file_path):
    """Fix all broken links in an HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Fix malformed links with HTML tags in href
        content = re.sub(r'href="/blog/plasma-donation-<a href=.*?"', 
                        'href="/blog/plasma-donation-eligibility-calculator.html"', content)
        content = re.sub(r'href="/blog/csl-<a href=.*?"', 
                        'href="/blog/csl-plasma-pay-chart-2025.html"', content)
        content = re.sub(r'href="/blog/<a href=.*?"', 
                        'href="/blog/"', content)
        
        # Fix calculator link
        content = re.sub(r'href="/calculator\.html"', 'href="/#calculator"', content)
        
        # Fix district-of-columbia path (it's in a subdirectory)
        content = re.sub(r'href="/calculators/district-of-columbia/"', 
                        'href="/calculators/district-of-columbia/washington/"', content)
        
        # Fix Spanish links (redirect to main site for now)
        content = re.sub(r'href="/es/[^"]*"', 'href="/"', content)
        
        # Fix relative paths that are broken
        if 'blog/' in file_path:
            # For blog files, fix relative paths
            content = re.sub(r'href="\.\./favicon\.svg"', 'href="/favicon.svg"', content)
            content = re.sub(r'href="\.\./about\.html"', 'href="/about.html"', content)
            content = re.sub(r'href="\.\./privacy\.html"', 'href="/privacy.html"', content)
            content = re.sub(r'href="\.\./terms\.html"', 'href="/terms.html"', content)
            content = re.sub(r'href="\.\./contact\.html"', 'href="/contact.html"', content)
            
            # Fix blog-to-blog relative links
            if '/index.html' in file_path:
                # For subdirectory index files
                content = re.sub(r'href="\.\./blog/([^"]+)"', r'href="/blog/\1"', content)
        
        # Fix california-cities typo
        content = re.sub(r'href="/california-cities"', 'href="/calculators/california/"', content)
        
        # Remove trailing commas and empty hrefs
        content = re.sub(r'href=","', 'href="/"', content)
        content = re.sub(r'href="  "', 'href="/"', content)
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False
    
    return False

def main():
    root_dir = '/Users/glengomezmeade/Projects/plasma-pay-calculator'
    
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
        if fix_all_links_in_file(html_file):
            fixed_count += 1
            if fixed_count % 50 == 0:
                print(f"  Fixed {fixed_count} files...")
    
    print(f"✅ Fixed links in {fixed_count} files")

if __name__ == '__main__':
    main()