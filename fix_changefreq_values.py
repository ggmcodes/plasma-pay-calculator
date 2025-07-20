#!/usr/bin/env python3
"""
Fix invalid changefreq values in sitemap
"""

import re

def fix_changefreq_values():
    """Replace invalid changefreq values with valid ones"""
    
    sitemap_path = "/Users/glengomezmeade/Projects/plasma-pay-calculator/sitemap.xml"
    
    try:
        with open(sitemap_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Replace 'quarterly' with 'yearly' (valid value)
        content = content.replace('<changefreq>quarterly</changefreq>', '<changefreq>yearly</changefreq>')
        
        # Count replacements
        replacements = original_content.count('<changefreq>quarterly</changefreq>')
        
        if content != original_content:
            with open(sitemap_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✅ Fixed {replacements} invalid changefreq values (quarterly → yearly)")
            return True
        else:
            print("ℹ️ No invalid changefreq values found")
            return False
            
    except Exception as e:
        print(f"❌ Error fixing changefreq values: {str(e)}")
        return False

def validate_sitemap():
    """Validate all changefreq values"""
    
    sitemap_path = "/Users/glengomezmeade/Projects/plasma-pay-calculator/sitemap.xml"
    valid_values = ['always', 'hourly', 'daily', 'weekly', 'monthly', 'yearly', 'never']
    
    try:
        with open(sitemap_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find all changefreq values
        changefreq_matches = re.findall(r'<changefreq>([^<]+)</changefreq>', content)
        
        invalid_values = [val for val in changefreq_matches if val not in valid_values]
        
        if invalid_values:
            print(f"❌ Found invalid changefreq values: {set(invalid_values)}")
            return False
        else:
            print(f"✅ All changefreq values are valid")
            print(f"📊 Found values: {set(changefreq_matches)}")
            return True
            
    except Exception as e:
        print(f"❌ Error validating sitemap: {str(e)}")
        return False

def main():
    """Main function"""
    print("🔧 Fixing invalid changefreq values in sitemap...")
    
    # Fix invalid values
    fix_changefreq_values()
    
    # Validate sitemap
    print("\n🔍 Validating sitemap changefreq values...")
    validate_sitemap()

if __name__ == "__main__":
    main()