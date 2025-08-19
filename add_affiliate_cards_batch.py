#!/usr/bin/env python3
import os
import re

# Theme configurations
THEMES = {
    'green': {
        'bg_gradient': 'from-green-50 to-emerald-50',
        'header_color': '#059669',
        'hover_bg': '#ecfdf5',
        'disclosure_bg': 'rgba(5, 150, 105, 0.1)',
        'disclosure_border': 'rgba(5, 150, 105, 0.2)',
        'disclosure_color': '#059669'
    },
    'red': {
        'bg_gradient': 'from-red-50 to-rose-50',
        'header_color': '#dc2626',
        'hover_bg': '#fef2f2',
        'disclosure_bg': 'rgba(220, 38, 38, 0.1)',
        'disclosure_border': 'rgba(220, 38, 38, 0.2)',
        'disclosure_color': '#dc2626'
    },
    'blue': {
        'bg_gradient': 'from-blue-50 to-indigo-50',
        'header_color': '#2563eb',
        'hover_bg': '#eff6ff',
        'disclosure_bg': 'rgba(37, 99, 235, 0.1)',
        'disclosure_border': 'rgba(37, 99, 235, 0.2)',
        'disclosure_color': '#2563eb'
    },
    'yellow': {
        'bg_gradient': 'from-yellow-50 to-amber-50',
        'header_color': '#d97706',
        'hover_bg': '#fffbeb',
        'disclosure_bg': 'rgba(217, 119, 6, 0.1)',
        'disclosure_border': 'rgba(217, 119, 6, 0.2)',
        'disclosure_color': '#d97706'
    },
    'gold': {
        'bg_gradient': 'from-yellow-50 to-yellow-100',
        'header_color': '#ca8a04',
        'hover_bg': '#fefce8',
        'disclosure_bg': 'rgba(202, 138, 4, 0.1)',
        'disclosure_border': 'rgba(202, 138, 4, 0.2)',
        'disclosure_color': '#ca8a04'
    }
}

