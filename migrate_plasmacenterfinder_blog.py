#!/usr/bin/env python3
"""
Blog Content Migration Script
Migrates blog content from plasmacenterfinder to plasma-pay-calculator

This script:
1. Reads all HTML files from plasmacenterfinder/guides/
2. Converts styling from Tailwind CSS to match plasma-pay-calculator blog format
3. Updates all branding from "Plasma Center Finder" to "Plasma Pay Calculator"
4. Updates all internal links and canonical URLs
5. Creates properly formatted blog posts for plasma-pay-calculator
"""

import os
import re
import shutil
from pathlib import Path

# Source and destination directories
SOURCE_DIR = "/Users/glengomezmeade/Projects/plasmacenterfinder/guides"
DEST_DIR = "/Users/glengomezmeade/Projects/plasma-pay-calculator/blog"

# URL mappings
OLD_DOMAIN = "plasmacenterfinder.com"
NEW_DOMAIN = "plasmapaycalculator.com"
OLD_BRANDING = "Plasma Center Finder"
NEW_BRANDING = "Plasma Pay Calculator"

def get_plasma_pay_calc_header():
    """Returns the standard header/navigation for plasma-pay-calculator blog posts"""
    return '''<!DOCTYPE html>
<html lang="en">
<head>
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-3180649272238451"
     crossorigin="anonymous"></script>

    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">'''

def get_plasma_pay_calc_nav():
    """Returns the standard navigation for plasma-pay-calculator"""
    return '''    <!-- Navigation -->
    <nav>
        <div class="nav-container">
            <div style="display: flex; align-items: center;">
                <a href="/" class="logo">
                    <div class="logo-icon">PPC</div>
                    Plasma Pay Calculator
                </a>
                <div class="trust-badge">Updated for 2025</div>
            </div>
            <ul class="nav-links">
                <li><a href="/#calculator">Calculator</a></li>
                <li><a href="/blog/">Blog</a></li>
                <li><a href="/states.html">States</a></li>
                <li><a href="/centers/" class="centers-highlight">🏥 Centers</a></li>
                <li><a href="/health/">Health</a></li>
                
                <li><a href="/faq.html">FAQ</a></li>
            </ul>
            <button class="mobile-menu-btn" onclick="toggleMobileMenu()">☰</button>
        </div>
        <div class="mobile-menu" id="mobileMenu">
            <ul>
                <li><a href="/#calculator">Calculator</a></li>
                <li><a href="/blog/">Blog</a></li>
                <li><a href="/states.html">States</a></li>
                <li><a href="/centers/" class="centers-highlight">🏥 Centers</a></li>
                <li><a href="/health/">Health</a></li>
                
                <li><a href="/faq.html">FAQ</a></li>
            </ul>
        </div>
    </nav>'''

