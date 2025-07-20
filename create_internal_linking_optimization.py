#!/usr/bin/env python3
"""
Create internal linking optimization and topic clusters for SEO dominance
"""

import os
import re
from glob import glob

def create_topic_clusters():
    """Create topic cluster hub pages for better internal linking"""
    
    clusters = {
        'earning-strategies': {
            'title': 'Plasma Donation Earning Strategies: Maximize Your Income 2025',
            'description': 'Complete guide to maximizing plasma donation earnings with proven strategies, bonus optimization, and center selection tips.',
            'pages': [
                '/blog/maximize-plasma-earnings.html',
                '/blog/highest-paying-plasma-centers-2025.html',
                '/blog/plasma-donation-bonuses-promotions.html',
                '/blog/can-you-make-1000-month-donating-plasma.html',
                '/blog/ab-plasma-donation-calculator.html'
            ]
        },
        'center-comparisons': {
            'title': 'Plasma Center Comparisons: Find the Highest Paying Centers',
            'description': 'Side-by-side comparisons of major plasma centers including CSL Plasma, BioLife, Octapharma, and Grifols.',
            'pages': [
                '/blog/plasma-center-comparison.html',
                '/blog/which-plasma-center-pays-most-money.html',
                '/blog/biolife-vs-csl-plasma-comparison.html',
                '/tools/csl-vs-biolife-calculator.html',
                '/tools/all-plasma-centers-comparison.html'
            ]
        },
        'requirements-eligibility': {
            'title': 'Plasma Donation Requirements & Eligibility Guide 2025',
            'description': 'Complete guide to plasma donation requirements, eligibility criteria, and qualification tips.',
            'pages': [
                '/blog/plasma-donation-requirements.html',
                '/blog/complete-medical-eligibility-guide-plasma-donation.html',
                '/blog/plasma-donation-weight-requirements.html',
                '/blog/can-you-donate-plasma-with-tattoos.html',
                '/health/'
            ]
        },
        'tax-legal': {
            'title': 'Plasma Donation Taxes & Legal Guide: IRS Reporting 2025',
            'description': 'Everything you need to know about reporting plasma income, 1099 forms, and tax optimization.',
            'pages': [
                '/blog/plasma-donation-tax-guide-2025.html',
                '/blog/does-irs-track-plasma-donations.html',
                '/blog/do-you-get-1099-plasma-donation.html',
                '/blog/do-plasma-centers-report-social-security.html',
                '/seasonal/tax-season-plasma-guide.html'
            ]
        }
    }
    
    created_count = 0
    
    for cluster_id, cluster_data in clusters.items():
        file_path = f"/Users/glengomezmeade/Projects/plasma-pay-calculator/topics/{cluster_id}/index.html"
        
        # Create directory
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{cluster_data['title']}</title>
    <meta name="description" content="{cluster_data['description']}">
    <meta name="keywords" content="plasma donation, {cluster_id.replace('-', ' ')}, plasma income guide">
    <link rel="canonical" href="https://plasmapaycalculator.com/topics/{cluster_id}/">
    
    <!-- Open Graph -->
    <meta property="og:title" content="{cluster_data['title']}">
    <meta property="og:description" content="{cluster_data['description']}">
    <meta property="og:url" content="https://plasmapaycalculator.com/topics/{cluster_id}/">
    <meta property="og:type" content="website">
    
    <!-- Topic Cluster Schema -->
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "CollectionPage",
        "name": "{cluster_data['title']}",
        "description": "{cluster_data['description']}",
        "url": "https://plasmapaycalculator.com/topics/{cluster_id}/",
        "mainEntity": {{
            "@type": "ItemList",
            "itemListElement": ['''

        # Add related pages to schema
        for i, page in enumerate(cluster_data['pages']):
            page_title = page.split('/')[-1].replace('.html', '').replace('-', ' ').title()
            content += f'''
                {{
                    "@type": "ListItem",
                    "position": {i + 1},
                    "item": {{
                        "@type": "WebPage",
                        "url": "https://plasmapaycalculator.com{page}",
                        "name": "{page_title}"
                    }}
                }}'''
            if i < len(cluster_data['pages']) - 1:
                content += ','

        content += f'''
            ]
        }}
    }}
    </script>
    
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    colors: {{
                        'primary': '#27ae60',
                        'secondary': '#2ecc71',
                        'accent': '#e74c3c'
                    }}
                }}
            }}
        }}
    </script>
