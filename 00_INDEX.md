# 00_INDEX — Peta Proyek Pemetaan Revisi Laporan TA

> File ini adalah pintu masuk. Setiap sesi (termasuk saat ganti model AI), **baca file ini dulu**, lalu ikuti urutan baca yang tercantum di `01_INSTRUCTIONS.md`.

---

## 1. Konteks Singkat

Proyek ini untuk **memetakan dan mengeksekusi revisi** laporan TA berdasarkan:
- Catatan dosen di draft laporan (banyak yang ambigu/hanya dilingkari tanpa keterangan)
- Hasil transcribe sidang Seminar 3 (sesi presentasi+tanya jawab, dan sesi saran) — transcribe ini hasil AI, rawan noise & halusinasi
- Materi tata tulis, panduan TA, dan template sebagai landasan "cara yang benar"
- File Test Cases (TC.csv) — bukti pengujian fungsional APE per-indikator

**Status saat ini: Fase Pemetaan SELESAI. Siap masuk Fase Revisi.**

---

## 2. File Sumber (read-only, jangan diedit)

| Path | Keterangan |
|---|---|
| `Dokumen TA/Hasil Perbaikan 2026006 15.16/20260706_[REVISI] Laporan Tugas Akhir.md` | **FILE UTAMA REVISI** — Naskah laporan terkini yang sedang disunting. |
| `Test Cases/Test Cases - TC.csv` | 42 test case pengujian APE awal. |
| `Dokumen TA/Hasil Perbaikan 2026006 15.16/NLP_Validation_Cases.csv` | **Baru:** 107 Test Case komprehensif (pengganti TC awal). |
| `FTA/Lampiran-Form Pengecekan Tata Tulis...md` | Checklist formal aturan tata tulis wajib. |
| `Materi Tata Tulis/` (8 file) | Materi kuliah tata tulis — landasan menulis ilmiah. |
| `Panduan/PANDUAN_TA_POLBAN...md` | Panduan umum TA Polban, fokus jalur riset. |
| `Template/2026 Template Laporan TA JTK...md` | Template laporan (fleksibel, tidak wajib persis). |
| `Transcribe/` | Transcribe sesi Q&A dan Saran sidang (SUMBER #2). |

---

## 3. File Kerja Revisi

| Path | Keterangan |
|---|---|
| `Dokumen TA/Hasil Perbaikan 2026006 15.16/20260706_[REVISI] Laporan Tugas Akhir.md` | **FILE UTAMA REVISI** — hanya file ini yang diedit. |
| `Dokumen TA/Hasil Perbaikan 2026006 15.16/Lampiran/` | Folder untuk menampung konten yang dipindah dari bab utama ke Lampiran. |
| `Dokumen TA/Hasil Perbaikan 2026006 15.16/run_nlp_tests_FINAL.py` | Script validasi NLP 107 test cases. |

---

## 4. File Output Pipeline (Pemetaan)

| File | Fungsi | Status |
|---|---|---|
| `00_INDEX.md` | File ini — peta proyek | ✅ Aktif |
| `01_INSTRUCTIONS.md` | Instruksi pipeline (jangan diubah) | Read-only |
| `02_PROGRESS.md` | Checklist fase pipeline | ✅ Lengkap |
| `03_STATE_LOG.md` | Log dinamis keputusan dan temuan | ✅ Aktif |
| `04_SUMMARIES/` | Ringkasan per dokumen sumber | ✅ Selesai |
| `05_TRANSCRIPT_CLEANED.md` | Transcript bersih + 14 tema dosen | ✅ Selesai |
| `06_COMMENT_MAPPING.md` | Peta komentar dosen → Pattern-ID | ✅ Selesai |
| `07_ROADMAP_INTERNAL.md` | Roadmap revisi per BAB (14 item, level sedang) | ✅ Selesai |
| `08_ROADMAP_EXTERNAL.md` | Hal luar dokumen (6 item tindakan) | ✅ Selesai |
| `09_OPEN_QUESTIONS.md` | Open questions (OQ-002 masih belum dijawab) | ⚠️ OQ-002 pending |
| `10_REVISION_INSTRUCTIONS.md` | **Instruksi revisi atomik per-aksi** — panduan eksekusi | ✅ **BARU** |

---

## 5. Temuan Kunci dari Review

### Test Cases (TC.csv) — Konteks untuk Dosen
Test Cases sudah diorganisasi per indikator:
- **TC01-13**: Pengujian antarmuka (13 PASS)
- **TC14-17**: F1 — Cakupan Rubrik (4 PASS)
- **TC18-22**: F2 — Koherensi Skor-Narasi (4 PASS, **1 FAIL** di TC18 — sistem gagal ekstrak predicted score saat narasi bersentimen sangat negatif)
- **TC23-26**: F3 — Kedalaman Elaborasi (4 PASS)
- **TC27-30**: F4 — Relevansi Topik (4 PASS)
- **TC31-42**: Scaffolding aktif/tidak aktif & Dekomposisi rubrik (12 PASS)
- **Total: 41 PASS, 1 FAIL dari 42 test case**

**Implikasi**: Jawaban atas pertanyaan dosen SP01/SP03 soal "pengujian per indikator" sudah ADA di file ini. Perlu ditampilkan dengan lebih eksplisit di BAB IV.4.3 laporan (lihat instruksi D3 di `10_REVISION_INSTRUCTIONS.md`).

### Paper HOTS — Konteks Argumen Sidang
*The effect of scaffolding-based digital instructional media on HOTS* (Setyaningrum et al., 2024) disinggung penguji SP03 di sidang. Domain berbeda (matematika SMP vs. feedback literacy mahasiswa), tapi paradigma riset sama. Jawaban sudah disiapkan di `08_ROADMAP_EXTERNAL.md` item 6.

### Overclaim di Kesimpulan
- "Mampu mendeteksi" → harus diperhalus (F1=0,43 untuk Relevansi Topik)
- "Dapat digunakan sebagai dasar" → harus diperhalus (3 dari 4 indikator tidak signifikan)
- Instruksi spesifik ada di `10_REVISION_INSTRUCTIONS.md` G1 dan G2.

---

## 6. Urutan Onboarding untuk Model AI Baru

1. Baca `00_INDEX.md` ini.
2. Baca `02_PROGRESS.md` — cek fase mana yang sudah selesai.
3. Baca `09_OPEN_QUESTIONS.md` — cek apakah ada yang belum dijawab User.
4. **LANGSUNG KE `10_REVISION_INSTRUCTIONS.md`** untuk memulai revisi — ini adalah panduan atomik yang siap dieksekusi.
5. File yang diedit adalah `Dokumen TA/REVISI_DOKUMEN.md` (dan `REVISI_DOKUMEN_LAMPIRAN.md` untuk konten yang dipindah).

---

*Terakhir diupdate: 2026-07-06*