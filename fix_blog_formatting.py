#!/usr/bin/env python3
"""
Script to fix blog post formatting issues and standardize with Tailwind CSS
"""

import os
import re
from pathlib import Path

# Files with specific issues to fix
CALIFORNIA_SPECIFIC_FILES = {
    'plasma-center-comparison.html': 'California Plasma Center Comparison Guide 2025',
    'plasma-donation-health-tips.html': 'California Plasma Donation Health Tips & Safety Guide 2025',
    'plasma-donation-schedule.html': 'California Plasma Donation Schedule Optimization Guide 2025',
    'plasma-donation-taxes.html': 'California Plasma Donation Tax Guide 2025 - IRS Requirements'
}

FORMATTING_ISSUES_FILES = [
    'best-plasma-centers-texas.html',
    'first-time-plasma-donation-what-to-expect.html',
    'plasma-donation-bonuses-promotions.html',
    'understanding-plasma-medical-uses.html',
    'plasma-donation-tips-beginners.html',
    'plasma-donation-weight-requirements.html',
    'can-you-donate-plasma-with-tattoos.html',
    'can-you-donate-plasma-twice-a-week.html',
    'biolife-vs-csl-plasma-comparison.html',
    'state-by-state-plasma-donation-laws-regulations-2025.html',
    'comprehensive-plasma-tax-guide-2025.html',
    'plasma-donation-side-effects-safety-guide.html',
    'weight-requirements-maximum-pay-guide.html',
    'complete-medical-eligibility-guide-plasma-donation.html',
    'csl-biolife-octapharma-comparison-guide.html'
]

# Standard header template with Tailwind CSS
STANDARD_HEADER = '''    <header class="bg-white shadow-lg sticky top-0 z-50">
        <div class="container mx-auto px-4 py-3">
            <div class="flex items-center justify-between">
                <!-- Logo -->
                <div class="flex items-center space-x-2">
                    <div class="w-8 h-8 bg-red-600 rounded-full flex items-center justify-center">
                        <span class="text-white font-bold text-sm">🩸</span>
                    </div>
                    <a href="/" class="text-xl font-bold text-gray-800 hover:text-red-600 transition-colors">
                        Plasma Pay Calculator
                    </a>
                </div>

                <!-- Desktop Navigation -->
                <nav class="hidden md:flex items-center space-x-6">
                    <a href="/calculators/" class="text-gray-700 hover:text-red-600 font-medium transition-colors">State Calculators</a>
                    <a href="/centers/" class="text-gray-700 hover:text-red-600 font-medium transition-colors">Find Centers</a>
                    <a href="/health/" class="text-gray-700 hover:text-red-600 font-medium transition-colors">Health Guide</a>
                    <a href="/blog/" class="text-gray-700 hover:text-red-600 font-medium transition-colors">Blog</a>
                    <div class="language-switcher">
                        <select id="languageSelect" class="bg-gray-100 border border-gray-300 rounded px-3 py-1 text-sm focus:outline-none focus:ring-2 focus:ring-red-500">
                            <option value="en">🇺🇸 English</option>
                            <option value="es">🇪🇸 Español</option>
                        </select>
                    </div>
                </nav>

                <!-- Mobile Menu Button -->
                <button id="mobileMenuBtn" class="md:hidden p-2 rounded-lg hover:bg-gray-100 transition-colors">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
                    </svg>
                </button>
            </div>

            <!-- Mobile Navigation Menu -->
            <div id="mobileMenu" class="md:hidden mt-4 pb-4 border-t border-gray-200 hidden">
                <div class="flex flex-col space-y-3 pt-4">
                    <a href="/calculators/" class="text-gray-700 hover:text-red-600 font-medium py-2 transition-colors">State Calculators</a>
                    <a href="/centers/" class="text-gray-700 hover:text-red-600 font-medium py-2 transition-colors">Find Centers</a>
                    <a href="/health/" class="text-gray-700 hover:text-red-600 font-medium py-2 transition-colors">Health Guide</a>
                    <a href="/blog/" class="text-gray-700 hover:text-red-600 font-medium py-2 transition-colors">Blog</a>
                    <div class="py-2">
                        <select id="mobileLanguageSelect" class="bg-gray-100 border border-gray-300 rounded px-3 py-2 text-sm w-full focus:outline-none focus:ring-2 focus:ring-red-500">
                            <option value="en">🇺🇸 English</option>
                            <option value="es">🇪🇸 Español</option>
                        </select>
                    </div>
                </div>
            </div>
        </div>
    </header>'''

