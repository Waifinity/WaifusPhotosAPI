import os
import json
import random

# CONFIGURAÇÕES
GITHUB_USER = "Waifinity"
REPO_NAME = "WaifusPhotosAPI"
IMAGES_DIR = "images"
JSON_FILE = "waifus.json"

RARIDADES_POSSIVEIS = ["N", "R", "SR", "SSR"]

# Tenta carregar o JSON antigo para manter raridades
if os.path.exists(JSON_FILE):
    with open(JSON_FILE, "r", encoding="utf-8") as f:
        waifus_data = json.load(f)
else:
    waifus_data = {}

# Caminho base do CDN
CDN_BASE = f"https://cdn.jsdelivr.net/gh/{GITHUB_USER}/{REPO_NAME}/images"

# Varre todas as categorias
for categoria in os.listdir(IMAGES_DIR):
    categoria_path = os.path.join(IMAGES_DIR, categoria)
    if not os.path.isdir(categoria_path):
        continue

    if categoria not in waifus_data:
        waifus_data[categoria] = []

    imagens_existentes = {img["nome"] for img in waifus_data[categoria]}

    for filename in os.listdir(categoria_path):
        if not filename.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
            continue

        if filename in imagens_existentes:
            continue  # Já está no JSON, não sobrescreve

        url = f"{CDN_BASE}/{categoria}/{filename}"
        nova_waifu = {
            "nome": filename,
            "url": url,
            "raridade": random.choice(RARIDADES_POSSIVEIS)
        }
        waifus_data[categoria].append(nova_waifu)
        print(f"Adicionada: {filename} na categoria {categoria} com raridade {nova_waifu['raridade']}")

# Salva o JSON atualizado
with open(JSON_FILE, "w", encoding="utf-8") as f:
    json.dump(waifus_data, f, indent=2, ensure_ascii=False)

print("✅ waifus.json atualizado com sucesso.")
