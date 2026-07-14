"""
run_template_coverage_tests.py  — ROUND 2
═══════════════════════════════════════════════════════════════════════
PELAJARAN DARI ROUND 1:
  1. d4=1 HANYA terpicu via "mutual exclusivity":
     narasi menggunakan keyword rubrik TAPI dalam konteks aspek yang BERBEDA
     (mis: narasi berisi keyword "standar kualitas" tapi pertanyaan meminta "produktivitas",
     atau narasi tentang pasar dengan keyword rubrik tertanam).
     → Narasi completely off-topic (resep, berita, dinosaurus) TIDAK memicu d4=1.

  2. d1=1 hampir SELALU co-trigger dengan d2=1:
     narasi yang inkoherensi (skor tidak sesuai narasi) cenderung tidak cover rubrik criteria.
     → Template "0100" (hanya d2=1) SANGAT SULIT karena memerlukan:
        narasi menyebut SEMUA keyword rubrik (d1=0) TAPI skor tidak sesuai narasi (d2=1).

  3. d4 cross-aspect strategy (paling reliabel untuk d4=1):
     Gunakan narasi yang membahas ASPEK RUBRIK YANG BERBEDA dari QID yang ditanya.
     Misal: Narasi produktivitas pada QID standar kualitas → sistem deteksi non-target lebih tinggi.

  4. Template yang BERHASIL di Round 1:
     invalid, 0000, 0001, 0101, 0111, 1000, 1010, 1100, 1101, 1110

  5. Template yang BELUM berhasil:
     0010, 0011, 0100, 0110, 1001, 1011, 1111

STRATEGI ROUND 2 per template yang sulit:
  0010 (d3=1 only):  Narasi EKSPLISIT semua keyword rubrik + skor koheren + <25 kata
  0011 (d3+d4=1):    Versi pendek narasi pasar + keyword rubrik + skor koheren
  0100 (d2=1 only):  Narasi panjang dengan SEMUA keyword rubrik tapi skor=5 vs narasi negatif
  0110 (d2+d3=1):    Versi pendek dari 0100
  1001 (d1+d4=1):    Narasi produktivitas di QID standar kualitas, panjang, skor koheren
  1011 (d1+d3+d4=1): Narasi produktivitas di QID standar kualitas, pendek, skor koheren
  1111 (all=1):      Narasi produktivitas singkat di QID standar kualitas, skor=1 inkoherensi
"""

import requests
import time
import json

ENDPOINT = "http://host.docker.internal:8080/feedback/analyze"

QID_STANDAR_KUALITAS = "a22b2712-2135-4eb0-ad5e-b5fdc2753283"
QID_PRODUKTIVITAS    = "a22b2712-1186-410c-b62b-98016b338b29"
QID_KOMUNIKASI       = "a22b2712-1ea5-4d48-871f-392c005c8311"
QID_MANAJEMEN_TIM    = "a22b2712-201d-407b-9f2c-248f9997f522"

ELABORASI_THRESHOLD = 25

def words(s): return len(s.split())

def load_templates(path="/workspace/prompt_templates.json"):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {k: {"active": [], "variables": []} for k in [
            "invalid", "0000",
            "0001","0010","0011","0100","0101","0110","0111",
            "1000","1001","1010","1011","1100","1101","1110","1111"
        ]}

def compute_template_key(valid, d1, d2, d3, d4):
    if not valid:
        return "invalid"
    return f"{d1}{d2}{d3}{d4}"