</head>
<body class="bg-gray-50">
    <!-- Navigation -->
    <header class="bg-white border-b border-gray-200 shadow-sm sticky top-0 z-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex items-center justify-between h-16">
                <div class="flex items-center space-x-2 font-semibold text-lg text-gray-900">
                    <span class="text-xl">💰</span>
                    <a href="/" class="font-inter">Plasma Pay Calculator</a>
                </div>
                <nav class="hidden md:flex items-center space-x-8">
                    <a href="/" class="text-gray-600 hover:text-gray-900 font-medium">Calculator</a>
                    <a href="/blog/" class="text-gray-600 hover:text-gray-900 font-medium">Blog</a>
                    <a href="/states.html" class="text-gray-600 hover:text-gray-900 font-medium">States</a>
                    <a href="/centers/" class="bg-primary hover:bg-secondary text-white px-4 py-2 rounded-lg font-semibold">Find Centers</a>
                </nav>
            </div>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="relative min-h-[50vh] flex items-center justify-center bg-gradient-to-br from-primary to-secondary text-white">
        <div class="relative z-20 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
            <h1 class="text-4xl md:text-5xl lg:text-6xl font-bold mb-6 leading-tight">
                📚 {cluster_data['title'].split(':')[0]}
            </h1>
            <p class="text-xl md:text-2xl mb-8 text-white/90 leading-relaxed">
                {cluster_data['description']}
            </p>
            <a href="/" class="bg-white text-primary px-8 py-4 rounded-lg font-semibold text-lg hover:bg-gray-100 transition-colors">
                Use Calculator
            </a>
        </div>
    </section>

    <!-- Content Grid -->
    <section class="py-16 bg-white">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <h2 class="text-3xl font-bold text-center text-gray-900 mb-12">
                Complete Resource Collection
            </h2>
            
            <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">'''

        # Add resource cards
        for page in cluster_data['pages']:
            page_title = page.split('/')[-1].replace('.html', '').replace('-', ' ').title()
            page_type = 'Calculator' if '/tools/' in page else 'Guide' if '/blog/' in page else 'Resource'
            
            content += f'''
                <div class="bg-white border border-gray-200 rounded-xl shadow-lg hover:shadow-xl transition-shadow p-6">
                    <div class="flex items-center justify-between mb-4">
                        <span class="bg-primary/10 text-primary px-3 py-1 rounded-full text-sm font-medium">{page_type}</span>
                        <span class="text-2xl">💡</span>
                    </div>
                    <h3 class="text-xl font-bold text-gray-900 mb-3">{page_title}</h3>
                    <p class="text-gray-600 mb-4">Comprehensive resource for maximizing your plasma donation experience and earnings.</p>
                    <a href="{page}" class="bg-primary hover:bg-secondary text-white px-4 py-2 rounded-lg font-semibold transition-colors">
                        Read More →
                    </a>
                </div>'''

        content += f'''
            </div>
        </div>
    </section>

    <!-- Call to Action -->
    <section class="py-16 bg-gray-50">
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
            <h2 class="text-3xl font-bold text-gray-900 mb-6">Ready to Maximize Your Earnings?</h2>
            <p class="text-xl text-gray-600 mb-8">Use our calculator to find the best paying plasma centers in your area</p>
            <a href="/" class="bg-primary hover:bg-secondary text-white px-8 py-4 rounded-lg font-semibold text-lg transition-colors">
                Calculate Your Earnings
            </a>
        </div>
    </section>

    <!-- Footer -->
    <footer class="bg-gray-900 text-white py-12">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid md:grid-cols-4 gap-8">
                <div>
                    <h4 class="text-lg font-semibold mb-4">Topic Clusters</h4>
                    <ul class="space-y-2 text-gray-400">
                        <li><a href="/topics/earning-strategies/" class="hover:text-white">Earning Strategies</a></li>
                        <li><a href="/topics/center-comparisons/" class="hover:text-white">Center Comparisons</a></li>
                        <li><a href="/topics/requirements-eligibility/" class="hover:text-white">Requirements</a></li>
                        <li><a href="/topics/tax-legal/" class="hover:text-white">Tax & Legal</a></li>
                    </ul>
                </div>
                <div>
                    <h4 class="text-lg font-semibold mb-4">Quick Links</h4>
                    <ul class="space-y-2 text-gray-400">
                        <li><a href="/" class="hover:text-white">Calculator</a></li>
                        <li><a href="/blog/" class="hover:text-white">Blog</a></li>
                        <li><a href="/centers/" class="hover:text-white">Find Centers</a></li>
                    </ul>
                </div>
                <div>
                    <h4 class="text-lg font-semibold mb-4">Tools</h4>
                    <ul class="space-y-2 text-gray-400">
                        <li><a href="/tools/csl-vs-biolife-calculator.html" class="hover:text-white">CSL vs BioLife</a></li>
                        <li><a href="/tools/all-plasma-centers-comparison.html" class="hover:text-white">All Centers</a></li>
                        <li><a href="/states.html" class="hover:text-white">State Rates</a></li>
                    </ul>
                </div>
                <div>
                    <h4 class="text-lg font-semibold mb-4">Support</h4>
                    <ul class="space-y-2 text-gray-400">
                        <li><a href="/faq.html" class="hover:text-white">FAQ</a></li>
                        <li><a href="/about.html" class="hover:text-white">About</a></li>
                        <li><a href="/contact.html" class="hover:text-white">Contact</a></li>
                    </ul>
                </div>
            </div>
            <div class="border-t border-gray-800 mt-8 pt-8 text-center text-gray-400">
                <p>&copy; 2025 Plasma Pay Calculator. All rights reserved.</p>
            </div>
        </div>
    </footer>
</body>
</html>'''

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Created topic cluster: {cluster_id}")
        created_count += 1
    
    return created_count

