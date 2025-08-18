#!/usr/bin/env python3

import os
import re
from pathlib import Path

def add_contextual_links():
    blog_dir = Path("/Users/glengomezmeade/Projects/plasma-pay-calculator/blog")
    blog_files = list(blog_dir.glob("*.html"))
    
    # Also process subdirectory index files
    for subdir in blog_dir.iterdir():
        if subdir.is_dir() and subdir.name != "." and subdir.name != "..":
            index_file = subdir / "index.html"
            if index_file.exists():
                blog_files.append(index_file)
    
    print(f"Processing {len(blog_files)} HTML files for contextual linking...")
    
    files_enhanced = 0
    links_added = 0
    
    # Define contextual link patterns
    link_patterns = [
        # Centers
        (r'\b(CSL Plasma|CSL plasma)\b(?![^<]*>)(?![^<]*</a>)', 
         '<a href="/blog/csl-plasma-pay-rates-2025.html" class="text-blue-600 hover:text-blue-800">\\1</a>'),
        (r'\b(BioLife|Biolife)\b(?![^<]*>)(?![^<]*</a>)', 
         '<a href="/blog/biolife-plasma-pay-chart-2025.html" class="text-blue-600 hover:text-blue-800">\\1</a>'),
        (r'\b(Grifols|grifols)\b(?![^<]*>)(?![^<]*</a>)', 
         '<a href="/blog/grifols-plasma-pay-calculator-2025.html" class="text-blue-600 hover:text-blue-800">\\1</a>'),
        (r'\b(KedPlasma|Kedplasma)\b(?![^<]*>)(?![^<]*</a>)', 
         '<a href="/blog/kedplasma-pay-chart-2025.html" class="text-blue-600 hover:text-blue-800">\\1</a>'),
        (r'\b(Octapharma)\b(?![^<]*>)(?![^<]*</a>)', 
         '<a href="/blog/octapharma-vs-competitors-payment-calculator.html" class="text-blue-600 hover:text-blue-800">\\1</a>'),
        
        # Key phrases
        (r'\b(first.time donor|new donor bonus|first donation)\b(?![^<]*>)(?![^<]*</a>)', 
         '<a href="/blog/first-time-plasma-donation.html" class="text-blue-600 hover:text-blue-800">\\1</a>'),
        (r'\b(maximize.*earnings|earn more money)\b(?![^<]*>)(?![^<]*</a>)', 
         '<a href="/blog/maximize-plasma-donation-earnings-2025.html" class="text-blue-600 hover:text-blue-800">\\1</a>'),
        (r'\b(side effects|donation safety)\b(?![^<]*>)(?![^<]*</a>)', 
         '<a href="/blog/plasma-donation-side-effects-safety-2025.html" class="text-blue-600 hover:text-blue-800">\\1</a>'),
        (r'\b(weight requirements)\b(?![^<]*>)(?![^<]*</a>)', 
         '<a href="/blog/plasma-donation-weight-requirements.html" class="text-blue-600 hover:text-blue-800">\\1</a>'),
        (r'\b(tax.*plasma|plasma.*tax|1099)\b(?![^<]*>)(?![^<]*</a>)', 
         '<a href="/blog/plasma-donation-tax-guide-2025.html" class="text-blue-600 hover:text-blue-800">\\1</a>'),
        (r'\b(highest.paying centers|best.paying plasma)\b(?![^<]*>)(?![^<]*</a>)', 
         '<a href="/blog/which-plasma-center-pays-most-money.html" class="text-blue-600 hover:text-blue-800">\\1</a>'),
    ]
    
    for blog_file in blog_files:
        try:
            with open(blog_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Skip if this is already heavily linked
            if content.count('class="text-blue-600 hover:text-blue-800"') > 20:
                continue
            
            # Only process article content, not navigation or headers
            article_match = re.search(r'(<article.*?>.*?</article>)', content, re.DOTALL)
            if article_match:
                article_content = article_match.group(1)
                original_article = article_content
                
                # Apply contextual links (limit to first 3 occurrences of each pattern)
                for pattern, replacement in link_patterns:
                    # Only link first 3 occurrences
                    count = 0
                    def replace_limited(match):
                        nonlocal count
                        if count < 3:
                            count += 1
                            return replacement.replace('\\1', match.group(1))
                        return match.group(0)
                    
                    article_content = re.sub(pattern, replace_limited, article_content, flags=re.IGNORECASE)
                
                # Replace article content if changed
                if article_content != original_article:
                    content = content.replace(original_article, article_content)
                    links_added += article_content.count('href=') - original_article.count('href=')
            
            # Add breadcrumb navigation if not present
            if '<nav class="breadcrumb"' not in content and '<main' in content:
                breadcrumb = '''    <!-- Breadcrumb -->
    <nav class="breadcrumb mb-6" aria-label="Breadcrumb">
        <ol class="flex items-center space-x-2 text-sm text-gray-600">
            <li><a href="/" class="hover:text-plasma-green">Home</a></li>
            <li><span class="mx-2">/</span></li>
            <li><a href="/blog/" class="hover:text-plasma-green">Blog</a></li>
            <li><span class="mx-2">/</span></li>
            <li class="text-gray-900 font-medium">Current Article</li>
        </ol>
    </nav>
'''
                content = re.sub(r'(<main[^>]*>)', r'\1\n' + breadcrumb, content, count=1)
            
            # Add "Back to Blog" button if not present
            if 'Back to Blog' not in content and '</article>' in content:
                back_button = '''
    <!-- Back to Blog -->
    <div class="mt-8 text-center">
        <a href="/blog/" class="inline-flex items-center px-4 py-2 border border-gray-300 rounded-md text-sm font-medium text-gray-700 bg-white hover:bg-gray-50">
            ← Back to All Articles
        </a>
    </div>
'''
                content = content.replace('</article>', '</article>\n' + back_button)
            
            # Save if modified
            if content != original_content:
                with open(blog_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                files_enhanced += 1
                print(f"✅ Enhanced: {blog_file.name}")
                
        except Exception as e:
            print(f"❌ Error processing {blog_file}: {e}")
    
    print(f"\n=== INTERNAL LINKING SUMMARY ===")
    print(f"Files enhanced: {files_enhanced}")
    print(f"Contextual links added: {links_added}")

if __name__ == "__main__":
    add_contextual_links()