# ══════════════════════════════════════════════════════════════════════════════
# SKENARIO (Round 2 — revised berdasarkan temuan Round 1)
# ══════════════════════════════════════════════════════════════════════════════
template_scenarios = [

    # ─────────────────────────────────────────────────────────────────
    # KELOMPOK V — Template "invalid" (valid=False)
    # Semua 4 PASS di Round 1 — tidak diubah
    # ─────────────────────────────────────────────────────────────────
    {
        "id": "V01", "group": "Template[invalid] — Narasi kosong",
        "q_id": QID_STANDAR_KUALITAS, "skor": 3,
        "narasi": "",
        "expected_template": "invalid", "expected": {"valid": False}
    },
    {
        "id": "V02", "group": "Template[invalid] — Hanya angka",
        "q_id": QID_STANDAR_KUALITAS, "skor": 3,
        "narasi": "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25",
        "expected_template": "invalid", "expected": {"valid": False}
    },
    {
        "id": "V03", "group": "Template[invalid] — Hanya spasi",
        "q_id": QID_STANDAR_KUALITAS, "skor": 3,
        "narasi": "           ",
        "expected_template": "invalid", "expected": {"valid": False}
    },
    {
        "id": "V04", "group": "Template[invalid] — Gibberish murni",
        "q_id": QID_STANDAR_KUALITAS, "skor": 3,
        "narasi": "asdfghjkl qwertyuiop asdfghjkl qwertyuiop zxcvbnm asdfghjkl",
        "expected_template": "invalid", "expected": {"valid": False}
    },

    # ─────────────────────────────────────────────────────────────────
    # KELOMPOK W — Template "0000" (semua indikator terpenuhi)
    # W01 PASS di Round 1 — tidak diubah
    # ─────────────────────────────────────────────────────────────────
    {
        "id": "W01",
        "group": "Template[0000] — Narasi ideal skor 5 (TERBUKTI Round 1)",
        "q_id": QID_STANDAR_KUALITAS, "skor": 5,
        "narasi": (
            "Rekan saya menunjukkan komitmen kerja yang sangat tinggi selama proyek berlangsung. "
            "Dia selalu memastikan kualitas hasil akhir memenuhi standar yang disepakati, "
            "melakukan evaluasi secara berkala dan segera memperbaiki kekurangan. "
            "Kontribusinya sangat menentukan keberhasilan tim."
        ),
        "expected_template": "0000", "expected": {"valid": True, "d1": 0, "d2": 0, "d3": 0, "d4": 0}
    },
    {
        "id": "W02",
        "group": "Template[0000] — Narasi ideal skor 5 versi I02 (terbukti koheren di FINAL test)",
        "q_id": QID_STANDAR_KUALITAS, "skor": 5,
        "narasi": (
            "Rekan saya adalah yang terbaik dalam hal komitmen kerja dan standar kualitas. "
            "Kualitas hasil akhir pekerjaannya selalu melampaui ekspektasi. "
            "Evaluasinya mendalam dan perbaikan yang dilakukan sangat signifikan meningkatkan mutu produk akhir tim."
        ),
        "expected_template": "0000", "expected": {"valid": True, "d1": 0, "d2": 0, "d3": 0, "d4": 0}
    },

    # ─────────────────────────────────────────────────────────────────
    # KELOMPOK U — Kombinasi "0001" hingga "1111"
    # ─────────────────────────────────────────────────────────────────

    # ── "0001": d4=1 saja — TERBUKTI PASS Round 1 ──
    {
        "id": "U01",
        "group": "Template[0001] — TERBUKTI: narasi pasar + keyword rubrik, skor koheren",
        "q_id": QID_STANDAR_KUALITAS, "skor": 3,
        "narasi": (
            "Saya kemarin pergi ke pasar membeli sayur dan menemukan komitmen kerja pedagang yang tinggi. "
            "Standar kualitas dagangannya terjaga, evaluasi dan perbaikan kualitas pekerjaan terlihat nyata "
            "pada setiap produk yang dijual di pasar tersebut setiap harinya."
        ),
        "expected_template": "0001", "expected": {"valid": True, "d1": 0, "d2": 0, "d3": 0, "d4": 1}
    },

    # ── "0010": d3=1 saja ──
    # Round 1 gagal: narasi 9 kata → 0111. Hipotesis: narasi terlalu pendek & ambigu
    # Strategi Round 2: Semua keyword rubrik disebut eksplisit (→d1=0) + skor=4 (→d2=0)
    # + di bawah 25 kata (→d3=1) + tidak off-topic (→d4=0)
    # Versi A: keyword eksplisit lengkap, ~12 kata
    {
        "id": "U02a",
        "group": "Template[0010] — d3=1: keyword rubrik eksplisit, skor 4 koheren, <25 kata (v.A)",
        "q_id": QID_STANDAR_KUALITAS, "skor": 4,
        "narasi": (
            "Komitmen kerja rekan baik. Standar kualitas terpenuhi. "
            "Kualitas hasil akhir memuaskan. Evaluasi dilakukan."
        ),
        "expected_template": "0010", "expected": {"valid": True, "d1": 0, "d2": 0, "d3": 1, "d4": 0}
    },
    # Versi B: kalimat narasi natural, ~18 kata
    {
        "id": "U02b",
        "group": "Template[0010] — d3=1: kalimat natural dengan keyword rubrik, skor 4 koheren (v.B)",
        "q_id": QID_STANDAR_KUALITAS, "skor": 4,
        "narasi": (
            "Rekan saya menunjukkan komitmen kerja yang baik. "
            "Standar kualitas dan kualitas hasil akhir pekerjaan sudah terpenuhi."
        ),
        "expected_template": "0010", "expected": {"valid": True, "d1": 0, "d2": 0, "d3": 1, "d4": 0}
    },

    # ── "0011": d3=1 + d4=1 ──
    # Strategi: Versi pendek narasi pasar + keyword rubrik (yang terbukti bisa d4=1)
    {
        "id": "U03",
        "group": "Template[0011] — d3+d4=1: pasar + keyword rubrik pendek, skor koheren",
        "q_id": QID_STANDAR_KUALITAS, "skor": 3,
        "narasi": (
            "Di pasar tadi saya melihat komitmen kerja yang bagus. "
            "Standar kualitas produk dijaga. Evaluasi rutin dilakukan."
        ),
        "expected_template": "0011", "expected": {"valid": True, "d1": 0, "d2": 0, "d3": 1, "d4": 1}
    },

    # ── "0100": d2=1 saja — PALING SULIT ──
    # Kunci: d1=0 memerlukan semua keyword rubrik tersebut eksplisit dalam narasi negatif
    # Skor=5 tapi narasi sangat negatif + panjang ≥25 kata + on-topic
    # Versi A: Langsung sebut semua criteria rubrik dengan konotasi negatif
    {
        "id": "U04a",
        "group": "Template[0100] — d2=1: semua keyword rubrik disebut + skor=5 + narasi negatif ≥25 kata (v.A)",
        "q_id": QID_STANDAR_KUALITAS, "skor": 5,
        "narasi": (
            "Standar kualitas pekerjaan rekan saya tidak dijaga dengan baik sama sekali. "
            "Kualitas hasil akhir yang dihasilkan selalu sangat buruk dan mengecewakan. "
            "Komitmen kerja sangat rendah dan evaluasi tidak pernah dilakukan secara konsisten "
            "selama proyek berlangsung dari awal hingga akhir penyelesaian."
        ),
        "expected_template": "0100", "expected": {"valid": True, "d1": 0, "d2": 1, "d3": 0, "d4": 0}
    },
    # Versi B: Formulasi berbeda — narasi negatif dgn penyebutan eksplisit semua kriteria
    {
        "id": "U04b",
        "group": "Template[0100] — d2=1: semua kriteria rubrik disebut dengan kata negatif, skor=5 (v.B)",
        "q_id": QID_STANDAR_KUALITAS, "skor": 5,
        "narasi": (
            "Komitmen kerja rekan saya sangat buruk dan tidak konsisten. "
            "Standar kualitas diabaikan dan kualitas hasil akhir sangat jauh dari ekspektasi. "
            "Evaluasi dan perbaikan kualitas pekerjaan tidak pernah dilakukan dengan serius. "
            "Motivasinya sangat rendah sepanjang proyek ini."
        ),
        "expected_template": "0100", "expected": {"valid": True, "d1": 0, "d2": 1, "d3": 0, "d4": 0}
    },

    # ── "0110": d2=1 + d3=1 ──
    # Strategi: Versi pendek dari 0100 (<25 kata) dengan semua keyword rubrik disebut
    {
        "id": "U06",
        "group": "Template[0110] — d2+d3=1: keyword rubrik pendek + skor=5 negatif",
        "q_id": QID_STANDAR_KUALITAS, "skor": 5,
        "narasi": (
            "Komitmen kerja buruk. Standar kualitas diabaikan. "
            "Kualitas hasil akhir mengecewakan. Evaluasi tidak dilakukan."
        ),
        "expected_template": "0110", "expected": {"valid": True, "d1": 0, "d2": 1, "d3": 1, "d4": 0}
    },

    # ── "0101": d2=1 + d4=1 ──
    # Strategi: Narasi pasar + keyword rubrik (d4=1) + skor=5 tapi narasi negatif (d2=1) + panjang
    {
        "id": "U05",
        "group": "Template[0101] — d2+d4=1: pasar + keyword rubrik panjang + skor=5 tapi negatif",
        "q_id": QID_STANDAR_KUALITAS, "skor": 5,
        "narasi": (
            "Saya kemarin ke pasar dan pedagangnya sama sekali tidak menjaga "
            "standar kualitas dagangannya. Komitmen kerja mereka rendah sekali dan kualitas hasil akhir "
            "produk sangat buruk. Evaluasi dan perbaikan kualitas pekerjaan tidak pernah dilakukan."
        ),
        "expected_template": "0101", "expected": {"valid": True, "d1": 0, "d2": 1, "d3": 0, "d4": 1}
    },

    # ── "0111": d2=1 + d3=1 + d4=1 ──
    # Strategi: Versi pendek dari 0101
    {
        "id": "U07",
        "group": "Template[0111] — d2+d3+d4=1: pasar + keyword rubrik pendek + skor=5 negatif",
        "q_id": QID_STANDAR_KUALITAS, "skor": 5,
        "narasi": (
            "Di pasar, standar kualitas tidak dijaga. "
            "Komitmen kerja rendah. Kualitas hasil akhir buruk."
        ),
        "expected_template": "0111", "expected": {"valid": True, "d1": 0, "d2": 1, "d3": 1, "d4": 1}
    },

    # ── "1000": d1=1 saja — TERBUKTI PASS Round 1 ──
    {
        "id": "U08",
        "group": "Template[1000] — TERBUKTI: pujian generik panjang skor koheren",
        "q_id": QID_STANDAR_KUALITAS, "skor": 5,
        "narasi": (
            "Rekan saya adalah orang yang sangat baik, ramah, dan selalu mau membantu siapapun yang kesulitan. "
            "Dia mudah bergaul dan menyenangkan diajak bekerjasama. "
            "Orangnya juga jujur dan tidak pernah berbohong kepada anggota tim."
        ),
        "expected_template": "1000", "expected": {"valid": True, "d1": 1, "d2": 0, "d3": 0, "d4": 0}
    },

    # ── "1001": d1=1 + d4=1 ──
    # Round 1 gagal: artikel berita → 1100 (d2 ikut terpicu, d4=0).
    # Strategi Round 2: Narasi produktivitas (aspek lain) di QID standar kualitas
    # → d1=1 (rubrik kualitas tidak covered) + d4=1 (mutual exclusivity)
    # + skor=3 netral (d2=0) + panjang ≥25 kata (d3=0)
    {
        "id": "U09",
        "group": "Template[1001] — d1+d4=1: narasi produktivitas di QID standar kualitas, panjang, skor netral",
        "q_id": QID_STANDAR_KUALITAS, "skor": 3,
        "narasi": (
            "Rekan saya cukup produktif dalam mengerjakan tugas-tugas yang diberikan oleh tim. "
            "Kontribusinya terhadap penyelesaian bagian proyek yang menjadi tanggung jawabnya "
            "cukup memadai meskipun tidak selalu tepat waktu. "
            "Tingkat produktivitas kerjanya berada di sekitar rata-rata anggota tim secara keseluruhan."
        ),
        "expected_template": "1001", "expected": {"valid": True, "d1": 1, "d2": 0, "d3": 0, "d4": 1}
    },

    # ── "1010": d1=1 + d3=1 — TERBUKTI PASS Round 1 ──
    {
        "id": "U10",
        "group": "Template[1010] — TERBUKTI: pujian generik singkat",
        "q_id": QID_STANDAR_KUALITAS, "skor": 5,
        "narasi": "Rekan saya sangat baik dan menyenangkan diajak kerja sama.",
        "expected_template": "1010", "expected": {"valid": True, "d1": 1, "d2": 0, "d3": 1, "d4": 0}
    },

    # ── "1011": d1=1 + d3=1 + d4=1 ──
    # Strategi: Versi pendek dari 1001 (produktivitas di QID kualitas, pendek, skor koheren)
    {
        "id": "U11",
        "group": "Template[1011] — d1+d3+d4=1: narasi produktivitas singkat di QID standar kualitas",
        "q_id": QID_STANDAR_KUALITAS, "skor": 3,
        "narasi": "Rekan saya cukup produktif dan kontribusi penyelesaian tugasnya memadai.",
        "expected_template": "1011", "expected": {"valid": True, "d1": 1, "d2": 0, "d3": 1, "d4": 1}
    },

    # ── "1100": d1=1 + d2=1 — TERBUKTI PASS Round 1 ──
    {
        "id": "U12",
        "group": "Template[1100] — TERBUKTI: pujian generik panjang skor=1",
        "q_id": QID_STANDAR_KUALITAS, "skor": 1,
        "narasi": (
            "Rekan saya adalah orang yang sangat baik hati, selalu ramah dan jujur "
            "kepada semua anggota tim. Dia menyenangkan untuk diajak bekerja sama "
            "dan tidak pernah membuat masalah apapun di dalam kelompok kami."
        ),
        "expected_template": "1100", "expected": {"valid": True, "d1": 1, "d2": 1, "d3": 0, "d4": 0}
    },

    # ── "1101": d1=1 + d2=1 + d4=1 ──
    # Round 1: X02 (narasi kualitas di QID produktivitas, skor=4) → 1101 (actual)
    # Konfirmasi: pakai skor=1 agar d2 lebih mudah terpicu (positif vs skor rendah)
    {
        "id": "U13",
        "group": "Template[1101] — KONFIRMASI X02 Round1: narasi kualitas di QID produktivitas, skor=1",
        "q_id": QID_PRODUKTIVITAS, "skor": 1,
        "narasi": (
            "Rekan saya menunjukkan standar kualitas yang baik dan selalu mengevaluasi pekerjaan "
            "serta memperbaiki kualitas hasil akhirnya. Komitmen kerjanya terhadap mutu produk "
            "sangat patut diapresiasi oleh seluruh anggota tim selama proyek berlangsung."
        ),
        "expected_template": "1101", "expected": {"valid": True, "d1": 1, "d2": 1, "d3": 0, "d4": 1}
    },

    # ── "1110": d1=1 + d2=1 + d3=1 — TERBUKTI PASS Round 1 ──
    {
        "id": "U14",
        "group": "Template[1110] — TERBUKTI: pujian generik singkat skor=1",
        "q_id": QID_STANDAR_KUALITAS, "skor": 1,
        "narasi": "Rekan saya sangat baik dan menyenangkan diajak kerja.",
        "expected_template": "1110", "expected": {"valid": True, "d1": 1, "d2": 1, "d3": 1, "d4": 0}
    },

    # ── "1111": semua d=1 ──
    # Strategi: narasi produktivitas SINGKAT di QID standar kualitas + skor=1 (inkoherensi)
    # → d1=1 (rubrik kualitas tidak covered) + d2=1 (skor=1 tapi narasi positif)
    # + d3=1 (<25 kata) + d4=1 (mutual exclusivity aspek produktivitas vs kualitas)
    {
        "id": "U15",
        "group": "Template[1111] — Semua d=1: narasi produktivitas singkat di QID kualitas, skor=1",
        "q_id": QID_STANDAR_KUALITAS, "skor": 1,
        "narasi": "Rekan saya sangat produktif dan selalu menyelesaikan tugas tepat waktu.",
        "expected_template": "1111", "expected": {"valid": True, "d1": 1, "d2": 1, "d3": 1, "d4": 1}
    },

    # ════════════════════════════════════════════════════════════════════
    # KELOMPOK X — Konfirmasi via QID berbeda + skenario eksplorasi
    # ════════════════════════════════════════════════════════════════════
    {
        "id": "X01",
        "group": "Template[0000] via QID Komunikasi — narasi komunikasi ideal (J03 PASS di FINAL)",
        "q_id": QID_KOMUNIKASI, "skor": 5,
        "narasi": (
            "Kualitas interaksi dan komunikasi rekan saya selama bekerja dalam tim sangat baik. "
            "Dia selalu menyampaikan informasi dengan jelas, efektif, dan tepat sasaran. "
            "Efektivitas komunikasinya membuat koordinasi tim menjadi jauh lebih lancar dan produktif."
        ),
        "expected_template": "0000", "expected": {"valid": True, "d3": 0}
    },
    {
        "id": "X02",
        "group": "Template[1101] KONFIRMASI via QID Produktivitas skor=4 (Round 1 X02 actual=1101)",
        "q_id": QID_PRODUKTIVITAS, "skor": 4,
        "narasi": (
            "Rekan saya menunjukkan standar kualitas yang baik dan selalu mengevaluasi pekerjaan "
            "serta memperbaiki kualitas hasil akhirnya. Komitmen kerjanya terhadap mutu produk "
            "sangat patut diapresiasi oleh seluruh anggota tim selama proyek."
        ),
        "expected_template": "1101", "expected": {"valid": True, "d1": 1, "d2": 1, "d3": 0, "d4": 1}
    },
    {
        "id": "X03",
        "group": "Template[1100] via QID Manajemen Tim — pujian generik skor=1",
        "q_id": QID_MANAJEMEN_TIM, "skor": 1,
        "narasi": (
            "Rekan saya adalah orang yang sangat baik hati dan selalu ramah kepada semua anggota tim. "
            "Dia mudah bergaul dan menyenangkan untuk diajak bekerjasama dalam kondisi apapun "
            "selama proyek berlangsung dari awal hingga selesai."
        ),
        "expected_template": "1100", "expected": {"valid": True, "d1": 1, "d2": 1, "d3": 0}
    },
    # Eksplorasi: narasi produktivitas di QID kualitas PANJANG skor=3 → apakah d4=1?
    {
        "id": "X04",
        "group": "Eksplorasi[1001?] — narasi produktivitas panjang di QID kualitas, skor 3",
        "q_id": QID_STANDAR_KUALITAS, "skor": 3,
        "narasi": (
            "Rekan saya sangat produktif selama pengerjaan proyek. "
            "Dia selalu menyelesaikan tugas lebih cepat dari deadline dan mengambil tanggung jawab ekstra. "
            "Kontribusi dan kecepatan kerjanya melampaui ekspektasi saya sejak awal proyek berlangsung."
        ),
        "expected_template": "1001",  # Hipotesis: d1=1 (kualitas tidak covered) + d4=1 (aspek lain)
        "expected": {"valid": True, "d1": 1, "d3": 0}  # d2, d4 observasional
    },

    # ════════════════════════════════════════════════════════════════════
    # KELOMPOK Y — Verifikasi Variabel Template (substitusi placeholder)
    # ════════════════════════════════════════════════════════════════════
    {
        "id": "Y01",
        "group": "Variabel[target_aspect] — Template 0001 (TERBUKTI PASS Round 1)",
        "q_id": QID_STANDAR_KUALITAS, "skor": 3,
        "narasi": (
            "Saya kemarin pergi ke pasar membeli sayur dan menemukan komitmen kerja pedagang yang tinggi. "
            "Standar kualitas dagangannya terjaga, evaluasi dan perbaikan kualitas pekerjaan terlihat nyata "
            "pada setiap produk yang dijual di pasar tersebut setiap harinya."
        ),
        "expected_template": "0001",
        "expected": {"valid": True, "d4": 1},
        "check_scaffold_vars": ["target_aspect"]
    },
    {
        "id": "Y02",
        "group": "Variabel[missing_coverage] — Template 1000 (TERBUKTI PASS Round 1)",
        "q_id": QID_STANDAR_KUALITAS, "skor": 5,
        "narasi": (
            "Rekan saya adalah orang yang sangat baik, ramah, dan selalu mau membantu siapapun yang kesulitan. "
            "Dia mudah bergaul dan menyenangkan diajak bekerjasama. "
            "Orangnya juga jujur dan tidak pernah berbohong kepada anggota tim."
        ),
        "expected_template": "1000",
        "expected": {"valid": True, "d1": 1},
        "check_scaffold_vars": ["missing_coverage"]
    },
    {
        "id": "Y03",
        "group": "Variabel[input_skor+predicted_skor] — Template 1100 (pakai narasi TERBUKTI 1100)",
        "q_id": QID_STANDAR_KUALITAS, "skor": 1,
        "narasi": (
            "Rekan saya adalah orang yang sangat baik hati, selalu ramah dan jujur "
            "kepada semua anggota tim. Dia menyenangkan untuk diajak bekerja sama "
            "dan tidak pernah membuat masalah apapun di dalam kelompok kami."
        ),
        "expected_template": "1100",
        "expected": {"valid": True, "d1": 1, "d2": 1},
        "check_scaffold_vars": ["input_skor", "predicted_skor"]
    },
    {
        "id": "Y04",
        "group": "Variabel[missing_coverage+input_skor+predicted_skor] — Template 1110 (TERBUKTI PASS)",
        "q_id": QID_STANDAR_KUALITAS, "skor": 1,
        "narasi": "Rekan saya sangat baik dan menyenangkan diajak kerja.",
        "expected_template": "1110",
        "expected": {"valid": True, "d1": 1, "d2": 1, "d3": 1},
        "check_scaffold_vars": ["missing_coverage", "input_skor", "predicted_skor"]
    },
]

