#!/bin/bash
# Auto-sync script - Run this when you START working

echo "🔄 Syncing with GitHub..."

# Pull latest changes
git pull origin main

if [ $? -eq 0 ]; then
    echo "✅ Successfully synced! You're up to date."
else
    echo "❌ Sync failed. You might have uncommitted changes."
    echo "Run 'git status' to see what's going on."
fi