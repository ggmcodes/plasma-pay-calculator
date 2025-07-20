#!/usr/bin/env python3
"""
Fix navigation links and add visual improvements throughout the site
"""

import os
import re
from pathlib import Path

def fix_navigation_links():
    """Fix navigation links that redirect to home instead of proper pages"""
    
    files_to_fix = []
    
    # Find all HTML files
    for root, dirs, files in os.walk("/Users/glengomezmeade/Projects/plasma-pay-calculator"):
        # Skip certain directories
        if any(skip_dir in root for skip_dir in ['.git', 'node_modules', '__pycache__']):
            continue
            
        for file in files:
            if file.endswith('.html'):
                files_to_fix.append(os.path.join(root, file))
    
    fixed_count = 0
    
    # Navigation fixes to apply
    navigation_fixes = [
        # Fix states links
        (r'href="/states"(?![\.html])', 'href="/states.html"'),
        (r'href="states"(?![\.html])', 'href="states.html"'),
        (r'href="../states"(?![\.html])', 'href="../states.html"'),
        
        # Fix calculator links
        (r'href="/calculator"(?![/\.])', 'href="/calculator/"'),
        (r'href="../calculator"(?![/\.])', 'href="../calculator/"'),
        
        # Fix centers links
        (r'href="/centers"(?![/\.])', 'href="/centers/"'),
        (r'href="../centers"(?![/\.])', 'href="../centers/"'),
        
        # Fix blog links
        (r'href="/blog"(?![/\.])', 'href="/blog/"'),
        (r'href="../blog"(?![/\.])', 'href="../blog/"'),
        
        # Fix health links
        (r'href="/health"(?![/\.])', 'href="/health/"'),
        (r'href="../health"(?![/\.])', 'href="../health/"'),
    ]
    
    for file_path in files_to_fix:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Apply all navigation fixes
            for pattern, replacement in navigation_fixes:
                content = re.sub(pattern, replacement, content)
            
            # Write back if changed
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                rel_path = os.path.relpath(file_path, "/Users/glengomezmeade/Projects/plasma-pay-calculator")
                print(f"✅ Fixed navigation links in {rel_path}")
                fixed_count += 1
                
        except Exception as e:
            print(f"❌ Error fixing {file_path}: {str(e)}")
    
    return fixed_count

