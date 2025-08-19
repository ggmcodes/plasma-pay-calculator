#!/usr/bin/env python3
import os
import re

def final_comprehensive_fix():
    """Final comprehensive fix for all remaining broken links"""
    
    fixes_made = 0
    
    # 1. Create the missing blog file (link to existing similar content)
    missing_blog = '/Users/glengomezmeade/Projects/plasma-pay-calculator/blog/plasma-donation-frequency-guidelines.html'
    existing_blog = '/Users/glengomezmeade/Projects/plasma-pay-calculator/blog/plasma-donation-frequency-schedule-optimization-2025.html'
    
    if not os.path.exists(missing_blog) and os.path.exists(existing_blog):
        # Copy the existing similar blog post
        with open(existing_blog, 'r') as f:
            content = f.read()
        with open(missing_blog, 'w') as f:
            f.write(content)
        print(f"Created missing blog file: plasma-donation-frequency-guidelines.html")
        fixes_made += 1
    
    # 2. Fix ALL Spanish links (both href and onclick) to point to English versions
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
            
            original_content = content
            
            # Fix all /es/calculators/ links to /calculators/ (in href attributes)
            content = re.sub(r'href="/es/calculators/', r'href="/calculators/', content)
            
            # Fix all /es/calculators/ links in onclick handlers
            content = re.sub(r"location\.href='/es/calculators/", r"location.href='/calculators/", content)
            content = re.sub(r'location\.href="/es/calculators/', r'location.href="/calculators/', content)
            
            # Also fix escaped quotes in onclick
            content = re.sub(r"\\&quot;location\.href='/es/calculators/", r"\\&quot;location.href='/calculators/", content)
            
            if content != original_content:
                with open(file_path, 'w') as f:
                    f.write(content)
                fixes_made += 1
                state_name = os.path.basename(os.path.dirname(file_path))
                print(f"Fixed all Spanish links in: {state_name}/index.html")
    
    print(f"\nTotal fixes made: {fixes_made}")
    return fixes_made

if __name__ == "__main__":
    final_comprehensive_fix()