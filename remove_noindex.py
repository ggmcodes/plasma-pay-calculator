#!/usr/bin/env python3

import os
import re

def remove_noindex_from_file(filepath):
    """Remove noindex meta tag from a single file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove noindex, nofollow meta tags
    patterns = [
        r'<meta content="noindex, nofollow" name="robots"/>\n?',
        r'<meta content="noindex, nofollow" name="robots">\n?',
        r'<meta name="robots" content="noindex, nofollow"/>\n?',
        r'<meta name="robots" content="noindex, nofollow">\n?',
        r'<meta content="noindex" name="robots"/>\n?',
        r'<meta content="noindex" name="robots">\n?',
        r'<meta name="robots" content="noindex"/>\n?',
        r'<meta name="robots" content="noindex">\n?'
    ]
    
    modified = False
    for pattern in patterns:
        if re.search(pattern, content):
            content = re.sub(pattern, '', content)
            modified = True
    
    if modified:
        # Add index, follow meta tag instead
        if 'name="robots"' not in content:
            # Find the head section and add the meta tag
            head_match = re.search(r'</title>', content)
            if head_match:
                insert_pos = head_match.end()
                content = content[:insert_pos] + '\n<meta name="robots" content="index, follow">' + content[insert_pos:]
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    
    return False

def main():
    """Remove noindex tags from all HTML files"""
    root_dir = '/Users/glengomezmeade/Projects/plasma-pay-calculator'
    modified_count = 0
    
    # Find all HTML files with noindex
    for root, dirs, files in os.walk(root_dir):
        # Skip hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                
                # Check if file contains noindex
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        if 'noindex' in f.read():
                            if remove_noindex_from_file(filepath):
                                rel_path = os.path.relpath(filepath, root_dir)
                                print(f"Removed noindex from: {rel_path}")
                                modified_count += 1
                except Exception as e:
                    print(f"Error processing {filepath}: {e}")
    
    print(f"\nTotal files modified: {modified_count}")
    print("All noindex tags have been removed and replaced with 'index, follow'")

if __name__ == '__main__':
    main()