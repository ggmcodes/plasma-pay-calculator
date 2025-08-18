#!/usr/bin/env python3

import os
import re
from pathlib import Path

# Get all blog HTML files
blog_dir = Path("/Users/glengomezmeade/Projects/plasma-pay-calculator/blog")
blog_files = sorted([f for f in blog_dir.glob("*.html") if f.name != "index.html"])

print(f"Found {len(blog_files)} blog files")

# Define blog entries with categories and metadata
blog_entries = []

# Read each blog file to extract title and description
for blog_file in blog_files:
    filename = blog_file.name
    slug = filename.replace('.html', '')
    
    # Read file to get title and description
    try:
        with open(blog_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Extract title
        title_match = re.search(r'<title>(.*?)</title>', content)
        title = title_match.group(1) if title_match else slug.replace('-', ' ').title()
        
        # Extract description
        desc_match = re.search(r'<meta name="description" content="(.*?)"', content)
        description = desc_match.group(1) if desc_match else ""
        
        # Determine category based on filename
        category = "general"
        if "csl" in slug or "biolife" in slug or "octapharma" in slug or "grifols" in slug or "kedplasma" in slug or "biomat" in slug:
            category = "centers"
        elif "earning" in slug or "money" in slug or "pay" in slug or "income" in slug or "bonus" in slug:
            category = "earnings"
        elif "health" in slug or "side-effect" in slug or "safe" in slug or "medical" in slug:
            category = "health"
        elif "requirement" in slug or "eligib" in slug or "weight" in slug or "tattoo" in slug:
            category = "requirements"
        elif "tax" in slug or "legal" in slug or "law" in slug or "ssi" in slug or "disability" in slug:
            category = "legal"
        elif "first-time" in slug or "beginner" in slug or "what-to-expect" in slug:
            category = "beginner"
        elif "process" in slug or "step-by-step" in slug:
            category = "process"
        elif "state" in slug or "texas" in slug or "california" in slug or "florida" in slug:
            category = "states"
        
        blog_entries.append({
            'filename': filename,
            'slug': slug,
            'title': title.replace(' | Plasma Pay Calculator', '').replace('2025: ', '').strip(),
            'description': description[:200] if description else "",
            'category': category
        })
        
    except Exception as e:
        print(f"Error processing {filename}: {e}")
        continue

# Group by category
categories = {}
for entry in blog_entries:
    cat = entry['category']
    if cat not in categories:
        categories[cat] = []
    categories[cat].append(entry)

# Category display names and order
category_order = [
    ('beginner', 'Beginner Guides', 'First Time'),
    ('earnings', 'Earnings & Income', 'Earnings'),
    ('centers', 'Center Reviews', 'Centers'),
    ('health', 'Health & Safety', 'Health'),
    ('requirements', 'Requirements & Eligibility', 'Requirements'),
    ('process', 'Process Guides', 'Process'),
    ('legal', 'Legal & Tax', 'Legal'),
    ('states', 'State Guides', 'States'),
    ('general', 'General Guides', 'Guide')
]

# Generate HTML for blog cards
html_output = []

for cat_key, cat_title, badge_text in category_order:
    if cat_key in categories:
        entries = categories[cat_key]
        html_output.append(f"\n<!-- {cat_title} -->")
        
        for entry in entries[:20]:  # Limit to 20 per category for now
            # Choose appropriate image based on category
            if cat_key == 'centers':
                img_url = "https://images.unsplash.com/photo-1586773860418-d37222d8fce3?ixlib=rb-4.0.3&w=800&h=400&fit=crop&q=85&auto=format&fm=webp"
            elif cat_key == 'earnings':
                img_url = "https://images.unsplash.com/photo-1554224155-6726b3ff858f?ixlib=rb-4.0.3&w=800&h=400&fit=crop&q=85&auto=format&fm=webp"
            elif cat_key == 'health':
                img_url = "https://images.unsplash.com/photo-1559757148-5c350d0d3c56?ixlib=rb-4.0.3&w=800&h=400&fit=crop&q=85&auto=format&fm=webp"
            elif cat_key == 'requirements':
                img_url = "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?ixlib=rb-4.0.3&w=800&h=400&fit=crop&q=85&auto=format&fm=webp"
            elif cat_key == 'legal':
                img_url = "https://images.unsplash.com/photo-1450101499163-c8848c66ca85?ixlib=rb-4.0.3&w=800&h=400&fit=crop&q=85&auto=format&fm=webp"
            elif cat_key == 'beginner':
                img_url = "https://images.unsplash.com/photo-1485182708500-e8f1f318ba72?ixlib=rb-4.0.3&w=800&h=400&fit=crop&q=85&auto=format&fm=webp"
            elif cat_key == 'states':
                img_url = "https://images.unsplash.com/photo-1449824913935-59a10b8d2000?ixlib=rb-4.0.3&w=800&h=400&fit=crop&q=85&auto=format&fm=webp"
            else:
                img_url = "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?ixlib=rb-4.0.3&w=800&h=400&fit=crop&q=85&auto=format&fm=webp"
            
            # Clean up title
            title = entry['title']
            if len(title) > 70:
                title = title[:67] + "..."
            
            # Clean up description
            desc = entry['description']
            if len(desc) > 150:
                desc = desc[:147] + "..."
            
            # Generate card HTML
            card_html = f"""<article class="blog-card" data-category="{cat_key}">
<div class="blog-image" style="background-image: url('{img_url}');">
<div class="category-badge">{badge_text}</div>
</div>
<div class="blog-content-area">
<h3 class="blog-title"><a href="/blog/{entry['filename']}">{title}</a></h3>
<p class="blog-excerpt">{desc}</p>
<div class="blog-meta">
<span>{badge_text} Guide</span>
<span class="read-time">8 min read</span>
</div>
</div>
</article>"""
            html_output.append(card_html)

print(f"\nGenerated HTML for {len(html_output)-8} blog cards")  # Subtract comment lines
print("\nHTML output saved to: blog_cards.html")

# Save the generated HTML
with open("/Users/glengomezmeade/Projects/plasma-pay-calculator/blog_cards.html", 'w', encoding='utf-8') as f:
    f.write('\n'.join(html_output))

print("\n✅ Blog cards HTML generated successfully!")
print(f"Total blogs processed: {len(blog_entries)}")
print(f"Categories found: {list(categories.keys())}")
