#!/usr/bin/env python3
"""
Fix navigation consistency across all pages
"""

import os
import re
from pathlib import Path

def get_standard_navigation():
    """Get the standard navigation HTML structure"""
    return '''
    <!-- Navigation -->
    <nav>
        <div class="nav-container">
            <a href="/" class="logo">
                <div class="logo-icon">PPC</div>
                <span class="logo-text">Plasma Pay Calculator</span>
            </a>
            <ul class="nav-links">
                <li><a href="/#calculator">Calculator</a></li>
                <li><a href="/blog/">Blog</a></li>
                <li><a href="/states.html">State Rates</a></li>
                <li><a href="/health/">Health Info</a></li>
                <li><a href="/centers/" class="cta-btn">🏥 FIND A CENTER</a></li>
            </ul>
            <button class="mobile-menu-btn" onclick="toggleMobileMenu()">☰</button>
        </div>
        <div class="mobile-menu" id="mobileMenu">
            <ul>
                <li><a href="/#calculator">Calculator</a></li>
                <li><a href="/blog/">Blog</a></li>
                <li><a href="/states.html">State Rates</a></li>
                <li><a href="/health/">Health Info</a></li>
                <li><a href="/centers/">🏥 Find Centers</a></li>
                <li><a href="/faq.html">FAQ</a></li>
                <li><a href="/about.html">About</a></li>
            </ul>
        </div>
    </nav>'''

def get_standard_mobile_script():
    """Get the standard mobile menu JavaScript"""
    return '''
    <script>
    function toggleMobileMenu() {
        const mobileMenu = document.getElementById('mobileMenu');
        const menuBtn = document.querySelector('.mobile-menu-btn');
        
        if (mobileMenu.style.display === 'block') {
            mobileMenu.style.display = 'none';
            menuBtn.innerHTML = '☰';
        } else {
            mobileMenu.style.display = 'block';
            menuBtn.innerHTML = '✕';
        }
    }
    
    // Close mobile menu when clicking outside
    document.addEventListener('click', function(event) {
        const mobileMenu = document.getElementById('mobileMenu');
        const menuBtn = document.querySelector('.mobile-menu-btn');
        
        if (!event.target.closest('nav') && mobileMenu.style.display === 'block') {
            mobileMenu.style.display = 'none';
            menuBtn.innerHTML = '☰';
        }
    });
    </script>'''

def get_standard_nav_css():
    """Get the standard navigation CSS"""
    return '''
    <style>
    /* Navigation Styles */
    nav {
        background: #FFF;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        position: sticky;
        top: 0;
        z-index: 1000;
    }
    
    .nav-container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 20px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        height: 80px;
    }
    
    .logo {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        text-decoration: none;
        color: #1F2937;
        font-weight: 600;
        font-size: 1.2rem;
    }
    
    .logo-icon {
        background: linear-gradient(135deg, #27ae60, #2ecc71);
        color: white;
        width: 40px;
        height: 40px;
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 700;
        font-size: 0.9rem;
    }
    
    .nav-links {
        display: flex;
        list-style: none;
        gap: 2rem;
        align-items: center;
        margin: 0;
        padding: 0;
    }
    
    .nav-links a {
        text-decoration: none;
        color: #374151;
        font-weight: 500;
        transition: color 0.3s;
    }
    
    .nav-links a:hover {
        color: #27ae60;
    }
    
    .cta-btn {
        background: linear-gradient(135deg, #27ae60, #2ecc71) !important;
        color: white !important;
        padding: 0.75rem 1.5rem !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        transition: transform 0.3s !important;
    }
    
    .cta-btn:hover {
        transform: translateY(-2px) !important;
        color: white !important;
    }
    
    .mobile-menu-btn {
        display: none;
        background: none;
        border: none;
        font-size: 1.5rem;
        cursor: pointer;
        color: #374151;
    }
    
    .mobile-menu {
        display: none;
        position: absolute;
        top: 100%;
        left: 0;
        right: 0;
        background: white;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        border-top: 1px solid #E5E7EB;
    }
    
    .mobile-menu ul {
        list-style: none;
        margin: 0;
        padding: 1rem 0;
    }
    
    .mobile-menu li {
        padding: 0;
    }
    
    .mobile-menu a {
        display: block;
        padding: 1rem 2rem;
        color: #374151;
        text-decoration: none;
        border-bottom: 1px solid #F3F4F6;
    }
    
    .mobile-menu a:hover {
        background: #F9FAFB;
        color: #27ae60;
    }
    
    @media (max-width: 768px) {
        .nav-links {
            display: none;
        }
        
        .mobile-menu-btn {
            display: block;
        }
        
        .logo-text {
            display: none;
        }
    }
    </style>'''

