"""
run_template_coverage_tests_round3.py
═══════════════════════════════════════════════════════════════════════
ROUND 3 — Targeted test untuk 4 template yang belum terpicu:
  • 0010 — Hanya d3=1
  • 0101 — d2=1 + d4=1
  • 1001 — d1=1 + d4=1
  • 1011 — d1=1 + d3=1 + d4=1

INSIGHT KRITIS ROUND 1 & 2:
  • "0101" TERBUKTI terpicu di Round 1 oleh W02 original (skor=5, narasi
    terbaik+melampaui ekspektasi, cover semua keyword kualitas).
    Sistem mendeteksi d4=1 (narasi terlalu "sempurna" = off-topic?)
    dan d2=1 (skor=5 vs narasi terlalu positif = inkoherensi?).
    → Gunakan narasi W02 Round 1 persis dengan expected=0101.

  • "1001"/"1011": "sangat produktif" di QID kualitas terbukti memicu d4=1
    (lihat U15 Round2: skor=1 → 1111). Butuh skor yang KOHEREN dengan narasi.
    → Coba skor=5 untuk "sangat produktif" sehingga d2=0.

  • "0010": Narasi pendek selalu memunculkan d2+d4. Kemungkinan STRUKTURAL
    bahwa `0010` tidak bisa dipicu karena narasi pendek selalu ambigu
    secara semantik bagi model embedding. Tetap coba beberapa variasi.
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
        return {k: {} for k in [
            "invalid","0000","0001","0010","0011","0100","0101","0110","0111",
            "1000","1001","1010","1011","1100","1101","1110","1111"
        ]}

def compute_template_key(valid, d1, d2, d3, d4):
    if not valid:
        return "invalid"
    return f"{d1}{d2}{d3}{d4}"

# ══════════════════════════════════════════════════════════════════════
# SKENARIO ROUND 3 — Hanya 4 template tersisa + variasi agresif
# ══════════════════════════════════════════════════════════════════════
scenarios_r3 = [

    # ════════════════════════════════════════════════════════════════════
    # TARGET: "0101" — d2=1 + d4=1 (d1=0, d3=0)
    # ════════════════════════════════════════════════════════════════════
    # TERBUKTI di Round 1: W02 original menghasilkan 0101!
    # Narasi: "Rekan saya adalah yang terbaik dalam hal komitmen kerja dan
    # standar kualitas. Kualitas hasil akhir pekerjaannya selalu melampaui
    # ekspektasi. Evaluasinya mendalam dan perbaikan yang dilakukan sangat
    # signifikan meningkatkan mutu produk akhir tim." skor=5
    {
        "id": "T0101_A",
        "group": "Template[0101] — TERBUKTI Round1 W02: pujian ekstrem skor=5 cover semua rubrik",
        "desc": (
            "Narasi yang di Round 1 menghasilkan actual=0101: "
            "Sangat positif, cover semua keyword, skor=5 — "
            "sistem mungkin deteksi 'd4=1' (konteks melampaui ekspektasi = aspek lain?) "
            "dan 'd2=1' (terlalu superlatif untuk rubrik normal)"
        ),
        "q_id": QID_STANDAR_KUALITAS, "skor": 5,
        "narasi": (
            "Rekan saya adalah yang terbaik dalam hal komitmen kerja dan standar kualitas. "
            "Kualitas hasil akhir pekerjaannya selalu melampaui ekspektasi. "
            "Evaluasinya mendalam dan perbaikan yang dilakukan sangat signifikan "
            "meningkatkan mutu produk akhir tim."
        ),
        "expected_template": "0101",
        "expected": {"valid": True, "d1": 0, "d2": 1, "d3": 0, "d4": 1}
    },
    # Variasi B: Coba narasi A02 dari FINAL test yang terbukti menghasilkan 0101 di Round 1 (W02)
    {
        "id": "T0101_B",
        "group": "Template[0101] — A02 original: narasi skor=4 cover rubrik tapi d2+d4 di Round1",
        "desc": "A02 (dari run_nlp_tests_FINAL.py) di Round1 menghasilkan d2=1, d4=1 → expect 0101",
        "q_id": QID_STANDAR_KUALITAS, "skor": 4,
        "narasi": (
            "Sepanjang proyek, rekan saya menunjukkan dedikasi yang kuat terhadap standar kualitas pekerjaan. "
            "Komitmen kerjanya terlihat dari setiap iterasi revisi yang dilakukan dengan teliti. "
            "Meskipun belum sempurna, dia selalu mengevaluasi hasil kerjanya dan berupaya memperbaikinya "
            "sebelum dikumpulkan."
        ),
        "expected_template": "0101",
        "expected": {"valid": True, "d1": 0, "d2": 1, "d3": 0, "d4": 1}
    },
    # Variasi C: Narasi panjang melampaui ekspektasi + skor 3 (inkoherensi arah lain)
    {
        "id": "T0101_C",
        "group": "Template[0101] — Skor=3 narasi sangat positif cover semua rubrik (inkoherensi + relevance?)",
        "desc": "Skor=3 tapi narasi sangat positif dan mencakup semua rubrik → d2=1 + d4=1 (jika inkoherensi terdeteksi ke aspek lain)",
        "q_id": QID_STANDAR_KUALITAS, "skor": 3,
        "narasi": (
            "Komitmen kerja rekan saya sangat luar biasa sepanjang proyek. "
            "Standar kualitas yang dijaganya melampaui ekspektasi semua orang. "
            "Kualitas hasil akhir selalu sempurna. Evaluasi mendalam dan perbaikan kualitas "
            "pekerjaan dilakukan secara sistematis dan konsisten setiap saat."
        ),
        "expected_template": "0101",
        "expected": {"valid": True, "d1": 0, "d2": 1, "d3": 0, "d4": 1}
    },

    # ════════════════════════════════════════════════════════════════════
    # TARGET: "1001" — d1=1 + d4=1 (d2=0, d3=0)
    # ════════════════════════════════════════════════════════════════════
    # U15 Round 2 PASS: "Rekan saya sangat produktif dan selalu menyelesaikan
    # tugas tepat waktu." skor=1 → 1111 (d2=1 karena skor=1 inkoherensi)
    # → Untuk 1001 (d2=0), perlu skor yang KOHEREN: skor=5 untuk "sangat produktif"
    {
        "id": "T1001_A",
        "group": "Template[1001] — Narasi produktivitas singkat skor=5 (skor koheren dgn 'sangat produktif')",
        "desc": (
            "Narasi produktivitas di QID kualitas (d4=1 via mutual exclusivity) "
            "skor=5 = koheren dengan 'sangat produktif' (d2=0) "
            "+ ≥25 kata (d3=0) + tanpa keyword kualitas (d1=1)"
        ),
        "q_id": QID_STANDAR_KUALITAS, "skor": 5,
        "narasi": (
            "Rekan saya sangat produktif selama pengerjaan proyek. "
            "Dia selalu menyelesaikan tugas lebih cepat dari deadline dan "
            "mengambil tanggung jawab ekstra di luar yang diharapkan. "
            "Tingkat produktivitas dan kontribusi kerjanya jauh melampaui rata-rata anggota tim."
        ),
        "expected_template": "1001",
        "expected": {"valid": True, "d1": 1, "d2": 0, "d3": 0, "d4": 1}
    },
    # Variasi B: skor=4 untuk narasi "produktif"
    {
        "id": "T1001_B",
        "group": "Template[1001] — Narasi produktivitas panjang skor=4 (koheren, tanpa keyword kualitas)",
        "desc": "Skor=4 + narasi 'cukup produktif' panjang di QID kualitas → d1=1 + d4=1 + d2=0 + d3=0",
        "q_id": QID_STANDAR_KUALITAS, "skor": 4,
        "narasi": (
            "Rekan saya cukup produktif selama pengerjaan proyek berlangsung. "
            "Kontribusinya terhadap penyelesaian tugas cukup besar meskipun tidak selalu tepat waktu. "
            "Tingkat produktivitas kerjanya secara keseluruhan berada di atas rata-rata "
            "dan dia selalu berusaha menyelesaikan tanggung jawabnya dengan baik."
        ),
        "expected_template": "1001",
        "expected": {"valid": True, "d1": 1, "d2": 0, "d3": 0, "d4": 1}
    },
    # Variasi C: via QID_STANDAR_KUALITAS, narasi panjang ttg komunikasi (aspek lain), skor=5
    {
        "id": "T1001_C",
        "group": "Template[1001] — Narasi komunikasi panjang di QID kualitas skor=5",
        "desc": "Narasi komunikasi (aspek lain) di QID kualitas skor=5 koheren → d1=1 + d4=1 + d2=0 + d3=0",
        "q_id": QID_STANDAR_KUALITAS, "skor": 5,
        "narasi": (
            "Rekan saya memiliki kemampuan komunikasi yang sangat luar biasa. "
            "Dia selalu menyampaikan informasi dengan jelas dan efektif kepada seluruh anggota tim. "
            "Kemampuannya dalam berkomunikasi dan berkoordinasi sangat membantu kelancaran kerja tim "
            "dari awal hingga akhir proyek."
        ),
        "expected_template": "1001",
        "expected": {"valid": True, "d1": 1, "d2": 0, "d3": 0, "d4": 1}
    },

    # ════════════════════════════════════════════════════════════════════
    # TARGET: "1011" — d1=1 + d3=1 + d4=1 (d2=0)
    # ════════════════════════════════════════════════════════════════════
    # U15 Round2: "Rekan saya sangat produktif dan selalu menyelesaikan tugas tepat waktu."
    # skor=1 → 1111. Jika skor=4 (koheren dengan "sangat produktif") → mungkin d2=0?
    {
        "id": "T1011_A",
        "group": "Template[1011] — 'sangat produktif' singkat skor=4 (koheren, <25 kata, di QID kualitas)",
        "desc": (
            "Versi skor=4 dari U15: skor=4 koheren dengan 'sangat produktif' (d2=0) "
            "+ <25 kata (d3=1) + di QID kualitas (d4=1 via mutual exclusivity) "
            "+ tanpa keyword kualitas (d1=1)"
        ),
        "q_id": QID_STANDAR_KUALITAS, "skor": 4,
        "narasi": "Rekan saya sangat produktif dan selalu menyelesaikan tugas tepat waktu.",
        "expected_template": "1011",
        "expected": {"valid": True, "d1": 1, "d2": 0, "d3": 1, "d4": 1}
    },
    # Variasi B: skor=5 "sangat produktif"
    {
        "id": "T1011_B",
        "group": "Template[1011] — 'sangat produktif' singkat skor=5 (koheren, <25 kata, di QID kualitas)",
        "desc": "skor=5 untuk 'sangat produktif' singkat di QID kualitas → d2=0 + d3=1 + d4=1 + d1=1",
        "q_id": QID_STANDAR_KUALITAS, "skor": 5,
        "narasi": "Rekan saya sangat produktif dan selalu menyelesaikan tugas tepat waktu.",
        "expected_template": "1011",
        "expected": {"valid": True, "d1": 1, "d2": 0, "d3": 1, "d4": 1}
    },
    # Variasi C: narasi komunikasi singkat di QID kualitas skor=5
    {
        "id": "T1011_C",
        "group": "Template[1011] — komunikasi singkat skor=5 di QID kualitas",
        "desc": "Narasi komunikasi singkat (aspek lain) di QID kualitas skor=5 → d1=1 + d4=1 + d3=1 + d2=0",
        "q_id": QID_STANDAR_KUALITAS, "skor": 5,
        "narasi": "Rekan saya berkomunikasi dengan sangat baik dan efektif.",
        "expected_template": "1011",
        "expected": {"valid": True, "d1": 1, "d2": 0, "d3": 1, "d4": 1}
    },

    # ════════════════════════════════════════════════════════════════════
    # TARGET: "0010" — d3=1 saja (PALING SULIT — mungkin struktural tidak bisa)
    # ════════════════════════════════════════════════════════════════════
    # Semua percobaan sebelumnya menghasilkan 0111 (d2+d4 ikut).
    # Hipotesis: narasi pendek selalu membuat model tidak bisa isolasi d3 saja.
    # Coba beberapa variasi agresif:
    {
        "id": "T0010_A",
        "group": "Template[0010] — Skor=5, sangat positif eksplisit semua keyword, ~14 kata",
        "desc": (
            "Narasi sangat positif dengan semua keyword rubrik (d1=0) "
            "+ skor=5 (harapan d2=0) + <25 kata (d3=1) + on-topic (d4=0)"
        ),
        "q_id": QID_STANDAR_KUALITAS, "skor": 5,
        "narasi": (
            "Komitmen kerja sangat tinggi. Standar kualitas dijaga. "
            "Kualitas hasil akhir memuaskan. Evaluasi rutin dilakukan."
        ),
        "expected_template": "0010",
        "expected": {"valid": True, "d1": 0, "d2": 0, "d3": 1, "d4": 0}
    },
    {
        "id": "T0010_B",
        "group": "Template[0010] — Skor=4, narasi natural 20 kata dengan keyword rubrik",
        "desc": "Narasi 20 kata natural dengan keyword rubrik + skor=4 → harapan 0010",
        "q_id": QID_STANDAR_KUALITAS, "skor": 4,
        "narasi": (
            "Rekan saya menunjukkan komitmen kerja yang baik dan menjaga "
            "standar kualitas serta kualitas hasil akhir dengan evaluasi yang cukup rutin."
        ),
        "expected_template": "0010",
        "expected": {"valid": True, "d1": 0, "d2": 0, "d3": 1, "d4": 0}
    },
    {
        "id": "T0010_C",
        "group": "Template[0010] — Skor=5, kalimat panjang satu kalimat 22 kata semua keyword",
        "desc": "Satu kalimat panjang 22 kata eksplisit semua keyword + skor=5 → harapan 0010",
        "q_id": QID_STANDAR_KUALITAS, "skor": 5,
        "narasi": (
            "Rekan saya memiliki komitmen kerja tinggi, menjaga standar kualitas, "
            "menghasilkan kualitas hasil akhir yang baik, serta rutin melakukan evaluasi dan perbaikan."
        ),
        "expected_template": "0010",
        "expected": {"valid": True, "d1": 0, "d2": 0, "d3": 1, "d4": 0}
    },
    # Eksperimen: skor=3 dengan narasi netral medium
    {
        "id": "T0010_D",
        "group": "Template[0010] — Skor=3, narasi cukup, 20 kata, semua keyword rubrik",
        "desc": "Skor=3 + narasi 'cukup' (koherensi terjaga) + <25 kata → harapan 0010",
        "q_id": QID_STANDAR_KUALITAS, "skor": 3,
        "narasi": (
            "Komitmen kerja cukup baik. Standar kualitas cukup terpenuhi. "
            "Kualitas hasil akhir rata-rata. Evaluasi dilakukan sesekali."
        ),
        "expected_template": "0010",
        "expected": {"valid": True, "d1": 0, "d2": 0, "d3": 1, "d4": 0}
    },

    # ════════════════════════════════════════════════════════════════════
    # OBSERVASIONAL: Dokumen temuan di mana template ini terpicu secara
    # tidak sengaja oleh skenario dari FINAL test suite
    # (sebagai bukti bahwa template EXISTS dan bisa terpicu)
    # ════════════════════════════════════════════════════════════════════
    # Berdasarkan Round1+2, cek apakah ada pola yang belum kita coba untuk 0010:
    # Skenario K02 dari run_nlp_tests_FINAL.py (30 kata, skor=4) — tapi K02 adalah observasional
    # Skenario N01 (12 kata, skor=4) → expected d3=1 → PASS (dari FINAL test)
    # Pertanyaan: apa actual d1, d2, d4 dari N01?
    # Kita tidak tahu, tapi mari coba ulang skenario N01 here untuk lihat semua d-bit
    {
        "id": "T0010_N01",
        "group": "Template[0010?] — Replikasi N01 dari FINAL test (12 kata skor=4, expected d3=1 PASS)",
        "desc": (
            "N01 dari FINAL test PASS dengan expected={d3:1}. "
            "Pertanyaan: berapa actual d1, d2, d4? → lihat apakah ini 0010 atau sesuatu lain"
        ),
        "q_id": QID_STANDAR_KUALITAS, "skor": 4,
        "narasi": "Rekan saya bekerja dengan komitmen yang baik dan selalu menjaga standar kualitas.",
        "expected_template": "0010",  # Harapan — sebenarnya observasional
        "expected": {"valid": True, "d3": 1}  # Hanya assert d3=1 (terbukti dari FINAL)
    },
]

# ══════════════════════════════════════════════════════════════════════
# RUNNER ROUND 3
# ══════════════════════════════════════════════════════════════════════
def run_round3():
    templates = load_templates()

    print("=" * 70)
    print("TEMPLATE COVERAGE TEST — Round 3 (Targeted 4 Template Tersisa)")
    print(f"Endpoint : {ENDPOINT}")
    print(f"Skenario : {len(scenarios_r3)} total")
    print("=" * 70)

    results = []
    total = len(scenarios_r3)

    for i, tc in enumerate(scenarios_r3):
        payload = {
            "NIM": f"R3_{tc['id']}",
            "type": "assessment",
            "question_id": tc["q_id"],
            "feedback": {
                "skor": tc["skor"],
                "narasi": tc["narasi"]
            }
        }

        try:
            print(f"[{i+1:02d}/{total}] {tc['id']} ({words(tc['narasi'])} kata) — {tc['group'][:55]}")
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
                    act_d1 if act_d1 is not None else 0,
                    act_d2 if act_d2 is not None else 0,
                    act_d3 if act_d3 is not None else 0,
                    act_d4 if act_d4 is not None else 0,
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
                    "ID": tc["id"],
                    "Group": tc["group"][:65],
                    "Target": exp_key,
                    "Skor": tc["skor"],
                    "Words": words(tc["narasi"]),
                    "valid": act_valid,
                    "d1": act_d1, "d2": act_d2, "d3": act_d3, "d4": act_d4,
                    "Act_Key": act_key,
                    "Verdict": verdict,
                    "Notes": ", ".join(notes) if notes else "-",
                    "Latency": latency,
                })
                icon = "✅" if verdict == "PASS" else "❌"
                print(f"  → act={act_key} | exp={exp_key} | d1={act_d1} d2={act_d2} d3={act_d3} d4={act_d4} | {icon} {verdict}")
                if notes:
                    print(f"     ↳ {', '.join(notes)}")
            else:
                results.append({
                    "ID": tc["id"], "Group": tc["group"][:65], "Target": tc.get("expected_template","?"),
                    "Skor": tc["skor"], "Words": words(tc["narasi"]),
                    "valid":"?","d1":"?","d2":"?","d3":"?","d4":"?",
                    "Act_Key":"?","Verdict":"ERROR","Notes":f"HTTP {resp.status_code}","Latency":"-"
                })
        except requests.exceptions.ConnectionError:
            print(f"  ⚠️  Connection refused — aborting")
            break
        except Exception as e:
            results.append({
                "ID": tc["id"], "Group": tc["group"][:65], "Target": tc.get("expected_template","?"),
                "Skor": tc["skor"], "Words": words(tc["narasi"]),
                "valid":"?","d1":"?","d2":"?","d3":"?","d4":"?",
                "Act_Key":"?","Verdict":"ERROR","Notes":str(e)[:80],"Latency":"-"
            })

    passed = sum(1 for r in results if r["Verdict"] == "PASS")
    failed = sum(1 for r in results if r["Verdict"] == "FAIL")

    triggered = {r["Act_Key"] for r in results if r["Act_Key"] not in ("?","unknown")}

    print(f"\n{'='*70}")
    print(f"SELESAI. {len(results)} skenario — ✅ {passed} PASS | ❌ {failed} FAIL")
    print(f"Template baru terpicu di Round 3: {sorted(triggered)}")
    newly_pass = [r for r in results if r["Verdict"] == "PASS"]
    if newly_pass:
        for r in newly_pass:
            print(f"  ✅ {r['ID']} → template '{r['Act_Key']}' BERHASIL")

    # Tulis laporan
    md_out = "/workspace/Template_Coverage_Results_Round3.md"
    with open(md_out, "w", encoding="utf-8") as f:
        f.write("# Hasil Validasi Template Coverage — Round 3\n\n")
        f.write(f"> **{len(results)} skenario targeted** | ✅ {passed} PASS | ❌ {failed} FAIL\n\n")
        f.write("> **Target**: Template `0010`, `0101`, `1001`, `1011`\n\n")

        f.write("## Hasil Detail\n\n")
        f.write("| ID | Target | Actual | Skor | Kata | valid | d1 | d2 | d3 | d4 | Verdict | Catatan |\n")
        f.write("|---|---|---|---|---|---|---|---|---|---|---|---|\n")
        for r in results:
            icon = "✅" if r["Verdict"] == "PASS" else "❌"
            f.write(
                f"| **{r['ID']}** | `{r['Target']}` | `{r['Act_Key']}` "
                f"| {r['Skor']} | {r['Words']} | {r['valid']} "
                f"| {r['d1']} | {r['d2']} | {r['d3']} | {r['d4']} "
                f"| {icon} {r['Verdict']} | {r['Notes']} |\n"
            )

        f.write("\n## Analisis per Target Template\n\n")
        targets = ["0010", "0101", "1001", "1011"]
        for tgt in targets:
            tgt_results = [r for r in results if r["Target"] == tgt or tgt in r["ID"]]
            actual_keys = set(r["Act_Key"] for r in tgt_results)
            success = any(r["Verdict"] == "PASS" for r in tgt_results)
            f.write(f"### Template `{tgt}` {'✅ BERHASIL' if success else '❌ Belum terpicu'}\n\n")
            f.write(f"Actual yang diperoleh: {sorted(actual_keys)}\n\n")
            if not success:
                f.write(
                    f"> **Kemungkinan penyebab struktural**: "
                    f"Kombinasi indikator `{tgt}` mungkin sulit atau tidak dapat dipicu "
                    f"secara deterministik karena interdependensi antar indikator dalam "
                    f"arsitektur model embedding yang digunakan.\n\n"
                )

        f.write("\n## Kesimpulan Coverage\n\n")
        # Combined dari semua round
        all_triggered_combined = {
            "invalid","0000","0001","0011","0100","0110","0111",
            "1000","1010","1100","1101","1110","1111"
        } | triggered
        not_triggered = set(templates.keys()) - all_triggered_combined
        f.write(f"- **Berhasil dipicu (kumulatif Round 1-3)**: {sorted(all_triggered_combined)}\n")
        f.write(f"- **Belum terpicu**: {sorted(not_triggered)}\n\n")

        f.write("## Temuan Akhir: Pola Perilaku Indikator\n\n")
        f.write("""| Indikator | Kondisi Pemicu | Catatan |
|---|---|---|
| **d4=1** (Relevansi) | Narasi mengandung keyword rubrik dalam konteks aspek rubrik BERBEDA dari pertanyaan (mutual exclusivity). Narasi completely off-topic TIDAK memicu d4. | Terpicu reliabel via cross-aspect (produktivitas di QID kualitas, atau narasi pasar+keyword rubrik) |
| **d1=1** (Cakupan) | Narasi tidak menyebut kriteria rubrik target secara semantik | Sering co-trigger dengan d2; konteks off-topic menurunkan d1 similarity meski keyword hadir |
| **d2=1** (Koherensi) | Skor dan sentimen narasi tidak selaras | Lebih mudah trigger ketika skor jauh berbeda dari sentimen narasi (skor=1 vs narasi positif, atau skor=5 vs narasi negatif) |
| **d3=1** (Elaborasi) | Jumlah kata < 25 | Paling deterministik; threshold tepat di len(narasi.split()) >= 25 |
""")
        f.write(f"\n---\n*Round 3 — {len(results)} skenario targeted*\n")

    print(f"\nLaporan: {md_out}")

if __name__ == "__main__":
    run_round3()
