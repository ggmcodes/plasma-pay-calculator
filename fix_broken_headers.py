#!/usr/bin/env python3
"""
Script to fix broken headers by copying the correct navigation from index.html
"""

import os
import re
from pathlib import Path

# The correct navigation HTML with styles
CORRECT_NAV_HTML = '''    <!-- Navigation -->
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
                <li><a href="/centers/">Centers</a></li>
                <li><a href="/health/">Health</a></li>
                <li><a href="/process/">Process</a></li>
                <li><a href="/faq.html">FAQ</a></li>
            </ul>
            <button class="mobile-menu-btn" onclick="toggleMobileMenu()">☰</button>
        </div>
        <div class="mobile-menu" id="mobileMenu">
            <ul>
                <li><a href="/#calculator">Calculator</a></li>
                <li><a href="/blog/">Blog</a></li>
                <li><a href="/states.html">States</a></li>
                <li><a href="/centers/">Centers</a></li>
                <li><a href="/health/">Health</a></li>
                <li><a href="/process/">Process</a></li>
                <li><a href="/faq.html">FAQ</a></li>
            </ul>
        </div>
    </nav>'''

# Navigation CSS styles
NAV_STYLES = '''        /* Navigation */
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

        /* Add padding to body to account for fixed nav */
        body {
            padding-top: 80px;
        }'''

# Mobile menu JavaScript
MOBILE_MENU_JS = '''    <script>
        function toggleMobileMenu() {
            const menu = document.getElementById('mobileMenu');
            menu.classList.toggle('active');
        }
    </script>'''

def fix_file_header(file_path):
    """Fix the header in a single file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Skip Spanish files
        if '/es/' in str(file_path):
            return False, "Spanish file - skipping"
        
        # Remove any existing broken header/nav sections
        # Look for various header patterns
        header_patterns = [
            r'<header[^>]*>.*?</header>',
            r'<nav[^>]*>.*?</nav>',
        ]
        
        for pattern in header_patterns:
            content = re.sub(pattern, '', content, flags=re.DOTALL)
        
        # Check if file has proper style section
        if '<style>' not in content:
            # Add style tag before </head>
            head_end = content.find('</head>')
            if head_end > -1:
                style_section = '\n    <style>\n' + NAV_STYLES + '\n    </style>\n'
                content = content[:head_end] + style_section + content[head_end:]
        else:
            # Check if navigation styles exist
            if 'nav {' not in content:
                # Find the closing style tag and insert nav styles
                style_close = content.find('</style>')
                if style_close > -1:
                    content = content[:style_close] + '\n' + NAV_STYLES + '\n' + content[style_close:]
        
        # Find body tag and insert navigation after it
        body_match = re.search(r'<body[^>]*>', content)
        if body_match:
            insert_pos = body_match.end()
            content = content[:insert_pos] + '\n' + CORRECT_NAV_HTML + '\n' + content[insert_pos:]
        else:
            return False, "No body tag found"
        
        # Add mobile menu JavaScript before </body> if not present
        if 'toggleMobileMenu' not in content:
            body_end = content.rfind('</body>')
            if body_end > -1:
                content = content[:body_end] + '\n' + MOBILE_MENU_JS + '\n' + content[body_end:]
        
        # Write the fixed content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True, "Fixed successfully"
        
    except Exception as e:
        return False, f"Error: {str(e)}"

def find_all_html_files():
    """Find all HTML files that need fixing"""
    root_path = Path("/Users/glengomezmeade/plasma-pay-calculator")
    html_files = []
    
    # Get all HTML files
    for file_path in root_path.rglob("*.html"):
        # Skip Spanish files
        if '/es/' in str(file_path):
            continue
        # Skip certain system files
        if any(skip in str(file_path) for skip in ['node_modules', '.git', 'backup']):
            continue
        html_files.append(file_path)
    
    return html_files

def main():
    """Main function to fix all headers"""
    print("🔧 Fixing Broken Headers...")
    print("=" * 50)
    
    html_files = find_all_html_files()
    print(f"Found {len(html_files)} HTML files to check\n")
    
    fixed_count = 0
    error_count = 0
    
    # Priority files that were mentioned as broken
    priority_files = [
        'index.html',
        'states.html', 
        'faq.html',
        'contact.html',
        'process/index.html',
        'health/index.html',
        'centers/index.html',
        'blog/index.html'
    ]
    
    # Process priority files first
    print("📍 Processing priority files...")
    for filename in priority_files:
        for file_path in html_files:
            if filename in str(file_path):
                success, message = fix_file_header(file_path)
                if success:
                    fixed_count += 1
                    print(f"✅ Fixed: {file_path.name}")
                else:
                    error_count += 1
                    print(f"❌ Error: {file_path.name} - {message}")
    
    # Process remaining files
    print("\n🔄 Processing all other files...")
    processed_files = set()
    for file_path in html_files:
        if file_path not in processed_files:
            success, message = fix_file_header(file_path)
            processed_files.add(file_path)
            
            if success:
                fixed_count += 1
                if fixed_count % 50 == 0:
                    print(f"   Progress: {fixed_count} files fixed...")
            else:
                if "Spanish file" not in message:
                    error_count += 1
    
    print(f"\n✨ Header Fix Complete!")
    print(f"   Fixed: {fixed_count} files")
    print(f"   Errors: {error_count} files")
    print(f"   Total processed: {len(html_files)} files")

if __name__ == "__main__":
    main()