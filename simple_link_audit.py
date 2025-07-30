#!/usr/bin/env python3
"""
Simple Comprehensive Link Audit Script for Plasma Pay Calculator Site
Checks for broken internal links using regex parsing (no external dependencies)
"""

import os
import re
import json
from collections import defaultdict

class SimpleLinkAuditor:
    def __init__(self, root_dir):
        self.root_dir = root_dir
        self.all_files = set()
        self.all_directories = set()
        self.issues = {
            'broken_links': [],
            'navigation_issues': [],
            'blog_link_issues': [],
            'health_section_issues': [],
            'language_switcher_issues': [],
            'hardcoded_urls': [],
            'missing_files': []
        }
        
    def discover_all_files(self):
        """Find all HTML files and create a comprehensive set of valid paths"""
        print("📁 Discovering all files and valid paths...")
        
        for root, dirs, files in os.walk(self.root_dir):
            # Skip certain directories
            if any(skip in root for skip in ['.git', 'node_modules', '__pycache__', '.DS_Store']):
                continue
                
            for file in files:
                if file.endswith('.html'):
                    full_path = os.path.join(root, file)
                    rel_path = os.path.relpath(full_path, self.root_dir)
                    
                    # Add various path formats that could be valid
                    self.all_files.add(rel_path)
                    self.all_files.add('/' + rel_path)
                    
                    # For index.html files, add directory versions
                    if file == 'index.html':
                        dir_path = os.path.dirname(rel_path)
                        if dir_path:
                            self.all_files.add(dir_path)
                            self.all_files.add('/' + dir_path)
                            self.all_files.add(dir_path + '/')
                            self.all_files.add('/' + dir_path + '/')
                            self.all_directories.add(dir_path)
                            self.all_directories.add('/' + dir_path)
        
        print(f"   Found {len(self.all_files)} valid paths")
        return len(self.all_files)
    
    def extract_links_from_file(self, file_path):
        """Extract all internal links from an HTML file using regex"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Find all href attributes
            href_pattern = r'href=(["\'])([^"\']*?)\1'
            links = []
            
            for match in re.finditer(href_pattern, content, re.IGNORECASE):
                href = match.group(2)
                # Skip external links, email, phone, and fragment-only links
                if not href.startswith(('http://', 'https://', 'mailto:', 'tel:')) and href != '#':
                    # Get some context around the link
                    start = max(0, match.start() - 50)
                    end = min(len(content), match.end() + 50)
                    context = content[start:end].replace('\n', ' ').strip()
                    
                    links.append({
                        'href': href,
                        'context': context
                    })
            
            return links, content
            
        except Exception as e:
            print(f"❌ Error reading {file_path}: {e}")
            return [], ""
    
    def normalize_and_check_path(self, link, base_file):
        """Normalize a link and check if target exists"""
        # Remove fragment and query parameters for existence check
        clean_link = link.split('?')[0].split('#')[0]
        
        if not clean_link or clean_link == '/':
            return True, '/'  # Root is valid
            
        # Handle relative vs absolute paths
        if clean_link.startswith('/'):
            normalized = clean_link
        else:
            # Relative path - resolve based on current file location
            base_dir = os.path.dirname(base_file)
            if base_dir:
                normalized = '/' + os.path.normpath(os.path.join(base_dir, clean_link)).replace('\\', '/')
            else:
                normalized = '/' + clean_link
        
        # Check if path exists in our discovered files
        exists = self.path_exists(normalized)
        return exists, normalized
    
    def path_exists(self, normalized_path):
        """Check if a normalized path exists"""
        # Direct match
        if normalized_path in self.all_files:
            return True
            
        # Remove leading slash and check
        clean_path = normalized_path.lstrip('/')
        if clean_path in self.all_files:
            return True
            
        # Check if it's a directory that should have index.html
        if normalized_path.endswith('/'):
            index_path = normalized_path + 'index.html'
            index_path_clean = normalized_path.rstrip('/') + '/index.html'
        else:
            index_path = normalized_path + '/index.html'
            index_path_clean = normalized_path + '/index.html'
            
        if index_path in self.all_files or index_path_clean in self.all_files:
            return True
            
        # Check actual file system as final fallback
        full_path = os.path.join(self.root_dir, clean_path)
        if os.path.exists(full_path):
            return True
            
        if os.path.exists(full_path + '/index.html'):
            return True
            
        return False
    
    def is_navigation_link(self, context):
        """Determine if a link is likely in navigation based on context"""
        nav_indicators = ['nav', 'menu', 'header', 'navigation', 'nav-links', 'nav-container']
        context_lower = context.lower()
        return any(indicator in context_lower for indicator in nav_indicators)
    
    def check_all_links(self):
        """Check all links in all HTML files"""
        print("🔗 Checking all internal links...")
        
        total_checked = 0
        
        for root, dirs, files in os.walk(self.root_dir):
            if any(skip in root for skip in ['.git', 'node_modules', '__pycache__']):
                continue
                
            for file in files:
                if not file.endswith('.html'):
                    continue
                    
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, self.root_dir)
                
                links, content = self.extract_links_from_file(file_path)
                total_checked += len(links)
                
                for link_info in links:
                    href = link_info['href']
                    context = link_info['context']
                    
                    if not href.startswith(('http://', 'https://', 'mailto:', 'tel:', '#')):
                        exists, normalized = self.normalize_and_check_path(href, rel_path)
                        
                        if not exists:
                            issue = {
                                'file': rel_path,
                                'link': href,
                                'normalized': normalized,
                                'context': context[:100]
                            }
                            
                            # Categorize the issue
                            if self.is_navigation_link(context):
                                self.issues['navigation_issues'].append(issue)
                            elif '/blog/' in rel_path or '/blog/' in href:
                                self.issues['blog_link_issues'].append(issue)
                            elif '/health/' in rel_path or '/health/' in href:
                                self.issues['health_section_issues'].append(issue)
                            elif (('/es/' in rel_path and '/es/' not in href) or 
                                  ('/es/' not in rel_path and '/es/' in href)):
                                self.issues['language_switcher_issues'].append(issue)
                            else:
                                self.issues['broken_links'].append(issue)
        
        print(f"   Checked {total_checked} links total")
    
    def check_hardcoded_urls(self):
        """Look for hardcoded URLs that should be relative paths"""
        print("🔗 Checking for hardcoded URLs...")
        
        hardcoded_patterns = [
            r'https?://[^/]*plasmapaycalculator\.com([^"\s<>]*)',
            r'https?://[^/]*plasma-pay-calculator([^"\s<>]*)'
        ]
        
        count = 0
        for root, dirs, files in os.walk(self.root_dir):
            if any(skip in root for skip in ['.git', 'node_modules', '__pycache__']):
                continue
                
            for file in files:
                if file.endswith('.html') and count < 50:  # Limit for performance
                    file_path = os.path.join(root, file)
                    rel_path = os.path.relpath(file_path, self.root_dir)
                    
                    try:
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()
                        
                        for pattern in hardcoded_patterns:
                            matches = re.finditer(pattern, content, re.IGNORECASE)
                            for match in matches:
                                # Skip certain valid hardcoded URLs
                                start = max(0, match.start() - 30)
                                end = min(len(content), match.end() + 30)
                                context = content[start:end]
                                
                                if any(valid in context.lower() for valid in ['canonical', 'og:url', 'hreflang']):
                                    continue
                                    
                                self.issues['hardcoded_urls'].append({
                                    'file': rel_path,
                                    'match': match.group(),
                                    'context': context.strip()[:100]
                                })
                        count += 1
                                
                    except Exception as e:
                        continue
    
    def run_comprehensive_audit(self):
        """Run the complete link audit"""
        print("🚀 Starting Simple Comprehensive Link Audit...")
        print("=" * 80)
        print(f"📂 Root directory: {self.root_dir}")
        
        # Step 1: Discover all files
        total_files = self.discover_all_files()
        
        # Step 2: Check all links
        self.check_all_links()
        
        # Step 3: Check hardcoded URLs
        self.check_hardcoded_urls()
        
        # Step 4: Generate report
        self.generate_report()
        
        return self.issues
    
    def generate_report(self):
        """Generate a comprehensive report of all issues found"""
        print("\n" + "="*80)
        print("🎯 COMPREHENSIVE LINK AUDIT REPORT")
        print("="*80)
        
        total_issues = sum(len(issues) for issues in self.issues.values())
        total_files_checked = len(self.all_files)
        
        print(f"📊 SUMMARY:")
        print(f"   • Total HTML files discovered: {total_files_checked}")
        print(f"   • Total issues found: {total_issues}")
        
        if total_issues == 0:
            print("   • Site health: ✅ EXCELLENT (No broken links found!)")
        elif total_issues < 10:
            print("   • Site health: 🟢 GOOD (Few issues to fix)")
        elif total_issues < 50:
            print("   • Site health: 🟡 FAIR (Some issues need attention)")
        else:
            print("   • Site health: 🔴 NEEDS WORK (Many issues to fix)")
        
        print(f"\n📋 ISSUES BY CATEGORY:")
        categories = {
            'navigation_issues': '🧭 Navigation Menu Issues',
            'blog_link_issues': '📝 Blog Link Issues', 
            'health_section_issues': '🏥 Health Section Issues',
            'language_switcher_issues': '🌍 Language Switcher Issues',
            'broken_links': '🔗 Other Broken Links',
            'hardcoded_urls': '🔗 Hardcoded URL Issues',
            'missing_files': '📄 Missing Files'
        }
        
        for category, display_name in categories.items():
            issues = self.issues.get(category, [])
            if issues:
                print(f"   {display_name}: {len(issues)} issues")
        
        # Detailed breakdown of critical issues
        if self.issues['navigation_issues']:
            print(f"\n🔴 CRITICAL: NAVIGATION MENU ISSUES ({len(self.issues['navigation_issues'])} found)")
            print("-" * 60)
            for i, issue in enumerate(self.issues['navigation_issues'][:5], 1):
                print(f"{i}. File: {issue['file']}")
                print(f"   Broken link: {issue['link']}")
                print(f"   Should point to: {issue['normalized']}")
                print()
            if len(self.issues['navigation_issues']) > 5:
                print(f"   ... and {len(self.issues['navigation_issues']) - 5} more navigation issues")
        
        if self.issues['language_switcher_issues']:
            print(f"\n🔴 CRITICAL: LANGUAGE SWITCHER ISSUES ({len(self.issues['language_switcher_issues'])} found)")
            print("-" * 60)
            for i, issue in enumerate(self.issues['language_switcher_issues'][:5], 1):
                print(f"{i}. File: {issue['file']}")
                print(f"   Broken link: {issue['link']}")
                print(f"   Should point to: {issue['normalized']}")
                print()
            if len(self.issues['language_switcher_issues']) > 5:
                print(f"   ... and {len(self.issues['language_switcher_issues']) - 5} more language switcher issues")
        
        if self.issues['blog_link_issues']:
            print(f"\n🟡 MEDIUM: BLOG LINK ISSUES ({len(self.issues['blog_link_issues'])} found)")
            print("-" * 60)
            for i, issue in enumerate(self.issues['blog_link_issues'][:3], 1):
                print(f"{i}. File: {issue['file']}")
                print(f"   Broken link: {issue['link']}")
                print()
            if len(self.issues['blog_link_issues']) > 3:
                print(f"   ... and {len(self.issues['blog_link_issues']) - 3} more blog issues")
        
        if self.issues['health_section_issues']:
            print(f"\n🟡 MEDIUM: HEALTH SECTION ISSUES ({len(self.issues['health_section_issues'])} found)")
            print("-" * 60)
            for i, issue in enumerate(self.issues['health_section_issues'][:3], 1):
                print(f"{i}. File: {issue['file']}")
                print(f"   Broken link: {issue['link']}")
                print()
            if len(self.issues['health_section_issues']) > 3:
                print(f"   ... and {len(self.issues['health_section_issues']) - 3} more health section issues")
        
        if self.issues['hardcoded_urls']:
            print(f"\n🟢 LOW: HARDCODED URL ISSUES ({len(self.issues['hardcoded_urls'])} found)")
            print("-" * 60)
            for i, issue in enumerate(self.issues['hardcoded_urls'][:3], 1):
                print(f"{i}. File: {issue['file']}")
                print(f"   Hardcoded URL: {issue['match']}")
                print()
            if len(self.issues['hardcoded_urls']) > 3:
                print(f"   ... and {len(self.issues['hardcoded_urls']) - 3} more hardcoded URL issues")
        
        # Save detailed JSON report
        report_data = {
            'summary': {
                'total_files': total_files_checked,
                'total_issues': total_issues,
                'issues_by_category': {k: len(v) for k, v in self.issues.items() if v}
            },
            'details': self.issues
        }
        
        report_file = os.path.join(self.root_dir, 'simple_link_audit_report.json')
        with open(report_file, 'w') as f:
            json.dump(report_data, f, indent=2)
        
        print(f"\n💾 Detailed JSON report saved to: simple_link_audit_report.json")
        
        # Final recommendations
        print(f"\n" + "="*80)
        print("🔧 PRIORITY RECOMMENDATIONS")
        print("="*80)
        
        if self.issues['navigation_issues']:
            print("🔥 URGENT: Fix navigation menu broken links")
            print("   → These affect user experience on every page visit")
            print("   → Users can't navigate properly between sections")
        
        if self.issues['language_switcher_issues']:
            print("🔥 URGENT: Fix language switcher functionality")
            print("   → Critical for bilingual site operation")
            print("   → Users can't switch between English/Spanish")
        
        if self.issues['blog_link_issues']:
            print("📝 IMPORTANT: Fix blog internal links")
            print("   → Affects content discoverability and SEO")
            print("   → Broken internal linking reduces page authority")
        
        if self.issues['health_section_issues']:
            print("🏥 IMPORTANT: Fix health section links")
            print("   → Recently updated content needs working links")
            print("   → Health information should be easily accessible")
        
        if self.issues['hardcoded_urls']:
            print("🔧 OPTIONAL: Replace hardcoded URLs with relative paths")
            print("   → Improves maintainability for development")
            print("   → Better for testing and staging environments")
        
        if total_issues == 0:
            print("🎉 EXCELLENT! No broken links found. Your site is healthy!")
        else:
            print(f"\n⚠️  Total of {total_issues} issues found.")
            print("   Start with URGENT items, then work through IMPORTANT ones.")
            print("   Focus on navigation and language switcher issues first.")

def main():
    """Run the simple comprehensive link audit"""
    root_dir = "/Users/glengomezmeade/plasma-pay-calculator"
    
    if not os.path.exists(root_dir):
        print(f"❌ Error: Directory {root_dir} does not exist")
        return None
    
    auditor = SimpleLinkAuditor(root_dir)
    issues = auditor.run_comprehensive_audit()
    
    return issues

if __name__ == "__main__":
    main()