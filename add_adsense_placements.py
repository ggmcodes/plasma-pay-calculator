#!/usr/bin/env python3
"""
Add strategic AdSense placements to all pages
Maximizes revenue while maintaining good UX
"""

import os
import re
from pathlib import Path

BASE_DIR = Path('/Users/glengomezmeade/Projects/plasma-pay-calculator')
PUB_ID = 'ca-pub-3180649272238451'

# Ad unit templates
AD_UNITS = {
    'header_leaderboard': f'''
<!-- AdSense Header Leaderboard -->
<div class="ad-container ad-header" style="text-align: center; margin: 1rem 0; min-height: 90px;">
    <ins class="adsbygoogle"
         style="display:block"
         data-ad-client="{PUB_ID}"
         data-ad-slot="auto"
         data-ad-format="horizontal"
         data-full-width-responsive="true"></ins>
    <script>(adsbygoogle = window.adsbygoogle || []).push({{}});</script>
</div>
''',
    'in_article': f'''
<!-- AdSense In-Article -->
<div class="ad-container ad-in-article" style="text-align: center; margin: 2rem 0; min-height: 250px;">
    <ins class="adsbygoogle"
         style="display:block; text-align:center;"
         data-ad-layout="in-article"
         data-ad-format="fluid"
         data-ad-client="{PUB_ID}"
         data-ad-slot="auto"></ins>
    <script>(adsbygoogle = window.adsbygoogle || []).push({{}});</script>
</div>
''',
    'sidebar_rectangle': f'''
<!-- AdSense Sidebar Rectangle -->
<div class="ad-container ad-sidebar" style="text-align: center; margin: 1rem 0; min-height: 250px;">
    <ins class="adsbygoogle"
         style="display:inline-block;width:300px;height:250px"
         data-ad-client="{PUB_ID}"
         data-ad-slot="auto"></ins>
    <script>(adsbygoogle = window.adsbygoogle || []).push({{}});</script>
</div>
''',
    'footer_leaderboard': f'''
<!-- AdSense Footer Leaderboard -->
<div class="ad-container ad-footer" style="text-align: center; margin: 2rem 0; min-height: 90px;">
    <ins class="adsbygoogle"
         style="display:block"
         data-ad-client="{PUB_ID}"
         data-ad-slot="auto"
         data-ad-format="horizontal"
         data-full-width-responsive="true"></ins>
    <script>(adsbygoogle = window.adsbygoogle || []).push({{}});</script>
</div>
''',
    'multiplex': f'''
<!-- AdSense Multiplex (Related Content Style) -->
<div class="ad-container ad-multiplex" style="margin: 2rem 0;">
    <ins class="adsbygoogle"
         style="display:block"
         data-ad-format="autorelaxed"
         data-ad-client="{PUB_ID}"
         data-ad-slot="auto"></ins>
    <script>(adsbygoogle = window.adsbygoogle || []).push({{}});</script>
</div>
'''
}

# CSS for ad containers
AD_CSS = '''
/* AdSense Container Styles */
.ad-container {
    background: var(--cream, #FAF8F5);
    border-radius: 8px;
    padding: 0.5rem;
    overflow: hidden;
}

.ad-container::before {
    content: 'Advertisement';
    display: block;
    text-align: center;
    font-size: 0.7rem;
    color: var(--gray, #6B7280);
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-bottom: 0.25rem;
}

@media (max-width: 768px) {
    .ad-header, .ad-footer {
        min-height: 50px;
    }
    .ad-sidebar {
        min-height: 100px;
    }
}
'''

stats = {'processed': 0, 'modified': 0, 'skipped': 0, 'errors': 0}

def has_ads(html):
    """Check if page already has ad placements"""
    return 'adsbygoogle' in html and html.count('adsbygoogle') >= 2

def is_blog_post(file_path):
    """Check if file is a blog post"""
    return '/blog/' in str(file_path) and file_path.name != 'index.html'

def is_calculator_page(file_path):
    """Check if file is a calculator page"""
    return '/calculators/' in str(file_path) or 'calculator' in file_path.name.lower()

def is_content_page(file_path):
    """Check if file is a content/guide page"""
    return file_path.suffix == '.html' and not is_blog_post(file_path) and not is_calculator_page(file_path)

