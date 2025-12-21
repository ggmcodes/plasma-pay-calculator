#!/usr/bin/env python3
"""
Add "Advertise With Us" footer section to all HTML pages.
Handles both custom CSS and Tailwind footer patterns.
Supports English and Spanish translations.
"""

import os
import re
from pathlib import Path

# Google Form link
FORM_LINK = "https://forms.gle/swUdMQWEixhXbxAg7"

# English advertise banner - Custom CSS pattern (inline styles)
ADVERTISE_BANNER_CUSTOM_EN = '''
    <div class="advertise-banner" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 1.5rem; margin-top: 2rem; border-radius: 10px; text-align: center;">
        <h4 style="color: white; margin-bottom: 0.5rem; font-size: 1.1rem;">Advertise With Us</h4>
        <p style="color: rgba(255,255,255,0.9); font-size: 0.9rem; margin-bottom: 1rem;">Reach thousands of active plasma donors searching for the best centers.</p>
        <a href="''' + FORM_LINK + '''" target="_blank" rel="noopener" style="display: inline-block; background: white; color: #667eea; padding: 0.6rem 1.5rem; border-radius: 5px; font-weight: 600; text-decoration: none;">Partner With Us</a>
    </div>
'''

# Spanish advertise banner - Custom CSS pattern (inline styles)
ADVERTISE_BANNER_CUSTOM_ES = '''
    <div class="advertise-banner" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 1.5rem; margin-top: 2rem; border-radius: 10px; text-align: center;">
        <h4 style="color: white; margin-bottom: 0.5rem; font-size: 1.1rem;">Anúnciate Con Nosotros</h4>
        <p style="color: rgba(255,255,255,0.9); font-size: 0.9rem; margin-bottom: 1rem;">Llega a miles de donantes de plasma activos buscando los mejores centros.</p>
        <a href="''' + FORM_LINK + '''" target="_blank" rel="noopener" style="display: inline-block; background: white; color: #667eea; padding: 0.6rem 1.5rem; border-radius: 5px; font-weight: 600; text-decoration: none;">Asóciate Con Nosotros</a>
    </div>
'''

# English advertise banner - Tailwind pattern
ADVERTISE_BANNER_TAILWIND_EN = '''
            <div class="mt-6 bg-gradient-to-r from-indigo-600 to-purple-600 rounded-lg p-4 text-center">
                <h4 class="text-white font-semibold mb-1">Advertise With Us</h4>
                <p class="text-indigo-100 text-sm mb-3">Reach thousands of active plasma donors searching for the best centers.</p>
                <a href="''' + FORM_LINK + '''" target="_blank" rel="noopener" class="inline-block bg-white text-indigo-600 px-4 py-2 rounded font-semibold hover:bg-gray-100 transition">Partner With Us</a>
            </div>
'''

# Spanish advertise banner - Tailwind pattern
ADVERTISE_BANNER_TAILWIND_ES = '''
            <div class="mt-6 bg-gradient-to-r from-indigo-600 to-purple-600 rounded-lg p-4 text-center">
                <h4 class="text-white font-semibold mb-1">Anúnciate Con Nosotros</h4>
                <p class="text-indigo-100 text-sm mb-3">Llega a miles de donantes de plasma activos buscando los mejores centros.</p>
                <a href="''' + FORM_LINK + '''" target="_blank" rel="noopener" class="inline-block bg-white text-indigo-600 px-4 py-2 rounded font-semibold hover:bg-gray-100 transition">Asóciate Con Nosotros</a>
            </div>
'''


def is_spanish_page(filepath: str) -> bool:
    """Check if the file is a Spanish page based on path."""
    return '/es/' in filepath or '\\es\\' in filepath


def has_advertise_banner(content: str) -> bool:
    """Check if the page already has an advertise banner."""
    return 'advertise-banner' in content.lower() or 'Advertise With Us' in content or 'Anúnciate Con Nosotros' in content


def detect_footer_pattern(content: str) -> str:
    """Detect which footer pattern is used."""
    if 'class="bg-gray-900 text-white py-8"' in content or 'class="bg-gray-900 text-white py-12"' in content:
        return 'tailwind'
    elif '<footer>' in content or 'class="footer-content"' in content:
        return 'custom'
    elif 'bg-gray-800' in content:
        return 'tailwind'
    else:
        return 'custom'  # Default to custom


