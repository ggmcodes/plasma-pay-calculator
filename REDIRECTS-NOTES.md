# _redirects annotations (moved out of _redirects: Cloudflare Pages caps the file at 64KB)

# Redirect from old domain to new domain
# Force HTTPS and remove www
# Ensure canonical URLs for main pages
# URL Structure Canonicalization Redirects
# Force HTTPS and non-www
# ===============================================
# NEW RULES FROM .HTACCESS - Added February 2026
# ===============================================
# New wildcard rules from .htaccess
# Note: trailing-slash-stripping wildcards on real directories were removed —
# they caused redirect loops against the host's directory index handling
# (301 strips slash → host 308 re-adds slash → loop).
# 2026-06-29 Hard consolidation of brand pay-chart cannibalization.
# Each pay-rates page ranked ONLY for "<brand> pay chart" terms its pay-chart sibling
# already owns better (GSC verified, zero unique winning queries). Canonicals weren't
# holding, so 301 the duplicates into the single winner per brand to merge the signals.
# CSL: collapse all three competing pages into the root authority URL (233 internal links)
# 2026-06-29 Consolidate 4 competing "biolife vs csl" comparison pages into one.
# They split ~1,174 impressions across pos 7-25 and earned 1 total click (cannibalization).
# Keep /blog/biolife-vs-csl-plasma-comparison (richest content, 20 internal links); 301 the rest.
# New static redirects from .htaccess
# ===============================================
# SPECIFIC CALCULATOR REDIRECTS
# Generated to prevent redirect chains
# ===============================================
## English State Pages
## English City Pages
## Spanish State Pages
## Spanish City Pages
# Removed: /calculators/*/ → /calculators/:splat caused infinite redirect
# loops on every state calculator (strip slash, host re-adds, repeat).
# Blog post .html redirects (remove .html)
# Specific blog post redirects mentioned in GSC
# Root page .html redirects
# Ensure clean URLs for common variations
# Fix 404 errors identified by Bing scan
# Redirect missing state pages to relevant calculators
# Redirect missing individual pages
# Health directory redirects — removed. Each /health/<topic>/ has its own
# index.html, so overriding them with 301s killed real content.
# Spanish blog post redirects - redirect to English versions since Spanish posts don't exist
# Spanish center redirects
# Removed: /es/centers/, /es/health/, /es/process/ — each has a real
# Spanish index.html page; redirecting them to /centers, /health, /process
# overrode the Spanish content with English.
# Spanish localized path aliases (nav links use Spanish words that don't
# resolve to real dirs; route to the existing English or es/ equivalent).
# Blog post renames (links point to outdated or never-created slugs)
# Spanish blog post renames
# Remaining blog renames (high-confidence fuzzy matches)
# Fallback for remaining unmapped blog posts → blog index
# Spanish blog renames
# Spanish localized root pages
# Spanish city-level calculator URLs that were never built → English equivalents
# Spanish health redirects
# Spanish page redirects
# Additional missing blog posts
# Replace meta refresh redirects with proper 301 redirects
# COMPREHENSIVE GSC REDIRECT FIXES
# =====================================
# 1. COMPREHENSIVE .HTML REMOVAL RULES
# Remove .html from all calculator pages (English)
# Remove .html from all Spanish calculator pages
# 2. COMPREHENSIVE STATE-TO-CALCULATOR REDIRECTS
# English state redirects (all patterns)
# Spanish state redirects (all patterns)
# 3. BLOG TRAILING SLASH FIXES
# Remove trailing slashes from blog posts
# 4. ROOT PAGE REDIRECTS
# 5. WWW SUBDOMAIN FIXES (additional patterns)
# 6. SPECIFIC GSC ERROR REDIRECTS
# Blog post specific redirects
# Root level page redirects
# Removed: /states/ → /states — /states/ serves states/index.html; this
# rule stripped the slash which the host then re-added, looping.
# Tools directory
# Spanish blog redirects
# Removed: /es/ → /es and /blog/california/ → /blog/ — both targeted
# real directories with index.html and caused loops or clobbered content.
# SPECIFIC 404 ERROR FIXES FROM GSC
# ==================================
# Missing California blog posts (redirect to existing ones or main blog)
# Missing Spanish blog posts
# Wrong calculator directory names (missing state suffixes)
# Double calculator path fix
# Tools redirects
# State page redirects (missing .html files)
# Spanish calculator directory redirect
# Spanish blog post that doesn't exist
# SPECIFIC GSC ERROR URL REDIRECTS
# =================================
# Calculator trailing slash variations
# State directory without .html
# Specific city calculator redirects without .html
# Additional calculator city redirects
# Missing state directories
# State page redirects (.html variations)
# ============================================================
# ADDITIONAL GSC ERROR FIXES - October 2025
# Added: 2025-10-15 - New crawl errors from GSC
# ============================================================
# Blog posts at root that should be in /blog/ (not covered by existing wildcards)
# Missing blog post - redirect to similar content
# Calculator pages that need trailing slashes  
# Blog post variations
# KEDPlasma specific (redirect to highest-paying centers)
# ===============================================
# GSC 404 ERROR FIXES - December 2025
# ===============================================
# Blog post filename variations (missing "2025" suffix or different names)
# Non-existent blog posts - redirect to similar content
# Blog post trailing slash and URL variations
# Singular /center/ to plural /centers/ redirect (fix for app.js bug)
# Duplicate calculators path fix
# Legacy state path redirects (if not already covered by existing rules)
# Redirects for deleted Spanish blog pages (consolidated to English versions)
# Redirects for deleted/renamed blog pages
# California stub page redirects
# ===============================================
# GSC 404 FIXES - February 2026
# ===============================================
# Missing blog slugs (no .html extension in GSC URL)
# Blog path pointing to root-level file
# Double .html extension (scraper/bot generated bad URL)
# Weird crawler paths
# Missing Spanish pages
# Affiliate / referral short URLs (Rakuten $50 — expires 2026-06-30)
# 2026-07-02 link audit: dead blog URLs -> closest existing page

## 2026-07-02 link audit findings (Claude)
- Cloudflare Pages hard limits: _redirects max 64KB, 2,000 static + 100 dynamic rules.
- CRITICAL GOTCHA: a mid-pattern splat source (e.g. `/blog/*.html`) is invalid and Pages
  silently stops parsing there — every rule after it is dead. A `/blog/*.html /blog/:splat`
  rule at ~line 106 had disabled ~85% of this file (588 rules) for months.
- .html -> clean-URL rules are unnecessary: Pages 308-normalizes automatically when the asset exists.
- Absolute-URL sources (https://domain/*) are Netlify syntax, no-ops on Pages; use zone-level
  Bulk Redirects for cross-domain (bestplasmacenters.com).
- All 686 rules verified 2026-07-02: loop-free, every final target serves content.
