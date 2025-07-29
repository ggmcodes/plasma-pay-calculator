#!/usr/bin/env python3
"""
Fix broken Spanish links by removing incorrect Spanish page references
"""

import os
import re
from pathlib import Path

def fix_spanish_links(file_path):
    """Remove broken Spanish links from English pages"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Only process English files
        if '/es/' in str(file_path):
            return False
            
        # Remove language switcher links to non-existent Spanish pages
        # But keep the ones for pages that DO have Spanish versions
        spanish_pages_that_exist = [
            '/es/',
            '/es/index.html',
            '/es/blog/',
            '/es/centers/',
            '/es/health/',
            '/es/process/',
            '/es/faq.html',
            '/es/states.html',
            '/es/contact.html',
            '/es/about.html'
        ]
        
        # Find language switcher pattern
        lang_pattern = r'<div class="language-switcher">.*?</div>'
        lang_match = re.search(lang_pattern, content, re.DOTALL)
        
        if lang_match:
            lang_html = lang_match.group(0)
            # Extract the Spanish link
            spanish_link_pattern = r'href="(/es/[^"]*)"'
            spanish_link_match = re.search(spanish_link_pattern, lang_html)
            
            if spanish_link_match:
                spanish_link = spanish_link_match.group(1)
                # Check if this Spanish page actually exists
                should_keep = False
                
                # Check against known Spanish pages
                for known_page in spanish_pages_that_exist:
                    if spanish_link == known_page:
                        should_keep = True
                        break
                
                # Check if it's a blog/calculator/center page (these have Spanish versions)
                if any(pattern in spanish_link for pattern in ['/es/blog/', '/es/calculators/', '/es/centers/']):
                    should_keep = True
                
                # If the Spanish page doesn't exist, remove the language switcher
                if not should_keep:
                    content = content.replace(lang_match.group(0), '')
                    
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    return True
                    
        return False
        
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")
        return False

def main():
    """Fix Spanish links in all English files"""
    root_path = Path("/Users/glengomezmeade/plasma-pay-calculator")
    fixed_count = 0
    
    print("🔧 Fixing broken Spanish links...")
    
    # Find all English HTML files
    for file_path in root_path.rglob("*.html"):
        if '/es/' not in str(file_path) and 'node_modules' not in str(file_path):
            if fix_spanish_links(file_path):
                fixed_count += 1
                if fixed_count % 50 == 0:
                    print(f"   Fixed {fixed_count} files...")
    
    print(f"\n✅ Fixed {fixed_count} files with broken Spanish links")

if __name__ == "__main__":
    main()