def get_plasma_pay_calc_styles():
    """Returns the CSS styles matching plasma-pay-calculator blog format"""
    return '''
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif;
            line-height: 1.6;
            color: #2c3e50;
            margin: 0;
            padding: 0;
            background: #f8f9fa;
        }

        nav {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            padding: 1rem 0;
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 1000;
            border-bottom: 1px solid rgba(39, 174, 96, 0.1);
        }

        .nav-container {
            max-width: 1400px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 1.5rem;
        }

        .logo {
            font-size: 1.2rem;
            font-weight: 700;
            color: #27ae60;
            text-decoration: none;
            display: flex;
            align-items: center;
            gap: 0.6rem;
        }

        .logo-icon {
            width: 32px;
            height: 32px;
            background: linear-gradient(135deg, #27ae60 0%, #2ecc71 100%);
            border-radius: 6px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: 700;
            font-size: 12px;
            box-shadow: 0 2px 6px rgba(39, 174, 96, 0.3);
        }

        .trust-badge {
            background: rgba(39, 174, 96, 0.1);
            color: #27ae60;
            padding: 0.2rem 0.6rem;
            border-radius: 12px;
            font-size: 0.7rem;
            font-weight: 500;
            margin-left: 0.8rem;
            white-space: nowrap;
        }

        .nav-links {
            display: flex;
            list-style: none;
            gap: 1.2rem;
            align-items: center;
        }

        .nav-links a {
            text-decoration: none;
            color: #2c3e50;
            font-weight: 500;
            transition: all 0.3s;
            padding: 0.4rem 0.8rem;
            border-radius: 6px;
            font-size: 0.9rem;
            white-space: nowrap;
        }
        
        .centers-highlight {
            background: linear-gradient(135deg, #27ae60 0%, #2ecc71 100%) !important;
            color: white !important;
            border-radius: 6px !important;
            font-weight: 700 !important;
            box-shadow: 0 2px 6px rgba(39, 174, 96, 0.3) !important;
            transform: scale(1.05);
        }
        
        .centers-highlight:hover {
            background: linear-gradient(135deg, #219a52 0%, #26be5f 100%) !important;
            color: white !important;
            transform: scale(1.08);
        }

        .nav-links a:hover,
        .nav-links a.active {
            color: #27ae60;
            background: rgba(39, 174, 96, 0.1);
        }

        .mobile-menu-btn {
            display: none;
            background: none;
            border: none;
            color: #2c3e50;
            font-size: 24px;
            cursor: pointer;
        }

        .mobile-menu {
            display: none;
            position: fixed;
            top: 80px;
            left: 0;
            right: 0;
            background: rgba(255, 255, 255, 0.98);
            backdrop-filter: blur(10px);
            border-bottom: 1px solid rgba(39, 174, 96, 0.1);
            z-index: 999;
            padding: 1rem;
        }

        .mobile-menu.active {
            display: block;
        }

        .mobile-menu ul {
            list-style: none;
            padding: 0;
            margin: 0;
        }

        .mobile-menu li {
            margin: 0.5rem 0;
        }

        .mobile-menu a {
            display: block;
            padding: 1rem;
            text-decoration: none;
            color: #2c3e50;
            font-weight: 500;
            border-radius: 8px;
            transition: all 0.3s;
        }

        .mobile-menu a:hover,
        .mobile-menu a.active {
            color: #27ae60;
            background: rgba(39, 174, 96, 0.1);
        }

        @media (max-width: 968px) {
            .nav-links {
                display: none;
            }
            
            .mobile-menu-btn {
                display: block;
            }
            
            .trust-badge {
                font-size: 0.6rem;
                padding: 0.15rem 0.4rem;
            }
            
            .logo {
                font-size: 1rem;
            }
            
            .logo-icon {
                width: 28px;
                height: 28px;
                font-size: 11px;
            }
        }

        /* Main Content */
        .main-content {
            margin-top: 80px;
            max-width: 800px;
            margin-left: auto;
            margin-right: auto;
            padding: 2rem;
            background: white;
            border-radius: 15px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            margin-bottom: 2rem;
        }

        .article-header {
            text-align: center;
            margin-bottom: 3rem;
            padding: 2rem 0;
            border-bottom: 2px solid #f8f9fa;
        }

        .article-title {
            font-size: 2.5rem;
            font-weight: 700;
            color: #2c3e50;
            margin-bottom: 1rem;
            line-height: 1.2;
        }

        .article-meta {
            color: #7f8c8d;
            font-size: 0.9rem;
            margin-bottom: 1rem;
        }

        .article-meta span {
            margin: 0 0.5rem;
        }

        /* Content Styling */
        .content {
            font-size: 1.1rem;
            line-height: 1.8;
        }

        .content h2 {
            font-size: 2rem;
            font-weight: 600;
            color: #2c3e50;
            margin: 2.5rem 0 1rem 0;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid #27ae60;
        }

        .content h3 {
            font-size: 1.5rem;
            font-weight: 600;
            color: #34495e;
            margin: 2rem 0 1rem 0;
        }

        .content h4 {
            font-size: 1.3rem;
            font-weight: 600;
            color: #34495e;
            margin: 1.5rem 0 0.8rem 0;
        }

        .content p {
            margin-bottom: 1.5rem;
        }

        .content ul, .content ol {
            margin: 1.5rem 0;
            padding-left: 2rem;
        }

        .content li {
            margin: 0.5rem 0;
        }

        .content blockquote {
            background: #f8f9fa;
            border-left: 4px solid #27ae60;
            padding: 1rem 1.5rem;
            margin: 2rem 0;
            font-style: italic;
        }

        .content a {
            color: #27ae60;
            text-decoration: none;
            font-weight: 500;
        }

        .content a:hover {
            color: #219a52;
            text-decoration: underline;
        }

        /* Special Content Boxes */
        .warning-box, .info-box, .tip-box {
            padding: 1.5rem;
            border-radius: 10px;
            margin: 2rem 0;
            border-left: 5px solid;
        }

        .warning-box {
            background: #fff5f5;
            border-color: #e53e3e;
            color: #742a2a;
        }

        .info-box {
            background: #f0f8ff;
            border-color: #3182ce;
            color: #2a4365;
        }

        .tip-box {
            background: #f0fff4;
            border-color: #27ae60;
            color: #276749;
        }

        /* Tables */
        .content table {
            width: 100%;
            border-collapse: collapse;
            margin: 2rem 0;
            background: white;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }

        .content table th {
            background: #27ae60;
            color: white;
            padding: 1rem;
            text-align: left;
            font-weight: 600;
        }

        .content table td {
            padding: 1rem;
            border-bottom: 1px solid #e2e8f0;
        }

        .content table tr:hover {
            background: #f8f9fa;
        }

        /* Footer */
        footer {
            background: #2c3e50;
            color: white;
            padding: 3rem 0;
            margin-top: 4rem;
            text-align: center;
        }

        footer p {
            margin: 0;
        }

        footer a {
            color: #bdc3c7;
            margin: 0 1rem;
            text-decoration: none;
        }

        footer a:hover {
            color: white;
        }

        /* Responsive */
        @media (max-width: 768px) {
            .main-content {
                margin: 80px 1rem 2rem 1rem;
                padding: 1.5rem;
            }

            .article-title {
                font-size: 2rem;
            }

            .content h2 {
                font-size: 1.6rem;
            }
        }
    </style>'''

