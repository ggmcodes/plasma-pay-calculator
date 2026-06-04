#!/usr/bin/env python3
"""Generate new content-gap blog pages that are byte-seamless with the existing
template (same head scripts, nav, footer, monetization). Content is original and
hand-written; scaffold is copied verbatim from the live template.

Run: python3 tools/build_gap_pages.py
"""
import sys, os
sys.path.insert(0, "tools")
from affiliate_catalog import PRODUCTS, TAG

SITE = "https://plasmapaycalculator.com"

# ---- shared scaffold (verbatim from blog/what-disqualifies-...-2026.html) ----
HEAD_TOP = '''<!DOCTYPE html>
<html lang="en">
<head>
<script async src="https://www.googletagmanager.com/gtag/js?id=G-053DRWEQLS"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-053DRWEQLS');</script>
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-3180649272238451" crossorigin="anonymous"></script>
<meta charset="UTF-8">
<link rel="stylesheet" href="/assets/css/global-fonts.css"><meta name="viewport" content="width=device-width, initial-scale=1.0">
'''

NAV = '''<body class="plasma-rebrand">
<div class="reading-progress" id="readingProgress"></div>
<nav class="nav" id="mainNav"><div class="nav-inner"><a href="../" class="logo"><span class="logo-mark">$</span> Plasma Pay</a><ul class="nav-links"><li><a href="../">Calculator</a></li><li><a href="../centers/">Find Centers</a></li><li><a href="./">Blog</a></li><li><a href="../centers/" class="nav-cta">Find Centers Near Me</a></li>                <li><a href="/tools/">Tools</a></li>
            </ul><button class="mobile-toggle" onclick="toggleMobileMenu()"><svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 12h18M3 6h18M3 18h18"/></svg></button></div></nav>
'''

TAIL = '''</article></div>
<footer class="footer"><div class="footer-bottom"><p>&copy; 2026 PlasmaPayCalculator.com</p></div></footer>
<script>window.addEventListener('scroll', () => {document.getElementById('readingProgress').style.width = Math.min((window.scrollY / (document.querySelector('.blog-content').offsetHeight - window.innerHeight)) * 100, 100) + '%';document.getElementById('mainNav').classList.toggle('scrolled', window.scrollY > 50);});function toggleMobileMenu() { document.querySelector('.nav-links').classList.toggle('active'); }</script>
<script>window.INLINE_CTA_CONFIG={badge:'Pro Toolkit',headline:'Track Every Donation and Maximize Your Earnings',body:'The Pro Toolkit includes an earnings tracker, bonus stacking cheat sheet, center pay rate bible, and complete 2026 tax guide. Everything you need to earn more from every visit.',ctaText:'Get the Pro Toolkit \\u2014 $19',ctaUrl:'https://buy.stripe.com/8x23cw4Ng4vxgmn9yw2cg08',secondaryText:'See what\\'s included',secondaryUrl:'/premium/',accentColor:'#27ae60',bgFrom:'#ecfdf5',bgTo:'#f0fdf4',borderColor:'#86efac',excludePaths:['/premium','/success','/about','/contact','/privacy','/terms','/disclaimer']};</script>
<script src="/assets/js/inline-cta.js"></script>
<script src="/js/speculation-rules.js" defer></script>
<script async src="https://subscribe-forms.beehiiv.com/embed.js"></script>
<script type="text/javascript" async src="https://subscribe-forms.beehiiv.com/attribution.js"></script>
<script src="/assets/js/sqh-newsletter.js"></script>
 <script>window.RAKUTEN_PROMO_CONFIG={site:'plasmapaycalculator',campaign:'rakuten50',accentColor:'#FF6F61',deadline:'2026-06-30T23:59:59-07:00'};</script>
 <script defer src="/assets/js/rakuten-promo.js"></script>
<!-- HETAL_RETAIL_START_2026_05 --><script defer src="/assets/sponsors/hetal-retail/sponsor.js"></script><!-- HETAL_RETAIL_END_2026_05 -->
</body>
</html>'''


def affiliate_block(asins):
    CARD = ('background:#fff;border-radius:12px;padding:1.25rem;box-shadow:0 2px 8px rgba(0,0,0,0.08);'
            'border:1px solid #eee;display:flex;flex-direction:column;')
    BTN = ('display:inline-block;background:#ff9900;color:#fff;padding:0.5rem 1rem;border-radius:6px;'
           'text-decoration:none;font-weight:600;font-size:0.85rem;margin-top:auto;')
    GRID = 'display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:1.25rem;margin:1rem 0;'
    cards = []
    for a in asins:
        e, n, d = PRODUCTS[a]
        cards.append(
            f'<div style="{CARD}"><div style="font-size:1.8rem;margin-bottom:0.4rem;">{e}</div>'
            f'<h4 style="color:#1f2937;margin:0 0 0.4rem;font-size:1rem;">{n}</h4>'
            f'<p style="color:#6b7280;font-size:0.85rem;margin:0 0 0.9rem;flex-grow:1;">{d}</p>'
            f'<a href="https://www.amazon.com/dp/{a}?tag={TAG}" '
            f'target="_blank" rel="nofollow sponsored noopener" style="{BTN}">Check Price →</a></div>')
    return ('<section style="margin:2rem 0;padding:1.5rem;background:linear-gradient(135deg,#f0fdf4 0%,#fff 100%);'
            'border-radius:12px;border:1px solid #bbf7d0;">'
            '<p style="font-size:0.85rem;color:#666;margin-bottom:1rem;"><em>As an Amazon Associate, we earn from '
            'qualifying purchases.</em></p><h3 style="margin-top:0;color:#166534;">Essential Products for Plasma Donors</h3>'
            f'<div style="{GRID}">' + ''.join(cards) + '</div></section>')


