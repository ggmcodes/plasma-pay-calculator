#!/usr/bin/env python3
"""
Script to add mobile menus to centers/ and health/ pages.
"""

import os
import re
from pathlib import Path

# Standard header HTML for special pages
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

def find_special_pages():
    """Find centers/ and health/ HTML files"""
    html_files = []
    
    # Get centers pages
    centers_path = Path("/Users/glengomezmeade/plasma-pay-calculator/centers")
    if centers_path.exists():
        html_files.extend(list(centers_path.rglob("*.html")))
    
    # Get health pages
    health_path = Path("/Users/glengomezmeade/plasma-pay-calculator/health")
    if health_path.exists():
        html_files.extend(list(health_path.rglob("*.html")))
    
    return html_files

def update_special_page(file_path):
    """Update a special page with mobile menu"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if already has mobile menu
        if 'id="mobileMenuBtn"' in content:
            return False, "Already has mobile menu"
        
        # Find existing header and replace, or insert after body
        header_pattern = r'<header[^>]*>.*?</header>'
        header_match = re.search(header_pattern, content, re.DOTALL)
        
        if header_match:
            # Replace existing header
            new_content = content.replace(header_match.group(0), STANDARD_HEADER)
        else:
            # Insert header after body tag
            body_match = re.search(r'<body[^>]*>', content)
            if body_match:
                insert_pos = body_match.end()
                new_content = content[:insert_pos] + '\n' + STANDARD_HEADER + '\n' + content[insert_pos:]
            else:
                return False, "No body tag found"
        
        # Add mobile menu JavaScript if not present
        if 'mobileMenuBtn' not in content:
            # Find the closing script tag before </body> or just before </body>
            script_pattern = r'</script>\s*</body>'
            script_match = re.search(script_pattern, new_content, re.IGNORECASE)
            
            if script_match:
                # Insert before the closing script tag
                insert_pos = script_match.start()
                new_content = new_content[:insert_pos] + MOBILE_MENU_JS + '\n        ' + new_content[insert_pos:]
            else:
                # Insert before </body>
                body_end_match = re.search(r'</body>', new_content, re.IGNORECASE)
                if body_end_match:
                    insert_pos = body_end_match.start()
                    new_content = new_content[:insert_pos] + '\n    <script>\n' + MOBILE_MENU_JS + '\n    </script>\n' + new_content[insert_pos:]
        
        # Write the updated content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return True, "Updated successfully"
        
    except Exception as e:
        return False, f"Error: {str(e)}"

def main():
    """Main function to process special pages"""
    html_files = find_special_pages()
    
    print(f"Found {len(html_files)} special pages to process")
    
    updated_count = 0
    skipped_count = 0
    error_count = 0
    
    for file_path in html_files:
        success, message = update_special_page(file_path)
        
        if success:
            updated_count += 1
            print(f"✅ Updated: {file_path}")
        elif "Already" in message:
            skipped_count += 1
            print(f"⏭️  Skipped: {file_path} ({message})")
        else:
            error_count += 1
            print(f"❌ Error: {file_path} ({message})")
    
    print(f"\n📊 Summary:")
    print(f"   Updated: {updated_count}")
    print(f"   Skipped: {skipped_count}")
    print(f"   Errors: {error_count}")
    print(f"   Total: {len(html_files)}")

if __name__ == "__main__":
    main()