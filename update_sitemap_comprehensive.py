#!/usr/bin/env python3
"""Update sitemap.xml with all new blog posts and centers pages"""

import os
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path

def update_sitemap():
    # Parse existing sitemap
    sitemap_path = 'sitemap.xml'
    
    # Register namespace
    ET.register_namespace('', 'http://www.sitemaps.org/schemas/sitemap/0.9')
    
    # Parse the existing sitemap
    tree = ET.parse(sitemap_path)
    root = tree.getroot()
    
    # Namespace
    ns = {'': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    
    # Get all existing URLs to avoid duplicates
    existing_urls = set()
    for url in root.findall('url', ns):
        loc = url.find('loc', ns)
        if loc is not None:
            existing_urls.add(loc.text)
    
    # Base URL
    base_url = 'https://www.plasmapaycalculator.com'
    
    # New blog posts to add
    new_blog_posts = [
        'best-plasma-centers-by-state-2025.html',
        'biolife-vs-csl-plasma-comparison-2025.html',
        'emergency-money-plasma-donation-financial-crisis-2025.html',
        'first-time-plasma-donor-guide-2025.html',
        'health-tips-plasma-donors-2025.html',
        'how-to-recover-faster-after-plasma-donation-2025.html',
        'maximize-plasma-donation-earnings-2025.html',
        'plasma-donation-disqualifications-complete-list-2025.html',
        'plasma-donation-myths-vs-facts-debunked-2025.html',
        'plasma-donation-payment-methods-2025.html',
        'plasma-donation-process-explained-2025.html',
        'plasma-donation-referral-bonuses-2025.html',
        'plasma-donation-requirements-2025.html',
        'plasma-donation-side-effects-safety-2025.html',
        'plasma-donation-vs-gig-economy-comparison-2025.html',
        'plasma-vs-blood-donation-guide-2025.html',
        'student-guide-plasma-donation-college-money-2025.html',
        'what-to-eat-before-after-plasma-donation-2025.html'
    ]
    
    # Centers pages to add
    centers_pages = [
        'centers/',
        'centers/biolife/',
        'centers/csl-plasma/',
        'centers/grifols/',
        'centers/octapharma/'
    ]
    
    # Current date for lastmod
    current_date = datetime.now().strftime('%Y-%m-%d')
    
    # Add new blog posts
    for post in new_blog_posts:
        post_url = f"{base_url}/blog/{post}"
        if post_url not in existing_urls:
            url_elem = ET.SubElement(root, 'url')
            loc_elem = ET.SubElement(url_elem, 'loc')
            loc_elem.text = post_url
            lastmod_elem = ET.SubElement(url_elem, 'lastmod')
            lastmod_elem.text = current_date
            changefreq_elem = ET.SubElement(url_elem, 'changefreq')
            changefreq_elem.text = 'monthly'
            priority_elem = ET.SubElement(url_elem, 'priority')
            priority_elem.text = '0.8'
            print(f"Added blog post: {post}")
    
    # Add centers pages
    for page in centers_pages:
        page_url = f"{base_url}/{page}"
        if page_url not in existing_urls:
            url_elem = ET.SubElement(root, 'url')
            loc_elem = ET.SubElement(url_elem, 'loc')
            loc_elem.text = page_url
            lastmod_elem = ET.SubElement(url_elem, 'lastmod')
            lastmod_elem.text = current_date
            changefreq_elem = ET.SubElement(url_elem, 'changefreq')
            # Centers directory should update more frequently
            changefreq_elem.text = 'weekly' if page == 'centers/' else 'monthly'
            priority_elem = ET.SubElement(url_elem, 'priority')
            # Higher priority for main centers page
            priority_elem.text = '0.9' if page == 'centers/' else '0.7'
            print(f"Added centers page: {page}")
    
    # Format the XML properly
    ET.indent(tree, space='  ')
    
    # Write the updated sitemap
    tree.write(sitemap_path, encoding='utf-8', xml_declaration=True)
    
    print(f"\nSitemap updated successfully!")
    print(f"Total URLs in sitemap: {len(root.findall('url', ns))}")
    
    # Count URLs by type
    blog_count = sum(1 for url in root.findall('url', ns) 
                     if '/blog/' in url.find('loc', ns).text)
    centers_count = sum(1 for url in root.findall('url', ns) 
                       if '/centers/' in url.find('loc', ns).text)
    
    print(f"Blog posts: {blog_count}")
    print(f"Centers pages: {centers_count}")

if __name__ == "__main__":
    update_sitemap()