# Mobile menu JavaScript
MOBILE_MENU_JS = '''        // Mobile menu functionality
        document.addEventListener('DOMContentLoaded', function() {
            const mobileMenuBtn = document.getElementById('mobileMenuBtn');
            const mobileMenu = document.getElementById('mobileMenu');
            
            if (mobileMenuBtn && mobileMenu) {
                mobileMenuBtn.addEventListener('click', function() {
                    mobileMenu.classList.toggle('hidden');
                });
            }

            // Language switcher functionality
            const languageSelect = document.getElementById('languageSelect');
            const mobileLanguageSelect = document.getElementById('mobileLanguageSelect');
            
            function handleLanguageChange(selectedLang) {
                if (selectedLang === 'es') {
                    const currentPath = window.location.pathname;
                    let spanishPath;
                    
                    if (currentPath === '/' || currentPath === '/index.html') {
                        spanishPath = '/es/';
                    } else {
                        spanishPath = '/es' + currentPath;
                    }
                    
                    window.location.href = spanishPath;
                }
            }
            
            if (languageSelect) {
                languageSelect.addEventListener('change', function() {
                    handleLanguageChange(this.value);
                });
            }
            
            if (mobileLanguageSelect) {
                mobileLanguageSelect.addEventListener('change', function() {
                    handleLanguageChange(this.value);
                });
            }
        });'''

# Tailwind CSS link
TAILWIND_LINK = '''    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>'''

def fix_california_titles(file_path, new_title):
    """Fix California-specific blog posts to mention California in title"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update title tag
        title_pattern = r'<title>.*?</title>'
        content = re.sub(title_pattern, f'<title>{new_title}</title>', content, flags=re.DOTALL)
        
        # Update h1 tag
        h1_pattern = r'<h1[^>]*>.*?</h1>'
        h1_match = re.search(h1_pattern, content, re.DOTALL)
        if h1_match:
            # Extract any classes or attributes
            h1_tag_start = re.match(r'<h1[^>]*>', h1_match.group(0))
            if h1_tag_start:
                new_h1 = f'{h1_tag_start.group(0)}{new_title}</h1>'
                content = content.replace(h1_match.group(0), new_h1)
        
        # Update meta description if it exists
        desc_pattern = r'<meta name="description" content="([^"]*)"'
        desc_match = re.search(desc_pattern, content)
        if desc_match:
            old_desc = desc_match.group(1)
            if 'california' not in old_desc.lower():
                new_desc = f"California guide: {old_desc}"
                content = content.replace(
                    f'<meta name="description" content="{old_desc}"',
                    f'<meta name="description" content="{new_desc}"'
                )
        
        return content
    except Exception as e:
        print(f"Error fixing California titles: {str(e)}")
        return None

def fix_blog_formatting(file_path):
    """Fix blog post formatting with proper Tailwind CSS"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if file already has Tailwind
        if 'cdn.tailwindcss.com' not in content:
            # Add Tailwind CSS before </head>
            head_end = content.find('</head>')
            if head_end > -1:
                content = content[:head_end] + TAILWIND_LINK + '\n' + content[head_end:]
        
        # Remove duplicate navigation sections
        nav_pattern = r'<nav[^>]*>.*?</nav>'
        nav_matches = list(re.finditer(nav_pattern, content, re.DOTALL))
        
        # Keep only the first nav and remove others
        if len(nav_matches) > 1:
            for match in reversed(nav_matches[1:]):
                content = content[:match.start()] + content[match.end():]
        
        # Replace old header with new standardized header
        header_pattern = r'<header[^>]*>.*?</header>'
        header_match = re.search(header_pattern, content, re.DOTALL)
        
        if header_match:
            content = content.replace(header_match.group(0), STANDARD_HEADER)
        else:
            # Insert header after body tag
            body_match = re.search(r'<body[^>]*>', content)
            if body_match:
                insert_pos = body_match.end()
                content = content[:insert_pos] + '\n' + STANDARD_HEADER + '\n' + content[insert_pos:]
        
        # Fix main content wrapper - use Tailwind classes
        main_pattern = r'<main[^>]*class="[^"]*"[^>]*>'
        main_match = re.search(main_pattern, content)
        if main_match:
            content = re.sub(main_pattern, '<main class="min-h-screen bg-gray-50">', content)
        else:
            content = re.sub(r'<main[^>]*>', '<main class="min-h-screen bg-gray-50">', content)
        
        # Fix article wrapper
        article_pattern = r'<article[^>]*class="[^"]*"[^>]*>'
        article_match = re.search(article_pattern, content)
        if article_match:
            content = re.sub(article_pattern, '<article class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-12">', content)
        else:
            content = re.sub(r'<article[^>]*>', '<article class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-12">', content)
        
        # Fix breadcrumb styling
        breadcrumb_pattern = r'<div[^>]*class="breadcrumb[^"]*"[^>]*>'
        content = re.sub(breadcrumb_pattern, '<div class="flex items-center space-x-2 text-sm text-gray-600 mb-8">', content)
        
        # Fix h1 styling
        h1_pattern = r'<h1[^>]*>'
        content = re.sub(h1_pattern, '<h1 class="text-4xl md:text-5xl font-bold text-gray-900 mb-6">', content)
        
        # Fix h2 styling
        h2_pattern = r'<h2[^>]*>'
        content = re.sub(h2_pattern, '<h2 class="text-2xl md:text-3xl font-bold text-gray-900 mt-8 mb-4">', content)
        
        # Fix h3 styling
        h3_pattern = r'<h3[^>]*>'
        content = re.sub(h3_pattern, '<h3 class="text-xl md:text-2xl font-bold text-gray-800 mt-6 mb-3">', content)
        
        # Fix paragraph styling
        p_pattern = r'<p(?![^>]*class=)'
        content = re.sub(p_pattern, '<p class="text-gray-700 leading-relaxed mb-4"', content)
        
        # Add mobile menu JS if not present
        if 'mobileMenuBtn' not in content:
            # Find the closing script tag before </body>
            script_pattern = r'</script>\s*</body>'
            script_match = re.search(script_pattern, content, re.IGNORECASE)
            
            if script_match:
                insert_pos = script_match.start()
                content = content[:insert_pos] + MOBILE_MENU_JS + '\n        ' + content[insert_pos:]
            else:
                # Insert before </body>
                body_end_match = re.search(r'</body>', content, re.IGNORECASE)
                if body_end_match:
                    insert_pos = body_end_match.start()
                    content = content[:insert_pos] + '\n    <script>\n' + MOBILE_MENU_JS + '\n    </script>\n' + content[insert_pos:]
        
        return content
        
    except Exception as e:
        print(f"Error fixing formatting: {str(e)}")
        return None

