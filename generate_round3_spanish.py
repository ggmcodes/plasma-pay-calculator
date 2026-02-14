#!/usr/bin/env python3
"""Generate Round 3 Spanish blog pages: 53 NEW pages total
Runs all 3 sub-scripts: medical (15), cities (15), process/center (23)
"""
import subprocess, sys, os

BASE = os.path.dirname(os.path.abspath(__file__))
scripts = [
    'generate_round3_spanish_medical.py',
    'generate_round3_spanish_cities.py',
    'generate_round3_spanish_process.py',
]

total = 0
for s in scripts:
    path = os.path.join(BASE, s)
    print(f"\n{'='*60}")
    print(f"Running: {s}")
    print('='*60)
    result = subprocess.run([sys.executable, path], capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(f"STDERR: {result.stderr}")
    if result.returncode != 0:
        print(f"ERROR: {s} failed with code {result.returncode}")
        sys.exit(1)

# Verify
ES_BLOG_DIR = os.path.join(BASE, 'es', 'blog')
new_slugs = [
    # Medical (15)
    'donar-plasma-con-lupus-2026', 'donar-plasma-con-artritis-2026',
    'donar-plasma-con-fibromialgia-2026', 'donar-plasma-con-epilepsia-2026',
    'donar-plasma-con-esclerosis-multiple-2026', 'donar-plasma-con-psoriasis-2026',
    'donar-plasma-con-apnea-sueno-2026', 'donar-plasma-con-enfermedad-renal-2026',
    'donar-plasma-con-herpes-2026', 'donar-plasma-despues-covid-2026',
    'donar-plasma-con-enfermedad-corazon-2026', 'donar-plasma-con-enfermedad-autoinmune-2026',
    'donar-plasma-con-colesterol-alto-2026', 'donar-plasma-con-eczema-2026',
    'donar-plasma-con-migranas-2026',
    # Cities (15)
    'cuanto-pagan-donar-plasma-san-francisco-2026', 'cuanto-pagan-donar-plasma-seattle-2026',
    'cuanto-pagan-donar-plasma-portland-2026', 'cuanto-pagan-donar-plasma-tampa-2026',
    'cuanto-pagan-donar-plasma-detroit-2026', 'cuanto-pagan-donar-plasma-memphis-2026',
    'cuanto-pagan-donar-plasma-indianapolis-2026', 'cuanto-pagan-donar-plasma-nashville-2026',
    'cuanto-pagan-donar-plasma-albuquerque-2026', 'cuanto-pagan-donar-plasma-raleigh-2026',
    'cuanto-pagan-donar-plasma-charlotte-2026', 'cuanto-pagan-donar-plasma-jacksonville-2026',
    'cuanto-pagan-donar-plasma-columbus-2026', 'cuanto-pagan-donar-plasma-milwaukee-2026',
    'cuanto-pagan-donar-plasma-kansas-city-2026',
    # Process/Financial (13)
    'como-donar-plasma-mas-rapido-2026', 'donar-plasma-y-medicaid-beneficios-2026',
    'donar-plasma-y-desempleo-2026', 'donar-plasma-para-trabajadores-gig-2026',
    'donar-plasma-para-veteranos-militares-2026', 'suplementos-para-donantes-plasma-2026',
    'hidratacion-donar-plasma-guia-2026', 'proteina-para-donar-plasma-2026',
    'hierro-hematocrito-donar-plasma-2026', 'reaccion-citrato-donar-plasma-2026',
    'diferimiento-donar-plasma-razones-2026', 'tarjeta-prepagada-plasma-guia-2026',
    'donar-plasma-impuestos-formulario-1099-2026',
    # Center/Comparison (10)
    'immunotek-cuanto-pagan-tarifas-2026', 'b-positive-plasma-cuanto-pagan-2026',
    'adma-biocenters-cuanto-pagan-2026', 'comparacion-todos-centros-plasma-2026',
    'mejor-centro-donantes-nuevos-2026', 'donar-plasma-varias-veces-semana-seguro-2026',
    'pros-contras-donar-plasma-2026', 'como-funciona-donacion-plasma-proceso-2026',
    'riesgos-beneficios-donar-plasma-2026', 'ganar-dinero-donando-plasma-1000-mes-2026',
]

print(f"\n{'='*60}")
print("VERIFICATION")
print('='*60)
missing = []
found = 0
for slug in new_slugs:
    path = os.path.join(ES_BLOG_DIR, f"{slug}.html")
    if os.path.exists(path):
        size = os.path.getsize(path)
        if size > 1000:
            found += 1
        else:
            missing.append(f"{slug} (too small: {size} bytes)")
    else:
        missing.append(f"{slug} (missing)")

print(f"Found: {found}/{len(new_slugs)} pages")
if missing:
    print(f"Missing/issues: {len(missing)}")
    for m in missing:
        print(f"  - {m}")
else:
    print("All 53 pages verified successfully!")
