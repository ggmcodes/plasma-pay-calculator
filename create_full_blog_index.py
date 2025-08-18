#!/usr/bin/env python3

import os
import re
from pathlib import Path

# Get all blog HTML files
blog_dir = Path("/Users/glengomezmeade/Projects/plasma-pay-calculator/blog")
blog_files = sorted([f for f in blog_dir.glob("*.html") if f.name != "index.html"])

print(f"Found {len(blog_files)} blog files")

# Read the current index.html
with open(blog_dir / "index.html", 'r', encoding='utf-8') as f:
    index_content = f.read()

# Find the blog grid section
grid_start = index_content.find('<div class="blog-grid" id="blogGrid">')
grid_end = index_content.find('</div>\n<div class="no-results"')

if grid_start == -1 or grid_end == -1:
    print("Error: Could not find blog grid section")
    exit(1)

# Extract before and after content
before_grid = index_content[:grid_start + len('<div class="blog-grid" id="blogGrid">')]
after_grid = index_content[grid_end:]

# Define blog entries with categories and metadata
blog_entries = []

# Read each blog file to extract title and description
for blog_file in blog_files:
    filename = blog_file.name
    slug = filename.replace('.html', '')
    
    # Read file to get title and description
    try:
        with open(blog_file, 'r', encoding='utf-8') as f:
            content = f.read()[:5000]  # Read first 5000 chars for performance
            
        # Extract title
        title_match = re.search(r'<title>(.*?)</title>', content)
        title = title_match.group(1) if title_match else slug.replace('-', ' ').title()
        
        # Clean up title
        title = title.replace(' | Plasma Pay Calculator', '').replace(' - Plasma Pay Calculator', '')
        title = re.sub(r'^\d{4}:\s*', '', title)  # Remove year prefix
        
        # Extract description
        desc_match = re.search(r'<meta name="description" content="(.*?)"', content)
        description = desc_match.group(1) if desc_match else ""
        
        # Determine category based on filename and content
        category = []
        slug_lower = slug.lower()
        
        # Multiple categories can apply
        if any(x in slug_lower for x in ["csl", "biolife", "octapharma", "grifols", "kedplasma", "biomat"]):
            category.append("centers")
        if any(x in slug_lower for x in ["earning", "money", "pay", "income", "bonus", "maximize"]):
            category.append("earnings")
        if any(x in slug_lower for x in ["health", "side-effect", "safe", "medical", "prepare"]):
            category.append("health")
        if any(x in slug_lower for x in ["requirement", "eligib", "weight", "tattoo", "age"]):
            category.append("requirements")
        if any(x in slug_lower for x in ["tax", "legal", "law", "ssi", "disability"]):
            category.append("legal")
        if any(x in slug_lower for x in ["first-time", "beginner", "what-to-expect", "new-donor"]):
            category.append("beginner")
        if any(x in slug_lower for x in ["process", "step-by-step"]):
            category.append("process")
        if any(x in slug_lower for x in ["texas", "california", "florida", "state"]):
            category.append("states")
        
        if not category:
            category = ["general"]
        
        blog_entries.append({
            'filename': filename,
            'slug': slug,
            'title': title.strip(),
            'description': description,
            'categories': category
        })
        
    except Exception as e:
        print(f"Error processing {filename}: {e}")
        continue

print(f"Processed {len(blog_entries)} blog entries")

# Group by primary category for organization
def get_primary_category(entry):
    cats = entry['categories']
    # Priority order
    priority = ['beginner', 'earnings', 'centers', 'health', 'requirements', 'process', 'legal', 'states', 'general']
    for p in priority:
        if p in cats:
            return p
    return cats[0] if cats else 'general'

# Organize by category
categories = {}
for entry in blog_entries:
    primary_cat = get_primary_category(entry)
    if primary_cat not in categories:
        categories[primary_cat] = []
    categories[primary_cat].append(entry)

