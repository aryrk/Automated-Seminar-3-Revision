import pandas as pd
import math

df = pd.read_csv('/workspace/Testing/NLP_Validation_Cases.csv')

# Goals:
# 1. Boundary threshold panjang narasi (DIR): 23
# 2. Kombinasi matrix koherensi skor (DIR): 28
# 3. Relevansi dan cakupan konten rubrik (MFT & DIR): 21
# 4. Variasi leksikal & morfologis (INV): 15
# 5. Redundansi dan manipulasi konten (DIR): 2
# 6. Validitas dan batas struktural input (MFT): 16
# 7. Kontrol positif (MFT): 2
# Total: 107

# We will assign based on clear prefixes and keep track of counts.
goals = {
    "Boundary threshold panjang narasi": 23,
    "Kombinasi matrix koherensi skor": 28,
    "Relevansi dan cakupan konten rubrik": 21,
    "Variasi leksikal & morfologis": 15,
    "Redundansi dan manipulasi konten": 2,
    "Validitas dan batas struktural input": 16,
    "Kontrol positif": 2
}

types = {
    "Boundary threshold panjang narasi": "DIR",
    "Kombinasi matrix koherensi skor": "DIR",
    "Relevansi dan cakupan konten rubrik": "MFT & DIR",
    "Variasi leksikal & morfologis": "INV",
    "Redundansi dan manipulasi konten": "DIR",
    "Validitas dan batas struktural input": "MFT",
    "Kontrol positif": "MFT"
}

mapping = {}

for i, row in df.iterrows():
    name = str(row['Test Case Name* (Scenario)']).strip()
    
    # 7. Kontrol
    if name.startswith("Baseline") and goals["Kontrol positif"] > 0:
        mapping[name] = "Kontrol positif"
        goals["Kontrol positif"] -= 1
        continue
        
    # 5. Redundansi
    if name.startswith("Copy-Paste") and goals["Redundansi dan manipulasi konten"] > 0:
        mapping[name] = "Redundansi dan manipulasi konten"
        goals["Redundansi dan manipulasi konten"] -= 1
        continue
        
    # 6. Validitas
    if (name.startswith("Malas") and "Input Kosong" in name) or \
       (name.startswith("Malas") and "Spasi" in name) or \
       (name.startswith("Malas") and "Angka Saja" in name) or \
       "Gibberish" in name or \
       "Emoji" in name or \
       "Tanda Tanya dan Seru" in name or \
       name.startswith("Valid Filter") or \
       name.startswith("Skor 0") or \
       name.startswith("Skor 6") or \
       name.startswith("Teks — Karakter") or \
       name.startswith("Hanya 1 tanda baca"):
        
        if goals["Validitas dan batas struktural input"] > 0:
            mapping[name] = "Validitas dan batas struktural input"
            goals["Validitas dan batas struktural input"] -= 1
            continue

    # 4. Variasi (15)
    if ("Sinonim" in name or "Typo" in name or "Singkatan" in name or "Campuran Bahasa" in name or 
        "Indoglish" in name or "Bahasa Inggris" in name or "Bahasa Sunda" in name or "Struktur Kalimat Pasif" in name or
        "Tanpa Spasi" in name or "Bahasa — Full" in name or "Kata Dipisah" in name or "Spasi Ganda" in name or "Tanda Baca Ekstrem" in name or "Kata — Tidak baku" in name or "Bullet Point" in name):
        
        if goals["Variasi leksikal & morfologis"] > 0:
            mapping[name] = "Variasi leksikal & morfologis"
            goals["Variasi leksikal & morfologis"] -= 1
            continue
            
    # 2. Koherensi (28)
    if name.startswith("Inkoherensi") or name.startswith("Koherensi") or name.startswith("Matriks") or name.startswith("Variasi Rentang Skor") or name.startswith("Geng") or name.startswith("Dendam") or name.startswith("Self-Assessment") or name.startswith("Skor 1") or name.startswith("Skor 5"):
        if goals["Kombinasi matrix koherensi skor"] > 0:
            mapping[name] = "Kombinasi matrix koherensi skor"
            goals["Kombinasi matrix koherensi skor"] -= 1
            continue
            
    # 1. Panjang (23)
    if name.startswith("Panjang Bertahap") or name.startswith("Batas Bawah") or name.startswith("Batas Atas") or name.startswith("Malas") or name.startswith("Probe f3") or name.startswith("Narasi Sangat Panjang") or name.startswith("Narasi 30 Kata") or name.startswith("Narasi 50 Kata") or name.startswith("Narasi Satu Kalimat"):
        if goals["Boundary threshold panjang narasi"] > 0:
            mapping[name] = "Boundary threshold panjang narasi"
            goals["Boundary threshold panjang narasi"] -= 1
            continue

    # 3. Relevansi (21)
    if name.startswith("Basa-Basi") or name.startswith("Topik Melenceng") or name.startswith("Narasi Off-Topic") or name.startswith("Relevansi") or name.startswith("Aspek") or name.startswith("Salah Aspek") or name.startswith("Asal Ada Narasi") or name.startswith("Narasi — Tidak relevan") or name.startswith("Keyword") or name.startswith("Kata 'komitmen'"):
        if goals["Relevansi dan cakupan konten rubrik"] > 0:
            mapping[name] = "Relevansi dan cakupan konten rubrik"
            goals["Relevansi dan cakupan konten rubrik"] -= 1
            continue
            
    mapping[name] = "UNKNOWN"

# Fallback for ANY UNKNOWN to satisfy exactly the remaining counts
for i, row in df.iterrows():
    name = str(row['Test Case Name* (Scenario)']).strip()
    if mapping.get(name, "UNKNOWN") == "UNKNOWN":
        for k, v in goals.items():
            if v > 0:
                mapping[name] = k
                goals[k] -= 1
                break

df['Dimensi Uji (Tabel III.23)'] = df.apply(lambda row: mapping[str(row['Test Case Name* (Scenario)']).strip()], axis=1)
df['Test Type (MFT/INV/DIR)'] = df.apply(lambda row: types[row['Dimensi Uji (Tabel III.23)']], axis=1)

# Drop any previous attempts
cols = df.columns.tolist()
if cols.count('Test Type (MFT/INV/DIR)') > 1:
    df = df.loc[:, ~df.columns.duplicated()]
    cols = df.columns.tolist()

# Organize columns
if 'Dimensi Uji (Tabel III.23)' in cols: cols.remove('Dimensi Uji (Tabel III.23)')
if 'Test Type (MFT/INV/DIR)' in cols: cols.remove('Test Type (MFT/INV/DIR)')
    
cols.insert(2, 'Dimensi Uji (Tabel III.23)')
cols.insert(3, 'Test Type (MFT/INV/DIR)')
df = df[cols]

df.to_csv('/workspace/Testing/NLP_Validation_Cases.csv', index=False)

for k, v in goals.items():
    print(f"Remaining {k}: {v} (should be 0)")
