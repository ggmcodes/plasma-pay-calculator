#!/usr/bin/env python3
"""
Audit PPC internal linking - ensure Spanish/English isolation and proper navigation
"""

import os
import re
from pathlib import Path
import urllib.parse

def audit_internal_links():
    """Audit all internal links for proper language isolation"""
    
    base_dir = "/Users/glengomezmeade/Projects/plasma-pay-calculator"
    
    english_violations = []
    spanish_violations = []
    broken_links = []
    
    print("🔍 PPC INTERNAL LINKING AUDIT")
    print("=" * 80)
    print("Checking language isolation and link integrity...")
    print()
    
    # Walk through all HTML files
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if not file.endswith('.html'):
                continue
                
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, base_dir)
            
            # Skip certain directories
            if any(skip in relative_path for skip in ['.git', 'node_modules', '.vscode']):
                continue
            
            is_spanish_page = '/es/' in relative_path or relative_path.startswith('es/')
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                # Find all internal links
                link_pattern = r'href=["\'](/[^"\']*)["\']'
                links = re.findall(link_pattern, content)
                
                for link in links:
                    # Skip external links, anchors, and special links
                    if (link.startswith('http') or 
                        link.startswith('#') or 
                        link.startswith('mailto:') or 
                        link.startswith('tel:') or
                        link in ['/', '/index.html']):
                        continue
                    
                    # Check language isolation
                    is_spanish_link = '/es/' in link
                    
                    if is_spanish_page and not is_spanish_link:
                        # Spanish page linking to English content (violation)
                        if not any(allowed in link for allowed in ['/css/', '/js/', '/images/', '/assets/']):
                            english_violations.append({
                                'file': relative_path,
                                'link': link,
                                'type': 'Spanish page -> English content'
                            })
                    
                    elif not is_spanish_page and is_spanish_link:
                        # English page linking to Spanish content (violation)
                        spanish_violations.append({
                            'file': relative_path,
                            'link': link,
                            'type': 'English page -> Spanish content'
                        })
                    
                    # Check if linked file exists (for internal content links)
                    if not link.startswith('/css/') and not link.startswith('/js/') and not link.startswith('/images/'):
                        # Convert URL path to file path
                        file_to_check = None
                        if link.endswith('/'):
                            file_to_check = os.path.join(base_dir, link.lstrip('/'), 'index.html')
                        elif not link.endswith('.html'):
                            file_to_check = os.path.join(base_dir, link.lstrip('/') + '.html')
                            if not os.path.exists(file_to_check):
                                file_to_check = os.path.join(base_dir, link.lstrip('/'), 'index.html')
                        else:
                            file_to_check = os.path.join(base_dir, link.lstrip('/'))
                        
                        if file_to_check and not os.path.exists(file_to_check):
                            broken_links.append({
                                'file': relative_path,
                                'link': link,
                                'expected_path': file_to_check
                            })
                            
            except Exception as e:
                print(f"⚠️  Error reading {relative_path}: {e}")
    
    # Report results
    print("📊 LANGUAGE ISOLATION AUDIT:")
    print("=" * 80)
    
    if english_violations:
        print(f"🚨 SPANISH → ENGLISH VIOLATIONS ({len(english_violations)}):")
        for violation in english_violations[:10]:  # Show first 10
            print(f"  • {violation['file']} → {violation['link']}")
        if len(english_violations) > 10:
            print(f"  ... and {len(english_violations) - 10} more")
        print()
    
    if spanish_violations:
        print(f"🚨 ENGLISH → SPANISH VIOLATIONS ({len(spanish_violations)}):")
        for violation in spanish_violations[:10]:  # Show first 10
            print(f"  • {violation['file']} → {violation['link']}")
        if len(spanish_violations) > 10:
            print(f"  ... and {len(spanish_violations) - 10} more")
        print()
    
    if broken_links:
        print(f"🚨 BROKEN INTERNAL LINKS ({len(broken_links)}):")
        for broken in broken_links[:10]:  # Show first 10
            print(f"  • {broken['file']} → {broken['link']}")
        if len(broken_links) > 10:
            print(f"  ... and {len(broken_links) - 10} more")
        print()
    
    total_violations = len(english_violations) + len(spanish_violations)
    
    if total_violations == 0 and len(broken_links) == 0:
        print("✅ PERFECT LANGUAGE ISOLATION - No violations found!")
        print("✅ ALL INTERNAL LINKS WORKING")
    else:
        if total_violations > 0:
            print(f"❌ {total_violations} language isolation violations found")
        if broken_links:
            print(f"❌ {len(broken_links)} broken internal links found")
    
    print("\n" + "=" * 80)
    print("📊 AUDIT SUMMARY:")
    print(f"   • Spanish→English violations: {len(english_violations)}")
    print(f"   • English→Spanish violations: {len(spanish_violations)}")
    print(f"   • Broken internal links: {len(broken_links)}")
    print(f"   • Total issues: {total_violations + len(broken_links)}")
    
    return {
        'english_violations': english_violations,
        'spanish_violations': spanish_violations,
        'broken_links': broken_links
    }

def audit_navigation_consistency():
    """Check navigation consistency within each language"""
    
    print("\n🧭 NAVIGATION CONSISTENCY AUDIT:")
    print("=" * 80)
    
    base_dir = "/Users/glengomezmeade/Projects/plasma-pay-calculator"
    
    # Check Spanish navigation
    spanish_navs = []
    spanish_files = []
    
    for root, dirs, files in os.walk(os.path.join(base_dir, 'es')):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, base_dir)
                spanish_files.append(relative_path)
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                    # Extract navigation structure
                    nav_links = re.findall(r'<nav.*?</nav>', content, re.DOTALL)
                    if nav_links:
                        spanish_navs.append((relative_path, nav_links[0]))
                        
                except Exception as e:
                    print(f"⚠️  Error reading {relative_path}: {e}")
    
    print(f"📊 Found {len(spanish_files)} Spanish pages")
    print(f"📊 Found {len(spanish_navs)} navigation structures")
    
    # Basic consistency check
    if len(spanish_navs) > 1:
        first_nav = spanish_navs[0][1]
        inconsistent = []
        
        for path, nav in spanish_navs[1:]:
            # Simple similarity check (could be more sophisticated)
            if abs(len(nav) - len(first_nav)) > 100:  # Allow some variation
                inconsistent.append(path)
        
        if inconsistent:
            print(f"⚠️  {len(inconsistent)} pages have potentially inconsistent navigation")
        else:
            print("✅ Navigation appears consistent across Spanish pages")
    
    return len(spanish_files), len(broken_links) if 'broken_links' in locals() else 0

def main():
    """Run complete internal linking audit"""
    
    # Audit internal links
    results = audit_internal_links()
    
    # Audit navigation consistency  
    audit_navigation_consistency()
    
    # Final summary
    total_issues = (len(results['english_violations']) + 
                   len(results['spanish_violations']) + 
                   len(results['broken_links']))
    
    print(f"\n🏁 FINAL AUDIT RESULTS:")
    print("=" * 80)
    if total_issues == 0:
        print("✅ PERFECT - All internal linking is properly isolated and functional!")
    else:
        print(f"⚠️  {total_issues} total issues found - needs attention")
    
    return results

if __name__ == "__main__":
    main()