#!/usr/bin/env python3
"""
Replace Spanish flag with Mexican flag in language switcher
"""

import os
import re
from pathlib import Path

def fix_mexican_flag():
    """Replace Spanish flag 🇪🇸 with Mexican flag 🇲🇽"""
    
    base_dir = "/Users/glengomezmeade/Projects/plasma-pay-calculator"
    
    print("🇲🇽 UPDATING TO MEXICAN FLAG")
    print("🔄 Replacing Spanish flag with Mexican flag")
    print("=" * 80)
    
    files_updated = 0
    total_replacements = 0
    
    # Walk through all HTML files
    for root, dirs, files in os.walk(base_dir):
        if any(skip in root for skip in ['.git', 'node_modules', '__pycache__']):
            continue
            
        for file in files:
            if not file.endswith('.html'):
                continue
                
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, base_dir)
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Count Spanish flags before replacement
                spanish_flag_count = content.count('🇪🇸')
                
                if spanish_flag_count > 0:
                    # Replace Spanish flag with Mexican flag
                    updated_content = content.replace('🇪🇸', '🇲🇽')
                    
                    # Write back to file
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(updated_content)
                    
                    files_updated += 1
                    total_replacements += spanish_flag_count
                    print(f"✅ Updated {spanish_flag_count} flags in {relative_path}")
                    
            except Exception as e:
                print(f"⚠️  Error processing {relative_path}: {e}")
    
    print(f"\n📊 MEXICAN FLAG UPDATE SUMMARY:")
    print(f"   📄 Files updated: {files_updated}")
    print(f"   🇲🇽 Total flag replacements: {total_replacements}")
    print("   ✅ Language switcher now uses Mexican flag")
    
    return files_updated, total_replacements

def main():
    """Update flags to Mexican"""
    
    files_updated, total_replacements = fix_mexican_flag()
    
    print(f"\n🇲🇽 MEXICAN FLAG UPDATE COMPLETE")
    print("=" * 80)
    print(f"✅ {files_updated} files updated")
    print(f"✅ {total_replacements} Spanish flags replaced with Mexican flags")
    print("✅ Language switcher now properly represents Mexican Spanish")
    print("🇺🇸 🇲🇽 Perfect US-Mexico bilingual experience!")
    
    return files_updated > 0

if __name__ == "__main__":
    main()