def create_affiliate_section(city_name, theme):
    theme_config = THEMES[theme]
    
    return f'''<!-- Affiliate Cards Section - {theme.title()} Theme -->
<section class="py-16 bg-gradient-to-br {theme_config['bg_gradient']}">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 class="text-3xl font-bold text-center text-gray-900 mb-12">
            🛍️ Essential Items for Plasma Donors in {city_name}
        </h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 24px; margin-bottom: 30px;">
            <!-- Health & Recovery -->
            <div style="background: white; border-radius: 12px; padding: 24px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
                <h3 style="color: {theme_config['header_color']}; font-size: 24px; margin-bottom: 16px; display: flex; align-items: center;">
                    💊 Health & Recovery
                </h3>
                <ul style="list-style: none; padding: 0; margin: 0;">
                    <li style="margin-bottom: 12px;">
                        <a href="https://www.amazon.com/dp/B000QSNYGI?tag=plasmadonor-20" target="_blank" rel="noopener nofollow" style="color: #333; text-decoration: none; display: flex; align-items: center; padding: 8px; border-radius: 6px; transition: background 0.3s;" onmouseover="this.style.background='{theme_config['hover_bg']}'" onmouseout="this.style.background='transparent'">
                            <span style="margin-right: 8px;">🏃</span>
                            <span>Electrolyte Powder - Rapid Recovery</span>
                        </a>
                    </li>
                    <li style="margin-bottom: 12px;">
                        <a href="https://www.amazon.com/dp/B00XPTFY4W?tag=plasmadonor-20" target="_blank" rel="noopener nofollow" style="color: #333; text-decoration: none; display: flex; align-items: center; padding: 8px; border-radius: 6px; transition: background 0.3s;" onmouseover="this.style.background='{theme_config['hover_bg']}'" onmouseout="this.style.background='transparent'">
                            <span style="margin-right: 8px;">💪</span>
                            <span>Iron Supplement - Stay Eligible</span>
                        </a>
                    </li>
                    <li style="margin-bottom: 12px;">
                        <a href="https://www.amazon.com/dp/B0B8C4H1N4?tag=plasmadonor-20" target="_blank" rel="noopener nofollow" style="color: #333; text-decoration: none; display: flex; align-items: center; padding: 8px; border-radius: 6px; transition: background 0.3s;" onmouseover="this.style.background='{theme_config['hover_bg']}'" onmouseout="this.style.background='transparent'">
                            <span style="margin-right: 8px;">🥤</span>
                            <span>Premium Protein Shakes</span>
                        </a>
                    </li>
                </ul>
            </div>
            <!-- Energy & Comfort -->
            <div style="background: white; border-radius: 12px; padding: 24px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
                <h3 style="color: {theme_config['header_color']}; font-size: 24px; margin-bottom: 16px; display: flex; align-items: center;">
                    ⚡ Energy & Comfort
                </h3>
                <ul style="list-style: none; padding: 0; margin: 0;">
                    <li style="margin-bottom: 12px;">
                        <a href="https://www.amazon.com/dp/B07YNSKBX4?tag=plasmadonor-20" target="_blank" rel="noopener nofollow" style="color: #333; text-decoration: none; display: flex; align-items: center; padding: 8px; border-radius: 6px; transition: background 0.3s;" onmouseover="this.style.background='{theme_config['hover_bg']}'" onmouseout="this.style.background='transparent'">
                            <span style="margin-right: 8px;">🎧</span>
                            <span>Noise-Canceling Earbuds</span>
                        </a>
                    </li>
                    <li style="margin-bottom: 12px;">
                        <a href="https://www.amazon.com/dp/B08KY684PB?tag=plasmadonor-20" target="_blank" rel="noopener nofollow" style="color: #333; text-decoration: none; display: flex; align-items: center; padding: 8px; border-radius: 6px; transition: background 0.3s;" onmouseover="this.style.background='{theme_config['hover_bg']}'" onmouseout="this.style.background='transparent'">
                            <span style="margin-right: 8px;">☕</span>
                            <span>Insulated Water Bottle</span>
                        </a>
                    </li>
                    <li style="margin-bottom: 12px;">
                        <a href="https://www.amazon.com/dp/B08GLX7TNT?tag=plasmadonor-20" target="_blank" rel="noopener nofollow" style="color: #333; text-decoration: none; display: flex; align-items: center; padding: 8px; border-radius: 6px; transition: background 0.3s;" onmouseover="this.style.background='{theme_config['hover_bg']}'" onmouseout="this.style.background='transparent'">
                            <span style="margin-right: 8px;">🔋</span>
                            <span>Portable Phone Charger</span>
                        </a>
                    </li>
                </ul>
            </div>
            <!-- Income & Savings -->
            <div style="background: white; border-radius: 12px; padding: 24px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
                <h3 style="color: {theme_config['header_color']}; font-size: 24px; margin-bottom: 16px; display: flex; align-items: center;">
                    💰 Income & Savings
                </h3>
                <ul style="list-style: none; padding: 0; margin: 0;">
                    <li style="margin-bottom: 12px;">
                        <a href="https://www.amazon.com/dp/B078GBQHG3?tag=plasmadonor-20" target="_blank" rel="noopener nofollow" style="color: #333; text-decoration: none; display: flex; align-items: center; padding: 8px; border-radius: 6px; transition: background 0.3s;" onmouseover="this.style.background='{theme_config['hover_bg']}'" onmouseout="this.style.background='transparent'">
                            <span style="margin-right: 8px;">📊</span>
                            <span>Budget Planner Notebook</span>
                        </a>
                    </li>
                    <li style="margin-bottom: 12px;">
                        <a href="https://www.amazon.com/dp/B07Q2X5VF3?tag=plasmadonor-20" target="_blank" rel="noopener nofollow" style="color: #333; text-decoration: none; display: flex; align-items: center; padding: 8px; border-radius: 6px; transition: background 0.3s;" onmouseover="this.style.background='{theme_config['hover_bg']}'" onmouseout="this.style.background='transparent'">
                            <span style="margin-right: 8px;">💳</span>
                            <span>RFID Blocking Wallet</span>
                        </a>
                    </li>
                    <li style="margin-bottom: 12px;">
                        <a href="https://www.amazon.com/dp/B08N5WRWNW?tag=plasmadonor-20" target="_blank" rel="noopener nofollow" style="color: #333; text-decoration: none; display: flex; align-items: center; padding: 8px; border-radius: 6px; transition: background 0.3s;" onmouseover="this.style.background='{theme_config['hover_bg']}'" onmouseout="this.style.background='transparent'">
                            <span style="margin-right: 8px;">📱</span>
                            <span>Expense Tracking Apps Guide</span>
                        </a>
                    </li>
                </ul>
            </div>
        </div>
        <div style="text-align: center; background: {theme_config['disclosure_bg']}; padding: 20px; border-radius: 12px; border: 2px solid {theme_config['disclosure_border']};">
            <p style="color: {theme_config['disclosure_color']}; font-size: 14px; margin: 0;">
                <strong>🔗 Affiliate Disclosure:</strong> We earn from qualifying purchases at no extra cost to you. 
                These products can help optimize your plasma donation experience in {city_name}.
            </p>
        </div>
    </div>
</section>

'''

