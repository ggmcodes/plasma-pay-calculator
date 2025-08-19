#!/usr/bin/env python3
import os
import re

def fix_spanish_to_english_links():
    """Fix Spanish links to point to English calculator pages"""
    
    fixes_made = 0
    
    # Files that have Spanish city links
    spanish_files = {
        '/Users/glengomezmeade/Projects/plasma-pay-calculator/es/calculators/missouri/index.html': [
            ('/es/calculators/missouri/springfield-mo/', '/calculators/missouri/springfield-mo/'),
            ('/es/calculators/missouri/columbia-mo/', '/calculators/missouri/columbia-mo/')
        ],
        '/Users/glengomezmeade/Projects/plasma-pay-calculator/es/calculators/virginia/index.html': [
            ('/es/calculators/virginia/alexandria/', '/calculators/virginia/alexandria/')
        ],
        '/Users/glengomezmeade/Projects/plasma-pay-calculator/es/calculators/maine/index.html': [
            ('/es/calculators/maine/portland-me/', '/calculators/maine/portland-me/'),
            ('/es/calculators/maine/auburn-me/', '/calculators/maine/auburn-me/')
        ],
        '/Users/glengomezmeade/Projects/plasma-pay-calculator/es/calculators/delaware/index.html': [
            ('/es/calculators/delaware/newark-de/', '/calculators/delaware/newark-de/')
        ],
        '/Users/glengomezmeade/Projects/plasma-pay-calculator/es/calculators/iowa/index.html': [
            ('/es/calculators/iowa/waterloo/', '/calculators/iowa/waterloo/')
        ],
        '/Users/glengomezmeade/Projects/plasma-pay-calculator/es/calculators/new-hampshire/index.html': [
            ('/es/calculators/new-hampshire/manchester-nh/', '/calculators/new-hampshire/manchester-nh/'),
            ('/es/calculators/new-hampshire/concord-nh/', '/calculators/new-hampshire/concord-nh/'),
            ('/es/calculators/new-hampshire/derry/', '/calculators/new-hampshire/derry/'),
            ('/es/calculators/new-hampshire/rochester-nh/', '/calculators/new-hampshire/rochester-nh/')
        ],
        '/Users/glengomezmeade/Projects/plasma-pay-calculator/es/calculators/west-virginia/index.html': [
            ('/es/calculators/west-virginia/charleston-wv/', '/calculators/west-virginia/charleston-wv/')
        ],
        '/Users/glengomezmeade/Projects/plasma-pay-calculator/es/calculators/south-dakota/index.html': [
            ('/es/calculators/south-dakota/watertown-sd/', '/calculators/south-dakota/watertown-sd/')
        ],
        '/Users/glengomezmeade/Projects/plasma-pay-calculator/es/calculators/south-carolina/index.html': [
            ('/es/calculators/south-carolina/columbia-sc/', '/calculators/south-carolina/columbia-sc/'),
            ('/es/calculators/south-carolina/greenville/', '/calculators/south-carolina/greenville/')
        ],
        '/Users/glengomezmeade/Projects/plasma-pay-calculator/es/calculators/montana/index.html': [
            ('/es/calculators/montana/helena/', '/calculators/montana/helena/')
        ],
        '/Users/glengomezmeade/Projects/plasma-pay-calculator/es/calculators/minnesota/index.html': [
            ('/es/calculators/minnesota/st-paul/', '/calculators/minnesota/st-paul/'),
            ('/es/calculators/minnesota/rochester-mn/', '/calculators/minnesota/rochester-mn/'),
            ('/es/calculators/minnesota/bloomington-mn/', '/calculators/minnesota/bloomington-mn/')
        ],
        '/Users/glengomezmeade/Projects/plasma-pay-calculator/es/calculators/hawaii/index.html': [
            ('/es/calculators/hawaii/kailua-hi/', '/calculators/hawaii/kailua-hi/')
        ],
        '/Users/glengomezmeade/Projects/plasma-pay-calculator/es/calculators/kansas/index.html': [
            ('/es/calculators/kansas/kansas-city-ks/', '/calculators/kansas/kansas-city-ks/')
        ],
        '/Users/glengomezmeade/Projects/plasma-pay-calculator/es/calculators/nebraska/index.html': [
            ('/es/calculators/nebraska/bellevue-ne/', '/calculators/nebraska/bellevue-ne/')
        ],
        '/Users/glengomezmeade/Projects/plasma-pay-calculator/es/calculators/new-jersey/index.html': [
            ('/es/calculators/new-jersey/newark-nj/', '/calculators/new-jersey/newark-nj/')
        ],
        '/Users/glengomezmeade/Projects/plasma-pay-calculator/es/calculators/oregon/index.html': [
            ('/es/calculators/oregon/salem-or/', '/calculators/oregon/salem-or/')
        ]
    }
    
    # Fix each file
    for file_path, replacements in spanish_files.items():
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                content = f.read()
            
            for old_link, new_link in replacements:
                # Replace in href attributes
                content = content.replace(f'href="{old_link}"', f'href="{new_link}"')
                fixes_made += 1
                print(f"Fixed: {old_link} -> {new_link} in {os.path.basename(os.path.dirname(file_path))}")
            
            with open(file_path, 'w') as f:
                f.write(content)
    
    # Fix the blog link
    blog_file = '/Users/glengomezmeade/Projects/plasma-pay-calculator/blog/plasma-donation-eligibility-quiz-viral/index.html'
    if os.path.exists(blog_file):
        with open(blog_file, 'r') as f:
            content = f.read()
        
        # Link exists as directory, not as .html file
        content = content.replace('href="/blog/plasma-donation-frequency-guidelines/"', 'href="/blog/plasma-donation-frequency-guidelines.html"')
        
        with open(blog_file, 'w') as f:
            f.write(content)
        fixes_made += 1
        print(f"Fixed blog link in plasma-donation-eligibility-quiz-viral")
    
    print(f"\nTotal fixes made: {fixes_made}")
    return fixes_made

if __name__ == "__main__":
    fix_spanish_to_english_links()