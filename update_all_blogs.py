#!/usr/bin/env python3
"""
Update all blog posts to match the Tailwind CSS format of the reference blog
"""

import os
import re
from pathlib import Path
from bs4 import BeautifulSoup

def extract_content_sections(soup):
    """Extract the main content from existing blog posts"""
    content_parts = {
        'title': '',
        'meta_desc': '',
        'keywords': '',
        'canonical': '',
        'schema': [],
        'article_content': ''
    }
    
    # Get title
    title_tag = soup.find('title')
    if title_tag:
        content_parts['title'] = title_tag.string or ''
    
    # Get meta description
    meta_desc = soup.find('meta', {'name': 'description'})
    if meta_desc:
        content_parts['meta_desc'] = meta_desc.get('content', '')
    
    # Get keywords
    meta_keywords = soup.find('meta', {'name': 'keywords'})
    if meta_keywords:
        content_parts['keywords'] = meta_keywords.get('content', '')
    
    # Get canonical
    canonical = soup.find('link', {'rel': 'canonical'})
    if canonical:
        content_parts['canonical'] = canonical.get('href', '')
    
    # Get schema scripts
    schema_scripts = soup.find_all('script', type='application/ld+json')
    for script in schema_scripts[:2]:  # Max 2 schemas
        if script.string:
            content_parts['schema'].append(script.string)
    
    # Extract article content
    # Try to find main content area
    main = soup.find('main')
    if main:
        # Remove nav and footer if present
        for tag in main.find_all(['nav', 'footer']):
            tag.decompose()
        content_parts['article_content'] = str(main.decode_contents())
    else:
        # Try article tag
        article = soup.find('article')
        if article:
            content_parts['article_content'] = str(article.decode_contents())
        else:
            # Get content sections
            sections = []
            for elem in soup.find_all(['div', 'section'], class_=re.compile('article-header|content-section|container')):
                sections.append(str(elem))
            if sections:
                content_parts['article_content'] = '\n'.join(sections)
            else:
                # Fallback: get body content
                body = soup.find('body')
                if body:
                    for tag in body.find_all(['nav', 'footer', 'script', 'style']):
                        tag.decompose()
                    content_parts['article_content'] = str(body.decode_contents())
    
    return content_parts

def convert_old_classes_to_tailwind(html_content):
    """Convert old CSS classes to Tailwind classes"""
    # Parse the HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Class mappings
    class_mappings = {
        'article-header': 'bg-white rounded-xl shadow-lg overflow-hidden mb-8',
        'content-section': 'mb-12',
        'highlight-box': 'bg-gradient-to-r from-blue-600 to-indigo-600 text-white p-6 rounded-xl text-center my-6',
        'warning-box': 'bg-yellow-50 border-l-4 border-yellow-500 p-6 mb-8 rounded-r-lg',
        'info-box': 'bg-blue-50 border border-blue-200 rounded-lg p-6',
        'comparison-table': 'bg-white rounded-xl shadow-md overflow-hidden',
        'cta-section': 'bg-gradient-to-r from-green-600 to-emerald-600 rounded-xl p-8 text-white',
        'form-example': 'bg-gray-100 border-2 border-gray-300 p-6 rounded-xl my-6 font-mono text-sm',
        'earnings-card': 'bg-white rounded-xl shadow-md p-6',
        'income-tier': 'bg-white rounded-xl shadow-md p-6',
        'paystub-card': 'bg-yellow-50 border border-yellow-200 rounded-xl p-6'
    }
    
    # Replace classes
    for old_class, new_classes in class_mappings.items():
        for elem in soup.find_all(class_=old_class):
            elem['class'] = new_classes.split()
    
    # Update headers if they don't have classes
    for h1 in soup.find_all('h1'):
        if not h1.get('class'):
            h1['class'] = 'text-3xl md:text-4xl font-bold mb-4 leading-tight'
    
    for h2 in soup.find_all('h2'):
        if not h2.get('class'):
            h2['class'] = 'text-2xl font-bold text-gray-900 mb-6'
    
    for h3 in soup.find_all('h3'):
        if not h3.get('class'):
            h3['class'] = 'text-xl font-bold text-gray-900'
    
    # Update paragraphs
    for p in soup.find_all('p'):
        if not p.get('class') and p.parent.name not in ['li', 'td', 'th']:
            p['class'] = 'text-gray-600 leading-relaxed mb-4'
    
    # Update lists
    for ul in soup.find_all('ul'):
        if not ul.get('class'):
            ul['class'] = 'space-y-2 text-gray-700'
    
    # Update tables
    for table in soup.find_all('table'):
        if not table.get('class'):
            table['class'] = 'w-full'
    
    for th in soup.find_all('th'):
        if not th.get('class'):
            th['class'] = 'px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider'
    
    for td in soup.find_all('td'):
        if not td.get('class'):
            td['class'] = 'px-6 py-4 whitespace-nowrap text-sm'
    
    return str(soup)

