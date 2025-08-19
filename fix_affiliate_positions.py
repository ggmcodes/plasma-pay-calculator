#!/usr/bin/env python3
"""
Script to move affiliate cards to proper positions:
- Calculator pages: move to bottom (before </main>)
- Blog pages: move to after main content (before closing tags)
"""

import os
import re
import glob

def move_affiliate_card_in_calculator(file_path):
    """Move affiliate card from top to bottom of calculator pages"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to find affiliate cards
    affiliate_pattern = r'<!-- .*? Donor .*?Kit -->\s*<div style="background: linear-gradient.*?</div>\s*</div>\s*\n'
    
    # Find the affiliate card
    match = re.search(affiliate_pattern, content, re.DOTALL)
    if not match:
        print(f"No affiliate card found in {file_path}")
        return False
    
    affiliate_card = match.group(0)
    
    # Remove the card from its current position
    content = content.replace(affiliate_card, '')
    
    # Insert before </main>
    if '</main>' in content:
        content = content.replace('</main>', f'\n{affiliate_card.strip()}\n\n</main>')
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Moved affiliate card in {file_path}")
        return True
    else:
        print(f"No </main> found in {file_path}")
        return False

def move_affiliate_card_in_blog(file_path):
    """Move affiliate card to after main content in blog pages"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to find affiliate cards that might be at the top
    affiliate_pattern = r'<!-- .*? Success Kit -->\s*<div.*?class=".*?gradient.*?</div>\s*</div>\s*'
    
    # Find the affiliate card
    match = re.search(affiliate_pattern, content, re.DOTALL)
    if not match:
        print(f"No affiliate card found at top of {file_path}")
        return False
    
    affiliate_card = match.group(0)
    
    # Remove the card from its current position if it's near the top
    if content.find(affiliate_card) < 2000:  # If card is in first 2000 chars (likely at top)
        content = content.replace(affiliate_card, '')
        
        # Insert before closing article tag or before back to blog section
        if '<!-- Back to Blog -->' in content:
            content = content.replace('<!-- Back to Blog -->', f'{affiliate_card.strip()}\n\n    <!-- Back to Blog -->')
        elif '</article>' in content:
            content = content.replace('</article>', f'</article>\n\n{affiliate_card.strip()}')
        elif '</main>' in content:
            content = content.replace('</main>', f'{affiliate_card.strip()}\n\n</main>')
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Moved affiliate card in {file_path}")
        return True
    
    return False

def main():
    base_path = "/Users/glengomezmeade/Projects/plasma-pay-calculator"
    
    # Fix calculator pages
    print("Fixing calculator pages...")
    calculator_pages = glob.glob(f"{base_path}/calculators/*/index.html")
    calculator_pages.extend(glob.glob(f"{base_path}/calculators/*/*/index.html"))
    
    for page in calculator_pages:
        move_affiliate_card_in_calculator(page)
    
    # Fix blog pages
    print("\nFixing blog pages...")
    blog_pages = glob.glob(f"{base_path}/blog/*.html")
    
    for page in blog_pages:
        move_affiliate_card_in_blog(page)
    
    print("\nDone!")

if __name__ == "__main__":
    main()