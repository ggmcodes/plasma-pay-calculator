#!/usr/bin/env python3
"""
Enhance internal linking across all pages for better SEO and user navigation
"""

import os
import re
from pathlib import Path

# Key linking opportunities
LINK_OPPORTUNITIES = {
    # Calculator-related keywords -> calculator page
    'plasma pay calculator': '/calculator/',
    'plasma calculator': '/calculator/',
    'donation calculator': '/calculator/',
    'earnings calculator': '/calculator/',
    
    # State-specific linking
    'california plasma': '/calculators/california/',
    'texas plasma': '/calculators/texas/',
    'florida plasma': '/calculators/florida/',
    'new york plasma': '/calculators/new-york/',
    
    # Centers-related keywords -> centers page
    'find plasma centers': '/centers/',
    'plasma centers near me': '/centers/',
    'nearest plasma center': '/centers/',
    'plasma center locations': '/centers/',
    
    # Company-specific links
    'csl plasma': '/centers/csl-plasma/',
    'biolife plasma': '/centers/biolife/',
    'octapharma plasma': '/centers/octapharma/',
    'grifols plasma': '/centers/grifols/',
    
    # FAQ linking
    'frequently asked questions': '/faq.html',
    'plasma donation faq': '/faq.html',
    'common questions': '/faq.html',
    
    # Health/eligibility linking
    'eligibility requirements': '/health/',
    'plasma donation requirements': '/health/',
    'who can donate plasma': '/health/',
    'health requirements': '/health/',
    
    # Blog category linking
    'plasma donation tips': '/blog/',
    'plasma donation guide': '/blog/',
    'donation process': '/blog/plasma-donation-process-step-by-step.html',
    'first time donor': '/blog/first-time-plasma-donation-what-to-expect.html',
    'side effects': '/blog/plasma-donation-side-effects.html',
    'tax information': '/blog/plasma-donation-tax-guide-2025.html',
}

# Pages to exclude from linking (to avoid circular references)
EXCLUDE_PATTERNS = [
    '/sitemap.xml',
    '/robots.txt',
    '.js',
    '.css',
    '.json',
    '.py',
    '.md',
    'backup',
    'migrate_'
]

def should_exclude_file(file_path):
    """Check if file should be excluded from linking"""
    return any(pattern in file_path for pattern in EXCLUDE_PATTERNS)

def add_internal_links(content, file_path):
    """Add strategic internal links to content"""
    if should_exclude_file(file_path):
        return content, 0
    
    links_added = 0
    rel_path = os.path.relpath(file_path, "/Users/glengomezmeade/Projects/plasma-pay-calculator")
    
    # Skip if this is the target page to avoid circular links
    for keyword, target_url in LINK_OPPORTUNITIES.items():
        # Skip if we're on the target page
        if target_url.strip('/') in rel_path:
            continue
            
        # Look for the keyword that's not already linked
        pattern = rf'(?<!<a[^>]*>)(?<!href=")({re.escape(keyword)})(?![^<]*</a>)'
        
        def replace_with_link(match):
            nonlocal links_added
            text = match.group(1)
            # Only link the first occurrence to avoid over-optimization
            if links_added < 3:  # Limit to 3 links per page
                links_added += 1
                return f'<a href="{target_url}" class="text-green-600 hover:text-green-800 underline">{text}</a>'
            return text
        
        # Replace only the first occurrence
        content = re.sub(pattern, replace_with_link, content, count=1, flags=re.IGNORECASE)
    
    return content, links_added

