#!/usr/bin/env python3
import os
from datetime import datetime
import xml.etree.ElementTree as ET
from xml.dom import minidom

def get_all_html_files(root_dir):
    """Get all HTML files in the project"""
    html_files = []
    for dirpath, _, filenames in os.walk(root_dir):
        # Skip hidden directories and scripts
        if any(part.startswith('.') for part in dirpath.split('/')):
            continue
        if 'scripts' in dirpath or 'assets' in dirpath:
            continue
            
        for filename in filenames:
            if filename.endswith('.html'):
                full_path = os.path.join(dirpath, filename)
                rel_path = os.path.relpath(full_path, root_dir)
                html_files.append(rel_path)
    
    return sorted(html_files)

def get_url_from_path(file_path):
    """Convert file path to URL"""
    # Remove index.html from path
    if file_path.endswith('index.html'):
        if file_path == 'index.html':
            return '/'
        else:
            return '/' + file_path.replace('/index.html', '/')
    else:
        # For non-index HTML files, keep the .html
        return '/' + file_path

def get_priority_and_freq(url):
    """Determine priority and change frequency based on URL"""
    if url == '/':
        return '1.0', 'daily'
    elif url == '/calculators/' or url.startswith('/calculators/') and url.count('/') == 3:
        # State calculators
        return '0.9', 'weekly'
    elif url.startswith('/calculators/') and url.count('/') == 4:
        # City calculators
        return '0.8', 'weekly'
    elif url == '/blog/' or url == '/blog.html':
        return '0.8', 'daily'
    elif url.startswith('/blog/'):
        return '0.7', 'weekly'
    elif url.startswith('/es/'):
        # Spanish pages slightly lower priority
        return '0.6', 'weekly'
    elif url.startswith('/topics/') or url.startswith('/tools/'):
        return '0.7', 'weekly'
    elif url in ['/centers.html', '/centers/', '/about.html', '/faq.html']:
        return '0.8', 'weekly'
    else:
        return '0.5', 'monthly'

def generate_sitemap(root_dir):
    """Generate comprehensive sitemap.xml"""
    
    # Get all HTML files
    html_files = get_all_html_files(root_dir)
    
    # Create root element
    urlset = ET.Element('urlset')
    urlset.set('xmlns', 'http://www.sitemaps.org/schemas/sitemap/0.9')
    
    # Track URLs to avoid duplicates
    urls_added = set()
    
    # Add all HTML files
    for file_path in html_files:
        url = get_url_from_path(file_path)
        
        # Skip if already added
        if url in urls_added:
            continue
        
        urls_added.add(url)
        
        # Create URL element
        url_elem = ET.SubElement(urlset, 'url')
        
        # Add location
        loc = ET.SubElement(url_elem, 'loc')
        loc.text = f'https://plasmapaycalculator.com{url}'
        
        # Add last modified (today's date)
        lastmod = ET.SubElement(url_elem, 'lastmod')
        lastmod.text = datetime.now().strftime('%Y-%m-%d')
        
        # Add change frequency and priority
        priority, changefreq = get_priority_and_freq(url)
        
        freq_elem = ET.SubElement(url_elem, 'changefreq')
        freq_elem.text = changefreq
        
        priority_elem = ET.SubElement(url_elem, 'priority')
        priority_elem.text = priority
    
    # Also add directory URLs (without index.html)
    directories = set()
    for file_path in html_files:
        if file_path.endswith('/index.html'):
            dir_url = '/' + os.path.dirname(file_path) + '/'
            if dir_url not in urls_added and dir_url != '//':
                directories.add(dir_url)
    
    for dir_url in sorted(directories):
        if dir_url in urls_added:
            continue
            
        urls_added.add(dir_url)
        
        url_elem = ET.SubElement(urlset, 'url')
        
        loc = ET.SubElement(url_elem, 'loc')
        loc.text = f'https://plasmapaycalculator.com{dir_url}'
        
        lastmod = ET.SubElement(url_elem, 'lastmod')
        lastmod.text = datetime.now().strftime('%Y-%m-%d')
        
        priority, changefreq = get_priority_and_freq(dir_url)
        
        freq_elem = ET.SubElement(url_elem, 'changefreq')
        freq_elem.text = changefreq
        
        priority_elem = ET.SubElement(url_elem, 'priority')
        priority_elem.text = priority
    
    # Convert to pretty XML
    rough_string = ET.tostring(urlset, encoding='unicode')
    reparsed = minidom.parseString(rough_string)
    pretty_xml = reparsed.toprettyxml(indent="  ")
    
    # Remove extra blank lines
    lines = pretty_xml.split('\n')
    lines = [line for line in lines if line.strip()]
    pretty_xml = '\n'.join(lines)
    
    # Save sitemap
    sitemap_path = os.path.join(root_dir, 'sitemap.xml')
    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write(pretty_xml)
    
    print(f"✅ Sitemap generated with {len(urls_added)} URLs")
    print(f"📍 Saved to: {sitemap_path}")
    
    # Stats
    blog_count = sum(1 for url in urls_added if url.startswith('/blog/'))
    calc_count = sum(1 for url in urls_added if url.startswith('/calculators/'))
    es_count = sum(1 for url in urls_added if url.startswith('/es/'))
    
    print(f"\n📊 Breakdown:")
    print(f"  - Blog posts: {blog_count}")
    print(f"  - Calculators: {calc_count}")
    print(f"  - Spanish pages: {es_count}")
    print(f"  - Other pages: {len(urls_added) - blog_count - calc_count - es_count}")

if __name__ == "__main__":
    root_dir = '/Users/glengomezmeade/Projects/plasma-pay-calculator'
    generate_sitemap(root_dir)