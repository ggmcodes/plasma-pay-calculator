#!/usr/bin/env python3
import os
import re

# Template for health/recovery pages
health_card_template = """    <!-- Affiliate Disclosure -->
    <div class="bg-gray-50 p-3 mb-4 rounded-lg border border-gray-200 text-xs text-gray-600">
        <strong>Disclosure:</strong> This page contains affiliate links. We may earn a commission at no extra cost to you. We only recommend products that support donor health.
    </div>

    <!-- Essential Donor Health Products Card -->
    <div class="bg-gradient-to-r from-green-50 to-blue-50 rounded-xl shadow-lg p-6 mb-8 border border-green-200">
        <h3 class="text-xl font-bold text-gray-900 mb-4 flex items-center">
            <span class="text-2xl mr-2">💊</span>
            Essential Health Products for Donors
        </h3>
        <div class="grid md:grid-cols-2 gap-4">
            <div class="bg-white rounded-lg p-4 border border-gray-200">
                <h4 class="font-semibold text-gray-800 mb-2">Hydration & Recovery</h4>
                <ul class="space-y-2 text-sm">
                    <li>• <a href="https://amzn.to/4k4ju2B" target="_blank" rel="noopener nofollow" class="text-blue-600 hover:underline">Liquid IV Hydration Multiplier</a> - Faster recovery</li>
                    <li>• <a href="https://amzn.to/3HRCtjk" target="_blank" rel="noopener nofollow" class="text-blue-600 hover:underline">HydroFlask 32oz</a> - Stay hydrated all day</li>
                </ul>
            </div>
            <div class="bg-white rounded-lg p-4 border border-gray-200">
                <h4 class="font-semibold text-gray-800 mb-2">Nutrition Support</h4>
                <ul class="space-y-2 text-sm">
                    <li>• <a href="https://amzn.to/44mHHwl" target="_blank" rel="noopener nofollow" class="text-blue-600 hover:underline">Optimum Nutrition Protein</a> - Maintain protein levels</li>
                    <li>• <a href="https://amzn.to/4egbDhd" target="_blank" rel="noopener nofollow" class="text-blue-600 hover:underline">Iron Supplement</a> - Support healthy iron levels</li>
                </ul>
            </div>
        </div>
    </div>

"""

# Template for student pages
student_card_template = """    <!-- Affiliate Disclosure -->
    <div class="bg-gray-50 p-3 mb-4 rounded-lg border border-gray-200 text-xs text-gray-600">
        <strong>Disclosure:</strong> This page contains affiliate links. We may earn a commission at no extra cost to you. We only recommend products helpful for student donors.
    </div>

    <!-- Student Essentials Card -->
    <div class="bg-gradient-to-r from-purple-50 to-pink-50 rounded-xl shadow-lg p-6 mb-8 border border-purple-200">
        <h3 class="text-xl font-bold text-gray-900 mb-4 flex items-center">
            <span class="text-2xl mr-2">🎓</span>
            Student Donor Essentials
        </h3>
        <div class="grid md:grid-cols-2 gap-4">
            <div class="bg-white rounded-lg p-4 border border-gray-200">
                <h4 class="font-semibold text-gray-800 mb-2">Health & Energy</h4>
                <ul class="space-y-2 text-sm">
                    <li>• <a href="https://amzn.to/44cHUkD" target="_blank" rel="noopener nofollow" class="text-blue-600 hover:underline">Quest Protein Bars</a> - Quick nutrition</li>
                    <li>• <a href="https://amzn.to/4k4ju2B" target="_blank" rel="noopener nofollow" class="text-blue-600 hover:underline">Liquid IV</a> - Stay hydrated on campus</li>
                </ul>
            </div>
            <div class="bg-white rounded-lg p-4 border border-gray-200">
                <h4 class="font-semibold text-gray-800 mb-2">Extra Income</h4>
                <ul class="space-y-2 text-sm">
                    <li>• <a href="https://go.fiverr.com/visit/?bta=1134704&brand=fiverrmarketplace" target="_blank" rel="noopener nofollow" class="text-blue-600 hover:underline">Fiverr Freelancing</a> - Use your skills</li>
                    <li>• <a href="https://amzn.to/42uPTIK" target="_blank" rel="noopener nofollow" class="text-blue-600 hover:underline">Productivity Guide</a> - Balance studies & work</li>
                </ul>
            </div>
        </div>
    </div>

"""

