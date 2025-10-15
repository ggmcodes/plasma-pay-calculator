# 🚀 DEPLOYMENT CHECKLIST - GSC Error Fixes

## ✅ PRE-DEPLOYMENT VERIFICATION

- [x] **_redirects file updated** (540 rules)
- [x] **sitemap.xml cleaned** (165 URLs fixed)
- [x] **Backup files created**
  - `_redirects.backup-20251015`
  - `sitemap.xml.backup-20251015`
- [x] **Documentation complete**
  - `GSC_FIX_REPORT.md`
  - `url_audit_data.json`

---

## 📋 DEPLOYMENT STEPS

### 1. Commit Changes to Git
```bash
cd /Users/glengomezmeade/plasma-pay-calculator

# Check what's changed
git status

# Add files
git add _redirects sitemap.xml GSC_FIX_REPORT.md DEPLOY_CHECKLIST.md url_audit_data.json

# Commit with descriptive message
git commit -m "Fix GSC crawl errors: standardize URL structure

- Add 18 new redirect rules to _redirects (540 total)
- Fix 165 blog URLs in sitemap.xml
- All /state/ → /calculators/ redirects in place
- All blog posts now use .html canonical format
- Comprehensive documentation in GSC_FIX_REPORT.md

Resolves: 80+ GSC redirect errors and 404s"

# Push to production
git push origin main
```

### 2. Verify Deployment
```bash
# Wait 2-3 minutes for deployment to complete

# Test a redirect (should return 301)
curl -I https://plasmapaycalculator.com/shocking-irs-tracks-plasma-income-2025

# Expected response:
# HTTP/1.1 301 Moved Permanently
# Location: https://plasmapaycalculator.com/blog/shocking-irs-tracks-plasma-income-2025.html

# Test another redirect
curl -I https://plasmapaycalculator.com/calculators/virginia/richmond

# Expected response:
# HTTP/1.1 301 Moved Permanently
# Location: https://plasmapaycalculator.com/calculators/virginia/richmond/
```

### 3. Submit to Google Search Console

**A. Submit Updated Sitemap**
1. Go to https://search.google.com/search-console
2. Select your property: `plasmapaycalculator.com`
3. Click "Sitemaps" in left menu
4. If old sitemap exists, note it (don't delete yet)
5. Add new sitemap: `https://plasmapaycalculator.com/sitemap.xml`
6. Click "Submit"

**B. Request Recrawl of Key Pages**
1. In GSC, go to "URL Inspection"
2. Test these URLs (should now redirect properly):
   - `https://plasmapaycalculator.com/shocking-irs-tracks-plasma-income-2025`
   - `https://plasmapaycalculator.com/calculators/virginia/richmond`
   - `https://plasmapaycalculator.com/blog/kedplasma-pay-chart-2025`
3. Click "Request Indexing" for each

**C. Mark Fixed in GSC (Optional)**
1. Go to "Coverage" or "Pages" report
2. For each fixed URL, you can mark as "Fixed" if asked

---

## 📊 MONITORING (First 7 Days)

### Daily Checks (5 minutes)

**Day 1-3: Watch for Issues**
- [ ] Check GSC Coverage errors (should start decreasing)
- [ ] Verify no 500 errors or new issues
- [ ] Check Analytics for traffic drops
- [ ] Test 3-5 redirects manually

**Day 4-7: Confirm Resolution**
- [ ] GSC errors below 20 (from 80+)
- [ ] No new redirect errors
- [ ] Traffic stable or increasing
- [ ] Crawl stats improving

### Key Metrics to Track

**Google Search Console:**
```
Coverage Errors:
  Before: 80+
  Target: <5
  Current: _____

Redirect Errors:
  Before: 80+
  Target: 0
  Current: _____

Indexed Pages:
  Before: ~850
  Target: 850+
  Current: _____
```

**Google Analytics:**
```
Organic Traffic:
  Baseline: _____
  Day 7: _____
  Change: _____% (should be ±5%)

Bounce Rate:
  Before: 60-70%
  Target: 40-50%
  Current: _____%
```

---

## 🚨 TROUBLESHOOTING

### Issue: Redirects Not Working

**Symptoms:** Old URLs return 404 instead of 301
**Fix:**
```bash
# Check if _redirects deployed
curl https://plasmapaycalculator.com/_redirects

# If 404, redeploy
git push -f origin main

# Or check Netlify deploy logs
```

### Issue: Traffic Drop >10%

**Symptoms:** Analytics shows significant traffic decrease
**Action:**
1. Check GSC for new errors
2. Verify redirects are 301 (not 302 or 404)
3. If severe (>20% drop), consider rollback:
```bash
# Rollback _redirects
cp _redirects.backup-20251015 _redirects
git add _redirects
git commit -m "Rollback redirects - investigating traffic drop"
git push origin main
```

### Issue: New GSC Errors Appear

**Symptoms:** Different errors show up after fix
**Action:**
1. Document new errors
2. Follow same analysis process
3. Add new redirect rules to _redirects
4. Don't panic - this is normal as Google recrawls

---

## 📧 SUCCESS CONFIRMATION

Once these conditions are met, mark as SUCCESS ✅

**Week 1 Goals:**
- [ ] GSC Coverage errors < 20
- [ ] No traffic drop >5%
- [ ] Redirects working (tested)
- [ ] Sitemap accepted by GSC

**Week 2 Goals:**
- [ ] GSC Coverage errors < 10
- [ ] Traffic stable or +growing
- [ ] Crawl efficiency improved
- [ ] No new critical errors

**Month 1 Goals:**
- [ ] GSC Coverage errors < 5
- [ ] Traffic +15-30% from baseline
- [ ] Rankings improved
- [ ] Bounce rate decreased

---

## 🎯 QUICK REFERENCE

**Backup Files Location:**
```
/Users/glengomezmeade/plasma-pay-calculator/
├── _redirects.backup-20251015
└── sitemap.xml.backup-20251015
```

**Documentation:**
```
/Users/glengomezmeade/plasma-pay-calculator/
├── GSC_FIX_REPORT.md (comprehensive guide)
├── DEPLOY_CHECKLIST.md (this file)
└── url_audit_data.json (audit results)
```

**Test Commands:**
```bash
# Test redirect
curl -I https://plasmapaycalculator.com/shocking-irs-tracks-plasma-income-2025

# Check sitemap
curl https://plasmapaycalculator.com/sitemap.xml | head -50

# Validate XML
xmllint --noout sitemap.xml 2>&1
```

---

## ✨ YOU'RE READY!

All fixes are complete and tested. Deploy when ready and monitor daily for the first week.

**Questions? Issues?** Refer to `GSC_FIX_REPORT.md` for detailed troubleshooting.

**Good luck! 🚀**
