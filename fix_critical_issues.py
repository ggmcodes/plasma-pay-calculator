#!/usr/bin/env python3
"""
Fix critical broken links and missing directories
"""

import os
import shutil
from pathlib import Path

def create_missing_directories():
    """Create missing directories and index files"""
    root_path = Path("/Users/glengomezmeade/plasma-pay-calculator")
    
    # Directories that need to exist
    required_dirs = [
        'health/requirements',
        'health/safety', 
        'health/frequency',
        'es/health',
        'es/centers',
        'es/process',
        'es/blog'
    ]
    
    created = 0
    for dir_path in required_dirs:
        full_path = root_path / dir_path
        if not full_path.exists():
            full_path.mkdir(parents=True, exist_ok=True)
            # Create a basic index.html
            index_content = f'''<!DOCTYPE html>
<html lang="{'es' if '/es/' in dir_path else 'en'}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{'Plasma Pay Calculator' if '/es/' not in dir_path else 'Calculadora Plasma'}</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body>
    <div class="min-h-screen bg-gray-50 flex items-center justify-center">
        <div class="text-center">
            <h1 class="text-4xl font-bold text-gray-800 mb-4">{'Coming Soon' if '/es/' not in dir_path else 'Próximamente'}</h1>
            <a href="{'/' if '/es/' not in dir_path else '/es/'}" class="text-blue-600 hover:underline">{'Return Home' if '/es/' not in dir_path else 'Volver al Inicio'}</a>
        </div>
    </div>
</body>
</html>'''
            
            index_file = full_path / 'index.html'
            with open(index_file, 'w', encoding='utf-8') as f:
                f.write(index_content)
            created += 1
            print(f"✅ Created: {dir_path}/index.html")
    
    return created

def fix_health_links():
    """Fix broken health section links"""
    health_index = Path("/Users/glengomezmeade/plasma-pay-calculator/health/index.html")
    
    if health_index.exists():
        with open(health_index, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Fix relative links
        content = content.replace('href="requirements"', 'href="/health/requirements/"')
        content = content.replace('href="safety"', 'href="/health/safety/"')
        content = content.replace('href="frequency"', 'href="/health/frequency/"')
        
        with open(health_index, 'w', encoding='utf-8') as f:
            f.write(content)
        print("✅ Fixed health section links")

def copy_favicon():
    """Ensure favicon exists in all formats"""
    root_path = Path("/Users/glengomezmeade/plasma-pay-calculator")
    
    # Create a simple favicon if it doesn't exist
    favicon_path = root_path / 'favicon.ico'
    if not favicon_path.exists():
        # Create empty favicon for now
        favicon_path.touch()
        print("✅ Created favicon.ico")

def main():
    print("🔧 Fixing critical site issues...")
    print("=" * 50)
    
    # Create missing directories
    created = create_missing_directories()
    print(f"\n📁 Created {created} missing directories")
    
    # Fix health links
    fix_health_links()
    
    # Ensure favicon exists
    copy_favicon()
    
    print("\n✨ Critical fixes complete!")

if __name__ == "__main__":
    main()