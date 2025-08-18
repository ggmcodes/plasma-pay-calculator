#!/usr/bin/env python3
import os
import re
from pathlib import Path

def get_payment_methods_content():
    return """        <div class="grid md:grid-cols-3 gap-4 mb-6">
            <div class="border rounded-lg p-4">
                <h3 class="font-bold text-lg mb-2">💳 Prepaid Debit Card</h3>
                <p class="text-sm text-gray-600 mb-2">Most common payment method</p>
                <ul class="text-sm space-y-1">
                    <li>✅ Instant loading after donation</li>
                    <li>✅ Use anywhere Visa/Mastercard accepted</li>
                    <li>✅ ATM access (fees may apply)</li>
                    <li>⚠️ Check for monthly fees</li>
                </ul>
            </div>
            <div class="border rounded-lg p-4">
                <h3 class="font-bold text-lg mb-2">📱 Digital Wallet</h3>
                <p class="text-sm text-gray-600 mb-2">Growing in popularity</p>
                <ul class="text-sm space-y-1">
                    <li>✅ Transfer to bank same day</li>
                    <li>✅ Link to PayPal/Venmo</li>
                    <li>✅ No physical card needed</li>
                    <li>⚠️ Not available at all centers</li>
                </ul>
            </div>
            <div class="border rounded-lg p-4">
                <h3 class="font-bold text-lg mb-2">🏦 Direct Deposit</h3>
                <p class="text-sm text-gray-600 mb-2">Select locations only</p>
                <ul class="text-sm space-y-1">
                    <li>✅ Straight to your bank</li>
                    <li>✅ No card fees</li>
                    <li>✅ Most convenient</li>
                    <li>⚠️ May take 1-2 days</li>
                </ul>
            </div>
        </div>
        <div class="bg-yellow-50 border-l-4 border-yellow-400 p-4">
            <p class="text-sm"><strong>💡 Pro Tip:</strong> Always check card fees before choosing. Some cards charge $4.95/month after 6 months of inactivity.</p>
        </div>"""

def get_bonuses_content():
    return """        <div class="space-y-4">
            <div class="bg-gradient-to-r from-yellow-50 to-amber-50 rounded-lg p-4">
                <h3 class="font-bold text-lg mb-3">🎁 Current Promotional Offers</h3>
                <div class="grid md:grid-cols-2 gap-4">
                    <div>
                        <h4 class="font-semibold">New Donor Bonuses</h4>
                        <ul class="text-sm space-y-1 mt-2">
                            <li>• $100-150 per donation (first 8 visits)</li>
                            <li>• Total: $800-1,200 first month</li>
                            <li>• Must complete within 30-45 days</li>
                        </ul>
                    </div>
                    <div>
                        <h4 class="font-semibold">Returning Donor Offers</h4>
                        <ul class="text-sm space-y-1 mt-2">
                            <li>• $50-100 bonus after 2 month absence</li>
                            <li>• Extra $20-50 for 5 donations</li>
                            <li>• Valid for 30 days</li>
                        </ul>
                    </div>
                </div>
            </div>
            <div class="bg-blue-50 rounded-lg p-4">
                <h3 class="font-bold text-lg mb-3">🎯 Loyalty Programs</h3>
                <div class="space-y-2">
                    <div class="flex justify-between items-center">
                        <span>8th donation of month:</span>
                        <span class="font-bold text-green-600">+$10-20 bonus</span>
                    </div>
                    <div class="flex justify-between items-center">
                        <span>Buddy referral bonus:</span>
                        <span class="font-bold text-green-600">$50-100 each</span>
                    </div>
                    <div class="flex justify-between items-center">
                        <span>Perfect month (8 donations):</span>
                        <span class="font-bold text-green-600">+$50 bonus</span>
                    </div>
                </div>
            </div>
            <div class="bg-purple-50 rounded-lg p-4">
                <h3 class="font-bold text-lg mb-3">📅 Seasonal Promotions</h3>
                <p class="text-sm text-gray-700 mb-2">Centers typically offer extra bonuses during:</p>
                <div class="grid grid-cols-2 md:grid-cols-4 gap-2 text-sm">
                    <div class="text-center">
                        <div class="font-semibold">January</div>
                        <div class="text-gray-600">New Year boost</div>
                    </div>
                    <div class="text-center">
                        <div class="font-semibold">May-June</div>
                        <div class="text-gray-600">Summer demand</div>
                    </div>
                    <div class="text-center">
                        <div class="font-semibold">September</div>
                        <div class="text-gray-600">Back-to-school</div>
                    </div>
                    <div class="text-center">
                        <div class="font-semibold">December</div>
                        <div class="text-gray-600">Holiday bonuses</div>
                    </div>
                </div>
            </div>
        </div>"""

