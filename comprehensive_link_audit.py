#!/usr/bin/env python3
"""
Comprehensive link audit for PPC - verify all English/Spanish links work correctly
"""

import os
import re
from pathlib import Path
import json

def comprehensive_link_audit():
    """Complete audit of all internal links"""
    
    base_dir = "/Users/glengomezmeade/Projects/plasma-pay-calculator"
    
    print("🔍 COMPREHENSIVE PPC LINK AUDIT")
    print("🎯 Verifying English ↔ Spanish Link Integrity")
    print("=" * 80)
    
    issues = {
        'broken_links': [],
        'cross_language_violations': [],
        'missing_counterparts': [],
        'navigation_issues': []
    }
    
    english_pages = {}
    spanish_pages = {}
    
    # 1. Catalog all pages
    print("📊 Cataloging all pages...")
    for root, dirs, files in os.walk(base_dir):
        if any(skip in root for skip in ['.git', 'node_modules', '__pycache__']):
            continue
            
        for file in files:
            if not file.endswith('.html'):
                continue
                
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, base_dir)
            
            if '/es/' in relative_path or relative_path.startswith('es/'):
                spanish_pages[relative_path] = file_path
            else:
                english_pages[relative_path] = file_path
    
    print(f"   📄 English pages: {len(english_pages)}")
    print(f"   📄 Spanish pages: {len(spanish_pages)}")
    
    # 2. Check internal links in each page
    print("\n🔗 Auditing internal links...")
    
    def check_page_links(page_path, relative_path, is_spanish):
        page_issues = []
        
        try:
            with open(page_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Find all internal links
            link_pattern = r'href=["\'](/[^"\'#]*)["\']'
            links = re.findall(link_pattern, content)
            
            for link in links:
                # Skip external links, assets, and anchors
                if (link.startswith('http') or 
                    link.startswith('#') or
                    link.startswith('mailto:') or
                    link.startswith('tel:') or
                    any(asset in link for asset in ['/css/', '/js/', '/images/', '/assets/', '/favicon'])):
                    continue
                
                # Check language isolation
                is_spanish_link = '/es/' in link
                
                if is_spanish and not is_spanish_link:
                    # Spanish page linking to English content (violation)
                    issues['cross_language_violations'].append({
                        'file': relative_path,
                        'link': link,
                        'type': 'Spanish → English'
                    })
                
                elif not is_spanish and is_spanish_link:
                    # English page linking to Spanish content (violation)
                    issues['cross_language_violations'].append({
                        'file': relative_path,
                        'link': link,
                        'type': 'English → Spanish'
                    })
                
                # Check if linked page exists
                target_exists = False
                possible_paths = [
                    link.lstrip('/') + '/index.html',
                    link.lstrip('/') + '.html',
                    link.lstrip('/')
                ]
                
                for possible_path in possible_paths:
                    full_path = os.path.join(base_dir, possible_path)
                    if os.path.exists(full_path):
                        target_exists = True
                        break
                
                if not target_exists and not link.endswith('.html'):
                    # Try with trailing slash
                    trailing_path = os.path.join(base_dir, link.lstrip('/') + '/', 'index.html')
                    if os.path.exists(trailing_path):
                        target_exists = True
                
                if not target_exists:
                    issues['broken_links'].append({
                        'file': relative_path,
                        'link': link,
                        'expected_paths': possible_paths
                    })
                    
        except Exception as e:
            print(f"⚠️  Error reading {relative_path}: {e}")
    
    # Check English pages
    for relative_path, file_path in english_pages.items():
        check_page_links(file_path, relative_path, False)
    
    # Check Spanish pages  
    for relative_path, file_path in spanish_pages.items():
        check_page_links(file_path, relative_path, True)
    
    # 3. Check for missing language counterparts
    print("\n🌐 Checking for missing language counterparts...")
    
    def find_counterpart(page_path, is_spanish_to_english=True):
        if is_spanish_to_english:
            # Spanish to English
            counterpart = page_path.replace('/es/', '/', 1)
            if counterpart.startswith('es/'):
                counterpart = counterpart[3:]
        else:
            # English to Spanish
            if page_path.startswith('/'):
                counterpart = '/es' + page_path
            else:
                counterpart = 'es/' + page_path
        
        return counterpart
    
    for spanish_path in spanish_pages.keys():
        english_counterpart = find_counterpart(spanish_path, True)
        if english_counterpart not in english_pages:
            issues['missing_counterparts'].append({
                'spanish_page': spanish_path,
                'missing_english': english_counterpart
            })
    
    # 4. Report results
    print(f"\n📋 AUDIT RESULTS:")
    print("=" * 80)
    
    print(f"🔗 Broken internal links: {len(issues['broken_links'])}")
    if issues['broken_links'][:5]:  # Show first 5
        for broken in issues['broken_links'][:5]:
            print(f"   • {broken['file']} → {broken['link']}")
        if len(issues['broken_links']) > 5:
            print(f"   ... and {len(issues['broken_links']) - 5} more")
    
    print(f"\n🚨 Language violations: {len(issues['cross_language_violations'])}")
    if issues['cross_language_violations'][:5]:  # Show first 5
        for violation in issues['cross_language_violations'][:5]:
            print(f"   • {violation['file']} → {violation['link']} ({violation['type']})")
        if len(issues['cross_language_violations']) > 5:
            print(f"   ... and {len(issues['cross_language_violations']) - 5} more")
    
    print(f"\n🌐 Missing counterparts: {len(issues['missing_counterparts'])}")
    if issues['missing_counterparts'][:5]:  # Show first 5
        for missing in issues['missing_counterparts'][:5]:
            print(f"   • {missing['spanish_page']} missing EN: {missing['missing_english']}")
        if len(issues['missing_counterparts']) > 5:
            print(f"   ... and {len(issues['missing_counterparts']) - 5} more")
    
    total_issues = (len(issues['broken_links']) + 
                   len(issues['cross_language_violations']) + 
                   len(issues['missing_counterparts']))
    
    print(f"\n🎯 TOTAL ISSUES: {total_issues}")
    
    if total_issues == 0:
        print("✅ PERFECT - All links working correctly!")
    else:
        print("⚠️  Issues found - creating fix recommendations...")
    
    return issues

def generate_fix_recommendations(issues):
    """Generate actionable fix recommendations"""
    
    print(f"\n🔧 FIX RECOMMENDATIONS:")
    print("=" * 80)
    
    if issues['cross_language_violations']:
        print("🚨 CRITICAL: Language Isolation Violations")
        print("   These links break the Spanish/English separation:")
        
        # Group by violation type
        spanish_to_english = [v for v in issues['cross_language_violations'] if v['type'] == 'Spanish → English']
        english_to_spanish = [v for v in issues['cross_language_violations'] if v['type'] == 'English → Spanish']
        
        if spanish_to_english:
            print(f"   📄 Spanish pages linking to English: {len(spanish_to_english)}")
            print("   🔧 FIX: Update these links to Spanish equivalents")
        
        if english_to_spanish:
            print(f"   📄 English pages linking to Spanish: {len(english_to_spanish)}")
            print("   🔧 FIX: Update these links to English equivalents")
    
    if issues['broken_links']:
        print(f"\n🔗 Broken Internal Links: {len(issues['broken_links'])}")
        print("   🔧 FIX: Update or remove these broken links")
    
    if issues['missing_counterparts']:
        print(f"\n🌐 Missing Language Counterparts: {len(issues['missing_counterparts'])}")
        print("   🔧 FIX: Create English versions or update Spanish links")

def main():
    """Run comprehensive link audit"""
    
    issues = comprehensive_link_audit()
    generate_fix_recommendations(issues)
    
    total_issues = (len(issues['broken_links']) + 
                   len(issues['cross_language_violations']) + 
                   len(issues['missing_counterparts']))
    
    print(f"\n🏁 AUDIT COMPLETE")
    print("=" * 80)
    if total_issues == 0:
        print("🎉 PERFECT LINK STRUCTURE - Ready for language switcher!")
    else:
        print(f"⚠️  {total_issues} issues need attention before language switcher")
    
    return issues

if __name__ == "__main__":
    main()