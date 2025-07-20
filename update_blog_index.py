#!/usr/bin/env python3
"""
Update blog index page with all blog posts and add Unsplash images
"""

import os
import re
from pathlib import Path

# Blog posts with their metadata and Unsplash image IDs
BLOG_POSTS = [
    # Featured guides
    {
        "file": "ultimate-plasma-donation-guide.html",
        "title": "Ultimate Plasma Donation Guide 2025: How to Earn $1,200+ Monthly",
        "excerpt": "The complete guide to maximizing plasma donation income. Learn how to earn $800-1,200 monthly, find the highest-paying opportunities, and optimize your earnings strategy.",
        "category": "Featured Guide",
        "read_time": "15 min",
        "unsplash_id": "ZiQkhI7417A",  # money/finances
        "featured": True
    },
    {
        "file": "which-plasma-center-pays-most-money.html",
        "title": "Which Plasma Center Pays the Most Money? 2025 Comparison",
        "excerpt": "Compare CSL Plasma, BioLife, Octapharma, and Grifols payment rates. Find the highest-paying plasma centers near you.",
        "category": "Center Comparison",
        "read_time": "12 min",
        "unsplash_id": "MJPr6nOdppw"  # medical/healthcare
    },
    {
        "file": "biolife-vs-csl-plasma-comparison.html",
        "title": "BioLife vs CSL Plasma: Which Pays More in 2025?",
        "excerpt": "Head-to-head comparison of the two largest plasma chains. See which offers better rates, bonuses, and donor experience.",
        "category": "Center Comparison",
        "read_time": "10 min",
        "unsplash_id": "L8tWZT4CcVQ"  # medical comparison
    },
    {
        "file": "csl-plasma-pay-rates-2025.html",
        "title": "CSL Plasma Pay Rates 2025: $70-$120 Per Visit Guide",
        "excerpt": "Complete CSL Plasma payment breakdown including new donor bonuses, loyalty rewards, and regional rate differences.",
        "category": "Payment Rates",
        "read_time": "8 min",
        "unsplash_id": "5fNmWej4tAA"  # money/calculator
    },
    {
        "file": "first-time-plasma-donation-what-to-expect.html",
        "title": "First Time Plasma Donation: Complete Guide & What to Expect",
        "excerpt": "Everything you need to know for your first plasma donation. Process, requirements, tips, and what to expect.",
        "category": "Beginner Guide",
        "read_time": "12 min",
        "unsplash_id": "SJWPKMb9u-k"  # medical/healthcare
    },
    {
        "file": "highest-paying-plasma-centers-near-me.html",
        "title": "Highest Paying Plasma Centers Near Me: 2025 Location Guide",
        "excerpt": "Find the best-paying plasma centers in your area. State-by-state breakdown of top earners and bonus programs.",
        "category": "Location Guide",
        "read_time": "10 min",
        "unsplash_id": "Q_Sei-TqSlc"  # location/map
    },
    {
        "file": "plasma-donation-side-effects.html",
        "title": "Plasma Donation Side Effects: What to Know & How to Minimize",
        "excerpt": "Understand common side effects, prevention tips, and when to seek medical attention for safe plasma donation.",
        "category": "Health & Safety",
        "read_time": "9 min",
        "unsplash_id": "uJ8LNVCBjFQ"  # health/medical
    },
    {
        "file": "plasma-donation-tax-guide-2025.html",
        "title": "Plasma Donation Tax Guide 2025: What You Need to Know",
        "excerpt": "Complete tax guide for plasma donors. Learn about 1099s, deductions, and how to report plasma income properly.",
        "category": "Tax & Legal",
        "read_time": "11 min",
        "unsplash_id": "KDeab4oW0lY"  # tax/paperwork
    },
    {
        "file": "best-plasma-centers-texas.html",
        "title": "Best Plasma Centers in Texas: Houston, Dallas, Austin Guide 2025",
        "excerpt": "Complete guide to Texas plasma centers with rates, locations, and insider tips for maximizing earnings.",
        "category": "State Guide",
        "read_time": "13 min",
        "unsplash_id": "PHIgYUGQPvU"  # Texas/location
    },
    {
        "file": "how-much-money-can-you-make-donating-plasma-2025.html",
        "title": "How Much Money Can You Make Donating Plasma in 2025?",
        "excerpt": "Realistic earnings breakdown: $400-$1,200 monthly potential based on frequency, location, and center choice.",
        "category": "Earnings Guide",
        "read_time": "10 min",
        "unsplash_id": "Dwheufds-pI"  # money counting
    },
    {
        "file": "plasma-donation-process-step-by-step.html",
        "title": "Plasma Donation Process: Step-by-Step Guide 2025",
        "excerpt": "Detailed walkthrough of the plasma donation process from arrival to payment. Know what to expect at each step.",
        "category": "Process Guide",
        "read_time": "8 min",
        "unsplash_id": "hpjSkU2UYSU"  # medical process
    },
    {
        "file": "plasma-donation-tips-beginners.html",
        "title": "Plasma Donation Tips for Beginners: Maximize Your Experience",
        "excerpt": "Essential tips for new plasma donors to optimize earnings, comfort, and safety during the donation process.",
        "category": "Beginner Tips",
        "read_time": "7 min",
        "unsplash_id": "Lks7vei-eAg"  # tips/advice
    },
    {
        "file": "state-by-state-plasma-donation-laws-regulations-2025.html",
        "title": "State-by-State Plasma Donation Laws & Regulations 2025",
        "excerpt": "Complete breakdown of plasma donation regulations across all 50 states including frequency limits and requirements.",
        "category": "Legal Guide",
        "read_time": "14 min",
        "unsplash_id": "yCdPU73kGSc"  # legal/government
    },
    {
        "file": "complete-medical-eligibility-guide-plasma-donation.html",
        "title": "Complete Medical Eligibility Guide for Plasma Donation",
        "excerpt": "Comprehensive guide to medical requirements, disqualifying conditions, and health screening process.",
        "category": "Medical Guide",
        "read_time": "12 min",
        "unsplash_id": "L8tWZT4CcVQ"  # medical checkup
    },
    {
        "file": "plasma-donation-bonuses-promotions.html",
        "title": "Plasma Donation Bonuses & Promotions: Maximize Your Earnings",
        "excerpt": "Guide to new donor bonuses, loyalty programs, and promotional offers at major plasma centers.",
        "category": "Bonuses & Promos",
        "read_time": "9 min",
        "unsplash_id": "3iexvMShGfQ"  # bonus/gift
    },
    {
        "file": "how-to-prepare-for-plasma-donation.html",
        "title": "How to Prepare for Plasma Donation: Complete Checklist",
        "excerpt": "Essential preparation tips including hydration, nutrition, sleep, and what to bring for optimal donation experience.",
        "category": "Preparation",
        "read_time": "6 min",
        "unsplash_id": "bJjsKbToY34"  # preparation/checklist
    },
    {
        "file": "understanding-plasma-medical-uses.html",
        "title": "Understanding Plasma Medical Uses: Why Your Donation Matters",
        "excerpt": "Learn about the life-saving medical uses of plasma and how your donations help create vital therapies.",
        "category": "Medical Impact",
        "read_time": "8 min",
        "unsplash_id": "qjnAnF0jIGk"  # medical research
    },
    {
        "file": "plasma-donation-weight-requirements.html",
        "title": "Plasma Donation Weight Requirements: Complete Guide 2025",
        "excerpt": "Weight requirements for plasma donation, how they affect payment, and tips for meeting eligibility criteria.",
        "category": "Requirements",
        "read_time": "5 min",
        "unsplash_id": "Zyx1bK9mqmA"  # weight/health
    },
    {
        "file": "can-you-donate-plasma-twice-a-week.html",
        "title": "Can You Donate Plasma Twice a Week? Frequency Guidelines",
        "excerpt": "FDA guidelines on plasma donation frequency, safety considerations, and how to maximize earnings safely.",
        "category": "Frequency Guide",
        "read_time": "6 min",
        "unsplash_id": "SlyCz11RhfY"  # calendar/schedule
    },
    {
        "file": "can-you-donate-plasma-with-tattoos.html",
        "title": "Can You Donate Plasma with Tattoos? Complete Guidelines",
        "excerpt": "Tattoo restrictions for plasma donation, waiting periods, and center-specific policies explained.",
        "category": "Eligibility",
        "read_time": "5 min",
        "unsplash_id": "XgOGw4UHx7A"  # tattoo/body art
    }
]

