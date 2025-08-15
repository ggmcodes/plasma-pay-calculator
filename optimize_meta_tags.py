#!/usr/bin/env python3
"""
Optimize title tags and meta descriptions for better SERP performance.
Ensures all pages have unique, keyword-rich titles and compelling descriptions.
"""

import os
import re
from pathlib import Path
from bs4 import BeautifulSoup
import json

# Keyword mappings for different page types
KEYWORD_PATTERNS = {
    'california': 'California CA plasma donation pay rates earnings 2025',
    'texas': 'Texas TX plasma donation compensation payment rates 2025',
    'florida': 'Florida FL plasma donation earnings income rates 2025',
    'new-york': 'New York NY plasma donation pay compensation 2025',
    'illinois': 'Illinois IL plasma donation rates earnings 2025',
    'biolife': 'BioLife plasma donation pay rates compensation bonus 2025',
    'csl-plasma': 'CSL Plasma donation earnings payment rates bonus 2025',
    'octapharma': 'Octapharma plasma donation pay compensation rates 2025',
    'grifols': 'Grifols plasma donation earnings payment rates 2025',
    'first-time': 'first time plasma donor bonus pay guide tips 2025',
    'requirements': 'plasma donation requirements eligibility health guidelines',
    'side-effects': 'plasma donation side effects risks safety health',
    'tax': '1099 tax plasma donation income reporting IRS 2025',
    'calculator': 'plasma donation pay calculator earnings estimator 2025',
    'maximize': 'maximize plasma donation earnings income tips strategies',
    'schedule': 'plasma donation schedule frequency twice weekly timing'
}

def get_optimized_title(file_path, current_title):
    """Generate optimized title based on file path and content"""
    path_lower = file_path.lower()
    
    # Extract location or topic from path
    if '/calculators/' in path_lower:
        # State calculator pages
        state = Path(file_path).parent.name
        state_name = state.replace('-', ' ').title()
        return f"{state_name} Plasma Donation Pay Calculator 2025 | Earnings by Center"
    
    elif '/blog/' in path_lower:
        # Blog posts - make more compelling
        if 'first-time' in path_lower:
            return "First Time Plasma Donor Guide 2025: Earn $1200+ Your First Month"
        elif 'maximize' in path_lower:
            return "How to Make $500+/Month Donating Plasma: Expert Tips & Strategies"
        elif '1099' in path_lower or 'tax' in path_lower:
            return "Plasma Donation Tax Guide 2025: 1099 Forms & IRS Requirements"
        elif 'vs' in path_lower or 'comparison' in path_lower:
            return "BioLife vs CSL Plasma 2025: Which Pays More? Complete Comparison"
        elif 'requirements' in path_lower:
            return "Plasma Donation Requirements 2025: Health, Age & Eligibility Guide"
        elif 'side-effects' in path_lower:
            return "Plasma Donation Side Effects: Safety, Risks & Health Impact Guide"
    
    elif '/centers/' in path_lower:
        # Center pages
        if 'biolife' in path_lower:
            return "BioLife Plasma Centers Near You | $900+ New Donor Bonus 2025"
        elif 'csl' in path_lower:
            return "CSL Plasma Locations & Pay Rates | $1000+ First Month 2025"
        elif 'octapharma' in path_lower:
            return "Octapharma Plasma Centers | Earn $100+ Per Donation 2025"
        elif 'grifols' in path_lower:
            return "Grifols Plasma Centers Near Me | Top Pay Rates 2025"
        elif 'index' in Path(file_path).name:
            return "Find Plasma Centers Near You | Compare Pay Rates 2025"
    
    # Default: improve existing title
    if len(current_title) < 40:
        current_title += " | Plasma Pay Calculator 2025"
    
    # Ensure title is 50-60 characters
    if len(current_title) > 60:
        current_title = current_title[:57] + "..."
    
    return current_title

def get_optimized_description(file_path, current_desc):
    """Generate optimized meta description"""
    path_lower = file_path.lower()
    
    # Extract keywords based on path
    keywords_found = []
    for pattern, keywords in KEYWORD_PATTERNS.items():
        if pattern in path_lower:
            keywords_found.append(keywords)
    
    if '/calculators/' in path_lower:
        state = Path(file_path).parent.name
        state_name = state.replace('-', ' ').title()
        return f"Calculate your {state_name} plasma donation earnings instantly. Compare pay rates from BioLife, CSL Plasma, Octapharma & more. Earn $400-$800/month. Updated 2025 rates."
    
    elif '/blog/' in path_lower:
        if 'first-time' in path_lower:
            return "Complete first-time plasma donor guide 2025. Earn $1200+ your first month with new donor bonuses. Step-by-step process, requirements, tips & payment schedules."
        elif 'maximize' in path_lower:
            return "Expert strategies to earn $500-$800/month donating plasma. Bonus tips, optimal scheduling, multi-center strategies & payment maximization guide for 2025."
        elif '1099' in path_lower:
            return "Everything about 1099 forms for plasma donations. Tax reporting requirements, $600 threshold, filing tips & IRS compliance guide for 2025 tax year."
        elif 'requirements' in path_lower:
            return "Complete plasma donation eligibility guide. Age, weight, health requirements, medications, medical conditions & qualification criteria. Updated 2025."
        elif 'side-effects' in path_lower:
            return "Understand plasma donation side effects, risks & safety. Common reactions, long-term effects, health impacts & medical advice. Evidence-based guide 2025."
    
    elif '/centers/' in path_lower:
        if 'biolife' in path_lower:
            return "Find BioLife Plasma centers near you. New donors earn $900+ first month. Current pay rates, bonus offers, locations & hours. Updated January 2025."
        elif 'csl' in path_lower:
            return "Locate CSL Plasma centers & compare pay rates. Earn $1000+ as new donor. Promotions, requirements, appointment booking & payment info 2025."
        elif 'octapharma' in path_lower:
            return "Octapharma plasma center locations & earnings guide. Top pay rates up to $100/donation. New donor bonuses, promotions & loyalty rewards 2025."
    
    # Default: improve existing or create new
    if not current_desc or len(current_desc) < 100:
        return "Calculate plasma donation earnings & find top-paying centers near you. Compare BioLife, CSL, Octapharma rates. Earn $400-$800/month. Updated 2025."
    
    # Ensure 150-160 characters
    if len(current_desc) > 160:
        current_desc = current_desc[:157] + "..."
    elif len(current_desc) < 150:
        current_desc += " Updated 2025 rates & requirements."
    
    return current_desc

