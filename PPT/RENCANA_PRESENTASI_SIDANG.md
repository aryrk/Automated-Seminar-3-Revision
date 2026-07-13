# RENCANA PRESENTASI SIDANG TUGAS AKHIR
## Pemanfaatan Digital Scaffolding Berbasis Rubrik untuk Mendukung Indikator Tekstual Feedback Literacy pada Project-Based Learning

> **Durasi target:** 25–28 menit (dari maksimum 30 menit)
> **Mode:** Tanpa demo APE (sistem tidak berubah dari Seminar 3)
> **Strategi utama:** Fokus ke riset, narasi skenario, dan analisis hasil — minimalkan bagian development

---

## ═══════════════════════════════════════════
## BAGIAN 0: AUDIT KESIAPAN DOKUMEN (Ceklis Pra-Sidang)
## ═══════════════════════════════════════════

### ✅ SUDAH DISELESAIKAN (Berdasarkan Analisis Dokumen 20260712)

| No | Saran Seminar 3 | Status | Bukti di Dokumen |
|:---|:---|:---|:---|
| 1 | Riset harus lebih bunyi dari development | ✅ Selesai | Seluruh SDLC, Use Case, Class Diagram → Lampiran 6 |
| 2 | Bab 4 jangan "Analisis Sistem Berjalan" — fokus ke scaffolding | ✅ Selesai | Bab IV kini = Problem Domain + Anotasi + Pemodelan Pipeline |
| 3 | Bahasa "Merancang Rubrik" → "Menyiapkan" | ✅ Selesai | I.4 pakai "Membangun dan mengkalibrasi konfigurasi optimal pipeline" |
| 4 | Model S-BERT posisikan sebagai black box tool | ✅ Selesai | II.1.6 + Lampiran 4 khusus teori NLP; teks utama hanya pakai outputnya |
| 5 | Kalibrasi harus dijelaskan prosesnya | ✅ Selesai | III.6.3 membahas grid search per indikator secara eksplisit |
| 6 | Pengujian APE + 4 indikator harus ada di laporan utama | ✅ Selesai | IV.4.1 Validasi Fungsionalitas ada; Lampiran 3 = test case lengkap |
| 7 | Eksperimen kenceng analisisnya | ✅ Selesai | Bab V = ±1500 baris berisi analisis mendalam F1, MANOVA, log interaksi |
| 8 | Peta RQ ke tahapan metodologi | ✅ Selesai | Tabel III.1 di awal Bab III |
| 9 | Diksi kesimpulan klaim terlalu kuat ("mampu") | ✅ Selesai | VII.1 pakai "memiliki indikasi menemukan konfigurasi optimal" |
| 10 | Data Leakage harus diakui | ✅ Selesai | V.4.4 + V.4.5 menjelaskan keterbatasan evaluasi & transfer threshold |
| 11 | Bab VI harus dampak riset, bukan fungsionalitas APE | ✅ Selesai | VI.2 = "Dampak Pedagogis Hasil Penelitian bagi Mitra" |
| 12 | Abstrak harus ada hasil numerik | ✅ Selesai | Abstrak mencantumkan p<0.05, rank-biserial 0.49, 4 indikator |
| 13 | Outcome kelompok stakeholder harus spesifik | ✅ Selesai | I.5 + VI.1 mendeskripsikan outcome mahasiswa vs. dosen secara terpisah |

### ⚠️ CATATAN MINOR (Tidak Perlu Revisi, Cukup Diingat)

| No | Item | Status | Catatan |
|:---|:---|:---|:---|
| 1 | Komentar reviewer (AR/M) di dokumen | ⚠️ Sisa | User akan hapus manual sebelum pengiriman |
| 2 | Daftar Pustaka | ⚠️ Kosong | User akan isi manual |
| 3 | AR1 (catatan halaman pertama) | ⚠️ Catatan dosen | Terlihat sudah direspons sebagian (sisi-sisi utama sudah ada) |

### 🔴 CELAH KRITIS YANG MASIH ADA (Perlu Waspada Saat Sidang)

| No | Celah | Risiko | Jurus Pertahanan |
|:---|:---|:---|:---|
| 1 | **n=56 di abstrak vs 30 di Cochran** | Penguji akan tanya inkonsistensi | n=30 adalah sampel eksperimen (Cochran), n=56 kemungkinan total submission narasi (multi-item per orang). Pastikan tahu angka persisnya. |
| 2 | **Data Leakage F1-score** | Dicecar kenapa F1 diklaim valid tapi data uji sama | Jawab dengan V.4.4: "sudah kami akui sebagai keterbatasan secara eksplisit" |
| 3 | **Threshold tidak divalidasi ulang di rubrik CATME** | Risiko "alat Anda belum teruji di rubrik yang dipakai" | Jawab dengan V.4.5: diakui, dan dijelaskan mitigasi melalui arsitektur frozen embedding |

