#!/usr/bin/env python3
"""
Enhance internal linking across all pages for better SEO and user navigation
"""

import os
import re
from pathlib import Path

# Key linking opportunities - simple patterns
LINK_OPPORTUNITIES = [
    # Calculator-related keywords -> calculator page
    ('plasma pay calculator', '/calculator/'),
    ('plasma calculator', '/calculator/'),
    ('donation calculator', '/calculator/'),
    ('earnings calculator', '/calculator/'),
    
    # Centers-related keywords -> centers page
    ('find plasma centers', '/centers/'),
    ('plasma centers near me', '/centers/'),
    ('nearest plasma center', '/centers/'),
    ('plasma center locations', '/centers/'),
    
    # FAQ linking
    ('frequently asked questions', '/faq.html'),
    ('plasma donation faq', '/faq.html'),
    ('common questions', '/faq.html'),
    
    # Health/eligibility linking
    ('eligibility requirements', '/health/'),
    ('plasma donation requirements', '/health/'),
    ('who can donate plasma', '/health/'),
    ('health requirements', '/health/'),
]

def add_internal_links(content, file_path):
    """Add strategic internal links to content"""
    links_added = 0
    rel_path = os.path.relpath(file_path, "/Users/glengomezmeade/Projects/plasma-pay-calculator")
    
    # Skip if this is the target page to avoid circular links
    for keyword, target_url in LINK_OPPORTUNITIES:
        # Skip if we're on the target page
        if target_url.strip('/') in rel_path:
            continue
            
        # Simple pattern - find keyword not already in links
        pattern = re.compile(f'\\b{re.escape(keyword)}\\b', re.IGNORECASE)
        
        # Check if keyword exists and is not already linked
        matches = pattern.findall(content)
        if matches and f'href="{target_url}"' not in content:
            # Replace only the first occurrence
            def replace_with_link(match):
                nonlocal links_added
                if links_added < 3:  # Limit to 3 links per page
                    links_added += 1
                    return f'<a href="{target_url}" class="text-green-600 hover:text-green-800 underline">{match.group(0)}</a>'
                return match.group(0)
            
            content = pattern.sub(replace_with_link, content, count=1)
    
    return content, links_added

def enhance_file_linking(file_path):
    """Enhance internal linking for a single file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        enhanced_content, links_added = add_internal_links(content, file_path)
        
        # Only write if changes were made
        if enhanced_content != original_content and links_added > 0:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(enhanced_content)
            return links_added
        
        return 0
        
    except Exception as e:
        print(f"❌ Error processing {file_path}: {str(e)}")
        return 0

def add_breadcrumb_navigation():
    """Add breadcrumb navigation to calculator pages"""
    base_dir = "/Users/glengomezmeade/Projects/plasma-pay-calculator/calculators"
    breadcrumbs_added = 0
    
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file == 'index.html':
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, base_dir)
                
                # Skip state-level pages (they already have good navigation)
                if rel_path.count('/') < 2:
                    continue
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Only add if breadcrumbs don't already exist
                    if 'breadcrumb' not in content.lower() and '<nav' in content:
                        # Extract state and city from path
                        parts = rel_path.split('/')
                        if len(parts) >= 2:
                            state = parts[0].replace('-', ' ').title()
                            city = parts[1].replace('-', ' ').title()
                            
                            breadcrumb_html = f'''
                            <nav class="breadcrumb mb-6">
                                <div class="container mx-auto px-4">
                                    <ol class="flex items-center space-x-2 text-sm text-gray-600">
                                        <li><a href="/" class="hover:text-green-600">Home</a></li>
                                        <li><span class="mx-2">›</span></li>
                                        <li><a href="/states.html" class="hover:text-green-600">States</a></li>
                                        <li><span class="mx-2">›</span></li>
                                        <li><a href="/calculators/{parts[0]}/" class="hover:text-green-600">{state}</a></li>
                                        <li><span class="mx-2">›</span></li>
                                        <li class="text-gray-800 font-medium">{city}</li>
                                    </ol>
                                </div>
                            </nav>
                            '''
                            
                            # Insert after opening body tag or first container
                            if '<body' in content:
                                content = content.replace('<body', breadcrumb_html + '\n<body', 1)
                            elif 'class="container' in content:
                                content = content.replace('class="container', breadcrumb_html + '\n<div class="container', 1)
                            
                            with open(file_path, 'w', encoding='utf-8') as f:
                                f.write(content)
                            
                            breadcrumbs_added += 1
                            print(f"✅ Added breadcrumbs to {rel_path}")
                
                except Exception as e:
                    print(f"❌ Error adding breadcrumbs to {file_path}: {str(e)}")
    
    return breadcrumbs_added

def main():
    """Main function"""
    print("🚀 Starting internal linking enhancement...")
    
    # Find all HTML files in key directories
    target_dirs = [
        "/Users/glengomezmeade/Projects/plasma-pay-calculator/blog",
        "/Users/glengomezmeade/Projects/plasma-pay-calculator/calculators",
        "/Users/glengomezmeade/Projects/plasma-pay-calculator/centers",
        "/Users/glengomezmeade/Projects/plasma-pay-calculator/health"
    ]
    
    html_files = []
    for target_dir in target_dirs:
        if os.path.exists(target_dir):
            for root, dirs, files in os.walk(target_dir):
                for file in files:
                    if file.endswith('.html'):
                        html_files.append(os.path.join(root, file))
    
    # Add main site files
    main_files = [
        "/Users/glengomezmeade/Projects/plasma-pay-calculator/index.html",
        "/Users/glengomezmeade/Projects/plasma-pay-calculator/about.html",
        "/Users/glengomezmeade/Projects/plasma-pay-calculator/faq.html",
        "/Users/glengomezmeade/Projects/plasma-pay-calculator/states.html"
    ]
    
    for main_file in main_files:
        if os.path.exists(main_file):
            html_files.append(main_file)
    
    print(f"📊 Found {len(html_files)} HTML files to enhance")
    
    total_links_added = 0
    files_enhanced = 0
    
    # Enhance individual files
    for file_path in html_files[:50]:  # Limit to first 50 files to avoid overwhelming
        rel_path = os.path.relpath(file_path, "/Users/glengomezmeade/Projects/plasma-pay-calculator")
        links_added = enhance_file_linking(file_path)
        
        if links_added > 0:
            print(f"✅ Enhanced {rel_path} (+{links_added} links)")
            files_enhanced += 1
            total_links_added += links_added
    
    print(f"\n🧭 Adding breadcrumb navigation...")
    breadcrumbs_added = add_breadcrumb_navigation()
    
    print(f"\n🎉 Internal linking enhancement complete!")
    print(f"📊 Files enhanced: {files_enhanced}")
    print(f"🔗 Total internal links added: {total_links_added}")
    print(f"🧭 Breadcrumbs added: {breadcrumbs_added}")
    print(f"📈 This will improve site navigation and SEO performance")

if __name__ == "__main__":
    main()