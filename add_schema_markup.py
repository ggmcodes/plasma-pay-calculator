#!/usr/bin/env python3
"""Add schema markup to all pages for better SEO"""

import json
import os
import re

def create_faq_schema(faqs):
    """Create FAQ schema markup"""
    faq_items = []
    for q, a in faqs:
        faq_items.append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": a
            }
        })
    
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": faq_items
    }

def create_local_business_schema(city, state):
    """Create local business schema for calculator pages"""
    return {
        "@context": "https://schema.org",
        "@type": "MedicalBusiness",
        "name": f"Plasma Donation Centers in {city}, {state}",
        "description": f"Find and compare plasma donation centers in {city}, {state}. Calculate earnings, compare pay rates, and find the highest paying locations.",
        "url": f"https://plasmapaycalculator.com/calculators/{state.lower()}/{city.lower()}/",
        "potentialAction": {
            "@type": "SearchAction",
            "target": "https://plasmapaycalculator.com/calculators/?search={search_term_string}",
            "query-input": "required name=search_term_string"
        }
    }

def create_article_schema(title, description, date_published="2025-01-01"):
    """Create article schema for blog posts"""
    return {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "description": description,
        "datePublished": date_published,
        "dateModified": "2025-01-15",
        "author": {
            "@type": "Organization",
            "name": "Plasma Pay Calculator"
        },
        "publisher": {
            "@type": "Organization",
            "name": "Plasma Pay Calculator",
            "logo": {
                "@type": "ImageObject",
                "url": "https://plasmapaycalculator.com/icon-512.png"
            }
        }
    }

def add_schema_to_file(filepath):
    """Add schema markup to an HTML file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Skip if schema already exists
        if '"@context":"https://schema.org"' in content:
            return False
        
        # Determine file type and create appropriate schema
        schema = None
        
        if '/calculators/' in filepath and '/index.html' in filepath:
            # Calculator page - add local business schema
            parts = filepath.split('/')
            if len(parts) >= 4:
                state = parts[-3]
                city = parts[-2].replace('-', ' ').title()
                schema = create_local_business_schema(city, state.title())
        
        elif '/blog/' in filepath and filepath.endswith('.html'):
            # Blog post - add article schema
            title_match = re.search(r'<title>([^<]+)</title>', content)
            desc_match = re.search(r'<meta name="description" content="([^"]+)"', content)
            
            if title_match and desc_match:
                schema = create_article_schema(
                    title_match.group(1),
                    desc_match.group(1)
                )
        
        elif 'faq.html' in filepath:
            # FAQ page - add FAQ schema
            faqs = [
                ("How much money can you make donating plasma?", 
                 "New donors can earn $900-1200 in their first month. Regular donors typically earn $400-800 monthly donating twice per week."),
                ("How often can you donate plasma?",
                 "You can donate plasma twice per week with at least 48 hours between donations."),
                ("What are the requirements to donate plasma?",
                 "You must be 18+ years old, weigh at least 110 pounds, pass a medical screening, and provide valid ID and proof of address."),
                ("Do plasma donations get reported to the IRS?",
                 "Plasma centers are required to report payments over $600 per year to the IRS using Form 1099-MISC."),
                ("Which plasma center pays the most?",
                 "CSL Plasma, BioLife, and Octapharma typically offer the highest pay rates, with new donor bonuses up to $1200.")
            ]
            schema = create_faq_schema(faqs)
        
        if schema:
            # Add schema before </head>
            schema_tag = f'\n<script type="application/ld+json">\n{json.dumps(schema, indent=2)}\n</script>\n'
            content = content.replace('</head>', schema_tag + '</head>')
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return True
        
        return False
        
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

def main():
    print("=" * 60)
    print("ADDING SCHEMA MARKUP FOR SEO")
    print("=" * 60)
    
    files_updated = 0
    
    # Process all HTML files
    for root, dirs, files in os.walk('.'):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'node_modules']
        
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                if add_schema_to_file(filepath):
                    files_updated += 1
                    print(f"✓ Added schema to: {filepath}")
    
    print("\n" + "=" * 60)
    print(f"Schema markup added to {files_updated} files")
    print("=" * 60)
    
    print("\n✅ Schema markup implementation complete!")
    print("\nBenefits:")
    print("- Rich snippets in search results")
    print("- Higher click-through rates")
    print("- Better search visibility")
    print("- Enhanced SERP appearance")

if __name__ == "__main__":
    main()