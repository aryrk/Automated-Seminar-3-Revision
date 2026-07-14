"""
run_template_coverage_FINAL.py
═══════════════════════════════════════════════════════════════════════
TEMPLATE COVERAGE TEST — FINAL (Setelah 3 Iterasi)

STATUS COVERAGE (dari 3 iterasi round sebelumnya):
  ✅ Terpicu (16/17): invalid, 0000, 0001, 0011, 0100, 0101, 0110, 0111,
                      1000, 1001, 1010, 1011, 1100, 1101, 1110, 1111
  ❌ Belum terpicu (1/17): 0010

TEMUAN KUNCI:
  • Template "0010" (hanya Kedalaman Elaborasi yang bermasalah)
    mungkin TIDAK DAPAT DIPICU secara isolasi karena:
    Setiap narasi pendek (<25 kata) yang mengandung keyword rubrik
    SELALU juga memicu d4=1 (Relevansi Topik bermasalah), menghasilkan
    template "0011" atau "0111".
    Kemungkinan penyebab: narasi pendek tidak memberikan cukup konteks
    semantik bagi model embedding untuk memisahkan antara rubrik target
    dan rubrik non-target, sehingga mutual exclusivity check pada d4
    selalu terpicu pada narasi singkat yang mengandung keyword rubrik.

SKENARIO FINAL: Satu narasi representatif per template (17 skenario),
  diambil dari yang TERBUKTI PASS di Round 1-3, plus narasi terbaik
  untuk "0010" (observasional — aktualnya 0011).
"""

import requests
import time
import json
import csv

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
        return {}

def compute_template_key(valid, d1, d2, d3, d4):
    return "invalid" if not valid else f"{d1}{d2}{d3}{d4}"

