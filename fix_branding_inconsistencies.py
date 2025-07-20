#!/usr/bin/env python3
"""
Fix critical branding inconsistencies across the site
"""

import os
import re
from pathlib import Path

def fix_centers_page_branding():
    """Fix critical branding issues in centers/index.html"""
    
    centers_file = "/Users/glengomezmeade/Projects/plasma-pay-calculator/centers/index.html"
    
    if not os.path.exists(centers_file):
        print("❌ Centers file not found")
        return False
    
    try:
        with open(centers_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Fix 1: Change logo from blood drop emoji to PPC
        content = re.sub(
            r'<span class="logo-icon">🩸</span>',
            '<div class="logo-icon">PPC</div>',
            content
        )
        
        # Fix 2: Update email addresses from bestplasmacenters to plasmapaycalculator
        content = re.sub(
            r'hello@bestplasmacenters\.com',
            'hello@plasmapaycalculator.com',
            content
        )
        
        # Fix 3: Update schema.org URL references
        content = re.sub(
            r'"url": "https://bestplasmacenters\.com"',
            '"url": "https://plasmapaycalculator.com"',
            content
        )
        
        # Fix 4: Update social media URLs in schema
        content = re.sub(
            r'https://twitter\.com/bestplasmacenters',
            'https://twitter.com/plasmapaycalc',
            content
        )
        content = re.sub(
            r'https://www\.facebook\.com/bestplasmacenters',
            'https://www.facebook.com/plasmapaycalc',
            content
        )
        
        # Fix 5: Update logo path if it references old images
        content = re.sub(
            r'"/images/logo\.png"',
            '"/images/ppc-logo.png"',
            content
        )
        
        # Fix 6: Update any remaining "Best Plasma Centers" text
        content = re.sub(
            r'Best Plasma Centers',
            'Plasma Pay Calculator',
            content,
            flags=re.IGNORECASE
        )
        
        if content != original_content:
            with open(centers_file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print("✅ Fixed critical branding issues in centers/index.html")
            return True
        else:
            print("ℹ️ No changes needed in centers/index.html")
            return False
            
    except Exception as e:
        print(f"❌ Error fixing centers branding: {str(e)}")
        return False

def fix_logo_inconsistencies():
    """Fix logo inconsistencies across all pages"""
    
    # Find all HTML files that might have logo issues
    files_to_fix = []
    
    for root, dirs, files in os.walk("/Users/glengomezmeade/Projects/plasma-pay-calculator"):
        if any(skip_dir in root for skip_dir in ['.git', 'node_modules', '__pycache__']):
            continue
            
        for file in files:
            if file.endswith('.html'):
                files_to_fix.append(os.path.join(root, file))
    
    fixed_count = 0
    
    for file_path in files_to_fix:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Fix blood drop emoji logos to PPC
            content = re.sub(
                r'<span class="logo-icon">🩸</span>',
                '<div class="logo-icon">PPC</div>',
                content
            )
            
            # Also fix any divs that might use the emoji
            content = re.sub(
                r'<div class="logo-icon">🩸</div>',
                '<div class="logo-icon">PPC</div>',
                content
            )
            
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                rel_path = os.path.relpath(file_path, "/Users/glengomezmeade/Projects/plasma-pay-calculator")
                print(f"✅ Fixed logo in {rel_path}")
                fixed_count += 1
                
        except Exception as e:
            rel_path = os.path.relpath(file_path, "/Users/glengomezmeade/Projects/plasma-pay-calculator")
            print(f"❌ Error fixing {rel_path}: {str(e)}")
    
    return fixed_count

def fix_email_references():
    """Fix email references across the site"""
    
    files_to_fix = []
    
    for root, dirs, files in os.walk("/Users/glengomezmeade/Projects/plasma-pay-calculator"):
        if any(skip_dir in root for skip_dir in ['.git', 'node_modules', '__pycache__']):
            continue
            
        for file in files:
            if file.endswith('.html'):
                files_to_fix.append(os.path.join(root, file))
    
    fixed_count = 0
    
    for file_path in files_to_fix:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Fix email addresses
            content = re.sub(
                r'hello@bestplasmacenters\.com',
                'hello@plasmapaycalculator.com',
                content
            )
            
            # Fix any other email patterns
            content = re.sub(
                r'@bestplasmacenters\.com',
                '@plasmapaycalculator.com',
                content
            )
            
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                rel_path = os.path.relpath(file_path, "/Users/glengomezmeade/Projects/plasma-pay-calculator")
                print(f"✅ Fixed email references in {rel_path}")
                fixed_count += 1
                
        except Exception as e:
            rel_path = os.path.relpath(file_path, "/Users/glengomezmeade/Projects/plasma-pay-calculator")
            print(f"❌ Error fixing {rel_path}: {str(e)}")
    
    return fixed_count

def fix_schema_and_meta():
    """Fix schema.org and meta data inconsistencies"""
    
    files_to_fix = []
    
    for root, dirs, files in os.walk("/Users/glengomezmeade/Projects/plasma-pay-calculator"):
        if any(skip_dir in root for skip_dir in ['.git', 'node_modules', '__pycache__']):
            continue
            
        for file in files:
            if file.endswith('.html'):
                files_to_fix.append(os.path.join(root, file))
    
    fixed_count = 0
    
    for file_path in files_to_fix:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Fix schema.org URL references
            content = re.sub(
                r'"url": "https://bestplasmacenters\.com"',
                '"url": "https://plasmapaycalculator.com"',
                content
            )
            
            # Fix any remaining domain references in meta tags
            content = re.sub(
                r'content="https://bestplasmacenters\.com',
                'content="https://plasmapaycalculator.com',
                content
            )
            
            # Fix canonical URLs
            content = re.sub(
                r'href="https://bestplasmacenters\.com',
                'href="https://plasmapaycalculator.com',
                content
            )
            
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                rel_path = os.path.relpath(file_path, "/Users/glengomezmeade/Projects/plasma-pay-calculator")
                print(f"✅ Fixed schema/meta in {rel_path}")
                fixed_count += 1
                
        except Exception as e:
            rel_path = os.path.relpath(file_path, "/Users/glengomezmeade/Projects/plasma-pay-calculator")
            print(f"❌ Error fixing {rel_path}: {str(e)}")
    
    return fixed_count

def fix_remaining_brand_text():
    """Fix any remaining 'Best Plasma Centers' text references"""
    
    files_to_fix = []
    
    for root, dirs, files in os.walk("/Users/glengomezmeade/Projects/plasma-pay-calculator"):
        if any(skip_dir in root for skip_dir in ['.git', 'node_modules', '__pycache__']):
            continue
            
        for file in files:
            if file.endswith('.html'):
                files_to_fix.append(os.path.join(root, file))
    
    fixed_count = 0
    
    for file_path in files_to_fix:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Fix remaining brand text (case insensitive)
            content = re.sub(
                r'Best Plasma Centers',
                'Plasma Pay Calculator',
                content,
                flags=re.IGNORECASE
            )
            
            # Fix any variations
            content = re.sub(
                r'bestplasmacenters',
                'plasmapaycalculator',
                content,
                flags=re.IGNORECASE
            )
            
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                rel_path = os.path.relpath(file_path, "/Users/glengomezmeade/Projects/plasma-pay-calculator")
                print(f"✅ Fixed brand text in {rel_path}")
                fixed_count += 1
                
        except Exception as e:
            rel_path = os.path.relpath(file_path, "/Users/glengomezmeade/Projects/plasma-pay-calculator")
            print(f"❌ Error fixing {rel_path}: {str(e)}")
    
    return fixed_count

def main():
    """Main function to fix all branding inconsistencies"""
    print("🔧 Starting comprehensive branding fix...")
    
    total_fixes = 0
    
    # Fix 1: Centers page critical issues
    print("\n🏥 Fixing centers page branding...")
    if fix_centers_page_branding():
        total_fixes += 1
    
    # Fix 2: Logo inconsistencies
    print("\n🎨 Fixing logo inconsistencies...")
    logo_fixes = fix_logo_inconsistencies()
    total_fixes += logo_fixes
    print(f"✅ Fixed logos in {logo_fixes} files")
    
    # Fix 3: Email references
    print("\n📧 Fixing email references...")
    email_fixes = fix_email_references()
    total_fixes += email_fixes
    print(f"✅ Fixed email references in {email_fixes} files")
    
    # Fix 4: Schema and meta data
    print("\n🔍 Fixing schema and meta data...")
    schema_fixes = fix_schema_and_meta()
    total_fixes += schema_fixes
    print(f"✅ Fixed schema/meta in {schema_fixes} files")
    
    # Fix 5: Remaining brand text
    print("\n📝 Fixing remaining brand text...")
    text_fixes = fix_remaining_brand_text()
    total_fixes += text_fixes
    print(f"✅ Fixed brand text in {text_fixes} files")
    
    print(f"\n🎉 Branding consistency fix complete!")
    print(f"📊 Total files updated: {total_fixes}")
    print(f"🌟 Site now has consistent Plasma Pay Calculator branding")

if __name__ == "__main__":
    main()