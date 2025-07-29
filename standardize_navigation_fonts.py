#!/usr/bin/env python3
"""
Standardize navigation fonts across all HTML pages
Fixes font inconsistencies in navigation menus site-wide
"""

import os
import re
from pathlib import Path

def standardize_navigation_fonts():
    """Fix font inconsistencies in navigation across all HTML files"""
    
    # Standard font family - prioritizing system fonts for consistency
    STANDARD_FONT_FAMILY = "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif"
    
    # Standard navigation CSS
    STANDARD_NAV_CSS = f"""        body {{
            font-family: {STANDARD_FONT_FAMILY};
            line-height: 1.6;
            color: #2c3e50;
        }}

        nav {{
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            padding: 1rem 0;
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 1000;
            border-bottom: 1px solid rgba(39, 174, 96, 0.1);
        }}

        .nav-container {{
            max-width: 1400px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 1.5rem;
        }}

        .logo {{
            font-size: 1.2rem;
            font-weight: 700;
            color: #27ae60;
            text-decoration: none;
            display: flex;
            align-items: center;
            gap: 0.6rem;
        }}

        .logo-icon {{
            width: 32px;
            height: 32px;
            background: linear-gradient(135deg, #27ae60 0%, #2ecc71 100%);
            border-radius: 6px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: 700;
            font-size: 12px;
            box-shadow: 0 2px 6px rgba(39, 174, 96, 0.3);
        }}

        .trust-badge {{
            background: rgba(39, 174, 96, 0.1);
            color: #27ae60;
            padding: 0.2rem 0.6rem;
            border-radius: 12px;
            font-size: 0.7rem;
            font-weight: 500;
            margin-left: 0.8rem;
            white-space: nowrap;
        }}

        .nav-links {{
            display: flex;
            list-style: none;
            gap: 1.2rem;
            align-items: center;
        }}

        .nav-links a {{
            text-decoration: none;
            color: #2c3e50;
            font-weight: 500;
            transition: all 0.3s;
            padding: 0.4rem 0.8rem;
            border-radius: 6px;
            font-size: 0.9rem;
            white-space: nowrap;
        }}

        .nav-links a:hover,
        .nav-links a.active {{
            color: #27ae60;
            background: rgba(39, 174, 96, 0.1);
        }}

        .mobile-menu-btn {{
            display: none;
            background: none;
            border: none;
            color: #2c3e50;
            font-size: 24px;
            cursor: pointer;
        }}

        .mobile-menu {{
            display: none;
            position: fixed;
            top: 80px;
            left: 0;
            right: 0;
            background: rgba(255, 255, 255, 0.98);
            backdrop-filter: blur(10px);
            border-bottom: 1px solid rgba(39, 174, 96, 0.1);
            z-index: 999;
            padding: 1rem;
        }}

        .mobile-menu.active {{
            display: block;
        }}

        .mobile-menu ul {{
            list-style: none;
            padding: 0;
            margin: 0;
        }}

        .mobile-menu li {{
            margin: 0.5rem 0;
        }}

        .mobile-menu a {{
            display: block;
            padding: 1rem;
            text-decoration: none;
            color: #2c3e50;
            font-weight: 500;
            border-radius: 8px;
            transition: all 0.3s;
        }}

        .mobile-menu a:hover,
        .mobile-menu a.active {{
            color: #27ae60;
            background: rgba(39, 174, 96, 0.1);
        }}

        @media (max-width: 968px) {{
            .nav-links {{
                display: none;
            }}
            
            .mobile-menu-btn {{
                display: block;
            }}
            
            .trust-badge {{
                font-size: 0.6rem;
                padding: 0.15rem 0.4rem;
            }}
            
            .logo {{
                font-size: 1rem;
            }}
            
            .logo-icon {{
                width: 28px;
                height: 28px;
                font-size: 11px;
            }}
        }}"""

    # Find all HTML files
    html_files = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    
    print(f"Found {len(html_files)} HTML files")
    
    # Process each file
    files_updated = 0
    
    for file_path in html_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Skip if no navigation present
            if '<nav>' not in content:
                continue
                
            # Check if needs font standardization
            needs_update = False
            
            # Check for non-standard font families in body or navigation
            if "'Roboto', -apple-system" in content:
                needs_update = True
            elif "font-size: 1.125rem" in content:  # Centers page smaller logo
                needs_update = True
            elif "font-weight: 600" in content and ".logo" in content:  # Centers page lighter logo
                needs_update = True
            elif "border-radius: 8px" in content and ".nav-links a" in content:  # States page different border
                needs_update = True
            elif "opacity: 0.8" in content and ".nav-links" in content:  # Centers page different hover
                needs_update = True
            
            if not needs_update:
                continue
                
            # Find and replace navigation CSS
            # Look for body font-family and nav styles
            body_pattern = r'body\s*\{[^}]*font-family[^}]*\}'
            nav_pattern = r'nav\s*\{[^}]*\}'
            nav_container_pattern = r'\.nav-container\s*\{[^}]*\}'
            logo_pattern = r'\.logo\s*\{[^}]*\}'
            logo_icon_pattern = r'\.logo-icon\s*\{[^}]*\}'
            trust_badge_pattern = r'\.trust-badge\s*\{[^}]*\}'
            nav_links_pattern = r'\.nav-links\s*\{[^}]*\}'
            nav_links_a_pattern = r'\.nav-links\s+a\s*\{[^}]*\}'
            nav_hover_pattern = r'\.nav-links\s+a:hover[^}]*\}'
            mobile_btn_pattern = r'\.mobile-menu-btn\s*\{[^}]*\}'
            mobile_menu_pattern = r'\.mobile-menu\s*\{[^}]*\}'
            
            # Replace or add standardized CSS
            if re.search(body_pattern, content):
                # Find the style section and replace navigation-related CSS
                style_start = content.find('<style>')
                style_end = content.find('</style>') + 8
                
                if style_start != -1 and style_end != -1:
                    # Extract existing styles that aren't navigation-related
                    existing_styles = content[style_start+7:style_end-8]
                    
                    # Remove navigation-related styles
                    patterns_to_remove = [
                        r'body\s*\{[^}]*\}',
                        r'nav\s*\{[^}]*\}',
                        r'\.nav-container\s*\{[^}]*\}',
                        r'\.logo\s*\{[^}]*\}',
                        r'\.logo-icon\s*\{[^}]*\}',
                        r'\.trust-badge\s*\{[^}]*\}',
                        r'\.nav-links\s*\{[^}]*\}',
                        r'\.nav-links\s+a\s*\{[^}]*\}',
                        r'\.nav-links\s+a:hover[^}]*\}',
                        r'\.nav-links\s+a\.active[^}]*\}',
                        r'\.mobile-menu-btn\s*\{[^}]*\}',
                        r'\.mobile-menu\s*\{[^}]*\}',
                        r'\.mobile-menu\.active\s*\{[^}]*\}',
                        r'\.mobile-menu\s+ul\s*\{[^}]*\}',
                        r'\.mobile-menu\s+li\s*\{[^}]*\}',
                        r'\.mobile-menu\s+a\s*\{[^}]*\}',
                        r'\.mobile-menu\s+a:hover[^}]*\}',
                        r'@media\s*\([^}]*max-width[^}]*\)\s*\{[^}]*\.nav-links[^}]*\}[^}]*\}',
                    ]
                    
                    cleaned_styles = existing_styles
                    for pattern in patterns_to_remove:
                        cleaned_styles = re.sub(pattern, '', cleaned_styles, flags=re.DOTALL)
                    
                    # Clean up extra whitespace
                    cleaned_styles = re.sub(r'\n\s*\n\s*\n', '\n\n', cleaned_styles)
                    
                    # Create new style section
                    new_style_section = f"<style>\n{STANDARD_NAV_CSS}\n\n{cleaned_styles.strip()}\n</style>"
                    
                    # Replace the entire style section
                    content = content[:style_start] + new_style_section + content[style_end:]
            
            # Write updated content
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            files_updated += 1
            print(f"Updated: {file_path}")
            
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            continue
    
    print(f"\nCompleted! Updated {files_updated} files with standardized navigation fonts.")

if __name__ == "__main__":
    standardize_navigation_fonts()