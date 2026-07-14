import requests
import time
import json

ENDPOINT = "http://host.docker.internal:8080/feedback/analyze"
QID_STANDAR_KUALITAS = "a22b2712-2135-4eb0-ad5e-b5fdc2753283"

def compute_template_key(valid, d1, d2, d3, d4):
    return "invalid" if not valid else f"{d1}{d2}{d3}{d4}"

# Kita akan buat puluhan variasi untuk mencoba mendapatkan 0010
# Syarat 0010:
# - d1=0: Cakupan terpenuhi (mengandung keyword rubrik Standar Kualitas)
# - d2=0: Koheren (skor sesuai sentimen, kita pakai 5 untuk positif, atau 1 untuk negatif jika eksplisit, tapi lebih gampang skor 5 dengan pujian eksplisit)
# - d3=1: Pendek (< 25 kata)
# - d4=0: Mutual exclusivity AMAN (tidak overlap dengan rubrik lain)

# Kita hindari kata-kata yang bisa memicu rubrik lain seperti:
# "komunikasi", "tepat waktu", "produktif", "manajemen", "tim", "diskusi"

narasumber = [
    # Sangat pendek (2-5 kata)
    "Kualitas pekerjaan sempurna.",
    "Komitmen kerja tinggi.",
    "Standar kualitas dijaga.",
    "Hasil akhir sangat bagus.",
    "Kualitas sangat tinggi.",
    "Evaluasi selalu dilakukan.",
    "Sangat menjaga kualitas.",
    "Komitmen sangat kuat.",
    "Kualitas hasil baik.",
    "Perbaikan kualitas rutin.",
    
    # Pendek sedang (6-10 kata)
    "Komitmen kerjanya terhadap standar kualitas sangat tinggi.",
    "Hasil akhir pekerjaannya selalu dievaluasi dan kualitasnya luar biasa.",
    "Dia sangat menjaga standar kualitas dalam setiap pekerjaannya.",
    "Evaluasi dan perbaikan kualitas pekerjaan rutin dilakukan.",
    "Kualitas hasil akhir dari pekerjaannya sangat memuaskan.",
    "Selalu memastikan kualitas pekerjaan mencapai standar tertinggi.",
    "Standar mutu dijaga ketat dalam setiap evaluasi akhir.",
    "Komitmen yang kuat untuk menghasilkan kualitas yang sempurna.",
    "Hasil kerjanya bagus karena selalu berpedoman pada standar.",
    "Evaluasi pekerjaan dilakukan demi menjaga kualitas hasil akhir.",

    # Agak panjang tapi < 25 kata (11-20 kata)
    "Komitmen terhadap standar kualitas sangat baik. Kualitas hasil akhir memuaskan. Evaluasi dan perbaikan pekerjaan senantiasa dilakukan.",
    "Pekerjaannya selalu dievaluasi. Kualitas hasil akhir sangat tinggi karena komitmen kerjanya tidak pernah menurun sepanjang proyek.",
    "Selalu menjaga standar kualitas. Evaluasi akhir membuktikan bahwa komitmen kerjanya menghasilkan perbaikan mutu yang sangat memuaskan.",
    "Tidak pernah mengabaikan standar kualitas. Evaluasi rutin dan perbaikan kualitas pekerjaan menjadi komitmen utamanya setiap saat.",
    "Hasil akhirnya selalu bagus. Dia menunjukkan komitmen tinggi dalam menjaga standar kualitas dan rutin melakukan evaluasi.",
    
    # Variasi dengan sinonim atau kata spesifik untuk menghindari overlap rubrik lain
    "Mutu pekerjaannya tiada duanya. Dia sungguh berdedikasi tinggi terhadap mutu dan terus mengevaluasi kekurangannya.",
    "Standar mutu sangat prima. Dedikasi terhadap hasil akhir sangat baik. Selalu ada evaluasi mutu.",
    "Hasil kinerjanya sangat bermutu tinggi. Dia punya komitmen kuat pada standar pekerjaannya.",
    "Pengecekan mutu selalu dilakukan. Hasil pekerjaannya sungguh luar biasa berkualitas tinggi dan bagus.",
    "Selalu melakukan perbaikan mutu. Komitmennya pada standar mutu sangat mengagumkan.",
    
    # Narasi sangat spesifik mengambil persis keyword tanpa tambahan kata lain
    "Komitmen kerja. Standar kualitas. Kualitas hasil akhir. Evaluasi. Perbaikan.",
    "Komitmen kerja tinggi. Standar kualitas tinggi. Kualitas hasil akhir tinggi. Evaluasi sering. Perbaikan sering.",
    "Menjaga komitmen kerja. Menjaga standar kualitas. Menjaga kualitas hasil akhir. Melakukan evaluasi. Melakukan perbaikan.",
    "Komitmen, standar, kualitas, hasil akhir, evaluasi, perbaikan.",
    
    # Narasi hanya mengulang-ulang keyword agar similarity ke rubrik target dominan
    "Kualitas kualitas kualitas kualitas kualitas standar standar standar standar standar komitmen komitmen komitmen",
    "Evaluasi kualitas hasil akhir evaluasi perbaikan kualitas standar komitmen kerja",
    "Kualitas hasil akhir sangat berkualitas. Standar kualitas di atas standar. Komitmen kualitas tinggi.",
    
    # Narasi dengan skor rendah (negatif) < 25 kata (siapa tahu lebih mudah)
    # Harus sangat spesifik eksplisit agar d1=0
    "Komitmen kerjanya sangat buruk. Standar kualitas diabaikan. Kualitas hasil akhir hancur. Evaluasi pekerjaan tidak ada.",
    "Sama sekali tidak menjaga standar kualitas. Komitmennya nol. Kualitas hasil akhir sangat mengecewakan. Tanpa evaluasi.",
    "Kualitas pekerjaan sangat jelek. Standar kualitas sama sekali tidak dipatuhi. Tidak punya komitmen.",
    "Sangat buruk komitmennya terhadap standar kualitas. Hasil akhirnya sangat jelek dan tidak ada evaluasi.",
]

