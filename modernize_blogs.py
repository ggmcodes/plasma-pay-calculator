#!/usr/bin/env python3
"""
Modernize Blog Posts
Converts all blog posts to use the new modern template with:
- Reading time
- Sticky table of contents
- Progress bar
- Clean typography
"""

import os
import re
from pathlib import Path
from html.parser import HTMLParser
from typing import Tuple, List, Dict

BASE_DIR = Path('/Users/glengomezmeade/Projects/plasma-pay-calculator')
BLOG_DIR = BASE_DIR / 'blog'

# Files to skip
SKIP_FILES = {'index.html'}

class HeadingExtractor(HTMLParser):
    """Extract headings from HTML content."""
    def __init__(self):
        super().__init__()
        self.headings = []
        self.current_tag = None
        self.current_text = ''
        self.current_id = None

    def handle_starttag(self, tag, attrs):
        if tag in ('h2', 'h3'):
            self.current_tag = tag
            self.current_text = ''
            attrs_dict = dict(attrs)
            self.current_id = attrs_dict.get('id', '')

    def handle_data(self, data):
        if self.current_tag:
            self.current_text += data

    def handle_endtag(self, tag):
        if tag in ('h2', 'h3') and self.current_tag == tag:
            text = self.current_text.strip()
            # Remove emojis for cleaner TOC
            text_clean = re.sub(r'[^\w\s\-\'\,\.\!\?]', '', text).strip()
            if text_clean:
                # Generate ID if not present
                heading_id = self.current_id or self.generate_id(text_clean)
                self.headings.append({
                    'tag': tag,
                    'text': text_clean[:60] + ('...' if len(text_clean) > 60 else ''),
                    'id': heading_id,
                    'original': text
                })
            self.current_tag = None
            self.current_text = ''

    def generate_id(self, text):
        # Create URL-safe ID
        id_text = text.lower()
        id_text = re.sub(r'[^\w\s-]', '', id_text)
        id_text = re.sub(r'\s+', '-', id_text)
        return id_text[:50]


def count_words(html_content: str) -> int:
    """Count words in HTML content."""
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', ' ', html_content)
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    # Count words
    words = text.split()
    return len(words)


def calculate_reading_time(word_count: int) -> int:
    """Calculate reading time in minutes (200 wpm average)."""
    return max(1, round(word_count / 200))


def extract_title(content: str) -> str:
    """Extract title from the page."""
    match = re.search(r'<title>([^<]+)</title>', content, re.IGNORECASE)
    if match:
        title = match.group(1)
        # Clean up common suffixes
        title = re.sub(r'\s*\|\s*Plasma Pay Calculator.*$', '', title)
        title = re.sub(r'\s*-\s*Plasma Pay Calculator.*$', '', title)
        return title.strip()
    return 'Untitled'


def extract_meta_description(content: str) -> str:
    """Extract meta description."""
    match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\']([^"\']+)["\']', content, re.IGNORECASE)
    if match:
        return match.group(1)
    return ''


def extract_main_content(content: str) -> str:
    """Extract the main article content."""
    # Try to find article or main content
    patterns = [
        r'<article[^>]*>([\s\S]*?)</article>',
        r'<main[^>]*>([\s\S]*?)</main>',
        r'<div[^>]*class="[^"]*content[^"]*"[^>]*>([\s\S]*?)</div>\s*(?=<footer|<script|</body)',
    ]

    for pattern in patterns:
        match = re.search(pattern, content, re.IGNORECASE)
        if match:
            return match.group(1)

    # Fallback: get content between nav and footer
    match = re.search(r'</nav>\s*([\s\S]*?)\s*<footer', content, re.IGNORECASE)
    if match:
        return match.group(1)

    return ''


def add_heading_ids(content: str, headings: List[Dict]) -> str:
    """Add IDs to headings that don't have them."""
    for heading in headings:
        original = heading['original']
        heading_id = heading['id']
        tag = heading['tag']

        # Find the heading without an ID and add one
        pattern = f'<{tag}(?![^>]*id=)[^>]*>\\s*{re.escape(original)}'
        replacement = f'<{tag} id="{heading_id}">{original}'
        content = re.sub(pattern, replacement, content, count=1)

    return content


def generate_toc_html(headings: List[Dict]) -> str:
    """Generate table of contents HTML."""
    if not headings:
        return ''

    toc_items = []
    for h in headings:
        css_class = 'toc-h3' if h['tag'] == 'h3' else ''
        toc_items.append(f'<li><a href="#{h["id"]}" class="{css_class}">{h["text"]}</a></li>')

    return '\n'.join(toc_items)


def create_modern_blog_template(
    title: str,
    description: str,
    main_content: str,
    toc_html: str,
    reading_time: int,
    word_count: int
) -> str:
    """Create the modern blog post template."""

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-053DRWEQLS"></script>
    <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-053DRWEQLS');</script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Plasma Pay Calculator</title>
    <meta name="description" content="{description}">
    <meta name="theme-color" content="#0D4F4F">
    <link rel="icon" type="image/svg+xml" href="/favicon.svg">

    <!-- Open Graph -->
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:type" content="article">

    <!-- Fonts & Theme -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Libre+Baskerville:wght@400;700&family=Outfit:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/css/theme.css">
    <link rel="stylesheet" href="/css/blog.css">