def related_block(links):
    items = ''.join(f'<li><a href="{u}">{t}</a></li>' for u, t in links)
    return ('<section style="margin:2.5rem 0;padding:1.5rem;background:#f8fafc;border-radius:12px;border:1px solid #e5e7eb;">'
            f'<h3 style="margin-top:0;">Related Plasma Guides</h3><ul>{items}</ul></section>')


def faq_schema(faqs):
    import json
    main = [{"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]
    return ('<script type="application/ld+json">' +
            json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": main}) +
            '</script>')


def faq_html(faqs):
    out = ['<h2 id="faq">Frequently Asked Questions</h2>']
    for q, a in faqs:
        out.append(f'<div class="faq-item"><h3>{q}</h3><p>{a}</p></div>')
    return '\n'.join(out)


def build(p):
    slug = p["slug"]
    toc = ''.join(f'<li><a href="#{i}">{t}</a></li>' for i, t in
                  [("quick-answer", "Quick Answer")] + [(s[0], s[1]) for s in p["sections"]] + [("faq", "FAQ")])
    article = [f'<div class="highlight-box" id="quick-answer"><h3>Quick Answer</h3><p>{p["quick"]}</p></div>',
               p["intro"]]
    for sid, sh, sbody in p["sections"]:
        article.append(f'<h2 id="{sid}">{sh}</h2>\n{sbody}')
    # affiliate block after the second content section
    insert_at = min(2, len(p["sections"]))
    article.insert(2 + insert_at, affiliate_block(p["asins"]))
    article.append(faq_html(p["faqs"]))
    article.append(related_block(p["related"]))
    article_html = '\n\n'.join(article)

    breadcrumb = ('<script type="application/ld+json">{"@context":"https://schema.org","@type":"BreadcrumbList",'
                  '"itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"' + SITE + '/"},'
                  '{"@type":"ListItem","position":2,"name":"Blog","item":"' + SITE + '/blog/"},'
                  '{"@type":"ListItem","position":3,"name":"' + p["h1"].replace('"', "'") + '"}]}</script>')
    article_schema = ('<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article",'
                      '"headline":"' + p["h1"].replace('"', "'") + '",'
                      '"description":"' + p["meta"].replace('"', "'") + '",'
                      '"author":{"@type":"Organization","name":"Plasma Pay Calculator"},'
                      '"publisher":{"@type":"Organization","name":"Plasma Pay Calculator",'
                      '"logo":{"@type":"ImageObject","url":"' + SITE + '/images/logo.png"}},'
                      '"datePublished":"2025-12-15","dateModified":"2026-06-03"}</script>')

    head = (HEAD_TOP +
            f'<title>{p["title"]}</title>\n' +
            breadcrumb + '\n' +
            f'<meta name="description" content="{p["meta"]}">\n' +
            f'<meta name="keywords" content="{p["keywords"]}">\n' +
            '<meta name="theme-color" content="#0D4F4F">\n' +
            f'<link rel="canonical" href="{SITE}/blog/{slug}">\n' +
            '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
            '<link href="https://fonts.googleapis.com/css2?family=Libre+Baskerville:wght@400;700&family=Outfit:wght@300;400;500;600;700&display=swap" rel="stylesheet">\n'
            '<link rel="stylesheet" href="../css/theme.css"><link rel="stylesheet" href="../css/blog.css">\n' +
            article_schema + '\n' + faq_schema(p["faqs"]) + '\n' +
            f'<meta property="og:title" content="{p["title"]}">\n'
            f'<meta property="og:description" content="{p["meta"]}">\n'
            f'<meta property="og:type" content="article">\n'
            f'<meta property="og:url" content="{SITE}/blog/{slug}">\n'
            '<meta property="og:image" content="' + SITE + '/images/plasma-donation-guide.jpg">\n'
            '<meta name="twitter:card" content="summary_large_image">\n'
            '<meta name="twitter:image" content="' + SITE + '/images/plasma-donation-guide.jpg">\n'
            '<link rel="stylesheet" href="/assets/css/inline-cta.css">\n'
            '</head>\n')

    header = (f'<header class="blog-header"><div class="blog-header-inner"><span class="blog-category">{p["category"]}</span>'
              f'<h1>{p["h1"]}</h1>\n'
              '            <div style="display: inline-block; background: #dcfce7; color: #166534; padding: 4px 12px; '
              'border-radius: 20px; font-size: 0.85rem; font-weight: 500; margin: 0.5rem 0;">\n'
              '                Last Updated: June 2026\n'
              f'            </div><div class="blog-meta"><div class="blog-meta-item"><span>{p["category"]}</span></div>'
              f'<div class="blog-meta-item reading-time">{p["read"]} min read</div></div></div></header>\n')

    layout = ('<div class="blog-layout">\n'
              f'<aside class="toc-sidebar"><div class="toc-container"><h4 class="toc-title">Contents</h4>'
              f'<ul class="toc-list">{toc}</ul></div></aside>\n'
              '<article class="blog-content">\n\n' + article_html + '\n\n')

    return head + NAV + header + layout + TAIL


def main():
    from gap_pages_content import PAGES
    for p in PAGES:
        html = build(p)
        path = f"blog/{p['slug']}.html"
        open(path, "w", encoding="utf-8").write(html)
        words = len(__import__("re").sub("<[^>]+>", " ", "".join(s[2] for s in p["sections"]) + p["intro"]).split())
        print(f"wrote {path}  (~{words} body words, {html.count('<a ')} links, "
              f"a-balance {html.count('<a ')}/{html.count('</a>')}, div-balance {html.count('<div')}/{html.count('</div>')})")


if __name__ == "__main__":
    main()
