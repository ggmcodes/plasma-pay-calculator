#!/usr/bin/env python3
"""
City Pages Migration Script
Migrates all 261 city pages from BestPlasmaCenters to PlasmaPayCalculator
"""

import os
import re
import shutil
from pathlib import Path

# Source and destination paths
SOURCE_BASE = "/Users/glengomezmeade/Projects/bestplasmacenters/public/state"
DEST_BASE = "/Users/glengomezmeade/Projects/plasma-pay-calculator/calculators"

def extract_city_info(file_path):
    """Extract state and city from file path"""
    # Example: public/state/texas/houston.html -> texas, houston
    path_parts = Path(file_path).parts
    state = path_parts[-2]
    city = Path(file_path).stem
    return state, city

def transform_content(content, state, city):
    """Transform content from BestPlasmaCenters to PlasmaPayCalculator format"""
    
    # Basic rebranding
    content = content.replace("Best Plasma Centers", "Plasma Pay Calculator")
    content = content.replace("bestplasmacenters.com", "plasmapaycalculator.com")
    
    # Update titles - change "Best Centers" to "Pay Calculator"
    content = re.sub(
        r'<title>Plasma Donation in ([^-]+) - Best Centers & Pay Rates 2025</title>',
        r'<title>\1 Plasma Pay Calculator - Calculate Your Earnings 2025</title>',
        content
    )
    
    # Update meta descriptions to focus on calculator
    content = re.sub(
        r'<meta name="description" content="[^"]*Find the best plasma donation centers[^"]*"',
        f'<meta name="description" content="Calculate your plasma donation earnings in {city.replace("-", " ").title()}, {state.replace("-", " ").title()}! Earn money donating plasma with our interactive calculator. Updated 2025."',
        content
    )
    
    # Update keywords to focus on calculator
    content = re.sub(
        r'(<meta name="keywords" content="[^"]*)',
        r'\1, plasma pay calculator, plasma earnings calculator, calculate plasma money',
        content
    )
    
    # Update author
    content = content.replace('<meta name="author" content="Best Plasma Centers">', 
                             '<meta name="author" content="Plasma Pay Calculator">')
    
    # Update Open Graph
    content = re.sub(
        r'<meta property="og:title" content="Plasma Donation in ([^-]+) - Best Centers & Pay Rates 2025">',
        r'<meta property="og:title" content="\1 Plasma Pay Calculator - Calculate Your Earnings 2025">',
        content
    )
    
    content = re.sub(
        r'<meta property="og:description" content="[^"]*Find the highest-paying plasma centers[^"]*">',
        f'<meta property="og:description" content="Calculate your plasma donation earnings in {city.replace("-", " ").title()}, {state.replace("-", " ").title()}. Interactive calculator with real pay rates.">',
        content
    )
    
    # Update URLs in Open Graph and schema
    content = re.sub(
        r'https://bestplasmacenters\.com/state/([^/]+)/([^"]+)',
        r'https://plasmapaycalculator.com/calculators/\1/\2/',
        content
    )
    
    # Update site name
    content = content.replace('<meta property="og:site_name" content="Best Plasma Centers">', 
                             '<meta property="og:site_name" content="Plasma Pay Calculator">')
    
    # Update Twitter cards
    content = re.sub(
        r'<meta name="twitter:title" content="Plasma Donation in ([^-]+) - Pay Rates & Centers">',
        r'<meta name="twitter:title" content="\1 Plasma Pay Calculator - Calculate Earnings">',
        content
    )
    
    # Update canonical URL
    content = re.sub(
        r'<link rel="canonical" href="https://bestplasmacenters\.com/state/([^/]+)/([^"]+)">',
        r'<link rel="canonical" href="https://plasmapaycalculator.com/calculators/\1/\2/">',
        content
    )
    
    # Update logo and header branding
    content = content.replace('<span class="text-xl">💙</span>', '<span class="text-xl">🩸</span>')
    content = content.replace('Best Plasma Centers</a>', 'Plasma Pay Calculator</a>')
    
    # Update navigation - change "Find Centers" to link to /centers/
    content = re.sub(
        r'<a href="/\?search=true" class="[^"]*">Find Centers</a>',
        r'<a href="/centers/" class="text-gray-600 hover:text-gray-900 font-medium transition-colors">Centers</a>',
        content
    )
    
    # Update navigation structure to match PPC
    nav_replacement = '''                <nav class="hidden md:flex items-center space-x-8">
                    <a href="/calculator/" class="text-gray-600 hover:text-gray-900 font-medium transition-colors">Calculator</a>
                    <a href="/blog/" class="text-gray-600 hover:text-gray-900 font-medium transition-colors">Blog</a>
                    <a href="/states.html" class="text-gray-600 hover:text-gray-900 font-medium transition-colors">States</a>
                    <a href="/centers/" class="text-gray-600 hover:text-gray-900 font-medium transition-colors">Centers</a>
                    <a href="/health/" class="text-gray-600 hover:text-gray-900 font-medium transition-colors">Health</a>
                    <a href="/faq.html" class="text-gray-600 hover:text-gray-900 font-medium transition-colors">FAQ</a>
                </nav>'''
    
    content = re.sub(
        r'<nav class="hidden md:flex items-center space-x-8">.*?</nav>',
        nav_replacement,
        content,
        flags=re.DOTALL
    )
    
    # Update breadcrumbs
    content = re.sub(
        r'<a href="/" class="hover:text-gray-900">Home</a>',
        r'<a href="/" class="hover:text-gray-900">Home</a>',
        content
    )
    
    content = re.sub(
        r'<a href="/state/([^"]+)\.html" class="hover:text-gray-900">([^<]+)</a>',
        r'<a href="/calculators/\1/" class="hover:text-gray-900">\2</a>',
        content
    )
    
    # Update any remaining links to "find centers" type content
    content = re.sub(
        r'href="[^"]*search=true[^"]*"',
        r'href="/centers/"',
        content
    )
    
    # Update any "find centers" text to link to centers page
    content = re.sub(
        r'(>find centers?</a>)',
        r'>Centers</a>',
        content,
        flags=re.IGNORECASE
    )
    
    # Remove Pay Calculator external link since we're now on PPC
    content = re.sub(
        r'<a href="https://plasmapaycalculator\.com"[^>]*>\s*Pay Calculator\s*</a>',
        '',
        content
    )
    
    # Update color scheme to match PPC (amber instead of blue)
    content = content.replace('plasma-blue', 'amber')
    content = content.replace('from-plasma-blue-500 to-plasma-blue-600', 'from-amber-500 to-amber-600')
    
    return content

