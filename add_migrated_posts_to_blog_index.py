#!/usr/bin/env python3
"""
Add Migrated Posts to Blog Index
Updates the blog/index.html to include the newly migrated posts from plasmacenterfinder
"""

import re

# List of migrated posts with their categories and descriptions
MIGRATED_POSTS = [
    {
        'file': 'first-time-plasma-donor-guide-2025.html',
        'title': 'First-Time Plasma Donor\'s Complete Guide 2025',
        'excerpt': 'Everything you need to know before your first plasma donation. Requirements, process, and what to expect step-by-step.',
        'category': 'beginner',
        'category_display': 'Beginner Guide',
        'read_time': '15 min read',
        'image': 'https://images.unsplash.com/photo-1485182708500-e8f1f318ba72?ixlib=rb-4.0.3&w=800&h=400&fit=crop&q=85&auto=format&fm=webp'
    },
    {
        'file': 'maximize-plasma-donation-earnings-2025.html',
        'title': 'How to Maximize Plasma Donation Earnings in 2025',
        'excerpt': 'Proven strategies to earn the most money from plasma donations. Bonuses, referrals, and timing tips for maximum income.',
        'category': 'earnings',
        'category_display': 'Earnings Guide',
        'read_time': '12 min read',
        'image': 'https://images.unsplash.com/photo-1554224155-6726b3ff858f?ixlib=rb-4.0.3&w=800&h=400&fit=crop&q=85&auto=format&fm=webp'
    },
    {
        'file': 'biolife-vs-csl-plasma-comparison-2025.html',
        'title': 'BioLife vs CSL Plasma: Detailed Comparison 2025',
        'excerpt': 'Compare the two largest plasma chains. Pay rates, bonuses, locations, and donor experiences side-by-side.',
        'category': 'centers',
        'category_display': 'Center Comparison',
        'read_time': '14 min read',
        'image': 'https://images.unsplash.com/photo-1586773860418-d37222d8fce3?ixlib=rb-4.0.3&w=800&h=400&fit=crop&q=85&auto=format&fm=webp'
    },
    {
        'file': 'plasma-donation-requirements-2025.html',
        'title': 'Plasma Donation Requirements & Eligibility 2025',
        'excerpt': 'Complete eligibility criteria. Age, weight, health requirements, and what can disqualify you from donating.',
        'category': 'requirements',
        'category_display': 'Requirements',
        'read_time': '13 min read',
        'image': 'https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?ixlib=rb-4.0.3&w=800&h=400&fit=crop&q=85&auto=format&fm=webp'
    },
    {
        'file': 'plasma-donation-side-effects-safety-2025.html',
        'title': 'Plasma Donation Side Effects & Safety Guide 2025',
        'excerpt': 'Understanding risks, side effects, and safety protocols. How to donate safely and minimize discomfort.',
        'category': 'health',
        'category_display': 'Health & Safety',
        'read_time': '16 min read',
        'image': 'https://images.unsplash.com/photo-1559757148-5c350d0d3c56?ixlib=rb-4.0.3&w=800&h=400&fit=crop&q=85&auto=format&fm=webp'
    },
    {
        'file': 'best-plasma-centers-by-state-2025.html',
        'title': 'Best Plasma Centers by State 2025',
        'excerpt': 'State-by-state breakdown of top-paying plasma centers. Regional differences and local earning opportunities.',
        'category': 'centers',
        'category_display': 'State Guide',
        'read_time': '18 min read',
        'image': 'https://images.unsplash.com/photo-1544197150-b99a580bb7a8?ixlib=rb-4.0.3&w=800&h=400&fit=crop&q=85&auto=format&fm=webp'
    },
    {
        'file': 'plasma-donation-payment-methods-2025.html',
        'title': 'Plasma Donation Payment Methods Explained 2025',
        'excerpt': 'How plasma centers pay donors. Prepaid cards, direct deposit, and payment schedules explained.',
        'category': 'earnings',
        'category_display': 'Payment Methods',
        'read_time': '11 min read',
        'image': 'https://images.unsplash.com/photo-1563013544-824ae1b704d3?ixlib=rb-4.0.3&w=800&h=400&fit=crop&q=85&auto=format&fm=webp'
    },
    {
        'file': 'plasma-donation-referral-bonuses-2025.html',
        'title': 'Plasma Referral Programs & Bonuses Guide 2025',
        'excerpt': 'Maximize earnings through referral programs. Current bonuses and how to qualify for extra payments.',
        'category': 'earnings',
        'category_display': 'Referral Bonuses',
        'read_time': '10 min read',
        'image': 'https://images.unsplash.com/photo-1563013544-824ae1b704d3?ixlib=rb-4.0.3&w=800&h=400&fit=crop&q=85&auto=format&fm=webp'
    },
    {
        'file': 'health-tips-plasma-donors-2025.html',
        'title': 'Health Tips for Regular Plasma Donors 2025',
        'excerpt': 'Stay healthy while donating regularly. Nutrition, hydration, and recovery tips for frequent donors.',
        'category': 'health',
        'category_display': 'Health Tips',
        'read_time': '11 min read',
        'image': 'https://images.unsplash.com/photo-1532938911079-1b06ac7ceec7?ixlib=rb-4.0.3&w=800&h=400&fit=crop&q=85&auto=format&fm=webp'
    },
    {
        'file': 'plasma-donation-process-explained-2025.html',
        'title': 'The Plasma Donation Process Step-by-Step 2025',
        'excerpt': 'Detailed walkthrough of the donation process. From registration to payment, know what to expect.',
        'category': 'beginner',
        'category_display': 'Process Guide',
        'read_time': '14 min read',
        'image': 'https://images.unsplash.com/photo-1551601651-2a8555f1a136?ixlib=rb-4.0.3&w=800&h=400&fit=crop&q=85&auto=format&fm=webp'
    },
    {
        'file': 'plasma-vs-blood-donation-guide-2025.html',
        'title': 'Plasma vs Blood Donation: Complete Guide 2025',
        'excerpt': 'How plasma donation differs from blood donation. Which is right for you and why it matters.',
        'category': 'beginner',
        'category_display': 'Comparison Guide',
        'read_time': '10 min read',
        'image': 'https://images.unsplash.com/photo-1582719471384-894fbb16e074?ixlib=rb-4.0.3&w=800&h=400&fit=crop&q=85&auto=format&fm=webp'
    },
    {
        'file': 'plasma-donation-tax-guide-2025.html',
        'title': 'Plasma Donation Income Tax Guide 2025',
        'excerpt': 'Understanding tax implications of plasma donation income. Reporting requirements and deduction tips.',
        'category': 'legal',
        'category_display': 'Tax Guide',
        'read_time': '14 min read',
        'image': 'https://images.unsplash.com/photo-1450101499163-c8848c66ca85?ixlib=rb-4.0.3&w=800&h=400&fit=crop&q=85&auto=format&fm=webp'
    },
    {
        'file': 'plasma-donation-disqualifications-complete-list-2025.html',
        'title': 'What Disqualifies You from Plasma Donation? Complete List 2025',
        'excerpt': 'Comprehensive guide to disqualifications including medical conditions, medications, travel history, and lifestyle factors.',
        'category': 'requirements',
        'category_display': 'Disqualifications',
        'read_time': '12 min read',
        'image': 'https://images.unsplash.com/photo-1565458788203-ac5a555ac862?ixlib=rb-4.0.3&w=800&h=400&fit=crop&q=85&auto=format&fm=webp'
    },
    {
        'file': 'student-guide-plasma-donation-college-money-2025.html',
        'title': 'Student Guide to Plasma Donation for College Money 2025',
        'excerpt': 'How college students can earn $400-800/month through plasma donation. Campus locations, scheduling, and success tips.',
        'category': 'earnings beginner',
        'category_display': 'Student Guide',
        'read_time': '13 min read',
        'image': 'https://images.unsplash.com/photo-1434030216411-0b793f4b4173?ixlib=rb-4.0.3&w=800&h=400&fit=crop&q=85&auto=format&fm=webp'
    },
    {
        'file': 'plasma-donation-myths-vs-facts-debunked-2025.html',
        'title': 'Plasma Donation Myths vs Facts: Everything Debunked 2025',
        'excerpt': 'Evidence-based truth about plasma donation. Debunking common myths about safety, health effects, and donation process.',
        'category': 'health beginner',
        'category_display': 'Myths vs Facts',
        'read_time': '11 min read',
        'image': 'https://images.unsplash.com/photo-1559757175-0eb30cd6b4d8?ixlib=rb-4.0.3&w=800&h=400&fit=crop&q=85&auto=format&fm=webp'
    },
    {
        'file': 'how-to-recover-faster-after-plasma-donation-2025.html',
        'title': 'How to Recover Faster After Plasma Donation: Complete Recovery Guide',
        'excerpt': 'Expert tips for optimal recovery including nutrition, hydration, rest strategies, and warning signs to watch for.',
        'category': 'health',
        'category_display': 'Recovery Guide',
        'read_time': '13 min read',
        'image': 'https://images.unsplash.com/photo-1583947215259-38e31be8751f?ixlib=rb-4.0.3&w=800&h=400&fit=crop&q=85&auto=format&fm=webp'
    },
    {
        'file': 'emergency-money-plasma-donation-financial-crisis-2025.html',
        'title': 'Emergency Money Through Plasma Donation: Your Financial Crisis Lifeline',
        'excerpt': 'How to earn $100-200+ weekly during financial emergencies. Crisis strategies, budgeting tips, and success stories.',
        'category': 'earnings',
        'category_display': 'Emergency Money',
        'read_time': '14 min read',
        'image': 'https://images.unsplash.com/photo-1560472355-536de3962603?ixlib=rb-4.0.3&w=800&h=400&fit=crop&q=85&auto=format&fm=webp'
    },
    {
        'file': 'what-to-eat-before-after-plasma-donation-2025.html',
        'title': 'What to Eat Before & After Plasma Donation: Complete Nutrition Guide',
        'excerpt': 'Optimal nutrition for plasma donors. What to eat before and after donation for better health and maximum earning potential.',
        'category': 'health',
        'category_display': 'Nutrition Guide',
        'read_time': '12 min read',
        'image': 'https://images.unsplash.com/photo-1490645935967-10de6ba17061?ixlib=rb-4.0.3&w=800&h=400&fit=crop&q=85&auto=format&fm=webp'
    },
    {
        'file': 'plasma-donation-vs-gig-economy-comparison-2025.html',
        'title': 'Plasma Donation vs Gig Economy: Which Pays More? 2025 Analysis',
        'excerpt': 'Complete comparison of plasma donation income vs popular gig economy jobs. Real earnings data and time investment analysis.',
        'category': 'earnings',
        'category_display': 'Income Comparison',
        'read_time': '15 min read',
        'image': 'https://images.unsplash.com/photo-1556742111-a301076d9d18?ixlib=rb-4.0.3&w=800&h=400&fit=crop&q=85&auto=format&fm=webp'
    }
]

