#!/usr/bin/env python3
"""
Script to remove Process menu items from all navigation menus 
and highlight Centers as the primary CTA across all HTML files.
"""

import os
import re
from pathlib import Path

def process_html_file(file_path):
    """Process a single HTML file to remove Process menu and highlight Centers"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        changes_made = []
        
        # Remove Process menu items from desktop navigation
        process_nav_pattern = r'<li><a href="/process/">Process</a></li>'
        if re.search(process_nav_pattern, content):
            content = re.sub(process_nav_pattern, '', content)
            changes_made.append("Removed desktop Process menu item")
        
        # Remove Process menu items from mobile navigation  
        process_mobile_pattern = r'<li><a href="/process/">Process</a></li>'
        if re.search(process_mobile_pattern, content):
            content = re.sub(process_mobile_pattern, '', content)
            changes_made.append("Removed mobile Process menu item")
        
        # Remove Spanish Process menu items
        process_spanish_pattern = r'<li><a href="/es/process/">Proceso</a></li>'
        if re.search(process_spanish_pattern, content):
            content = re.sub(process_spanish_pattern, '', content)
            changes_made.append("Removed Spanish Process menu item")
        
        # Highlight Centers menu item with special styling
        centers_pattern = r'<li><a href="/centers/">Centers</a></li>'
        centers_replacement = '<li><a href="/centers/" class="centers-highlight">🏥 Centers</a></li>'
        if re.search(centers_pattern, content):
            content = re.sub(centers_pattern, centers_replacement, content)
            changes_made.append("Highlighted Centers menu item")
        
        # Highlight Spanish Centers menu item  
        centers_spanish_pattern = r'<li><a href="/es/centers/">Centros</a></li>'
        centers_spanish_replacement = '<li><a href="/es/centers/" class="centers-highlight">🏥 Centros</a></li>'
        if re.search(centers_spanish_pattern, content):
            content = re.sub(centers_spanish_pattern, centers_spanish_replacement, content)
            changes_made.append("Highlighted Spanish Centers menu item")
        
        # Add CSS for Centers highlighting if nav styles are present
        nav_css_pattern = r'(\.nav-links a \{[^}]*\})'
        if re.search(nav_css_pattern, content):
            centers_css = """
        
        .centers-highlight {
            background: linear-gradient(135deg, #27ae60 0%, #2ecc71 100%) !important;
            color: white !important;
            border-radius: 6px !important;
            font-weight: 700 !important;
            box-shadow: 0 2px 6px rgba(39, 174, 96, 0.3) !important;
            transform: scale(1.05);
        }
        
        .centers-highlight:hover {
            background: linear-gradient(135deg, #219a52 0%, #26be5f 100%) !important;
            color: white !important;
            transform: scale(1.08);
        }"""
            
            content = re.sub(nav_css_pattern, r'\1' + centers_css, content)
            changes_made.append("Added Centers highlight CSS")
        
        # Only write if changes were made
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return changes_made
        
        return []
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return []

def main():
    """Main function to process all HTML files"""
    base_dir = Path("/Users/glengomezmeade/plasma-pay-calculator")
    
    # Find all HTML files
    html_files = []
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.html'):
                html_files.append(Path(root) / file)
    
    print(f"Found {len(html_files)} HTML files to process...")
    
    total_files_modified = 0
    total_changes = 0
    
    for html_file in html_files:
        changes = process_html_file(html_file)
        if changes:
            total_files_modified += 1
            total_changes += len(changes)
            print(f"✅ {html_file.relative_to(base_dir)}: {', '.join(changes)}")
    
    print(f"\n🎯 Summary:")
    print(f"Files processed: {len(html_files)}")
    print(f"Files modified: {total_files_modified}")
    print(f"Total changes: {total_changes}")
    
    print(f"\n✨ Process menu items removed from navigation")
    print(f"🏥 Centers menu items highlighted with special styling")
    print(f"Ready to push Centers as the primary CTA!")

if __name__ == "__main__":
    main()