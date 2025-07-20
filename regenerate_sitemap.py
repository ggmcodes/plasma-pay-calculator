#!/usr/bin/env python3
"""
Regenerate sitemap.xml with proper structure and all content
"""

import os
import re
from pathlib import Path
from datetime import datetime

def get_all_html_files():
    """Find all HTML files that should be in sitemap"""
    
    base_dir = "/Users/glengomezmeade/Projects/plasma-pay-calculator"
    html_files = []
    
    # Find all HTML files recursively
    for root, dirs, files in os.walk(base_dir):
        # Skip certain directories
        skip_dirs = {'.git', 'node_modules', '__pycache__', '.DS_Store'}
        dirs[:] = [d for d in dirs if d not in skip_dirs]
        
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, base_dir)
                html_files.append(rel_path)
    
    return sorted(html_files)

def path_to_url(file_path):
    """Convert file path to URL"""
    
    base_url = "https://plasmapaycalculator.com"
    
    # Handle index.html files
    if file_path.endswith('/index.html'):
        url_path = file_path[:-11]  # Remove '/index.html'
        if url_path == '':
            return f"{base_url}/"
        else:
            return f"{base_url}/{url_path}/"
    
    # Handle regular HTML files
    elif file_path.endswith('.html'):
        url_path = file_path[:-5]  # Remove '.html'
        return f"{base_url}/{url_path}.html"
    
    return None

def get_priority_and_changefreq(file_path):
    """Determine priority and change frequency based on file type"""
    
    if file_path == 'index.html':
        return '1.0', 'daily'
    elif file_path in ['states.html', 'centers/index.html', 'blog/index.html']:
        return '0.9', 'weekly'
    elif file_path.startswith('calculators/') and not '/' in file_path[12:]:
        # State calculator pages
        return '0.8', 'monthly'
    elif file_path.startswith('calculators/'):
        # City calculator pages
        return '0.7', 'monthly'
    elif file_path.startswith('blog/') and file_path != 'blog/index.html':
        # Blog posts
        return '0.6', 'monthly'
    elif file_path in ['about.html', 'faq.html', 'contact.html', 'privacy.html', 'terms.html']:
        # Static pages
        return '0.5', 'quarterly'
    else:
        return '0.6', 'monthly'

def generate_sitemap():
    """Generate complete sitemap.xml"""
    
    current_date = datetime.now().strftime('%Y-%m-%d')
    
    # Get all HTML files
    html_files = get_all_html_files()
    
    # Start sitemap XML
    sitemap_content = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
'''
    
    url_count = 0
    
    for file_path in html_files:
        url = path_to_url(file_path)
        if not url:
            continue
            
        priority, changefreq = get_priority_and_changefreq(file_path)
        
        # Add URL entry
        sitemap_content += f'''  <url>
    <loc>{url}</loc>
    <lastmod>{current_date}</lastmod>
    <changefreq>{changefreq}</changefreq>
    <priority>{priority}</priority>
'''
        
        # Add hreflang for pages with Spanish versions
        if file_path in ['index.html', 'about.html', 'faq.html', 'blog/index.html']:
            es_url = url.replace('plasmapaycalculator.com/', 'plasmapaycalculator.com/es/')
            sitemap_content += f'''    <xhtml:link rel="alternate" hreflang="es" href="{es_url}" />
    <xhtml:link rel="alternate" hreflang="en" href="{url}" />
'''
        
        sitemap_content += '  </url>\n\n'
        url_count += 1
    
    # Close sitemap
    sitemap_content += '</urlset>'
    
    return sitemap_content, url_count

def main():
    """Main function to regenerate sitemap"""
    print("🗺️ Regenerating sitemap.xml...")
    
    try:
        sitemap_content, url_count = generate_sitemap()
        
        # Write new sitemap
        sitemap_path = "/Users/glengomezmeade/Projects/plasma-pay-calculator/sitemap.xml"
        
        # Backup original
        if os.path.exists(sitemap_path):
            backup_path = f"{sitemap_path}.backup"
            os.rename(sitemap_path, backup_path)
            print(f"📋 Backed up original sitemap to {backup_path}")
        
        # Write new sitemap
        with open(sitemap_path, 'w', encoding='utf-8') as f:
            f.write(sitemap_content)
        
        print(f"✅ Generated new sitemap with {url_count} URLs")
        print(f"📊 Sitemap saved to: {sitemap_path}")
        
        # Validate XML structure
        if '</urlset>' in sitemap_content and '<?xml' in sitemap_content:
            print("✅ XML structure validation passed")
        else:
            print("❌ XML structure validation failed")
            
        return True
        
    except Exception as e:
        print(f"❌ Error regenerating sitemap: {str(e)}")
        return False

if __name__ == "__main__":
    main()