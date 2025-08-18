#!/bin/bash

echo "=== Fixing Subdirectory Blog Files ==="
echo ""

fixed_count=0
total_count=0

# Loop through all main blog HTML files
for main_file in /Users/glengomezmeade/Projects/plasma-pay-calculator/blog/*.html; do
    # Skip the index.html
    if [[ "$main_file" == *"/index.html" ]]; then
        continue
    fi
    
    # Get the base name without extension
    filename=$(basename "$main_file" .html)
    
    # Check if subdirectory exists
    subdir="/Users/glengomezmeade/Projects/plasma-pay-calculator/blog/$filename"
    if [ -d "$subdir" ]; then
        subdir_index="$subdir/index.html"
        total_count=$((total_count + 1))
        
        # Copy the main file content to subdirectory index
        if [ -f "$subdir_index" ]; then
            cp "$main_file" "$subdir_index"
            echo "✅ Fixed: $filename/index.html"
            fixed_count=$((fixed_count + 1))
        else
            echo "⚠️  No index.html in $filename/"
        fi
    fi
done

echo ""
echo "=== SUMMARY ==="
echo "Total subdirectories processed: $total_count"
echo "Files fixed: $fixed_count"
echo "✅ All subdirectory index.html files now have complete content!"