def add_contextual_internal_links():
    """Add contextual internal links to existing content"""
    
    # Define link opportunities in existing content
    link_patterns = {
        'plasma center': '/centers/',
        'calculate your earnings': '/',
        'plasma pay rates': '/blog/plasma-center-comparison.html',
        'new donor bonus': '/blog/plasma-donation-bonuses-promotions.html',
        'CSL Plasma': '/centers/csl-plasma/',
        'BioLife': '/centers/biolife/',
        'Octapharma': '/centers/octapharma/',
        'tax guide': '/blog/plasma-donation-tax-guide-2025.html',
        'eligibility requirements': '/blog/complete-medical-eligibility-guide-plasma-donation.html'
    }
    
    # Files to update with contextual links
    files_to_update = [
        '/Users/glengomezmeade/Projects/plasma-pay-calculator/blog/maximize-plasma-earnings.html',
        '/Users/glengomezmeade/Projects/plasma-pay-calculator/blog/plasma-center-comparison.html'
    ]
    
    links_added = 0
    
    for file_path in files_to_update:
        if not os.path.exists(file_path):
            continue
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Add contextual internal links
            for keyword, link_url in link_patterns.items():
                # Only add links if the keyword exists and isn't already linked
                pattern = f'(?<!href=")(?<!">){re.escape(keyword)}(?!</a>)'
                replacement = f'<a href="{link_url}" class="text-primary hover:text-secondary underline">{keyword}</a>'
                
                # Only replace first occurrence to avoid over-linking
                content = re.sub(pattern, replacement, content, count=1, flags=re.IGNORECASE)
            
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                links_added += 1
                filename = os.path.basename(file_path)
                print(f"✅ Added contextual links to {filename}")
            
        except Exception as e:
            print(f"❌ Error adding links to {file_path}: {str(e)}")
    
    return links_added