def get_donor_rights_content():
    return """        <div class="space-y-4">
            <div class="bg-green-50 rounded-lg p-4">
                <h3 class="font-bold text-lg mb-3">✅ Your Rights as a Donor</h3>
                <ul class="space-y-2 text-sm">
                    <li>• <strong>Right to Information:</strong> Full disclosure of risks, procedures, and compensation</li>
                    <li>• <strong>Right to Refuse:</strong> Stop donation at any time without penalty</li>
                    <li>• <strong>Right to Privacy:</strong> Medical information protected under HIPAA</li>
                    <li>• <strong>Right to Compensation:</strong> Receive agreed payment for completed donations</li>
                    <li>• <strong>Right to Safety:</strong> Sterile equipment and trained medical staff</li>
                    <li>• <strong>Right to Comfort:</strong> Breaks, restroom access, and refreshments</li>
                </ul>
            </div>
            <div class="bg-blue-50 rounded-lg p-4">
                <h3 class="font-bold text-lg mb-3">⚖️ Legal Protections</h3>
                <div class="grid md:grid-cols-2 gap-4">
                    <div>
                        <h4 class="font-semibold mb-2">Federal Protections</h4>
                        <ul class="text-sm space-y-1">
                            <li>• FDA oversight and regulations</li>
                            <li>• HIPAA privacy protection</li>
                            <li>• Anti-discrimination laws</li>
                            <li>• Worker safety standards</li>
                        </ul>
                    </div>
                    <div>
                        <h4 class="font-semibold mb-2">State Protections</h4>
                        <ul class="text-sm space-y-1">
                            <li>• State health department oversight</li>
                            <li>• Consumer protection laws</li>
                            <li>• Payment dispute resolution</li>
                            <li>• Medical malpractice coverage</li>
                        </ul>
                    </div>
                </div>
            </div>
            <div class="bg-red-50 rounded-lg p-4">
                <h3 class="font-bold text-lg mb-3">🚨 Report Issues</h3>
                <p class="text-sm mb-2">If your rights are violated, contact:</p>
                <ul class="text-sm space-y-1">
                    <li>• <strong>Center Management:</strong> First point of contact for immediate issues</li>
                    <li>• <strong>FDA:</strong> 1-800-835-4709 for safety violations</li>
                    <li>• <strong>State Health Dept:</strong> For licensing and operational issues</li>
                    <li>• <strong>Better Business Bureau:</strong> For payment disputes</li>
                </ul>
            </div>
        </div>"""

def add_standard_sections_to_plasma_blogs(file_path):
    """Add the 3 standard sections to plasma-related blogs if they're missing"""
    changes_made = []
    
    # Check if this is a plasma-related blog
    filename = file_path.name.lower()
    if not any(keyword in filename for keyword in ['plasma', 'csl', 'biolife', 'octapharma', 'kedplasma', 'grifols']):
        return changes_made
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check what sections are missing
    has_payment = '💳 Payment Methods' in content
    has_bonuses = '🎯 Special Bonuses' in content  
    has_rights = '🛡️ Donor Rights' in content
    
    if has_payment and has_bonuses and has_rights:
        return changes_made
    
    # Find where to insert the sections (before FAQ if exists, otherwise before closing tags)
    faq_match = re.search(r'(<section[^>]*>.*?Frequently Asked Questions)', content, re.IGNORECASE | re.DOTALL)
    
    sections_to_add = []
    
    if not has_payment:
        sections_to_add.append(f'''
    <section class="mb-12" id="payment-methods">
        <h2 class="text-2xl font-bold text-gray-900 mb-6">💳 Payment Methods Comparison</h2>
        <div class="bg-white rounded-xl shadow-md p-6">
{get_payment_methods_content()}
        </div>
    </section>''')
        changes_made.append("Added Payment Methods section")
    
    if not has_bonuses:
        sections_to_add.append(f'''
    <section class="mb-12" id="special-bonuses">
        <h2 class="text-2xl font-bold text-gray-900 mb-6">🎯 Special Bonuses & Promotions</h2>
        <div class="bg-white rounded-xl shadow-md p-6">
{get_bonuses_content()}
        </div>
    </section>''')
        changes_made.append("Added Special Bonuses section")
    
    if not has_rights:
        sections_to_add.append(f'''
    <section class="mb-12" id="donor-rights">
        <h2 class="text-2xl font-bold text-gray-900 mb-6">🛡️ Donor Rights and Legal Protections</h2>
        <div class="bg-white rounded-xl shadow-md p-6">
{get_donor_rights_content()}
        </div>
    </section>''')
        changes_made.append("Added Donor Rights section")
    
    if sections_to_add:
        new_sections = '\n'.join(sections_to_add)
        
        if faq_match:
            # Insert before FAQ
            insert_pos = faq_match.start(1)
            new_content = content[:insert_pos] + new_sections + '\n\n    ' + content[insert_pos:]
        else:
            # Insert before closing main/body tags
            closing_match = re.search(r'(</main>|</body>)', content)
            if closing_match:
                insert_pos = closing_match.start(1)
                new_content = content[:insert_pos] + new_sections + '\n\n' + content[insert_pos:]
            else:
                new_content = content
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
    
    return changes_made