def generate_blog_card(post):
    """Generate HTML for a blog card"""
    return f'''            <article class="blog-card" data-category="{post['category']}">
                <div class="blog-image" style="background-image: url('{post['image']}');">
                    <div class="category-badge">{post['category_display']}</div>
                </div>
                <div class="blog-content-area">
                    <h3 class="blog-title"><a href="/blog/{post['file']}">{post['title']}</a></h3>
                    <p class="blog-excerpt">{post['excerpt']}</p>
                    <div class="blog-meta">
                        <span>{post['category_display']}</span>
                        <span class="read-time">{post['read_time']}</span>
                    </div>
                </div>
            </article>

'''

def main():
    """Main function to update blog index"""
    
    # Read current blog index
    blog_index_path = '/Users/glengomezmeade/Projects/plasma-pay-calculator/blog/index.html'
    with open(blog_index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("Generating blog cards for migrated posts...")
    
    # Generate new blog cards
    new_cards = []
    for post in MIGRATED_POSTS:
        new_cards.append(generate_blog_card(post))
    
    new_cards_html = ''.join(new_cards)
    
    # Find the insertion point (after the existing blog cards, before the closing </div>)
    # We'll add them at the end of the existing articles
    pattern = r'(</article>\s*\n\s*)</div>\s*\n\s*<div class="no-results"'
    
    # Insert the new cards
    replacement = r'\1' + new_cards_html + r'        </div>\n\n        <div class="no-results"'
    
    updated_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    # If that didn't work, try a different pattern
    if updated_content == content:
        # Look for the end of the blog grid
        pattern = r'(</article>\s*\n\s*)(        </div>\s*\n\s*<div class="no-results")'
        replacement = r'\1' + new_cards_html + r'\2'
        updated_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    # Write the updated content
    with open(blog_index_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print(f"✓ Added {len(MIGRATED_POSTS)} new blog cards to blog/index.html")
    print("\nAdded posts:")
    for post in MIGRATED_POSTS:
        print(f"  - {post['title']}")
    
    print("\nNext steps:")
    print("1. Test the blog index page")
    print("2. Verify search functionality works with new posts")
    print("3. Update sitemap.xml")

if __name__ == "__main__":
    main()