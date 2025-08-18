#!/usr/bin/env python3

import os
from pathlib import Path
from datetime import datetime
import xml.etree.ElementTree as ET

def generate_sitemap():
    base_url = "https://plasmapaycalculator.com"
    
    # Create root element
    urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    
    # Priority pages
    priority_pages = [
        ("/", "1.0", "daily"),
        ("/blog/", "0.9", "daily"),
        ("/centers/", "0.9", "weekly"),
        ("/states.html", "0.8", "weekly"),
        ("/faq.html", "0.8", "weekly"),
        ("/#calculator", "1.0", "daily"),
    ]
    
    # Add priority pages
    for path, priority, freq in priority_pages:
        url = ET.SubElement(urlset, "url")
        ET.SubElement(url, "loc").text = base_url + path
        ET.SubElement(url, "lastmod").text = datetime.now().strftime("%Y-%m-%d")
        ET.SubElement(url, "changefreq").text = freq
        ET.SubElement(url, "priority").text = priority
    
    # Add all blog posts
    blog_dir = Path("/Users/glengomezmeade/Projects/plasma-pay-calculator/blog")
    blog_files = sorted([f for f in blog_dir.glob("*.html") if f.name != "index.html"])
    
    for blog_file in blog_files:
        # Add main blog file
        url = ET.SubElement(urlset, "url")
        ET.SubElement(url, "loc").text = f"{base_url}/blog/{blog_file.name}"
        ET.SubElement(url, "lastmod").text = datetime.now().strftime("%Y-%m-%d")
        ET.SubElement(url, "changefreq").text = "weekly"
        ET.SubElement(url, "priority").text = "0.7"
        
        # Add subdirectory version
        slug = blog_file.stem
        url = ET.SubElement(urlset, "url")
        ET.SubElement(url, "loc").text = f"{base_url}/blog/{slug}/"
        ET.SubElement(url, "lastmod").text = datetime.now().strftime("%Y-%m-%d")
        ET.SubElement(url, "changefreq").text = "weekly"
        ET.SubElement(url, "priority").text = "0.7"
    
    # Add center pages if they exist
    centers_dir = Path("/Users/glengomezmeade/Projects/plasma-pay-calculator/centers")
    if centers_dir.exists():
        for center_file in centers_dir.glob("*.html"):
            if center_file.name != "index.html":
                url = ET.SubElement(urlset, "url")
                ET.SubElement(url, "loc").text = f"{base_url}/centers/{center_file.name}"
                ET.SubElement(url, "lastmod").text = datetime.now().strftime("%Y-%m-%d")
                ET.SubElement(url, "changefreq").text = "weekly"
                ET.SubElement(url, "priority").text = "0.7"
    
    # Add topics pages if they exist
    topics_dir = Path("/Users/glengomezmeade/Projects/plasma-pay-calculator/topics")
    if topics_dir.exists():
        for topic_dir in topics_dir.iterdir():
            if topic_dir.is_dir():
                url = ET.SubElement(urlset, "url")
                ET.SubElement(url, "loc").text = f"{base_url}/topics/{topic_dir.name}/"
                ET.SubElement(url, "lastmod").text = datetime.now().strftime("%Y-%m-%d")
                ET.SubElement(url, "changefreq").text = "weekly"
                ET.SubElement(url, "priority").text = "0.7"
    
    # Create tree and write to file
    tree = ET.ElementTree(urlset)
    ET.indent(tree, space="  ")
    
    sitemap_path = Path("/Users/glengomezmeade/Projects/plasma-pay-calculator/sitemap.xml")
    tree.write(sitemap_path, encoding="utf-8", xml_declaration=True)
    
    # Count URLs
    url_count = len(urlset.findall("url"))
    
    print(f"✅ Sitemap generated successfully!")
    print(f"📍 Location: {sitemap_path}")
    print(f"🔗 Total URLs: {url_count}")
    print(f"📝 Blog posts: {len(blog_files)} (x2 for subdirectories)")
    
    return url_count

if __name__ == "__main__":
    generate_sitemap()
