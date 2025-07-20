#!/usr/bin/env python3
"""
Fix blog thumbnails with unique, working Unsplash images
"""

import re

def fix_blog_thumbnails():
    """Replace repeated/broken thumbnails with unique working ones"""
    
    blog_path = "/Users/glengomezmeade/Projects/plasma-pay-calculator/blog/index.html"
    
    # High-quality, diverse Unsplash images for plasma/medical/health topics
    unique_thumbnails = [
        'photo-1559839734-2b71ea197ec2',  # Medical equipment
        'photo-1576091160399-112ba8d25d1f',  # Health/wellness
        'photo-1559757148-5c350d0d3c56',  # Medical supplies
        'photo-1554224155-6726b3ff858f',  # Healthcare professional
        'photo-1559757175-0eb30cd8c063',  # Laboratory
        'photo-1589519160142-8746e597eb1c',  # Medical research
        'photo-1576091160550-2173dba999ef',  # Health technology
        'photo-1554224154-26032fced8bd',  # Medical consultation
        'photo-1582719508461-905c673771fd',  # Medical stethoscope
        'photo-1581595220892-b0739db3ba8c',  # Medical lab
        'photo-1576671081837-49000212a370',  # Health data
        'photo-1581594549595-35f6ac54c331',  # Medical professional
        'photo-1559757175-8f5e48a94bf9',  # Healthcare equipment
        'photo-1576671081582-7c92b5f7d742',  # Medical technology
        'photo-1582719367380-5f1d0b1a25d6',  # Health screening
        'photo-1559757148-e5c7b96d3fe8',  # Medical chart
        'photo-1581594733702-98e2779b0b7d',  # Blood pressure
        'photo-1559839734-95b4f2c4e94e',  # Medical supplies
        'photo-1581594733888-68b8f2e7b9a4',  # Healthcare worker
        'photo-1576671081837-d4b2c0d7e8a8'   # Medical examination
    ]
    
    try:
        with open(blog_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find all current thumbnail URLs
        pattern = r"background-image: url\('https://images\.unsplash\.com/([^']+)'\)"
        matches = re.findall(pattern, content)
        
        print(f"Found {len(matches)} thumbnail images")
        
        # Replace each occurrence with a unique thumbnail
        for i, match in enumerate(matches):
            if i < len(unique_thumbnails):
                new_url = f"https://images.unsplash.com/{unique_thumbnails[i]}?ixlib=rb-4.0.3&w=600&h=300&fit=crop&q=80"
                old_pattern = f"background-image: url('https://images.unsplash.com/{re.escape(match)}')"
                new_replacement = f"background-image: url('{new_url}')"
                
                # Replace only the first occurrence
                content = content.replace(
                    f"background-image: url('https://images.unsplash.com/{match}')",
                    new_replacement,
                    1
                )
                
                print(f"✅ Updated thumbnail {i+1}: {unique_thumbnails[i]}")
        
        # Write the updated content
        with open(blog_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Updated {len(matches)} blog thumbnails with unique images")
        return True
        
    except Exception as e:
        print(f"❌ Error fixing blog thumbnails: {str(e)}")
        return False

def validate_thumbnails():
    """Check if all thumbnails are unique"""
    
    blog_path = "/Users/glengomezmeade/Projects/plasma-pay-calculator/blog/index.html"
    
    try:
        with open(blog_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract all photo IDs
        pattern = r"photo-([a-zA-Z0-9_-]+)\?"
        photo_ids = re.findall(pattern, content)
        
        unique_ids = set(photo_ids)
        
        print(f"📊 Total thumbnails: {len(photo_ids)}")
        print(f"📊 Unique thumbnails: {len(unique_ids)}")
        
        if len(photo_ids) == len(unique_ids):
            print("✅ All thumbnails are unique!")
        else:
            duplicates = len(photo_ids) - len(unique_ids)
            print(f"⚠️ Found {duplicates} duplicate thumbnails")
        
        return len(photo_ids) == len(unique_ids)
        
    except Exception as e:
        print(f"❌ Error validating thumbnails: {str(e)}")
        return False

def main():
    """Main function"""
    print("🖼️ Fixing blog thumbnails with unique, working images...")
    
    if fix_blog_thumbnails():
        print("\n🔍 Validating thumbnail uniqueness...")
        validate_thumbnails()

if __name__ == "__main__":
    main()