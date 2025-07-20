#!/usr/bin/env python3
"""
Fix canonical tag and URL structure issues for better SEO indexing
"""

import os
import re
from pathlib import Path

def fix_calculator_canonical_tags():
    """Fix trailing slash issues in calculator page canonical tags"""
    
    # Find all calculator index.html files
    calculator_pages = []
    calculators_dir = "/Users/glengomezmeade/Projects/plasma-pay-calculator/calculators"
    
    for root, dirs, files in os.walk(calculators_dir):
        if "index.html" in files:
            calculator_pages.append(os.path.join(root, "index.html"))
    
    fixed_count = 0
    
    for page_path in calculator_pages:
        try:
            with open(page_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Fix canonical tags - remove trailing slash for consistency with actual serving
            # Change from /calculators/state/ to /calculators/state
            content = re.sub(
                r'<link rel="canonical" href="https://plasmapaycalculator\.com/calculators/([^/]+)/">',
                r'<link rel="canonical" href="https://plasmapaycalculator.com/calculators/\1">',
                content
            )
            
            # Also fix Open Graph URLs to match
            content = re.sub(
                r'<meta property="og:url" content="https://plasmapaycalculator\.com/calculators/([^/]+)/">',
                r'<meta property="og:url" content="https://plasmapaycalculator.com/calculators/\1">',
                content
            )
            
            if content != original_content:
                with open(page_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                rel_path = os.path.relpath(page_path, "/Users/glengomezmeade/Projects/plasma-pay-calculator")
                print(f"✅ Fixed canonical tag in {rel_path}")
                fixed_count += 1
            else:
                rel_path = os.path.relpath(page_path, "/Users/glengomezmeade/Projects/plasma-pay-calculator")
                print(f"ℹ️ No canonical changes needed in {rel_path}")
                
        except Exception as e:
            rel_path = os.path.relpath(page_path, "/Users/glengomezmeade/Projects/plasma-pay-calculator")
            print(f"❌ Error fixing canonical in {rel_path}: {str(e)}")
    
    return fixed_count

def fix_blog_canonical_tags():
    """Fix blog post canonical tags to match serving URLs"""
    
    blog_dir = "/Users/glengomezmeade/Projects/plasma-pay-calculator/blog"
    
    # Blog posts that need canonical fixes
    blog_posts = [
        "plasma-center-comparison.html",
        "maximize-plasma-earnings.html"
    ]
    
    fixed_count = 0
    
    for filename in blog_posts:
        file_path = os.path.join(blog_dir, filename)
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                
                # Fix canonical tags - remove .html extension for cleaner URLs
                base_name = filename.replace('.html', '')
                
                # Update canonical tag
                content = re.sub(
                    r'<link rel="canonical" href="https://plasmapaycalculator\.com/blog/[^"]+\.html">',
                    f'<link rel="canonical" href="https://plasmapaycalculator.com/blog/{base_name}">',
                    content
                )
                
                # Also fix Open Graph URL
                content = re.sub(
                    r'<meta property="og:url" content="https://plasmapaycalculator\.com/blog/[^"]+\.html">',
                    f'<meta property="og:url" content="https://plasmapaycalculator.com/blog/{base_name}">',
                    content
                )
                
                if content != original_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    print(f"✅ Fixed canonical tag in blog/{filename}")
                    fixed_count += 1
                else:
                    print(f"ℹ️ No canonical changes needed in blog/{filename}")
                    
            except Exception as e:
                print(f"❌ Error fixing canonical in blog/{filename}: {str(e)}")
        else:
            print(f"⚠️ Blog file not found: {filename}")
    
    return fixed_count

def fix_root_page_canonicals():
    """Fix canonical tags on root pages"""
    
    root_pages = [
        "/Users/glengomezmeade/Projects/plasma-pay-calculator/plasma-donation-requirements-2025.html",
        "/Users/glengomezmeade/Projects/plasma-pay-calculator/index.html"
    ]
    
    fixed_count = 0
    
    for page_path in root_pages:
        if os.path.exists(page_path):
            try:
                with open(page_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                
                # Fix canonical to ensure no .html extension on root pages
                if "plasma-donation-requirements-2025.html" in page_path:
                    content = re.sub(
                        r'<link rel="canonical" href="https://plasmapaycalculator\.com/plasma-donation-requirements-2025">',
                        '<link rel="canonical" href="https://plasmapaycalculator.com/plasma-donation-requirements-2025">',
                        content
                    )
                elif "index.html" in page_path:
                    # Ensure homepage canonical is clean
                    content = re.sub(
                        r'<link rel="canonical" href="https://plasmapaycalculator\.com/index\.html">',
                        '<link rel="canonical" href="https://plasmapaycalculator.com/">',
                        content
                    )
                    content = re.sub(
                        r'<link rel="canonical" href="https://plasmapaycalculator\.com">',
                        '<link rel="canonical" href="https://plasmapaycalculator.com/">',
                        content
                    )
                
                if content != original_content:
                    with open(page_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    rel_path = os.path.relpath(page_path, "/Users/glengomezmeade/Projects/plasma-pay-calculator")
                    print(f"✅ Fixed canonical tag in {rel_path}")
                    fixed_count += 1
                else:
                    rel_path = os.path.relpath(page_path, "/Users/glengomezmeade/Projects/plasma-pay-calculator")
                    print(f"ℹ️ No canonical changes needed in {rel_path}")
                    
            except Exception as e:
                rel_path = os.path.relpath(page_path, "/Users/glengomezmeade/Projects/plasma-pay-calculator")
                print(f"❌ Error fixing canonical in {rel_path}: {str(e)}")
    
    return fixed_count

def create_redirect_rules():
    """Create 301 redirect rules for URL variations"""
    
    redirects_content = """
# URL Structure Canonicalization Redirects

# Force HTTPS and non-www
http://plasmapaycalculator.com/* https://plasmapaycalculator.com/:splat 301!
http://www.plasmapaycalculator.com/* https://plasmapaycalculator.com/:splat 301!
https://www.plasmapaycalculator.com/* https://plasmapaycalculator.com/:splat 301!

# Calculator trailing slash redirects (remove trailing slash)
/calculators/*/  /calculators/:splat 301

# Blog post .html redirects (remove .html)
/blog/*.html /blog/:splat 301

# Specific blog post redirects mentioned in GSC
/blog/plasma-center-comparison.html /blog/plasma-center-comparison 301
/blog/maximize-plasma-earnings.html /blog/maximize-plasma-earnings 301

# Root page .html redirects
/plasma-donation-requirements-2025.html /plasma-donation-requirements-2025 301
/index.html / 301

# Ensure clean URLs for common variations
/calculators/georgia/ /calculators/georgia 301
/calculators/california/ /calculators/california 301
"""
    
    redirects_path = "/Users/glengomezmeade/Projects/plasma-pay-calculator/_redirects"
    
    try:
        # Check if _redirects file already exists
        if os.path.exists(redirects_path):
            with open(redirects_path, 'r', encoding='utf-8') as f:
                existing_content = f.read()
            
            # Append new redirects if they don't already exist
            if "URL Structure Canonicalization Redirects" not in existing_content:
                with open(redirects_path, 'a', encoding='utf-8') as f:
                    f.write(redirects_content)
                print("✅ Added canonical redirect rules to existing _redirects file")
                return True
            else:
                print("ℹ️ Canonical redirect rules already exist in _redirects file")
                return False
        else:
            # Create new _redirects file
            with open(redirects_path, 'w', encoding='utf-8') as f:
                f.write(redirects_content.strip())
            print("✅ Created new _redirects file with canonical rules")
            return True
            
    except Exception as e:
        print(f"❌ Error creating redirect rules: {str(e)}")
        return False

def main():
    """Main function to fix all canonical and URL issues"""
    print("🔧 Fixing canonical tags and URL structure issues...")
    
    total_fixes = 0
    
    # Fix 1: Calculator page canonicals
    print("\n📊 Fixing calculator page canonical tags...")
    calc_fixes = fix_calculator_canonical_tags()
    total_fixes += calc_fixes
    print(f"✅ Fixed {calc_fixes} calculator page canonicals")
    
    # Fix 2: Blog post canonicals  
    print("\n📝 Fixing blog post canonical tags...")
    blog_fixes = fix_blog_canonical_tags()
    total_fixes += blog_fixes
    print(f"✅ Fixed {blog_fixes} blog post canonicals")
    
    # Fix 3: Root page canonicals
    print("\n🏠 Fixing root page canonical tags...")
    root_fixes = fix_root_page_canonicals()
    total_fixes += root_fixes
    print(f"✅ Fixed {root_fixes} root page canonicals")
    
    # Fix 4: Create redirect rules
    print("\n🔀 Creating 301 redirect rules...")
    if create_redirect_rules():
        total_fixes += 1
        print("✅ Added redirect rules for URL variations")
    
    print(f"\n🎉 Canonical and URL structure fixes complete!")
    print(f"📊 Total fixes applied: {total_fixes}")
    print(f"🌟 URLs now have consistent structure for better SEO")
    print(f"📈 Google should properly index all pages after next crawl")

if __name__ == "__main__":
    main()