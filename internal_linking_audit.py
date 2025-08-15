#!/usr/bin/env python3
"""Comprehensive internal linking audit for the website"""

import os
import re
from urllib.parse import urlparse, urljoin
from collections import defaultdict
import json
from bs4 import BeautifulSoup

def extract_links_from_html(filepath):
    """Extract all internal links from an HTML file"""
    links = []
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
            
        # Find all anchor tags
        for tag in soup.find_all('a', href=True):
            href = tag['href']
            
            # Skip external links, mailto, tel, and anchors
            if (href.startswith('http://') or 
                href.startswith('https://') or 
                href.startswith('mailto:') or 
                href.startswith('tel:') or 
                href.startswith('#')):
                continue
                
            links.append(href)
            
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
    
    return links

def normalize_path(path, source_file):
    """Normalize a path relative to the source file"""
    # Remove any fragments
    if '#' in path:
        path = path.split('#')[0]
    
    # Remove query parameters
    if '?' in path:
        path = path.split('?')[0]
    
    # Handle absolute paths
    if path.startswith('/'):
        return path.lstrip('/')
    
    # Handle relative paths
    source_dir = os.path.dirname(source_file)
    normalized = os.path.normpath(os.path.join(source_dir, path))
    
    return normalized

def check_link_exists(link_path):
    """Check if a link target exists"""
    # Remove leading slash if present
    if link_path.startswith('/'):
        link_path = link_path[1:]
    
    # Check for exact file
    if os.path.exists(link_path):
        return True
    
    # Check with .html extension
    if not link_path.endswith('.html'):
        if os.path.exists(link_path + '.html'):
            return True
        
        # Check for index.html in directory
        index_path = os.path.join(link_path, 'index.html')
        if os.path.exists(index_path):
            return True
    
    return False

def main():
    print("=" * 60)
    print("INTERNAL LINKING AUDIT")
    print("=" * 60)
    
    all_files = []
    broken_links = defaultdict(list)
    link_stats = {
        'total_files': 0,
        'total_internal_links': 0,
        'broken_links': 0,
        'working_links': 0
    }
    
    # Collect all HTML files
    for root, dirs, files in os.walk('.'):
        # Skip hidden directories and node_modules
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'node_modules']
        
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                all_files.append(filepath)
    
    link_stats['total_files'] = len(all_files)
    
    print(f"\nAnalyzing {len(all_files)} HTML files...")
    print("-" * 60)
    
    # Check links in each file
    for filepath in all_files:
        relative_path = filepath[2:] if filepath.startswith('./') else filepath
        links = extract_links_from_html(filepath)
        
        for link in links:
            link_stats['total_internal_links'] += 1
            
            # Normalize the link path
            normalized_link = normalize_path(link, relative_path)
            
            # Check if link exists
            if not check_link_exists(normalized_link):
                broken_links[relative_path].append(link)
                link_stats['broken_links'] += 1
            else:
                link_stats['working_links'] += 1
    
    # Print results
    print("\n" + "=" * 60)
    print("AUDIT RESULTS")
    print("=" * 60)
    
    print(f"\n📊 STATISTICS:")
    print(f"   Total HTML files scanned: {link_stats['total_files']}")
    print(f"   Total internal links found: {link_stats['total_internal_links']}")
    print(f"   ✅ Working links: {link_stats['working_links']}")
    print(f"   ❌ Broken links: {link_stats['broken_links']}")
    
    if link_stats['total_internal_links'] > 0:
        success_rate = (link_stats['working_links'] / link_stats['total_internal_links']) * 100
        print(f"   Success rate: {success_rate:.1f}%")
    
    # Report broken links
    if broken_links:
        print("\n" + "=" * 60)
        print("❌ BROKEN LINKS FOUND:")
        print("=" * 60)
        
        # Sort by number of broken links
        sorted_files = sorted(broken_links.items(), key=lambda x: len(x[1]), reverse=True)
        
        for file, links in sorted_files[:20]:  # Show top 20 files with broken links
            print(f"\n📄 {file}")
            unique_links = list(set(links))
            for link in unique_links[:5]:  # Show first 5 broken links per file
                print(f"   → {link}")
            if len(unique_links) > 5:
                print(f"   ... and {len(unique_links) - 5} more broken links")
    else:
        print("\n✅ No broken internal links found!")
    
    # Save detailed report
    report = {
        'statistics': link_stats,
        'broken_links': dict(broken_links)
    }
    
    with open('internal_linking_audit_report.json', 'w') as f:
        json.dump(report, f, indent=2)
    
    print("\n" + "=" * 60)
    print("📝 Detailed report saved to: internal_linking_audit_report.json")
    print("=" * 60)
    
    # Suggest common fixes
    if broken_links:
        print("\n💡 COMMON ISSUES TO CHECK:")
        print("   1. Links to /centers/ directory (recently restored)")
        print("   2. Links to /guides/ (should be /blog/)")
        print("   3. Missing .html extensions")
        print("   4. Incorrect relative paths")
        print("   5. Links to deleted pages")

if __name__ == "__main__":
    main()