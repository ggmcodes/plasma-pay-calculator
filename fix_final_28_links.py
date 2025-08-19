#!/usr/bin/env python3
import os
import re

def fix_final_links():
    """Fix the final 28 broken links"""
    
    fixes_made = 0
    
    # Fix 1: blog/plasma-donation-eligibility-quiz-viral/index.html 
    # Link: /blog/plasma-donation-frequency-guidelines.html should be /blog/plasma-donation-frequency-guidelines/
    file1 = '/Users/glengomezmeade/Projects/plasma-pay-calculator/blog/plasma-donation-eligibility-quiz-viral/index.html'
    if os.path.exists(file1):
        with open(file1, 'r') as f:
            content = f.read()
        
        # Fix the broken link
        content = content.replace('/blog/plasma-donation-frequency-guidelines.html', '/blog/plasma-donation-frequency-guidelines/')
        
        with open(file1, 'w') as f:
            f.write(content)
        fixes_made += 1
        print(f"Fixed link in {file1}")
    
    # Fix 2: blog/ab-plasma-secret-income-revealed/index.html
    # Link: ../blog/ab-plasma-donation-calculator.html should be /blog/ab-plasma-donation-calculator/
    file2 = '/Users/glengomezmeade/Projects/plasma-pay-calculator/blog/ab-plasma-secret-income-revealed/index.html'
    if os.path.exists(file2):
        with open(file2, 'r') as f:
            content = f.read()
        
        # Fix the broken link
        content = content.replace('../blog/ab-plasma-donation-calculator.html', '/blog/ab-plasma-donation-calculator/')
        
        with open(file2, 'w') as f:
            f.write(content)
        fixes_made += 1
        print(f"Fixed link in {file2}")
    
    # Fix 3: Create favicon.svg files where they're missing
    favicon_locations = [
        '/Users/glengomezmeade/Projects/plasma-pay-calculator/calculators/',
        '/Users/glengomezmeade/Projects/plasma-pay-calculator/es/'
    ]
    
    # First check if a favicon.svg exists in root
    root_favicon = '/Users/glengomezmeade/Projects/plasma-pay-calculator/favicon.svg'
    if os.path.exists(root_favicon):
        # Copy it to missing locations
        with open(root_favicon, 'r') as f:
            favicon_content = f.read()
    else:
        # Create a simple SVG favicon
        favicon_content = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">
  <rect width="32" height="32" fill="#27ae60"/>
  <text x="16" y="22" font-family="Arial, sans-serif" font-size="20" font-weight="bold" text-anchor="middle" fill="white">$</text>
</svg>'''
    
    for location in favicon_locations:
        favicon_path = os.path.join(location, 'favicon.svg')
        if not os.path.exists(favicon_path):
            os.makedirs(location, exist_ok=True)
            with open(favicon_path, 'w') as f:
                f.write(favicon_content)
            fixes_made += 1
            print(f"Created favicon.svg at {favicon_path}")
    
    # Fix 4: Remove Spanish /es/ links that don't exist
    # These are on Spanish state pages linking to cities that don't exist
    spanish_state_files = [
        '/Users/glengomezmeade/Projects/plasma-pay-calculator/es/calculators/missouri/index.html',
        '/Users/glengomezmeade/Projects/plasma-pay-calculator/es/calculators/virginia/index.html',
        '/Users/glengomezmeade/Projects/plasma-pay-calculator/es/calculators/maine/index.html',
        '/Users/glengomezmeade/Projects/plasma-pay-calculator/es/calculators/delaware/index.html',
        '/Users/glengomezmeade/Projects/plasma-pay-calculator/es/calculators/iowa/index.html',
        '/Users/glengomezmeade/Projects/plasma-pay-calculator/es/calculators/new-hampshire/index.html',
        '/Users/glengomezmeade/Projects/plasma-pay-calculator/es/calculators/west-virginia/index.html',
        '/Users/glengomezmeade/Projects/plasma-pay-calculator/es/calculators/south-dakota/index.html',
        '/Users/glengomezmeade/Projects/plasma-pay-calculator/es/calculators/south-carolina/index.html',
        '/Users/glengomezmeade/Projects/plasma-pay-calculator/es/calculators/montana/index.html',
        '/Users/glengomezmeade/Projects/plasma-pay-calculator/es/calculators/minnesota/index.html',
        '/Users/glengomezmeade/Projects/plasma-pay-calculator/es/calculators/hawaii/index.html',
        '/Users/glengomezmeade/Projects/plasma-pay-calculator/es/calculators/kansas/index.html',
        '/Users/glengomezmeade/Projects/plasma-pay-calculator/es/calculators/nebraska/index.html',
        '/Users/glengomezmeade/Projects/plasma-pay-calculator/es/calculators/new-jersey/index.html',
        '/Users/glengomezmeade/Projects/plasma-pay-calculator/es/calculators/oregon/index.html'
    ]
    
    for file_path in spanish_state_files:
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                content = f.read()
            
            # Find all /es/calculators/ city links and replace with English versions
            # Pattern: /es/calculators/STATE/CITY/ -> /calculators/STATE/CITY/
            content = re.sub(r'href="/es/calculators/([^"]+)"', r'href="/calculators/\1"', content)
            
            with open(file_path, 'w') as f:
                f.write(content)
            fixes_made += 1
            print(f"Fixed Spanish links in {file_path}")
    
    print(f"\nTotal fixes made: {fixes_made}")
    return fixes_made

if __name__ == "__main__":
    fix_final_links()