def get_plasma_pay_calc_footer():
    """Returns the standard footer for plasma-pay-calculator"""
    return '''    <footer>
        <div style="max-width: 1200px; margin: 0 auto; text-align: center; padding: 0 2rem;">
            <p>&copy; 2025 Plasma Pay Calculator. All rights reserved.</p>
            <div style="margin-top: 1rem;">
                <a href="/privacy.html">Privacy Policy</a>
                <a href="/terms.html">Terms of Service</a>
                <a href="/contact.html">Contact</a>
            </div>
        </div>
    </footer>

    <script>
        function toggleMobileMenu() {
            const mobileMenu = document.getElementById('mobileMenu');
            mobileMenu.classList.toggle('active');
        }
    </script>'''

def convert_content_format(content):
    """Convert content from Tailwind classes to our custom styles"""
    
    # Remove Tailwind CSS script
    content = re.sub(r'<script src="https://cdn\.tailwindcss\.com"></script>', '', content)
    
    # Convert Tailwind nav classes to our nav structure
    content = re.sub(r'<nav class="bg-white shadow-sm border-b">.*?</nav>', get_plasma_pay_calc_nav(), content, flags=re.DOTALL)
    
    # Convert main content container
    content = re.sub(r'<article class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-12">', '<div class="main-content">', content)
    content = re.sub(r'</article>', '</div>', content)
    
    # Convert hero sections to simple headers
    content = re.sub(r'<div class="relative h-96[^>]*>.*?</div>', '', content, flags=re.DOTALL)
    
    # Convert article headers
    content = re.sub(r'<header class="mb-8">', '<div class="article-header">', content)
    content = re.sub(r'</header>', '</div>', content)
    
    # Convert title classes
    content = re.sub(r'class="text-4xl md:text-5xl font-bold text-gray-900 mb-4"', 'class="article-title"', content)
    content = re.sub(r'class="flex items-center text-sm text-gray-600"', 'class="article-meta"', content)
    
    # Wrap main content in content div
    content = re.sub(r'(<div class="article-header">.*?</div>)(.*?)(<footer|$)', r'\1<div class="content">\2</div>\3', content, flags=re.DOTALL)
    
    # Convert Tailwind text colors and sizes to our classes
    content = re.sub(r'class="text-2xl font-bold[^"]*"', 'class=""', content)
    content = re.sub(r'class="text-3xl font-bold[^"]*"', '', content)
    
    # Remove remaining Tailwind classes
    content = re.sub(r'class="[^"]*(?:text-|bg-|p-|m-|flex|grid|rounded|shadow)[^"]*"', '', content)
    
    return content

def update_branding_and_links(content):
    """Update all branding and links from plasmacenterfinder to plasma-pay-calculator"""
    
    # Update domain references
    content = content.replace(OLD_DOMAIN, NEW_DOMAIN)
    content = content.replace(OLD_BRANDING, NEW_BRANDING)
    
    # Update canonical URLs
    content = re.sub(r'https://plasmacenterfinder\.com/', 'https://plasmapaycalculator.com/', content)
    
    # Update navigation links
    content = re.sub(r'href="/guides/"', 'href="/blog/"', content)
    
    # Update internal guide links to blog links
    content = re.sub(r'href="/guides/([^"]+)"', r'href="/blog/\1"', content)
    
    # Update author info
    content = content.replace('By Glen Meade', 'By Plasma Pay Calculator Team')
    content = content.replace('"Glen Meade"', '"Plasma Pay Calculator Team"')
    
    return content

