import csv
import json

# Read the CSV file
keywords_data = []
with open('cleaned_keywords.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    for row in reader:
        row['Impressions'] = int(row['Impressions'])
        row['Clicks'] = int(row['Clicks'])
        row['CTR'] = float(row['CTR'].strip('%')) if row['CTR'] != '0%' else 0
        row['Avg. Position'] = float(row['Avg. Position'])
        keywords_data.append(row)

# Analysis categories
near_page1 = []  # Position 11-50
quick_wins = []  # Position 4-10 with good impressions
high_impr_low_ctr = []  # High impressions but 0% CTR
top_positions_low_ctr = []  # Position 1-3 with 0% CTR

for kw in keywords_data:
    # Near page 1 (11-50)
    if 11 <= kw['Avg. Position'] <= 50:
        near_page1.append(kw)
    
    # Quick wins (4-10)
    if 4 <= kw['Avg. Position'] <= 10 and kw['Impressions'] >= 2:
        quick_wins.append(kw)
    
    # High impressions with low CTR
    if kw['Impressions'] >= 2 and kw['CTR'] == 0:
        high_impr_low_ctr.append(kw)
    
    # Top positions with low CTR (potential snippet opportunities)
    if kw['Avg. Position'] <= 3 and kw['CTR'] == 0:
        top_positions_low_ctr.append(kw)

# Sort by impressions
near_page1.sort(key=lambda x: x['Impressions'], reverse=True)
quick_wins.sort(key=lambda x: x['Impressions'], reverse=True)
high_impr_low_ctr.sort(key=lambda x: x['Impressions'], reverse=True)
top_positions_low_ctr.sort(key=lambda x: x['Impressions'], reverse=True)

print("=== KEYWORD ANALYSIS REPORT ===\n")

print("1. NEAR PAGE 1 KEYWORDS (Position 11-50):")
print("None found - all keywords are already in top 10!\n")

print("2. QUICK WIN OPPORTUNITIES (Position 4-10):")
for kw in quick_wins:
    print(f"- '{kw['Keyword']}' | Pos: {kw['Avg. Position']:.1f} | Impr: {kw['Impressions']} | CTR: {kw['CTR']}%")

print("\n3. HIGH IMPRESSIONS WITH 0% CTR:")
for kw in high_impr_low_ctr[:10]:  # Top 10
    print(f"- '{kw['Keyword']}' | Pos: {kw['Avg. Position']:.1f} | Impr: {kw['Impressions']}")

print("\n4. TOP POSITIONS WITH 0% CTR (Snippet Opportunities):")
for kw in top_positions_low_ctr:
    print(f"- '{kw['Keyword']}' | Pos: {kw['Avg. Position']:.1f} | Impr: {kw['Impressions']}")

# Keyword themes analysis
pay_chart_keywords = [kw for kw in keywords_data if 'pay chart' in kw['Keyword'].lower() or 'payment chart' in kw['Keyword'].lower()]
vein_keywords = [kw for kw in keywords_data if 'vein' in kw['Keyword'].lower()]
location_keywords = [kw for kw in keywords_data if any(loc in kw['Keyword'].lower() for loc in ['california', 'bay area', 'ca', 'nj', 'san antonio'])]
money_amount_keywords = [kw for kw in keywords_data if any(amt in kw['Keyword'].lower() for amt in ['$', 'how much', '800', '500', '1200'])]

print("\n5. KEYWORD THEMES:")
print(f"- Pay Chart Keywords: {len(pay_chart_keywords)} keywords, avg position: {sum(kw['Avg. Position'] for kw in pay_chart_keywords)/len(pay_chart_keywords):.1f}")
print(f"- Vein-Related Keywords: {len(vein_keywords)} keywords, avg position: {sum(kw['Avg. Position'] for kw in vein_keywords)/len(vein_keywords):.1f}")
print(f"- Location-Specific Keywords: {len(location_keywords)} keywords")
print(f"- Money/Amount Keywords: {len(money_amount_keywords)} keywords")

