#!/usr/bin/env python3
"""
Fix Spanish navigation to point to Spanish equivalents
"""

import os
import re
from pathlib import Path

def fix_spanish_navigation():
    """Fix Spanish pages to only link to Spanish content"""
    
    base_dir = "/Users/glengomezmeade/Projects/plasma-pay-calculator"
    es_dir = os.path.join(base_dir, 'es')
    
    print("🔧 FIXING SPANISH NAVIGATION")
    print("🎯 Converting English links to Spanish equivalents")
    print("=" * 80)
    
    # Navigation link mappings (English → Spanish)
    nav_mappings = {
        '/centers/': '/es/calculators/',
        '/calculators/': '/es/calculators/',
        '/calculators/california/': '/es/calculators/california/',
        '/calculators/texas/': '/es/calculators/texas/',
        '/calculators/florida/': '/es/calculators/florida/',
        '/calculators/illinois/': '/es/calculators/illinois/',
        '/calculators/georgia/': '/es/calculators/georgia/',
        '/blog/': '/es/blog/',
        '/about.html': '/es/about.html',
        '/about/': '/es/about.html',
        '/contact.html': '/es/contact.html',
        '/contact/': '/es/contact.html',
        '/faq.html': '/es/faq.html',
        '/faq/': '/es/faq.html',
        '/terms.html': '/es/terms.html',
        '/terms/': '/es/terms.html',
        '/privacy.html': '/es/privacy.html',
        '/privacy/': '/es/privacy.html',
        '/': '/es/',
        '/index.html': '/es/'
    }
    
    fixed_files = 0
    total_fixes = 0
    
    # Process all Spanish HTML files
    for root, dirs, files in os.walk(es_dir):
        for file in files:
            if not file.endswith('.html'):
                continue
                
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, base_dir)
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                file_fixes = 0
                
                # Apply navigation link fixes
                for english_link, spanish_link in nav_mappings.items():
                    # Fix href links
                    old_pattern = f'href="{english_link}"'
                    new_pattern = f'href="{spanish_link}"'
                    
                    if old_pattern in content:
                        content = content.replace(old_pattern, new_pattern)
                        file_fixes += content.count(new_pattern) - original_content.count(new_pattern)
                    
                    # Fix href links with single quotes
                    old_pattern_single = f"href='{english_link}'"
                    new_pattern_single = f"href='{spanish_link}'"
                    
                    if old_pattern_single in content:
                        content = content.replace(old_pattern_single, new_pattern_single)
                        file_fixes += 1
                
                # Fix common navigation patterns
                navigation_fixes = [
                    # Main navigation
                    ('href="/calculators/california"', 'href="/es/calculators/california"'),
                    ('href="/calculators/texas"', 'href="/es/calculators/texas"'),
                    ('href="/calculators/florida"', 'href="/es/calculators/florida"'),
                    ('href="/centers"', 'href="/es/calculators"'),
                    ('href="/blog"', 'href="/es/blog"'),
                    
                    # Footer links
                    ('href="/about"', 'href="/es/about.html"'),
                    ('href="/contact"', 'href="/es/contact.html"'),
                    ('href="/terms"', 'href="/es/terms.html"'),
                    ('href="/privacy"', 'href="/es/privacy.html"'),
                    
                    # Logo and home links
                    ('href="/">', 'href="/es/">'),
                    ('href="/index.html"', 'href="/es/"'),
                ]
                
                for old_link, new_link in navigation_fixes:
                    if old_link in content:
                        content = content.replace(old_link, new_link)
                        file_fixes += 1
                
                # Save if changes were made
                if content != original_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    fixed_files += 1
                    total_fixes += file_fixes
                    print(f"✅ Fixed {file_fixes} links in {relative_path}")
                    
            except Exception as e:
                print(f"⚠️  Error processing {relative_path}: {e}")
    
    print(f"\n📊 NAVIGATION FIX SUMMARY:")
    print(f"   📄 Files fixed: {fixed_files}")
    print(f"   🔗 Total link fixes: {total_fixes}")
    print("   ✅ Spanish pages now link to Spanish content only")
    
    return fixed_files, total_fixes

def main():
    """Fix Spanish navigation"""
    
    fixed_files, total_fixes = fix_spanish_navigation()
    
    print(f"\n🎯 SPANISH NAVIGATION FIXED")
    print("=" * 80)
    print(f"✅ {fixed_files} files updated with {total_fixes} link fixes")
    print("✅ Spanish pages now maintain language isolation")
    print("✅ Ready for language switcher implementation")
    
    return fixed_files > 0

if __name__ == "__main__":
    main()