def add_banner_tailwind(content: str, is_spanish: bool) -> str:
    """Add advertise banner to Tailwind-styled footer."""
    banner = ADVERTISE_BANNER_TAILWIND_ES if is_spanish else ADVERTISE_BANNER_TAILWIND_EN

    # Pattern: Insert before the border-t copyright section
    # Look for: <div class="border-t border-gray-800
    pattern = r'(\s*)(<div class="border-t border-gray-800)'

    if re.search(pattern, content):
        return re.sub(pattern, r'\1' + banner.strip() + r'\n\1\2', content, count=1)

    # Alternative: Insert before </footer>
    pattern2 = r'(\s*)(</footer>)'
    if re.search(pattern2, content):
        return re.sub(pattern2, banner + r'\1\2', content, count=1)

    return content


def add_banner_custom(content: str, is_spanish: bool) -> str:
    """Add advertise banner to custom CSS footer."""
    banner = ADVERTISE_BANNER_CUSTOM_ES if is_spanish else ADVERTISE_BANNER_CUSTOM_EN

    # Pattern 1: Insert after </div> that closes footer-content, before copyright <p>
    # Look for the copyright line after footer-content
    pattern = r'(</div>\s*\n)(\s*<p>&copy;)'
    if re.search(pattern, content):
        return re.sub(pattern, r'\1' + banner + r'\n\2', content, count=1)

    # Pattern 2: Insert before </footer>
    pattern2 = r'(\s*)(</footer>)'
    if re.search(pattern2, content):
        return re.sub(pattern2, banner + r'\1\2', content, count=1)

    return content


def process_file(filepath: str) -> tuple[bool, str]:
    """Process a single HTML file. Returns (success, message)."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Skip if no footer
        if '<footer' not in content.lower():
            return False, 'No footer found'

        # Skip if already has advertise banner
        if has_advertise_banner(content):
            return False, 'Already has advertise banner'

        is_spanish = is_spanish_page(filepath)
        pattern = detect_footer_pattern(content)

        if pattern == 'tailwind':
            new_content = add_banner_tailwind(content, is_spanish)
        else:
            new_content = add_banner_custom(content, is_spanish)

        # Check if content was actually modified
        if new_content == content:
            return False, 'Could not find insertion point'

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

        lang = 'Spanish' if is_spanish else 'English'
        return True, f'Added {lang} {pattern} banner'

    except Exception as e:
        return False, f'Error: {str(e)}'


def main():
    """Main function to process all HTML files."""
    base_dir = Path('/Users/glengomezmeade/Projects/plasma-pay-calculator')

    # Find all HTML files (excluding node_modules)
    html_files = []
    for root, dirs, files in os.walk(base_dir):
        # Skip node_modules
        dirs[:] = [d for d in dirs if d != 'node_modules']

        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))

    print(f"Found {len(html_files)} HTML files")

    stats = {
        'success': 0,
        'skipped_no_footer': 0,
        'skipped_already_has': 0,
        'skipped_no_insertion': 0,
        'errors': 0
    }

    for filepath in html_files:
        success, message = process_file(filepath)

        rel_path = os.path.relpath(filepath, base_dir)

        if success:
            stats['success'] += 1
            print(f"✅ {rel_path}: {message}")
        elif 'No footer' in message:
            stats['skipped_no_footer'] += 1
        elif 'Already has' in message:
            stats['skipped_already_has'] += 1
            print(f"⏭️  {rel_path}: {message}")
        elif 'Could not find' in message:
            stats['skipped_no_insertion'] += 1
            print(f"⚠️  {rel_path}: {message}")
        else:
            stats['errors'] += 1
            print(f"❌ {rel_path}: {message}")

    print("\n" + "="*50)
    print("SUMMARY")
    print("="*50)
    print(f"✅ Successfully updated: {stats['success']}")
    print(f"⏭️  Already had banner: {stats['skipped_already_has']}")
    print(f"📄 No footer found: {stats['skipped_no_footer']}")
    print(f"⚠️  No insertion point: {stats['skipped_no_insertion']}")
    print(f"❌ Errors: {stats['errors']}")


if __name__ == '__main__':
    main()
