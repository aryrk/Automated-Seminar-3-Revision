import pandas as pd
import sys

df = pd.read_csv('/workspace/Testing/NLP_Validation_Cases.csv')
names = df['Test Case Name* (Scenario)'].str.strip().tolist()

mapping = {}
for n in names:
    mapping[n] = "UNKNOWN"

# 1. Kontrol Positif (2)
mapping["Baseline — Ideal (semua indikator terpenuhi)"] = "Kontrol positif"
mapping["Baseline — Ideal Panjang"] = "Kontrol positif"

# 2. Redundansi (2)
mapping["Copy-Paste — Satu kalimat diulang 5x"] = "Redundansi dan manipulasi konten"
mapping["Copy-Paste — Kata 'baik' diulang 30x"] = "Redundansi dan manipulasi konten"

# 3. Validitas (16)
validitas = [
    "Malas — Input Kosong", "Malas — Hanya Spasi Panjang", "Malas — Mengisi Angka Saja",
    "Teks Gibberish Murni", "Hanya Tanda Tanya dan Seru", "Emoji Saja",
    "Valid Filter — Satu kata bermakna", "Valid Filter — Dua kata bermakna",
    "Valid Filter — Kalimat minimal S+P", "Valid Filter — 50% bermakna 50% gibberish",
    "Valid Filter — Teks dengan URL", "Valid Filter — Kata nonsense dicampur kata valid",
    "Valid Filter — Bahasa Inggris formal pendek", "Valid Filter — Bahasa Melayu (dekat dengan Indonesia)",
    "Skor 0 — di bawah rentang 1-5 (masih valid per backend)", "Skor 6 — di atas rentang 1-5"
]
for x in validitas: mapping[x] = "Validitas dan batas struktural input"

# 4. Variasi (15)
variasi = [
    "Substitusi Sinonim (Sama makna, beda kata)", "Singkatan — \"Tdk\", \"bgs\", \"yg\"",
    "Typo — Salah ketik wajar (\"kualtas\", \"bagsu\")", "Campuran Bahasa (Inggris - Indonesia)",
    "Bahasa Inggris Murni", "Bahasa Sunda", "Struktur Kalimat Pasif — \"Pekerjaan diselesaikan dengan baik olehnya\"",
    "Tanpa Spasi (Kesalahan input) — \"Sangatbaikdanjujursekali\"", "Narasi Pakai Bullet Point / Numbering",
    "Indoglish — Campuran Bahasa Indonesia-Inggris", "Bahasa — Full Inggris Ideal", "Bahasa — Full Inggris Negatif",
    "Kata Dipisah Tanda Baca (tanpa spasi)", "Spasi Ganda Antar Kata", "Tanda Baca Ekstrem — \"!!!???\""
]
# Wait, "Tanda Baca Ekstrem — \"!!!???\"" or "Kata — Tidak baku..." ?
# Wait, let's look at the list. "Tanda Baca Ekstrem — \"!!!???\"" is in the list.
# Are there 15?
for x in variasi: 
    if x in mapping: mapping[x] = "Variasi leksikal & morfologis"

# 5. Panjang (23)
panjang = [
    "Malas — Hanya 1 kata", "Malas — 5 kata", "Malas — 15 kata", "Malas — 20 kata",
    "Malas — Tepat 24 Kata (Edge Case Bawah f3)", "Malas — Tepat 25 Kata (Edge Case Atas f3)",
    "Narasi Sangat Panjang (100+ kata) — Komprehensif", "Narasi 30 Kata Persis — Cukup tapi Minimal",
    "Narasi 50 Kata dengan Transisi Alami", "Narasi Satu Kalimat Sangat Panjang",
    "Probe f3 — 12 kata (Python split)", "Probe f3 — 16 kata (Python split)",
    "Probe f3 — 18 kata (Python split)", "Probe f3 — 20 kata (Python split)",
    "Probe f3 — 22 kata (Python split)", "Probe f3 — 24 kata TEPAT (harus d3=1)",
    "Probe f3 — 25 kata TEPAT (harus d3=0)", "Probe f3 — 26 kata (harus d3=0)",
    "Probe f3 — 25 kata dengan tanda baca (split() tidak peduli koma)",
    "Probe f3 — Kata Majemuk dengan tanda hubung ('kerja-keras')",
    "Probe f3 — Teks dengan singkatan (dll., dsb.)",
    "Panjang Bertahap (7 kata)", "Panjang Bertahap (12 kata)", "Panjang Bertahap (18 kata)",
    "Panjang Bertahap (22 kata)", "Panjang Bertahap (26 kata)", "Panjang Bertahap (35 kata)",
    "Panjang Bertahap (50 kata)", "Panjang Bertahap (75 kata)", "Panjang Bertahap (100 kata)",
    "Panjang Bertahap (150 kata)", "Batas Bawah 1", "Batas Bawah 2", "Batas Bawah 3", "Batas Bawah 4", "Batas Bawah 5",
    "Batas Atas 1", "Batas Atas 2", "Batas Atas 3", "Batas Atas 4", "Batas Atas 5"
]
# Wait, if I take all of them, there are too many. The list output by list_cases.py had 107 items.
# Let's count them by iterating all UNKNOWN and assigning carefully.