def enhance_file_linking(file_path):
    """Enhance internal linking for a single file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        enhanced_content, links_added = add_internal_links(content, file_path)
        
        # Only write if changes were made
        if enhanced_content != original_content and links_added > 0:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(enhanced_content)
            return links_added
        
        return 0
        
    except Exception as e:
        print(f"❌ Error processing {file_path}: {str(e)}")
        return 0

def find_html_files():
    """Find all HTML files to enhance"""
    base_dir = "/Users/glengomezmeade/Projects/plasma-pay-calculator"
    html_files = []
    
    for root, dirs, files in os.walk(base_dir):
        # Skip certain directories
        if any(skip_dir in root for skip_dir in ['.git', 'node_modules', '__pycache__']):
            continue
            
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                if not should_exclude_file(file_path):
                    html_files.append(file_path)
    
    return html_files

def add_contextual_blog_links():
    """Add contextual links between related blog posts"""
    blog_dir = "/Users/glengomezmeade/Projects/plasma-pay-calculator/blog"
    
    # Related post mappings
    related_posts = {
        'first-time-plasma-donation-what-to-expect.html': [
            'plasma-donation-tips-beginners.html',
            'plasma-donation-process-step-by-step.html',
            'how-to-prepare-for-plasma-donation.html'
        ],
        'csl-plasma-pay-rates-2025.html': [
            'biolife-vs-csl-plasma-comparison.html',
            'highest-paying-plasma-centers-near-me.html',
            'which-plasma-center-pays-most-money.html'
        ],
        'plasma-donation-side-effects.html': [
            'plasma-donation-health-screening-guide.html',
            'complete-medical-eligibility-guide-plasma-donation.html',
            'how-to-prepare-for-plasma-donation.html'
        ],
        'plasma-donation-tax-guide-2025.html': [
            'how-much-money-can-you-make-donating-plasma-2025.html',
            'is-plasma-donation-worth-it-financial-analysis.html',
            'plasma-donation-side-hustle-complete-guide.html'
        ]
    }
    
    links_added = 0
    
    for post, related in related_posts.items():
        post_path = os.path.join(blog_dir, post)
        if os.path.exists(post_path):
            try:
                with open(post_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Add related posts section before closing body tag
                related_links_html = '''
                <div class="bg-gray-50 p-6 rounded-lg mt-8">
                    <h3 class="text-xl font-bold text-gray-900 mb-4">Related Articles</h3>
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                '''
                
                for related_post in related[:3]:  # Limit to 3 related posts
                    title = related_post.replace('-', ' ').replace('.html', '').title()
                    related_links_html += f'''
                        <a href="/blog/{related_post}" class="block p-4 bg-white rounded-lg shadow hover:shadow-md transition-shadow">
                            <h4 class="font-semibold text-green-600 hover:text-green-800">{title}</h4>
                        </a>
                    '''
                
                related_links_html += '''
                    </div>
                </div>
                '''
                
                # Insert before closing body tag
                if '</body>' in content and 'Related Articles' not in content:
                    content = content.replace('</body>', related_links_html + '</body>')
                    
                    with open(post_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    links_added += len(related[:3])
                    print(f"✅ Added related links to {post}")
                
            except Exception as e:
                print(f"❌ Error adding related links to {post}: {str(e)}")
    
    return links_added

def main():
    """Main function"""
    print("🚀 Starting internal linking enhancement...")
    
    # Find all HTML files
    html_files = find_html_files()
    print(f"📊 Found {len(html_files)} HTML files to enhance")
    
    total_links_added = 0
    files_enhanced = 0
    
    # Enhance individual files
    for file_path in html_files:
        rel_path = os.path.relpath(file_path, "/Users/glengomezmeade/Projects/plasma-pay-calculator")
        links_added = enhance_file_linking(file_path)
        
        if links_added > 0:
            print(f"✅ Enhanced {rel_path} (+{links_added} links)")
            files_enhanced += 1
            total_links_added += links_added
        # else:
        #     print(f"⚪ No enhancements needed: {rel_path}")
    
    print(f"\n🔗 Adding contextual blog post links...")
    blog_links_added = add_contextual_blog_links()
    total_links_added += blog_links_added
    
    print(f"\n🎉 Internal linking enhancement complete!")
    print(f"📊 Files enhanced: {files_enhanced}")
    print(f"🔗 Total internal links added: {total_links_added}")
    print(f"📈 This will improve site navigation and SEO performance")

if __name__ == "__main__":
    main()