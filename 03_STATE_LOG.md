# 03_STATE_LOG — Log Dinamis Kumulatif

> Ini log kumulatif. JANGAN HAPUS entri lama. Tambahkan entri baru di PALING ATAS (paling baru di atas) supaya model berikutnya langsung baca yang terbaru dulu. Tujuan file ini: kalau proyek pindah dari satu model AI ke model lain, model baru harus bisa memahami PERSIS state, keputusan, dan asumsi yang sudah diambil tanpa perlu bertanya ulang ke User untuk hal yang sudah pernah dijawab.

---

## [2026-07-04 19:30] — Model: Claude Sonnet 4.6 (thinking)

**Fase dikerjakan**: Fase 1 — Membaca Materi Pendukung

**Yang dikerjakan**:
- Membaca semua 8 file Materi Tata Tulis, FTA checklist, Panduan TA Polban 2017, dan Template 2026.
- Membuat 4 file ringkasan di `04_SUMMARIES/`: S01 (FTA), S02 (Materi Tata Tulis gabungan), S03 (Panduan 2017), S04 (Template 2026 tipe Riset).

**Keputusan/asumsi baru diambil**:
- Template 2026 (`S04`) lebih prioritas dari Panduan 2017 (`S03`) untuk konten, karena lebih baru dan lebih spesifik untuk tipe TA Riset. Panduan 2017 tetap berlaku untuk tata tulis formal (margin, font, penomoran).
- 8 file Materi Tata Tulis diringkas dalam 1 file gabungan karena saling melengkapi.

**Temuan penting dari pembacaan materi**:
1. **Konflik format sitasi**: APA 7th (materi kuliah) vs Harvard-like Panduan 2017 vs "Harvard style" Template 2026. Perlu konfirmasi → OQ-002.
2. **Jumlah BAB**: Template 2026 tipe Riset mewajibkan 7 BAB (I–VII), Panduan 2017 hanya 5 BAB. Perlu verifikasi ke draft → OQ-003.
3. **Judul TA**: Panduan 2017 = 12–15 kata; Template 2026 = 12–20 kata. Patokan: Template 2026 (lebih baru).
4. **APE**: BAB IV khusus untuk Aplikasi Pendukung Eksperimen — elemen kritis yang tidak ada di Panduan 2017.
5. **Tujuan outcome-based**: "Membuat aplikasi" = salah; "Membuktikan..." = benar.
6. **Turnitin max 20%** (Template 2026).
7. **"dkk." bukan "et al."** untuk ≥3 penulis di teks (Panduan Polban).

**Kontradiksi/kendala ditemukan**:
- Panduan 2017 vs Template 2026 untuk beberapa hal — tabel perbandingan ada di `S04`.

**Yang harus dilanjutkan sesi berikutnya**:
- Fase 2: Baca PPT sidang MD hybrid + browser untuk slide gambar.
- Ajukan OQ-002 dan OQ-003 ke User.

---

## [2026-07-04 19:20] — Model: Claude Sonnet 4.6 (thinking)

**Fase dikerjakan**: Fase 0 — Orientasi

**Yang dikerjakan**:
- Membaca `01_INSTRUCTIONS.md` secara lengkap (149 baris).
- Scan seluruh folder project untuk memverifikasi keberadaan semua file sumber.
- Membaca file-file output yang sudah ada (00, 02, 03, 05, 06, 07, 08, 09) untuk cek apakah ada pekerjaan sebelumnya — semua file output kosong/template awal, konfirmasi proyek baru mulai dari nol.
- Update `00_INDEX.md`, `02_PROGRESS.md`, dan `03_STATE_LOG.md` (file ini).

**Temuan Verifikasi File**:
- ✅ Semua file yang disebutkan di `01_INSTRUCTIONS.md` ditemukan.
- ✅ `20260407_[REVISI] Laporan Tugas Akhir.md` ada, ukuran 740.888 bytes (besar — perlu dibaca bertahap di Fase 4).
- ✅ FTA: 1 file `.md`.
- ✅ Materi Tata Tulis: 8 file `.md` (instruksi menyebut "7 file" tapi faktanya ada 8 — lihat catatan di bawah).
- ✅ Panduan: 1 file `.md`.
- ✅ Template: 1 file `.md`.
- ✅ PPT: 2 file `.pdf` — ini format gambar/biner, TIDAK bisa dibaca langsung sebagai teks. Perlu penanganan khusus (lihat OQ-001).
- ✅ Transcribe: 2 file `.txt`.

**Catatan Discrepancy — Materi Tata Tulis**:
- Instruksi di `01_INSTRUCTIONS.md` menyebut "(7 file materi kuliah tata tulis)" tapi aktualnya ada **8 file**:
  1. `0_Intro Dunia Menulis.md`
  2. `1_Tata_Tulis_Laporan_Ilmiah_Pengantar_dan_Etika.md`
  3. `2_Kata_Kalimat_Paragraf_dan_Kalimat_Efektif.md`
  4. `3_Teknik_Sitasi_dan_Manajemen_Referensi.md`
  5. `02_Struktur dan Ketentuan Umum Lap Ilmiah.md`
  6. `03_Literature Review.md`
  7. `04_Methodologi.md`
  8. `20241004_Ilustrasi Penentuan Variabel Penelitian_BW.md`
- **Keputusan**: Semua 8 file akan dibaca dan diringkas di Fase 1. Discrepancy angka dianggap typo di instruksi, bukan masalah serius.

**Keputusan/asumsi baru diambil**:
- File-file output (05–09) yang sudah ada tapi kosong akan diisi dari awal (bukan dilanjutkan dari state sebelumnya karena tidak ada state sebelumnya).
- PPT dalam format PDF biner — untuk Fase 2, akan mencoba ekstraksi via browser subagent. Jika tidak berhasil, akan ditanyakan ke User cara akses kontennya.

**Kontradiksi/kendala ditemukan**:
- PPT format PDF tidak bisa dibaca langsung sebagai teks. Ini adalah kendala teknis yang perlu diklarifikasi (OQ-001).

**Yang harus dilanjutkan sesi berikutnya**:
- Tunggu konfirmasi User soal hasil Fase 0 dan pertanyaan OQ-001 (PPT PDF).
- Jika User setuju lanjut, mulai Fase 1: baca 8 file Materi Tata Tulis + FTA + Panduan + Template, buat ringkasan di `04_SUMMARIES/`.

---

## Asumsi & Keputusan Awal (baseline, berlaku sejak proyek dimulai)

- Skema confidence yang dipakai konsisten di seluruh file: **Tinggi / Sedang / Rendah** (definisi lengkap ada di `01_INSTRUCTIONS.md` bagian 1).
- Speaker transcript hanya diklasifikasi 2 kelas: `MAHASISWA` dan `DOSEN` (tidak dibedakan individu/peran pembimbing vs penguji), karena label speaker mentah berpotensi halusinasi.
- Roadmap internal (`07_ROADMAP_INTERNAL.md`) terstruktur PRIMARY per BAB, dengan index pattern global di bagian akhir file — bukan sebaliknya.
- Tidak ada kolom "penanggung jawab/siapa mengerjakan" di roadmap manapun — fokus murni pada kelengkapan pemetaan masalah.
- Estimasi effort di roadmap bersifat rentang wajar, bukan presisi tinggi, dan mengasumsikan sebagian pekerjaan akan dibantu AI di eksekusinya nanti.
- Agent dilarang menulis ulang/memperbaiki isi laporan TA — tugas murni memetakan.

---

(Entri sesi kerja baru ditambahkan di ATAS baris "Asumsi & Keputusan Awal")