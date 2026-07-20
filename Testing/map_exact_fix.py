import pandas as pd

df = pd.read_csv('/workspace/Testing/NLP_Validation_Cases.csv')

def get_actual_counts():
    c = df['Dimensi Uji (Tabel III.23)'].value_counts().to_dict()
    print("Actual vs Expected:")
    print(f"Kontrol positif: {c.get('Kontrol positif',0)} (Expected: 2)")
    print(f"Redundansi: {c.get('Redundansi dan manipulasi konten',0)} (Expected: 2)")
    print(f"Validitas: {c.get('Validitas dan batas struktural input',0)} (Expected: 16)")
    print(f"Variasi: {c.get('Variasi leksikal & morfologis',0)} (Expected: 15)")
    print(f"Panjang: {c.get('Boundary threshold panjang narasi',0)} (Expected: 23)")
    print(f"Koherensi: {c.get('Kombinasi matrix koherensi skor',0)} (Expected: 28)")
    print(f"Relevansi: {c.get('Relevansi dan cakupan konten rubrik',0)} (Expected: 21)")
    
get_actual_counts()

# To perfectly match, I will adjust mapping.
# We have 31 Panjang (need 23, so -8)
# We have 26 Koherensi (need 28, so +2)
# We have 15 Relevansi (need 21, so +6)
# Note: 8 from Panjang should move to Koherensi (2) and Relevansi (6).

# In Relevansi, maybe some "Probe f3" or "Malas" were actually testing Relevansi?
# Let's inspect the names of Panjang and Koherensi.