for name in names:
    if mapping[name] != "UNKNOWN": continue
    if name.startswith("Probe f3") or name.startswith("Malas") or name.startswith("Panjang Bertahap") or name.startswith("Batas Bawah") or name.startswith("Batas Atas") or name.startswith("Narasi Sangat Panjang") or name.startswith("Narasi 30 Kata") or name.startswith("Narasi 50 Kata") or name.startswith("Narasi Satu Kalimat"):
        mapping[name] = "Boundary threshold panjang narasi"

# 6. Koherensi (28)
for name in names:
    if mapping[name] != "UNKNOWN": continue
    if name.startswith("Matriks") or name.startswith("Inkoherensi") or name.startswith("Koherensi") or name.startswith("Variasi Rentang Skor") or name.startswith("Skor 1") or name.startswith("Skor 5") or name.startswith("Geng") or name.startswith("Dendam") or name.startswith("Self-Assessment"):
        mapping[name] = "Kombinasi matrix koherensi skor"

# 7. Relevansi (21)
for name in names:
    if mapping[name] != "UNKNOWN": continue
    mapping[name] = "Relevansi dan cakupan konten rubrik"

# Validate counts
counts = {"Kontrol positif":0, "Redundansi dan manipulasi konten":0, "Validitas dan batas struktural input":0,
          "Variasi leksikal & morfologis":0, "Boundary threshold panjang narasi":0,
          "Kombinasi matrix koherensi skor":0, "Relevansi dan cakupan konten rubrik":0}
for k,v in mapping.items():
    counts[v] += 1

print("Counts:")
for k,v in counts.items():
    print(f"{k}: {v}")
    
# Apply to df
def get_dimensi(row):
    return mapping[str(row['Test Case Name* (Scenario)']).strip()]

def get_type(dimensi):
    if dimensi == "Boundary threshold panjang narasi": return "DIR"
    if dimensi == "Kombinasi matrix koherensi skor": return "DIR"
    if dimensi == "Redundansi dan manipulasi konten": return "DIR"
    if dimensi == "Relevansi dan cakupan konten rubrik": return "MFT & DIR"
    if dimensi == "Variasi leksikal & morfologis": return "INV"
    if dimensi == "Validitas dan batas struktural input": return "MFT"
    if dimensi == "Kontrol positif": return "MFT"
    return "UNKNOWN"

df['Dimensi Uji (Tabel III.23)'] = df.apply(get_dimensi, axis=1)
df['Test Type (MFT/INV/DIR)'] = df.apply(lambda row: get_type(row['Dimensi Uji (Tabel III.23)']), axis=1)

cols = df.columns.tolist()
if 'Dimensi Uji (Tabel III.23)' in cols: cols.remove('Dimensi Uji (Tabel III.23)')
if 'Test Type (MFT/INV/DIR)' in cols: cols.remove('Test Type (MFT/INV/DIR)')
cols.insert(2, 'Dimensi Uji (Tabel III.23)')
cols.insert(3, 'Test Type (MFT/INV/DIR)')
df = df[cols]

df.to_csv('/workspace/Testing/NLP_Validation_Cases.csv', index=False)
print("Updated successfully.")
