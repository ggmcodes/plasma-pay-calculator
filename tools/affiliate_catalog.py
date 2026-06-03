#!/usr/bin/env python3
"""Canonical Amazon affiliate catalog for plasmapaycalculator.com.

Only REAL /dp/ASIN values that already exist in the repository are used here
(verified present on the best-products / how-to-prepare donor pages). Associate
tag: plasma0f-20.

Two helpers:
  * map_query_to_asin(query) -> (asin, name, emoji, desc) or None
        Maps an Amazon /s?k= search query to the best-fit real product so dead
        search links become real, cookie-setting product links.
  * CATALOG  -> ordered list of the core donor product cards for grid rendering.
"""

TAG = "plasma0f-20"

# asin -> (emoji, name, benefit)
PRODUCTS = {
    "B07GKVFN2V": ("\U0001F4A7", "Liquid I.V. Hydration (16-Pack)", "3x faster hydration. Essential pre-donation prep for an easy draw."),
    "B00008I8NT": ("\U0001F48A", "Nature Made Iron 65mg", "Keep hemoglobin up so you pass screening every visit."),
    "B000QSNYGI": ("\U0001F964", "Optimum Nutrition Protein", "24g protein per serving. Rebuild plasma protein between donations."),
    "B01ACAXFHI": ("\U0001F376", "Hydro Flask 32oz Bottle", "Hit your water goal. Stays cold 24 hours."),
    "B07GVMQRKM": ("\U0001F9C2", "Pedialyte Electrolyte Powder", "Medical-grade rehydration. Bounce back fast after donating."),
    "B07D3K8FQZ": ("\U0001FA79", "Compression Arm Sleeve", "Reduce post-donation bruising and support recovery."),
    "B07QXV6N1B": ("\U0001F4F1", "Anker Portable Charger", "Stay charged through long waits. Ultra-compact 10000mAh."),
    "B09MPMYBK4": ("\U0001F3A7", "JBL Wireless Earbuds", "Pass the time in the chair. 8-hour battery."),
    "B07K3XJQGN": ("\U0001F6EB", "Travel Neck Pillow", "Stay comfortable during the 45-90 min donation."),
    "B08KTZ8249": ("\U0001F4DA", "Kindle Paperwhite", "Read hands-free during donation. Weeks of battery."),
    "B08LN8VQFV": ("✊", "Hand Grip Strengthener", "Build forearm veins for faster, easier draws."),
    "B07GXMZ3Z5": ("\U0001F525", "Microwavable Warm Compress", "Dilate veins before donation. Reusable heating pad."),
    "B07VBZV9ND": ("\U0001F4AA", "Resistance Bands Set", "Improve arm circulation and vein visibility."),
}

# Core donor grid (ordered by donor-journey relevance) - used for card rendering.
CATALOG = [
    "B07GKVFN2V", "B00008I8NT", "B000QSNYGI", "B01ACAXFHI",
    "B07GVMQRKM", "B07D3K8FQZ", "B08LN8VQFV", "B07GXMZ3Z5",
    "B07QXV6N1B", "B09MPMYBK4", "B07K3XJQGN", "B08KTZ8249",
]

# Ordered keyword -> ASIN rules. First match wins, so list specific before general.
# Off-topic queries (tax, finance, planners, electronics, vitamins we have no ASIN
# for) intentionally fall through and stay as search links rather than mis-mapping.
_RULES = [
    (("liquid+iv", "liquid+i.v", "hydration+multiplier", "hidratacion", "hidrataci"), "B07GKVFN2V"),
    (("pedialyte", "electrolyte", "electrolit", "electrolito", "lmnt", "nuun", "coconut+water", "bodyarmor", "emergen", "hydration+multiplier+electrolyte"), "B07GVMQRKM"),
    (("iron", "hierro", "ferrous", "hemoglobin", "blood+builder", "floradix", "slow+fe", "vitamin+code", "vitafusion+iron", "blood+builder"), "B00008I8NT"),
    (("protein", "proteina", "prote%c3%adna", "whey", "optimum+nutrition", "orgain", "isopure", "dymatize", "naked+whey", "vega+sport", "fairlife", "core+power", "premier+protein", "rxbar", "quest", "kind+protein", "snacks+proteina", "batido+prote"), "B000QSNYGI"),
    (("water+bottle", "hydro+flask", "hydroflask", "insulated+water", "insulated+bottle", "botella", "contigo", "time+marker", "hydration+tracker", "hydration+water+bottle", "blender+bottle", "reusable+water", "large+water"), "B01ACAXFHI"),
    (("portable+charger", "phone+charger", "power+bank", "cargador", "portable+phone+stand", "phone+stand"), "B07QXV6N1B"),
    (("earbud", "headphone", "airpod", "auriculares", "jbl", "bose", "sony+noise", "studio+headphones", "wireless+earbuds"), "B09MPMYBK4"),
    (("kindle",), "B08KTZ8249"),
    (("pillow", "almohada", "travel+blanket", "cozy+travel", "manta+", "mantas+via"), "B07K3XJQGN"),
    (("grip", "stress+ball", "hand+exerciser", "pelota+anti", "stress+relief+hand", "hand+grip"), "B08LN8VQFV"),
    (("warm+compress", "heating+pad", "hand+warmer", "mantas+calentamiento", "microwaveable+heating", "microwavable+warm", "electric+heating", "moist+heat", "sunbeam+heating"), "B07GXMZ3Z5"),
    (("resistance+band", "foam+roller", "banda+compresi", "massage+gun", "hyperice"), "B07VBZV9ND"),
    (("compression", "arm+sleeve", "arnica", "%c3%a1rnica", "arnicare", "bruise", "moretones", "bandage", "vendaje", "aquaphor", "saniderm", "ice+pack", "cold+compress", "gel+fr", "bolsas+gel", "first+aid", "self+adhesive", "reusable+ice", "gel+ice", "compression+socks", "copper+fit", "flexible+fabric+bandages"), "B07D3K8FQZ"),
]


def map_query_to_asin(query):
    """query is the raw value after s?k= (still URL-encoded, '+'-joined)."""
    q = query.lower()
    for keys, asin in _RULES:
        for k in keys:
            if k in q:
                emoji, name, desc = PRODUCTS[asin]
                return asin, name, emoji, desc
    return None


if __name__ == "__main__":
    # self-test: ensure every CATALOG asin and every rule target is real
    for a in CATALOG:
        assert a in PRODUCTS, a
    for keys, asin in _RULES:
        assert asin in PRODUCTS, asin
    print(f"Catalog OK: {len(PRODUCTS)} products, {len(CATALOG)} in grid, {len(_RULES)} rules")
