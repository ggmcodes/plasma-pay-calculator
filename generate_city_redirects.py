#!/usr/bin/env python3
"""
Generate 301 redirects for all city pages
"""

import os
from pathlib import Path

# Source and destination paths
SOURCE_BASE = "/Users/glengomezmeade/Projects/bestplasmacenters/public/state"
DEST_BASE = "https://plasmapaycalculator.com/calculators"

def extract_city_info(file_path):
    """Extract state and city from file path"""
    # Example: public/state/texas/houston.html -> texas, houston
    path_parts = Path(file_path).parts
    state = path_parts[-2]
    city = Path(file_path).stem
    return state, city

def generate_redirects():
    """Generate all redirect rules for city pages"""
    redirects = []
    
    # Find all city pages
    city_pages = []
    for root, dirs, files in os.walk(SOURCE_BASE):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                # Skip state-level files (they're in state/ directory directly)
                if len(Path(file_path).parts) > len(Path(SOURCE_BASE).parts) + 1:
                    city_pages.append(file_path)
    
    print(f"Generating redirects for {len(city_pages)} city pages...")
    
    for city_page in sorted(city_pages):
        state, city = extract_city_info(city_page)
        
        # Generate redirect with .html
        old_url_html = f"/state/{state}/{city}.html"
        new_url = f"{DEST_BASE}/{state}/{city}/"
        redirects.append(f"{old_url_html} {new_url} 301")
        
        # Generate redirect without .html
        old_url_no_html = f"/state/{state}/{city}"
        redirects.append(f"{old_url_no_html} {new_url} 301")
    
    return redirects

def main():
    """Generate and display all redirects"""
    redirects = generate_redirects()
    
    print("\n# City page redirects - Migration to PlasmaPayCalculator.com")
    for redirect in redirects:
        print(redirect)
    
    print(f"\nTotal redirects generated: {len(redirects)}")
    
    # Write to file
    with open('/tmp/city_redirects.txt', 'w') as f:
        f.write("# City page redirects - Migration to PlasmaPayCalculator.com\n")
        for redirect in redirects:
            f.write(redirect + "\n")
    
    print("\nRedirects written to /tmp/city_redirects.txt")

if __name__ == "__main__":
    main()