# Category display info
category_info = {
    'beginner': ('Beginner Guides', 'First Time', 'https://images.unsplash.com/photo-1485182708500-e8f1f318ba72?ixlib=rb-4.0.3&w=800&h=400&fit=crop&q=85&auto=format&fm=webp'),
    'earnings': ('Earnings & Income', 'Earnings', 'https://images.unsplash.com/photo-1554224155-6726b3ff858f?ixlib=rb-4.0.3&w=800&h=400&fit=crop&q=85&auto=format&fm=webp'),
    'centers': ('Center Reviews', 'Centers', 'https://images.unsplash.com/photo-1586773860418-d37222d8fce3?ixlib=rb-4.0.3&w=800&h=400&fit=crop&q=85&auto=format&fm=webp'),
    'health': ('Health & Safety', 'Health', 'https://images.unsplash.com/photo-1559757148-5c350d0d3c56?ixlib=rb-4.0.3&w=800&h=400&fit=crop&q=85&auto=format&fm=webp'),
    'requirements': ('Requirements', 'Requirements', 'https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?ixlib=rb-4.0.3&w=800&h=400&fit=crop&q=85&auto=format&fm=webp'),
    'process': ('Process Guides', 'Process', 'https://images.unsplash.com/photo-1551601651-2a8555f1a136?ixlib=rb-4.0.3&w=800&h=400&fit=crop&q=85&auto=format&fm=webp'),
    'legal': ('Legal & Tax', 'Legal', 'https://images.unsplash.com/photo-1450101499163-c8848c66ca85?ixlib=rb-4.0.3&w=800&h=400&fit=crop&q=85&auto=format&fm=webp'),
    'states': ('State Guides', 'States', 'https://images.unsplash.com/photo-1449824913935-59a10b8d2000?ixlib=rb-4.0.3&w=800&h=400&fit=crop&q=85&auto=format&fm=webp'),
    'general': ('General Guides', 'Guide', 'https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?ixlib=rb-4.0.3&w=800&h=400&fit=crop&q=85&auto=format&fm=webp')
}

# Generate HTML for blog cards
html_cards = []

# Process categories in order
category_order = ['beginner', 'earnings', 'centers', 'health', 'requirements', 'process', 'legal', 'states', 'general']

for cat_key in category_order:
    if cat_key in categories:
        entries = categories[cat_key]
        cat_title, badge_text, default_img = category_info.get(cat_key, ('Guides', 'Guide', 'https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?ixlib=rb-4.0.3&w=800&h=400&fit=crop&q=85&auto=format&fm=webp'))
        
        html_cards.append(f"\n<!-- {cat_title} -->")
        
        for entry in entries:
            # Join all categories for data-category attribute
            cat_data = ' '.join(entry['categories'])
            
            # Clean up title and description
            title = entry['title']
            if len(title) > 80:
                title = title[:77] + "..."
            
            desc = entry['description']
            if len(desc) > 160:
                desc = desc[:157] + "..."
            
            # Special badge for featured/important articles
            badge_class = ""
            if "ssi" in entry['slug'] or "disability" in entry['slug']:
                badge_class = " important"
                badge_text = "SSI/Disability"
            elif "2025" in entry['title'] and "biolife" in entry['slug']:
                badge_class = " featured"
                badge_text = "BioLife 2025"
            elif "2025" in entry['title'] and "grifols" in entry['slug']:
                badge_class = " featured"
                badge_text = "Grifols 2025"
            elif "2025" in entry['title'] and "kedplasma" in entry['slug']:
                badge_class = " featured"
                badge_text = "KedPlasma 2025"
            
            # Generate card HTML
            card_html = f'''<article class="blog-card" data-category="{cat_data}">
<div class="blog-image" style="background-image: url('{default_img}');">
<div class="category-badge{badge_class}">{badge_text}</div>
</div>
<div class="blog-content-area">
<h3 class="blog-title"><a href="/blog/{entry['filename']}">{title}</a></h3>
<p class="blog-excerpt">{desc}</p>
<div class="blog-meta">
<span>{badge_text if not badge_class else 'Guide'}</span>
<span class="read-time">8 min read</span>
</div>
</div>
</article>'''
            html_cards.append(card_html)

# Build the new index content
new_index = before_grid + '\n' + '\n'.join(html_cards) + '\n' + after_grid

# Write the updated index
with open(blog_dir / "index.html", 'w', encoding='utf-8') as f:
    f.write(new_index)

print(f"\n✅ Blog index updated successfully!")
print(f"Total blog cards added: {len(blog_entries)}")
print(f"Categories: {list(categories.keys())}")
print(f"Cards per category:")
for cat, entries in categories.items():
    print(f"  {cat}: {len(entries)} blogs")
