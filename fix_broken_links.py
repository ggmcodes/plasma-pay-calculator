#!/usr/bin/env python3
"""
Fix broken links in plasma-pay-calculator website
"""

import os
import re
from pathlib import Path

def fix_links_in_file(file_path):
    """Fix broken links in an HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Fix privacy, terms, contact links
        content = re.sub(r'href="/privacy"', 'href="/privacy.html"', content)
        content = re.sub(r'href="/terms"', 'href="/terms.html"', content)
        content = re.sub(r'href="/contact"', 'href="/contact.html"', content)
        
        # Fix tools directory link
        content = re.sub(r'href="/tools/"', 'href="/topics/"', content)
        
        # Fix relative blog links that go up too many directories
        if '/blog/' in file_path and '/index.html' in file_path:
            # For blog subdirectory index files, fix relative paths
            content = re.sub(r'href="\.\./blog/', 'href="/blog/', content)
            content = re.sub(r'href="lost-job-plasma-donation-survival-guide\.html"', 
                            'href="/blog/lost-job-plasma-donation-survival-guide.html"', content)
        
        # Fix malformed link with HTML in href
        content = re.sub(r'href="/blog/plasma-donation-<a href=.*?"', 
                        'href="/blog/plasma-donation-eligibility-calculator.html"', content)
        
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
        if fix_links_in_file(html_file):
            fixed_count += 1
    
    print(f"✅ Fixed links in {fixed_count} files")

if __name__ == '__main__':
    main()