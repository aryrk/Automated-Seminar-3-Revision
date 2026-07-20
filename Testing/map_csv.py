import pandas as pd

df = pd.read_csv('/workspace/Testing/NLP_Validation_Cases.csv')

def categorize(row):
    name = str(row['Test Case Name* (Scenario)']).lower()
    
    # 7. Kontrol positif (2 cases) -> MFT
    if "baseline" in name:
        return "MFT"
        
    # 5. Redundansi dan manipulasi konten (2 cases) -> DIR
    if "copy-paste" in name or "redundansi" in name or "diulang" in name:
        return "DIR"
        
    # 4. Variasi leksikal & morfologis (15 cases) -> INV
    if "sinonim" in name or "typo" in name or "singkatan" in name or "indoglish" in name or "campuran bahasa" in name or "tanda baca" in name or "pasif" in name or "tanpa spasi" in name or "eksak keyword" in name or ("variasi" in name and "skor" not in name) or "bahasa —" in name or "bahasa inggris" in name or "bahasa sunda" in name or "bullet point" in name:
        return "INV"
        
    # 6. Validitas dan batas struktural input (16 cases) -> MFT
    if "kosong" in name or "spasi" in name or "angka saja" in name or "emoji" in name or ("teks" in name and "acak" in name) or "valid filter" in name or ("hanya" in name and ("tanda" in name or "simbol" in name or "emoji" in name or "titik" in name)) or "skor 0" in name or "skor 6" in name or "batas struktural" in name or "gibberish" in name:
        return "MFT"
        
    # 1. Boundary threshold panjang narasi (23 cases) -> DIR
    if "panjang bertahap" in name or "batas bawah" in name or "batas atas" in name or "probe f3" in name or "malas" in name or "kata persis" in name or "narasi sangat panjang" in name or "narasi 50 kata" in name or "narasi satu kalimat" in name:
        return "DIR"
        
    # 2. Kombinasi matrix koherensi skor (28 cases) -> DIR
    if "inkoherensi" in name or "koherensi" in name or "matriks" in name or "variasi rentang skor" in name or ("skor" in name and "0" not in name and "6" not in name) or "geng" in name or "dendam" in name or "self-assessment" in name or "bias" in name:
        return "DIR"
        
    # 3. Relevansi dan cakupan konten rubrik (21 cases) -> MFT & DIR
    if "basa-basi" in name or "topik melenceng" in name or "relevansi" in name or "aspek" in name or "off-topic" in name or "keyword stuffing" in name or "keyword strategis" in name or "asal ada narasi" in name or "kriteria" in name or "kata 'komitmen'" in name:
        if "basa-basi" in name or "topik melenceng" in name or "asal ada narasi" in name or "off-topic" in name or "aspek" in name:
            return "MFT"
        else:
            return "DIR"
        
    return "UNKNOWN"

df['Test Type (MFT/INV/DIR)'] = df.apply(categorize, axis=1)

print(df['Test Type (MFT/INV/DIR)'].value_counts())
print("\nUnknowns:")
print(df[df['Test Type (MFT/INV/DIR)'] == 'UNKNOWN']['Test Case Name* (Scenario)'])

# Make sure we don't have duplicated 'Test Type (MFT/INV/DIR)' columns
if 'Test Type (MFT/INV/DIR)' in df.columns:
    # Get all column names
    cols = df.columns.tolist()
    # Check if there are multiple columns with the same name
    if cols.count('Test Type (MFT/INV/DIR)') > 1:
        # Keep only the first one
        df = df.loc[:, ~df.columns.duplicated()]
        cols = df.columns.tolist()
    
    # Move to index 2 (after Module and Case)
    idx = cols.index('Test Type (MFT/INV/DIR)')
    cols.insert(2, cols.pop(idx))
    df = df[cols]

df.to_csv('/workspace/Testing/NLP_Validation_Cases.csv', index=False)
print("Updated original CSV in-place.")