# ══════════════════════════════════════════════════════════════════════
# RUNNER
# ══════════════════════════════════════════════════════════════════════
def run_template_tests():
    templates = load_templates()

    print("=" * 70)
    print("TEMPLATE COVERAGE TEST — Round 2")
    print(f"Endpoint : {ENDPOINT}")
    print(f"Skenario : {len(template_scenarios)} total")
    print("=" * 70)

    results = []
    total = len(template_scenarios)

    for i, tc in enumerate(template_scenarios):
        payload = {
            "NIM": f"TMPL_R2_{tc['id']}",
            "type": "assessment",
            "question_id": tc["q_id"],
            "feedback": {
                "skor": tc["skor"],
                "narasi": tc["narasi"]
            }
        }

        try:
            print(f"[{i+1:02d}/{total}] {tc['id']} — {tc['group'][:60]}")
            t0 = time.time()
            resp = requests.post(ENDPOINT, json=payload, timeout=15)
            latency = round(time.time() - t0, 2)

            if resp.status_code == 200:
                data = resp.json()
                ind = data.get("indicators", {})

                act_valid = ind.get("valid", None)
                act_d1    = ind.get("d1", None)
                act_d2    = ind.get("d2", None)
                act_d3    = ind.get("d3", None)
                act_d4    = ind.get("d4", None)

                if act_valid is not None:
                    act_key = compute_template_key(
                        act_valid,
                        act_d1 if act_d1 is not None else 0,
                        act_d2 if act_d2 is not None else 0,
                        act_d3 if act_d3 is not None else 0,
                        act_d4 if act_d4 is not None else 0,
                    )
                else:
                    act_key = "unknown"

                verdict = "PASS"
                notes = []

                for key, exp in tc.get("expected", {}).items():
                    act = ind.get(key)
                    if act != exp:
                        verdict = "FAIL"
                        notes.append(f"{key}(E:{exp},A:{act})")

                exp_key = tc.get("expected_template", "?")
                if act_key != exp_key:
                    verdict = "FAIL"
                    notes.append(f"key(E:{exp_key},A:{act_key})")

                scaffold_output = str(
                    data.get("scaffolding") or data.get("scaffold") or
                    data.get("prompt") or data.get("message") or ""
                )
                scaffold_var_status = "-"
                if tc.get("check_scaffold_vars"):
                    unresolved = [v for v in tc["check_scaffold_vars"] if "{"+v+"}" in scaffold_output]
                    if unresolved:
                        scaffold_var_status = f"UNRESOLVED:{unresolved}"
                        if scaffold_output:
                            verdict = "FAIL"
                            notes.append(f"unresolved:{unresolved}")
                    elif scaffold_output:
                        scaffold_var_status = "vars_ok"
                    else:
                        scaffold_var_status = "no_scaffold_field"

                template_exists = exp_key in templates
                results.append({
                    "ID": tc["id"], "Group": tc["group"][:65],
                    "Skor": tc["skor"], "Words": words(tc["narasi"]),
                    "valid": act_valid,
                    "d1": act_d1, "d2": act_d2, "d3": act_d3, "d4": act_d4,
                    "Act_Key": act_key, "Exp_Key": exp_key,
                    "Template_InJSON": template_exists,
                    "Scaffold_Vars": scaffold_var_status,
                    "Verdict": verdict,
                    "Notes": ", ".join(notes) if notes else "-",
                    "Latency": latency,
                })
                icon = "✅" if verdict == "PASS" else "❌"
                print(f"  → act={act_key} | exp={exp_key} | {icon} {verdict} | {', '.join(notes) or '-'}")
            else:
                results.append({
                    "ID": tc["id"], "Group": tc["group"][:65],
                    "Skor": tc["skor"], "Words": words(tc["narasi"]),
                    "valid":"?","d1":"?","d2":"?","d3":"?","d4":"?",
                    "Act_Key":"?","Exp_Key":tc.get("expected_template","?"),
                    "Template_InJSON":False,"Scaffold_Vars":"-",
                    "Verdict":"ERROR","Notes":f"HTTP {resp.status_code}","Latency":"-"
                })
        except requests.exceptions.ConnectionError:
            print(f"  ⚠️  Connection refused!")
            results.append({
                "ID":tc["id"],"Group":tc["group"][:65],
                "Skor":tc["skor"],"Words":words(tc["narasi"]),
                "valid":"?","d1":"?","d2":"?","d3":"?","d4":"?",
                "Act_Key":"?","Exp_Key":tc.get("expected_template","?"),
                "Template_InJSON":False,"Scaffold_Vars":"-",
                "Verdict":"ERROR","Notes":"Connection refused","Latency":"-"
            })
            break
        except Exception as e:
            results.append({
                "ID":tc["id"],"Group":tc["group"][:65],
                "Skor":tc["skor"],"Words":words(tc["narasi"]),
                "valid":"?","d1":"?","d2":"?","d3":"?","d4":"?",
                "Act_Key":"?","Exp_Key":tc.get("expected_template","?"),
                "Template_InJSON":False,"Scaffold_Vars":"-",
                "Verdict":"ERROR","Notes":str(e)[:80],"Latency":"-"
            })

    passed = sum(1 for r in results if r["Verdict"] == "PASS")
    failed = sum(1 for r in results if r["Verdict"] == "FAIL")
    errors = sum(1 for r in results if r["Verdict"] == "ERROR")

    expected_keys = set(templates.keys())
    triggered_keys = {r["Act_Key"] for r in results if r["Act_Key"] not in ("?","unknown")}
    not_triggered = expected_keys - triggered_keys

    print(f"\n{'='*70}")
    print(f"SELESAI. {len(results)} skenario.")
    print(f"✅ PASS={passed} | ❌ FAIL={failed} | ⚠️ ERR={errors}")
    print(f"Terpicu    : {sorted(triggered_keys)}")
    print(f"Belum      : {sorted(not_triggered)}")

    md_out = "/workspace/Template_Coverage_Results_Round2.md"
    with open(md_out, "w", encoding="utf-8") as f:
        f.write("# Hasil Validasi Template Coverage — Round 2\n\n")
        f.write(f"> **{len(results)} skenario** | ✅ {passed} PASS | ❌ {failed} FAIL | ⚠️ {errors} Error\n\n")

        f.write("## Coverage Matrix\n\n")
        f.write("| Template | Active Indicators | Status | Skenario |\n")
        f.write("|---|---|---|---|\n")
        for key in sorted(templates.keys()):
            active = ", ".join(templates[key].get("active", [])) or "(tidak ada intervensi)"
            trig = "✅ Terpicu" if key in triggered_keys else "❌ Belum terpicu"
            sc_ids = [r["ID"] for r in results if r["Act_Key"] == key]
            f.write(f"| `{key}` | {active} | {trig} | {', '.join(sc_ids) or '-'} |\n")

        groups = [
            ("V","V — Template 'invalid'"),
            ("W","W — Template '0000' (semua terpenuhi)"),
            ("U","U — Kombinasi '0001'–'1111'"),
            ("X","X — Variasi Multi-Question"),
            ("Y","Y — Verifikasi Variabel Template"),
        ]
        for prefix, label in groups:
            gr = [r for r in results if r["ID"].startswith(prefix)]
            if not gr: continue
            f.write(f"\n## {label}\n\n")
            f.write("| ID | Exp | Act | Skor | Kata | valid | d1 | d2 | d3 | d4 | Vars | Verdict | Catatan |\n")
            f.write("|---|---|---|---|---|---|---|---|---|---|---|---|---|\n")
            for r in gr:
                icon = {"PASS":"✅","FAIL":"❌","ERROR":"⚠️"}.get(r["Verdict"],"?")
                f.write(
                    f"| **{r['ID']}** | `{r['Exp_Key']}` | `{r['Act_Key']}` "
                    f"| {r['Skor']} | {r['Words']} | {r['valid']} "
                    f"| {r['d1']} | {r['d2']} | {r['d3']} | {r['d4']} "
                    f"| {r['Scaffold_Vars']} | {icon} {r['Verdict']} | {r['Notes']} |\n"
                )

        f.write("\n---\n\n## Temuan & Analisis Round 2\n\n")
        if not_triggered:
            f.write("### ⚠️ Template Belum Terpicu\n")
            for k in sorted(not_triggered):
                f.write(f"- `{k}` ({', '.join(templates[k].get('active',[]))})\n")
        else:
            f.write("### ✅ SEMUA 17 TEMPLATE BERHASIL TERPICU\n")

        f.write("\n### Pola Perilaku d-bit yang Teridentifikasi\n\n")
        f.write(
            "| Indikator | Pola Perilaku |\n"
            "|---|---|\n"
            "| **d4 (Relevansi Topik)** | Hanya terpicu via *mutual exclusivity* — narasi menggunakan keyword rubrik dalam konteks aspek berbeda (pasar, produktivitas di QID kualitas). Narasi completely off-topic (resep, berita) TIDAK memicu d4. |\n"
            "| **d1 (Cakupan Rubrik)** | Sering co-trigger dengan d2. Narasi yang inkoherensi (skor≠narasi) cenderung tidak cover kriteria rubrik secara eksplisit. |\n"
            "| **d2 (Koherensi)** | Dapat berdiri sendiri (template 0100) hanya jika narasi EKSPLISIT menyebut semua keyword rubrik tapi skor tidak sesuai. |\n"
            "| **d3 (Elaborasi)** | Paling deterministik: count kata < 25 → d3=1. Sering co-trigger karena narasi pendek juga ambigu secara semantik. |\n"
        )
        f.write(f"\n---\n*Round 2 — {len(results)} skenario*\n")

    print(f"\nLaporan: {md_out}")

if __name__ == "__main__":
    run_template_tests()
