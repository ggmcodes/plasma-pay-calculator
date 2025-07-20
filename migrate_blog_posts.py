#!/usr/bin/env python3
"""
Migrate blog posts from BestPlasmaCenters to PlasmaPayCalculator
"""

import os
import re
import shutil
from pathlib import Path
from datetime import datetime

# Source and destination paths
SOURCE_BLOG_DIR = "/Users/glengomezmeade/Projects/bestplasmacenters/public/blog"
DEST_BLOG_DIR = "/Users/glengomezmeade/Projects/plasma-pay-calculator/blog"

def transform_blog_content(content, filename):
    """Transform blog content for PlasmaPayCalculator branding"""
    
    # Update site branding
    content = re.sub(r'Best Plasma Centers', 'Plasma Pay Calculator', content, flags=re.IGNORECASE)
    content = re.sub(r'bestplasmacenters\.com', 'plasmapaycalculator.com', content)
    
    # Update meta tags and titles
    content = re.sub(
        r'<title>([^<]+)</title>',
        lambda m: f'<title>{m.group(1).replace("Best Plasma Centers", "Plasma Pay Calculator")}</title>',
        content
    )
    
    # Update meta descriptions
    content = re.sub(
        r'<meta name="description" content="([^"]+)"',
        lambda m: f'<meta name="description" content="{m.group(1).replace("Best Plasma Centers", "Plasma Pay Calculator").replace("best plasma centers", "plasma pay calculator")}"',
        content,
        flags=re.IGNORECASE
    )
    
    # Update navigation to match PPC structure
    nav_replacement = '''<nav class="hidden md:flex items-center space-x-8">
                <a href="/calculator/" class="text-gray-600 hover:text-gray-900 font-medium transition-colors">Calculator</a>
                <a href="/blog/" class="text-gray-600 hover:text-gray-900 font-medium transition-colors">Blog</a>
                <a href="/states.html" class="text-gray-600 hover:text-gray-900 font-medium transition-colors">States</a>
                <a href="/centers/" class="text-gray-600 hover:text-gray-900 font-medium transition-colors">Centers</a>
                <a href="/health/" class="text-gray-600 hover:text-gray-900 font-medium transition-colors">Health</a>
                <a href="/faq.html" class="text-gray-600 hover:text-gray-900 font-medium transition-colors">FAQ</a>
            </nav>'''
    
    # Replace navigation
    content = re.sub(
        r'<nav class="hidden md:flex items-center space-x-8">.*?</nav>',
        nav_replacement,
        content,
        flags=re.DOTALL
    )
    
    # Update all "find centers" links to point to /centers/
    content = re.sub(
        r'href="[^"]*bestplasmacenters\.com[^"]*"[^>]*>([^<]*(?:find|center|location)[^<]*)</a>',
        r'href="/centers/" target="_blank">\1</a>',
        content,
        flags=re.IGNORECASE
    )
    
    # Update internal blog links to use relative paths
    content = re.sub(
        r'href="https://bestplasmacenters\.com/blog/([^"]+)"',
        r'href="/blog/\1"',
        content
    )
    
    # Update internal links to use PPC structure
    content = re.sub(
        r'href="https://bestplasmacenters\.com/state/([^/]+)/([^"]+)"',
        r'href="/calculators/\1/\2"',
        content
    )
    
    # Update CSS paths if needed
    content = re.sub(r'/styles\.css', '/styles.css', content)
    
    # Update color scheme to match PPC
    content = re.sub(r'#e74c3c', '#27ae60', content)  # Red to green
    content = re.sub(r'#c0392b', '#1e8449', content)  # Dark red to dark green
    
    # Update footer branding
    content = re.sub(
        r'© \d{4} Best Plasma Centers',
        f'© {datetime.now().year} Plasma Pay Calculator',
        content
    )
    
    # Update any remaining absolute URLs
    content = re.sub(
        r'https://bestplasmacenters\.com/',
        '/',
        content
    )
    
    print(f"✅ Transformed content for {filename}")
    return content

def migrate_blog_posts():
    """Migrate all blog posts from BPC to PPC"""
    
    # Ensure destination directory exists
    os.makedirs(DEST_BLOG_DIR, exist_ok=True)
    
    # Get list of blog posts to migrate
    blog_files = []
    for file in os.listdir(SOURCE_BLOG_DIR):
        if file.endswith('.html') and not file.endswith('.backup'):
            blog_files.append(file)
    
    print(f"🚀 Starting migration of {len(blog_files)} blog posts...")
    
    migrated_count = 0
    
    for blog_file in sorted(blog_files):
        source_path = os.path.join(SOURCE_BLOG_DIR, blog_file)
        dest_path = os.path.join(DEST_BLOG_DIR, blog_file)
        
        # Skip if already exists on PPC
        if os.path.exists(dest_path):
            print(f"⚠️  Skipping {blog_file} - already exists on PPC")
            continue
        
        try:
            # Read source content
            with open(source_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Transform content
            transformed_content = transform_blog_content(content, blog_file)
            
            # Write to destination
            with open(dest_path, 'w', encoding='utf-8') as f:
                f.write(transformed_content)
            
            migrated_count += 1
            print(f"✅ Migrated: {blog_file}")
            
        except Exception as e:
            print(f"❌ Error migrating {blog_file}: {str(e)}")
    
    print(f"\n🎉 Migration complete! Migrated {migrated_count} blog posts to PlasmaPayCalculator")
    return migrated_count

def main():
    """Main function"""
    print("🚀 Starting blog post migration from BestPlasmaCenters to PlasmaPayCalculator...")
    
    # Check if source directory exists
    if not os.path.exists(SOURCE_BLOG_DIR):
        print(f"❌ Source blog directory not found: {SOURCE_BLOG_DIR}")
        return
    
    # Migrate blog posts
    migrated_count = migrate_blog_posts()
    
    print(f"\n✅ Blog migration completed!")
    print(f"📊 Total posts migrated: {migrated_count}")
    print(f"📁 Destination: {DEST_BLOG_DIR}")

if __name__ == "__main__":
    main()