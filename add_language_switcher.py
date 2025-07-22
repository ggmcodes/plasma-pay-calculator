#!/usr/bin/env python3
"""
Add comprehensive language switcher with flags throughout the entire site
"""

import os
import re
from pathlib import Path

def add_language_switcher():
    """Add language switcher with flags to all pages"""
    
    base_dir = "/Users/glengomezmeade/Projects/plasma-pay-calculator"
    
    print("🌐 ADDING LANGUAGE SWITCHER WITH FLAGS")
    print("🇺🇸 🇪🇸 English ↔ Spanish Navigation")
    print("=" * 80)
    
    # Language switcher HTML templates
    english_switcher = '''
    <div class="language-switcher">
        <a href="{spanish_url}" class="lang-option spanish" title="Español">
            <span class="flag">🇪🇸</span>
            <span class="lang-text">ES</span>
        </a>
    </div>'''
    
    spanish_switcher = '''
    <div class="language-switcher">
        <a href="{english_url}" class="lang-option english" title="English">
            <span class="flag">🇺🇸</span>
            <span class="lang-text">EN</span>
        </a>
    </div>'''
    
    # CSS for language switcher
    switcher_css = '''
    <style>
    .language-switcher {
        position: fixed;
        top: 20px;
        right: 20px;
        z-index: 1000;
        background: white;
        border-radius: 8px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        border: 1px solid #e2e8f0;
    }
    .lang-option {
        display: flex;
        align-items: center;
        padding: 8px 12px;
        text-decoration: none;
        color: #374151;
        font-weight: 500;
        transition: all 0.2s ease;
        border-radius: 7px;
        min-width: 60px;
        justify-content: center;
    }
    .lang-option:hover {
        background: #f8fafc;
        color: #1f2937;
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    .lang-option .flag {
        margin-right: 6px;
        font-size: 16px;
    }
    .lang-option .lang-text {
        font-size: 12px;
        font-weight: 600;
    }
    @media (max-width: 768px) {
        .language-switcher {
            top: 10px;
            right: 10px;
        }
        .lang-option {
            padding: 6px 10px;
            min-width: 50px;
        }
        .lang-option .flag {
            margin-right: 4px;
            font-size: 14px;
        }
        .lang-option .lang-text {
            font-size: 11px;
        }
    }
    </style>'''
    
    def get_counterpart_url(file_path, is_spanish_to_english=True):
        """Get the URL for the language counterpart"""
        
        relative_path = os.path.relpath(file_path, base_dir)
        
        if is_spanish_to_english:
            # Spanish to English
            if relative_path.startswith('es/'):
                english_path = relative_path[3:]  # Remove 'es/'
                if english_path == 'index.html':
                    return '/'
                elif english_path.endswith('/index.html'):
                    return '/' + english_path[:-11] + '/'  # Remove /index.html, add trailing slash
                elif english_path.endswith('.html'):
                    return '/' + english_path[:-5] + '/'  # Remove .html, add trailing slash
                else:
                    return '/' + english_path
            return '/'
        else:
            # English to Spanish
            if relative_path == 'index.html':
                return '/es/'
            elif relative_path.endswith('/index.html'):
                spanish_path = '/es/' + relative_path[:-11] + '/'  # Remove /index.html
                return spanish_path
            elif relative_path.endswith('.html'):
                spanish_path = '/es/' + relative_path[:-5] + '.html'  # Keep .html for Spanish
                return spanish_path
            else:
                return '/es/' + relative_path
    
    def add_switcher_to_file(file_path, is_spanish=False):
        """Add language switcher to a single file"""
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Skip if already has language switcher
            if 'language-switcher' in content:
                return False
            
            # Get counterpart URL
            if is_spanish:
                counterpart_url = get_counterpart_url(file_path, True)
                switcher_html = spanish_switcher.format(english_url=counterpart_url)
            else:
                counterpart_url = get_counterpart_url(file_path, False)
                switcher_html = english_switcher.format(spanish_url=counterpart_url)
            
            # Add CSS if not present
            if 'language-switcher' not in content:
                # Find head tag and add CSS
                head_match = re.search(r'</head>', content, re.IGNORECASE)
                if head_match:
                    content = content[:head_match.start()] + switcher_css + '\n' + content[head_match.start():]
            
            # Add switcher HTML after body tag
            body_match = re.search(r'<body[^>]*>', content, re.IGNORECASE)
            if body_match:
                insert_pos = body_match.end()
                content = content[:insert_pos] + '\n' + switcher_html + '\n' + content[insert_pos:]
                
                # Save file
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                return True
            
        except Exception as e:
            print(f"⚠️  Error processing {file_path}: {e}")
        
        return False
    
    english_updated = 0
    spanish_updated = 0
    
    # Process English pages
    print("🇺🇸 Adding switcher to English pages...")
    for root, dirs, files in os.walk(base_dir):
        # Skip Spanish directory
        if '/es' in root or root.endswith('/es'):
            continue
            
        if any(skip in root for skip in ['.git', 'node_modules', '__pycache__']):
            continue
            
        for file in files:
            if not file.endswith('.html'):
                continue
                
            file_path = os.path.join(root, file)
            if add_switcher_to_file(file_path, False):
                english_updated += 1
    
    # Process Spanish pages
    print("🇪🇸 Adding switcher to Spanish pages...")
    es_dir = os.path.join(base_dir, 'es')
    if os.path.exists(es_dir):
        for root, dirs, files in os.walk(es_dir):
            for file in files:
                if not file.endswith('.html'):
                    continue
                    
                file_path = os.path.join(root, file)
                if add_switcher_to_file(file_path, True):
                    spanish_updated += 1
    
    print(f"\n📊 LANGUAGE SWITCHER SUMMARY:")
    print(f"   🇺🇸 English pages updated: {english_updated}")
    print(f"   🇪🇸 Spanish pages updated: {spanish_updated}")
    print(f"   🌐 Total pages with switcher: {english_updated + spanish_updated}")
    print("   ✅ Users can now switch languages easily!")
    
    return english_updated + spanish_updated

