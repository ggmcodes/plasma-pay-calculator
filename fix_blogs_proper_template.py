#!/usr/bin/env python3

import os
import re
from bs4 import BeautifulSoup

def fix_blog_post(filepath):
    """Fix a single blog post to match the working template"""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    
    # Get the title from the existing file
    title_tag = soup.find('title')
    title = title_tag.text if title_tag else 'Plasma Donation Guide'
    
    # Get meta description
    meta_desc = soup.find('meta', attrs={'name': 'description'})
    description = meta_desc.get('content', '') if meta_desc else ''
    
    # Get the main content from the existing file
    # Find all text content from sections
    main_content = []
    
    # Get the article title 
    h1 = soup.find('h1')
    if h1:
        article_title = h1.get_text(strip=True)
    else:
        article_title = title.replace(' - Plasma Pay Calculator', '')
    
    # Get all sections and their content
    sections = soup.find_all('section')
    
    # Build the new HTML with proper template
    new_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{description}">
    <meta name="keywords" content="plasma donation, plasma pay, donation guide, plasma centers">
    <link rel="canonical" href="https://plasmapaycalculator.com/blog/{os.path.basename(filepath)}">
    <link rel="icon" type="image/svg+xml" href="/favicon.svg">
    
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-053DRWEQLS"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());
      gtag('config', 'G-053DRWEQLS');
    </script>
    
    <!-- AdSense -->
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-3180649272238451"
         crossorigin="anonymous"></script>
    
    <!-- Styles -->
    <link rel="stylesheet" href="/styles.css">
    
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    colors: {{
                        'plasma': {{
                            50: '#eff6ff',
                            500: '#3b82f6', 
                            600: '#2563eb',
                            700: '#1d4ed8'
                        }}
                    }}
                }}
            }}
        }}
    </script>
    
    <style>
        .earnings-card {{transition:all 0.3s ease;background:linear-gradient(135deg,#f0f9ff 0%,#e0f2fe 100%);border-left:4px solid #0ea5e9;}}
        .earnings-card:hover {{transform:translateY(-4px);box-shadow:0 20px 40px rgba(14,165,233,0.15);}}
        .logo {{font-size:1.2rem;font-weight:700;color:#27ae60;text-decoration:none;display:flex;align-items:center;gap:0.6rem;}}
        .logo-icon {{width:32px;height:32px;background:linear-gradient(135deg,#27ae60 0%,#2ecc71 100%);border-radius:6px;display:flex;align-items:center;justify-content:center;color:white;font-weight:700;font-size:12px;box-shadow:0 2px 6px rgba(39,174,96,0.3);}}
        .trust-badge {{background:rgba(39,174,96,0.1);color:#27ae60;padding:0.2rem 0.6rem;border-radius:12px;font-size:0.7rem;font-weight:500;margin-left:0.8rem;white-space:nowrap;}}
        .nav-container {{max-width:1400px;margin:0 auto;display:flex;justify-content:space-between;align-items:center;padding:0 1.5rem;}}
        .nav-links {{display:flex;list-style:none;gap:1.2rem;align-items:center;}}
        .nav-links a {{text-decoration:none;color:#2c3e50;font-weight:500;transition:all 0.3s;padding:0.4rem 0.8rem;border-radius:6px;font-size:0.9rem;white-space:nowrap;}}
        .centers-highlight {{background:linear-gradient(135deg,#27ae60 0%,#2ecc71 100%) !important;color:white !important;border-radius:6px !important;font-weight:700 !important;box-shadow:0 2px 6px rgba(39,174,96,0.3) !important;transform:scale(1.05);}}
        .centers-highlight:hover {{background:linear-gradient(135deg,#219a52 0%,#26be5f 100%) !important;color:white !important;transform:scale(1.08);}}
        .nav-links a:hover,.nav-links a.active {{color:#27ae60;background:rgba(39,174,96,0.1);}}
        .mobile-menu-btn {{display:none;background:none;border:none;color:#2c3e50;font-size:24px;cursor:pointer;}}
        .mobile-menu {{display:none;position:fixed;top:80px;left:0;right:0;background:rgba(255,255,255,0.98);backdrop-filter:blur(10px);border-bottom:1px solid rgba(39,174,96,0.1);z-index:999;padding:1rem;}}
        .mobile-menu.active {{display:block;}}
        nav {{background:rgba(255,255,255,0.95);backdrop-filter:blur(10px);padding:1rem 0;position:fixed;width:100%;top:0;z-index:1000;border-bottom:1px solid rgba(39,174,96,0.1);}}
        body {{padding-top:80px;}}
        @media (max-width:768px) {{.nav-links {{display:none;}}.mobile-menu-btn {{display:block;}}}}
    </style>
</head>
<body class="bg-gray-50">
    <!-- Navigation -->
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
                <li><a href="/topics/requirements-eligibility/">Health</a></li>
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
                <li><a href="/topics/requirements-eligibility/">Health</a></li>
                <li><a href="/faq.html">FAQ</a></li>
            </ul>
        </div>
    </nav>

    <!-- Main Content -->
    <main class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <!-- Article Header -->
        <article class="bg-white rounded-xl shadow-lg overflow-hidden mb-8">
            <div class="bg-gradient-to-r from-green-600 to-emerald-600 px-8 py-12 text-white">
                <div class="max-w-3xl">
                    <div class="flex items-center gap-3 mb-4">
                        <span class="bg-white/20 backdrop-blur-sm px-3 py-1 rounded-full text-sm font-semibold">Plasma Guide 2025</span>
                        <span class="text-green-100">Updated January 2025</span>
                    </div>
                    <h1 class="text-3xl md:text-4xl font-bold mb-4 leading-tight">
                        {article_title}
                    </h1>
                    <p class="text-xl text-green-100 leading-relaxed">
                        {description[:200] if description else 'Your complete guide to plasma donation in 2025.'}
                    </p>
                </div>
            </div>
        </article>
'''

    # Process each section and add it with proper formatting
    for section in sections:
        section_id = section.get('id', '')
        
        # Get section heading
        h2 = section.find(['h2', 'h3'])
        if h2:
            heading_text = h2.get_text(strip=True)
            new_html += f'''
        <section class="mb-12" id="{section_id}">
            <h2 class="text-2xl font-bold text-gray-900 mb-6">{heading_text}</h2>
'''
        else:
            new_html += f'''
        <section class="mb-12">
'''
        
        # Get all paragraphs in the section
        paragraphs = section.find_all('p')
        for p in paragraphs:
            text = p.get_text(strip=True)
            if text:
                new_html += f'''            <p class="text-gray-700 leading-relaxed mb-4">{text}</p>
'''
        
        # Get any lists in the section
        lists = section.find_all(['ul', 'ol'])
        for lst in lists:
            if lst.name == 'ul':
                new_html += '''            <ul class="list-disc list-inside space-y-2 mb-6 text-gray-700">
'''
            else:
                new_html += '''            <ol class="list-decimal list-inside space-y-2 mb-6 text-gray-700">
'''
            
            items = lst.find_all('li')
            for item in items:
                item_text = item.get_text(strip=True)
                if item_text:
                    new_html += f'''                <li>{item_text}</li>
'''
            
            if lst.name == 'ul':
                new_html += '''            </ul>
'''
            else:
                new_html += '''            </ol>
'''
        
        new_html += '''        </section>
'''

    # Add footer
    new_html += '''
        <!-- CTA Section -->
        <div class="bg-gradient-to-r from-green-50 to-emerald-50 border-2 border-green-200 rounded-2xl p-8 mb-8">
            <div class="text-center">
                <h2 class="text-2xl font-bold text-gray-900 mb-4">Calculate Your Plasma Earnings</h2>
                <p class="text-gray-700 mb-6">Use our free calculator to see how much you could earn at centers near you</p>
                <a href="/#calculator" class="inline-flex items-center px-6 py-3 bg-gradient-to-r from-green-600 to-emerald-600 text-white font-semibold rounded-lg hover:from-green-700 hover:to-emerald-700 transition-all duration-200">
                    Calculate My Earnings →
                </a>
            </div>
        </div>
    </main>

    <!-- Footer -->
    <footer class="bg-gray-900 text-gray-400 py-12 mt-20">
        <div class="max-w-7xl mx-auto px-4">
            <div class="text-center">
                <p>&copy; 2025 Plasma Pay Calculator. All rights reserved.</p>
                <div class="mt-4 space-x-6">
                    <a href="/privacy.html" class="hover:text-white">Privacy Policy</a>
                    <a href="/terms.html" class="hover:text-white">Terms of Service</a>
                    <a href="/contact.html" class="hover:text-white">Contact</a>
                </div>
            </div>
        </div>
    </footer>

    <script>
        function toggleMobileMenu() {{
            const menu = document.getElementById('mobileMenu');
            menu.classList.toggle('active');
        }}
    </script>
</body>
</html>'''

    return new_html

def main():
    blog_dir = '/Users/glengomezmeade/Projects/plasma-pay-calculator/blog'
    
    # Process specific problem file first
    problem_file = os.path.join(blog_dir, 'first-time-plasma-donor-guide-2025.html')
    if os.path.exists(problem_file):
        print(f"Fixing {problem_file}...")
        new_content = fix_blog_post(problem_file)
        with open(problem_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed {problem_file}")
    
    # Then process all other blog files
    for filename in os.listdir(blog_dir):
        if filename.endswith('.html') and filename != 'index.html':
            filepath = os.path.join(blog_dir, filename)
            
            # Skip the working one
            if 'how-much-money-can-you-make-donating-plasma-2025' in filename:
                print(f"Skipping already working: {filename}")
                continue
                
            print(f"Fixing {filename}...")
            try:
                new_content = fix_blog_post(filepath)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Fixed {filename}")
            except Exception as e:
                print(f"Error fixing {filename}: {e}")

if __name__ == '__main__':
    main()