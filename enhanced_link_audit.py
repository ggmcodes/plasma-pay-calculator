#!/usr/bin/env python3
"""
Enhanced Comprehensive Link Audit Script for Plasma Pay Calculator Site
Checks for broken internal links, navigation issues, language switcher problems, and more
"""

import os
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import json
from collections import defaultdict
import sys

class EnhancedLinkAuditor:
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
            'duplicate_links': [],
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
        """Extract all internal links from an HTML file with detailed analysis"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                
            soup = BeautifulSoup(content, 'html.parser')
            links = []
            
            # Find all <a> tags with href
            for a_tag in soup.find_all('a', href=True):
                href = a_tag['href']
                # Skip external links, email, phone, and fragment-only links
                if not href.startswith(('http://', 'https://', 'mailto:', 'tel:')) and href != '#':
                    links.append({
                        'href': href,
                        'text': a_tag.get_text(strip=True)[:100],  # Limit text length
                        'tag': 'a',
                        'parent_element': a_tag.parent.name if a_tag.parent else 'unknown',
                        'classes': ' '.join(a_tag.get('class', []))
                    })
            
            return links, soup, content
            
        except Exception as e:
            print(f"❌ Error reading {file_path}: {e}")
            return [], None, ""
    
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
    
    def check_navigation_links(self):
        """Check navigation menu links on all pages"""
        print("🧭 Checking navigation links...")
        nav_issues = []
        
        # Key pages to check navigation
        key_pages = [
            'index.html',
            'about.html', 
            'faq.html',
            'states.html',
            'contact.html',
            'blog/index.html',
            'health/index.html',
            'process/index.html'
        ]
        
        spanish_pages = [
            'es/index.html',
            'es/about.html',
            'es/faq.html', 
            'es/states.html',
            'es/contact.html',
            'es/blog/index.html',
            'es/health/index.html',
            'es/process/index.html'
        ]
        
        all_test_pages = key_pages + spanish_pages
        
        for page in all_test_pages:
            full_path = os.path.join(self.root_dir, page)
            if os.path.exists(full_path):
                links, soup, content = self.extract_links_from_file(full_path)
                
                # Look for navigation-specific elements
                if soup:
                    nav_elements = soup.find_all(['nav', 'header'])
                    nav_elements.extend(soup.find_all('div', class_=re.compile(r'nav|menu')))
                    
                    for nav in nav_elements:
                        nav_links = nav.find_all('a', href=True)
                        for link in nav_links:
                            href = link['href']
                            if not href.startswith(('http://', 'https://', 'mailto:', 'tel:', '#')):
                                exists, normalized = self.normalize_and_check_path(href, page)
                                if not exists:
                                    nav_issues.append({
                                        'file': page,
                                        'link': href,
                                        'text': link.get_text(strip=True)[:50],
                                        'normalized': normalized,
                                        'section': 'navigation'
                                    })
        
        self.issues['navigation_issues'] = nav_issues
        print(f"   Found {len(nav_issues)} navigation issues")
        return len(nav_issues)
    
    def check_blog_links(self):
        """Check blog post internal references and cross-links"""
        print("📝 Checking blog links...")
        blog_issues = []
        
        # Check English blog
        english_blog = os.path.join(self.root_dir, 'blog')
        if os.path.exists(english_blog):
            self._check_blog_directory(english_blog, 'blog', blog_issues)
        
        # Check Spanish blog
        spanish_blog = os.path.join(self.root_dir, 'es/blog')
        if os.path.exists(spanish_blog):
            self._check_blog_directory(spanish_blog, 'es/blog', blog_issues)
        
        self.issues['blog_link_issues'] = blog_issues
        print(f"   Found {len(blog_issues)} blog link issues")
        return len(blog_issues)
    
    def _check_blog_directory(self, blog_dir, blog_path, blog_issues):
        """Helper method to check links in a blog directory"""
        for root, dirs, files in os.walk(blog_dir):
            for file in files:
                if file.endswith('.html'):
                    file_path = os.path.join(root, file)
                    rel_path = os.path.relpath(file_path, self.root_dir)
                    
                    links, soup, content = self.extract_links_from_file(file_path)
                    
                    for link_info in links:
                        href = link_info['href']
                        if not href.startswith(('http://', 'https://', 'mailto:', 'tel:', '#')):
                            exists, normalized = self.normalize_and_check_path(href, rel_path)
                            if not exists:
                                blog_issues.append({
                                    'file': rel_path,
                                    'link': href,
                                    'text': link_info['text'],
                                    'normalized': normalized,
                                    'section': 'blog'
                                })
    
    def check_health_section_links(self):
        """Check health section links that were recently updated"""
        print("🏥 Checking health section links...")
        health_issues = []
        
        # Check English health section
        english_health = os.path.join(self.root_dir, 'health')
        if os.path.exists(english_health):
            self._check_health_directory(english_health, 'health', health_issues)
        
        # Check Spanish health section
        spanish_health = os.path.join(self.root_dir, 'es/health')
        if os.path.exists(spanish_health):
            self._check_health_directory(spanish_health, 'es/health', health_issues)
        
        self.issues['health_section_issues'] = health_issues
        print(f"   Found {len(health_issues)} health section issues")
        return len(health_issues)
    
    def _check_health_directory(self, health_dir, health_path, health_issues):
        """Helper method to check links in health directory"""
        for root, dirs, files in os.walk(health_dir):
            for file in files:
                if file.endswith('.html'):
                    file_path = os.path.join(root, file)
                    rel_path = os.path.relpath(file_path, self.root_dir)
                    
                    links, soup, content = self.extract_links_from_file(file_path)
                    
                    for link_info in links:
                        href = link_info['href']
                        if not href.startswith(('http://', 'https://', 'mailto:', 'tel:', '#')):
                            exists, normalized = self.normalize_and_check_path(href, rel_path)
                            if not exists:
                                health_issues.append({
                                    'file': rel_path,
                                    'link': href,
                                    'text': link_info['text'],
                                    'normalized': normalized,
                                    'section': 'health'
                                })
    
    def check_language_switcher(self):
        """Test language switcher functionality"""
        print("🌍 Checking language switcher links...")
        lang_issues = []
        
        # Sample pages to test language switching
        test_pages = [
            ('index.html', 'es/index.html'),
            ('about.html', 'es/about.html'),
            ('faq.html', 'es/faq.html'),
            ('blog/index.html', 'es/blog/index.html'),
            ('health/index.html', 'es/health/index.html')
        ]
        
        for en_page, es_page in test_pages:
            # Check English page for Spanish switcher
            en_path = os.path.join(self.root_dir, en_page)
            if os.path.exists(en_path):
                links, soup, content = self.extract_links_from_file(en_path)
                
                # Look for language switcher elements
                spanish_link_found = False
                for link_info in links:
                    href = link_info['href']
                    if ('/es/' in href or href.startswith('es/')) and not href.startswith('http'):
                        spanish_link_found = True
                        exists, normalized = self.normalize_and_check_path(href, en_page)
                        if not exists:
                            lang_issues.append({
                                'file': en_page,
                                'link': href,
                                'text': link_info['text'],
                                'normalized': normalized,
                                'type': 'en_to_es_broken',
                                'section': 'language_switcher'
                            })
                
                # Also check for language switcher in content
                if 'español' in content.lower() or 'spanish' in content.lower():
                    if not spanish_link_found:
                        lang_issues.append({
                            'file': en_page,
                            'link': 'missing',
                            'text': 'Language switcher referenced but no link found',
                            'normalized': 'N/A',
                            'type': 'missing_spanish_link',
                            'section': 'language_switcher'
                        })
            
            # Check Spanish page for English switcher
            es_path = os.path.join(self.root_dir, es_page)
            if os.path.exists(es_path):
                links, soup, content = self.extract_links_from_file(es_path)
                
                english_link_found = False
                for link_info in links:
                    href = link_info['href']
                    # Links going back to English (not containing /es/)
                    if (href.startswith('../') or href.startswith('/')) and '/es/' not in href and not href.startswith('http'):
                        english_link_found = True
                        exists, normalized = self.normalize_and_check_path(href, es_page)
                        if not exists:
                            lang_issues.append({
                                'file': es_page,
                                'link': href,
                                'text': link_info['text'],
                                'normalized': normalized,
                                'type': 'es_to_en_broken',
                                'section': 'language_switcher'
                            })
        
        self.issues['language_switcher_issues'] = lang_issues
        print(f"   Found {len(lang_issues)} language switcher issues")
        return len(lang_issues)
    
    def check_hardcoded_urls(self):
        """Look for hardcoded URLs that should be relative paths"""
        print("🔗 Checking for hardcoded URLs...")
        hardcoded_issues = []
        
        # Sample files to check (limit to avoid performance issues)
        sample_files = []
        count = 0
        for root, dirs, files in os.walk(self.root_dir):
            if any(skip in root for skip in ['.git', 'node_modules', '__pycache__']):
                continue
            for file in files:
                if file.endswith('.html') and count < 100:  # Limit sample size
                    sample_files.append(os.path.join(root, file))
                    count += 1
        
        hardcoded_patterns = [
            r'https?://[^/]*plasmapaycalculator\.com([^"\s<>]*)',
            r'https?://[^/]*plasma-pay-calculator([^"\s<>]*)',
            r'href=["\']https?://[^/]*plasmapaycalculator\.com([^"\']*)["\']',
            r'src=["\']https?://[^/]*plasmapaycalculator\.com([^"\']*)["\']'
        ]
        
        for file_path in sample_files:
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                rel_path = os.path.relpath(file_path, self.root_dir)
                
                for pattern in hardcoded_patterns:
                    matches = re.finditer(pattern, content, re.IGNORECASE)
                    for match in matches:
                        # Skip certain valid hardcoded URLs (like canonical links)
                        context = content[max(0, match.start()-20):match.end()+20]
                        if any(valid in context.lower() for valid in ['canonical', 'og:url', 'hreflang']):
                            continue
                            
                        hardcoded_issues.append({
                            'file': rel_path,
                            'match': match.group(),
                            'context': context.strip(),
                            'position': match.start(),
                            'section': 'hardcoded_urls'
                        })
                        
            except Exception as e:
                continue
        
        self.issues['hardcoded_urls'] = hardcoded_issues
        print(f"   Found {len(hardcoded_issues)} hardcoded URL issues")
        return len(hardcoded_issues)
    
    def check_duplicate_links(self):
        """Check for duplicate or conflicting link references"""
        print("🔍 Checking for duplicate links...")
        duplicate_issues = []
        
        # This is a basic implementation - can be enhanced
        link_map = defaultdict(list)
        
        # Sample key pages
        key_files = [
            'index.html', 
            'about.html',
            'blog/index.html',
            'es/index.html',
            'es/about.html'
        ]
        
        for page in key_files:
            full_path = os.path.join(self.root_dir, page)
            if os.path.exists(full_path):
                links, soup, content = self.extract_links_from_file(full_path)
                
                page_links = defaultdict(int)
                for link_info in links:
                    href = link_info['href']
                    if not href.startswith(('http://', 'https://', 'mailto:', 'tel:', '#')):
                        page_links[href] += 1
                
                # Find duplicates within page
                for href, count in page_links.items():
                    if count > 3:  # More than 3 identical links might be excessive
                        duplicate_issues.append({
                            'file': page,
                            'link': href,
                            'count': count,
                            'type': 'excessive_duplicates',
                            'section': 'duplicates'
                        })
        
        self.issues['duplicate_links'] = duplicate_issues
        print(f"   Found {len(duplicate_issues)} duplicate link issues")
        return len(duplicate_issues)
    
    def run_comprehensive_audit(self):
        """Run the complete enhanced link audit"""
        print("🚀 Starting Enhanced Comprehensive Link Audit...")
        print("=" * 80)
        print(f"📂 Root directory: {self.root_dir}")
        
        # Step 1: Discover all files
        total_files = self.discover_all_files()
        
        # Step 2: Run all checks
        nav_issues = self.check_navigation_links()
        blog_issues = self.check_blog_links()
        health_issues = self.check_health_section_links()
        lang_issues = self.check_language_switcher()
        hardcoded_issues = self.check_hardcoded_urls()
        duplicate_issues = self.check_duplicate_links()
        
        # Step 3: Generate comprehensive report
        self.generate_detailed_report()
        
        return self.issues
    
    def generate_detailed_report(self):
        """Generate a comprehensive report of all issues found"""
        print("\n" + "="*80)
        print("🎯 ENHANCED COMPREHENSIVE LINK AUDIT REPORT")
        print("="*80)
        
        total_issues = sum(len(issues) for issues in self.issues.values())
        total_files_checked = len(self.all_files)
        
        print(f"📊 SUMMARY:")
        print(f"   • Total HTML files discovered: {total_files_checked}")
        print(f"   • Total issues found: {total_issues}")
        print(f"   • Site health score: {max(0, 100 - (total_issues * 100 // max(total_files_checked, 1)))}%")
        
        print(f"\n📋 ISSUES BY CATEGORY:")
        for category, issues in self.issues.items():
            if issues:
                category_name = category.replace('_', ' ').title()
                print(f"   🔸 {category_name}: {len(issues)} issues")
        
        # Detailed breakdown
        print(f"\n" + "="*80)
        print("📝 DETAILED ISSUE BREAKDOWN")
        print("="*80)
        
        for category, issues in self.issues.items():
            if issues:
                category_name = category.replace('_', ' ').upper()
                print(f"\n🔴 {category_name} ({len(issues)} issues):")
                print("-" * 60)
                
                # Show top 10 issues in each category
                for i, issue in enumerate(issues[:10], 1):
                    print(f"{i:2d}. File: {issue['file']}")
                    
                    if 'link' in issue:
                        print(f"    Link: {issue['link']}")
                    if 'match' in issue:
                        print(f"    Match: {issue['match']}")
                    if 'text' in issue and issue['text']:
                        print(f"    Text: {issue['text'][:60]}...")
                    if 'normalized' in issue:
                        print(f"    Target: {issue['normalized']}")
                    if 'type' in issue:
                        print(f"    Type: {issue['type']}")
                    if 'context' in issue:
                        print(f"    Context: {issue['context'][:80]}...")
                    print()
                
                if len(issues) > 10:
                    print(f"    ... and {len(issues) - 10} more issues in this category")
                print()
        
        # Save detailed JSON report
        report_data = {
            'summary': {
                'total_files': total_files_checked,
                'total_issues': total_issues,
                'health_score': max(0, 100 - (total_issues * 100 // max(total_files_checked, 1))),
                'issues_by_category': {k: len(v) for k, v in self.issues.items()}
            },
            'details': self.issues
        }
        
        with open(os.path.join(self.root_dir, 'enhanced_link_audit_report.json'), 'w') as f:
            json.dump(report_data, f, indent=2)
        
        print(f"💾 Detailed JSON report saved to: enhanced_link_audit_report.json")
        
        # Final recommendations
        print(f"\n" + "="*80)
        print("🔧 PRIORITY RECOMMENDATIONS")
        print("="*80)
        
        if self.issues['navigation_issues']:
            print("🔥 HIGH PRIORITY: Fix navigation menu broken links")
            print("   These affect user experience on every page")
        
        if self.issues['language_switcher_issues']:
            print("🔥 HIGH PRIORITY: Fix language switcher functionality")
            print("   Critical for bilingual site operation")
        
        if self.issues['blog_link_issues']:
            print("📝 MEDIUM PRIORITY: Fix blog internal links")
            print("   Important for content discoverability and SEO")
        
        if self.issues['health_section_issues']:
            print("🏥 MEDIUM PRIORITY: Fix health section links")
            print("   Important for recently updated content")
        
        if self.issues['hardcoded_urls']:
            print("🔗 LOW PRIORITY: Replace hardcoded URLs with relative paths")
            print("   Good for maintainability and development")
        
        if total_issues == 0:
            print("🎉 EXCELLENT! No broken links found. Site is healthy!")
        else:
            print(f"⚠️  {total_issues} issues found. Start with high priority items.")

def main():
    """Run the enhanced comprehensive link audit"""
    root_dir = "/Users/glengomezmeade/plasma-pay-calculator"
    
    if not os.path.exists(root_dir):
        print(f"❌ Error: Directory {root_dir} does not exist")
        sys.exit(1)
    
    auditor = EnhancedLinkAuditor(root_dir)
    issues = auditor.run_comprehensive_audit()
    
    return issues

if __name__ == "__main__":
    main()