def generate_blog_card_html(post, index=0):
    """Generate HTML for a single blog card with Unsplash image"""
    
    # Use different image sizes for variety
    if post.get('featured'):
        image_size = "800x400"
        grid_span = 'style="grid-column: span 2;"'
        card_style = 'style="background: linear-gradient(135deg, #27ae60 0%, #2ecc71 100%);"'
        title_style = 'style="color: white; font-size: 1.8rem; line-height: 1.2;"'
        excerpt_style = 'style="color: rgba(255,255,255,0.9);"'
        category_style = 'style="background: rgba(255,255,255,0.2); color: white;"'
        read_time_style = 'style="color: white;"'
    else:
        image_size = "600x300"
        grid_span = ''
        card_style = ''
        title_style = ''
        excerpt_style = ''
        category_style = ''
        read_time_style = ''
    
    # Unsplash image URL
    image_url = f"https://images.unsplash.com/{post['unsplash_id']}/{image_size}?auto=format&fit=crop&q=80"
    
    return f'''
            <a href="{post['file']}" class="blog-card" {grid_span} {card_style}>
                <div class="blog-image" style="background-image: url('{image_url}'); background-size: cover; background-position: center; height: 200px; position: relative;">
                    <div style="position: absolute; top: 16px; right: 16px; background: rgba(0,0,0,0.7); color: white; padding: 8px 12px; border-radius: 20px; font-size: 0.8rem; font-weight: 500;">
                        {post['category']}
                    </div>
                </div>
                <div class="blog-card-content">
                    <h3 class="blog-title" {title_style}>{post['title']}</h3>
                    <p class="blog-excerpt" {excerpt_style}>{post['excerpt']}</p>
                    <div class="blog-meta">
                        <span class="blog-category" {category_style}>{post['category']}</span>
                        <span class="read-time" {read_time_style}>{post['read_time']} read</span>
                    </div>
                </div>
            </a>'''