---

## ═══════════════════════════════════════════
## BAGIAN 1: STRATEGI PRESENTASI SIDANG
## ═══════════════════════════════════════════

### Prinsip Presentasi Sidang vs Seminar 3

Seminar 3 terlalu lama karena:
1. Menjelaskan arsitektur teknis APE terlalu dalam
2. Urutan slide linier mengikuti bab (I → VII) sehingga penguji menunggu lama untuk sampai ke "inti riset"
3. Tidak cukup memperlihatkan contoh data nyata sebagai *anchor* argumen

**Strategi baru untuk sidang:**
- **"Problem-first, Evidence-second":** Mulai dari masalah konkret, langsung lompat ke *bukti* eksperimen
- **Angka dulu, penjelasan kemudian:** Setiap slide hasil harus punya 1 angka besar di tengah yang langsung membuat penguji fokus
- **Contoh nyata teks mahasiswa:** Perlihatkan actual text dari mahasiswa (anonimasi) sebagai ilustrasi — bukan diagram abstrak
- **Keterbatasan diajukan sendiri sebelum ditanya:** Ini adalah taktik kritis yang akan membuat penguji respek

---

## ═══════════════════════════════════════════
## BAGIAN 2: SUSUNAN SLIDE LENGKAP
## ═══════════════════════════════════════════

> Total target: **~25 slide + 3 slide cadangan**
> Durasi estimasi per slide: ~1 menit untuk slide isi, ~30 detik untuk slide transisi

---

### ── BABAK 1: KONTEKS & MASALAH (5 menit | Slide 1–5) ──

#### SLIDE 1 — COVER
- Judul penelitian
- Nama + NIM kedua mahasiswa
- Tanggal sidang
- Logo Polban
- *Tipe TA: Riset (Experiment Tools)*

---

#### SLIDE 2 — "APA MASALAHNYA?" (Latar Belakang)
**Judul:** *Mahasiswa Bisa Menilai, Tapi Kesulitan Mengartikulasikannya*

**Isi visual:**
- Kotak besar di kiri: Contoh riil narasi feedback buruk:
  > *"Skor: 4 | Narasi: Sudah sangat baik mengumpulkan data yang diminta"*
- Kotak besar di kanan: Apa yang **seharusnya** ditulis (mengacu kriteria rubrik spesifik)
- Di bawah: **Angka kunci** → `18,4% narasi selaras` (Setiawan, 2026a)
  - Self Assessment: 23,7% | Peer Assessment: 13,2%

**Script narasi (60 detik):**
> "Dalam lingkungan PjBL, self dan peer assessment adalah jendela bagi dosen untuk melihat dinamika kelompok yang tidak tampak dari produk akhir. Namun temuan Setiawan (2026a) pada 93 mahasiswa di Polban menunjukkan bahwa hanya 18,4% narasi feedback yang selaras dengan rubrik. Ini bukan masalah kemampuan menilai — mahasiswa sebenarnya *bisa* menilai. Masalahnya adalah mereka kesulitan *mengartikulasikannya* ke dalam bentuk narasi yang bermakna. Itulah yang kami sebut sebagai kesenjangan evaluative expression."

---

#### SLIDE 3 — "4 GEJALA YANG TERIDENTIFIKASI" (Problem Lebih Dalam)
**Judul:** *Empat Pola Tekstual yang Membatasi Kualitas Narasi Feedback*

**Isi visual (4 kotak dengan ikon + contoh singkat):**
| Indikator | Gejala | Contoh Teks Buruk |
|:---|:---|:---|
| 🔴 Cakupan Rubrik | Tidak menyebut kriteria rubrik sama sekali | *"Sudah sangat baik"* |
| 🟠 Koherensi Skor | Skor 5 tapi narasi bernada buruk (atau sebaliknya) | *Skor 4, narasi: "kurang aktif"* |
| 🟡 Kedalaman | Narasi < 25 kata = tidak ada ruang untuk elaborasi | *"Kerjasama oke"* |
| 🔵 Relevansi | Narasi membahas hal di luar aspek yang dinilai | *Ditanya soal komunikasi, jawab soal tugas* |

**Script narasi (45 detik):**
> "Dari analisis 9.180 data historis (Setiawan et al., 2026), empat pola ini muncul secara sistematis. Keempatnya dapat dideteksi dari teks — tidak perlu observasi manusia. Inilah yang kemudian kami jadikan sebagai empat indikator komputasional dalam pipeline penelitian ini."

---

#### SLIDE 4 — "MENGAPA INI MASALAH TEKNOLOGI?" (Gap Komputasional)
**Judul:** *Sistem yang Ada Masih Bersifat Sumatif*