def create_tailwind_blog(content_parts):
    """Create a properly formatted blog post with Tailwind CSS"""
    
    # Build schema scripts
    schema_html = ''
    for schema in content_parts['schema']:
        schema_html += f'<script type="application/ld+json">\n{schema}\n</script>\n'
    
    # Convert content to Tailwind
    article_content = convert_old_classes_to_tailwind(content_parts['article_content'])
    
    template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{content_parts['title']}</title>
    <meta name="description" content="{content_parts['meta_desc']}">
    <meta name="keywords" content="{content_parts['keywords']}">
    <link rel="canonical" href="{content_parts['canonical']}">
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
    
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    colors: {{
                        'plasma-green': '#27ae60',
                        'plasma-green-dark': '#219a52',
                    }}
                }}
            }}
        }}
    </script>
    
    {schema_html}
</head>
<body class="bg-gray-50">
    <!-- Navigation -->
    <nav class="fixed top-0 w-full bg-white/95 backdrop-blur-md shadow-sm z-50 border-b border-gray-100">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between items-center h-16">
                <div class="flex items-center">
                    <a href="/" class="flex items-center space-x-2">
                        <div class="w-8 h-8 bg-gradient-to-br from-plasma-green to-green-500 rounded-lg flex items-center justify-center text-white font-bold text-xs">
                            PPC
                        </div>
                        <span class="font-bold text-lg text-gray-900">Plasma Pay Calculator</span>
                    </a>
                    <span class="ml-3 px-2 py-1 bg-green-100 text-plasma-green text-xs font-medium rounded-full">
                        Updated 2025
                    </span>
                </div>
                <div class="hidden md:flex items-center space-x-4">
                    <a href="/#calculator" class="text-gray-600 hover:text-plasma-green transition-colors px-3 py-2 rounded-md text-sm font-medium">Calculator</a>
                    <a href="/blog/" class="text-gray-600 hover:text-plasma-green transition-colors px-3 py-2 rounded-md text-sm font-medium">Blog</a>
                    <a href="/states.html" class="text-gray-600 hover:text-plasma-green transition-colors px-3 py-2 rounded-md text-sm font-medium">States</a>
                    <a href="/centers/" class="bg-gradient-to-r from-plasma-green to-green-500 text-white px-4 py-2 rounded-md text-sm font-bold hover:scale-105 transition-transform shadow-md">
                        🏥 Centers
                    </a>
                    <a href="/topics/requirements-eligibility/" class="text-gray-600 hover:text-plasma-green transition-colors px-3 py-2 rounded-md text-sm font-medium">Health</a>
                    <a href="/faq.html" class="text-gray-600 hover:text-plasma-green transition-colors px-3 py-2 rounded-md text-sm font-medium">FAQ</a>
                </div>
                <button class="md:hidden text-gray-600" onclick="toggleMobileMenu()">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
                    </svg>
                </button>
            </div>
        </div>
    </nav>

    <!-- Mobile Menu -->
    <div id="mobileMenu" class="hidden fixed top-16 left-0 right-0 bg-white shadow-lg z-40 md:hidden">
        <div class="px-2 pt-2 pb-3 space-y-1">
            <a href="/#calculator" class="block px-3 py-2 text-gray-600 hover:text-plasma-green hover:bg-gray-50 rounded-md">Calculator</a>
            <a href="/blog/" class="block px-3 py-2 text-gray-600 hover:text-plasma-green hover:bg-gray-50 rounded-md">Blog</a>
            <a href="/states.html" class="block px-3 py-2 text-gray-600 hover:text-plasma-green hover:bg-gray-50 rounded-md">States</a>
            <a href="/centers/" class="block px-3 py-2 bg-gradient-to-r from-plasma-green to-green-500 text-white rounded-md font-bold">🏥 Centers</a>
            <a href="/topics/requirements-eligibility/" class="block px-3 py-2 text-gray-600 hover:text-plasma-green hover:bg-gray-50 rounded-md">Health</a>
            <a href="/faq.html" class="block px-3 py-2 text-gray-600 hover:text-plasma-green hover:bg-gray-50 rounded-md">FAQ</a>
        </div>
    </div>

    <!-- Main Content -->
    <main class="pt-20 pb-16">
        <article class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
            {article_content}
        </article>
    </main>

    <!-- Footer -->
    <footer class="bg-gray-900 text-gray-300 py-12">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <div>
                    <h4 class="text-white font-bold mb-4">Plasma Pay Calculator</h4>
                    <p class="text-sm">Get accurate plasma donation income estimates with current 2025 rates.</p>
                </div>
                <div>
                    <h4 class="text-white font-bold mb-4">Resources</h4>
                    <ul class="space-y-2 text-sm">
                        <li><a href="/calculators/california/" class="hover:text-white transition-colors">Earnings Calculator</a></li>
                        <li><a href="/blog/" class="hover:text-white transition-colors">Income Tips</a></li>
                        <li><a href="/faq.html" class="hover:text-white transition-colors">FAQ</a></li>
                    </ul>
                </div>
                <div>
                    <h4 class="text-white font-bold mb-4">Legal</h4>
                    <ul class="space-y-2 text-sm">
                        <li><a href="/about.html" class="hover:text-white transition-colors">About</a></li>
                        <li><a href="/privacy" class="hover:text-white transition-colors">Privacy Policy</a></li>
                        <li><a href="/terms" class="hover:text-white transition-colors">Terms of Service</a></li>
                        <li><a href="/contact" class="hover:text-white transition-colors">Contact</a></li>
                    </ul>
                </div>
            </div>
            <div class="mt-8 pt-8 border-t border-gray-800 text-center text-sm">
                <p>&copy; 2025 Plasma Pay Calculator. Information for educational purposes.</p>
            </div>
        </div>
    </footer>

    <script>
        function toggleMobileMenu() {{
            const menu = document.getElementById('mobileMenu');
            menu.classList.toggle('hidden');
        }}
    </script>
