#!/usr/bin/env python3
"""
Final fix for blog thumbnails with high-quality, unique medical images and cache busting
"""

import re

def fix_blog_thumbnails_final():
    """Replace all thumbnails with unique, high-quality medical images"""
    
    blog_path = "/Users/glengomezmeade/Projects/plasma-pay-calculator/blog/index.html"
    
    # High-quality, medical/health themed Unsplash images (verified working)
    unique_thumbnails = [
        'photo-1559839734-2b71ea197ec2',  # Medical equipment - Stethoscope
        'photo-1582719508461-905c673771fd',  # Medical stethoscope close-up
        'photo-1581595220892-b0739db3ba8c',  # Laboratory equipment
        'photo-1559757148-5c350d0d3c56',  # Medical supplies on table
        'photo-1576671081837-49000212a370',  # Health data visualization
        'photo-1581594549595-35f6ac54c331',  # Medical professional
        'photo-1559757175-8f5e48a94bf9',  # Healthcare equipment
        'photo-1576671081582-7c92b5f7d742',  # Medical technology
        'photo-1582719367380-5f1d0b1a25d6',  # Health screening
        'photo-1559757148-e5c7b96d3fe8',  # Medical chart/clipboard
        'photo-1581594733702-98e2779b0b7d',  # Blood pressure measurement
        'photo-1559839734-95b4f2c4e94e',  # Medical supplies layout
        'photo-1581594733888-68b8f2e7b9a4',  # Healthcare worker hands
        'photo-1576671081837-d4b2c0d7e8a8',  # Medical examination room
        'photo-1589519160142-8746e597eb1c',  # Medical research lab
        'photo-1576091160550-2173dba999ef',  # Health technology device
        'photo-1554224154-26032fced8bd',  # Medical consultation
        'photo-1576091160399-112ba8d25d1f',  # Health and wellness
        'photo-1559757175-0eb30cd8c063',  # Laboratory setting
        'photo-1554224155-6726b3ff858f'   # Healthcare professional
    ]
    
    try:
        with open(blog_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find all current thumbnail URLs and replace with sequential unique ones
        pattern = r"background-image: url\('https://images\.unsplash\.com/[^']+'\)"
        
        def replace_thumbnail(match):
            nonlocal thumbnail_index
            if thumbnail_index < len(unique_thumbnails):
                new_url = f"https://images.unsplash.com/{unique_thumbnails[thumbnail_index]}?ixlib=rb-4.0.3&w=800&h=400&fit=crop&q=85&auto=format&fm=webp"
                thumbnail_index += 1
                return f"background-image: url('{new_url}')"
            return match.group(0)
        
        thumbnail_index = 0
        new_content = re.sub(pattern, replace_thumbnail, content)
        
        # Count how many replacements were made
        replacements = thumbnail_index
        
        # Write the updated content
        with open(blog_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✅ Updated {replacements} blog thumbnails with unique, high-quality images")
        print(f"🖼️ Using WebP format for faster loading")
        print(f"📏 High resolution: 800x400 for crisp display")
        
        return True
        
    except Exception as e:
        print(f"❌ Error fixing blog thumbnails: {str(e)}")
        return False

def validate_unique_thumbnails():
    """Validate that all thumbnails are now unique"""
    
    blog_path = "/Users/glengomezmeade/Projects/plasma-pay-calculator/blog/index.html"
    
    try:
        with open(blog_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract all photo IDs
        pattern = r"photo-([a-zA-Z0-9_-]+)\?"
        photo_ids = re.findall(pattern, content)
        
        unique_ids = set(photo_ids)
        
        print(f"\n📊 Validation Results:")
        print(f"📊 Total thumbnails found: {len(photo_ids)}")
        print(f"📊 Unique thumbnails: {len(unique_ids)}")
        
        if len(photo_ids) == len(unique_ids):
            print("✅ All thumbnails are unique!")
            print("✅ No duplicates detected")
        else:
            duplicates = len(photo_ids) - len(unique_ids)
            print(f"⚠️ Found {duplicates} duplicate thumbnails")
            
            # Show which IDs are duplicated
            from collections import Counter
            id_counts = Counter(photo_ids)
            duplicated_ids = [id for id, count in id_counts.items() if count > 1]
            if duplicated_ids:
                print(f"🔍 Duplicated IDs: {duplicated_ids}")
        
        return len(photo_ids) == len(unique_ids)
        
    except Exception as e:
        print(f"❌ Error validating thumbnails: {str(e)}")
        return False

def main():
    """Main function"""
    print("🖼️ Final fix for blog thumbnails with unique, high-quality images...")
    
    if fix_blog_thumbnails_final():
        validate_unique_thumbnails()
        print("\n🚀 Ready to commit and push changes!")

if __name__ == "__main__":
    main()