**Isi visual:**
- Timeline sederhana: [Mahasiswa Menulis] → [Submit] → [Analisis NLP] → [Hasil]
- Tanda MERAH di tengah: ❌ *"Tidak ada intervensi SELAMA penulisan berlangsung"*
- Solusi yang diusulkan: [Mahasiswa Menulis] → [Analisis Real-time] → [Scaffolding muncul] → [Mahasiswa revisi] → [Submit]

**Script narasi (30 detik):**
> "Penelitian NLP sebelumnya (Rahimi, 2017; Omotehinwa, 2025) berhenti pada tahap analisis — hasilnya baru tersedia setelah mahasiswa selesai menulis. Kami mengisi kesenjangan ini dengan memberikan scaffolding **selama proses penulisan berlangsung**, real-time, berbasis analisis semantik otomatis."

---

#### SLIDE 5 — RESEARCH QUESTION
**Judul:** *Dua Pertanyaan Penelitian*

**Isi visual (dua kotak besar berdampingan):**

**RQ 1:**
> *Sejauh mana pipeline digital scaffolding, melalui kalibrasi model embedding dan aturan heuristik berbasis rubrik, dapat mencapai kesesuaian dengan ground truth dalam mendeteksi keempat indikator tekstual narasi feedback?*

↕ *Dijawab oleh:* Evaluasi F1-Score (Bab V.2.1)

**RQ 2:**
> *Sejauh mana intervensi scaffolding memengaruhi pemenuhan indikator tekstual, ditinjau dari perbedaan kelompok treatment vs kontrol dan pola interaksi mahasiswa?*

↕ *Dijawab oleh:* MANOVA + Log Analysis (Bab V.2.3–V.2.4)

---

### ── BABAK 2: METODOLOGI RINGKAS (5 menit | Slide 6–9) ──

#### SLIDE 6 — GAMBARAN SISTEM (Overview Pipeline)
**Judul:** *Arsitektur Pipeline: S-BERT + Rule-Based + Template Scaffolding*

**Isi visual (diagram alur horizontal, bukan UML teknis):**
```
[Teks Mahasiswa] 
       ↓
[Model Embedding: intfloat/multilingual-e5-large-instruct]  ← Black-box tool
       ↓
[Cosine Similarity vs. Rubrik Terdekomposisi]
       ↓
[Rule-Based Decision Table] → 16 kombinasi keputusan biner
       ↓
[Template Scaffolding → Ditampilkan ke mahasiswa]
```

**Script narasi (60 detik):**
> "Pipeline kami terdiri dari tiga komponen. Pertama, model sentence embedding yang mengubah teks narasi dan kriteria rubrik menjadi vektor semantik — ini kami perlakukan sebagai *black-box tool*, bukan objek riset. Kedua, perbandingan cosine similarity antara vektor narasi mahasiswa dengan vektor rubrik yang telah didekomposisi. Ketiga, decision table rule-based yang memetakan kombinasi hasil deteksi ke teks scaffolding yang sesuai. Hasilnya adalah prompt adaptif yang muncul secara real-time selama mahasiswa mengetik."

---

#### SLIDE 7 — KALIBRASI PIPELINE (Menjawab "Kenapa Angkanya Itu?")
**Judul:** *Kalibrasi: Mencari Threshold Optimal per Indikator*

**Isi visual:**
- Analogi: "Seperti mengkalibrasi timbangan sebelum dipakai"
- Tabel ringkas hasil kalibrasi:

| Indikator | Model Terpilih | Metode | Threshold (θ) | F1-Score |
|:---|:---|:---|:---|:---|
| Cakupan Rubrik | multilingual-e5-large | Semantic Chunking | 0.89 | 0.61 |
| Koherensi Skor | multilingual-e5-large | Mutual Exclusivity | 0.84 | 0.53 |
| Kedalaman | - | Rule-based (jumlah kata) | 25 kata | Deterministik |
| Relevansi Topik | multilingual-e5-large | Whole-text | 0.82 | 0.43 |

- **Catatan penting:** *"F1-score ini bersifat in-sample — diukur pada data kalibrasi yang sama (V.4.4). Kami akui sebagai keterbatasan metodologis."*

**Script narasi (45 detik):**
> "Proses kalibrasi kami lakukan melalui grid search pada 384 data anotasi manual. Threshold yang ditemukan bukan konstanta universal — ini adalah hasil empiris yang disesuaikan dengan pola diksi data historis JTK Polban. F1-Score yang kami laporkan merepresentasikan feasibility sistem pada fase kalibrasi, bukan klaim akurasi generalisasi."

---

#### SLIDE 8 — DESAIN EKSPERIMEN
**Judul:** *Randomized Posttest-Only Control Group Design (Desain 6)*

**Isi visual (diagram sederhana):**
```
Populasi 32 mahasiswa (MK Manajemen Kualitas Terpadu)
         ↓ Random Assignment (Cochran n=30)
    ┌────────────────┬────────────────┐
    │ Kelompok       │ Kelompok       │
    │ TREATMENT      │ KONTROL        │
    │ (n=15)         │ (n=15)         │
    │ Scaffolding ON │ Scaffolding OFF│
    └────────────────┴────────────────┘
         ↓ Posttest (skor 4 indikator per mahasiswa)
    Analisis MANOVA + Univariat
```

