#!/usr/bin/env python3
import os
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path

def create_sitemap():
    """Generate a clean sitemap with only existing URLs"""
    
    base_url = "https://plasmapaycalculator.com"
    root_dir = Path(".")
    
    # Create XML structure
    urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    
    def add_url(loc, priority="0.5", changefreq="weekly"):
        """Add a URL to the sitemap"""
        url = ET.SubElement(urlset, "url")
        ET.SubElement(url, "loc").text = loc
        ET.SubElement(url, "lastmod").text = datetime.now().strftime("%Y-%m-%d")
        ET.SubElement(url, "changefreq").text = changefreq
        ET.SubElement(url, "priority").text = priority
    
    # Add homepage
    add_url(base_url + "/", "1.0", "daily")
    
    # Add main pages
    main_pages = [
        ("about.html", "0.8", "monthly"),
        ("centers.html", "0.9", "weekly"),
        ("faq.html", "0.7", "monthly"),
        ("privacy.html", "0.3", "yearly"),
        ("terms.html", "0.3", "yearly"),
        ("contact.html", "0.5", "monthly")
    ]
    
    for page, priority, freq in main_pages:
        if os.path.exists(page):
            add_url(f"{base_url}/{page}", priority, freq)
    
    # Add calculator main page
    if os.path.exists("calculators/index.html"):
        add_url(f"{base_url}/calculators/", "1.0", "daily")
    
    # Add state calculators
    calc_dir = Path("calculators")
    if calc_dir.exists():
        for state_dir in sorted(calc_dir.iterdir()):
            if state_dir.is_dir():
                state_name = state_dir.name
                
                # Add state index page
                state_index = state_dir / "index.html"
                if state_index.exists():
                    add_url(f"{base_url}/calculators/{state_name}/", "0.8", "weekly")
                
                # Add city pages
                for city_dir in sorted(state_dir.iterdir()):
                    if city_dir.is_dir():
                        city_name = city_dir.name
                        city_index = city_dir / "index.html"
                        if city_index.exists():
                            add_url(f"{base_url}/calculators/{state_name}/{city_name}/", "0.7", "weekly")
    
    # Add blog posts (only .html files, not directories)
    blog_dir = Path("blog")
    if blog_dir.exists():
        # Add blog index
        if (blog_dir / "index.html").exists():
            add_url(f"{base_url}/blog/", "0.9", "daily")
        
        # Add individual blog posts
        for blog_file in sorted(blog_dir.glob("*.html")):
            if blog_file.name != "index.html":
                add_url(f"{base_url}/blog/{blog_file.name}", "0.7", "weekly")
        
        # Add blog subdirectories
        for subdir in sorted(blog_dir.iterdir()):
            if subdir.is_dir():
                for blog_file in sorted(subdir.glob("index.html")):
                    add_url(f"{base_url}/blog/{subdir.name}/", "0.7", "weekly")
    
    # Add tools
    tools_dir = Path("tools")
    if tools_dir.exists():
        for tool_file in sorted(tools_dir.glob("*.html")):
            add_url(f"{base_url}/tools/{tool_file.name}", "0.6", "monthly")
    
    # Add Spanish pages
    es_dir = Path("es")
    if es_dir.exists():
        # Add Spanish homepage
        if (es_dir / "index.html").exists():
            add_url(f"{base_url}/es/", "0.8", "weekly")
        
        # Add Spanish main pages
        for page in sorted(es_dir.glob("*.html")):
            if page.name != "index.html":
                add_url(f"{base_url}/es/{page.name}", "0.6", "monthly")
        
        # Add Spanish calculators
        es_calc_dir = es_dir / "calculators"
        if es_calc_dir.exists() and (es_calc_dir / "index.html").exists():
            add_url(f"{base_url}/es/calculators/", "0.7", "weekly")
            
            # Add Spanish state pages
            for state_dir in sorted(es_calc_dir.iterdir()):
                if state_dir.is_dir() and (state_dir / "index.html").exists():
                    add_url(f"{base_url}/es/calculators/{state_dir.name}/", "0.6", "weekly")
        
        # Add Spanish blog
        es_blog_dir = es_dir / "blog"
        if es_blog_dir.exists():
            if (es_blog_dir / "index.html").exists():
                add_url(f"{base_url}/es/blog/", "0.7", "weekly")
            
            for blog_file in sorted(es_blog_dir.glob("*.html")):
                if blog_file.name != "index.html":
                    add_url(f"{base_url}/es/blog/{blog_file.name}", "0.6", "weekly")
    
    # Create the tree and write to file
    tree = ET.ElementTree(urlset)
    ET.indent(tree, space="  ")
    
    with open("sitemap.xml", "wb") as f:
        f.write(b'<?xml version="1.0" encoding="UTF-8"?>\n')
        tree.write(f, encoding="UTF-8", xml_declaration=False)
    
    # Count URLs
    url_count = len(urlset.findall("url"))
    print(f"Generated sitemap.xml with {url_count} URLs")
    
    return url_count

if __name__ == "__main__":
    count = create_sitemap()
    print(f"✅ Sitemap generation complete: {count} valid URLs")