def ensure_directory_exists(file_path):
    """Ensure the directory for the file exists"""
    directory = os.path.dirname(file_path)
    os.makedirs(directory, exist_ok=True)

def migrate_city_page(source_file):
    """Migrate a single city page"""
    try:
        state, city = extract_city_info(source_file)
        
        # Read source content
        with open(source_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Transform content
        transformed_content = transform_content(content, state, city)
        
        # Create destination path
        dest_dir = os.path.join(DEST_BASE, state, city)
        dest_file = os.path.join(dest_dir, 'index.html')
        
        # Ensure directory exists
        ensure_directory_exists(dest_file)
        
        # Write transformed content
        with open(dest_file, 'w', encoding='utf-8') as f:
            f.write(transformed_content)
        
        print(f"✅ Migrated: {state}/{city}")
        return True
        
    except Exception as e:
        print(f"❌ Error migrating {source_file}: {e}")
        return False

def main():
    """Main migration function"""
    print("🚀 Starting city pages migration...")
    
    # Find all city pages
    city_pages = []
    for root, dirs, files in os.walk(SOURCE_BASE):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                # Skip state-level files (they're in state/ directory directly)
                if len(Path(file_path).parts) > len(Path(SOURCE_BASE).parts) + 1:
                    city_pages.append(file_path)
    
    print(f"📊 Found {len(city_pages)} city pages to migrate")
    
    # Migrate each page
    success_count = 0
    for city_page in city_pages:
        if migrate_city_page(city_page):
            success_count += 1
    
    print(f"\n🎉 Migration complete!")
    print(f"✅ Successfully migrated: {success_count}/{len(city_pages)} pages")
    
    if success_count < len(city_pages):
        print(f"❌ Failed: {len(city_pages) - success_count} pages")

if __name__ == "__main__":
    main()