def add_hero_images_to_key_pages():
    """Add hero images to key pages that don't have them"""
    
    pages_to_enhance = [
        {
            "file": "/Users/glengomezmeade/Projects/plasma-pay-calculator/states.html",
            "unsplash_id": "Q_Sei-TqSlc",  # US map
            "title": "Plasma Centers by State"
        },
        {
            "file": "/Users/glengomezmeade/Projects/plasma-pay-calculator/about.html", 
            "unsplash_id": "SJWPKMb9u-k",  # medical/healthcare team
            "title": "About Plasma Pay Calculator"
        },
        {
            "file": "/Users/glengomezmeade/Projects/plasma-pay-calculator/faq.html",
            "unsplash_id": "Lks7vei-eAg",  # FAQ/help
            "title": "Frequently Asked Questions"
        },
        {
            "file": "/Users/glengomezmeade/Projects/plasma-pay-calculator/centers/index.html",
            "unsplash_id": "MJPr6nOdppw",  # medical centers
            "title": "Find Plasma Centers"
        },
        {
            "file": "/Users/glengomezmeade/Projects/plasma-pay-calculator/health/index.html",
            "unsplash_id": "uJ8LNVCBjFQ",  # health/medical
            "title": "Health & Safety Guide"
        }
    ]
    
    enhanced_count = 0
    
    for page in pages_to_enhance:
        if os.path.exists(page["file"]):
            try:
                with open(page["file"], 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Check if already has a hero image
                if 'background-image' not in content or 'hero' not in content.lower():
                    # Find the main content area or first section
                    hero_html = f'''
                    <!-- Hero Section -->
                    <section class="hero" style="background: linear-gradient(rgba(39, 174, 96, 0.8), rgba(46, 204, 113, 0.8)), url('https://images.unsplash.com/{page["unsplash_id"]}/1200x600?auto=format&fit=crop&q=80') center/cover; color: white; padding: 80px 20px; text-align: center; margin-top: 80px;">
                        <div class="container mx-auto max-w-4xl">
                            <h1 style="font-size: 3rem; font-weight: 700; margin-bottom: 1rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">{page["title"]}</h1>
                            <p style="font-size: 1.3rem; opacity: 0.95; max-width: 600px; margin: 0 auto;">Your trusted guide to plasma donation with accurate information and expert insights.</p>
                        </div>
                    </section>
                    '''
                    
                    # Insert after body tag or before main content
                    body_index = content.find('<body')
                    if body_index != -1:
                        body_end = content.find('>', body_index) + 1
                        content = content[:body_end] + hero_html + content[body_end:]
                        
                        with open(page["file"], 'w', encoding='utf-8') as f:
                            f.write(content)
                        
                        rel_path = os.path.relpath(page["file"], "/Users/glengomezmeade/Projects/plasma-pay-calculator")
                        print(f"✅ Added hero image to {rel_path}")
                        enhanced_count += 1
                
            except Exception as e:
                print(f"❌ Error enhancing {page['file']}: {str(e)}")
    
    return enhanced_count

def add_thumbnails_to_blog_posts():
    """Add thumbnail images to individual blog posts"""
    
    blog_dir = "/Users/glengomezmeade/Projects/plasma-pay-calculator/blog"
    
    # Blog post image mappings
    blog_images = {
        "ultimate-plasma-donation-guide.html": "ZiQkhI7417A",
        "which-plasma-center-pays-most-money.html": "MJPr6nOdppw",
        "biolife-vs-csl-plasma-comparison.html": "L8tWZT4CcVQ",
        "csl-plasma-pay-rates-2025.html": "5fNmWej4tAA",
        "first-time-plasma-donation-what-to-expect.html": "SJWPKMb9u-k",
        "highest-paying-plasma-centers-near-me.html": "Q_Sei-TqSlc",
        "plasma-donation-side-effects.html": "uJ8LNVCBjFQ",
        "plasma-donation-tax-guide-2025.html": "KDeab4oW0lY",
        "best-plasma-centers-texas.html": "PHIgYUGQPvU",
        "how-much-money-can-you-make-donating-plasma-2025.html": "Dwheufds-pI",
        "plasma-donation-process-step-by-step.html": "hpjSkU2UYSU",
        "plasma-donation-tips-beginners.html": "Lks7vei-eAg",
        "state-by-state-plasma-donation-laws-regulations-2025.html": "yCdPU73kGSc",
        "complete-medical-eligibility-guide-plasma-donation.html": "L8tWZT4CcVQ",
        "plasma-donation-bonuses-promotions.html": "3iexvMShGfQ",
        "how-to-prepare-for-plasma-donation.html": "bJjsKbToY34",
        "understanding-plasma-medical-uses.html": "qjnAnF0jIGk",
        "plasma-donation-weight-requirements.html": "Zyx1bK9mqmA",
        "can-you-donate-plasma-twice-a-week.html": "SlyCz11RhfY",
        "can-you-donate-plasma-with-tattoos.html": "XgOGw4UHx7A"
    }
    
    enhanced_count = 0
    
    for filename, unsplash_id in blog_images.items():
        file_path = os.path.join(blog_dir, filename)
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Check if already has an article image
                if 'article-image' not in content and 'hero-image' not in content:
                    # Add article header image
                    image_html = f'''
                    <div class="article-image" style="background: url('https://images.unsplash.com/{unsplash_id}/1200x400?auto=format&fit=crop&q=80') center/cover; height: 300px; margin: 2rem 0; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);"></div>
                    '''
                    
                    # Find h1 tag and insert image after it
                    h1_match = re.search(r'<h1[^>]*>.*?</h1>', content)
                    if h1_match:
                        insert_pos = h1_match.end()
                        content = content[:insert_pos] + image_html + content[insert_pos:]
                        
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(content)
                        
                        print(f"✅ Added thumbnail to {filename}")
                        enhanced_count += 1
                
            except Exception as e:
                print(f"❌ Error enhancing {filename}: {str(e)}")
    
    return enhanced_count

def main():
    """Main function"""
    print("🚀 Fixing navigation and adding visual improvements...")
    
    # Fix navigation links
    print("\n🔧 Fixing navigation links...")
    nav_fixes = fix_navigation_links()
    print(f"✅ Fixed navigation in {nav_fixes} files")
    
    # Add hero images to key pages
    print("\n🖼️ Adding hero images to key pages...")
    hero_count = add_hero_images_to_key_pages()
    print(f"✅ Added {hero_count} hero images")
    
    # Add thumbnails to blog posts
    print("\n📸 Adding thumbnails to blog posts...")
    thumb_count = add_thumbnails_to_blog_posts()
    print(f"✅ Added {thumb_count} blog thumbnails")
    
    print(f"\n🎉 Visual improvements complete!")
    print(f"📊 Total enhancements: {nav_fixes + hero_count + thumb_count}")
    print(f"🌟 Site now feels more human and visually appealing")

if __name__ == "__main__":
    main()