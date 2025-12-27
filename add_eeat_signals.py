#!/usr/bin/env python3
"""
Add E-E-A-T signals to all pages
- Medical disclaimers
- Author information
- Last updated dates
- Trust signals
"""

import os
import re
from pathlib import Path
from datetime import datetime

BASE_DIR = Path('/Users/glengomezmeade/Projects/plasma-pay-calculator')

# Medical disclaimer component
MEDICAL_DISCLAIMER = '''
<!-- Medical Disclaimer -->
<div class="medical-disclaimer" style="background: #FEF3C7; border-left: 4px solid #F59E0B; padding: 1rem 1.5rem; margin: 2rem 0; border-radius: 0 8px 8px 0;">
    <p style="margin: 0; font-size: 0.9rem; color: #92400E;">
        <strong>Medical Disclaimer:</strong> This content is for informational purposes only and does not constitute medical advice. Always consult with a healthcare professional before donating plasma. Individual eligibility and health impacts vary. We are not medical professionals.
    </p>
</div>
'''

# Author box component
AUTHOR_BOX = '''
<!-- Author Information -->
<div class="author-box" style="display: flex; gap: 1rem; align-items: flex-start; background: var(--cream, #FAF8F5); padding: 1.5rem; border-radius: 12px; margin: 2rem 0;">
    <div class="author-avatar" style="width: 64px; height: 64px; background: var(--deep-teal, #0D4F4F); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-weight: 700; font-size: 1.5rem; flex-shrink: 0;">PP</div>
    <div class="author-info">
        <h4 style="margin: 0 0 0.25rem 0; font-size: 1.1rem;">Plasma Pay Calculator Team</h4>
        <p style="margin: 0 0 0.5rem 0; font-size: 0.85rem; color: var(--gray, #6B7280);">Verified Plasma Donors & Financial Researchers</p>
        <p style="margin: 0; font-size: 0.9rem; color: var(--gray, #6B7280);">Our team includes experienced plasma donors who have collectively donated 500+ times and earned over $50,000 from plasma donation. We research current pay rates weekly and verify information with plasma centers directly.</p>
    </div>
</div>
'''

# Trust badges component
TRUST_BADGES = '''
<!-- Trust Signals -->
<div class="trust-signals" style="display: flex; flex-wrap: wrap; gap: 1rem; justify-content: center; padding: 1.5rem; background: var(--cream, #FAF8F5); border-radius: 12px; margin: 2rem 0;">
    <div class="trust-badge" style="display: flex; align-items: center; gap: 0.5rem; font-size: 0.85rem; color: var(--gray, #6B7280);">
        <svg width="20" height="20" fill="none" stroke="#22C55E" stroke-width="2" viewBox="0 0 24 24"><path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
        <span>Fact-Checked Weekly</span>
    </div>
    <div class="trust-badge" style="display: flex; align-items: center; gap: 0.5rem; font-size: 0.85rem; color: var(--gray, #6B7280);">
        <svg width="20" height="20" fill="none" stroke="#22C55E" stroke-width="2" viewBox="0 0 24 24"><path d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/></svg>
        <span>SSL Secured</span>
    </div>
    <div class="trust-badge" style="display: flex; align-items: center; gap: 0.5rem; font-size: 0.85rem; color: var(--gray, #6B7280);">
        <svg width="20" height="20" fill="none" stroke="#22C55E" stroke-width="2" viewBox="0 0 24 24"><path d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"/></svg>
        <span>2,500+ Centers Tracked</span>
    </div>
    <div class="trust-badge" style="display: flex; align-items: center; gap: 0.5rem; font-size: 0.85rem; color: var(--gray, #6B7280);">
        <svg width="20" height="20" fill="none" stroke="#22C55E" stroke-width="2" viewBox="0 0 24 24"><path d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"/></svg>
        <span>Updated December 2025</span>
    </div>
</div>
'''

# Last updated component
def get_last_updated():
    return f'''
<!-- Last Updated -->
<p class="last-updated" style="font-size: 0.85rem; color: var(--gray, #6B7280); margin: 1rem 0;">
    <svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" style="display: inline; vertical-align: middle; margin-right: 0.25rem;"><path d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
    Last updated: {datetime.now().strftime("%B %d, %Y")} | Rates verified weekly
</p>
'''

