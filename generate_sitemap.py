import os
from datetime import datetime

today = datetime.now().strftime('%Y-%m-%d')

sitemap_header = '''<?xml version='1.0' encoding='UTF-8'?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
'''

sitemap_footer = '</urlset>'

# Main pages
main_pages = [
    ('/', 1.0, 'daily'),
    ('/blog/', 0.9, 'daily'),
    ('/centers/', 0.9, 'weekly'),
    ('/about.html', 0.6, 'monthly'),
    ('/contact.html', 0.6, 'monthly'),
    ('/faq.html', 0.7, 'monthly'),
    ('/privacy.html', 0.4, 'monthly'),
    ('/terms.html', 0.4, 'monthly'),
]

urls = []

# Add main pages
for path, priority, freq in main_pages:
    urls.append(f'''<url>
    <loc>https://plasmapaycalculator.com{path}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>{freq}</changefreq>
    <priority>{priority}</priority>
</url>''')

# Add all blog posts
blog_dir = 'blog'
for filename in sorted(os.listdir(blog_dir)):
    if filename.endswith('.html') and filename != 'index.html':
        # Higher priority for 2026 content
        priority = 0.8 if '2026' in filename else 0.7
        urls.append(f'''<url>
    <loc>https://plasmapaycalculator.com/blog/{filename}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>{priority}</priority>
</url>''')

# Add centers pages
centers_dir = 'centers'
if os.path.exists(centers_dir):
    for filename in sorted(os.listdir(centers_dir)):
        if filename.endswith('.html'):
            urls.append(f'''<url>
    <loc>https://plasmapaycalculator.com/centers/{filename}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.7</priority>
</url>''')

# Write sitemap
with open('sitemap.xml', 'w') as f:
    f.write(sitemap_header)
    f.write('\n'.join(urls))
    f.write('\n')
    f.write(sitemap_footer)

print(f"Sitemap generated with {len(urls)} URLs")