</head>
<body>
    <!-- Reading Progress Bar -->
    <div class="reading-progress" id="readingProgress"></div>

    <!-- Navigation -->
    <nav class="nav" id="mainNav">
        <div class="nav-inner">
            <a href="/" class="logo">
                <span class="logo-mark">$</span>
                Plasma Pay
            </a>
            <ul class="nav-links">
                <li><a href="/">Calculator</a></li>
                <li><a href="/centers/">Find Centers</a></li>
                <li><a href="/blog/">Blog</a></li>
                <li><a href="/faq.html">FAQ</a></li>
                <li><a href="/centers/" class="nav-cta">Find Centers Near Me</a></li>
            </ul>
            <button class="mobile-toggle" onclick="toggleMobileMenu()" aria-label="Toggle menu">
                <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M3 12h18M3 6h18M3 18h18"/>
                </svg>
            </button>
        </div>
    </nav>

    <!-- Blog Header -->
    <header class="blog-header">
        <div class="blog-header-inner">
            <span class="blog-category">Guide</span>
            <h1>{title}</h1>
            <div class="blog-meta">
                <div class="blog-meta-item">
                    <svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                        <circle cx="12" cy="12" r="10"/>
                        <path d="M12 6v6l4 2"/>
                    </svg>
                    <span class="reading-time">{reading_time} min read</span>
                </div>
                <div class="blog-meta-item">
                    <svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                        <path d="M12 20h9M16.5 3.5a2.12 2.12 0 013 3L7 19l-4 1 1-4L16.5 3.5z"/>
                    </svg>
                    <span>{word_count:,} words</span>
                </div>
                <div class="blog-meta-item">
                    <svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                        <rect x="3" y="4" width="18" height="18" rx="2" ry="2"/>
                        <line x1="16" y1="2" x2="16" y2="6"/>
                        <line x1="8" y1="2" x2="8" y2="6"/>
                        <line x1="3" y1="10" x2="21" y2="10"/>
                    </svg>
                    <span>Updated 2025</span>
                </div>
            </div>
        </div>
    </header>

    <!-- Blog Layout -->
    <div class="blog-layout">
        <!-- Table of Contents Sidebar -->
        <aside class="toc-sidebar">
            <button class="toc-mobile-toggle" onclick="this.classList.toggle('active')">
                Table of Contents
                <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                    <path d="M6 9l6 6 6-6"/>
                </svg>
            </button>
            <div class="toc-container">
                <div class="toc-title">On This Page</div>
                <ul class="toc-list">
                    {toc_html}
                </ul>
            </div>
        </aside>

        <!-- Main Content -->
        <article class="blog-content">
            {main_content}

            <!-- Share Section -->
            <div class="share-section">
                <div class="share-title">Share this guide</div>
                <div class="share-buttons">
                    <a href="#" class="share-btn" onclick="shareOnTwitter()" title="Share on Twitter">
                        <svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
                    </a>
                    <a href="#" class="share-btn" onclick="shareOnFacebook()" title="Share on Facebook">
                        <svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
                    </a>
                    <a href="#" class="share-btn" onclick="copyLink()" title="Copy link">
                        <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M10 13a5 5 0 007.54.54l3-3a5 5 0 00-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 00-7.54-.54l-3 3a5 5 0 007.07 7.07l1.71-1.71"/></svg>
                    </a>
                </div>
            </div>

            <!-- Author Box -->
            <div class="author-box">
                <div class="author-avatar">PP</div>
                <div class="author-info">
                    <h4>Plasma Pay Calculator Team</h4>
                    <p>Helping donors maximize their plasma donation earnings since 2023.</p>
                </div>
            </div>
        </article>
    </div>

    <!-- Footer -->
    <footer class="footer">
        <div class="footer-grid">
            <div class="footer-brand">
                <a href="/" class="logo">
                    <span class="logo-mark">$</span>
                    Plasma Pay
                </a>
                <p>Helping thousands of donors maximize their plasma donation earnings since 2023.</p>
            </div>
            <div class="footer-section">
                <h4>Calculators</h4>
                <ul>
                    <li><a href="/">Plasma Pay Calculator</a></li>
                    <li><a href="/biolife-plasma-pay-chart.html">BioLife Pay Chart</a></li>
                    <li><a href="/csl-plasma-pay-chart.html">CSL Pay Chart</a></li>
                </ul>
            </div>
            <div class="footer-section">
                <h4>Resources</h4>
                <ul>
                    <li><a href="/centers/">Find Centers</a></li>
                    <li><a href="/blog/">Blog</a></li>
                    <li><a href="/faq.html">FAQ</a></li>
                </ul>
            </div>
            <div class="footer-section">
                <h4>Company</h4>
                <ul>
                    <li><a href="/about.html">About Us</a></li>
                    <li><a href="/advertise.html">Advertise</a></li>
                    <li><a href="/privacy.html">Privacy</a></li>
                </ul>
            </div>
        </div>
        <div class="advertise-banner">
            <p>Are you a plasma center looking to reach new donors?</p>
            <a href="/advertise.html">Advertise With Us</a>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2024 PlasmaPayCalculator.com. All rights reserved.</p>
            <div class="footer-legal">
                <a href="/privacy.html">Privacy</a>
                <a href="/terms.html">Terms</a>
            </div>
        </div>
    </footer>

    <script>
    // Nav scroll effect
    window.addEventListener('scroll', () => {{
        const nav = document.getElementById('mainNav');
        if (window.scrollY > 50) {{
            nav.classList.add('scrolled');
        }} else {{
            nav.classList.remove('scrolled');
        }}

        // Reading progress
        const article = document.querySelector('.blog-content');
        if (article) {{
            const articleTop = article.offsetTop;
            const articleHeight = article.offsetHeight;
            const windowHeight = window.innerHeight;
            const scrolled = window.scrollY - articleTop + windowHeight / 2;
            const progress = Math.min(100, Math.max(0, (scrolled / articleHeight) * 100));
            document.getElementById('readingProgress').style.width = progress + '%';
        }}
    }});

    // Mobile menu toggle
    function toggleMobileMenu() {{
        const navLinks = document.querySelector('.nav-links');
        navLinks.classList.toggle('active');
    }}

    // TOC active state
    const tocLinks = document.querySelectorAll('.toc-list a');
    const headings = document.querySelectorAll('.blog-content h2, .blog-content h3');

    window.addEventListener('scroll', () => {{
        let current = '';
        headings.forEach(heading => {{
            const sectionTop = heading.offsetTop;
            if (window.scrollY >= sectionTop - 120) {{
                current = heading.getAttribute('id');
            }}
        }});

        tocLinks.forEach(link => {{
            link.classList.remove('active');
            if (link.getAttribute('href') === '#' + current) {{
                link.classList.add('active');
            }}
        }});
    }});

    // Share functions
    function shareOnTwitter() {{
        window.open('https://twitter.com/intent/tweet?url=' + encodeURIComponent(window.location.href) + '&text=' + encodeURIComponent(document.title), '_blank');
    }}

    function shareOnFacebook() {{
        window.open('https://www.facebook.com/sharer/sharer.php?u=' + encodeURIComponent(window.location.href), '_blank');
    }}

    function copyLink() {{
        navigator.clipboard.writeText(window.location.href);
        alert('Link copied to clipboard!');
    }}
    </script>
