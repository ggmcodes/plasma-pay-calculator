#!/usr/bin/env python3
"""
Fix all internal links in PlasmaPayCalculator to remove bestplasmacenters.com references
"""

import os
import re
from pathlib import Path

def fix_file_links(file_path):
    """Fix links in a single file"""
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        changes_made = False
        
        # Fix bestplasmacenters.com links to point to /centers/
        if re.search(r'href="[^"]*bestplasmacenters\.com[^"]*"', content):
            # Update find center / location links to point to /centers/
            content = re.sub(
                r'href="[^"]*bestplasmacenters\.com[^"]*"([^>]*>.*?(?:find|center|location).*?</a>)',
                r'href="/centers/" target="_blank"\1',
                content,
                flags=re.IGNORECASE
            )
            
            # Update other bestplasmacenters.com links to relative paths
            content = re.sub(
                r'href="https://bestplasmacenters\.com/"',
                r'href="/centers/"',
                content
            )
            
            content = re.sub(
                r'href="https://bestplasmacenters\.com"',
                r'href="/centers/"',
                content
            )
            
            changes_made = True
        
        # Fix any remaining absolute URLs to relative
        if 'bestplasmacenters.com' in content:
            content = re.sub(
                r'https://bestplasmacenters\.com/',
                '/',
                content
            )
            changes_made = True
        
        # If changes were made, write the file
        if changes_made and content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        
        return False
        
    except Exception as e:
        print(f"❌ Error processing {file_path}: {str(e)}")
        return False

def find_files_with_links():
    """Find all files containing bestplasmacenters.com references"""
    
    base_dir = "/Users/glengomezmeade/Projects/plasma-pay-calculator"
    files_with_links = []
    
    # Search for files with bestplasmacenters.com
    for root, dirs, files in os.walk(base_dir):
        # Skip certain directories
        if any(skip_dir in root for skip_dir in ['.git', 'node_modules', '__pycache__']):
            continue
            
        for file in files:
            if file.endswith(('.html', '.js', '.css', '.md')):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        if 'bestplasmacenters.com' in content:
                            files_with_links.append(file_path)
                except:
                    continue
    
    return files_with_links

def main():
    """Main function"""
    print("🚀 Starting internal link fix for PlasmaPayCalculator...")
    
    # Find all files with bestplasmacenters.com references
    files_with_links = find_files_with_links()
    
    print(f"📊 Found {len(files_with_links)} files with bestplasmacenters.com references")
    
    if not files_with_links:
        print("✅ No files found with bestplasmacenters.com references!")
        return
    
    print("\nFiles to fix:")
    for file_path in files_with_links:
        rel_path = os.path.relpath(file_path, "/Users/glengomezmeade/Projects/plasma-pay-calculator")
        print(f"  - {rel_path}")
    
    print(f"\n🔧 Fixing links in {len(files_with_links)} files...")
    
    fixed_count = 0
    
    for file_path in files_with_links:
        rel_path = os.path.relpath(file_path, "/Users/glengomezmeade/Projects/plasma-pay-calculator")
        
        if fix_file_links(file_path):
            print(f"✅ Fixed: {rel_path}")
            fixed_count += 1
        else:
            print(f"⚠️  No changes needed: {rel_path}")
    
    print(f"\n🎉 Link fixing complete!")
    print(f"📊 Files fixed: {fixed_count}/{len(files_with_links)}")

if __name__ == "__main__":
    main()