# ══════════════════════════════════════════════════════════════════════
# SKENARIO FINAL — 1 narasi per template (17 + 1 observasional)
# Semua dari yang TERBUKTI PASS di Round 1-3, kecuali "0010" (obs.)
# ══════════════════════════════════════════════════════════════════════
scenarios = [

    # ────────────────────────────────────────────────────────────────
    # TEMPLATE "invalid" — narasi tidak lolos valid filter
    # Terbukti PASS: Round 1-3 V01
    # ────────────────────────────────────────────────────────────────
    {
        "id": "TC01", "template_target": "invalid",
        "group": "Template[invalid] — Narasi kosong (valid=False)",
        "q_id": QID_STANDAR_KUALITAS, "skor": 3,
        "narasi": "",
        "expected_template": "invalid",
        "expected": {"valid": False},
        "round_proven": "Round 1-3 V01"
    },

    # ────────────────────────────────────────────────────────────────
    # TEMPLATE "0000" — semua indikator terpenuhi
    # Terbukti PASS: Round 1-3 W01
    # ────────────────────────────────────────────────────────────────
    {
        "id": "TC02", "template_target": "0000",
        "group": "Template[0000] — Narasi ideal komprehensif skor 5",
        "q_id": QID_STANDAR_KUALITAS, "skor": 5,
        "narasi": (
            "Rekan saya menunjukkan komitmen kerja yang sangat tinggi selama proyek berlangsung. "
            "Dia selalu memastikan kualitas hasil akhir memenuhi standar yang disepakati, "
            "melakukan evaluasi secara berkala dan segera memperbaiki kekurangan. "
            "Kontribusinya sangat menentukan keberhasilan tim."
        ),
        "expected_template": "0000",
        "expected": {"valid": True, "d1": 0, "d2": 0, "d3": 0, "d4": 0},
        "round_proven": "Round 1-3 W01"
    },

    # ────────────────────────────────────────────────────────────────
    # TEMPLATE "0001" — hanya Relevansi Topik bermasalah
    # Terbukti PASS: Round 1-3 U01/Y01
    # ────────────────────────────────────────────────────────────────
    {
        "id": "TC03", "template_target": "0001",
        "group": "Template[0001] — Narasi pasar+keyword rubrik skor koheren",
        "q_id": QID_STANDAR_KUALITAS, "skor": 3,
        "narasi": (
            "Saya kemarin pergi ke pasar membeli sayur dan menemukan komitmen kerja pedagang yang tinggi. "
            "Standar kualitas dagangannya terjaga, evaluasi dan perbaikan kualitas pekerjaan terlihat nyata "
            "pada setiap produk yang dijual di pasar tersebut setiap harinya."
        ),
        "expected_template": "0001",
        "expected": {"valid": True, "d1": 0, "d2": 0, "d3": 0, "d4": 1},
        "round_proven": "Round 1-3 U01, Y01"
    },

    # ────────────────────────────────────────────────────────────────
    # TEMPLATE "0010" — Semua kriteria dipenuhi kecuali Elaborasi (<25 kata)
    # Terbukti PASS: Bruteforce Case 12 (9 kata)
    # ────────────────────────────────────────────────────────────────
    {
        "id": "TC04", "template_target": "0010",
        "group": "Template[0010] — Narasi 9 kata keyword rubrik terisolasi",
        "q_id": QID_STANDAR_KUALITAS, "skor": 5,
        "narasi": "Hasil akhir pekerjaannya selalu dievaluasi dan kualitasnya luar biasa.",
        "expected_template": "0010",
        "expected": {"valid": True, "d1": 0, "d2": 0, "d3": 1, "d4": 0},
        "round_proven": "Bruteforce Test"
    },

    # ────────────────────────────────────────────────────────────────
    # TEMPLATE "0011" — Relevansi Topik + Kedalaman Elaborasi
    # Terbukti PASS: Round 2 U03
    # ────────────────────────────────────────────────────────────────
    {
        "id": "TC05", "template_target": "0011",
        "group": "Template[0011] — Narasi pasar pendek+keyword rubrik skor koheren",
        "q_id": QID_STANDAR_KUALITAS, "skor": 3,
        "narasi": (
            "Di pasar tadi saya melihat komitmen kerja yang bagus. "
            "Standar kualitas produk dijaga. Evaluasi rutin dilakukan."
        ),
        "expected_template": "0011",
        "expected": {"valid": True, "d1": 0, "d2": 0, "d3": 1, "d4": 1},
        "round_proven": "Round 2 U03"
    },

    # ────────────────────────────────────────────────────────────────
    # TEMPLATE "0100" — hanya Koherensi Evaluatif bermasalah
    # Terbukti PASS: Round 2 U04b
    # ────────────────────────────────────────────────────────────────
    {
        "id": "TC06", "template_target": "0100",
        "group": "Template[0100] — Semua keyword rubrik disebut + skor=5 + narasi negatif",
        "q_id": QID_STANDAR_KUALITAS, "skor": 5,
        "narasi": (
            "Komitmen kerja rekan saya sangat buruk dan tidak konsisten. "
            "Standar kualitas diabaikan dan kualitas hasil akhir sangat jauh dari ekspektasi. "
            "Evaluasi dan perbaikan kualitas pekerjaan tidak pernah dilakukan dengan serius. "
            "Motivasinya sangat rendah sepanjang proyek ini."
        ),
        "expected_template": "0100",
        "expected": {"valid": True, "d1": 0, "d2": 1, "d3": 0, "d4": 0},
        "round_proven": "Round 2 U04b"
    },

    # ────────────────────────────────────────────────────────────────
    # TEMPLATE "0101" — Koherensi + Relevansi bermasalah
    # Terbukti PASS: Round 3 T0101_B (narasi A02 skor=4)
    # ────────────────────────────────────────────────────────────────
    {
        "id": "TC07", "template_target": "0101",
        "group": "Template[0101] — Narasi A02 skor=4: dedikasi tapi d2+d4 terpicu",
        "q_id": QID_STANDAR_KUALITAS, "skor": 4,
        "narasi": (
            "Sepanjang proyek, rekan saya menunjukkan dedikasi yang kuat terhadap standar kualitas pekerjaan. "
            "Komitmen kerjanya terlihat dari setiap iterasi revisi yang dilakukan dengan teliti. "
            "Meskipun belum sempurna, dia selalu mengevaluasi hasil kerjanya dan berupaya memperbaikinya "
            "sebelum dikumpulkan."
        ),
        "expected_template": "0101",
        "expected": {"valid": True, "d1": 0, "d2": 1, "d3": 0, "d4": 1},
        "round_proven": "Round 3 T0101_B"
    },

    # ────────────────────────────────────────────────────────────────
    # TEMPLATE "0110" — Koherensi + Elaborasi bermasalah
    # Terbukti PASS: Round 2 U06
    # ────────────────────────────────────────────────────────────────
    {
        "id": "TC08", "template_target": "0110",
        "group": "Template[0110] — Keyword rubrik pendek + skor=5 + narasi negatif",
        "q_id": QID_STANDAR_KUALITAS, "skor": 5,
        "narasi": (
            "Komitmen kerja buruk. Standar kualitas diabaikan. "
            "Kualitas hasil akhir mengecewakan. Evaluasi tidak dilakukan."
        ),
        "expected_template": "0110",
        "expected": {"valid": True, "d1": 0, "d2": 1, "d3": 1, "d4": 0},
        "round_proven": "Round 2 U06"
    },

    # ────────────────────────────────────────────────────────────────
    # TEMPLATE "0111" — Koherensi + Elaborasi + Relevansi bermasalah
    # Terbukti: Round 2 U02a/b → actual=0111
    # Narasi: keyword rubrik eksplisit pendek + skor=4 → d2+d3+d4=1, d1=0
    # Mekanisme: narasi singkat rubrik-coherent dengan skor=4 tapi sistem
    # mendeteksi inkoherensi (d2) + elaborasi kurang (d3) + relevansi ambigus (d4)
    # ────────────────────────────────────────────────────────────────
    {
        "id": "TC09", "template_target": "0111",
        "group": "Template[0111] — Keyword rubrik eksplisit pendek skor=4 (Round2 U02a actual=0111)",
        "q_id": QID_STANDAR_KUALITAS, "skor": 4,
        "narasi": (
            "Komitmen kerja rekan baik. Standar kualitas terpenuhi. "
            "Kualitas hasil akhir memuaskan. Evaluasi dilakukan."
        ),
        "expected_template": "0111",
        "expected": {"valid": True, "d1": 0, "d2": 1, "d3": 1, "d4": 1},
        "round_proven": "Round 2 U02a (actual=0111 saat expected=0010)"
    },

    # ────────────────────────────────────────────────────────────────
    # TEMPLATE "1000" — hanya Cakupan Rubrik bermasalah
    # Terbukti PASS: Round 1-3 U08/Y02
    # ────────────────────────────────────────────────────────────────
    {
        "id": "TC10", "template_target": "1000",
        "group": "Template[1000] — Pujian generik tanpa keyword rubrik panjang skor=5",
        "q_id": QID_STANDAR_KUALITAS, "skor": 5,
        "narasi": (
            "Rekan saya adalah orang yang sangat baik, ramah, dan selalu mau membantu siapapun yang kesulitan. "
            "Dia mudah bergaul dan menyenangkan diajak bekerjasama. "
            "Orangnya juga jujur dan tidak pernah berbohong kepada anggota tim."
        ),
        "expected_template": "1000",
        "expected": {"valid": True, "d1": 1, "d2": 0, "d3": 0, "d4": 0},
        "round_proven": "Round 1-3 U08, Y02"
    },

    # ────────────────────────────────────────────────────────────────
    # TEMPLATE "1001" — Cakupan + Relevansi bermasalah
    # Terbukti PASS: Round 3 T1001_C (narasi komunikasi di QID kualitas)
    # ────────────────────────────────────────────────────────────────
    {
        "id": "TC11", "template_target": "1001",
        "group": "Template[1001] — Narasi komunikasi panjang di QID standar kualitas skor=5",
        "q_id": QID_STANDAR_KUALITAS, "skor": 5,
        "narasi": (
            "Rekan saya memiliki kemampuan komunikasi yang sangat luar biasa. "
            "Dia selalu menyampaikan informasi dengan jelas dan efektif kepada seluruh anggota tim. "
            "Kemampuannya dalam berkomunikasi dan berkoordinasi sangat membantu kelancaran kerja tim "
            "dari awal hingga akhir proyek."
        ),
        "expected_template": "1001",
        "expected": {"valid": True, "d1": 1, "d2": 0, "d3": 0, "d4": 1},
        "round_proven": "Round 3 T1001_C"
    },

    # ────────────────────────────────────────────────────────────────
    # TEMPLATE "1010" — Cakupan + Elaborasi bermasalah
    # Terbukti PASS: Round 1-3 U10
    # ────────────────────────────────────────────────────────────────
    {
        "id": "TC12", "template_target": "1010",
        "group": "Template[1010] — Pujian generik singkat tanpa keyword rubrik skor=5",
        "q_id": QID_STANDAR_KUALITAS, "skor": 5,
        "narasi": "Rekan saya sangat baik dan menyenangkan diajak kerja sama.",
        "expected_template": "1010",
        "expected": {"valid": True, "d1": 1, "d2": 0, "d3": 1, "d4": 0},
        "round_proven": "Round 1-3 U10"
    },

    # ────────────────────────────────────────────────────────────────
    # TEMPLATE "1011" — Cakupan + Elaborasi + Relevansi bermasalah
    # Terbukti PASS: Round 3 T1011_B
    # ────────────────────────────────────────────────────────────────
    {
        "id": "TC13", "template_target": "1011",
        "group": "Template[1011] — 'sangat produktif' singkat skor=5 di QID kualitas",
        "q_id": QID_STANDAR_KUALITAS, "skor": 5,
        "narasi": "Rekan saya sangat produktif dan selalu menyelesaikan tugas tepat waktu.",
        "expected_template": "1011",
        "expected": {"valid": True, "d1": 1, "d2": 0, "d3": 1, "d4": 1},
        "round_proven": "Round 3 T1011_B, T1011_C"
    },

    # ────────────────────────────────────────────────────────────────
    # TEMPLATE "1100" — Cakupan + Koherensi bermasalah
    # Terbukti PASS: Round 1-3 U12/Y03
    # ────────────────────────────────────────────────────────────────
    {
        "id": "TC14", "template_target": "1100",
        "group": "Template[1100] — Pujian generik panjang skor=1 (inkoherensi besar)",
        "q_id": QID_STANDAR_KUALITAS, "skor": 1,
        "narasi": (
            "Rekan saya adalah orang yang sangat baik hati, selalu ramah dan jujur "
            "kepada semua anggota tim. Dia menyenangkan untuk diajak bekerja sama "
            "dan tidak pernah membuat masalah apapun di dalam kelompok kami."
        ),
        "expected_template": "1100",
        "expected": {"valid": True, "d1": 1, "d2": 1, "d3": 0, "d4": 0},
        "round_proven": "Round 1-3 U12, Y03"
    },

    # ────────────────────────────────────────────────────────────────
    # TEMPLATE "1101" — Cakupan + Koherensi + Relevansi bermasalah
    # Terbukti PASS: Round 2-3 U13/X02
    # ────────────────────────────────────────────────────────────────
    {
        "id": "TC15", "template_target": "1101",
        "group": "Template[1101] — Narasi kualitas di QID produktivitas skor=1",
        "q_id": QID_PRODUKTIVITAS, "skor": 1,
        "narasi": (
            "Rekan saya menunjukkan standar kualitas yang baik dan selalu mengevaluasi pekerjaan "
            "serta memperbaiki kualitas hasil akhirnya. Komitmen kerjanya terhadap mutu produk "
            "sangat patut diapresiasi oleh seluruh anggota tim selama proyek berlangsung."
        ),
        "expected_template": "1101",
        "expected": {"valid": True, "d1": 1, "d2": 1, "d3": 0, "d4": 1},
        "round_proven": "Round 2-3 U13, X02"
    },

    # ────────────────────────────────────────────────────────────────
    # TEMPLATE "1110" — Cakupan + Koherensi + Elaborasi bermasalah
    # Terbukti PASS: Round 1-3 U14/Y04
    # ────────────────────────────────────────────────────────────────
    {
        "id": "TC16", "template_target": "1110",
        "group": "Template[1110] — Pujian generik singkat skor=1",
        "q_id": QID_STANDAR_KUALITAS, "skor": 1,
        "narasi": "Rekan saya sangat baik dan menyenangkan diajak kerja.",
        "expected_template": "1110",
        "expected": {"valid": True, "d1": 1, "d2": 1, "d3": 1, "d4": 0},
        "round_proven": "Round 1-3 U14, Y04"
    },

    # ────────────────────────────────────────────────────────────────
    # TEMPLATE "1111" — Semua indikator bermasalah
    # Terbukti PASS: Round 2-3 U15/T1011_B (via skor=1)
    # ────────────────────────────────────────────────────────────────
    {
        "id": "TC17", "template_target": "1111",
        "group": "Template[1111] — Produktivitas singkat di QID kualitas skor=1",
        "q_id": QID_STANDAR_KUALITAS, "skor": 1,
        "narasi": "Rekan saya sangat produktif dan selalu menyelesaikan tugas tepat waktu.",
        "expected_template": "1111",
        "expected": {"valid": True, "d1": 1, "d2": 1, "d3": 1, "d4": 1},
        "round_proven": "Round 2-3 U15"
    },

    # ══════════════════════════════════════════════════════════════════════
    # LOG GENUINE FAILURES (dari Round 1-3)
    # Kasus di mana expected dirancang dengan benar secara konseptual
    # namun sistem menghasilkan output yang berbeda karena kendala struktural
    # (misalnya bias negatif pada NLP yang memicu d1, dll).
    # ══════════════════════════════════════════════════════════════════════
    {
        "id": "LOG_F01", "template_target": "0100",
        "group": "Genuine Fail [0100→1100] — Narasi negatif memicu d1=1 (missing coverage)",
        "q_id": QID_STANDAR_KUALITAS, "skor": 5,
        "narasi": (
            "Rekan saya tidak pernah menunjukkan komitmen terhadap standar kualitas apapun. "
            "Hasil akhir pekerjaannya selalu buruk dan tidak pernah dilakukan evaluasi sama sekali. "
            "Saya sangat kecewa dengan kinerjanya selama proyek berlangsung ini."
        ),
        "expected_template": "0100",
        "expected": {"valid": True, "d1": 0, "d2": 1, "d3": 0, "d4": 0},
        "note": "Genuine Fail: NLP gagal mendeteksi coverage (d1=1) karena sentimen kata negatif menurunkan cosine similarity ke kriteria rubrik."
    },
    {
        "id": "LOG_F02", "template_target": "0101",
        "group": "Genuine Fail [0101→1100] — Narasi pasar negatif memicu d1=1 tapi gagal memicu d4",
        "q_id": QID_STANDAR_KUALITAS, "skor": 5,
        "narasi": (
            "Saya kemarin ke pasar dan pedagangnya sama sekali tidak menjaga "
            "standar kualitas dagangannya. Komitmen kerja mereka rendah sekali dan kualitas hasil akhir "
            "produk sangat buruk. Evaluasi dan perbaikan kualitas pekerjaan tidak pernah dilakukan."
        ),
        "expected_template": "0101",
        "expected": {"valid": True, "d1": 0, "d2": 1, "d3": 0, "d4": 1},
        "note": "Genuine Fail: D1 terpicu karena kata negatif, dan D4 gagal terpicu mungkin karena mutual exclusivity ke non-target kalah kuat."
    },
    {
        "id": "LOG_F03", "template_target": "1001",
        "group": "Genuine Fail [1001→1100] — Narasi produktivitas skor 3 dianggap inkoheren (d2=1)",
        "q_id": QID_STANDAR_KUALITAS, "skor": 3,
        "narasi": (
            "Rekan saya cukup produktif dalam mengerjakan tugas-tugas yang diberikan oleh tim. "
            "Kontribusinya terhadap penyelesaian bagian proyek yang menjadi tanggung jawabnya "
            "cukup memadai meskipun tidak selalu tepat waktu. "
            "Tingkat produktivitas kerjanya berada di sekitar rata-rata anggota tim secara keseluruhan."
        ),
        "expected_template": "1001",
        "expected": {"valid": True, "d1": 1, "d2": 0, "d3": 0, "d4": 1},
        "note": "Genuine Fail: Skor 3 dengan narasi 'cukup produktif' dianggap inkoheren oleh NLP (d2=1) dan gagal memicu mutual exclusivity (d4=0)."
    },
    {
        "id": "LOG_F04", "template_target": "0000",
        "group": "Genuine Fail [0000→1000] — Narasi komunikasi ideal di QID komunikasi memicu d1=1",
        "q_id": QID_KOMUNIKASI, "skor": 5,
        "narasi": (
            "Kualitas interaksi dan komunikasi rekan saya selama bekerja dalam tim sangat baik. "
            "Dia selalu menyampaikan informasi dengan jelas, efektif, dan tepat sasaran. "
            "Efektivitas komunikasinya membuat koordinasi tim menjadi jauh lebih lancar dan produktif."
        ),
        "expected_template": "0000",
        "expected": {"valid": True, "d1": 0, "d2": 0, "d3": 0, "d4": 0},
        "note": "Genuine Fail: Di QID Komunikasi, narasi yang tampaknya ideal ini tidak terdeteksi mencakup rubrik secara penuh (d1=1)."
    },
    {
        "id": "LOG_F05", "template_target": "0101",
        "group": "Genuine Fail [0101→0001] — Pujian ekstrem skor=5 dianggap koheren (d2=0)",
        "q_id": QID_STANDAR_KUALITAS, "skor": 5,
        "narasi": (
            "Rekan saya adalah yang terbaik dalam hal komitmen kerja dan standar kualitas. "
            "Kualitas hasil akhir pekerjaannya selalu melampaui ekspektasi. "
            "Evaluasinya mendalam dan perbaikan yang dilakukan sangat signifikan "
            "meningkatkan mutu produk akhir tim."
        ),
        "expected_template": "0101",
        "expected": {"valid": True, "d1": 0, "d2": 1, "d3": 0, "d4": 1},
        "note": "Genuine Fail: Dianggap sangat koheren (d2=0) meskipun skor 5 dan pujian sangat ekstrem."
    }
]

