#!/usr/bin/env python3
"""
Comprehensive SEO audit for PPC to achieve #1 Google ranking
"""

import os
import re
from pathlib import Path
import json

def audit_seo_fundamentals():
    """Audit basic SEO elements"""
    
    base_dir = "/Users/glengomezmeade/Projects/plasma-pay-calculator"
    
    print("🎯 SEO FUNDAMENTALS AUDIT")
    print("=" * 80)
    
    seo_issues = []
    pages_audited = 0
    
    # Walk through all HTML files
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if not file.endswith('.html'):
                continue
                
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, base_dir)
            
            # Skip certain directories
            if any(skip in relative_path for skip in ['.git', 'node_modules', '.vscode']):
                continue
            
            pages_audited += 1
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Check title tag
                title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
                if not title_match:
                    seo_issues.append(f"❌ {relative_path}: Missing <title> tag")
                elif len(title_match.group(1).strip()) < 30:
                    seo_issues.append(f"⚠️  {relative_path}: Title too short ({len(title_match.group(1))} chars)")
                elif len(title_match.group(1).strip()) > 60:
                    seo_issues.append(f"⚠️  {relative_path}: Title too long ({len(title_match.group(1))} chars)")
                
                # Check meta description
                meta_desc = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', content, re.IGNORECASE)
                if not meta_desc:
                    seo_issues.append(f"❌ {relative_path}: Missing meta description")
                elif len(meta_desc.group(1).strip()) < 120:
                    seo_issues.append(f"⚠️  {relative_path}: Meta description too short ({len(meta_desc.group(1))} chars)")
                elif len(meta_desc.group(1).strip()) > 160:
                    seo_issues.append(f"⚠️  {relative_path}: Meta description too long ({len(meta_desc.group(1))} chars)")
                
                # Check H1 tag
                h1_matches = re.findall(r'<h1[^>]*>(.*?)</h1>', content, re.IGNORECASE | re.DOTALL)
                if not h1_matches:
                    seo_issues.append(f"❌ {relative_path}: Missing <h1> tag")
                elif len(h1_matches) > 1:
                    seo_issues.append(f"⚠️  {relative_path}: Multiple H1 tags ({len(h1_matches)})")
                
                # Check heading hierarchy
                headings = re.findall(r'<h([1-6])[^>]*>', content, re.IGNORECASE)
                if headings:
                    heading_levels = [int(h) for h in headings]
                    # Check if it starts with H1
                    if heading_levels[0] != 1:
                        seo_issues.append(f"⚠️  {relative_path}: First heading is not H1")
                
                # Check alt text for images
                img_tags = re.findall(r'<img[^>]*>', content, re.IGNORECASE)
                missing_alt = 0
                for img in img_tags:
                    if 'alt=' not in img.lower():
                        missing_alt += 1
                if missing_alt > 0:
                    seo_issues.append(f"⚠️  {relative_path}: {missing_alt} images missing alt text")
                
                # Check schema markup
                if 'application/ld+json' not in content:
                    seo_issues.append(f"⚠️  {relative_path}: Missing structured data (schema.org)")
                
                # Check canonical URL
                if 'rel="canonical"' not in content:
                    seo_issues.append(f"⚠️  {relative_path}: Missing canonical URL")
                
                # Check hreflang for Spanish pages
                is_spanish = '/es/' in relative_path or relative_path.startswith('es/')
                if is_spanish and 'hreflang=' not in content:
                    seo_issues.append(f"⚠️  {relative_path}: Missing hreflang attributes")
                
            except Exception as e:
                seo_issues.append(f"❌ {relative_path}: Error reading file - {e}")
    
    return pages_audited, seo_issues

def audit_keyword_optimization():
    """Audit keyword usage and optimization"""
    
    print("\n🔍 KEYWORD OPTIMIZATION AUDIT")
    print("=" * 80)
    
    target_keywords = [
        'plasma donation',
        'plasma pay',
        'plasma calculator',
        'donating plasma',
        'plasma centers',
        'plasma earnings',
        'how much plasma donation pay',
        'best plasma centers',
        'CSL plasma',
        'BioLife plasma'
    ]
    
    spanish_keywords = [
        'donación de plasma',
        'calculadora de plasma',
        'pago de plasma',
        'centros de plasma',
        'ganancias plasma',
        'donación plasma dinero'
    ]
    
    base_dir = "/Users/glengomezmeade/Projects/plasma-pay-calculator"
    keyword_analysis = {}
    
    # Sample a few key pages
    key_pages = [
        'index.html',
        'calculators/california/index.html', 
        'es/index.html',
        'es/calculators/california/index.html'
    ]
    
    for page in key_pages:
        page_path = os.path.join(base_dir, page)
        if os.path.exists(page_path):
            try:
                with open(page_path, 'r', encoding='utf-8') as f:
                    content = f.read().lower()
                
                is_spanish = '/es/' in page or page.startswith('es/')
                keywords_to_check = spanish_keywords if is_spanish else target_keywords
                
                page_keywords = {}
                for keyword in keywords_to_check:
                    count = content.count(keyword.lower())
                    page_keywords[keyword] = count
                
                keyword_analysis[page] = page_keywords
                
            except Exception as e:
                print(f"⚠️  Error reading {page}: {e}")
    
    # Report keyword usage
    for page, keywords in keyword_analysis.items():
        print(f"\n📄 {page}:")
        for keyword, count in keywords.items():
            if count == 0:
                print(f"  ❌ '{keyword}': Not found")
            elif count < 3:
                print(f"  ⚠️  '{keyword}': {count} occurrences (low)")
            else:
                print(f"  ✅ '{keyword}': {count} occurrences")
    
    return keyword_analysis

