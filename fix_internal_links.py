#!/usr/bin/env python3

import os
import re
from pathlib import Path

def fix_internal_links():
    blog_dir = Path("/Users/glengomezmeade/Projects/plasma-pay-calculator/blog")
    blog_files = list(blog_dir.glob("*.html"))
    
    # Also process subdirectory index files
    for subdir in blog_dir.iterdir():
        if subdir.is_dir() and subdir.name != "." and subdir.name != "..":
            index_file = subdir / "index.html"
            if index_file.exists():
                blog_files.append(index_file)
    
    print(f"Processing {len(blog_files)} HTML files...")
    
    fixes_made = 0
    files_fixed = 0
    
    for blog_file in blog_files:
        try:
            with open(blog_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Fix calculator links
            content = re.sub(r'href="\.\./#calculator"', 'href="/#calculator"', content)
            content = re.sub(r'href="#calculator"(?![^>]*class=".*?centers-highlight)', 'href="/#calculator"', content)
            
            # Fix blog links
            content = re.sub(r'href="\.\./(blog/)"', 'href="/blog/"', content)
            
            # Fix center links
            content = re.sub(r'href="\.\./(centers/)"', 'href="/centers/"', content)
            
            # Fix state links
            content = re.sub(r'href="\.\./(states\.html)"', 'href="/states.html"', content)
            
            # Fix FAQ links
            content = re.sub(r'href="\.\./(faq\.html)"', 'href="/faq.html"', content)
            
            # Fix broken calculators/california link
            content = re.sub(r'href="/calculators/california/"', 'href="/#calculator"', content)
            
            # Add internal links between related articles
            if 'first-time' in str(blog_file):
                # Add links to other beginner guides
                if 'Related Guides' not in content and '</article>' in content:
                    related_section = '''
    <section class="mb-12" id="related-guides">
        <h2 class="text-2xl font-bold text-gray-900 mb-6">📚 Related Guides</h2>
        <div class="bg-white rounded-xl shadow-md p-6">
            <div class="grid md:grid-cols-2 gap-4">
                <div>
                    <h3 class="font-bold text-lg mb-3">Beginner Resources</h3>
                    <ul class="space-y-2 text-sm">
                        <li>• <a href="/blog/plasma-donation-process-step-by-step.html" class="text-blue-600 hover:text-blue-800">Step-by-Step Process Guide</a></li>
                        <li>• <a href="/blog/plasma-donation-tips-beginners.html" class="text-blue-600 hover:text-blue-800">Essential Tips for Beginners</a></li>
                        <li>• <a href="/blog/how-to-prepare-for-plasma-donation.html" class="text-blue-600 hover:text-blue-800">How to Prepare for Donation</a></li>
                        <li>• <a href="/blog/plasma-donation-requirements.html" class="text-blue-600 hover:text-blue-800">Complete Requirements Guide</a></li>
                    </ul>
                </div>
                <div>
                    <h3 class="font-bold text-lg mb-3">Maximize Your Earnings</h3>
                    <ul class="space-y-2 text-sm">
                        <li>• <a href="/blog/maximize-plasma-donation-earnings-2025.html" class="text-blue-600 hover:text-blue-800">Maximize Your Earnings Guide</a></li>
                        <li>• <a href="/blog/plasma-donation-bonuses-promotions.html" class="text-blue-600 hover:text-blue-800">Current Bonuses & Promotions</a></li>
                        <li>• <a href="/blog/highest-paying-plasma-centers-near-me.html" class="text-blue-600 hover:text-blue-800">Find Highest Paying Centers</a></li>
                        <li>• <a href="/blog/biolife-vs-csl-plasma-comparison-2025.html" class="text-blue-600 hover:text-blue-800">Compare Top Centers</a></li>
                    </ul>
                </div>
            </div>
        </div>
    </section>
'''
                    content = content.replace('</main>', related_section + '\n</main>')
            
            # Add related guides for earnings posts
            if 'earning' in str(blog_file).lower() or 'money' in str(blog_file).lower():
                if 'Related Guides' not in content and '</article>' in content:
                    related_section = '''
    <section class="mb-12" id="related-guides">
        <h2 class="text-2xl font-bold text-gray-900 mb-6">💰 Related Earnings Guides</h2>
        <div class="bg-white rounded-xl shadow-md p-6">
            <div class="grid md:grid-cols-2 gap-4">
                <div>
                    <h3 class="font-bold text-lg mb-3">Earnings Strategies</h3>
                    <ul class="space-y-2 text-sm">
                        <li>• <a href="/blog/maximize-plasma-donation-earnings-2025.html" class="text-blue-600 hover:text-blue-800">Maximize Your Earnings</a></li>
                        <li>• <a href="/blog/plasma-donation-bonuses-promotions.html" class="text-blue-600 hover:text-blue-800">Bonus Strategies</a></li>
                        <li>• <a href="/blog/plasma-donation-schedule.html" class="text-blue-600 hover:text-blue-800">Optimal Donation Schedule</a></li>
                        <li>• <a href="/blog/plasma-donation-referral-bonuses-2025.html" class="text-blue-600 hover:text-blue-800">Referral Income Guide</a></li>
                    </ul>
                </div>
                <div>
                    <h3 class="font-bold text-lg mb-3">Center Comparisons</h3>
                    <ul class="space-y-2 text-sm">
                        <li>• <a href="/blog/which-plasma-center-pays-most-money.html" class="text-blue-600 hover:text-blue-800">Highest Paying Centers</a></li>
                        <li>• <a href="/blog/csl-plasma-pay-rates-2025.html" class="text-blue-600 hover:text-blue-800">CSL Plasma Rates</a></li>
                        <li>• <a href="/blog/biolife-plasma-pay-chart-2025.html" class="text-blue-600 hover:text-blue-800">BioLife Pay Chart</a></li>
                        <li>• <a href="/blog/grifols-plasma-pay-calculator-2025.html" class="text-blue-600 hover:text-blue-800">Grifols Calculator</a></li>
                    </ul>
                </div>
            </div>
        </div>
    </section>
'''
                    content = content.replace('</main>', related_section + '\n</main>')
            
            # Add related guides for health posts
            if 'health' in str(blog_file).lower() or 'side-effect' in str(blog_file).lower() or 'safe' in str(blog_file).lower():
                if 'Related Guides' not in content and '</article>' in content:
                    related_section = '''
    <section class="mb-12" id="related-guides">
        <h2 class="text-2xl font-bold text-gray-900 mb-6">🏥 Related Health Guides</h2>
        <div class="bg-white rounded-xl shadow-md p-6">
            <div class="grid md:grid-cols-2 gap-4">
                <div>
                    <h3 class="font-bold text-lg mb-3">Health & Safety</h3>
                    <ul class="space-y-2 text-sm">
                        <li>• <a href="/blog/plasma-donation-side-effects-safety-2025.html" class="text-blue-600 hover:text-blue-800">Side Effects & Safety</a></li>
                        <li>• <a href="/blog/how-to-prepare-for-plasma-donation.html" class="text-blue-600 hover:text-blue-800">Preparation Guide</a></li>
                        <li>• <a href="/blog/plasma-donation-recovery-tips-complete-guide-2025.html" class="text-blue-600 hover:text-blue-800">Recovery Tips</a></li>
                        <li>• <a href="/blog/plasma-donation-nutrition-diet-optimization-2025.html" class="text-blue-600 hover:text-blue-800">Nutrition Guide</a></li>
                    </ul>
                </div>
                <div>
                    <h3 class="font-bold text-lg mb-3">Medical Requirements</h3>
                    <ul class="space-y-2 text-sm">
                        <li>• <a href="/blog/complete-medical-eligibility-guide-plasma-donation.html" class="text-blue-600 hover:text-blue-800">Medical Eligibility</a></li>
                        <li>• <a href="/blog/plasma-donation-weight-requirements.html" class="text-blue-600 hover:text-blue-800">Weight Requirements</a></li>
                        <li>• <a href="/blog/can-you-donate-plasma-with-tattoos.html" class="text-blue-600 hover:text-blue-800">Tattoo Guidelines</a></li>
                        <li>• <a href="/blog/plasma-donation-disqualifications-complete-list-2025.html" class="text-blue-600 hover:text-blue-800">Disqualifications List</a></li>
                    </ul>
                </div>
            </div>
        </div>
    </section>
'''
                    content = content.replace('</main>', related_section + '\n</main>')
            
            # Count fixes
            if content != original_content:
                files_fixed += 1
                fixes_made += len(re.findall(r'href="[^"]*"', original_content)) - len(re.findall(r'href="[^"]*"', content))
                
                # Write fixed content
                with open(blog_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                print(f"✅ Fixed: {blog_file.name}")
            
        except Exception as e:
            print(f"❌ Error processing {blog_file}: {e}")
    
    print(f"\n=== SUMMARY ===")
    print(f"Files processed: {len(blog_files)}")
    print(f"Files fixed: {files_fixed}")
    print(f"Total fixes: {fixes_made}")

if __name__ == "__main__":
    fix_internal_links()