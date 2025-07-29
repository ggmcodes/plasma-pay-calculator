#!/usr/bin/env python3
"""
Script to add AdSense code to all HTML files missing it.
Ensures all pages use the correct plasmapaycalculator.com AdSense client ID.
"""

import os
import re
from pathlib import Path

# The correct AdSense code that should be in every page
CORRECT_ADSENSE_CODE = '''<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-3180649272238451"
     crossorigin="anonymous"></script>'''

# Alternative formats to look for (different client IDs or formats)
ADSENSE_PATTERNS = [
    r'<script[^>]*src="https://pagead2\.googlesyndication\.com/pagead/js/adsbygoogle\.js[^>]*>',
    r'<script[^>]*src="https://pagead2\.googlesyndication\.com/pagead/js?[^>]*>',
    r'ca-pub-\d+',
]

def has_adsense_code(content):
    """Check if content already has AdSense code"""
    for pattern in ADSENSE_PATTERNS:
        if re.search(pattern, content, re.IGNORECASE):
            return True
    return False

def has_correct_adsense_code(content):
    """Check if content has the correct AdSense code"""
    return 'ca-pub-3180649272238451' in content

def add_adsense_code(content):
    """Add AdSense code after Google Analytics if present, otherwise after <head>"""
    
    # Look for Google Analytics gtag config line
    gtag_pattern = r"(\s*gtag\('config',\s*'[^']+'\);\s*\n\s*</script>)"
    gtag_match = re.search(gtag_pattern, content)
    
    if gtag_match:
        # Insert AdSense code after Google Analytics
        insert_pos = gtag_match.end()
        new_content = (
            content[:insert_pos] + 
            '\n' + CORRECT_ADSENSE_CODE + '\n' +
            content[insert_pos:]
        )
        return new_content
    
    # If no Google Analytics, insert after <head>
    head_pattern = r'(<head[^>]*>)'
    head_match = re.search(head_pattern, content, re.IGNORECASE)
    
    if head_match:
        insert_pos = head_match.end()
        new_content = (
            content[:insert_pos] + 
            '\n' + CORRECT_ADSENSE_CODE + '\n' +
            content[insert_pos:]
        )
        return new_content
    
    return content

def replace_adsense_code(content):
    """Replace existing AdSense code with the correct one"""
    
    # Remove any existing AdSense scripts
    patterns_to_remove = [
        r'<script[^>]*src="https://pagead2\.googlesyndication\.com/pagead/js/adsbygoogle\.js[^>]*>[^<]*</script>',
        r'<script[^>]*src="https://pagead2\.googlesyndication\.com/pagead/js\?[^>]*>[^<]*</script>',
    ]
    
    for pattern in patterns_to_remove:
        content = re.sub(pattern, '', content, flags=re.IGNORECASE | re.DOTALL)
    
    # Add the correct AdSense code
    return add_adsense_code(content)

def process_html_file(file_path):
    """Process a single HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        if has_correct_adsense_code(content):
            return f"✅ {file_path} - Already has correct AdSense code"
        
        elif has_adsense_code(content):
            # Replace with correct code
            content = replace_adsense_code(content)
            action = "🔄 Replaced AdSense code"
        
        else:
            # Add AdSense code
            content = add_adsense_code(content)
            action = "➕ Added AdSense code"
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return f"{action} in {file_path}"
        else:
            return f"⚠️  {file_path} - Could not modify"
            
    except Exception as e:
        return f"❌ Error processing {file_path}: {str(e)}"

def main():
    """Main function to process all HTML files"""
    root_dir = Path('/Users/glengomezmeade/plasma-pay-calculator')
    
    # Find all HTML files
    html_files = []
    for pattern in ['**/*.html']:
        html_files.extend(root_dir.glob(pattern))
    
    # Exclude certain directories
    exclude_dirs = {'node_modules', '.git', '__pycache__'}
    html_files = [f for f in html_files if not any(part in exclude_dirs for part in f.parts)]
    
    print(f"Found {len(html_files)} HTML files to process...\n")
    
    # Process files by category for better organization
    categories = {
        'Root Pages': [],
        'Blog Posts': [],
        'Calculator Pages': [],
        'Center Pages': [],
        'Tool Pages': [],
        'Other Pages': []
    }
    
    # Categorize files
    for file_path in html_files:
        path_str = str(file_path)
        if '/blog/' in path_str:
            categories['Blog Posts'].append(file_path)
        elif '/calculators/' in path_str:
            categories['Calculator Pages'].append(file_path)
        elif '/centers/' in path_str:
            categories['Center Pages'].append(file_path)
        elif '/tools/' in path_str:
            categories['Tool Pages'].append(file_path)
        elif file_path.parent == root_dir:
            categories['Root Pages'].append(file_path)
        else:
            categories['Other Pages'].append(file_path)
    
    # Process each category
    total_processed = 0
    total_modified = 0
    
    for category, files in categories.items():
        if not files:
            continue
            
        print(f"\n=== {category} ({len(files)} files) ===")
        
        for file_path in sorted(files):
            result = process_html_file(file_path)
            print(result)
            
            total_processed += 1
            if any(indicator in result for indicator in ['➕', '🔄']):
                total_modified += 1
    
    print(f"\n=== SUMMARY ===")
    print(f"Total files processed: {total_processed}")
    print(f"Files modified: {total_modified}")
    print(f"Files with correct AdSense: {total_processed - total_modified}")

if __name__ == "__main__":
    main()