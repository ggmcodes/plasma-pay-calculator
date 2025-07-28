#!/bin/bash

# Submit ALL pages to IndexNow in batches

echo "Finding all HTML pages..."
ALL_URLS=$(find . -name "*.html" -type f | grep -v node_modules | sed 's|^\./||' | sed 's|^|https://plasmapaycalculator.com/|')

# Convert to array
URLS_ARRAY=($ALL_URLS)
TOTAL=${#URLS_ARRAY[@]}

echo "Found $TOTAL pages to submit"

# Submit in batches of 100 (to avoid command line limits)
BATCH_SIZE=100
for ((i=0; i<$TOTAL; i+=BATCH_SIZE)); do
    BATCH=("${URLS_ARRAY[@]:$i:$BATCH_SIZE}")
    echo "Submitting batch $((i/BATCH_SIZE + 1)) (${#BATCH[@]} URLs)..."
    node submit-indexnow.js "${BATCH[@]}"
    sleep 1  # Small delay between batches
done

echo "All $TOTAL pages submitted to IndexNow!"