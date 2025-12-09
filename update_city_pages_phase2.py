#!/usr/bin/env python3
"""
Phase 2: Apply layout changes to all ~267 city pages
- Delete all "Start Earning" CTA sections
- Delete "Written by Glen Meade" author byline
- Reorder sections: Helpful Guides → About Author → Sources → Medical Disclaimer
"""

import re
import os
from pathlib import Path

def update_city_page(file_path):
    """Apply layout changes to a single city page"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # 1. Delete "Ready to Start Earning" CTA section (first CTA)
        pattern1 = r'        <!-- Quick Action CTA -->[\s\S]*?</section>\n\n        <!-- Local Centers Section -->'
        replacement1 = '        <!-- Local Centers Section -->'
        content = re.sub(pattern1, replacement1, content)

        # 2. Delete "💰 Start Earning in [City] Today" CTA within earnings guide
        pattern2 = r'                \n                <div class="mt-12 bg-gradient-to-r from-green-600 to-blue-600[\s\S]*?</div>\n            </div>\n        </section>'
        replacement2 = '            </div>\n        </section>'
        content = re.sub(pattern2, replacement2, content)

        # 3. Delete "Written by Glen Meade" author byline
        pattern3 = r'<div class="author-byline"[\s\S]*?</div>\n\n'
        content = re.sub(pattern3, '', content)

        # 4. Extract sections that need to be reordered
        # Extract Medical Disclaimer
        medical_pattern = r'(<div class="medical-disclaimer"[\s\S]*?</div>)\n\n'
        medical_match = re.search(medical_pattern, content)
        if medical_match:
            medical_disclaimer = medical_match.group(1)
            content = re.sub(medical_pattern, '', content)
        else:
            medical_disclaimer = None

        # Extract About the Author
        author_pattern = r'(<div class="author-bio"[\s\S]*?</div>)\n\n'
        author_match = re.search(author_pattern, content)
        if author_match:
            author_bio = author_match.group(1)
            content = re.sub(author_pattern, '', content)
        else:
            author_bio = None

        # Extract Sources & References
        sources_pattern = r'(<div class="source-citations"[\s\S]*?</div>)\n\n'
        sources_match = re.search(sources_pattern, content)
        if sources_match:
            sources = sources_match.group(1)
            content = re.sub(sources_pattern, '', content)
        else:
            sources = None

        # Remove any leftover "<!-- Footer -->" comments that were left behind
        content = re.sub(r'<!-- Footer -->\n    \n', '', content)

        # 5. Find the Helpful Guides section and insert sections after it in correct order
        helpful_guides_pattern = r'(                </div>\n            </div>\n        </section>\n<footer class="bg-gray-900 text-white py-8">)'

        # Build the new sections in correct order with proper formatting
        new_sections = '\n\n'

        if author_bio:
            # Update author bio styling to match the target format
            author_bio_updated = author_bio.replace(
                'style="background: #f9fafb; border: 1px solid #e5e7eb; padding: 1.5rem; border-radius: 12px; margin-top: 3rem;">',
                'style="background: #f9fafb; border: 1px solid #e5e7eb; padding: 1.5rem; border-radius: 12px; margin: 2rem auto; max-width: 1280px; padding-left: 1.5rem; padding-right: 1.5rem;">'
            )
            new_sections += author_bio_updated + '\n\n'

        if sources:
            # Update sources styling to match the target format
            sources_updated = sources.replace(
                'style="background: #f3f4f6; padding: 1.5rem; border-radius: 8px; margin-top: 2rem;">',
                'style="background: #f3f4f6; padding: 1.5rem; border-radius: 8px; margin: 2rem auto; max-width: 1280px; padding-left: 1.5rem; padding-right: 1.5rem;">'
            )
            new_sections += sources_updated + '\n\n'

        if medical_disclaimer:
            # Update medical disclaimer styling to match the target format
            medical_updated = medical_disclaimer.replace(
                'style="background: #fef3c7; border: 1px solid #fbbf24; padding: 1rem; border-radius: 8px; margin-bottom: 1.5rem;">',
                'style="background: #fef3c7; border: 1px solid #fbbf24; padding: 1rem; border-radius: 8px; margin: 2rem auto; max-width: 1280px; padding-left: 1.5rem; padding-right: 1.5rem;">'
            )
            new_sections += medical_updated + '\n\n'

        # Insert the reordered sections
        replacement_with_sections = new_sections.rstrip('\n\n') + '\n\n' + r'\1'
        content = re.sub(helpful_guides_pattern, replacement_with_sections, content)

        # 6. Delete "Start Earning" final CTA section (before footer, after footer opening)
        final_cta_pattern = r'            </div>\n\n<!-- Final CTA -->[\s\S]*?</section>\n    </main>\n\n            <div class="border-t border-gray-800'
        final_cta_replacement = r'            </div>\n\n            <div class="border-t border-gray-800'
        content = re.sub(final_cta_pattern, final_cta_replacement, content)

        # Only write if content changed
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    # Find all city pages (depth 3 in calculators directory)
    calculators_dir = Path('calculators')
    city_pages = []

    for state_dir in calculators_dir.iterdir():
        if state_dir.is_dir():
            for city_dir in state_dir.iterdir():
                if city_dir.is_dir():
                    index_file = city_dir / 'index.html'
                    if index_file.exists():
                        city_pages.append(index_file)

    print(f"Found {len(city_pages)} city pages to update")

    updated_count = 0
    for i, page in enumerate(city_pages, 1):
        if update_city_page(page):
            updated_count += 1
            if updated_count % 10 == 0:
                print(f"Progress: {updated_count}/{len(city_pages)} pages updated")

    print(f"\nComplete! Updated {updated_count} out of {len(city_pages)} city pages")

if __name__ == '__main__':
    main()