**Script narasi (45 detik):**
> "Kami memilih desain posttest-only untuk menghindari testing effect — jika kami ukur dulu di awal, mahasiswa akan sadar bahwa tulisannya sedang dianalisis, dan ini akan mengubah perilaku alami mereka. Dengan randomisasi, kedua kelompok diasumsikan setara sejak awal. Kedua kelompok mengisi self dan peer assessment di platform yang sama; hanya kelompok treatment yang mendapat scaffolding real-time."

---

#### SLIDE 9 — ALASAN MANOVA
**Judul:** *Mengapa MANOVA? (Bukan 4 T-Test Terpisah)*

**Isi visual:**
- Kotak kiri: ❌ 4 T-Test terpisah → Type I Error meningkat (0,05⁴)
- Kotak kanan: ✅ MANOVA → Menguji 4 indikator **simultan**, menjaga matriks kovarians
- **Pillai's Trace:** Dipilih karena paling *robust* terhadap pelanggaran Box's M (ukuran sampel seimbang)

---

### ── BABAK 3: SKENARIO & HASIL (12 menit | Slide 10–22) ──

> **INI ADALAH INTI PRESENTASI — Porsi terbesar waktu dan energi**

#### SLIDE 10 — TRANSISI: "APA YANG DITEMUKAN?"
**Judul:** *Dari Pipeline ke Eksperimen: Apa yang Terjadi?*

**Isi visual:** Kerangka 3-dimensi analisis (dari laporan V.14 dan V.17):
```
┌─────────────────────────────────────────────────────┐
│ DIMENSI 1: Kemampuan Deteksi Pipeline (RQ 1)        │
│ → Seberapa akurat sistem mendeteksi 4 indikator?    │
├─────────────────────────────────────────────────────┤
│ DIMENSI 2: Dampak Intervensi (RQ 2a)                │
│ → Apakah treatment vs kontrol berbeda secara        │
│   statistik? Seberapa besar effectnya?              │
├─────────────────────────────────────────────────────┤
│ DIMENSI 3: Pola Interaksi Mahasiswa (RQ 2b)         │
│ → Bagaimana mahasiswa *merespons* scaffolding?      │
└─────────────────────────────────────────────────────┘
```

---

#### SLIDE 11 — HASIL RQ1: KEMAMPUAN DETEKSI
**Judul:** *Kemampuan Deteksi Pipeline: Bervariasi Sesuai Kompleksitas Indikator*

**Isi visual — Tabel besar + analisis:**

| Indikator | F1 | Precision | Recall | Pola Error Utama |
|:---|:---|:---|:---|:---|
| Cakupan Rubrik | **0.61** | — | — | FP: teks panjang tapi generik; FN: narasi singkat tapi tepat |
| Koherensi Skor | **0.53** | — | — | Sulit deteksi inkoherensi implisit |
| Kedalaman | Deterministik | — | — | Tidak ada ambiguitas (rule-based murni) |
| Relevansi Topik | **0.43** | — | — | Inferensi implisit: analogi & metafora tidak terdeteksi |

**Script narasi (90 detik):**
> "Hasil ini menunjukkan bahwa kemampuan deteksi pipeline bervariasi sesuai kompleksitas kognitif yang dibutuhkan per indikator. Cakupan rubrik dan koherensi — dua indikator yang paling sering dideteksi butuh bantuan — memiliki F1 menengah. Kedalaman elaborasi bersifat deterministik karena berbasis jumlah kata, jadi tidak ada ambiguitas. Relevansi topik adalah yang tersulit — karena memerlukan *inferensi tingkat tinggi*. Ketika mahasiswa menulis tentang aspek yang sama tapi menggunakan analogi atau metafora, sistem kami kesulitan mengenali relevansinya. Ini bukan kelemahan model, ini keterbatasan struktural yang kami akui."

---

#### SLIDE 12 — SKENARIO KASUS: FALSE POSITIVE CAKUPAN RUBRIK
**Judul:** *Contoh: Mengapa Sistem Salah Mendeteksi "Sudah Terpenuhi"?*

**Isi visual:**

**FP Case (Sistem Prediksi PASS, Anotasi FAIL):**
> Narasi: *"Anggota tim ini sangat rajin, responsif, dan selalu berusaha memberikan yang terbaik dalam setiap situasi yang ada."*
>
> **Masalah:** Teks ini panjang dan positif, sehingga cosine similarity-nya tinggi terhadap deskripsi rubrik. Padahal tidak ada referensi eksplisit ke kriteria teknis rubrik.