</body>
</html>'''


def process_blog_file(filepath: str, dry_run: bool = False) -> Tuple[bool, str]:
    """Process a single blog file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Skip if already modernized
        if 'blog.css' in content:
            return False, 'Already modernized'

        # Extract info
        title = extract_title(content)
        description = extract_meta_description(content)
        main_content = extract_main_content(content)

        if not main_content:
            return False, 'Could not extract main content'

        # Extract headings
        parser = HeadingExtractor()
        parser.feed(main_content)
        headings = parser.headings

        # Add IDs to headings
        main_content = add_heading_ids(main_content, headings)

        # Calculate reading time
        word_count = count_words(main_content)
        reading_time = calculate_reading_time(word_count)

        # Generate TOC
        toc_html = generate_toc_html(headings)

        # Create new template
        new_content = create_modern_blog_template(
            title=title,
            description=description[:160] if description else title,
            main_content=main_content,
            toc_html=toc_html,
            reading_time=reading_time,
            word_count=word_count
        )

        if not dry_run:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)

        return True, f'{reading_time} min read, {len(headings)} headings'

    except Exception as e:
        return False, f'Error: {str(e)}'


def main(dry_run: bool = False):
    """Main function."""
    print("=" * 60)
    print("MODERNIZE BLOG POSTS")
    print("=" * 60)
    print(f"Mode: {'DRY RUN' if dry_run else 'LIVE'}")
    print()

    # Find all blog HTML files
    blog_files = []
    for root, dirs, files in os.walk(BLOG_DIR):
        for file in files:
            if file.endswith('.html') and file not in SKIP_FILES:
                blog_files.append(os.path.join(root, file))

    print(f"Found {len(blog_files)} blog files")
    print()

    stats = {'updated': 0, 'skipped': 0, 'errors': 0}

    for filepath in sorted(blog_files):
        rel_path = os.path.relpath(filepath, BASE_DIR)
        success, message = process_blog_file(filepath, dry_run)

        if success:
            stats['updated'] += 1
            print(f"  [OK] {rel_path}: {message}")
        elif 'Error' in message:
            stats['errors'] += 1
            print(f"  [ERR] {rel_path}: {message}")
        else:
            stats['skipped'] += 1

    print()
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"  Updated: {stats['updated']}")
    print(f"  Skipped: {stats['skipped']}")
    print(f"  Errors:  {stats['errors']}")

    if dry_run:
        print("\nThis was a DRY RUN. Run with --live to apply changes.")


if __name__ == '__main__':
    import sys
    dry_run = '--live' not in sys.argv
    main(dry_run=dry_run)
