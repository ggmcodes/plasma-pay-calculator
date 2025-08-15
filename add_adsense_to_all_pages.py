#!/usr/bin/env python3
"""Add AdSense code to all HTML pages that are missing it"""

import os
import re

# AdSense script to add
ADSENSE_SCRIPT = """<!-- Google AdSense -->
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-3180649272238451"
     crossorigin="anonymous"></script>"""

def add_adsense_to_file(filepath):
    """Add AdSense code to an HTML file if it's missing"""
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if AdSense is already present
        if 'ca-pub-3180649272238451' in content:
            return False
        
        # Find the </head> tag and insert AdSense before it
        if '</head>' in content:
            # Insert AdSense script before </head>
            content = content.replace('</head>', f'{ADSENSE_SCRIPT}\n</head>')
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✓ Added AdSense to: {filepath}")
            return True
        else:
            print(f"⚠ No </head> tag found in: {filepath}")
            return False
            
    except Exception as e:
        print(f"✗ Error processing {filepath}: {e}")
        return False

def main():
    # Files that need AdSense
    files_needing_adsense = [
        './plasmacenterfinder_index.html',
        './includes/topic-navigation.html',
        './es/health/index.html',
        './es/centers/index.html',
        './es/process/index.html'
    ]
    
    added_count = 0
    
    for filepath in files_needing_adsense:
        if os.path.exists(filepath):
            if add_adsense_to_file(filepath):
                added_count += 1
        else:
            print(f"✗ File not found: {filepath}")
    
    print(f"\n{'='*50}")
    print(f"Added AdSense to {added_count} files")
    
    # Verify final count
    print("\nVerifying AdSense implementation...")
    total_html = 0
    with_adsense = 0
    
    for root, dirs, files in os.walk('.'):
        # Skip hidden directories and node_modules
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'node_modules']
        
        for file in files:
            if file.endswith('.html'):
                total_html += 1
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        if 'ca-pub-3180649272238451' in f.read():
                            with_adsense += 1
                except:
                    pass
    
    print(f"Total HTML files: {total_html}")
    print(f"Files with AdSense: {with_adsense}")
    print(f"Coverage: {with_adsense/total_html*100:.1f}%")

if __name__ == "__main__":
    main()