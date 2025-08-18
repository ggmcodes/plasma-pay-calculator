#!/usr/bin/env python3
import os
import re
from pathlib import Path

blog_dir = Path('/Users/glengomezmeade/Projects/plasma-pay-calculator/blog')
issues = []

for html_file in blog_dir.glob('*.html'):
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for empty section divs
    empty_sections = re.findall(r'<h2[^>]*>(.*?)</h2>\s*<div[^>]*>\s*\n\s*</div>', content, re.DOTALL)
    
    # Check for sections with just whitespace
    whitespace_sections = re.findall(r'<div class="bg-white rounded-xl shadow-md p-6">\s*\n\s*</div>', content)
    
    # Check for specific missing sections in plasma-related files
    filename = html_file.name
    if 'plasma' in filename.lower() or 'csl' in filename.lower() or 'biolife' in filename.lower() or 'octapharma' in filename.lower():
        has_payment_methods = '💳 Payment Methods' in content
        has_bonuses = '🎯 Special Bonuses' in content  
        has_rights = '🛡️ Donor Rights' in content
        
        if not has_payment_methods or not has_bonuses:
            issues.append({
                'file': filename,
                'empty_sections': len(empty_sections),
                'whitespace_sections': len(whitespace_sections),
                'missing_payment_methods': not has_payment_methods,
                'missing_bonuses': not has_bonuses,
                'missing_rights': not has_rights
            })
    elif empty_sections or whitespace_sections:
        issues.append({
            'file': filename,
            'empty_sections': len(empty_sections),
            'whitespace_sections': len(whitespace_sections),
            'missing_payment_methods': False,
            'missing_bonuses': False,
            'missing_rights': False
        })

# Print report
print(f"=== BLOG CONTENT AUDIT REPORT ===\n")
print(f"Total files scanned: {len(list(blog_dir.glob('*.html')))}")
print(f"Files with issues: {len(issues)}\n")

if issues:
    print("CRITICAL ISSUES FOUND:\n")
    
    # Group by issue type
    empty_section_files = [i for i in issues if i['empty_sections'] > 0 or i['whitespace_sections'] > 0]
    missing_content_files = [i for i in issues if i['missing_payment_methods'] or i['missing_bonuses'] or i['missing_rights']]
    
    if empty_section_files:
        print(f"\n📌 Files with EMPTY sections ({len(empty_section_files)} files):")
        for issue in empty_section_files[:10]:
            print(f"  - {issue['file']}: {issue['empty_sections'] + issue['whitespace_sections']} empty sections")
    
    if missing_content_files:
        print(f"\n📌 Plasma/Center files MISSING key sections ({len(missing_content_files)} files):")
        for issue in missing_content_files[:10]:
            missing = []
            if issue['missing_payment_methods']: missing.append('Payment Methods')
            if issue['missing_bonuses']: missing.append('Bonuses')
            if issue['missing_rights']: missing.append('Donor Rights')
            print(f"  - {issue['file']}: Missing {', '.join(missing)}")