#!/usr/bin/env python3
"""
Update sitemap.xml to match the new canonical URL structure
"""

import os
import re
from datetime import datetime

def update_sitemap_urls():
    """Update sitemap.xml to use consistent canonical URL format"""
    
    sitemap_path = "/Users/glengomezmeade/Projects/plasma-pay-calculator/sitemap.xml"
    
    if not os.path.exists(sitemap_path):
        print("❌ Sitemap.xml not found")
        return False
    
    try:
        with open(sitemap_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Fix 1: Remove trailing slashes from calculator URLs
        content = re.sub(
            r'<loc>https://plasmapaycalculator\.com/calculators/([^/]+)/</loc>',
            r'<loc>https://plasmapaycalculator.com/calculators/\1</loc>',
            content
        )
        
        # Fix 2: Remove .html from blog post URLs (if any)
        content = re.sub(
            r'<loc>https://plasmapaycalculator\.com/blog/([^<]+)\.html</loc>',
            r'<loc>https://plasmapaycalculator.com/blog/\1</loc>',
            content
        )
        
        # Fix 3: Update lastmod dates to current date for changed URLs
        current_date = datetime.now().strftime('%Y-%m-%d')
        
        # Update lastmod for any URLs we just changed
        content = re.sub(
            r'(<loc>https://plasmapaycalculator\.com/calculators/[^<]+</loc>\s*<lastmod>)[^<]+(</lastmod>)',
            f'\\1{current_date}\\2',
            content
        )
        
        content = re.sub(
            r'(<loc>https://plasmapaycalculator\.com/blog/[^<]+</loc>\s*<lastmod>)[^<]+(</lastmod>)',
            f'\\1{current_date}\\2',
            content
        )
        
        # Fix 4: Ensure homepage is clean (no index.html)
        content = re.sub(
            r'<loc>https://plasmapaycalculator\.com/index\.html</loc>',
            '<loc>https://plasmapaycalculator.com/</loc>',
            content
        )
        
        # Fix 5: Remove any duplicate entries that might exist
        # Split into lines, remove duplicates while preserving order
        lines = content.split('\n')
        seen_urls = set()
        unique_lines = []
        
        for line in lines:
            # Check if this is a URL line
            url_match = re.search(r'<loc>(https://[^<]+)</loc>', line)
            if url_match:
                url = url_match.group(1)
                if url not in seen_urls:
                    seen_urls.add(url)
                    unique_lines.append(line)
            else:
                unique_lines.append(line)
        
        content = '\n'.join(unique_lines)
        
        if content != original_content:
            with open(sitemap_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print("✅ Updated sitemap.xml with canonical URL structure")
            return True
        else:
            print("ℹ️ Sitemap.xml already uses correct URL structure")
            return False
            
    except Exception as e:
        print(f"❌ Error updating sitemap: {str(e)}")
        return False

def add_missing_urls_to_sitemap():
    """Add any important URLs that might be missing from sitemap"""
    
    sitemap_path = "/Users/glengomezmeade/Projects/plasma-pay-calculator/sitemap.xml"
    
    # Important URLs that should be in sitemap
    important_urls = [
        "https://plasmapaycalculator.com/",
        "https://plasmapaycalculator.com/blog/",
        "https://plasmapaycalculator.com/states.html",
        "https://plasmapaycalculator.com/about.html",
        "https://plasmapaycalculator.com/faq.html",
        "https://plasmapaycalculator.com/centers/",
        "https://plasmapaycalculator.com/health/",
        "https://plasmapaycalculator.com/plasma-donation-requirements-2025"
    ]
    
    try:
        with open(sitemap_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check which URLs are missing
        missing_urls = []
        for url in important_urls:
            if f"<loc>{url}</loc>" not in content:
                missing_urls.append(url)
        
        if missing_urls:
            # Add missing URLs before the closing </urlset> tag
            current_date = datetime.now().strftime('%Y-%m-%d')
            new_entries = []
            
            for url in missing_urls:
                new_entry = f"""  <url>
    <loc>{url}</loc>
    <lastmod>{current_date}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>"""
                new_entries.append(new_entry)
            
            # Insert before closing tag
            new_content = content.replace(
                '</urlset>',
                '\n' + '\n'.join(new_entries) + '\n</urlset>'
            )
            
            with open(sitemap_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"✅ Added {len(missing_urls)} missing URLs to sitemap")
            return True
        else:
            print("ℹ️ All important URLs already in sitemap")
            return False
            
    except Exception as e:
        print(f"❌ Error adding URLs to sitemap: {str(e)}")
        return False

def validate_sitemap():
    """Basic validation of sitemap.xml"""
    
    sitemap_path = "/Users/glengomezmeade/Projects/plasma-pay-calculator/sitemap.xml"
    
    try:
        with open(sitemap_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Count URLs
        url_count = len(re.findall(r'<loc>', content))
        
        # Check for common issues
        issues = []
        
        # Check for trailing slashes in calculator URLs
        trailing_slash_calculators = re.findall(r'<loc>https://plasmapaycalculator\.com/calculators/[^/]+/</loc>', content)
        if trailing_slash_calculators:
            issues.append(f"Found {len(trailing_slash_calculators)} calculator URLs with trailing slashes")
        
        # Check for .html in blog URLs
        html_blog_urls = re.findall(r'<loc>https://plasmapaycalculator\.com/blog/[^<]+\.html</loc>', content)
        if html_blog_urls:
            issues.append(f"Found {len(html_blog_urls)} blog URLs with .html extension")
        
        # Check for proper XML structure
        if not content.startswith('<?xml') or '</urlset>' not in content:
            issues.append("Invalid XML structure")
        
        print(f"📊 Sitemap validation results:")
        print(f"  - Total URLs: {url_count}")
        
        if issues:
            print(f"  - Issues found: {len(issues)}")
            for issue in issues:
                print(f"    • {issue}")
            return False
        else:
            print(f"  - ✅ No issues found")
            return True
            
    except Exception as e:
        print(f"❌ Error validating sitemap: {str(e)}")
        return False

def main():
    """Main function to update sitemap"""
    print("🗺️ Updating sitemap.xml for canonical URL structure...")
    
    total_changes = 0
    
    # Update existing URLs to canonical format
    print("\n📝 Updating existing URLs...")
    if update_sitemap_urls():
        total_changes += 1
    
    # Add any missing important URLs
    print("\n➕ Adding missing URLs...")
    if add_missing_urls_to_sitemap():
        total_changes += 1
    
    # Validate the final sitemap
    print("\n✅ Validating sitemap...")
    is_valid = validate_sitemap()
    
    print(f"\n🎉 Sitemap update complete!")
    print(f"📊 Changes made: {total_changes}")
    
    if is_valid:
        print(f"✅ Sitemap is valid and ready for search engines")
    else:
        print(f"⚠️ Sitemap has validation issues that need attention")

if __name__ == "__main__":
    main()