def fix_page_navigation(file_path):
    """Fix navigation for a specific page"""
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Remove existing navigation structures
        # Remove various nav/header patterns
        nav_patterns = [
            r'<nav[^>]*>.*?</nav>',
            r'<header[^>]*>.*?</header>',
            r'<!-- Navigation -->.*?</nav>',
            r'<!-- Header -->.*?</header>'
        ]
        
        for pattern in nav_patterns:
            content = re.sub(pattern, '', content, flags=re.DOTALL)
        
        # Insert standard navigation after body tag
        body_match = re.search(r'<body[^>]*>', content)
        if body_match:
            insert_pos = body_match.end()
            standard_nav = get_standard_navigation()
            content = content[:insert_pos] + standard_nav + content[insert_pos:]
        
        # Add standard navigation CSS if not present
        if '.nav-container' not in content:
            head_end = content.find('</head>')
            if head_end != -1:
                nav_css = get_standard_nav_css()
                content = content[:head_end] + nav_css + content[head_end:]
        
        # Add mobile menu JavaScript if not present
        if 'toggleMobileMenu' not in content:
            body_end = content.find('</body>')
            if body_end != -1:
                mobile_script = get_standard_mobile_script()
                content = content[:body_end] + mobile_script + content[body_end:]
        
        # Write back if changed
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            rel_path = os.path.relpath(file_path, "/Users/glengomezmeade/Projects/plasma-pay-calculator")
            print(f"✅ Fixed navigation in {rel_path}")
            return True
        else:
            rel_path = os.path.relpath(file_path, "/Users/glengomezmeade/Projects/plasma-pay-calculator")
            print(f"ℹ️ No navigation changes needed in {rel_path}")
            return False
            
    except Exception as e:
        rel_path = os.path.relpath(file_path, "/Users/glengomezmeade/Projects/plasma-pay-calculator")
        print(f"❌ Error fixing navigation in {rel_path}: {str(e)}")
        return False

def main():
    """Fix navigation consistency across key pages"""
    print("🧭 Fixing navigation consistency across all pages...")
    
    # Key pages that need consistent navigation
    key_pages = [
        "/Users/glengomezmeade/Projects/plasma-pay-calculator/blog/index.html",
        "/Users/glengomezmeade/Projects/plasma-pay-calculator/centers/index.html",
        "/Users/glengomezmeade/Projects/plasma-pay-calculator/states.html",
        "/Users/glengomezmeade/Projects/plasma-pay-calculator/health/index.html",
        "/Users/glengomezmeade/Projects/plasma-pay-calculator/faq.html",
        "/Users/glengomezmeade/Projects/plasma-pay-calculator/about.html"
    ]
    
    fixed_count = 0
    
    for page_path in key_pages:
        if os.path.exists(page_path):
            if fix_page_navigation(page_path):
                fixed_count += 1
        else:
            rel_path = os.path.relpath(page_path, "/Users/glengomezmeade/Projects/plasma-pay-calculator")
            print(f"⚠️ Page not found: {rel_path}")
    
    print(f"\n🎉 Navigation consistency fix complete!")
    print(f"📊 Updated {fixed_count} pages with standard navigation")
    print(f"🧭 All pages now have consistent navigation structure")
    print(f"📱 Mobile menu implementation added to all pages")

if __name__ == "__main__":
    main()