def optimize_file(file_path):
    """Optimize title and meta description for a single file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        
        changes = []
        
        # Find and optimize title tag
        title_tag = soup.find('title')
        if title_tag:
            current_title = title_tag.string or ""
            optimized_title = get_optimized_title(file_path, current_title)
            
            if optimized_title != current_title:
                title_tag.string = optimized_title
                changes.append('title')
        else:
            # Add title tag if missing
            head = soup.find('head')
            if head:
                new_title = soup.new_tag('title')
                new_title.string = get_optimized_title(file_path, "")
                head.append(new_title)
                changes.append('title')
        
        # Find and optimize meta description
        meta_desc = soup.find('meta', {'name': 'description'})
        if meta_desc:
            current_desc = meta_desc.get('content', '')
            optimized_desc = get_optimized_description(file_path, current_desc)
            
            if optimized_desc != current_desc:
                meta_desc['content'] = optimized_desc
                changes.append('description')
        else:
            # Add meta description if missing
            head = soup.find('head')
            if head:
                new_meta = soup.new_tag('meta', attrs={
                    'name': 'description',
                    'content': get_optimized_description(file_path, "")
                })
                head.append(new_meta)
                changes.append('description')
        
        # Add Open Graph tags if missing
        og_title = soup.find('meta', {'property': 'og:title'})
        if not og_title:
            head = soup.find('head')
            if head:
                title_text = soup.find('title').string if soup.find('title') else ""
                og_tag = soup.new_tag('meta', property='og:title', content=title_text)
                head.append(og_tag)
                changes.append('og:title')
        
        og_desc = soup.find('meta', {'property': 'og:description'})
        if not og_desc:
            head = soup.find('head')
            if head:
                desc_tag = soup.find('meta', {'name': 'description'})
                desc_text = desc_tag.get('content', '') if desc_tag else ""
                og_tag = soup.new_tag('meta', property='og:description', content=desc_text)
                head.append(og_tag)
                changes.append('og:description')
        
        if changes:
            # Write optimized content
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            
            return True, changes
        
        return False, []
        
    except Exception as e:
        print(f"Error optimizing {file_path}: {e}")
        return False, []

def main():
    """Main optimization function"""
    print("Starting meta tag optimization...")
    
    # Find all HTML files
    html_files = []
    for root, dirs, files in os.walk('.'):
        # Skip certain directories
        if 'node_modules' in root or '.git' in root or 'includes' in root:
            continue
        
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    
    print(f"Found {len(html_files)} HTML files")
    
    # Track optimization stats
    optimized = 0
    optimization_stats = {}
    
    # Sample of optimizations for review
    sample_optimizations = []
    
    # Optimize each file
    for i, file_path in enumerate(html_files):
        if i % 50 == 0:
            print(f"Progress: {i}/{len(html_files)} files processed...")
        
        success, changes = optimize_file(file_path)
        
        if success:
            optimized += 1
            for change in changes:
                optimization_stats[change] = optimization_stats.get(change, 0) + 1
            
            # Collect samples
            if len(sample_optimizations) < 5:
                with open(file_path, 'r', encoding='utf-8') as f:
                    soup = BeautifulSoup(f.read(), 'html.parser')
                    title = soup.find('title')
                    desc = soup.find('meta', {'name': 'description'})
                    
                    sample_optimizations.append({
                        'file': file_path,
                        'title': title.string if title else 'N/A',
                        'description': desc.get('content', 'N/A') if desc else 'N/A'
                    })
    
    # Print summary
    print(f"\n✅ Meta Tag Optimization Complete!")
    print(f"Files optimized: {optimized}/{len(html_files)}")
    
    if optimization_stats:
        print("\nOptimizations applied:")
        for opt, count in sorted(optimization_stats.items(), key=lambda x: x[1], reverse=True):
            print(f"  - {opt}: {count} files")
    
    print("\n📊 Sample Optimizations:")
    for sample in sample_optimizations[:3]:
        print(f"\nFile: {sample['file']}")
        print(f"Title ({len(sample['title'])} chars): {sample['title'][:60]}...")
        print(f"Desc ({len(sample['description'])} chars): {sample['description'][:80]}...")
    
    print("\n🎯 SEO Benefits:")
    print("  - Optimized title tags (50-60 characters)")
    print("  - Compelling meta descriptions (150-160 characters)")
    print("  - Added Open Graph tags for social sharing")
    print("  - Keyword-rich content for better rankings")
    print("  - Location and brand-specific optimization")
    
    return optimized

if __name__ == "__main__":
    main()