# Define cities and their themes
cities_to_update = [
    # Indiana (Red theme) - remaining 4 cities
    ('/Users/glengomezmeade/Projects/plasma-pay-calculator/calculators/indiana/fort-wayne/index.html', 'Fort Wayne', 'red'),
    ('/Users/glengomezmeade/Projects/plasma-pay-calculator/calculators/indiana/evansville/index.html', 'Evansville', 'red'),
    ('/Users/glengomezmeade/Projects/plasma-pay-calculator/calculators/indiana/south-bend/index.html', 'South Bend', 'red'),
    ('/Users/glengomezmeade/Projects/plasma-pay-calculator/calculators/indiana/carmel/index.html', 'Carmel', 'red'),
    
    # Washington (Green theme) - 5 cities
    ('/Users/glengomezmeade/Projects/plasma-pay-calculator/calculators/washington/seattle/index.html', 'Seattle', 'green'),
    ('/Users/glengomezmeade/Projects/plasma-pay-calculator/calculators/washington/spokane/index.html', 'Spokane', 'green'),
    ('/Users/glengomezmeade/Projects/plasma-pay-calculator/calculators/washington/tacoma/index.html', 'Tacoma', 'green'),
    ('/Users/glengomezmeade/Projects/plasma-pay-calculator/calculators/washington/vancouver/index.html', 'Vancouver', 'green'),
    ('/Users/glengomezmeade/Projects/plasma-pay-calculator/calculators/washington/bellevue/index.html', 'Bellevue', 'green'),
]

def update_city_page(file_path, city_name, theme):
    """Update a single city page with affiliate cards"""
    try:
        # Read the file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Create the affiliate section
        affiliate_section = create_affiliate_section(city_name, theme)
        
        # Pattern to find where to insert (before AdSense Ad Slot 2)
        pattern = r'<!-- AdSense Ad Slot 2 -->\s*<section class="py-6 bg-white">\s*<div class="max-w-4xl mx-auto px-4 text-center">\s*<ins class="adsbygoogle"[^>]*></ins>\s*</div>\s*</section>'
        
        # Replacement with affiliate section before AdSense
        replacement = affiliate_section + '''<!-- AdSense Ad Slot 2 -->
<section class="py-6 bg-white">
<div class="max-w-4xl mx-auto px-4 text-center">
<ins class="adsbygoogle" data-ad-client="ca-pub-3180649272238451" data-ad-format="auto" data-ad-slot="9876543210" data-full-width-responsive="true" style="display:block"></ins>
</div>
</section>'''
        
        # Perform the replacement
        new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        
        # If no match found, try alternative pattern (simple donor success tips)
        if new_content == content:
            donor_pattern = r'<!-- City Page\s+Section -->\s*<section class="py-8 bg-blue-50">.*?</section>'
            if re.search(donor_pattern, content, re.DOTALL):
                new_content = re.sub(donor_pattern, affiliate_section.rstrip(), content, flags=re.DOTALL)
        
        # Write back to file if changes were made
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✅ Updated {city_name} with {theme} theme")
            return True
        else:
            print(f"⚠️  No changes made to {city_name} - pattern not found")
            return False
            
    except Exception as e:
        print(f"❌ Error updating {city_name}: {str(e)}")
        return False

def main():
    print("🚀 Starting batch update of affiliate cards...")
    
    updated_count = 0
    for file_path, city_name, theme in cities_to_update:
        if os.path.exists(file_path):
            if update_city_page(file_path, city_name, theme):
                updated_count += 1
        else:
            print(f"❌ File not found: {file_path}")
    
    print(f"\n📊 Summary: Updated {updated_count}/{len(cities_to_update)} cities")

if __name__ == "__main__":
    main()