def update_blog_index():
    """Update the blog index page with all blog posts"""
    
    blog_index_path = "/Users/glengomezmeade/Projects/plasma-pay-calculator/blog/index.html"
    
    try:
        with open(blog_index_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Generate all blog cards
        blog_cards_html = ""
        for i, post in enumerate(BLOG_POSTS):
            blog_cards_html += generate_blog_card_html(post, i)
        
        # Find the blog grid section and replace it
        grid_start = content.find('<div class="blog-grid">')
        grid_end = content.find('</div>', grid_start) + 6
        
        if grid_start != -1 and grid_end != -1:
            new_grid = f'''<div class="blog-grid">{blog_cards_html}
        </div>'''
            
            content = content[:grid_start] + new_grid + content[grid_end:]
            
            # Write updated content
            with open(blog_index_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✅ Updated blog index with {len(BLOG_POSTS)} posts")
            return True
        else:
            print("❌ Could not find blog grid section")
            return False
            
    except Exception as e:
        print(f"❌ Error updating blog index: {str(e)}")
        return False

def add_hero_image_to_blog_index():
    """Add a hero image to the blog index page"""
    
    blog_index_path = "/Users/glengomezmeade/Projects/plasma-pay-calculator/blog/index.html"
    
    try:
        with open(blog_index_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find the hero section
        hero_start = content.find('<div class="hero-content">')
        if hero_start != -1:
            # Add hero background image
            hero_section_start = content.rfind('<section', 0, hero_start)
            if hero_section_start != -1:
                # Find the opening tag
                tag_end = content.find('>', hero_section_start)
                if tag_end != -1:
                    # Add background image style
                    hero_bg_style = '''style="background: linear-gradient(rgba(39, 174, 96, 0.9), rgba(46, 204, 113, 0.9)), url('https://images.unsplash.com/XJXWbfSo2f0/1200x600?auto=format&fit=crop&q=80') center/cover; color: white;"'''
                    
                    # Insert the style
                    content = content[:tag_end] + f' {hero_bg_style}' + content[tag_end:]
                    
                    with open(blog_index_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    print("✅ Added hero background image")
                    return True
        
        print("❌ Could not find hero section")
        return False
        
    except Exception as e:
        print(f"❌ Error adding hero image: {str(e)}")
        return False

def main():
    """Main function"""
    print("🚀 Updating blog index with all posts and images...")
    
    # Update blog index with all posts
    if update_blog_index():
        print(f"📝 Added {len(BLOG_POSTS)} blog posts with Unsplash images")
    
    # Add hero image
    if add_hero_image_to_blog_index():
        print("🎨 Added hero background image")
    
    print("🎉 Blog index update complete!")
    print("📊 All migrated blog posts are now visible and discoverable")
    print("🖼️ Beautiful Unsplash images make the site feel more human")

if __name__ == "__main__":
    main()