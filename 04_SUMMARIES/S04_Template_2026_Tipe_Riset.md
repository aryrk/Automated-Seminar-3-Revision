# RINGKASAN: Template Laporan TA JTK STr TI (RevMei2026) — Tipe Riset

> **Fungsi dalam pipeline**: Ini adalah template **aktual** yang harus diikuti untuk laporan TA tipe Riset (Experiment tools). **Ini lebih prioritas dari Panduan 2017** untuk aspek struktur konten dan tujuan tiap bab.

> **Tipe TA**: Riset (Experiment tools) — berarti TA ini membangun Aplikasi Pendukung Eksperimen (APE) sebagai instrumen, lalu melakukan eksperimen, lalu menganalisis dampak hasil.

---

## 1. Struktur Bab yang WAJIB (7 BAB + Lampiran)

| BAB | Judul | Isi Inti |
|---|---|---|
| I | Pendahuluan | Latar belakang, rumusan masalah, RQ & hipotesis, tujuan & manfaat, pemangku kepentingan, dukungan data, ruang lingkup & batasan, sistematika |
| II | Tinjauan Pustaka | Dasar teori, karya ilmiah sejenis |
| III | Metodologi Penelitian | Penjelasan penelitian, variabel penelitian, data penelitian, objek penelitian, perangkat pendukung, tahapan pelaksanaan penelitian |
| IV | Hasil Pengembangan APE | Analisis kebutuhan eksperimen, pengembangan aplikasi (SDLC) |
| V | Hasil dan Pembahasan Eksperimen | Hasil eksperimen, pembahasan |
| VI | Analisis Dampak Hasil Penelitian | Outcome ke mitra/pengguna, hasil uji adopsi |
| VII | Penutup | Kesimpulan, saran, rencana keberlanjutan & komersialisasi |

> **KRITIS**: Template ini punya **7 BAB** (plus BAB VI tentang dampak dan BAB VII penutup), berbeda dari struktur generik 5 bab di Panduan 2017. Jika draft laporan User masih 5 bab, ini adalah perbedaan struktural yang signifikan.

---

## 2. Detail Konten Per Bab yang Kritis

### BAB I — Pendahuluan

**Rumusan Masalah** (kriteria khusus untuk tipe Riset):
- Harus dalam bentuk **PERNYATAAN** (bukan pertanyaan)
- Harus berakar dari latar belakang (tidak boleh muncul tiba-tiba)
- Harus berisi: (1) pernyataan masalahnya apa, (2) dampak/urgensi masalah, (3) usulan solusi

**Research Question (RQ)**:
- Pertanyaan utama penelitian, dituliskan sebagai pernyataan
- Harus menggambarkan fokus penelitian
- Hipotesis: hanya diperlukan jika ada pembuktian dugaan awal (bukan untuk penelitian eksploratif)

**Tujuan Penelitian** — prinsip outcome-based:
- ❌ SALAH: "Membuat aplikasi..." atau "Melakukan analisis terhadap..."
- ✅ BENAR: "Membuktikan..." atau "Menentukan arsitektur/model... yang..." + pernyataan outcome (meningkatkan akurasi X%, mengurangi waktu Y%, dll)

**Dukungan Data**: Sumber data, link jika sekunder, nama organisasi jika primer — detail ada di III.3

### BAB II — Tinjauan Pustaka

**Dasar Teori**:
- Akhir setiap sub-bab: jelaskan teori ini akan digunakan untuk apa dalam TA
- Gambar/tabel dari sumber lain wajib ada sitasi

**Karya Ilmiah Sejenis**:
- Jangan dibahas per paper (menyebabkan pengulangan) — buat sub-bab berdasarkan **fokusan yang berkaitan dengan penelitian**
- Wajib ada tabel ringkasan (Tabel II.1 format)
- Di akhir: jelaskan state of the art, posisi TA terhadap karya sejenis (SWOT analysis atau analisis serupa)
- Urutan sub-bab (Dasar Teori vs Karya Ilmiah Sejenis) **bisa dibalik** tergantung asal inspirasi

### BAB III — Metodologi

**Variabel Penelitian**:
- Jelaskan variabel bebas dan terikat, hubungan antar variabel, alasan pemilihan
- Gambarkan kaitan antar variabel (contoh Gambar III.1)

**Data Penelitian** harus memenuhi: Relevan, Time Suitability (terbaru), Valid, Sufficient (jumlah cukup), Accurate

**Tahapan Pelaksanaan**:
- Dilengkapi luaran dan indikator capaian terukur di setiap tahapan
- Dilengkapi gambaran alur penelitian detail (jika menggunakan library/karya orang lain, beri keterangan berbeda)
- APE (Aplikasi Pendukung Eksperimen) dijelaskan rencananya di sini

