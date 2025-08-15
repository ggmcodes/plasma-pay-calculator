#!/usr/bin/env python3

import os
import re
from pathlib import Path

def fix_canonical_in_file(filepath):
    """Fix canonical tags in HTML files"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Get the correct URL path
    rel_path = os.path.relpath(filepath, '/Users/glengomezmeade/Projects/plasma-pay-calculator')
    
    # Remove .html extension for canonical URL
    canonical_path = rel_path.replace('.html', '')
    if canonical_path.endswith('/index'):
        canonical_path = canonical_path[:-6] + '/'
    elif canonical_path == 'index':
        canonical_path = '/'
    else:
        canonical_path = '/' + canonical_path
    
    # Ensure trailing slash for directories
    if not canonical_path.endswith('/') and '.' not in os.path.basename(canonical_path):
        canonical_path += '/'
    
    canonical_url = f'https://plasmapaycalculator.com{canonical_path}'
    
    # Find and replace canonical tag
    canonical_pattern = r'<link[^>]*rel="canonical"[^>]*>'
    new_canonical = f'<link rel="canonical" href="{canonical_url}">'
    
    if re.search(canonical_pattern, content):
        content = re.sub(canonical_pattern, new_canonical, content)
    else:
        # Add canonical tag after title
        title_match = re.search(r'</title>', content)
        if title_match:
            insert_pos = title_match.end()
            content = content[:insert_pos] + f'\n{new_canonical}' + content[insert_pos:]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def create_redirects():
    """Create/update _redirects file for Netlify"""
    redirects_content = """# Redirects for Netlify

# Fix query parameter redirects
/?search=true /calculators/indiana/ 301!

