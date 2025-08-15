#!/usr/bin/env python3
"""
Performance optimization script for improving Core Web Vitals and page speed.
Optimizes HTML files for better Google rankings.
"""

import os
import re
from pathlib import Path
from bs4 import BeautifulSoup
import json

def minify_inline_css(css):
    """Minify inline CSS"""
    # Remove comments
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.DOTALL)
    # Remove unnecessary whitespace
    css = re.sub(r'\s+', ' ', css)
    css = re.sub(r':\s+', ':', css)
    css = re.sub(r';\s+', ';', css)
    css = re.sub(r'{\s+', '{', css)
    css = re.sub(r'}\s+', '}', css)
    css = re.sub(r',\s+', ',', css)
    return css.strip()

def minify_inline_js(js):
    """Basic JS minification"""
    # Remove single-line comments (but keep URLs)
    js = re.sub(r'(?<!:)//[^\n]*', '', js)
    # Remove multi-line comments
    js = re.sub(r'/\*.*?\*/', '', js, flags=re.DOTALL)
    # Remove excessive whitespace
    js = re.sub(r'\s+', ' ', js)
    js = re.sub(r';\s+', ';', js)
    js = re.sub(r'{\s+', '{', js)
    js = re.sub(r'}\s+', '}', js)
    return js.strip()

def add_lazy_loading(soup):
    """Add lazy loading to images"""
    images = soup.find_all('img')
    modified = False
    
    for img in images:
        if not img.get('loading'):
            # Skip logo and above-the-fold images
            if 'logo' in str(img.get('class', '')) or 'logo' in str(img.get('id', '')):
                continue
            if 'hero' in str(img.get('class', '')) or 'banner' in str(img.get('class', '')):
                continue
            
            img['loading'] = 'lazy'
            modified = True
    
    return modified

def optimize_critical_css(soup):
    """Extract and inline critical CSS"""
    # Find all style tags
    style_tags = soup.find_all('style')
    
    if style_tags:
        # Combine all styles
        all_css = ''
        for tag in style_tags:
            if tag.string:
                all_css += tag.string
        
        # Minify the CSS
        minified = minify_inline_css(all_css)
        
        # Remove old style tags
        for tag in style_tags[1:]:  # Keep first one
            tag.decompose()
        
        # Update first style tag with minified CSS
        if style_tags:
            style_tags[0].string = minified
            return True
    
    return False

def add_preconnect_hints(soup):
    """Add preconnect hints for external resources"""
    head = soup.find('head')
    if not head:
        return False
    
    # Check for existing preconnects
    existing_preconnects = set()
    for link in soup.find_all('link', {'rel': 'preconnect'}):
        href = link.get('href')
        if href:
            existing_preconnects.add(href)
    
    # Add preconnects for common services
    preconnects = [
        'https://fonts.googleapis.com',
        'https://fonts.gstatic.com',
        'https://www.googletagmanager.com',
        'https://pagead2.googlesyndication.com'
    ]
    
    modified = False
    for url in preconnects:
        if url not in existing_preconnects:
            # Add preconnect
            new_link = soup.new_tag('link', rel='preconnect', href=url)
            head.insert(0, new_link)
            
            # Add dns-prefetch as fallback
            dns_link = soup.new_tag('link', rel='dns-prefetch', href=url)
            head.insert(0, dns_link)
            modified = True
    
    return modified

def defer_non_critical_js(soup):
    """Add defer attribute to non-critical JavaScript"""
    scripts = soup.find_all('script', src=True)
    modified = False
    
    for script in scripts:
        src = script.get('src', '')
        
        # Skip critical scripts (analytics, ads)
        if 'gtag' in src or 'analytics' in src or 'adsbygoogle' in src:
            # These should load async
            if not script.get('async'):
                script['async'] = True
                modified = True
            continue
        
        # Defer other external scripts
        if not script.get('defer') and not script.get('async'):
            script['defer'] = True
            modified = True
    
    return modified

def optimize_file(file_path):
    """Optimize a single HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        
        changes = []
        
        # Add preconnect hints
        if add_preconnect_hints(soup):
            changes.append('preconnect hints')
        
        # Add lazy loading to images
        if add_lazy_loading(soup):
            changes.append('lazy loading')
        
        # Optimize critical CSS
        if optimize_critical_css(soup):
            changes.append('CSS optimization')
        
        # Defer non-critical JavaScript
        if defer_non_critical_js(soup):
            changes.append('JS defer')
        
        # Minify inline scripts
        script_tags = soup.find_all('script')
        for script in script_tags:
            if script.string and not script.get('src') and len(script.string) > 100:
                # Don't minify JSON-LD
                if 'application/ld+json' not in str(script.get('type', '')):
                    minified = minify_inline_js(script.string)
                    if len(minified) < len(script.string):
                        script.string = minified
                        if 'JS minification' not in changes:
                            changes.append('JS minification')
        
        if changes:
            # Write optimized content
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            
            return True, changes
        
        return False, []
        
    except Exception as e:
        print(f"Error optimizing {file_path}: {e}")
        return False, []

def main():
    """Main optimization function"""
    print("Starting performance optimization...")
    
    # Find all HTML files
    html_files = []
    for root, dirs, files in os.walk('.'):
        # Skip certain directories
        if 'node_modules' in root or '.git' in root:
            continue
        
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    
    print(f"Found {len(html_files)} HTML files")
    
    # Track optimization stats
    optimized = 0
    optimization_stats = {}
    
    # Optimize each file
    for i, file_path in enumerate(html_files):
        if i % 50 == 0:
            print(f"Progress: {i}/{len(html_files)} files processed...")
        
        success, changes = optimize_file(file_path)
        
        if success:
            optimized += 1
            for change in changes:
                optimization_stats[change] = optimization_stats.get(change, 0) + 1
    
    # Print summary
    print(f"\n✅ Optimization Complete!")
    print(f"Files optimized: {optimized}/{len(html_files)}")
    
    if optimization_stats:
        print("\nOptimizations applied:")
        for opt, count in sorted(optimization_stats.items(), key=lambda x: x[1], reverse=True):
            print(f"  - {opt}: {count} files")
    
    print("\n🚀 Core Web Vitals improvements:")
    print("  - Reduced render-blocking resources")
    print("  - Added lazy loading for images")
    print("  - Minified inline CSS and JavaScript")
    print("  - Added resource hints (preconnect/dns-prefetch)")
    print("  - Deferred non-critical JavaScript")
    
    return optimized

if __name__ == "__main__":
    main()