def test_switcher_urls():
    """Test a few switcher URL mappings"""
    
    print(f"\n🧪 TESTING SWITCHER URL MAPPINGS:")
    print("=" * 80)
    
    test_cases = [
        ('index.html', False, '/es/'),
        ('es/index.html', True, '/'),
        ('calculators/california/index.html', False, '/es/calculators/california/'),
        ('es/calculators/california/index.html', True, '/calculators/california/'),
        ('blog/index.html', False, '/es/blog/'),
        ('es/blog/index.html', True, '/blog/'),
        ('about.html', False, '/es/about.html'),
        ('es/about.html', True, '/about/'),
    ]
    
    base_dir = "/Users/glengomezmeade/Projects/plasma-pay-calculator"
    
    def get_counterpart_url(file_path, is_spanish_to_english=True):
        relative_path = os.path.relpath(file_path, base_dir)
        
        if is_spanish_to_english:
            if relative_path.startswith('es/'):
                english_path = relative_path[3:]
                if english_path == 'index.html':
                    return '/'
                elif english_path.endswith('/index.html'):
                    return '/' + english_path[:-11] + '/'
                elif english_path.endswith('.html'):
                    return '/' + english_path[:-5] + '/'
                else:
                    return '/' + english_path
            return '/'
        else:
            if relative_path == 'index.html':
                return '/es/'
            elif relative_path.endswith('/index.html'):
                spanish_path = '/es/' + relative_path[:-11] + '/'
                return spanish_path
            elif relative_path.endswith('.html'):
                spanish_path = '/es/' + relative_path[:-5] + '.html'
                return spanish_path
            else:
                return '/es/' + relative_path
    
    for file_path, is_spanish, expected in test_cases:
        full_path = os.path.join(base_dir, file_path)
        result = get_counterpart_url(full_path, is_spanish)
        status = "✅" if result == expected else "❌"
        print(f"   {status} {file_path} → {result} (expected: {expected})")

def main():
    """Add language switcher to all pages"""
    
    total_updated = add_language_switcher()
    test_switcher_urls()
    
    print(f"\n🎯 LANGUAGE SWITCHER COMPLETE")
    print("=" * 80)
    print(f"✅ {total_updated} pages updated with language switcher")
    print("✅ Fixed-position switcher with country flags")
    print("✅ Responsive design for mobile/desktop")
    print("✅ Hover effects and smooth transitions")
    print("🇺🇸 🇪🇸 Perfect bilingual navigation experience!")
    
    return total_updated > 0

if __name__ == "__main__":
    main()