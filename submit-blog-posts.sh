#!/bin/bash

# Submit all blog posts to IndexNow
echo "Submitting all blog posts to IndexNow..."

# Get all blog post URLs
BLOG_URLS=$(find blog/ -name "*.html" | sed 's|^|https://plasmapaycalculator.com/|')

# Convert to space-separated list for the Node.js script
node submit-indexnow.js $BLOG_URLS

echo "Blog posts submitted to IndexNow!"