# Fix old state paths
/state/* /calculators/:splat 301!

# Remove trailing .html from blog posts
/blog/*.html /blog/:splat 301!

# Fix blog subdirectory issues
/blog/california/centers.html /centers/ 301!
/blog/california/california-cities.html /calculators/california/ 301!

# Spanish blog redirect
/es/blog/cuanto-pagan-por-donar-plasma /blog/cuanto-pagan-por-donar-plasma-guia-completa-2025 301!

# FAQ redirect
/faq /faq.html 301!

# Add trailing slashes to directories
/calculators/michigan/lansing /calculators/michigan/lansing/ 301!
/calculators/oregon/eugene /calculators/oregon/eugene/ 301!
/calculators/new-jersey/edison /calculators/new-jersey/edison/ 301!
/calculators/wyoming/laramie /calculators/wyoming/laramie/ 301!
/calculators/hawaii/honolulu /calculators/hawaii/honolulu/ 301!
/calculators/ohio/akron /calculators/ohio/akron/ 301!
/calculators/oregon/salem /calculators/oregon/salem/ 301!
/calculators/south-dakota/watertown /calculators/south-dakota/watertown/ 301!
/calculators/georgia/savannah /calculators/georgia/savannah/ 301!
/calculators/virginia/virginia-beach /calculators/virginia/virginia-beach/ 301!

# Blog post redirects (remove .html)
/blog/plasma-donation-health-tips.html /blog/plasma-donation-health-tips/ 301!
/blog/plasma-donation-health-risks-medical-analysis-2025.html /blog/plasma-donation-health-risks-medical-analysis-2025/ 301!
/blog/california/how-to-increase-vein-size-plasma-donation.html /blog/how-to-increase-vein-size-plasma-donation/ 301!
/blog/cuanto-pagan-por-donar-plasma-guia-completa-2025.html /blog/cuanto-pagan-por-donar-plasma-guia-completa-2025/ 301!
/blog/plasma-donation-requirements.html /blog/plasma-donation-requirements/ 301!
/blog/plasma-donation-referral-income-maximization-2025.html /blog/plasma-donation-referral-income-maximization-2025/ 301!
/blog/emergency-money-plasma-donation-broke.html /blog/emergency-money-plasma-donation-broke/ 301!
/blog/guia-completa-donacion-plasma.html /blog/guia-completa-donacion-plasma/ 301!

# Spanish calculator redirects
/es/calculators/new-jersey/ /calculators/new-jersey/ 301!

# Existing redirects from plasmacenterfinder
https://plasmacenterfinder.com/* https://plasmapaycalculator.com/centers/:splat 301!
https://www.plasmacenterfinder.com/* https://plasmapaycalculator.com/centers/:splat 301!
http://plasmacenterfinder.com/* https://plasmapaycalculator.com/centers/:splat 301!
http://www.plasmacenterfinder.com/* https://plasmapaycalculator.com/centers/:splat 301!

# Specific path redirects
https://plasmacenterfinder.com/guides/* https://plasmapaycalculator.com/blog/:splat 301!
https://www.plasmacenterfinder.com/guides/* https://plasmapaycalculator.com/blog/:splat 301!
"""
    
    with open('/Users/glengomezmeade/Projects/plasma-pay-calculator/_redirects', 'w') as f:
        f.write(redirects_content)
    
    print("Created/updated _redirects file")

def fix_blog_urls():
    """Fix blog post URLs to not use .html"""
    blog_dir = '/Users/glengomezmeade/Projects/plasma-pay-calculator/blog'
    
    for filename in os.listdir(blog_dir):
        if filename.endswith('.html') and filename != 'index.html':
            filepath = os.path.join(blog_dir, filename)
            
            # Fix canonical tag
            fix_canonical_in_file(filepath)
            
            # Create directory structure for clean URLs
            name_without_ext = filename[:-5]
            new_dir = os.path.join(blog_dir, name_without_ext)
            
            if not os.path.exists(new_dir):
                os.makedirs(new_dir)
                
            # Copy file as index.html in new directory
            new_filepath = os.path.join(new_dir, 'index.html')
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Update canonical URL in the new file
            canonical_url = f'https://plasmapaycalculator.com/blog/{name_without_ext}/'
            content = re.sub(
                r'<link[^>]*rel="canonical"[^>]*>',
                f'<link rel="canonical" href="{canonical_url}">',
                content
            )
            
            with open(new_filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"Created clean URL structure for {name_without_ext}")

def create_missing_pages():
    """Create missing pages that are returning 404s"""
    
    # Create blog/california directory if it doesn't exist
    california_dir = '/Users/glengomezmeade/Projects/plasma-pay-calculator/blog/california'
    if not os.path.exists(california_dir):
        os.makedirs(california_dir)
    
    # Create redirect pages for California blog posts
    redirects = {
        'centers.html': '/centers/',
        'california-cities.html': '/calculators/california/',
        'california-plasma-donation-earnings-calculator.html': '/calculators/california/',
        'california-plasma-donation-budget-planning.html': '/calculators/california/'
    }
    
    for filename, redirect_to in redirects.items():
        filepath = os.path.join(california_dir, filename)
        content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="refresh" content="0; url={redirect_to}">
    <link rel="canonical" href="https://plasmapaycalculator.com{redirect_to}">
    <title>Redirecting...</title>
</head>
<body>
    <p>This page has moved. Redirecting to <a href="{redirect_to}">{redirect_to}</a>...</p>
</body>
</html>'''
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Created redirect page: {filename}")

def fix_calculator_pages():
    """Ensure all calculator pages have proper canonical tags and directory structure"""
    calc_dir = '/Users/glengomezmeade/Projects/plasma-pay-calculator/calculators'
    
    for root, dirs, files in os.walk(calc_dir):
        for file in files:
            if file == 'index.html':
                filepath = os.path.join(root, file)
                fix_canonical_in_file(filepath)

def main():
    print("Fixing all SEO issues...")
    
    print("\n1. Creating/updating redirects...")
    create_redirects()
    
    print("\n2. Fixing blog URLs and creating clean URL structure...")
    fix_blog_urls()
    
    print("\n3. Creating missing pages...")
    create_missing_pages()
    
    print("\n4. Fixing calculator canonical tags...")
    fix_calculator_pages()
    
    print("\n✅ All SEO issues fixed!")
    print("\nChanges made:")
    print("- Created _redirects file with all necessary redirects")
    print("- Created clean URL structure for blog posts (directories with index.html)")
    print("- Fixed canonical tags on all pages")
    print("- Created redirect pages for missing California blog posts")
    print("\nReady to push to GitHub and submit to Google Search Console!")

if __name__ == '__main__':
    main()