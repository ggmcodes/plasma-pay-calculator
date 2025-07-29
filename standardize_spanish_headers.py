#!/usr/bin/env python3
"""
Script to standardize Spanish page headers and mobile navigation across all Spanish calculator pages.
This script adds consistent header structure and mobile menu functionality for Spanish pages.
"""

import os
import re
from pathlib import Path

# Standard header HTML for Spanish pages
STANDARD_SPANISH_HEADER = '''    <header class="bg-white shadow-lg sticky top-0 z-50">
        <div class="container mx-auto px-4 py-3">
            <div class="flex items-center justify-between">
                <!-- Logo -->
                <div class="flex items-center space-x-2">
                    <div class="w-8 h-8 bg-red-600 rounded-full flex items-center justify-center">
                        <span class="text-white font-bold text-sm">🩸</span>
                    </div>
                    <a href="/es/" class="text-xl font-bold text-gray-800 hover:text-red-600 transition-colors">
                        Calculadora de Pago por Plasma
                    </a>
                </div>

                <!-- Desktop Navigation -->
                <nav class="hidden md:flex items-center space-x-6">
                    <a href="/es/calculadoras/" class="text-gray-700 hover:text-red-600 font-medium transition-colors">Calculadoras</a>
                    <a href="/es/centros/" class="text-gray-700 hover:text-red-600 font-medium transition-colors">Centros</a>
                    <a href="/es/salud/" class="text-gray-700 hover:text-red-600 font-medium transition-colors">Guía de Salud</a>
                    <a href="/es/blog/" class="text-gray-700 hover:text-red-600 font-medium transition-colors">Blog</a>
                    <div class="language-switcher">
                        <select id="languageSelect" class="bg-gray-100 border border-gray-300 rounded px-3 py-1 text-sm focus:outline-none focus:ring-2 focus:ring-red-500">
                            <option value="es">🇪🇸 Español</option>
                            <option value="en">🇺🇸 English</option>
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
                    <a href="/es/calculadoras/" class="text-gray-700 hover:text-red-600 font-medium py-2 transition-colors">Calculadoras</a>
                    <a href="/es/centros/" class="text-gray-700 hover:text-red-600 font-medium py-2 transition-colors">Centros</a>
                    <a href="/es/salud/" class="text-gray-700 hover:text-red-600 font-medium py-2 transition-colors">Guía de Salud</a>
                    <a href="/es/blog/" class="text-gray-700 hover:text-red-600 font-medium py-2 transition-colors">Blog</a>
                    <div class="py-2">
                        <select id="mobileLanguageSelect" class="bg-gray-100 border border-gray-300 rounded px-3 py-2 text-sm w-full focus:outline-none focus:ring-2 focus:ring-red-500">
                            <option value="es">🇪🇸 Español</option>
                            <option value="en">🇺🇸 English</option>
                        </select>
                    </div>
                </div>
            </div>
        </div>
    </header>'''

# Mobile menu JavaScript for Spanish pages
SPANISH_MOBILE_MENU_JS = '''        // Mobile menu functionality
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
                if (selectedLang === 'en') {
                    const currentPath = window.location.pathname;
                    let englishPath;
                    
                    if (currentPath === '/es/' || currentPath === '/es/index.html') {
                        englishPath = '/';
                    } else {
                        // Remove /es prefix
                        englishPath = currentPath.replace('/es', '');
                    }
                    
                    window.location.href = englishPath;
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

def find_spanish_html_files():
    """Find all Spanish HTML files"""
    html_files = []
    
    # Get all Spanish calculator HTML files
    es_path = Path("/Users/glengomezmeade/plasma-pay-calculator/es")
    if es_path.exists():
        html_files.extend(list(es_path.rglob("*.html")))
    
    return html_files

def update_spanish_html_file(file_path):
    """Update a single Spanish HTML file with standardized header and mobile menu"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if already has standard header
        if 'id="mobileMenuBtn"' in content:
            return False, "Already has mobile menu"
        
        # Find existing header and replace it
        header_pattern = r'<header[^>]*>.*?</header>'
        header_match = re.search(header_pattern, content, re.DOTALL)
        
        if header_match:
            # Replace existing header
            new_content = content.replace(header_match.group(0), STANDARD_SPANISH_HEADER)
        else:
            # Insert header after body tag
            body_match = re.search(r'<body[^>]*>', content)
            if body_match:
                insert_pos = body_match.end()
                new_content = content[:insert_pos] + '\n' + STANDARD_SPANISH_HEADER + '\n' + content[insert_pos:]
            else:
                return False, "No body tag found"
        
        # Add mobile menu JavaScript if not present
        if 'mobileMenuBtn' not in content:
            # Find the closing script tag before </body>
            script_pattern = r'</script>\s*</body>'
            script_match = re.search(script_pattern, new_content)
            
            if script_match:
                # Insert before the closing script tag
                insert_pos = script_match.start()
                new_content = new_content[:insert_pos] + SPANISH_MOBILE_MENU_JS + '\n        ' + new_content[insert_pos:]
            else:
                # Insert before </body>
                body_end_match = re.search(r'</body>', new_content)
                if body_end_match:
                    insert_pos = body_end_match.start()
                    new_content = new_content[:insert_pos] + '\n    <script>\n' + SPANISH_MOBILE_MENU_JS + '\n    </script>\n' + new_content[insert_pos:]
        
        # Write the updated content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return True, "Updated successfully"
        
    except Exception as e:
        return False, f"Error: {str(e)}"

def main():
    """Main function to process all Spanish HTML files"""
    html_files = find_spanish_html_files()
    
    print(f"Found {len(html_files)} Spanish HTML files to process")
    
    updated_count = 0
    skipped_count = 0
    error_count = 0
    
    for file_path in html_files:
        success, message = update_spanish_html_file(file_path)
        
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