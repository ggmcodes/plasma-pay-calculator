#!/usr/bin/env python3
"""
Fix broken Unsplash thumbnail images on blog index page
"""

import os
import re

def fix_unsplash_urls():
    """Fix malformed Unsplash URLs in blog index"""
    
    blog_index_path = "/Users/glengomezmeade/Projects/plasma-pay-calculator/blog/index.html"
    
    # Mapping of broken IDs to proper Unsplash photo IDs
    url_fixes = {
        'ZiQkhI7417A': 'photo-1559839734-2b71ea197ec2',  # Medical/health
        'MJPr6nOdppw': 'photo-1576091160399-112ba8d25d1f',  # Business/money
        'L8tWZT4CcVQ': 'photo-1559757148-5c350d0d3c56',  # Medical equipment
        '5fNmWej4tAA': 'photo-1554224155-6726b3ff858f',  # Business/finance
        'SJWPKMb9u-k': 'photo-1559757175-0eb30cd8c063',  # Healthcare
        'Q_Sei-TqSlc': 'photo-1589519160142-8746e597eb1c',  # Medical center
        'uJ8LNVCBjFQ': 'photo-1576091160550-2173dba999ef',  # Health safety
        'KDeab4oW0lY': 'photo-1554224154-26032fced8bd',  # Tax/legal documents
        'PHIgYUGQPvU': 'photo-1559757148-5c350d0d3c56',  # Texas theme
        'Dwheufds-pI': 'photo-1559839734-2b71ea197ec2',  # Money/earnings
        'hpjSkU2UYSU': 'photo-1576091160399-112ba8d25d1f',  # Process guide
        'Lks7vei-eAg': 'photo-1559757175-0eb30cd8c063',  # Tips/advice
        'yCdPU73kGSc': 'photo-1554224155-6726b3ff858f',  # Legal/regulations
        '3iexvMShGfQ': 'photo-1589519160142-8746e597eb1c',  # Bonuses/promotions
        'bJjsKbToY34': 'photo-1576091160550-2173dba999ef',  # Preparation
        'qjnAnF0jIGk': 'photo-1559839734-2b71ea197ec2',  # Medical uses
        'Zyx1bK9mqmA': 'photo-1554224154-26032fced8bd',  # Weight requirements
        'SlyCz11RhfY': 'photo-1559757148-5c350d0d3c56',  # Frequency guide
        'XgOGw4UHx7A': 'photo-1576091160399-112ba8d25d1f',  # Tattoo eligibility
    }
    
    try:
        with open(blog_index_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        fixes_made = 0
        
        # Fix each broken URL
        for broken_id, correct_id in url_fixes.items():
            # Pattern to match the broken URL
            pattern = f"https://images\\.unsplash\\.com/{broken_id}/600x300\\?auto=format&fit=crop&q=80"
            replacement = f"https://images.unsplash.com/{correct_id}?ixlib=rb-4.0.3&w=600&h=300&fit=crop&q=80"
            
            if pattern.replace('\\', '') in content:
                content = re.sub(pattern, replacement, content)
                fixes_made += 1
                print(f"✅ Fixed {broken_id} → {correct_id}")
        
        # Also fix the 800x400 image
        content = re.sub(
            r"https://images\.unsplash\.com/ZiQkhI7417A/800x400\?auto=format&fit=crop&q=80",
            "https://images.unsplash.com/photo-1559839734-2b71ea197ec2?ixlib=rb-4.0.3&w=800&h=400&fit=crop&q=80",
            content
        )
        
        if content != original_content:
            with open(blog_index_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✅ Fixed {fixes_made} thumbnail images in blog index")
            return True
        else:
            print("ℹ️ No thumbnail fixes needed")
            return False
            
    except Exception as e:
        print(f"❌ Error fixing thumbnails: {str(e)}")
        return False

def main():
    """Main function to fix blog thumbnails"""
    print("🖼️ Fixing blog thumbnail images...")
    
    if fix_unsplash_urls():
        print("🎉 Blog thumbnails fixed successfully!")
    else:
        print("ℹ️ No changes needed for blog thumbnails")

if __name__ == "__main__":
    main()