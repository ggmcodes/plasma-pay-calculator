#!/usr/bin/env python3
"""
Fix the final 20 broken internal links to achieve 100% success rate.
"""

import os
from pathlib import Path

class FinalLinkFixer:
    def __init__(self, base_dir):
        self.base_dir = Path(base_dir)
        self.fixes_applied = 0
    
    def fix_california_blog_links(self):
        """Fix broken links in California blog index by redirecting to existing content"""
        
        # Map broken links to existing content
        california_fixes = {
            "california-plasma-donation-earnings-calculator.html": "../california-plasma-donation-pay-rates-complete-guide-2025.html",
            "california-plasma-donation-income-tax-deductions.html": "../california-tech-irs-plasma-tracking.html",
            "california-plasma-donation-budget-planning.html": "../california-plasma-donation-maximize-earnings.html",
            "california-plasma-donation-financial-planning.html": "../california-plasma-donation-maximize-earnings.html",
            "california-plasma-donation-health-benefits.html": "../california-plasma-donation-side-effects-safety.html",
            "california-plasma-donation-eligibility-requirements.html": "california-plasma-donation-requirements-eligibility.html",
            "california-plasma-donation-side-effects.html": "california-plasma-donation-side-effects-safety.html",
            "california-plasma-donation-recovery-tips.html": "../california-vein-health-plasma-donation.html",
            "california-plasma-donation-preparation-guide.html": "../first-time-plasma-donation.html",
            "california-plasma-donation-bay-area.html": "california-plasma-donation-los-angeles-san-diego.html",
            "california-plasma-donation-san-francisco.html": "california-plasma-donation-los-angeles-san-diego.html",
            "california-plasma-donation-sacramento.html": "california-plasma-donation-los-angeles-san-diego.html",
            "california-plasma-donation-fresno.html": "california-plasma-donation-los-angeles-san-diego.html",
            "california-plasma-donation-center-comparison.html": "../california-plasma-donation-pay-rates-complete-guide-2025.html",
            "california-plasma-donation-first-time-guide.html": "first-time-plasma-donation.html",
            "california-plasma-donation-what-to-expect.html": "first-time-plasma-donation.html",
            "california-plasma-donation-tips-for-beginners.html": "../first-time-plasma-donation.html",
            "california-plasma-donation-myths-debunked.html": "ultimate-plasma-donation-guide.html"
        }
        
        california_index_path = self.base_dir / "blog" / "california" / "index.html"
        
        if california_index_path.exists():
            with open(california_index_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            updated_content = content
            for broken_link, replacement_link in california_fixes.items():
                original_href = f'href="{broken_link}"'
                new_href = f'href="{replacement_link}"'
                
                if original_href in updated_content:
                    updated_content = updated_content.replace(original_href, new_href)
                    self.fixes_applied += 1
                    print(f"Fixed {broken_link} → {replacement_link}")
            
            if updated_content != content:
                with open(california_index_path, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                print(f"Updated {california_index_path}")
        
        # Fix the specific broken link in california-plasma-donation-los-angeles-san-diego.html
        la_sd_file = self.base_dir / "blog" / "california" / "california-plasma-donation-los-angeles-san-diego.html"
        if la_sd_file.exists():
            with open(la_sd_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Replace broken link with existing content
            updated_content = content.replace(
                'href="california-plasma-donation-center-comparison.html"',
                'href="../california-plasma-donation-pay-rates-complete-guide-2025.html"'
            )
            
            if updated_content != content:
                with open(la_sd_file, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                self.fixes_applied += 1
                print(f"Fixed california-plasma-donation-center-comparison.html link")
    
    def fix_calculators_blog_link(self):
        """Fix broken blog/ link in calculators index"""
        calculators_index = self.base_dir / "calculators" / "index.html"
        
        if calculators_index.exists():
            with open(calculators_index, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Replace blog/ with /blog/
            updated_content = content.replace('href="blog/"', 'href="/blog/"')
            
            if updated_content != content:
                with open(calculators_index, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                self.fixes_applied += 1
                print("Fixed blog/ link in calculators index")
    
    def run_final_fixes(self):
        """Run all final fixes"""
        print("Applying final fixes for remaining 20 broken links...")
        
        # Fix California blog links
        self.fix_california_blog_links()
        
        # Fix calculators blog link
        self.fix_calculators_blog_link()
        
        print(f"\nTotal final fixes applied: {self.fixes_applied}")
        return self.fixes_applied

if __name__ == "__main__":
    base_directory = "/Users/glengomezmeade/Projects/plasma-pay-calculator"
    fixer = FinalLinkFixer(base_directory)
    fixer.run_final_fixes()