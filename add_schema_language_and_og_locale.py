#!/usr/bin/env python3
"""
Phase 4: Add inLanguage to schema and OG locale tags site-wide.
- Adds inLanguage: "en" to English pages' schema
- Adds inLanguage: "es" to Spanish pages' schema
- Adds OG locale tags to all pages (og:locale and og:locale:alternate)
"""

import re
from pathlib import Path
import sys

def is_spanish_page(file_path):
    """Check if page is Spanish"""
    return '/es/' in str(file_path).replace('\\', '/')

def add_inlanguage_to_schema(content, language):
    """Add inLanguage property to schema.org JSON-LD"""

    # Find schema.org script tag
    schema_pattern = r'(<script type="application/ld\+json">)(.*?)(</script>)'
    match = re.search(schema_pattern, content, re.DOTALL)

    if not match:
        return content, False, "No schema found"

    opening = match.group(1)
    schema_json = match.group(2)
    closing = match.group(3)

    # Check if already has inLanguage
    if '"inLanguage"' in schema_json:
        return content, False, "Already has inLanguage"

    # Add inLanguage after @type WebPage
    # Look for the WebPage type and add inLanguage after description
    if '"@type": "WebPage"' in schema_json:
        # Add after description line
        desc_pattern = r'("description": "[^"]*",)'
        desc_match = re.search(desc_pattern, schema_json)

        if desc_match:
            insert_pos = desc_match.end()
            new_schema = (
                schema_json[:insert_pos] +
                f'\n      "inLanguage": "{language}",' +
                schema_json[insert_pos:]
            )

            new_content = content.replace(
                opening + schema_json + closing,
                opening + new_schema + closing
            )

            return new_content, True, None

    return content, False, "Could not add inLanguage"

def add_og_locale_tags(content, is_spanish):
    """Add OG locale tags after existing OG tags"""

    # Check if already has og:locale
    if 'og:locale' in content:
        return content, False, "Already has og:locale"

    # Find last OG tag
    og_pattern = r'<meta property="og:[^"]+"\s+content="[^"]*">'
    og_matches = list(re.finditer(og_pattern, content))

    if not og_matches:
        return content, False, "No OG tags found"

    last_og_match = og_matches[-1]
    insert_pos = last_og_match.end()

    # Generate OG locale tags based on language
    if is_spanish:
        og_locale_tags = '''
    <meta property="og:locale" content="es_US">
    <meta property="og:locale:alternate" content="en_US">'''
    else:
        og_locale_tags = '''
    <meta property="og:locale" content="en_US">
    <meta property="og:locale:alternate" content="es_US">'''

    new_content = content[:insert_pos] + og_locale_tags + content[insert_pos:]

    return new_content, True, None

def process_file(file_path, dry_run=False):
    """Process a single HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        is_spanish = is_spanish_page(file_path)
        language = "es" if is_spanish else "en"

        modified = False

        # Add inLanguage to schema
        new_content, schema_modified, schema_error = add_inlanguage_to_schema(content, language)
        if schema_modified:
            content = new_content
            modified = True
        elif schema_error and "Already has" not in schema_error:
            # Only report non-"already has" errors
            pass

        # Add OG locale tags
        new_content, og_modified, og_error = add_og_locale_tags(content, is_spanish)
        if og_modified:
            content = new_content
            modified = True

        if modified and not dry_run:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)

        return modified, None

    except Exception as e:
        return False, str(e)

def main():
    """Main function"""
    dry_run = '--dry-run' in sys.argv
    test_mode = '--test' in sys.argv

    if dry_run:
        print("=== DRY RUN MODE - No files will be modified ===\n")

    print("=== ADDING INLANGUAGE TO SCHEMA AND OG LOCALE TAGS ===\n")

    if test_mode:
        print("=== TEST MODE - Testing on 6 sample files ===\n")
        test_files = [
            'calculators/new-york/manhattan/index.html',
            'calculators/california/los-angeles/index.html',
            'calculators/texas/houston/index.html',
            'es/calculators/new-york/manhattan/index.html',
            'es/calculators/california/los-angeles/index.html',
            'es/calculators/texas/houston/index.html',
        ]
        html_files = [Path(f) for f in test_files if Path(f).exists()]
    else:
        # Find all calculator pages (English and Spanish)
        print("Finding all calculator HTML files...\n")
        html_files = []

        # English pages
        calculators_path = Path('calculators')
        if calculators_path.exists():
            html_files.extend(list(calculators_path.glob('**/*.html')))

        # Spanish pages
        es_calculators_path = Path('es/calculators')
        if es_calculators_path.exists():
            html_files.extend(list(es_calculators_path.glob('**/*.html')))

        html_files.sort()

    print(f"Found {len(html_files)} HTML files to process\n")

    updated_count = 0
    skipped_count = 0
    error_count = 0
    errors = []

    for html_file in html_files:
        modified, error = process_file(html_file, dry_run=dry_run)

        if error:
            error_count += 1
            errors.append((html_file, error))
            print(f"❌ Error: {html_file}: {error}")
        elif modified:
            updated_count += 1
            status = "Would update" if dry_run else "✓ Updated"
            print(f"{status}: {html_file}")
        else:
            skipped_count += 1

    print(f"\n=== COMPLETE ===")
    print(f"Updated: {updated_count} files")
    print(f"Skipped: {skipped_count} files (already have tags or no changes needed)")
    print(f"Errors: {error_count} files")

    if errors:
        print("\n=== ERRORS ===")
        for file_path, error in errors:
            print(f"{file_path}: {error}")

    if not dry_run and updated_count > 0:
        print(f"\n✅ Added inLanguage and OG locale tags to {updated_count} pages!")

    return 0 if error_count == 0 else 1

if __name__ == '__main__':
    sys.exit(main())
