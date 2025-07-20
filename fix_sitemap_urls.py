#!/usr/bin/env python3
"""
Fix sitemap URL consistency to match canonical tags (remove trailing slashes)
"""

import os
import re

def fix_sitemap_trailing_slashes():
    """Remove trailing slashes from calculator URLs in sitemap to match canonicals"""
    
    sitemap_path = "/Users/glengomezmeade/Projects/plasma-pay-calculator/sitemap.xml"
    
    try:
        with open(sitemap_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Fix calculator URLs - remove trailing slashes to match canonical tags
        content = re.sub(
            r'<loc>https://plasmapaycalculator\.com/calculators/([^/]+)/([^/]+)/</loc>',
            r'<loc>https://plasmapaycalculator.com/calculators/\1/\2</loc>',
            content
        )
        
        # Fix state calculator URLs - remove trailing slashes
        content = re.sub(
            r'<loc>https://plasmapaycalculator\.com/calculators/([^/]+)/</loc>',
            r'<loc>https://plasmapaycalculator.com/calculators/\1</loc>',
            content
        )
        
        # Fix any other directory URLs that shouldn't have trailing slashes
        # but keep trailing slashes for legitimate directory pages like /blog/, /centers/
        
        if content != original_content:
            # Backup original
            backup_path = f"{sitemap_path}.backup2"
            with open(backup_path, 'w', encoding='utf-8') as f:
                f.write(original_content)
            
            # Write fixed sitemap
            with open(sitemap_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print("✅ Fixed sitemap URL trailing slash consistency")
            
            # Count fixes
            city_fixes = len(re.findall(r'/calculators/[^/]+/[^/]+</loc>', content))
            state_fixes = len(re.findall(r'/calculators/[^/]+</loc>', content)) - city_fixes
            
            print(f"📊 Fixed {city_fixes} city calculator URLs")
            print(f"📊 Fixed {state_fixes} state calculator URLs")
            
            return True
        else:
            print("ℹ️ No trailing slash fixes needed")
            return False
            
    except Exception as e:
        print(f"❌ Error fixing sitemap: {str(e)}")
        return False

def validate_sitemap_consistency():
    """Validate that sitemap URLs match canonical tag patterns"""
    
    sitemap_path = "/Users/glengomezmeade/Projects/plasma-pay-calculator/sitemap.xml"
    
    try:
        with open(sitemap_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for remaining inconsistencies
        issues = []
        
        # Check for calculator URLs with trailing slashes
        trailing_slash_calcs = re.findall(r'<loc>https://plasmapaycalculator\.com/calculators/[^<]+/</loc>', content)
        if trailing_slash_calcs:
            issues.append(f"Found {len(trailing_slash_calcs)} calculator URLs with trailing slashes")
        
        # Check for proper directory URLs
        proper_dirs = ['blog/', 'centers/', 'health/', 'metro/']
        for directory in proper_dirs:
            if f"/{directory}" in content and f"/{directory[:-1]}</loc>" in content:
                issues.append(f"Directory {directory} missing trailing slash")
        
        if issues:
            print("⚠️ Sitemap consistency issues found:")
            for issue in issues:
                print(f"  • {issue}")
            return False
        else:
            print("✅ Sitemap URLs are consistent with canonical patterns")
            return True
            
    except Exception as e:
        print(f"❌ Error validating sitemap: {str(e)}")
        return False

def main():
    """Main function to fix sitemap URL consistency"""
    print("🔧 Fixing sitemap URL consistency issues...")
    
    # Fix trailing slashes
    if fix_sitemap_trailing_slashes():
        print("✅ Sitemap trailing slashes fixed")
    
    # Validate consistency
    print("\n🔍 Validating sitemap consistency...")
    if validate_sitemap_consistency():
        print("✅ Sitemap validation passed")
    else:
        print("⚠️ Additional sitemap issues need attention")

if __name__ == "__main__":
    main()