**FN Case (Sistem Prediksi FAIL, Anotasi PASS):**
> Narasi: *"Kontribusi teknis pada modul backend sangat konkret."*
>
> **Masalah:** Kalimat ini sangat pendek tapi spesifik dan tepat sasaran. Sistem mendeteksinya sebagai tidak mencakup rubrik karena kalimatnya singkat.

**Script narasi (60 detik):**
> "Ini adalah dua kasus nyata dari 384 data anotasi kami. False Positive terjadi ketika teks panjang dan bernada positif — cosine similarity-nya tinggi karena pola leksikalnya mirip rubrik, meski tidak ada kriteria yang disebut eksplisit. False Negative terjadi pada narasi yang sangat singkat namun tepat sasaran. Temuan ini mengkonfirmasi bahwa model embedding cukup baik untuk *surface-level semantics*, tapi belum sensitif untuk mendeteksi *evaluative specificity*."

---

#### SLIDE 13 — SKENARIO KASUS: KOHERENSI SKOR (KASUS MENARIK)
**Judul:** *Fenomena Menarik: Skor Tinggi, Narasi Bernada Buruk*

**Isi visual:**

> **Kasus asli dari data eksperimen:**
> - Skor diberikan: **5 (Sangat Baik)**
> - Narasi: *"Masih kurang aktif dalam pengerjaan tugas, perlu lebih inisiatif lagi."*
>
> ↓ Sistem mendeteksi: *INCOHERENT* ✅ (Benar terdeteksi)
>
> Scaffolding muncul: *"Narasi Anda tampaknya mencerminkan evaluasi yang berbeda dari skor yang Anda berikan. Pertimbangkan untuk menyelaraskan justifikasi Anda."*

**Script narasi (60 detik):**
> "Kasus seperti ini adalah fenomena *leniency bias* — mahasiswa memberikan skor tinggi agar tidak menyakiti teman, tapi narasinya justru mengungkap evaluasi yang berbeda. Ini adalah gap evaluative expression yang paling nyata. Sistem kami berhasil mendeteksi inkonsistensi ini, dan memberikan scaffolding yang mengajak mahasiswa untuk merefleksikan ulang keselarasan penilaiannya."

---

#### SLIDE 14 — HASIL MANOVA (RQ2 — Bukti Utama)
**Judul:** *Hasil MANOVA: Intervensi Scaffolding Berpengaruh pada Peer Assessment*

**Isi visual — Tabel hasil + interpretasi:**

| Kelompok Assessment | Pillai's Trace | p-value | Interpretasi |
|:---|:---|:---|:---|
| Self Assessment | 0.21 | 0.21 (n.s.) | Tidak signifikan |
| **Peer Assessment** | **0.3047** | **0.0441** ✅ | **Signifikan (p<0.05)** |

> *Note: Pillai's Trace dipilih karena Box's M gagal (heterogenitas kovarians) — metrik ini paling robust.*

**Script narasi (60 detik):**
> "Pada pengujian multivariat, peer assessment menunjukkan perbedaan yang signifikan secara statistik antara kelompok treatment dan kontrol. Self assessment tidak. Ini konsisten dengan logika: mahasiswa dalam peer assessment menghadapi evaluasi pihak lain yang lebih kompleks secara kognitif, sehingga scaffolding lebih berpengaruh. Pada self assessment, mahasiswa mengevaluasi diri sendiri — ada kecenderungan pola penulisan yang lebih konsisten di kedua kelompok."

---

#### SLIDE 15 — HASIL UNIVARIAT (FOLLOW-UP MANOVA)
**Judul:** *Follow-up Univariat: Kedalaman Elaborasi Satu-satunya yang Konsisten Signifikan*

**Isi visual — Heatmap atau tabel warna:**

| Indikator | Self Assessment (p) | Peer Assessment (p) | Effect Size |
|:---|:---|:---|:---|
| Cakupan Rubrik | n.s. | n.s. | kecil |
| Koherensi Skor | n.s. | n.s. | kecil |
| **Kedalaman Elaborasi** | **0.005 ✅** | **0.0059 ✅** | **0.49 (sedang-besar)** |
| Relevansi Topik | n.s. | n.s. | kecil |

**Script narasi (60 detik):**
> "Follow-up univariat mengungkap bahwa dari keempat indikator, hanya kedalaman elaborasi yang signifikan secara konsisten — baik di self maupun peer assessment. Effect size 0.49 (rank-biserial correlation) tergolong sedang hingga besar untuk konteks eksperimen pedagogi. Ini bukan kebetulan — dan kita akan lihat mengapa ini terjadi di slide berikutnya."

---

#### SLIDE 16 — MENGAPA HANYA KEDALAMAN? (Log Analysis)
**Judul:** *Analisis Log: Mahasiswa Merespons Scaffolding dengan Menambah Teks*

**Isi visual:**