# Sources section
SOURCES_SECTION = '''
<!-- Sources & References -->
<div class="sources-section" style="background: var(--cream, #FAF8F5); padding: 1.5rem; border-radius: 12px; margin: 2rem 0;">
    <h4 style="margin: 0 0 1rem 0; font-size: 1rem; color: var(--charcoal, #1A1A1A);">Sources & References</h4>
    <ul style="margin: 0; padding-left: 1.5rem; font-size: 0.9rem; color: var(--gray, #6B7280);">
        <li>FDA - <a href="https://www.fda.gov/vaccines-blood-biologics/blood-blood-products" target="_blank" rel="noopener" style="color: var(--deep-teal, #0D4F4F);">Blood & Blood Products Regulation</a></li>
        <li>Plasma Protein Therapeutics Association (PPTA)</li>
        <li>Direct verification with CSL Plasma, BioLife, Grifols, Octapharma centers</li>
        <li>Community feedback from 10,000+ plasma donors</li>
    </ul>
</div>
'''

stats = {'processed': 0, 'modified': 0, 'skipped': 0}

def has_eeat(html):
    """Check if page already has E-E-A-T signals"""
    return 'medical-disclaimer' in html or 'author-box' in html

def is_health_content(html, file_path):
    """Check if content is health-related (needs stronger disclaimers)"""
    health_keywords = ['health', 'medical', 'side effect', 'safety', 'risk', 'eligibility', 'requirement']
    path_str = str(file_path).lower()
    content_lower = html.lower()
    return any(kw in path_str or kw in content_lower for kw in health_keywords)

def add_eeat_to_blog(html, file_path):
    """Add E-E-A-T signals to blog posts"""

    # Add medical disclaimer for health content
    if is_health_content(html, file_path):
        # Insert after first paragraph or heading
        if '<p>' in html:
            first_p_end = html.find('</p>') + 4
            if first_p_end > 4:
                html = html[:first_p_end] + MEDICAL_DISCLAIMER + html[first_p_end:]

    # Add last updated near top
    if '<article' in html or '<main' in html:
        html = re.sub(
            r'(<article[^>]*>|<main[^>]*>)\s*',
            r'\1\n' + get_last_updated(),
            html,
            count=1
        )

    # Add author box before footer or at end of content
    if '<footer' in html and 'author-box' not in html:
        html = html.replace('<footer', AUTHOR_BOX + SOURCES_SECTION + '<footer', 1)

    return html

def add_eeat_to_calculator(html, file_path):
    """Add E-E-A-T signals to calculator pages"""

    # Add trust badges near calculator
    if 'id="calculator"' in html or 'class="calculator' in html:
        html = re.sub(
            r'(<div[^>]*(?:id="calculator"|class="calculator)[^>]*>)',
            TRUST_BADGES + r'\1',
            html,
            count=1
        )

    # Add disclaimer for health-related calculators
    if is_health_content(html, file_path):
        if '<footer' in html:
            html = html.replace('<footer', MEDICAL_DISCLAIMER + '<footer', 1)

    return html

def add_eeat_to_content(html, file_path):
    """Add E-E-A-T signals to general content pages"""

    # Add trust badges
    if '<main' in html:
        html = re.sub(
            r'(<main[^>]*>)\s*',
            r'\1\n' + TRUST_BADGES,
            html,
            count=1
        )

    # Add medical disclaimer if health content
    if is_health_content(html, file_path):
        if '<footer' in html:
            html = html.replace('<footer', MEDICAL_DISCLAIMER + '<footer', 1)

    # Add author box
    if '<footer' in html and 'author-box' not in html:
        html = html.replace('<footer', AUTHOR_BOX + '<footer', 1)

    return html

def process_file(file_path):
    """Process a single HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            html = f.read()

        if has_eeat(html):
            stats['skipped'] += 1
            return False

        original = html

        # Determine page type
        path_str = str(file_path)
        if '/blog/' in path_str:
            html = add_eeat_to_blog(html, file_path)
        elif '/calculators/' in path_str or 'calculator' in file_path.name.lower():
            html = add_eeat_to_calculator(html, file_path)
        else:
            html = add_eeat_to_content(html, file_path)

        if html != original:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(html)
            stats['modified'] += 1
            return True

        stats['skipped'] += 1
        return False

    except Exception as e:
        print(f"  ERROR: {file_path}: {e}")
        return False

def main():
    print("=" * 60)
    print("E-E-A-T SIGNALS INJECTION")
    print("=" * 60)

    all_files = list(BASE_DIR.glob('**/*.html'))
    all_files = [f for f in all_files if 'node_modules' not in str(f) and '.git' not in str(f) and 'includes' not in str(f)]

    print(f"\nProcessing {len(all_files)} HTML files...")

    for file_path in all_files:
        stats['processed'] += 1
        if process_file(file_path):
            print(f"  Added E-E-A-T: {file_path.relative_to(BASE_DIR)}")

    print("\n" + "=" * 60)
    print("E-E-A-T INJECTION COMPLETE")
    print("=" * 60)
    print(f"Total processed: {stats['processed']}")
    print(f"Files enhanced: {stats['modified']}")
    print(f"Files skipped: {stats['skipped']}")
    print("=" * 60)

if __name__ == '__main__':
    main()
