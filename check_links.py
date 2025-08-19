#!/usr/bin/env python3
"""
Link checker for plasma-pay-calculator website
Checks all internal links and identifies broken links
"""

import os
import re
from pathlib import Path
from collections import defaultdict
import json

def extract_links_from_html(file_path):
    """Extract all links from an HTML file"""
    links = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
            # Find all href attributes
            href_pattern = r'href=[\'"]([^\'"]+)[\'"]'
            matches = re.findall(href_pattern, content)
            
            for link in matches:
                # Skip external links, anchors, and javascript
                if not link.startswith(('http://', 'https://', '#', 'javascript:', 'mailto:', 'tel:')):
                    links.append(link)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    
    return links

def normalize_link(link, current_file):
    """Normalize a link relative to the current file"""
    if link.startswith('/'):
        # Absolute path from root
        return link.lstrip('/')
    else:
        # Relative path
        current_dir = os.path.dirname(current_file)
        if current_dir:
            return os.path.normpath(os.path.join(current_dir, link))
        return link

def check_link_exists(link, root_dir):
    """Check if a link points to an existing file"""
    # Remove any query parameters or anchors
    clean_link = link.split('?')[0].split('#')[0]
    
    # Check if it's a directory (should have index.html)
    if clean_link.endswith('/'):
        clean_link = clean_link + 'index.html'
    elif not clean_link or clean_link == '':
        clean_link = 'index.html'
    elif '.' not in os.path.basename(clean_link):
        # No extension, might be a directory
        clean_link = clean_link + '/index.html'
    
    full_path = os.path.join(root_dir, clean_link)
    return os.path.exists(full_path), full_path

def main():
    root_dir = '/Users/glengomezmeade/Projects/plasma-pay-calculator'
    
    # Find all HTML files
    html_files = []
    for root, dirs, files in os.walk(root_dir):
        # Skip hidden directories and node_modules
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'node_modules']
        
        for file in files:
            if file.endswith('.html'):
                rel_path = os.path.relpath(os.path.join(root, file), root_dir)
                html_files.append(rel_path)
    
    print(f"Found {len(html_files)} HTML files")
    
    # Check all links
    broken_links = defaultdict(list)
    all_links = defaultdict(set)
    external_links = set()
    
    for html_file in html_files:
        full_path = os.path.join(root_dir, html_file)
        links = extract_links_from_html(full_path)
        
        for link in links:
            if link.startswith(('http://', 'https://')):
                external_links.add(link)
                continue
                
            normalized = normalize_link(link, html_file)
            all_links[html_file].add(link)
            
            exists, checked_path = check_link_exists(normalized, root_dir)
            if not exists:
                broken_links[html_file].append({
                    'link': link,
                    'normalized': normalized,
                    'checked_path': checked_path
                })
    
    # Report results
    print("\n" + "="*60)
    print("LINK CHECK REPORT")
    print("="*60)
    
    if broken_links:
        print(f"\n❌ Found {sum(len(v) for v in broken_links.values())} broken links in {len(broken_links)} files:\n")
        
        for file, links in sorted(broken_links.items())[:20]:  # Show first 20 files
            print(f"\n📄 {file}")
            for link_info in links[:5]:  # Show first 5 broken links per file
                print(f"   ❌ {link_info['link']}")
                print(f"      -> Looking for: {link_info['normalized']}")
    else:
        print("\n✅ No broken internal links found!")
    
    # Summary statistics
    print("\n" + "="*60)
    print("SUMMARY STATISTICS")
    print("="*60)
    print(f"Total HTML files: {len(html_files)}")
    print(f"Files with broken links: {len(broken_links)}")
    print(f"Total broken links: {sum(len(v) for v in broken_links.values())}")
    print(f"Total external links found: {len(external_links)}")
    
    # Save detailed report
    report = {
        'total_files': len(html_files),
        'files_with_broken_links': len(broken_links),
        'total_broken_links': sum(len(v) for v in broken_links.values()),
        'broken_links': dict(broken_links)
    }
    
    with open('/Users/glengomezmeade/Projects/plasma-pay-calculator/link_check_report.json', 'w') as f:
        json.dump(report, f, indent=2)
    
    print("\n📊 Detailed report saved to link_check_report.json")

if __name__ == '__main__':
    main()