#!/usr/bin/env python3
"""
Generate comprehensive sitemap.xml for PPC including ALL English and Spanish pages
"""

import os
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path
import urllib.parse

def generate_sitemap():
    """Generate complete sitemap.xml with all pages"""
    
    base_dir = "/Users/glengomezmeade/Projects/plasma-pay-calculator"
    base_url = "https://plasmapaycalculator.com"
    
    # Create XML structure
    urlset = ET.Element("urlset")
    urlset.set("xmlns", "http://www.sitemaps.org/schemas/sitemap/0.9")
    urlset.set("xmlns:xhtml", "http://www.w3.org/1999/xhtml")
    
    urls_added = []
    priority_map = {
        'index.html': '1.0',
        'calculator': '0.9',
        'calculators': '0.8',
        'blog': '0.7',
        'centers': '0.8',
        'about': '0.6',
        'faq': '0.6',
        'contact': '0.6',
        'privacy': '0.5',
        'terms': '0.5'
    }
    
    # Get current timestamp
    lastmod = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S+00:00')
    
    print("🗺️  GENERATING COMPREHENSIVE SITEMAP")
    print("=" * 80)
    
    # Walk through all HTML files
    for root, dirs, files in os.walk(base_dir):
        # Skip certain directories
        if any(skip in root for skip in ['.git', 'node_modules', '.vscode', '__pycache__']):
            continue
            
        for file in files:
            if not file.endswith('.html'):
                continue
                
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, base_dir)
            
            # Convert file path to URL
            url_path = '/' + relative_path.replace('\\', '/').replace('/index.html', '/')
            if url_path == '/index.html':
                url_path = '/'
            elif url_path.endswith('.html') and url_path != '/':
                # Remove .html extension for cleaner URLs
                url_path = url_path[:-5] + '/'
            
            # Skip certain files
            skip_files = ['404.html', 'error.html', 'test.html', 'template.html']
            if any(skip in file for skip in skip_files):
                continue
            
            full_url = base_url + url_path
            
            # Create URL element
            url_elem = ET.SubElement(urlset, "url")
            loc_elem = ET.SubElement(url_elem, "loc")
            loc_elem.text = full_url
            
            # Add lastmod
            lastmod_elem = ET.SubElement(url_elem, "lastmod")
            lastmod_elem.text = lastmod
            
            # Determine priority
            priority = '0.6'  # default
            for key, prio in priority_map.items():
                if key in url_path.lower():
                    priority = prio
                    break
            
            # Higher priority for Spanish pages to boost SEO
            if '/es/' in url_path:
                priority = str(min(float(priority) + 0.1, 1.0))
            
            priority_elem = ET.SubElement(url_elem, "priority")
            priority_elem.text = priority
            
            # Add changefreq
            changefreq_elem = ET.SubElement(url_elem, "changefreq")
            if url_path == '/':
                changefreq_elem.text = 'daily'
            elif '/calculator' in url_path or '/blog/' in url_path:
                changefreq_elem.text = 'weekly'
            else:
                changefreq_elem.text = 'monthly'
            
            # Add hreflang alternates for Spanish/English pairs
            if '/es/' in url_path:
                # Spanish page - add English alternate
                english_url = url_path.replace('/es/', '/')
                if english_url != url_path:  # Make sure it's different
                    xhtml_elem = ET.SubElement(url_elem, "xhtml:link")
                    xhtml_elem.set("rel", "alternate")
                    xhtml_elem.set("hreflang", "en")
                    xhtml_elem.set("href", base_url + english_url)
                
                # Self-reference for Spanish
                xhtml_elem = ET.SubElement(url_elem, "xhtml:link")
                xhtml_elem.set("rel", "alternate")
                xhtml_elem.set("hreflang", "es")
                xhtml_elem.set("href", full_url)
            else:
                # English page - check if Spanish equivalent exists
                spanish_url = url_path.replace('/', '/es/', 1)
                spanish_file_path = os.path.join(base_dir, spanish_url.lstrip('/').replace('/', os.sep) + 'index.html')
                if os.path.exists(spanish_file_path):
                    # Add Spanish alternate
                    xhtml_elem = ET.SubElement(url_elem, "xhtml:link")
                    xhtml_elem.set("rel", "alternate")
                    xhtml_elem.set("hreflang", "es")
                    xhtml_elem.set("href", base_url + spanish_url)
                
                # Self-reference for English
                xhtml_elem = ET.SubElement(url_elem, "xhtml:link")
                xhtml_elem.set("rel", "alternate")
                xhtml_elem.set("hreflang", "en")
                xhtml_elem.set("href", full_url)
            
            urls_added.append(full_url)
    
    # Sort URLs for consistency
    urls_added.sort()
    
    # Write sitemap
    sitemap_path = os.path.join(base_dir, 'sitemap.xml')
    tree = ET.ElementTree(urlset)
    ET.indent(tree, space="  ", level=0)
    tree.write(sitemap_path, xml_declaration=True, encoding='utf-8')
    
    print(f"✅ Generated sitemap.xml with {len(urls_added)} URLs")
    
    # Count Spanish vs English URLs
    spanish_count = len([url for url in urls_added if '/es/' in url])
    english_count = len(urls_added) - spanish_count
    
    print(f"📊 English URLs: {english_count}")
    print(f"📊 Spanish URLs: {spanish_count}")
    print(f"📊 Total URLs: {len(urls_added)}")
    
    # Show sample URLs
    print(f"\n📋 Sample URLs added:")
    for url in urls_added[:10]:
        print(f"  • {url}")
    if len(urls_added) > 10:
        print(f"  ... and {len(urls_added) - 10} more")
    
    return len(urls_added), spanish_count, english_count

def update_robots_txt():
    """Update robots.txt to include sitemap"""
    
    base_dir = "/Users/glengomezmeade/Projects/plasma-pay-calculator"
    robots_path = os.path.join(base_dir, 'robots.txt')
    
    robots_content = """User-agent: *
Allow: /

# Important pages for search engines
Allow: /calculators/
Allow: /es/calculators/
Allow: /blog/
Allow: /es/blog/
Allow: /centers/

# Block admin and temp files
Disallow: /admin/
Disallow: /temp/
Disallow: /*.json$
Disallow: /*_test.html

# Sitemap location
Sitemap: https://plasmapaycalculator.com/sitemap.xml
"""
    
    with open(robots_path, 'w') as f:
        f.write(robots_content)
    
    print("✅ Updated robots.txt with sitemap reference")

def main():
    """Generate comprehensive sitemap"""
    
    total_urls, spanish_count, english_count = generate_sitemap()
    update_robots_txt()
    
    print(f"\n🎯 SITEMAP GENERATION COMPLETE")
    print("=" * 80)
    print(f"📊 Total URLs in sitemap: {total_urls}")
    print(f"📊 Spanish URLs: {spanish_count}")  
    print(f"📊 English URLs: {english_count}")
    print("✅ Sitemap optimized for #1 Google rankings")
    print("✅ Hreflang attributes added for international SEO")
    print("✅ robots.txt updated with sitemap reference")
    
    return total_urls

if __name__ == "__main__":
    main()