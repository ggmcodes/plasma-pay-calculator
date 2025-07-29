#!/usr/bin/env python3
"""
Remove all manual AdSense ad blocks from HTML files.
Keeps the Auto Ads script in <head> but removes manual <ins> ad blocks.
"""

import os
import re
from pathlib import Path

def remove_adsense_blocks(content):
    """Remove manual AdSense ad blocks from HTML content."""
    
    # Pattern to match complete AdSense ad blocks including surrounding div/comments
    patterns = [
        # Match <!-- Ad Space --> comments and their content
        r'<!--\s*[Aa]d[^>]*-->\s*<div[^>]*>.*?</div>',
        
        # Match AdSense ins blocks with optional surrounding divs
        r'<div[^>]*>\s*<ins\s+class="adsbygoogle"[^>]*>.*?</ins>\s*<script[^>]*>\s*\(adsbygoogle[^}]*}\);\s*</script>\s*</div>',
        
        # Match standalone ins blocks
        r'<ins\s+class="adsbygoogle"[^>]*>.*?</ins>\s*<script[^>]*>\s*\(adsbygoogle[^}]*}\);\s*</script>',
        
        # Match div containers with "ad-space" class or style
        r'<div[^>]*class="ad-space"[^>]*>.*?</div>',
        
        # Match div containers with advertisement text
        r'<div[^>]*>\s*<p>\s*Advertisement\s*</p>\s*</div>',
        
        # Match high-value header ad comments and blocks
        r'<!--\s*High-Value Header Ad\s*-->\s*<div[^>]*>.*?</div>',
    ]
    
    # Apply all patterns with DOTALL flag to match across newlines
    for pattern in patterns:
        content = re.sub(pattern, '', content, flags=re.DOTALL | re.IGNORECASE)
    
    # Clean up multiple consecutive empty lines
    content = re.sub(r'\n\s*\n\s*\n+', '\n\n', content)
    
    return content

def process_file(file_path):
    """Process a single HTML file to remove AdSense blocks."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            original_content = f.read()
        
        # Skip if no AdSense blocks found
        if not any(keyword in original_content.lower() for keyword in ['adsbygoogle', 'data-ad-slot', 'ad-space', 'advertisement']):
            return False
        
        cleaned_content = remove_adsense_blocks(original_content)
        
        # Only write if content changed
        if cleaned_content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(cleaned_content)
            return True
        
        return False
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    """Remove AdSense blocks from all HTML files in the project."""
    base_dir = Path('/Users/glengomezmeade/plasma-pay-calculator')
    
    # Find all HTML files
    html_files = list(base_dir.rglob('*.html'))
    
    print(f"Found {len(html_files)} HTML files to process...")
    
    modified_count = 0
    modified_files = []
    
    for file_path in html_files:
        if process_file(file_path):
            modified_count += 1
            modified_files.append(str(file_path.relative_to(base_dir)))
            print(f"✅ Cleaned AdSense blocks from: {file_path.relative_to(base_dir)}")
    
    print(f"\n🎉 Processing complete!")
    print(f"📊 Modified {modified_count} files out of {len(html_files)} total files")
    
    if modified_files:
        print(f"\n📝 Files with AdSense blocks removed:")
        for file in modified_files[:10]:  # Show first 10
            print(f"   • {file}")
        if len(modified_files) > 10:
            print(f"   • ... and {len(modified_files) - 10} more files")
    
    print(f"\n✨ All manual AdSense ad blocks removed!")
    print(f"🚀 Auto Ads script in <head> tags preserved for automatic ad placement")

if __name__ == "__main__":
    main()