**Distribusi pola revisi mahasiswa setelah mendapat scaffolding:**
```
Insertion (Menambah kata)     ████████████████ 68%
Replacement (Menulis ulang)   ████             20%
Deletion (Menghapus)          ██               12%
```

**Script narasi (90 detik):**
> "Data log interaksi mengungkap pola yang sangat konsisten: mahasiswa merespons scaffolding hampir selalu dengan **menambahkan kata** ke narasi yang sudah ada, bukan menulis ulang. Ini adalah insight kunci. Kedalaman elaborasi diukur murni berdasarkan jumlah kata — maka operasi insertion secara langsung dan mekanis meningkatkan indikator ini. Sedangkan cakupan rubrik dan koherensi memerlukan *penyelarasan substantif* — mahasiswa harus memahami kriteria rubrik secara mendalam, lalu merestrukturisasi argumennya. Itu tidak bisa dicapai hanya dengan menambah kalimat. Ini menjelaskan mengapa scaffolding paling efektif pada kedalaman, dan kurang efektif pada indikator yang menuntut penalaran evaluatif lebih kompleks."

---

#### SLIDE 17 — CONTOH REVISI MAHASISWA (Nyata dari Data)
**Judul:** *Skenario Nyata: Mahasiswa Merespons Scaffolding*

**Isi visual (storyboard 3 langkah):**

**Step 1 — Narasi Awal (Scaffolding Muncul):**
> *"Kinerjanya bagus dan bisa diandalkan."*
> ↓ Sistem: "Kedalaman elaborasi belum terpenuhi (<25 kata). Pertimbangkan mendeskripsikan secara spesifik kontribusi teknis yang Anda amati."

**Step 2 — Revisi Mahasiswa:**
> *"Kinerjanya bagus dan bisa diandalkan. Selalu tepat waktu dalam mengumpulkan bagian modul yang ditugaskan, dan aktif memberikan solusi ketika ada bug."*
> ↓ Sistem: "Kedalaman elaborasi ✅ terpenuhi. Cakupan rubrik: perlu ditinjau."

**Step 3 — Narasi Final:**
> *"Kinerjanya bagus dan bisa diandalkan. Selalu tepat waktu dalam mengumpulkan bagian modul yang ditugaskan, dan aktif memberikan solusi ketika ada bug. Berdasarkan kriteria kerja sama dalam rubrik, kontribusinya selaras dengan ekspektasi level baik."*

**Script narasi (60 detik):**
> "Inilah yang terjadi di lapangan. Scaffolding berfungsi sebagai *pemicu kognitif* — bukan paksaan. Mahasiswa yang tadinya menulis dua kata, akhirnya merangkai tiga kalimat yang jauh lebih substantif. Ini adalah manifestasi nyata dari teori ZPD: mahasiswa tidak bisa sampai ke sana sendiri, tapi dengan bantuan yang tepat sasaran, mereka bisa."

---

#### SLIDE 18 — HASIL KUESIONER (Paradoks Utilitas)
**Judul:** *Mahasiswa Merasa Terbantu — Tapi Ada Efek Samping Kognitif*

**Isi visual (dua kolom berdampingan):**

**👍 Yang Paling Membantu:**
- "Arahan mengenai apa yang harus ditulis" (7 responden)
- "Mengingatkan kriteria yang terlewat" (mayoritas setuju)
- Rata-rata TAM: positif

**👎 Yang Paling Mengganggu:**
- "Arahan mengenai apa yang harus ditulis" (juga 6 responden! — paradoks)
- *Split-attention effect*: teks scaffolding berubah saat mahasiswa mengetik
- *Auto-scroll issue*: layar bergeser saat teks diperbarui

**Script narasi (45 detik):**
> "Temuan kuesioner mengungkap paradoks menarik: fitur yang paling membantu adalah sekaligus yang paling mengganggu. Komponen arahan dirasa relevan secara substantif, namun mekanisme penyajian real-time menimbulkan split-attention effect. Ini adalah temuan penting yang kami dokumentasikan sebagai arah pengembangan — dan sudah kami respons dengan modifikasi UI collapsible di Lampiran 7, meskipun belum sempat diuji dalam eksperimen ulang."

---

### ── BABAK 4: SINTESIS & PENUTUP (5 menit | Slide 19–22) ──

#### SLIDE 19 — KETERBATASAN (Diajukan Sendiri)
**Judul:** *Keterbatasan Penelitian — Transparansi Ilmiah*

**Isi visual (4 kotak dengan tanda ⚠️):**

| # | Keterbatasan | Implikasi |
|:---|:---|:---|
| 1 | **Data Leakage (V.4.4)** | F1-Score bersifat in-sample, belum divalidasi pada held-out test set |
| 2 | **Transfer Threshold (V.4.5)** | Threshold dikalibrasi di rubrik lama, dipakai di rubrik CATME tanpa validasi ulang |
| 3 | **Desain Posttest-Only (V.4.2)** | Tidak bisa ukur perubahan individu; random assignment diasumsikan setara |
| 4 | **Konteks Tunggal (V.4.1)** | Satu kelas, satu mata kuliah — generalisasi terbatas |

