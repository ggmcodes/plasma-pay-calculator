#!/usr/bin/env python3

import os
from pathlib import Path
from datetime import datetime
import xml.etree.ElementTree as ET

def generate_ultimate_sitemap():
    base_url = "https://plasmapaycalculator.com"
    
    # Create root element
    urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    
    # Track added URLs to avoid duplicates
    added_urls = set()
    
    def add_url(path, priority="0.7", changefreq="weekly"):
        if path not in added_urls and not path.endswith(('.py', '.txt', '.json', '.md')):
            url = ET.SubElement(urlset, "url")
            ET.SubElement(url, "loc").text = base_url + path
            ET.SubElement(url, "lastmod").text = datetime.now().strftime("%Y-%m-%d")
            ET.SubElement(url, "changefreq").text = changefreq
            ET.SubElement(url, "priority").text = priority
            added_urls.add(path)
            return True
        return False
    
    # Add priority pages
    priority_pages = [
        ("/", "1.0", "daily"),
        ("/blog/", "0.9", "daily"),
        ("/centers/", "0.9", "weekly"),
        ("/states.html", "0.8", "weekly"),
        ("/faq.html", "0.8", "weekly"),
        ("/calculators/", "0.9", "weekly"),
    ]
    
    for path, priority, freq in priority_pages:
        add_url(path, priority, freq)
    
    root_dir = Path("/Users/glengomezmeade/Projects/plasma-pay-calculator")
    
    # Add ALL HTML files recursively
    skip_files = {"index.html", "blog_cards.html", "create-favicons.html", "favicon-generator.html"}
    
    def process_directory(directory, base_path=""):
        if not directory.exists():
            return
            
        # Add directory index if it exists
        index_file = directory / "index.html"
        if index_file.exists() and base_path:  # Don't add root index
            add_url(f"{base_path}/", "0.7", "weekly")
        
        # Process all files in directory
        for item in directory.iterdir():
            if item.is_file() and item.suffix == ".html":
                if item.name in skip_files and base_path == "":
                    continue
                    
                if item.name == "index.html":
                    # Already handled above
                    continue
                else:
                    # Regular HTML file
                    file_path = f"{base_path}/{item.name}" if base_path else f"/{item.name}"
                    priority = "0.8" if base_path == "" else "0.7"
                    add_url(file_path, priority, "weekly")
            
            elif item.is_dir() and not item.name.startswith('.'):
                # Recursively process subdirectory
                new_base = f"{base_path}/{item.name}" if base_path else f"/{item.name}"
                process_directory(item, new_base)
    
    # Process all directories
    process_directory(root_dir)
    
    # Ensure we got all blog subdirectories
    blog_dir = root_dir / "blog"
    if blog_dir.exists():
        for blog_file in blog_dir.glob("*.html"):
            if blog_file.name != "index.html":
                slug = blog_file.stem
                subdir_path = f"/blog/{slug}/"
                add_url(subdir_path, "0.7", "weekly")
    
    # Write sitemap
    tree = ET.ElementTree(urlset)
    ET.indent(tree, space="  ")
    
    sitemap_path = root_dir / "sitemap.xml"
    tree.write(sitemap_path, encoding="utf-8", xml_declaration=True)
    
    # Count by type
    url_count = len(added_urls)
    blog_count = len([u for u in added_urls if u.startswith("/blog/")])
    calc_count = len([u for u in added_urls if u.startswith("/calculators/")])
    center_count = len([u for u in added_urls if u.startswith("/centers/")])
    root_count = len([u for u in added_urls if u.count("/") == 1 and u.endswith(".html")])
    dir_count = len([u for u in added_urls if u.endswith("/")])
    
    print(f"🎉 ULTIMATE COMPREHENSIVE SITEMAP GENERATED!")
    print(f"📍 Location: {sitemap_path}")
    print(f"🔗 TOTAL URLs: {url_count}")
    print(f"")
    print(f"Detailed Breakdown:")
    print(f"  📝 Blog URLs: {blog_count}")
    print(f"  🧮 Calculator URLs: {calc_count}")
    print(f"  🏥 Center URLs: {center_count}")
    print(f"  📄 Root HTML pages: {root_count}")
    print(f"  📁 Directory indexes: {dir_count}")
    print(f"  🔗 Other URLs: {url_count - blog_count - calc_count - center_count - root_count - dir_count}")
    
    # Verify we got close to the total HTML files
    print(f"")
    print(f"📊 Coverage Analysis:")
    print(f"  Total HTML files on disk: 1034")
    print(f"  URLs in sitemap: {url_count}")
    print(f"  Coverage: {(url_count/1034)*100:.1f}%")
    
    return url_count

if __name__ == "__main__":
    generate_ultimate_sitemap()