def main():
    """Main function to fix all blog issues"""
    blog_path = Path("/Users/glengomezmeade/plasma-pay-calculator/blog")
    
    print("🔧 Fixing Blog Post Issues...")
    print("=" * 50)
    
    # Fix California-specific titles
    print("\n📍 Fixing California-specific titles...")
    for filename, new_title in CALIFORNIA_SPECIFIC_FILES.items():
        file_path = blog_path / filename
        if file_path.exists():
            content = fix_california_titles(file_path, new_title)
            if content:
                # Also apply formatting fixes
                content = fix_blog_formatting(file_path)
                if content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"✅ Fixed: {filename} -> {new_title}")
                else:
                    print(f"❌ Failed to fix formatting: {filename}")
            else:
                print(f"❌ Failed to fix title: {filename}")
        else:
            print(f"⚠️  File not found: {filename}")
    
    # Fix formatting issues
    print("\n🎨 Fixing formatting issues...")
    for filename in FORMATTING_ISSUES_FILES:
        file_path = blog_path / filename
        if file_path.exists():
            content = fix_blog_formatting(file_path)
            if content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✅ Fixed formatting: {filename}")
            else:
                print(f"❌ Failed to fix: {filename}")
        else:
            print(f"⚠️  File not found: {filename}")
    
    # Check for files that might not exist with exact names
    print("\n🔍 Checking for similar files...")
    all_blog_files = list(blog_path.glob("*.html"))
    
    # Files that were mentioned but might have different names
    problematic_patterns = [
        'weight-requirements',
        'tax-guide',
        'side-effects',
        'medical-eligibility',
        'csl-biolife'
    ]
    
    for pattern in problematic_patterns:
        matching_files = [f for f in all_blog_files if pattern in f.name.lower()]
        if matching_files:
            for file_path in matching_files:
                if file_path.name not in FORMATTING_ISSUES_FILES:
                    content = fix_blog_formatting(file_path)
                    if content:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(content)
                        print(f"✅ Fixed additional file: {file_path.name}")
    
    print("\n✨ Blog formatting fixes complete!")

if __name__ == "__main__":
    main()