def add_ads_to_blog(html):
    """Add ads to blog posts: header, mid-content, footer"""

    # Add header ad after blog header/hero
    if '<section class="blog-header"' in html or '<header' in html:
        # Insert after the first major section
        html = re.sub(
            r'(</section>\s*<main|</header>\s*<main)',
            AD_UNITS['header_leaderboard'] + r'\1',
            html,
            count=1
        )

    # Add in-article ad after first major heading (h2)
    h2_matches = list(re.finditer(r'</h2>', html))
    if len(h2_matches) >= 2:
        # Insert after second h2
        pos = h2_matches[1].end()
        html = html[:pos] + AD_UNITS['in_article'] + html[pos:]
    elif len(h2_matches) == 1:
        pos = h2_matches[0].end()
        html = html[:pos] + AD_UNITS['in_article'] + html[pos:]

    # Add multiplex ad before footer
    if '<footer' in html:
        html = html.replace('<footer', AD_UNITS['multiplex'] + '<footer', 1)

    return html

def add_ads_to_calculator(html):
    """Add ads to calculator pages: above calc, below results"""

    # Add ad before calculator form
    if 'id="calculator"' in html or 'class="calculator' in html:
        html = re.sub(
            r'(<div[^>]*(?:id="calculator"|class="calculator)[^>]*>)',
            AD_UNITS['header_leaderboard'] + r'\1',
            html,
            count=1
        )

    # Add ad after results section
    if 'id="results"' in html or 'class="results' in html:
        html = re.sub(
            r'(</div>\s*)(<!--\s*(?:End\s+)?Results|<section|<div class="(?:cta|related))',
            r'\1' + AD_UNITS['in_article'] + r'\2',
            html,
            count=1
        )

    # Add footer ad
    if '<footer' in html:
        html = html.replace('<footer', AD_UNITS['footer_leaderboard'] + '<footer', 1)

    return html

def add_ads_to_content(html):
    """Add ads to general content pages"""

    # Add header ad after first section/hero
    html = re.sub(
        r'(</section>\s*)(<main|<section|<div class="content)',
        r'\1' + AD_UNITS['header_leaderboard'] + r'\2',
        html,
        count=1
    )

    # Add mid-content ad
    h2_matches = list(re.finditer(r'</h2>', html))
    if h2_matches:
        mid_point = len(h2_matches) // 2
        if mid_point > 0:
            pos = h2_matches[mid_point].end()
            html = html[:pos] + AD_UNITS['in_article'] + html[pos:]

    # Add footer ad
    if '<footer' in html:
        html = html.replace('<footer', AD_UNITS['footer_leaderboard'] + '<footer', 1)

    return html

def add_ad_css(html):
    """Add ad container CSS to head"""
    if '.ad-container' not in html:
        css_tag = f'<style>{AD_CSS}</style>'
        html = html.replace('</head>', css_tag + '</head>')
    return html

def process_file(file_path):
    """Process a single HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            html = f.read()

        # Skip if already has sufficient ads
        if has_ads(html):
            stats['skipped'] += 1
            return False

        original = html

        # Determine page type and add appropriate ads
        if is_blog_post(file_path):
            html = add_ads_to_blog(html)
        elif is_calculator_page(file_path):
            html = add_ads_to_calculator(html)
        else:
            html = add_ads_to_content(html)

        # Add CSS
        html = add_ad_css(html)

        if html != original:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(html)
            stats['modified'] += 1
            return True

        stats['skipped'] += 1
        return False

    except Exception as e:
        print(f"  ERROR: {file_path}: {e}")
        stats['errors'] += 1
        return False

def main():
    print("=" * 60)
    print("ADSENSE PLACEMENT INJECTION")
    print("=" * 60)

    # Get all HTML files
    all_files = list(BASE_DIR.glob('**/*.html'))
    all_files = [f for f in all_files if 'node_modules' not in str(f) and '.git' not in str(f) and 'includes' not in str(f)]

    print(f"\nProcessing {len(all_files)} HTML files...")

    for file_path in all_files:
        stats['processed'] += 1
        if process_file(file_path):
            print(f"  Added ads: {file_path.relative_to(BASE_DIR)}")

    print("\n" + "=" * 60)
    print("ADSENSE INJECTION COMPLETE")
    print("=" * 60)
    print(f"Total processed: {stats['processed']}")
    print(f"Files with ads added: {stats['modified']}")
    print(f"Files skipped (already has ads): {stats['skipped']}")
    print(f"Errors: {stats['errors']}")
    print("=" * 60)

if __name__ == '__main__':
    main()
