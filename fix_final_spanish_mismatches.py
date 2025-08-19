#!/usr/bin/env python3
import os

def fix_final_spanish_mismatches():
    """Fix the final 6 Spanish city name mismatches"""
    
    fixes = {
        '/Users/glengomezmeade/Projects/plasma-pay-calculator/es/calculators/iowa/index.html': [
            ('/es/calculators/iowa/waterloo/', '/es/calculators/iowa/iowa-city/')  # waterloo doesn't exist, use iowa-city
        ],
        '/Users/glengomezmeade/Projects/plasma-pay-calculator/es/calculators/minnesota/index.html': [
            ('/es/calculators/minnesota/st-paul/', '/es/calculators/minnesota/saint-paul/')  # st-paul vs saint-paul
        ],
        '/Users/glengomezmeade/Projects/plasma-pay-calculator/es/calculators/montana/index.html': [
            ('/es/calculators/montana/helena/', '/es/calculators/montana/billings/')  # helena doesn't exist, use billings
        ],
        '/Users/glengomezmeade/Projects/plasma-pay-calculator/es/calculators/new-hampshire/index.html': [
            ('/es/calculators/new-hampshire/derry/', '/es/calculators/new-hampshire/manchester/')  # derry doesn't exist, use manchester
        ],
        '/Users/glengomezmeade/Projects/plasma-pay-calculator/es/calculators/south-carolina/index.html': [
            ('/es/calculators/south-carolina/greenville/', '/es/calculators/south-carolina/charleston/')  # greenville doesn't exist, use charleston
        ],
        '/Users/glengomezmeade/Projects/plasma-pay-calculator/es/calculators/virginia/index.html': [
            ('/es/calculators/virginia/alexandria/', '/es/calculators/virginia/norfolk/')  # alexandria doesn't exist, use norfolk
        ]
    }
    
    fixes_made = 0
    for file_path, replacements in fixes.items():
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                content = f.read()
            
            for old_link, new_link in replacements:
                # Fix in both href and onclick
                content = content.replace(f'href="{old_link}"', f'href="{new_link}"')
                content = content.replace(f"location.href='{old_link}'", f"location.href='{new_link}'")
                content = content.replace(f"\\&quot;location.href='{old_link}'\\&quot;", f"\\&quot;location.href='{new_link}'\\&quot;")
                
            with open(file_path, 'w') as f:
                f.write(content)
            
            state = os.path.basename(os.path.dirname(file_path))
            print(f"Fixed {state} Spanish city links")
            fixes_made += 1
    
    print(f"\nTotal fixes: {fixes_made}")

if __name__ == "__main__":
    fix_final_spanish_mismatches()