def create_topic_navigation():
    """Create topic navigation component for better UX"""
    
    nav_file = "/Users/glengomezmeade/Projects/plasma-pay-calculator/includes/topic-navigation.html"
    
    # Create includes directory
    os.makedirs(os.path.dirname(nav_file), exist_ok=True)
    
    nav_content = '''<!-- Topic Navigation Component -->
<section class="bg-primary/5 py-8 border-t border-primary/20">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h3 class="text-xl font-bold text-gray-900 mb-6 text-center">Explore Related Topics</h3>
        
        <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-4">
            <a href="/topics/earning-strategies/" class="bg-white rounded-lg p-4 shadow-sm hover:shadow-md transition-shadow border border-gray-200">
                <div class="flex items-center space-x-3">
                    <span class="text-2xl">💰</span>
                    <div>
                        <h4 class="font-semibold text-gray-900">Earning Strategies</h4>
                        <p class="text-sm text-gray-600">Maximize income</p>
                    </div>
                </div>
            </a>
            
            <a href="/topics/center-comparisons/" class="bg-white rounded-lg p-4 shadow-sm hover:shadow-md transition-shadow border border-gray-200">
                <div class="flex items-center space-x-3">
                    <span class="text-2xl">⚖️</span>
                    <div>
                        <h4 class="font-semibold text-gray-900">Center Comparisons</h4>
                        <p class="text-sm text-gray-600">Find best rates</p>
                    </div>
                </div>
            </a>
            
            <a href="/topics/requirements-eligibility/" class="bg-white rounded-lg p-4 shadow-sm hover:shadow-md transition-shadow border border-gray-200">
                <div class="flex items-center space-x-3">
                    <span class="text-2xl">📋</span>
                    <div>
                        <h4 class="font-semibold text-gray-900">Requirements</h4>
                        <p class="text-sm text-gray-600">Eligibility guide</p>
                    </div>
                </div>
            </a>
            
            <a href="/topics/tax-legal/" class="bg-white rounded-lg p-4 shadow-sm hover:shadow-md transition-shadow border border-gray-200">
                <div class="flex items-center space-x-3">
                    <span class="text-2xl">📊</span>
                    <div>
                        <h4 class="font-semibold text-gray-900">Tax & Legal</h4>
                        <p class="text-sm text-gray-600">IRS reporting</p>
                    </div>
                </div>
            </a>
        </div>
    </div>
</section>'''
    
    with open(nav_file, 'w', encoding='utf-8') as f:
        f.write(nav_content)
    
    print("✅ Created topic navigation component")
    return True

def main():
    """Main function to create internal linking optimization"""
    print("🔗 Creating internal linking optimization and topic clusters...")
    
    total_implementations = 0
    
    # Create topic clusters
    print("\n📚 Creating topic cluster hub pages...")
    cluster_count = create_topic_clusters()
    total_implementations += cluster_count
    print(f"✅ Created {cluster_count} topic cluster pages")
    
    # Add contextual internal links
    print("\n🔗 Adding contextual internal links...")
    link_count = add_contextual_internal_links()
    total_implementations += link_count
    print(f"✅ Added contextual links to {link_count} pages")
    
    # Create topic navigation
    print("\n🧭 Creating topic navigation component...")
    if create_topic_navigation():
        total_implementations += 1
    
    print(f"\n🎉 Internal linking optimization complete!")
    print(f"📊 Total implementations: {total_implementations}")
    print(f"🚀 Enhanced topic clustering for SEO authority")
    print(f"🎯 Improved internal PageRank distribution")

if __name__ == "__main__":
    main()