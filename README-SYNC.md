# 🔄 Auto-Sync Guide

## Quick Start

### When you START working:
```bash
./sync-start.sh
```
This downloads any changes from GitHub (like changes you made at home).

### When you're DONE working:
```bash
./sync-done.sh
```
This saves your changes to GitHub automatically.

## That's it! 🎉

### What if I forget?
- If you forget to run `sync-start.sh`, you might get conflicts
- If you forget to run `sync-done.sh`, your changes won't be on GitHub
- Don't worry - Git will tell you what to do if something goes wrong

### Tips:
1. Always run `sync-start.sh` first
2. Make your changes
3. Run `sync-done.sh` when done
4. At home, do the same thing!

### Common Issues:
- **"Push failed"**: Someone else (or you at home) made changes. Run `./sync-start.sh` first
- **"You have uncommitted changes"**: Run `./sync-done.sh` to save them first