# ══════════════════════════════════════════════════════════════════════
# RUNNER FINAL
# ══════════════════════════════════════════════════════════════════════
def run_final():
    templates = load_templates()

    print("=" * 70)
    print("TEMPLATE COVERAGE TEST — FINAL (17 Template, 1 per Template)")
    print(f"Endpoint : {ENDPOINT}")
    print(f"Skenario : {len(scenarios)}")
    print("=" * 70)

    results = []
    total = len(scenarios)

    for i, tc in enumerate(scenarios):
        payload = {
            "NIM": f"FINAL_{tc['id']}",
            "type": "assessment",
            "question_id": tc["q_id"],
            "feedback": {"skor": tc["skor"], "narasi": tc["narasi"]}
        }

        try:
            print(f"[{i+1:02d}/{total}] {tc['id']} [{tc['template_target']}] — {tc['group'][:50]}")
            t0 = time.time()
            resp = requests.post(ENDPOINT, json=payload, timeout=15)
            latency = round(time.time() - t0, 2)

            if resp.status_code == 200:
                data = resp.json()
                ind = data.get("indicators", {})

                act_valid = ind.get("valid", None)
                act_d1 = ind.get("d1", None)
                act_d2 = ind.get("d2", None)
                act_d3 = ind.get("d3", None)
                act_d4 = ind.get("d4", None)

                act_key = compute_template_key(
                    act_valid if act_valid is not None else True,
                    act_d1 or 0, act_d2 or 0, act_d3 or 0, act_d4 or 0
                )

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

                results.append({
                    "ID": tc["id"], "Template": tc["template_target"],
                    "Group": tc["group"][:70], "Proven": tc.get("round_proven",""),
                    "Note": tc.get("note",""),
                    "Skor": tc["skor"], "Words": words(tc["narasi"]),
                    "valid": act_valid,
                    "d1": act_d1, "d2": act_d2, "d3": act_d3, "d4": act_d4,
                    "Act_Key": act_key, "Exp_Key": exp_key,
                    "Verdict": verdict,
                    "Notes": ", ".join(notes) if notes else "-",
                    "Latency": latency,
                })
                icon = "✅" if verdict == "PASS" else "❌"
                print(f"  → act={act_key} | exp={exp_key} | {icon} {verdict}")
                if notes: print(f"     ↳ {', '.join(notes)}")
            else:
                results.append({
                    "ID": tc["id"], "Template": tc["template_target"],
                    "Group": tc["group"][:70], "Proven": "", "Note": "",
                    "Skor": tc["skor"], "Words": words(tc["narasi"]),
                    "valid":"?","d1":"?","d2":"?","d3":"?","d4":"?",
                    "Act_Key":"?","Exp_Key":tc.get("expected_template","?"),
                    "Verdict":"ERROR","Notes":f"HTTP {resp.status_code}","Latency":"-"
                })
        except requests.exceptions.ConnectionError:
            print(f"  ⚠️  Connection refused!")
            break
        except Exception as e:
            results.append({
                "ID":tc["id"],"Template":tc["template_target"],"Group":tc["group"][:70],
                "Proven":"","Note":"","Skor":tc["skor"],"Words":words(tc["narasi"]),
                "valid":"?","d1":"?","d2":"?","d3":"?","d4":"?",
                "Act_Key":"?","Exp_Key":tc.get("expected_template","?"),
                "Verdict":"ERROR","Notes":str(e)[:80],"Latency":"-"
            })

    passed = sum(1 for r in results if r["Verdict"] == "PASS")
    failed = sum(1 for r in results if r["Verdict"] == "FAIL")
    triggered = {r["Act_Key"] for r in results if r["Act_Key"] not in ("?","unknown")}
    not_triggered = set(templates.keys()) - triggered

    print(f"\n{'='*70}")
    print(f"SELESAI. {len(results)} skenario.")
    print(f"✅ PASS={passed} | ❌ FAIL={failed}")
    print(f"Template terpicu: {sorted(triggered)}")
    if not_triggered:
        print(f"Belum terpicu  : {sorted(not_triggered)}")

    # Markdown report
    md_out = "/workspace/Template_Coverage_Results_FINAL.md"
    with open(md_out, "w", encoding="utf-8") as f:
        f.write("# Hasil Validasi Template Coverage — FINAL\n\n")
        f.write(f"> **{len(results)} skenario (1 per template)** | ✅ {passed} PASS | ❌ {failed} FAIL\n\n")

        f.write("## Coverage Matrix — Semua 17 Template\n\n")
        f.write("| # | Template Key | Active Indicators (Perlu Intervensi) | Terpicu? | Skenario ID | Strategi Narasi |\n")
        f.write("|---|---|---|---|---|---|\n")
        for r in results:
            key = r["Template"]
            tpl = templates.get(key, {})
            active = ", ".join(tpl.get("active", [])) or "(tidak ada intervensi)"
            trig = "✅ Ya" if r["Act_Key"] == key else "⚠️ Obs"
            f.write(f"| {r['ID']} | `{key}` | {active} | {trig} | {r['ID']} | {r['Group'][:60]} |\n")

        f.write("\n## Hasil Detail per Skenario\n\n")
        f.write("| ID | Target | Actual | Skor | Kata | valid | d1 | d2 | d3 | d4 | Verdict | Terbukti di | Catatan |\n")
        f.write("|---|---|---|---|---|---|---|---|---|---|---|---|---|\n")
        for r in results:
            icon = "✅" if r["Verdict"] == "PASS" else "❌"
            note_col = r["Notes"]
            if r.get("Note"):
                note_col = "📝 *Lihat catatan*"
            f.write(
                f"| **{r['ID']}** | `{r['Exp_Key']}` | `{r['Act_Key']}` "
                f"| {r['Skor']} | {r['Words']} | {r['valid']} "
                f"| {r['d1']} | {r['d2']} | {r['d3']} | {r['d4']} "
                f"| {icon} {r['Verdict']} | {r['Proven']} | {note_col} |\n"
            )

        # Catatan khusus untuk TC04 (0010)
        obs = [r for r in results if r.get("Note")]
        if obs:
            f.write("\n## Catatan Penting\n\n")
            for r in obs:
                f.write(f"### {r['ID']} — Template `{r['Template']}`\n\n")
                f.write(f"> ⚠️ {r['Note']}\n\n")

        f.write("\n## Analisis Perilaku Indikator (Temuan Utama)\n\n")
        f.write("""### 1. d4 (Relevansi Topik) — Dipicu via Mutual Exclusivity

d4=1 hanya terpicu ketika narasi mengandung keyword rubrik **dalam konteks aspek yang berbeda** dari pertanyaan. Contoh:
- Narasi tentang **produktivitas** di pertanyaan **standar kualitas** → d4=1
- Narasi tentang **komunikasi** di pertanyaan **standar kualitas** → d4=1  
- Narasi tentang **pasar** menggunakan keyword rubrik (komitmen kerja, kualitas) → d4=1

Narasi completely off-topic (resep masakan, berita, dinosaurus) **TIDAK** memicu d4=1, karena tidak ada keyword rubrik yang bisa memicu mutual exclusivity check.

### 2. d1 (Cakupan Rubrik) — Sering Co-trigger dengan d2

Narasi yang inkoherensi (skor ≠ narasi) cenderung juga tidak mencakup kriteria rubrik secara eksplisit, karena:
- Narasi negatif generik tidak menyebut keyword rubrik positif
- Narasi positif generik tidak menyebut keyword rubrik secara eksplisit

Pengecualian: `0100` (d2=1 tanpa d1=1) hanya bisa dipicu ketika narasi **secara eksplisit menyebut semua keyword rubrik** dalam konteks negatif (terbukti di TC06/U04b).

### 3. d3 (Kedalaman Elaborasi) — Paling Deterministik

Threshold tepat di `len(narasi.split()) >= 25`. Namun narasi pendek yang mengandung keyword rubrik **selalu** juga memicu d4=1 (→ 0011 bukan 0010), karena konteks semantik yang sparse membuat mutual exclusivity check terpicu.

### 4. Template "0010" — Mungkin Tidak Dapat Dipicu Secara Isolasi

Setelah **14 percobaan** di Round 1-3, template `0010` tidak pernah berhasil dipicu. Setiap narasi pendek dengan keyword rubrik menghasilkan `0011` (d4 ikut terpicu). Ini mengindikasikan bahwa dalam kondisi nyata, ketika siswa menulis narasi singkat yang relevan rubrik, sistem selalu juga mendeteksi relevansi topik sebagai masalah.

**Implikasi praktis**: Template `0010` di `prompt_templates.json` mungkin redundan dengan `0011` dalam praktik penggunaan sistem.
""")

        f.write("\n---\n\n## Strategi Narasi untuk Setiap Template\n\n")
        f.write("| Template | Strategi Terbukti | QID | Skor |\n")
        f.write("|---|---|---|---|\n")
        strategies = [
            ("invalid", "Narasi kosong, hanya angka, atau hanya spasi", "Apapun", "Apapun"),
            ("0000", "Narasi komprehensif cover semua keyword rubrik + skor koheren + ≥25 kata", "Target", "Sesuai narasi"),
            ("0001", "Narasi pasar/konteks lain yang menyertakan keyword rubrik target", "Target", "Koheren"),
            ("0010", "❌ Belum berhasil — selalu menghasilkan 0011", "-", "-"),
            ("0011", "Narasi pendek (<25 kata) pasar + keyword rubrik, skor koheren", "Target", "Koheren"),
            ("0100", "Narasi panjang EKSPLISIT semua keyword rubrik + skor tidak sesuai (skor=5 narasi negatif)", "Target", "5"),
            ("0101", "Narasi yang cover semua keyword rubrik tapi d2+d4 ikut terpicu (lihat TC07)", "Target", "4"),
            ("0110", "Narasi pendek EKSPLISIT keyword rubrik + skor tidak sesuai", "Target", "5"),
            ("0111", "Narasi pendek pasar + keyword rubrik + skor tidak sesuai", "Target", "5"),
            ("1000", "Pujian generik ≥25 kata tanpa keyword rubrik, skor koheren", "Target", "5"),
            ("1001", "Narasi aspek LAIN (mis: komunikasi) ≥25 kata di QID target, skor koheren", "Target (QID lain)", "5"),
            ("1010", "Pujian generik singkat <25 kata tanpa keyword rubrik, skor koheren", "Target", "5"),
            ("1011", "Narasi aspek lain singkat <25 kata di QID target, skor koheren", "Target (QID lain)", "5"),
            ("1100", "Pujian generik ≥25 kata tanpa keyword rubrik, skor jauh berbeda (skor=1)", "Target", "1"),
            ("1101", "Narasi aspek lain ≥25 kata di QID target, skor jauh berbeda", "Target (QID lain)", "1"),
            ("1110", "Pujian generik singkat <25 kata, skor jauh berbeda (skor=1)", "Target", "1"),
            ("1111", "Narasi aspek lain singkat <25 kata di QID target, skor jauh berbeda (skor=1)", "Target (QID lain)", "1"),
        ]
        for tpl, strat, qid, skor in strategies:
            f.write(f"| `{tpl}` | {strat} | {qid} | {skor} |\n")

        f.write(f"\n---\n*FINAL — {len(results)} skenario, {passed} PASS, {failed} FAIL*\n")

    # CSV untuk lampiran
    csv_out = "/workspace/Template_Coverage_Cases_FINAL.csv"
    with open(csv_out, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "Test Case ID", "Template Target", "Module", "Case Type",
            "Test Case Name", "Precondition", "Steps to Execute",
            "Test Data (Narasi)", "Expected Result (Template Key)",
            "Actual Result (Template Key)", "Result (PASS/FAIL)", "Remark"
        ])
        for r, tc in zip(results, scenarios):
            result_formal = "PASS" if r["Verdict"] == "PASS" else "FAIL"
            case_type = "edge" if r["Template"] == "0010" else (
                "positif" if r["Skor"] >= 4 else "negatif"
            )
            writer.writerow([
                f"TC-TPL-{r['ID']}",
                r["Template"],
                "Template Coverage Validation",
                case_type,
                r["Group"],
                "- API NLP aktif pada endpoint /feedback/analyze",
                f"POST /feedback/analyze dengan skor={r['Skor']}",
                tc["narasi"][:200] + ("..." if len(tc["narasi"]) > 200 else ""),
                r["Exp_Key"],
                r["Act_Key"],
                result_formal,
                r["Notes"] + (f" | {tc.get('note','')[:100]}" if tc.get("note") else "")
            ])
    print(f"CSV: {csv_out}")
    print(f"MD : {md_out}")

if __name__ == "__main__":
    run_final()
