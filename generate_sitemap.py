#!/usr/bin/env python3

import os
from datetime import datetime
from pathlib import Path
import xml.etree.ElementTree as ET
from xml.dom import minidom

def get_priority(filepath):
    """Assign priority based on page importance"""
    if filepath == 'index.html':
        return '1.0'
    elif filepath == 'blog/index.html':
        return '0.9'
    elif filepath.startswith('centers/'):
        return '0.9'
    elif filepath.startswith('calculators/'):
        return '0.8'
    elif filepath.startswith('blog/'):
        return '0.7'
    elif filepath.startswith('topics/'):
        return '0.6'
    else:
        return '0.5'

def get_changefreq(filepath):
    """Assign change frequency based on page type"""
    if filepath == 'index.html':
        return 'daily'
    elif filepath.startswith('blog/'):
        return 'weekly'
    elif filepath.startswith('centers/'):
        return 'weekly'
    elif filepath.startswith('calculators/'):
        return 'monthly'
    else:
        return 'monthly'

def generate_sitemap():
    """Generate sitemap.xml with all HTML pages"""
    
    base_url = 'https://plasmapaycalculator.com'
    root_dir = '/Users/glengomezmeade/Projects/plasma-pay-calculator'
    
    # Create root element
    urlset = ET.Element('urlset')
    urlset.set('xmlns', 'http://www.sitemaps.org/schemas/sitemap/0.9')
    
    # Find all HTML files
    html_files = []
    for root, dirs, files in os.walk(root_dir):
        # Skip hidden directories and common non-content directories
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['node_modules', '__pycache__']]
        
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                # Get relative path from project root
                rel_path = os.path.relpath(filepath, root_dir)
                # Skip test files and templates
                if not any(x in rel_path for x in ['test', 'template', 'example', '404']):
                    html_files.append(rel_path)
    
    # Sort files for consistent output
    html_files.sort()
    
    # Get current date
    today = datetime.now().strftime('%Y-%m-%d')
    
    # Add each HTML file to sitemap
    for filepath in html_files:
        # Convert file path to URL
        if filepath == 'index.html':
            url_path = '/'
        elif filepath.endswith('/index.html'):
            url_path = '/' + filepath.replace('/index.html', '/')
        else:
            url_path = '/' + filepath
        
        # Create URL element
        url_elem = ET.SubElement(urlset, 'url')
        
        # Add location
        loc = ET.SubElement(url_elem, 'loc')
        loc.text = base_url + url_path
        
        # Add last modified date
        lastmod = ET.SubElement(url_elem, 'lastmod')
        lastmod.text = today
        
        # Add change frequency
        changefreq = ET.SubElement(url_elem, 'changefreq')
        changefreq.text = get_changefreq(filepath)
        
        # Add priority
        priority = ET.SubElement(url_elem, 'priority')
        priority.text = get_priority(filepath)
    
    # Create tree and format it
    tree = ET.ElementTree(urlset)
    
    # Convert to string and prettify
    xml_str = ET.tostring(urlset, encoding='unicode')
    dom = minidom.parseString(xml_str)
    pretty_xml = dom.toprettyxml(indent='  ', encoding='UTF-8')
    
    # Remove extra blank lines
    lines = pretty_xml.decode('utf-8').split('\n')
    lines = [line for line in lines if line.strip()]
    pretty_xml = '\n'.join(lines)
    
    # Write to file
    with open(os.path.join(root_dir, 'sitemap.xml'), 'w', encoding='utf-8') as f:
        f.write(pretty_xml)
    
    print(f"Sitemap generated with {len(html_files)} URLs")
    print(f"Sitemap saved to sitemap.xml")
    
    # Print statistics
    blog_count = sum(1 for f in html_files if f.startswith('blog/'))
    center_count = sum(1 for f in html_files if f.startswith('centers/'))
    calc_count = sum(1 for f in html_files if f.startswith('calculators/'))
    
    print(f"\nBreakdown:")
    print(f"  Blog posts: {blog_count}")
    print(f"  Center pages: {center_count}")
    print(f"  Calculator pages: {calc_count}")
    print(f"  Other pages: {len(html_files) - blog_count - center_count - calc_count}")

if __name__ == '__main__':
    generate_sitemap()