print("="*60)
print(f"BRUTEFORCE TEMPLATE 0010 - {len(narasumber)} Skenario")
print("="*60)

berhasil = 0
hasil_list = []

for i, narasi in enumerate(narasumber):
    skor = 1 if "buruk" in narasi.lower() or "nol" in narasi.lower() or "jelek" in narasi.lower() or "hancur" in narasi.lower() else 5
    
    payload = {
        "NIM": f"BF_0010_{i:02d}",
        "type": "assessment",
        "question_id": QID_STANDAR_KUALITAS,
        "feedback": {"skor": skor, "narasi": narasi}
    }
    
    try:
        resp = requests.post(ENDPOINT, json=payload, timeout=10)
        if resp.status_code == 200:
            ind = resp.json().get("indicators", {})
            act_key = compute_template_key(
                ind.get("valid", True),
                ind.get("d1", 0),
                ind.get("d2", 0),
                ind.get("d3", 0),
                ind.get("d4", 0)
            )
            
            d1, d2, d3, d4 = ind.get("d1"), ind.get("d2"), ind.get("d3"), ind.get("d4")
            if act_key == "0010":
                berhasil += 1
                status = "✅ BINGO!"
            else:
                status = f"❌ {act_key}"
                
            print(f"[{i+1:02d}] {status} | len={len(narasi.split())} | d1={d1} d2={d2} d3={d3} d4={d4} | {narasi[:50]}...")
            
            hasil_list.append({
                "narasi": narasi,
                "skor": skor,
                "key": act_key,
                "d1": d1, "d2": d2, "d3": d3, "d4": d4
            })
            
        else:
            print(f"[{i+1:02d}] ERROR {resp.status_code}")
    except Exception as e:
        print(f"[{i+1:02d}] EXCEPTION {str(e)[:30]}")

print("="*60)
print(f"TOTAL BINGO 0010: {berhasil} dari {len(narasumber)} percobaan.")

# Simpan yang berhasil atau rekap jika ada
with open("/workspace/Testing/bruteforce_0010_log.json", "w") as f:
    json.dump(hasil_list, f, indent=2)

