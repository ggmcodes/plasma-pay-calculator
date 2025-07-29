#!/usr/bin/env python3
"""
Comprehensive site debugging script to check all links and ensure everything is working
"""

import os
import re
from pathlib import Path
from urllib.parse import urlparse
import json

class SiteDebugger:
    def __init__(self, root_path):
        self.root_path = Path(root_path)
        self.issues = []
        self.checked_files = 0
        self.total_links = 0
        self.broken_links = []
        self.missing_files = []
        
    def check_file_exists(self, file_path, reference_file):
        """Check if a linked file exists"""
        # Handle absolute paths
        if file_path.startswith('/'):
            full_path = self.root_path / file_path.lstrip('/')
        else:
            # Relative path from reference file
            ref_dir = Path(reference_file).parent
            full_path = ref_dir / file_path
            
        # Remove anchors and query strings
        clean_path = str(full_path).split('#')[0].split('?')[0]
        
        # For directory links, check for index.html
        if clean_path.endswith('/'):
            clean_path = clean_path + 'index.html'
            
        return os.path.exists(clean_path), clean_path
    
    def extract_links(self, content):
        """Extract all links from HTML content"""
        links = []
        
        # Find href links
        href_pattern = r'href=["\']([^"\']+)["\']'
        links.extend(re.findall(href_pattern, content))
        
        # Find src links (images, scripts)
        src_pattern = r'src=["\']([^"\']+)["\']'
        links.extend(re.findall(src_pattern, content))
        
        return links
    
    def check_html_file(self, file_path):
        """Check a single HTML file for issues"""
        self.checked_files += 1
        local_issues = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Check for required elements
            if '<nav>' not in content and '<nav ' not in content:
                local_issues.append(f"Missing navigation")
                
            if 'PPC' not in content:
                local_issues.append(f"Missing PPC logo")
                
            if 'toggleMobileMenu' not in content:
                local_issues.append(f"Missing mobile menu functionality")
                
            # Check all links
            links = self.extract_links(content)
            self.total_links += len(links)
            
            for link in links:
                # Skip external links and anchors
                if link.startswith('http') or link.startswith('#') or link.startswith('mailto:'):
                    continue
                    
                # Skip data URLs
                if link.startswith('data:'):
                    continue
                    
                # Check if file exists
                exists, checked_path = self.check_file_exists(link, file_path)
                if not exists and checked_path not in self.missing_files:
                    self.broken_links.append({
                        'file': str(file_path),
                        'link': link,
                        'expected_path': checked_path
                    })
                    self.missing_files.append(checked_path)
                    
            # Check for common issues
            if '/es/' in str(file_path):
                # Spanish file checks
                if 'href="/"' in content and 'href="/es/"' not in content:
                    local_issues.append("Spanish page linking to English home")
                if 'Plasma Pay Calculator' in content and 'Calculadora Plasma' not in content:
                    local_issues.append("English text in Spanish page")
            else:
                # English file checks
                if 'href="/es/"' in content and 'language' not in content.lower():
                    local_issues.append("English page incorrectly linking to Spanish")
                    
            if local_issues:
                self.issues.append({
                    'file': str(file_path),
                    'issues': local_issues
                })
                
        except Exception as e:
            self.issues.append({
                'file': str(file_path),
                'issues': [f"Error reading file: {str(e)}"]
            })
    
    def check_required_files(self):
        """Check if all required files exist"""
        required_files = [
            'index.html',
            'favicon.ico',
            'favicon.svg',
            'styles.css',
            'states.html',
            'faq.html',
            'contact.html',
            'blog/index.html',
            'centers/index.html',
            'health/index.html',
            'process/index.html',
            'calculators/index.html',
            'es/index.html',
            'es/states.html',
            'es/faq.html'
        ]
        
        missing_required = []
        for file in required_files:
            full_path = self.root_path / file
            if not full_path.exists():
                missing_required.append(file)
                
        return missing_required
    
    def run_debug(self):
        """Run the complete debugging process"""
        print("🔍 Starting Site Debug...")
        print("=" * 60)
        
        # Check required files
        print("\n📋 Checking required files...")
        missing_required = self.check_required_files()
        if missing_required:
            print(f"❌ Missing required files: {', '.join(missing_required)}")
        else:
            print("✅ All required files present")
            
        # Find all HTML files
        html_files = list(self.root_path.rglob("*.html"))
        html_files = [f for f in html_files if 'node_modules' not in str(f) and '.git' not in str(f)]
        
        print(f"\n📄 Found {len(html_files)} HTML files to check")
        
        # Check each file
        for i, file_path in enumerate(html_files):
            if i % 100 == 0 and i > 0:
                print(f"   Progress: {i}/{len(html_files)} files checked...")
            self.check_html_file(file_path)
            
        # Generate report
        print("\n" + "=" * 60)
        print("📊 DEBUG REPORT")
        print("=" * 60)
        
        print(f"\n✅ Files Checked: {self.checked_files}")
        print(f"🔗 Total Links Checked: {self.total_links}")
        
        if self.broken_links:
            print(f"\n❌ BROKEN LINKS FOUND: {len(self.broken_links)}")
            # Group by missing file
            link_groups = {}
            for broken in self.broken_links[:20]:  # Show first 20
                missing = broken['expected_path']
                if missing not in link_groups:
                    link_groups[missing] = []
                link_groups[missing].append(broken['file'])
                
            for missing, files in link_groups.items():
                print(f"\n   Missing: {missing}")
                print(f"   Referenced in: {files[0]}")
                if len(files) > 1:
                    print(f"   And {len(files)-1} other files...")
        else:
            print("\n✅ No broken links found!")
            
        if self.issues:
            print(f"\n⚠️  OTHER ISSUES FOUND: {len(self.issues)}")
            for issue in self.issues[:10]:  # Show first 10
                print(f"\n   File: {issue['file']}")
                for problem in issue['issues']:
                    print(f"   - {problem}")
        else:
            print("\n✅ No other issues found!")
            
        # Save detailed report
        report = {
            'total_files': self.checked_files,
            'total_links': self.total_links,
            'broken_links': self.broken_links,
            'issues': self.issues,
            'missing_files': list(set(self.missing_files))
        }
        
        with open('site_debug_report.json', 'w') as f:
            json.dump(report, f, indent=2)
            
        print("\n📄 Detailed report saved to site_debug_report.json")
        
        return len(self.broken_links) == 0 and len(self.issues) == 0

if __name__ == "__main__":
    debugger = SiteDebugger("/Users/glengomezmeade/plasma-pay-calculator")
    success = debugger.run_debug()
    
    if success:
        print("\n🎉 SITE IS 100% READY!")
    else:
        print("\n❗ Issues found - please fix before going live!")