</body>
</html>"""
    
    return template

def main():
    """Update all blog posts to proper Tailwind format"""
    blog_dir = Path('./blog')
    blog_files = list(blog_dir.glob('*.html'))
    
    # Skip these files
    skip_files = ['index.html', 'how-much-money-can-you-make-donating-plasma-2025.html']
    
    updated = 0
    errors = 0
    
    print(f"Updating {len(blog_files)} blog files to Tailwind format...")
    
    for blog_file in blog_files:
        if blog_file.name in skip_files:
            continue
        
        try:
            # Read current file
            with open(blog_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Skip if already has proper Tailwind
            if 'tailwindcss.com' in content and 'bg-gray-50' in content:
                print(f"✓ Already formatted: {blog_file.name}")
                continue
            
            # Parse and extract content
            soup = BeautifulSoup(content, 'html.parser')
            content_parts = extract_content_sections(soup)
            
            # Create new Tailwind version
            new_html = create_tailwind_blog(content_parts)
            
            # Write updated file
            with open(blog_file, 'w', encoding='utf-8') as f:
                f.write(new_html)
            
            updated += 1
            print(f"✅ Updated: {blog_file.name}")
            
        except Exception as e:
            errors += 1
            print(f"❌ Error with {blog_file.name}: {e}")
    
    print(f"\n✨ Complete!")
    print(f"  Updated: {updated} files")
    print(f"  Errors: {errors} files")
    print(f"  Skipped: {len(skip_files)} files")

if __name__ == "__main__":
    main()