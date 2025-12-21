#!/usr/bin/env python3
"""
Update footer advertise banner links to point to /advertise.html
instead of the Google Form directly.
"""

import os
import re
from pathlib import Path

def process_file(filepath: str) -> tuple[bool, str]:
    """Process a single HTML file. Returns (success, message)."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Skip the advertise.html page itself
        if filepath.endswith('advertise.html'):
            return False, 'Skipped advertise.html'

        # Check if file has the advertise banner with Google Form link
        if 'advertise-banner' not in content.lower() and 'Advertise With Us' not in content:
            return False, 'No advertise banner found'

        # Pattern to find the Google Form link in advertise banners
        # We need to be careful to only replace links within the advertise banner context
        old_link = 'href="https://forms.gle/swUdMQWEixhXbxAg7"'
        new_link = 'href="/advertise.html"'

        if old_link not in content:
            return False, 'Google Form link not found'

        new_content = content.replace(old_link, new_link)

        if new_content == content:
            return False, 'No changes made'

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

        return True, 'Updated link to /advertise.html'

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
        'skipped': 0,
        'errors': 0
    }

    for filepath in html_files:
        success, message = process_file(filepath)

        rel_path = os.path.relpath(filepath, base_dir)

        if success:
            stats['success'] += 1
            print(f"✅ {rel_path}: {message}")
        elif 'Error' in message:
            stats['errors'] += 1
            print(f"❌ {rel_path}: {message}")
        else:
            stats['skipped'] += 1

    print("\n" + "="*50)
    print("SUMMARY")
    print("="*50)
    print(f"✅ Successfully updated: {stats['success']}")
    print(f"⏭️  Skipped: {stats['skipped']}")
    print(f"❌ Errors: {stats['errors']}")


if __name__ == '__main__':
    main()
