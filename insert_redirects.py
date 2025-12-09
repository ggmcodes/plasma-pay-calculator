#!/usr/bin/env python3
"""
Insert generated calculator redirects into _redirects file.
Places them after line 20 (after domain/protocol redirects).
"""

def main():
    print("=== INSERTING REDIRECTS INTO _redirects FILE ===\n")
    
    # Read existing _redirects
    with open('_redirects', 'r') as f:
        existing_lines = f.readlines()
    
    # Read generated redirects
    with open('calculator_redirects.txt', 'r') as f:
        new_redirects = f.read()
    
    # Find insertion point (after line 20)
    # Insert after the HTTPS/www normalization section
    insertion_line = 20
    
    print(f"Current _redirects file: {len(existing_lines)} lines")
    print(f"Inserting after line {insertion_line}...")
    
    # Create new file content
    new_content = []
    
    # Add first 20 lines
    new_content.extend(existing_lines[:insertion_line])
    
    # Add blank line and new redirects
    new_content.append('\n')
    new_content.append(new_redirects)
    new_content.append('\n\n')
    
    # Add rest of existing redirects
    new_content.extend(existing_lines[insertion_line:])
    
    # Write updated file
    with open('_redirects', 'w') as f:
        f.writelines(new_content)
    
    # Count final lines
    final_lines = len([l for l in new_content if l.strip()])
    
    print(f"\n✓ Updated _redirects file")
    print(f"✓ New file size: ~{sum(len(l) for l in new_content) // 1024}KB")
    print(f"✓ Approximate line count: {len(new_content)}")
    print(f"\nRedirects inserted successfully!")
    print(f"Ready to commit and deploy.")

if __name__ == '__main__':
    main()