**Script narasi (45 detik):**
> "Kami sampaikan keterbatasan ini secara proaktif karena kejujuran ilmiah adalah bagian dari rigor penelitian. Keterbatasan ini bukan kegagalan — melainkan peta jalan bagi penelitian selanjutnya yang lebih kuat metodologinya."

---

#### SLIDE 20 — KESIMPULAN (Menjawab Kedua RQ)
**Judul:** *Kesimpulan: Jawaban atas Dua Research Question*

**RQ 1:**
> Pipeline berhasil dikalibrasi untuk mendeteksi 4 indikator dengan tingkat kesesuaian bervariasi (F1: 0.43–0.61 pada data kalibrasi). Performa lebih baik pada indikator yang bergantung pada *surface-level semantic matching*, menurun pada indikator yang membutuhkan inferensi evaluatif kompleks.

**RQ 2:**
> Intervensi scaffolding memberikan dampak signifikan pada peer assessment (Pillai's Trace=0.3047, p=0.0441, effect size sedang-besar pada kedalaman elaborasi). Dampak paling kuat pada indikator yang selaras dengan pola revisi alami mahasiswa (penambahan teks). Indikator yang memerlukan restrukturisasi evaluatif belum menunjukkan perbedaan signifikan.

---

#### SLIDE 21 — KONTRIBUSI & FUTURE WORK
**Judul:** *Tiga Kontribusi dan Arah Pengembangan*

**Kontribusi:**
1. Pipeline digital scaffolding berbasis rubrik untuk narasi feedback Bahasa Indonesia (NLP + rule-based hybrid)
2. Eksplorasi kelayakan 4 indikator tekstual sebagai dasar komputasional, sekaligus identifikasi batas performa
3. Bukti empiris awal dengan estimasi effect size sebagai dasar *power analysis* penelitian selanjutnya

**Future Work (dari Saran di VII.2):**
1. Fine-tuning model embedding untuk bahasa evaluatif Indonesia
2. Eksperimen dengan pre-test dan skala sampel lebih besar
3. Eksplorasi scaffolding reflektif/metakognitif
4. Modifikasi UI (collapsible) diuji ulang pada kelompok eksperimen baru
5. Replikasi di mata kuliah PjBL lain

---

#### SLIDE 22 — PENUTUP
**Judul:** *Sistem yang Mendengarkan Mahasiswa Saat Mereka Menulis*

**Isi visual:** Satu kalimat ringkasan besar + visual sederhana (mahasiswa mengetik dengan scaffolding muncul di samping layar)

> *"Penelitian ini menunjukkan bahwa teknologi NLP dapat bertindak bukan hanya sebagai detektor pasca-penulisan, melainkan sebagai pendamping kognitif real-time yang mendukung mahasiswa mengartikulasikan penilaian mereka lebih baik — dengan catatan bahwa efektivitasnya paling kuat pada indikator yang selaras dengan strategi revisi alami mahasiswa."*

**Ucapan terima kasih + slide pertanyaan terbuka**

---

### ── SLIDE CADANGAN (Hanya Keluarkan Jika Ditanya) ──

#### SLIDE CADANGAN A — Rumus Cosine Similarity
Detail matematika transformasi teks ke vektor dan perhitungan cosine similarity

#### SLIDE CADANGAN B — Tabel Perbandingan 6 Model Embedding
Lengkap dengan F1 per model per indikator (dari IV.3.3)

#### SLIDE CADANGAN C — Ilustrasi Dekomposisi Rubrik
Proses mengubah rubrik dosen menjadi unit-unit evaluatif yang dapat dibandingkan secara komputasional

---

## ═══════════════════════════════════════════
## BAGIAN 3: JADWAL WAKTU PRESENTASI
## ═══════════════════════════════════════════

| Babak | Slide | Waktu | Kumulatif |
|:---|:---|:---|:---|
| Pembukaan + Masalah | 1–5 | 5 menit | 0:00–5:00 |
| Metodologi Ringkas | 6–9 | 5 menit | 5:00–10:00 |
| Skenario & Hasil | 10–18 | 12 menit | 10:00–22:00 |
| Keterbatasan + Kesimpulan | 19–22 | 5 menit | 22:00–27:00 |
| Buffer | — | 3 menit | 27:00–30:00 |

---

## ═══════════════════════════════════════════
## BAGIAN 4: SKENARIO TANYA JAWAB (ANTISIPASI)
## ═══════════════════════════════════════════

### Q: "Ini TA bikin aplikasi atau riset?"
> "Fokus utama kami adalah riset eksperimental, Bapak/Ibu. APE adalah instrumen pengumpulan data — equivalent dengan kuesioner atau alat ukur. Seluruh dokumentasi teknis APE kami isolasi di Lampiran 6 dan 7. Yang kami presentasikan hari ini adalah proses kalibrasi NLP dan hasil uji dampak intervensi."

### Q: "F1-score 0.43 itu rendah. Ini berarti sistemnya tidak valid?"
> "F1-score relevansi topik memang terendah, karena indikator ini memerlukan inferensi kognitif tingkat tinggi yang belum dapat ditangkap oleh pendekatan cosine similarity konvensional. Ini kami dokumentasikan sebagai keterbatasan dan sebagai saran riset lanjutan. Meskipun demikian, sistem tetap digunakan dalam eksperimen karena bahkan dengan akurasi terbatas, scaffolding yang dipicu masih memberikan dampak signifikan pada kedalaman elaborasi."

### Q: "Mengapa Self Assessment tidak signifikan?"
> "Ini adalah temuan yang kami duga dari awal. Self assessment — mengevaluasi diri sendiri — memiliki kompleksitas kognitif yang berbeda dari peer assessment. Mahasiswa cenderung memiliki pola penulisan yang lebih konsisten dan lebih defensif saat menilai diri, sehingga scaffolding kurang memicu perubahan. Ini konsisten dengan temuan leniency bias pada self assessment di literatur."

### Q: "Kenapa threshold tidak divalidasi ulang di rubrik CATME?"
> "Ini adalah keterbatasan metodologis yang kami akui secara eksplisit di V.4.5. Keterbatasan sumber daya waktu mencegah kami melakukan re-kalibrasi. Kami memilih untuk tetap menggunakan threshold yang ada dengan memahami bahwa degradasi performa adalah risiko yang harus dikuantifikasi di penelitian berikutnya. Ini justru menjadi kontribusi: kami menyediakan estimasi awal yang dapat digunakan sebagai baseline."

### Q: "Sampelnya hanya 30 orang — apakah cukup untuk klaim yang valid?"
> "Penelitian ini kami posisikan sebagai pilot study, bukan large-scale study. Ukuran sampel 30 dipilih menggunakan formula Cochran untuk populasi terbatas (32 mahasiswa). Dalam konteks pilot study untuk estimasi effect size awal, sampel ini memadai. Effect size yang kami temukan (0.49) justru memberikan dasar power analysis untuk menentukan berapa sampel yang dibutuhkan dalam replikasi skala penuh."

### Q: "Kenapa tidak pakai pre-test?"
> "Pre-test akan menciptakan testing threat dan priming effect — mahasiswa menjadi sadar kriteria penilaian dan mengubah perilaku alami mereka. Desain posttest-only mengorbankan kemampuan mengukur perubahan individu, namun menjaga validitas internal melalui randomisasi. Trade-off ini kami jelaskan secara eksplisit di V.4.2."

---

## ═══════════════════════════════════════════
## BAGIAN 5: CATATAN TEKNIS UNTUK PEMBUAT SLIDE
## ═══════════════════════════════════════════

### Rekomendasi Desain Slide
1. **Warna utama:** Biru tua JTK + aksen oranye/hijau untuk highlight angka kunci
2. **Font:** Sans-serif (Inter/Roboto), heading min 28pt, body min 20pt
3. **Setiap slide harus punya 1 "Anchor Number"** — satu angka besar yang pertama dilihat mata
4. **Hindari bullet point panjang** — gunakan tabel, diagram, atau kotak kontras
5. **Gunakan warna merah untuk masalah, hijau untuk solusi/hasil positif**

### Prioritas Slide yang Harus Ada Visually Impactful
- Slide 3 (4 gejala tekstual) — tabel dengan warna merah/kuning
- Slide 11 (Hasil RQ1) — tabel F1 dengan highlight
- Slide 14 (Hasil MANOVA) — angka p=0.0441 dibuat besar dan bold
- Slide 16 (Log analysis) — diagram bar visual untuk insertion/replacement/deletion

### Hal yang Harus Hindari
- ❌ Jangan tampilkan Use Case Diagram atau Class Diagram
- ❌ Jangan jelaskan arsitektur teknis Vue.js/Laravel/FastAPI
- ❌ Jangan tampilkan seluruh tabel test case
- ❌ Jangan buat slide "Daftar Pustaka" — tidak diperlukan saat presentasi sidang

---
*Dokumen ini dibuat berdasarkan analisis komprehensif terhadap:*
- *`20260712_[REVISI] Laporan Tugas Akhir.md` (dokumen final)*
- *`20260629_Seminar 3.md` (PPT seminar sebelumnya)*
- *`Manual transcribe.md` dan `Transkrip_QnA_Terklarifikasi.md` (saran penguji)*
- *`10_REVISION_INSTRUCTIONS.md` (instruksi revisi atomik)*
- *`Cheat Sheet.md` (pertahanan sidang)*