### BAB IV — Hasil Pengembangan APE

**APE (Aplikasi Pendukung Eksperimen)** adalah instrumen yang dibangun untuk mendukung eksperimen — **BUKAN produk akhir**.

Komponen wajib:
1. Tujuan APE: mengapa perlu dibuat, fungsi utama, justifikasi kenapa existing tools tidak cukup
2. Arsitektur & Spesifikasi Teknis: teknologi, diagram arsitektur, alur kerja APE, modul kritis
3. Peran APE: apa yang diukur, kontrol variabel, instrumentasi
4. Tahapan Pengembangan sesuai SDLC: Analisis → Desain → Implementasi → Pengujian

**Pilot Testing APE**: Buktikan APE bekerja sebelum eksperimen dilakukan (uji fungsi 100% tanpa bug kritis)

### BAB V — Hasil dan Pembahasan Eksperimen

Komponen wajib:
1. Pengantar bab
2. Ringkasan metodologi eksperimen (refer ke Bab III)
3. Hasil eksperimen: tabel, grafik, screenshot — deskriptif saja (apa yang terjadi), jangan interpretasi dulu
4. Pembahasan/analisis: interpretasi data, korelasi dengan tujuan, faktor yang mempengaruhi, anomali
5. Pembahasan implementasi pada sistem/perangkat lunak
6. Perbandingan dengan penelitian terdahulu
7. Keterbatasan penelitian
8. Kesimpulan bab

### BAB VI — Analisis Dampak

- Membuktikan hasil penelitian bermanfaat untuk mitra/pengguna
- Berisi: pernyataan rekognisi mitra, hasil uji adopsi, feedback pengguna
- Pengujian: fungsionalitas, kinerja, usabilitas (jika ada), keterbatasan sistem

### BAB VII — Penutup

**Saran** yang baik: berbasis hasil penelitian, spesifik, terukur, realistis

**Rencana Keberlanjutan**: Pengembangan teknis, pemberdayaan, maintenance

**Komersialisasi**: Potensi, model bisnis, target pasar, strategi pemasaran, keunggulan kompetitif, perlindungan KI

---

## 3. Format Daftar Pustaka (Template 2026)

Template 2026 menggunakan **Harvard style** dengan contoh format per jenis sumber:

| Jenis | Format |
|---|---|
| Buku | Penulis. Tahun. *Judul Buku (italic)*. Edisi. Penerbit. Tempat. |
| Jurnal | Penulis. Tahun. Judul artikel. *Nama Jurnal (italic)*. Volume(Nomor): Hal. |
| Prosiding | Penulis. Tahun. Judul. *Nama Konferensi*. Tanggal, Kota, Negara. Hal. |
| Internet | Penulis. Tahun. *Judul (italic)*. URL. Tanggal akses. |

---

## 4. Perbedaan Kunci Template 2026 vs Panduan 2017

| Aspek | Panduan 2017 | Template 2026 |
|---|---|---|
| Jumlah BAB | 5 BAB | 7 BAB |
| Tipe TA | Generik | Spesifik Riset (Experiment tools) |
| Judul max | 12–15 kata | 12–20 kata |
| Abstrak max | 250 kata | 300 kata |
| BAB IV | Hasil & Pembahasan | Hasil Pengembangan APE |
| BAB V | Kesimpulan | Hasil & Pembahasan Eksperimen |
| BAB VI | — | Analisis Dampak |
| BAB VII | — | Penutup |
| RQ & Hipotesis | Tidak disebutkan | Wajib ada (sub-bab I.3) |
| Pemangku Kepentingan | Tidak ada | Sub-bab I.5 (wajib) |
| Dukungan Data | Tidak ada | Sub-bab I.6 (wajib) |

---

## 5. Catatan Teknis Penting

- Format nomor halaman: angka romawi kecil untuk bagian awal, angka Arab untuk konten
- Template menyebut jarak 1 spasi untuk abstrak dan daftar pustaka
- Biodata penulis: ada di halaman awal (sebelum abstrak)
- Turnitin: maksimal 20% (template menyebut 20%, FTA tidak spesifik)
- Kata pengantar: harus formal, dengan kontribusi spesifik setiap pihak; **DILARANG** mencantumkan nama yang tidak berkaitan dengan TA (pacar, dll)

---

*Sumber: `Template/2026 Template Laporan TA JTK-[R]-STr TI (RevMei2026).md`*
*Diringkas: 2026-07-04 — Fase 1*
