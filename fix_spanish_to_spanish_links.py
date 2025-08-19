#!/usr/bin/env python3
import os
import re

def fix_spanish_links_properly():
    """Fix Spanish pages to link to Spanish calculators (not English)"""
    
    fixes_made = 0
    
    # Map of files and their link corrections
    spanish_fixes = {
        '/Users/glengomezmeade/Projects/plasma-pay-calculator/es/calculators/missouri/index.html': [
            ('/calculators/missouri/springfield-mo/', '/es/calculators/missouri/springfield/'),
            ('/calculators/missouri/columbia-mo/', '/es/calculators/missouri/columbia/'),
            ('/calculators/missouri/kansas-city/', '/es/calculators/missouri/kansas-city/'),
            ('/calculators/missouri/st-louis/', '/es/calculators/missouri/st-louis/'),
            ('/calculators/missouri/independence/', '/es/calculators/missouri/independence/')
        ],
        '/Users/glengomezmeade/Projects/plasma-pay-calculator/es/calculators/virginia/index.html': [
            ('/calculators/virginia/alexandria/', '/es/calculators/virginia/alexandria/'),
            ('/calculators/virginia/virginia-beach/', '/es/calculators/virginia/virginia-beach/'),
            ('/calculators/virginia/norfolk/', '/es/calculators/virginia/norfolk/'),
            ('/calculators/virginia/richmond/', '/es/calculators/virginia/richmond/'),
            ('/calculators/virginia/newport-news/', '/es/calculators/virginia/newport-news/')
        ],
        '/Users/glengomezmeade/Projects/plasma-pay-calculator/es/calculators/maine/index.html': [
            ('/calculators/maine/portland-me/', '/es/calculators/maine/portland/'),
            ('/calculators/maine/auburn-me/', '/es/calculators/maine/auburn/'),
            ('/calculators/maine/lewiston/', '/es/calculators/maine/lewiston/'),
            ('/calculators/maine/bangor/', '/es/calculators/maine/bangor/'),
            ('/calculators/maine/south-portland/', '/es/calculators/maine/south-portland/')
        ],
        '/Users/glengomezmeade/Projects/plasma-pay-calculator/es/calculators/delaware/index.html': [
            ('/calculators/delaware/newark-de/', '/es/calculators/delaware/newark/'),
            ('/calculators/delaware/wilmington/', '/es/calculators/delaware/wilmington/'),
            ('/calculators/delaware/dover/', '/es/calculators/delaware/dover/'),
            ('/calculators/delaware/middletown/', '/es/calculators/delaware/middletown/'),
            ('/calculators/delaware/smyrna/', '/es/calculators/delaware/smyrna/')
        ],
        '/Users/glengomezmeade/Projects/plasma-pay-calculator/es/calculators/iowa/index.html': [
            ('/calculators/iowa/waterloo/', '/es/calculators/iowa/waterloo/'),
            ('/calculators/iowa/des-moines/', '/es/calculators/iowa/des-moines/'),
            ('/calculators/iowa/cedar-rapids/', '/es/calculators/iowa/cedar-rapids/'),
            ('/calculators/iowa/davenport/', '/es/calculators/iowa/davenport/'),
            ('/calculators/iowa/sioux-city/', '/es/calculators/iowa/sioux-city/')
        ],
        '/Users/glengomezmeade/Projects/plasma-pay-calculator/es/calculators/new-hampshire/index.html': [
            ('/calculators/new-hampshire/manchester-nh/', '/es/calculators/new-hampshire/manchester/'),
            ('/calculators/new-hampshire/concord-nh/', '/es/calculators/new-hampshire/concord/'),
            ('/calculators/new-hampshire/derry/', '/es/calculators/new-hampshire/derry/'),
            ('/calculators/new-hampshire/rochester-nh/', '/es/calculators/new-hampshire/rochester/'),
            ('/calculators/new-hampshire/nashua/', '/es/calculators/new-hampshire/nashua/')
        ],
        '/Users/glengomezmeade/Projects/plasma-pay-calculator/es/calculators/west-virginia/index.html': [
            ('/calculators/west-virginia/charleston-wv/', '/es/calculators/west-virginia/charleston/'),
            ('/calculators/west-virginia/huntington/', '/es/calculators/west-virginia/huntington/'),
            ('/calculators/west-virginia/parkersburg/', '/es/calculators/west-virginia/parkersburg/'),
            ('/calculators/west-virginia/morgantown/', '/es/calculators/west-virginia/morgantown/'),
            ('/calculators/west-virginia/wheeling/', '/es/calculators/west-virginia/wheeling/')
        ],
        '/Users/glengomezmeade/Projects/plasma-pay-calculator/es/calculators/south-dakota/index.html': [
            ('/calculators/south-dakota/watertown-sd/', '/es/calculators/south-dakota/watertown/'),
            ('/calculators/south-dakota/sioux-falls/', '/es/calculators/south-dakota/sioux-falls/'),
            ('/calculators/south-dakota/rapid-city/', '/es/calculators/south-dakota/rapid-city/'),
            ('/calculators/south-dakota/aberdeen/', '/es/calculators/south-dakota/aberdeen/'),
            ('/calculators/south-dakota/brookings/', '/es/calculators/south-dakota/brookings/')
        ],
        '/Users/glengomezmeade/Projects/plasma-pay-calculator/es/calculators/south-carolina/index.html': [
            ('/calculators/south-carolina/columbia-sc/', '/es/calculators/south-carolina/columbia/'),
            ('/calculators/south-carolina/greenville/', '/es/calculators/south-carolina/greenville/'),
            ('/calculators/south-carolina/charleston/', '/es/calculators/south-carolina/charleston/'),
            ('/calculators/south-carolina/north-charleston/', '/es/calculators/south-carolina/north-charleston/'),
            ('/calculators/south-carolina/rock-hill/', '/es/calculators/south-carolina/rock-hill/')
        ],
        '/Users/glengomezmeade/Projects/plasma-pay-calculator/es/calculators/montana/index.html': [
            ('/calculators/montana/helena/', '/es/calculators/montana/helena/'),
            ('/calculators/montana/billings/', '/es/calculators/montana/billings/'),
            ('/calculators/montana/missoula/', '/es/calculators/montana/missoula/'),
            ('/calculators/montana/great-falls/', '/es/calculators/montana/great-falls/'),
            ('/calculators/montana/bozeman/', '/es/calculators/montana/bozeman/')
        ],
        '/Users/glengomezmeade/Projects/plasma-pay-calculator/es/calculators/minnesota/index.html': [
            ('/calculators/minnesota/st-paul/', '/es/calculators/minnesota/st-paul/'),
            ('/calculators/minnesota/rochester-mn/', '/es/calculators/minnesota/rochester/'),
            ('/calculators/minnesota/bloomington-mn/', '/es/calculators/minnesota/bloomington/'),
            ('/calculators/minnesota/minneapolis/', '/es/calculators/minnesota/minneapolis/'),
            ('/calculators/minnesota/duluth/', '/es/calculators/minnesota/duluth/')
        ],
        '/Users/glengomezmeade/Projects/plasma-pay-calculator/es/calculators/hawaii/index.html': [
            ('/calculators/hawaii/kailua-hi/', '/es/calculators/hawaii/kailua/'),
            ('/calculators/hawaii/honolulu/', '/es/calculators/hawaii/honolulu/'),
            ('/calculators/hawaii/hilo/', '/es/calculators/hawaii/hilo/'),
            ('/calculators/hawaii/pearl-city/', '/es/calculators/hawaii/pearl-city/'),
            ('/calculators/hawaii/kaneohe/', '/es/calculators/hawaii/kaneohe/')
        ],
        '/Users/glengomezmeade/Projects/plasma-pay-calculator/es/calculators/kansas/index.html': [
            ('/calculators/kansas/kansas-city-ks/', '/es/calculators/kansas/kansas-city/'),
            ('/calculators/kansas/wichita/', '/es/calculators/kansas/wichita/'),
            ('/calculators/kansas/overland-park/', '/es/calculators/kansas/overland-park/'),
            ('/calculators/kansas/topeka/', '/es/calculators/kansas/topeka/'),
            ('/calculators/kansas/olathe/', '/es/calculators/kansas/olathe/')
        ],
        '/Users/glengomezmeade/Projects/plasma-pay-calculator/es/calculators/nebraska/index.html': [
            ('/calculators/nebraska/bellevue-ne/', '/es/calculators/nebraska/bellevue/'),
            ('/calculators/nebraska/omaha/', '/es/calculators/nebraska/omaha/'),
            ('/calculators/nebraska/lincoln/', '/es/calculators/nebraska/lincoln/'),
            ('/calculators/nebraska/grand-island/', '/es/calculators/nebraska/grand-island/'),
            ('/calculators/nebraska/kearney/', '/es/calculators/nebraska/kearney/')
        ],
        '/Users/glengomezmeade/Projects/plasma-pay-calculator/es/calculators/new-jersey/index.html': [
            ('/calculators/new-jersey/newark/', '/es/calculators/new-jersey/newark/'),
            ('/calculators/new-jersey/jersey-city/', '/es/calculators/new-jersey/jersey-city/'),
            ('/calculators/new-jersey/paterson/', '/es/calculators/new-jersey/paterson/'),
            ('/calculators/new-jersey/elizabeth/', '/es/calculators/new-jersey/elizabeth/'),
            ('/calculators/new-jersey/edison/', '/es/calculators/new-jersey/edison/')
        ],
        '/Users/glengomezmeade/Projects/plasma-pay-calculator/es/calculators/oregon/index.html': [
            ('/calculators/oregon/salem-or/', '/es/calculators/oregon/salem/'),
            ('/calculators/oregon/portland/', '/es/calculators/oregon/portland/'),
            ('/calculators/oregon/eugene/', '/es/calculators/oregon/eugene/'),
            ('/calculators/oregon/gresham/', '/es/calculators/oregon/gresham/'),
            ('/calculators/oregon/hillsboro/', '/es/calculators/oregon/hillsboro/')
        ]
    }
    
    for file_path, replacements in spanish_fixes.items():
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                content = f.read()
            
            for old_link, new_link in replacements:
                # Fix both in href and onclick handlers
                content = content.replace(f'href="{old_link}"', f'href="{new_link}"')
                content = content.replace(f"location.href='{old_link}'", f"location.href='{new_link}'")
                # Also fix escaped quotes
                content = content.replace(f"\\&quot;location.href='{old_link}'\\&quot;", f"\\&quot;location.href='{new_link}'\\&quot;")
                
            with open(file_path, 'w') as f:
                f.write(content)
            
            state_name = os.path.basename(os.path.dirname(file_path))
            print(f"Fixed {state_name} to use Spanish calculator links")
            fixes_made += 1
    
    print(f"\nTotal files fixed: {fixes_made}")
    return fixes_made

if __name__ == "__main__":
    fix_spanish_links_properly()