def audit_technical_seo():
    """Audit technical SEO elements"""
    
    print("\n⚙️ TECHNICAL SEO AUDIT")
    print("=" * 80)
    
    base_dir = "/Users/glengomezmeade/Projects/plasma-pay-calculator"
    technical_issues = []
    
    # Check for robots.txt
    robots_path = os.path.join(base_dir, 'robots.txt')
    if not os.path.exists(robots_path):
        technical_issues.append("❌ Missing robots.txt file")
    else:
        print("✅ robots.txt exists")
    
    # Check for sitemap.xml
    sitemap_path = os.path.join(base_dir, 'sitemap.xml')
    if not os.path.exists(sitemap_path):
        technical_issues.append("❌ Missing sitemap.xml file")
    else:
        print("✅ sitemap.xml exists")
        
        # Check sitemap content
        try:
            with open(sitemap_path, 'r') as f:
                sitemap_content = f.read()
            
            # Count URLs in sitemap
            url_count = sitemap_content.count('<url>')
            print(f"📊 Sitemap contains {url_count} URLs")
            
            # Check for Spanish URLs
            spanish_urls = sitemap_content.count('/es/')
            print(f"📊 Sitemap contains {spanish_urls} Spanish URLs")
            
            if spanish_urls == 0:
                technical_issues.append("⚠️  Sitemap missing Spanish URLs")
                
        except Exception as e:
            technical_issues.append(f"❌ Error reading sitemap: {e}")
    
    # Check for essential files
    essential_files = ['favicon.ico', 'manifest.json']
    for file in essential_files:
        if not os.path.exists(os.path.join(base_dir, file)):
            technical_issues.append(f"⚠️  Missing {file}")
    
    return technical_issues

def audit_page_speed():
    """Basic page speed audit"""
    
    print("\n⚡ PAGE SPEED AUDIT")
    print("=" * 80)
    
    base_dir = "/Users/glengomezmeade/Projects/plasma-pay-calculator"
    speed_issues = []
    
    # Check CSS files
    css_files = []
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.css'):
                file_path = os.path.join(root, file)
                size = os.path.getsize(file_path)
                css_files.append((file, size))
    
    total_css_size = sum(size for _, size in css_files)
    print(f"📊 Total CSS size: {total_css_size / 1024:.1f} KB")
    
    if total_css_size > 100000:  # 100KB
        speed_issues.append(f"⚠️  Large CSS files: {total_css_size / 1024:.1f} KB")
    
    # Check JS files
    js_files = []
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.js') and 'node_modules' not in root:
                file_path = os.path.join(root, file)
                size = os.path.getsize(file_path)
                js_files.append((file, size))
    
    total_js_size = sum(size for _, size in js_files)
    print(f"📊 Total JS size: {total_js_size / 1024:.1f} KB")
    
    if total_js_size > 200000:  # 200KB
        speed_issues.append(f"⚠️  Large JavaScript files: {total_js_size / 1024:.1f} KB")
    
    return speed_issues

def main():
    """Run comprehensive SEO audit"""
    
    print("🎯 COMPREHENSIVE PPC SEO AUDIT")
    print("🎯 Optimizing for #1 Google Rankings")
    print("=" * 80)
    
    # Run all audits
    pages_audited, seo_issues = audit_seo_fundamentals()
    keyword_analysis = audit_keyword_optimization()
    technical_issues = audit_technical_seo()
    speed_issues = audit_page_speed()
    
    # Summary
    total_issues = len(seo_issues) + len(technical_issues) + len(speed_issues)
    
    print(f"\n🏁 SEO AUDIT SUMMARY")
    print("=" * 80)
    print(f"📊 Pages audited: {pages_audited}")
    print(f"❌ SEO issues: {len(seo_issues)}")
    print(f"❌ Technical issues: {len(technical_issues)}")
    print(f"❌ Speed issues: {len(speed_issues)}")
    print(f"🎯 Total issues: {total_issues}")
    
    if total_issues == 0:
        print("\n✅ PERFECT SEO - Ready for #1 Google rankings!")
    else:
        print(f"\n⚠️  SEO optimization needed - {total_issues} issues to fix")
        
        # Show critical issues
        print("\n🚨 CRITICAL SEO ISSUES:")
        critical_count = 0
        for issue in seo_issues[:20]:  # Show first 20
            if "❌" in issue:
                print(f"  {issue}")
                critical_count += 1
        
        for issue in technical_issues:
            print(f"  {issue}")
        
        if critical_count > 20:
            print(f"  ... and {len(seo_issues) - 20} more issues")
    
    return {
        'pages_audited': pages_audited,
        'seo_issues': seo_issues,
        'technical_issues': technical_issues,
        'speed_issues': speed_issues,
        'keyword_analysis': keyword_analysis
    }

if __name__ == "__main__":
    main()