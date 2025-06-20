#!/bin/bash
# Auto-sync script - Run this when you're DONE working

echo "🔄 Saving your work to GitHub..."

# Check if there are changes
if [ -z "$(git status --porcelain)" ]; then
    echo "✅ No changes to save. You're all good!"
    exit 0
fi

# Show what changed
echo "📝 Here's what changed:"
git status --short

# Add all changes
git add .

# Commit with timestamp
timestamp=$(date +"%Y-%m-%d %H:%M")
git commit -m "Auto-save: $timestamp"

# Push to GitHub
git push origin main

if [ $? -eq 0 ]; then
    echo "✅ Successfully saved to GitHub!"
    echo "🏠 You can now access these changes from your home computer."
else
    echo "❌ Push failed. You might need to pull first:"
    echo "Run: git pull origin main"
fi