#!/usr/bin/env python3
"""
Comprehensive script to fix broken internal links in the plasma-pay-calculator website.

This script addresses the main broken link patterns found in the audit:
1. /state/* links -> /calculators/*
2. /health/ links -> appropriate alternatives
3. City-specific donation page links -> /calculators/state/city/
4. /calculator/ links -> /calculators/ (add 's')
5. Blog post links to non-existent content

Usage: python fix_broken_internal_links.py [--dry-run] [--verbose]
"""

import os
import re
import argparse
from pathlib import Path
from typing import Dict, List, Tuple
import json

class LinkFixer:
    def __init__(self, root_dir: str, dry_run: bool = False, verbose: bool = False):
        self.root_dir = Path(root_dir)
        self.dry_run = dry_run
        self.verbose = verbose
        self.fixes_made = []
        self.stats = {
            'files_processed': 0,
            'state_links_fixed': 0,
            'health_links_fixed': 0,
            'city_links_fixed': 0,
            'calculator_links_fixed': 0,
            'total_fixes': 0
        }
        
        # Define link replacement patterns
        self.link_patterns = [
            # Pattern 1: /state/statename/cityname.html -> /calculators/statename/cityname/
            {
                'pattern': r'/state/([^/]+)/([^/.]+)\.html',
                'replacement': r'/calculators/\1/\2/',
                'description': 'state links to calculators',
                'stat_key': 'state_links_fixed'
            },
            
            # Pattern 2: /calculator/ -> /calculators/ (singular to plural)
            {
                'pattern': r'/calculator/',
                'replacement': r'/calculators/',
                'description': 'calculator to calculators',
                'stat_key': 'calculator_links_fixed'
            },
            
            # Pattern 3: /health/ -> /topics/requirements-eligibility/
            {
                'pattern': r'/health/',
                'replacement': r'/topics/requirements-eligibility/',
                'description': 'health to requirements-eligibility',
                'stat_key': 'health_links_fixed'
            },
            
            # Pattern 4: Specific city donation pages
            {
                'pattern': r'/frederick-md-plasma-donation\.html',
                'replacement': r'/calculators/maryland/frederick/',
                'description': 'Frederick MD donation page',
                'stat_key': 'city_links_fixed'
            },
            {
                'pattern': r'/lowell-ma-plasma-donation\.html',
                'replacement': r'/calculators/massachusetts/lowell/',
                'description': 'Lowell MA donation page',
                'stat_key': 'city_links_fixed'
            },
            
            # Pattern 5: Other common city patterns (if they exist)
            {
                'pattern': r'/([a-z-]+)-([a-z]{2})-plasma-donation\.html',
                'replacement': self._city_replacement_helper,
                'description': 'generic city donation pages',
                'stat_key': 'city_links_fixed'
            }
        ]
        
        # State abbreviation mappings
        self.state_mappings = {
            'al': 'alabama', 'ak': 'alaska', 'az': 'arizona', 'ar': 'arkansas', 'ca': 'california',
            'co': 'colorado', 'ct': 'connecticut', 'de': 'delaware', 'fl': 'florida', 'ga': 'georgia',
            'hi': 'hawaii', 'id': 'idaho', 'il': 'illinois', 'in': 'indiana', 'ia': 'iowa',
            'ks': 'kansas', 'ky': 'kentucky', 'la': 'louisiana', 'me': 'maine', 'md': 'maryland',
            'ma': 'massachusetts', 'mi': 'michigan', 'mn': 'minnesota', 'ms': 'mississippi',
            'mo': 'missouri', 'mt': 'montana', 'ne': 'nebraska', 'nv': 'nevada', 'nh': 'new-hampshire',
            'nj': 'new-jersey', 'nm': 'new-mexico', 'ny': 'new-york', 'nc': 'north-carolina',
            'nd': 'north-dakota', 'oh': 'ohio', 'ok': 'oklahoma', 'or': 'oregon', 'pa': 'pennsylvania',
            'ri': 'rhode-island', 'sc': 'south-carolina', 'sd': 'south-dakota', 'tn': 'tennessee',
            'tx': 'texas', 'ut': 'utah', 'vt': 'vermont', 'va': 'virginia', 'wa': 'washington',
            'wv': 'west-virginia', 'wi': 'wisconsin', 'wy': 'wyoming', 'dc': 'district-of-columbia'
        }

    def _city_replacement_helper(self, match):
        """Helper function for city pattern replacement"""
        city = match.group(1)
        state_abbr = match.group(2).lower()
        
        if state_abbr in self.state_mappings:
            state_name = self.state_mappings[state_abbr]
            # Check if the calculator page exists
            calculator_path = self.root_dir / 'calculators' / state_name / city / 'index.html'
            if calculator_path.exists():
                return f'/calculators/{state_name}/{city}/'
        
        # Fallback: return original if we can't map it
        return match.group(0)

    def process_file(self, file_path: Path) -> bool:
        """Process a single HTML file and apply link fixes"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            file_fixes = []
            
            # Apply each pattern
            for pattern_info in self.link_patterns:
                pattern = pattern_info['pattern']
                replacement = pattern_info['replacement']
                description = pattern_info['description']
                stat_key = pattern_info['stat_key']
                
                if callable(replacement):
                    # Handle function-based replacements
                    matches = list(re.finditer(pattern, content))
                    for match in reversed(matches):  # Process in reverse to maintain positions
                        new_link = replacement(match)
                        if new_link != match.group(0):
                            content = content[:match.start()] + new_link + content[match.end():]
                            file_fixes.append({
                                'pattern': description,
                                'old': match.group(0),
                                'new': new_link,
                                'position': match.start()
                            })
                            self.stats[stat_key] += 1
                else:
                    # Handle regex replacements
                    new_content, num_subs = re.subn(pattern, replacement, content)
                    if num_subs > 0:
                        matches = re.finditer(pattern, original_content)
                        for match in matches:
                            file_fixes.append({
                                'pattern': description,
                                'old': match.group(0),
                                'new': re.sub(pattern, replacement, match.group(0)),
                                'position': match.start()
                            })
                        content = new_content
                        self.stats[stat_key] += num_subs
            
            # Write the file if changes were made and not in dry-run mode
            if content != original_content:
                if not self.dry_run:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                
                self.fixes_made.append({
                    'file': str(file_path.relative_to(self.root_dir)),
                    'fixes': file_fixes
                })
                
                if self.verbose:
                    print(f"Fixed {len(file_fixes)} link(s) in {file_path.relative_to(self.root_dir)}")
                
                return True
            
            return False
            
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            return False

    def find_html_files(self) -> List[Path]:
        """Find all HTML files in the website"""
        html_files = []
        
        # Process main HTML files
        for pattern in ['*.html', '**/*.html']:
            html_files.extend(self.root_dir.glob(pattern))
        
        # Filter out certain directories that shouldn't be processed
        excluded_patterns = ['node_modules', '.git', '__pycache__']
        filtered_files = []
        
        for file_path in html_files:
            skip_file = False
            for excluded in excluded_patterns:
                if excluded in str(file_path):
                    skip_file = True
                    break
            if not skip_file:
                filtered_files.append(file_path)
        
        return sorted(filtered_files)

    def run(self):
        """Main execution method"""
        print(f"Starting link fix process in {'DRY RUN' if self.dry_run else 'LIVE'} mode...")
        print(f"Root directory: {self.root_dir}")
        
        html_files = self.find_html_files()
        print(f"Found {len(html_files)} HTML files to process")
        
        files_modified = 0
        
        for file_path in html_files:
            self.stats['files_processed'] += 1
            if self.process_file(file_path):
                files_modified += 1
        
        # Calculate total fixes
        self.stats['total_fixes'] = sum(
            self.stats[key] for key in self.stats if key.endswith('_fixed')
        )
        
        # Print summary
        print("\n" + "="*60)
        print("LINK FIX SUMMARY")
        print("="*60)
        print(f"Files processed: {self.stats['files_processed']}")
        print(f"Files modified: {files_modified}")
        print(f"State links fixed: {self.stats['state_links_fixed']}")
        print(f"Health links fixed: {self.stats['health_links_fixed']}")
        print(f"City-specific links fixed: {self.stats['city_links_fixed']}")
        print(f"Calculator links fixed: {self.stats['calculator_links_fixed']}")
        print(f"Total fixes applied: {self.stats['total_fixes']}")
        
        if self.dry_run:
            print("\nNOTE: This was a DRY RUN - no files were actually modified.")
        
        # Save detailed report
        report_file = self.root_dir / f"link_fix_report{'_dry_run' if self.dry_run else ''}.json"
        with open(report_file, 'w') as f:
            json.dump({
                'stats': self.stats,
                'fixes_made': self.fixes_made
            }, f, indent=2)
        
        print(f"\nDetailed report saved to: {report_file}")

def main():
    parser = argparse.ArgumentParser(description='Fix broken internal links in plasma-pay-calculator website')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be changed without making changes')
    parser.add_argument('--verbose', '-v', action='store_true', help='Show detailed output')
    parser.add_argument('--root-dir', default='.', help='Root directory of the website (default: current directory)')
    
    args = parser.parse_args()
    
    root_dir = Path(args.root_dir).resolve()
    if not root_dir.exists():
        print(f"Error: Root directory {root_dir} does not exist")
        return 1
    
    fixer = LinkFixer(root_dir, dry_run=args.dry_run, verbose=args.verbose)
    fixer.run()
    
    return 0

if __name__ == '__main__':
    exit(main())