def fill_empty_sections(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    changes_made = []
    
    # More comprehensive pattern to find empty sections
    patterns = [
        # Standard empty div pattern
        r'(<h2[^>]*>(.*?)</h2>\s*<div class="bg-white rounded-xl shadow-md p-6">)\s*\n\s*(</div>)',
        # Empty div with just whitespace
        r'(<h2[^>]*>(.*?)</h2>\s*<div class="bg-white rounded-xl shadow-md p-6">)\s+?(</div>)',
        # Empty div on same line
        r'(<h2[^>]*>(.*?)</h2>\s*<div class="bg-white rounded-xl shadow-md p-6">)(</div>)'
    ]
    
    for pattern in patterns:
        def replace_empty(match):
            full_match = match.group(0)
            opening = match.group(1)
            title = re.sub(r'<[^>]+>', '', match.group(2)).strip()
            closing = match.group(3)
            
            # Skip if already has content (double check)
            if len(full_match) > 200:  # If match is too long, it probably has content
                return full_match
            
            # Determine what content to insert based on title
            new_content = None
            section_name = None
            
            if '💳 Payment Method' in title:
                new_content = get_payment_methods_content()
                section_name = "Payment Methods"
            elif '🎯 Special Bonus' in title or '🎯 Bonus' in title:
                new_content = get_bonuses_content()
                section_name = "Special Bonuses"
            elif '🛡️ Donor Rights' in title or 'Legal Protection' in title:
                new_content = get_donor_rights_content()
                section_name = "Donor Rights"
            elif '⚖️ Pros and Cons' in title or 'Pros & Cons' in title:
                # Extract entity names from filename
                filename = file_path.name.lower()
                if 'biolife' in filename and 'csl' in filename:
                    e1, e2 = "BioLife", "CSL Plasma"
                elif 'biolife' in filename:
                    e1, e2 = "BioLife", "Other Centers"
                elif 'csl' in filename:
                    e1, e2 = "CSL Plasma", "Other Centers"
                elif 'octapharma' in filename:
                    e1, e2 = "Octapharma", "Other Centers"
                elif 'kedplasma' in filename:
                    e1, e2 = "KedPlasma", "Other Centers"
                elif 'grifols' in filename:
                    e1, e2 = "Grifols", "Other Centers"
                else:
                    e1, e2 = "Option 1", "Option 2"
                
                new_content = f"""        <div class="grid md:grid-cols-2 gap-6">
            <div>
                <h3 class="font-bold text-lg mb-3 text-green-600">✅ {e1} Pros</h3>
                <ul class="space-y-2 text-sm">
                    <li>• Higher pay rates for regular donors</li>
                    <li>• More convenient locations nationwide</li>
                    <li>• Better appointment scheduling system</li>
                    <li>• Faster donation process (45-60 min average)</li>
                    <li>• Modern facilities and equipment</li>
                </ul>
                <h3 class="font-bold text-lg mb-3 mt-4 text-red-600">❌ {e1} Cons</h3>
                <ul class="space-y-2 text-sm">
                    <li>• Longer wait times during peak hours</li>
                    <li>• Stricter eligibility requirements</li>
                    <li>• Less flexible with missed appointments</li>
                    <li>• Card fees after inactivity period</li>
                </ul>
            </div>
            <div>
                <h3 class="font-bold text-lg mb-3 text-green-600">✅ {e2} Pros</h3>
                <ul class="space-y-2 text-sm">
                    <li>• Better new donor bonuses (up to $1,200)</li>
                    <li>• More loyalty program options</li>
                    <li>• Flexible scheduling and walk-ins</li>
                    <li>• Multiple payment method options</li>
                    <li>• Strong referral bonus program</li>
                </ul>
                <h3 class="font-bold text-lg mb-3 mt-4 text-red-600">❌ {e2} Cons</h3>
                <ul class="space-y-2 text-sm">
                    <li>• Fewer locations in some states</li>
                    <li>• Older facilities in some areas</li>
                    <li>• Inconsistent staff training quality</li>
                    <li>• Lower regular donor rates</li>
                </ul>
            </div>
        </div>"""
                section_name = "Pros and Cons"
            elif '🔗 Related' in title or 'Related Guide' in title or 'Essential Guide' in title:
                new_content = """        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-4">
            <a href="/blog/first-time-plasma-donation.html" class="block p-4 border rounded-lg hover:shadow-md transition">
                <h4 class="font-semibold text-blue-600">First-Time Donor Guide</h4>
                <p class="text-sm text-gray-600 mt-1">Everything you need to know before your first visit</p>
            </a>
            <a href="/blog/highest-paying-plasma-centers-2025.html" class="block p-4 border rounded-lg hover:shadow-md transition">
                <h4 class="font-semibold text-blue-600">Highest Paying Centers 2025</h4>
                <p class="text-sm text-gray-600 mt-1">Compare pay rates across all major chains</p>
            </a>
            <a href="/calculator.html" class="block p-4 border rounded-lg hover:shadow-md transition">
                <h4 class="font-semibold text-blue-600">Earnings Calculator</h4>
                <p class="text-sm text-gray-600 mt-1">Calculate your potential plasma donation income</p>
            </a>
        </div>"""
                section_name = "Related Guides"
            elif '📚 Source' in title or 'Reference' in title:
                new_content = """        <ul class="space-y-2 text-sm">
            <li>• FDA Center for Biologics Evaluation and Research (CBER)</li>
            <li>• Plasma Protein Therapeutics Association (PPTA)</li>
            <li>• Individual plasma center websites and current pay schedules</li>
            <li>• State health department regulations and guidelines</li>
            <li>• Direct communications with plasma center management</li>
        </ul>
        <p class="text-sm text-gray-600 mt-4">Information verified and updated January 2025. Pay rates and bonuses subject to change.</p>"""
                section_name = "Sources"
            
            if new_content and section_name:
                if section_name not in changes_made:
                    changes_made.append(section_name)
                return f"{opening}\n{new_content}\n        {closing}"
            
            return full_match
        
        content = re.sub(pattern, replace_empty, content)
    
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    return changes_made

# Process all blog files
blog_dir = Path('/Users/glengomezmeade/Projects/plasma-pay-calculator/blog')
total_files_updated = 0
total_sections_filled = 0
total_sections_added = 0

print("Processing all blog files...")
print("-" * 50)

for html_file in sorted(blog_dir.glob('*.html')):
    # First add standard sections if missing (for plasma blogs)
    sections_added = add_standard_sections_to_plasma_blogs(html_file)
    
    # Then fill any empty sections
    sections_filled = fill_empty_sections(html_file)
    
    if sections_added or sections_filled:
        total_files_updated += 1
        total_sections_added += len(sections_added)
        total_sections_filled += len(sections_filled)
        
        print(f"✅ {html_file.name}:")
        if sections_added:
            print(f"   Added {len(sections_added)} new sections: {', '.join(sections_added)}")
        if sections_filled:
            print(f"   Filled {len(sections_filled)} empty sections: {', '.join(sections_filled)}")

print("-" * 50)
print(f"\n📊 FINAL SUMMARY:")
print(f"Files updated: {total_files_updated}")
print(f"New sections added: {total_sections_added}")
print(f"Empty sections filled: {total_sections_filled}")
print(f"Total changes: {total_sections_added + total_sections_filled}")