def process_html_file(source_file, dest_file):
    """Process a single HTML file for migration"""
    
    print(f"Processing: {source_file} -> {dest_file}")
    
    with open(source_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract title and meta description for later use
    title_match = re.search(r'<title>(.*?)</title>', content)
    desc_match = re.search(r'<meta name="description" content="(.*?)"', content)
    
    title = title_match.group(1) if title_match else "Plasma Donation Guide"
    description = desc_match.group(1) if desc_match else "Expert plasma donation guide"
    
    # Start building new content
    new_content = get_plasma_pay_calc_header()
    
    # Add title and meta tags
    new_content += f'''
    <title>{title}</title>
    <meta name="description" content="{description}">
    <meta name="keywords" content="plasma donation, plasma pay, donation guide, plasma centers">
    
    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="article">
    <meta property="og:url" content="https://plasmapaycalculator.com/blog/{os.path.basename(dest_file)}">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">

    <!-- Twitter -->
    <meta property="twitter:card" content="summary_large_image">
    <meta property="twitter:url" content="https://plasmapaycalculator.com/blog/{os.path.basename(dest_file)}">
    <meta property="twitter:title" content="{title}">
    <meta property="twitter:description" content="{description}">
    
    <link rel="canonical" href="https://plasmapaycalculator.com/blog/{os.path.basename(dest_file)}">
    <link rel="icon" type="image/x-icon" href="/favicon.ico">'''
    
    # Add CSS styles
    new_content += get_plasma_pay_calc_styles()
    
    new_content += '''
</head>
<body>'''
    
    # Add navigation
    new_content += get_plasma_pay_calc_nav()
    
    # Extract and convert main content
    body_match = re.search(r'<body[^>]*>(.*?)</body>', content, flags=re.DOTALL)
    if body_match:
        body_content = body_match.group(1)
        
        # Remove the original navigation
        body_content = re.sub(r'<nav.*?</nav>', '', body_content, flags=re.DOTALL)
        
        # Remove the original footer
        body_content = re.sub(r'<footer.*?</footer>', '', body_content, flags=re.DOTALL)
        
        # Remove any scripts
        body_content = re.sub(r'<script.*?</script>', '', body_content, flags=re.DOTALL)
        
        # Convert content format
        body_content = convert_content_format(body_content)
        
        # Update branding and links
        body_content = update_branding_and_links(body_content)
        
        new_content += body_content
    
    # Add footer
    new_content += get_plasma_pay_calc_footer()
    
    new_content += '''
</body>
</html>'''
    
    # Write the new file
    with open(dest_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✓ Successfully migrated: {os.path.basename(dest_file)}")

def main():
    """Main migration function"""
    
    print("Starting blog content migration from plasmacenterfinder to plasma-pay-calculator...")
    print(f"Source: {SOURCE_DIR}")
    print(f"Destination: {DEST_DIR}")
    print()
    
    # Ensure destination directory exists
    os.makedirs(DEST_DIR, exist_ok=True)
    
    # Get list of HTML files to migrate (exclude index.html)
    source_files = []
    for file in os.listdir(SOURCE_DIR):
        if file.endswith('.html') and file != 'index.html':
            source_files.append(file)
    
    print(f"Found {len(source_files)} files to migrate:")
    for file in source_files:
        print(f"  - {file}")
    print()
    
    # Process each file
    migrated_files = []
    for file in source_files:
        source_path = os.path.join(SOURCE_DIR, file)
        dest_path = os.path.join(DEST_DIR, file)
        
        try:
            process_html_file(source_path, dest_path)
            migrated_files.append(file)
        except Exception as e:
            print(f"✗ Error processing {file}: {e}")
    
    print()
    print(f"Migration completed!")
    print(f"Successfully migrated {len(migrated_files)} out of {len(source_files)} files")
    print()
    print("Migrated files:")
    for file in migrated_files:
        print(f"  ✓ {file}")
    
    print()
    print("Next steps:")
    print("1. Update blog/index.html to include the new posts")
    print("2. Update sitemap.xml")
    print("3. Test all migrated content")
    print("4. Update any additional internal links")

if __name__ == "__main__":
    main()