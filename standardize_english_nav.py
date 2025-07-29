#!/usr/bin/env python3
"""
Script to standardize navigation and mobile menu across all English pages
"""

import os
import re
from pathlib import Path

# Define the standard English navigation template
ENGLISH_NAV_TEMPLATE = '''<nav>
        <div class="nav-container">
            <div style="display: flex; align-items: center;">
                <a href="/" class="logo">
                    <div class="logo-icon">PPC</div>
                    Plasma Pay Calculator
                </a>
                <div class="trust-badge">Updated for 2025</div>
            </div>
            <ul class="nav-links">
                <li><a href="/" class="active">Calculator</a></li>
                <li><a href="/blog/">Blog</a></li>
                <li><a href="/states.html">States</a></li>
                <li><a href="/centers/">Centers</a></li>
                <li><a href="/faq.html">FAQ</a></li>
                <li><a href="/about.html">About</a></li>
                <li><a href="/es/" class="language-switcher">🇲🇽 Español</a></li>
            </ul>
            <button class="mobile-menu-btn" onclick="toggleMobileMenu()">☰</button>
        </div>
        <div class="mobile-menu" id="mobileMenu">
            <ul>
                <li><a href="/">Calculator</a></li>
                <li><a href="/blog/">Blog</a></li>
                <li><a href="/states.html">States</a></li>
                <li><a href="/centers/">Centers</a></li>
                <li><a href="/faq.html">FAQ</a></li>
                <li><a href="/about.html">About</a></li>
                <li><a href="/es/" class="language-switcher">🇲🇽 Español</a></li>
            </ul>
        </div>
    </nav>'''

# Define the standard CSS for mobile menu
MOBILE_MENU_CSS = '''        .logo {
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

        .mobile-menu a:hover {
            color: #27ae60;
            background: rgba(39, 174, 96, 0.1);
        }

        @media (max-width: 768px) {
            .nav-links {
                display: none;
            }

            .mobile-menu-btn {
                display: block;
            }
        }'''

# JavaScript function for mobile menu
MOBILE_MENU_JS = '''    <script>
        function toggleMobileMenu() {
            const mobileMenu = document.getElementById('mobileMenu');
            mobileMenu.classList.toggle('active');
        }
    </script>'''

def process_html_file(file_path):
    """Process a single HTML file to standardize navigation"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Skip if file already has standardized navigation
        if 'class="mobile-menu"' in content and 'toggleMobileMenu' in content:
            print(f"✓ {file_path} - Already has mobile menu")
            return True
            
        modified = False
        
        # Add mobile menu CSS if not present
        if 'mobile-menu-btn' not in content:
            # Find existing CSS section and add mobile menu CSS
            css_patterns = [
                (r'(</style>)', f'{MOBILE_MENU_CSS}\n        \\1'),
                (r'(\.nav-links\s*\{[^}]*\})', f'\\1\n\n{MOBILE_MENU_CSS}'),
            ]
            
            for pattern, replacement in css_patterns:
                if re.search(pattern, content, re.DOTALL):
                    content = re.sub(pattern, replacement, content, flags=re.DOTALL)
                    modified = True
                    break
        
        # Replace navigation structure if it exists
        nav_patterns = [
            r'<nav[^>]*>.*?</nav>',
            r'<header[^>]*>.*?</header>',
        ]
        
        for pattern in nav_patterns:
            if re.search(pattern, content, re.DOTALL | re.IGNORECASE):
                content = re.sub(pattern, ENGLISH_NAV_TEMPLATE, content, flags=re.DOTALL | re.IGNORECASE)
                modified = True
                break
        
        # Add JavaScript function if not present
        if 'toggleMobileMenu' not in content:
            content = content.replace('</body>', f'{MOBILE_MENU_JS}\n</body>')
            modified = True
        
        if modified:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ {file_path} - Updated with mobile navigation")
            return True
        else:
            print(f"- {file_path} - No navigation found to update")
            return False
            
    except Exception as e:
        print(f"✗ {file_path} - Error: {e}")
        return False

def main():
    """Main function to process all English HTML files"""
    base_dir = Path('/Users/glengomezmeade/plasma-pay-calculator')
    
    # Files to process (excluding Spanish /es/ directory)
    html_files = []
    
    # Root level HTML files
    for file in base_dir.glob('*.html'):
        html_files.append(file)
    
    # Blog files
    blog_dir = base_dir / 'blog'
    if blog_dir.exists():
        for file in blog_dir.glob('*.html'):
            html_files.append(file)
    
    # Centers files
    centers_dir = base_dir / 'centers'
    if centers_dir.exists():
        for file in centers_dir.rglob('*.html'):
            html_files.append(file)
    
    # Health files
    health_dir = base_dir / 'health'
    if health_dir.exists():
        for file in health_dir.rglob('*.html'):
            html_files.append(file)
    
    # Calculator files (English only)
    calc_dir = base_dir / 'calculators' 
    if calc_dir.exists():
        for file in calc_dir.rglob('*.html'):
            html_files.append(file)
    
    print(f"Processing {len(html_files)} English HTML files...\n")
    
    processed = 0
    updated = 0
    
    for file_path in html_files:
        if process_html_file(file_path):
            updated += 1
        processed += 1
    
    print(f"\nCompleted: {processed} files processed, {updated} files updated with mobile navigation")

if __name__ == "__main__":
    main()