# Template for first-time donor pages
first_time_card_template = """    <!-- Affiliate Disclosure -->
    <div class="bg-gray-50 p-3 mb-4 rounded-lg border border-gray-200 text-xs text-gray-600">
        <strong>Disclosure:</strong> This page contains affiliate links. We may earn a commission at no extra cost to you. We only recommend products helpful for new donors.
    </div>

    <!-- First-Time Donor Prep Kit Card -->
    <div class="bg-gradient-to-r from-blue-50 to-cyan-50 rounded-xl shadow-lg p-6 mb-8 border border-blue-200">
        <h3 class="text-xl font-bold text-gray-900 mb-4 flex items-center">
            <span class="text-2xl mr-2">🎯</span>
            First-Time Donor Prep Kit
        </h3>
        <div class="grid md:grid-cols-2 gap-4">
            <div class="bg-white rounded-lg p-4 border border-gray-200">
                <h4 class="font-semibold text-gray-800 mb-2">Before Your Visit</h4>
                <ul class="space-y-2 text-sm">
                    <li>• <a href="https://amzn.to/4k4ju2B" target="_blank" rel="noopener nofollow" class="text-blue-600 hover:underline">Liquid IV</a> - Pre-hydrate effectively</li>
                    <li>• <a href="https://amzn.to/4egbDhd" target="_blank" rel="noopener nofollow" class="text-blue-600 hover:underline">Iron Supplement</a> - Boost iron levels</li>
                </ul>
            </div>
            <div class="bg-white rounded-lg p-4 border border-gray-200">
                <h4 class="font-semibold text-gray-800 mb-2">Recovery Support</h4>
                <ul class="space-y-2 text-sm">
                    <li>• <a href="https://amzn.to/44mHHwl" target="_blank" rel="noopener nofollow" class="text-blue-600 hover:underline">Protein Powder</a> - Quick recovery</li>
                    <li>• <a href="https://amzn.to/40hZJxg" target="_blank" rel="noopener nofollow" class="text-blue-600 hover:underline">Compression Sleeves</a> - Arm comfort</li>
                </ul>
            </div>
        </div>
    </div>

"""

def add_affiliate_card(filepath, card_template, page_type):
    """Add affiliate card after the main heading if not already present"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Skip if already has affiliate disclosure
        if 'Affiliate Disclosure' in content or 'affiliate links' in content:
            return False
        
        # Find a good insertion point (after navigation, before main content)
        patterns = [
            r'(</nav>\s*\n\s*<!-- Main Content -->)',
            r'(</div>\s*\n\s*<!-- Main Content -->)',
            r'(<main[^>]*>\s*\n)',
            r'(<article[^>]*>\s*\n)',
        ]
        
        inserted = False
        for pattern in patterns:
            match = re.search(pattern, content)
            if match:
                # Insert after the matched pattern
                insert_pos = match.end()
                content = content[:insert_pos] + '\n' + card_template + content[insert_pos:]
                inserted = True
                break
        
        if not inserted:
            # Try to find h1 tag and insert after it
            h1_match = re.search(r'(<h1[^>]*>.*?</h1>\s*\n)', content)
            if h1_match:
                insert_pos = h1_match.end()
                content = content[:insert_pos] + '\n' + card_template + content[insert_pos:]
                inserted = True
        
        if inserted:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Added {page_type} card to: {os.path.basename(filepath)}")
            return True
        else:
            print(f"⚠️  Could not find insertion point in: {os.path.basename(filepath)}")
            return False
            
    except Exception as e:
        print(f"❌ Error processing {filepath}: {e}")
        return False

def main():
    base_dir = "/Users/glengomezmeade/Projects/plasma-pay-calculator"
    count = 5  # Already did 5 pages manually
    max_pages = 200
    
    # Process health/recovery pages
    health_keywords = ['health', 'recovery', 'nutrition', 'hydration', 'vein', 'iron', 'protein', 'diet', 'wellness']
    health_files = []
    
    for keyword in health_keywords:
        files = os.popen(f'find {base_dir}/blog -name "*{keyword}*.html" 2>/dev/null').read().strip().split('\n')
        health_files.extend([f for f in files if f and 'index.html' not in f])
    
    health_files = list(set(health_files))[:30]  # Limit to 30 health pages
    
    for filepath in health_files:
        if count >= max_pages:
            break
        if filepath and os.path.exists(filepath):
            if add_affiliate_card(filepath, health_card_template, "health"):
                count += 1
    
    print(f"\n📊 Progress: {count}/{max_pages} pages completed")
    
    # Process student pages
    student_keywords = ['student', 'college', 'university', 'campus']
    student_files = []
    
    for keyword in student_keywords:
        files = os.popen(f'find {base_dir}/blog -name "*{keyword}*.html" 2>/dev/null').read().strip().split('\n')
        student_files.extend([f for f in files if f and 'index.html' not in f])
    
    student_files = list(set(student_files))[:15]  # Limit to 15 student pages
    
    for filepath in student_files:
        if count >= max_pages:
            break
        if filepath and os.path.exists(filepath):
            if add_affiliate_card(filepath, student_card_template, "student"):
                count += 1
    
    print(f"\n📊 Progress: {count}/{max_pages} pages completed")
    
    # Process first-time donor pages
    first_time_keywords = ['first-time', 'beginner', 'new-donor', 'guide', 'start']
    first_time_files = []
    
    for keyword in first_time_keywords:
        files = os.popen(f'find {base_dir}/blog -name "*{keyword}*.html" 2>/dev/null').read().strip().split('\n')
        first_time_files.extend([f for f in files if f and 'index.html' not in f])
    
    first_time_files = list(set(first_time_files))[:15]  # Limit to 15 first-time pages
    
    for filepath in first_time_files:
        if count >= max_pages:
            break
        if filepath and os.path.exists(filepath):
            if add_affiliate_card(filepath, first_time_card_template, "first-time"):
                count += 1
    
    print(f"\n✅ Final count: {count}/{max_pages} pages with affiliate cards")

if __name__ == "__main__":
    main()