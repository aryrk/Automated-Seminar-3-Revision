# 05_TRANSCRIPT_CLEANED — Ringkasan Transcript Seminar 3

> **Fungsi dalam pipeline**: Sumber primer untuk Fase 4 (Analisis Komentar Dosen). Berisi semua poin substansial yang disampaikan dosen dalam sesi tanya jawab dan saran, sudah dibersihkan dari noise transcript.
>
> **Catatan kualitas transcript**: Transcript hasil speech-to-text mengandung banyak noise. Hanya poin yang bisa dipahami konteksnya secara reasonable yang disertakan.

---

## IDENTIFIKASI PEMBICARA

| Label | Identitas (Inferensi dari konteks) |
|---|---|
| SPEAKER_00 | Mahasiswa 1 — Aryo Rakatama (bagian pipeline & APE) |
| SPEAKER_01 | Ketua Sidang / Pembimbing — Irwan Setiawan, S.Si., M.T. |
| SPEAKER_02 | Mahasiswa 2 — Muhammad Rama Nurimani (metodologi & eksperimen) |
| SPEAKER_03 | Penguji — Yudi Widhiyasana, S.Si., M.T. (pertanyaan teknis mendalam) |
| SPEAKER_04 | Pembimbing 2 / Penguji — Jonner Hutahaean (komentar sesi saran) |
| SPEAKER_05 | Mahasiswa (bergantian dengan SP00 dan SP02) |
| SPEAKER_06 | Penguji — Ani Rahmani, S.Si., M.T. (komentar sesi saran) |

---

## BAGIAN 1: SESI PRESENTASI + TANYA JAWAB

### [T1] Jenis TA — Riset atau Desain?

**Penanya**: SP03 (~00:36:17)
> "Ini death copy apa riset sih? ... Nah kalau riset, maksudnya kan dibuangin saja tentang sesuatu yang sempet jadi apa yang dikajinnya juga?"

**Jawaban mahasiswa**: Dua fokus kajian: (1) menganalisa sejauh mana pipeline mendeteksi 4 indikator (F1-score), (2) perubahan pada subjek setelah mendapat scaffolding vs tidak (signifikansi pemenuhan indikator).

**Implikasi untuk laporan**: TA ini adalah **riset**, bukan desain. Dokumen harus mencerminkan paradigma riset secara konsisten.

---

### [T2] Alur teknis embedding — dari teks ke angka

**Penanya**: SP03 (~00:41:24)
> "Kita udah tau mau statistik mau apapun ceritanya kamu langsung ngomong F1 score... Bagaimana cara kamu melakukan deteksi?"

**Penanya**: SP01 (~00:53:29)
> "Buat saya, yang empat indikator itu kan menjadi vektor-vektor kan, ya gimana perjalanan dari veksi yang ada di rubrik hasil siswa tulis itu menjadi angka-angka itu loh?"

**Jawaban mahasiswa** (setelah diskusi panjang):
- Narasi → vektor menggunakan model embedding (multilingual-e5-large-instruct, pre-trained)
- Vektor narasi vs vektor rubrik → cosine similarity
- Cosine similarity → True/False menggunakan threshold (dicari via grid search)

**Catatan SP03** (~01:04:34):
> "kalau gitu menurut saya nggak perlu ada teori yang terlalu banyak... secara teori nggak perlu tingkat di langitnya kalau kita pakai model yang outputnya ya kita terima output"

**Catatan SP01** (~01:10:32):
> "Saya melihat beberapa bagian agak nyampur — bagaimana yang implementasi sendiri, bagaimana yang ambil dari mana, dari mana tulis sumbernya."

**Implikasi untuk laporan**:
1. Bab III: jelaskan bahwa model embedding adalah tools pre-trained (black box), bukan dikaji
2. Teori internal model embedding **tidak perlu** dibahas mendalam
3. Ada "pencampuran" antara yang dibuat sendiri vs yang diambil dari library — perlu diklarifikasi

---

### [T3] Batas scope kajian

**Klarifikasi mahasiswa** (~01:41:56):
> "Kami menggunakan model embedding sebatas black box, menggunakan outputnya, menggunakan fungsionalitasnya saja untuk dirangkaikan menjadi sebuah digital scaffolding. Jadi, urusan terkait model embedding dan teman-temannya itu di luar kajian."

**Respons SP01, SP03**: Oke, tapi batas ini harus dinyatakan **eksplisit** di dokumen.

**Implikasi untuk laporan**: Di awal Bab IV atau Bab III, perlu pernyataan eksplisit yang membatasi scope kajian — embedding model = tools (black box), bukan objek riset.

---

### [T4] Kalibrasi dan threshold — penjelasan perlu lebih jelas

**SP03** (~01:16:23) dan **SP01** (~01:21:50) mempertanyakan terminologi "kalibrasi" dan bagaimana threshold diperoleh.

**Catatan SP01**:
> "di setiap aspek yang diimplementasi sudah diuji supaya... sehingga kesimpulan kita juga valid"

**Implikasi untuk laporan**: Penjelasan proses kalibrasi dan cara mendapatkan threshold harus lebih jelas di dokumen — di mana dibahas (Bab III/IV), bagaimana interpretasinya.

---

### [T5] Pengujian APE — perlu lebih detail per indikator

**SP01** (~01:12:00): Mempertanyakan bagaimana APE diuji agar eksperimen valid.

**SP01** (~01:28:35):
> "cara yang berbeda itu mekanisme ini lebih datang ya kan beda karakter indikatornya kan beda sehingga pengujiannya beda... test case kan beda"

**Implikasi untuk laporan**: Pengujian APE harus dijelaskan per indikator (karena mekanisme berbeda), termasuk test case positif/negatif per indikator.

---

### [T6] Terminologi "intervensi" vs "rekomendasi"

**SP01** (~01:22:43):
> "Kapan seseorang harus dikasih intervensi? Intervensi apa saja yang dimungkinkan."

**SP03** (~01:32:58):
> "rekomendasi boleh tidak dilakukan tapi kalau intervensi biasanya sifatnya perintah yang namanya perintah harus dilakukan"

**SP01** (~01:27:05): Menjelaskan analogi scaffolding dalam konteks belajar — dari panduan penuh → bertahap dikurangi → mandiri.

**Implikasi untuk laporan**: Terminologi "intervensi" vs "rekomendasi" perlu diklarifikasi. Apakah scaffolding bersifat memaksa atau hanya saran? Bagaimana respon jika ada konflik antara skor dan narasi?

---

### [T7] Pencampuran konten antar bab

**SP01** (~01:10:56):
> "e teori ada di kontraiga [bab 3]... saya melihat beberapa bagian agak nyampur."

**SP01** (~01:59:00):
> "Pertama ini yang pertama pembahasannya di bab dua, kemudian ini dievaluasi pada bab empat."

**Implikasi untuk laporan**: Ada kemungkinan konten yang salah bab — teori di metodologi, atau hasil evaluasi di bab yang salah. Perlu audit penempatan konten per bab.

---

### [T8] Hal yang diakui mahasiswa belum dilakukan (dari presentasi sendiri)

**SP00/mahasiswa** (~00:25:12):
> "Untuk hal-hal yang belum kami lakukan, pertama kami sadar bahwa beberapa hal yang didokumen perlu ada diorganisir, kemudian untuk rekognisi mitra maupun rencana keberlanjutan itu belum kami tuahkan karena perlu diskusi lebih dalam maupun abstrak dan kata pengantar."

**Item yang belum dilakukan (menurut pengakuan mahasiswa sendiri)**:
1. Dokumen perlu diorganisir (struktur/isi)
2. Rekognisi mitra (Bab VI — Analisis Dampak)
3. Rencana keberlanjutan (Bab VII)
4. Abstrak dan kata pengantar belum rapi/selesai

---

## BAGIAN 2: SESI SARAN

### [S1] Saran SP04 — Fokus ke kajian, pindahkan (bukan hapus) konten APE

**SP04** (~00:01:13):
> "Kamu harusnya lebih banyak ekspos... Tentang misalnya, di sini baiknya kamu pakai, bukan kamu pakai, tapi kamu gunakan. dari sisi aplikasi contohnya tadi kalau kamu sekarang tidak mengkaji seperti yang ini dari sini tidak usah ada"

**SP04** (~00:02:28):
> "kalau oh lebih ke arah penelitian mungkin yang tadi misalnya dipindahkan bukan hilangkan mungkin bahasanya dipindahkan jadi lebih fokus ke kajian."

**Saran inti**: APE (development) terlalu mendominasi dokumen riset. Solusi: **pindahkan** (bukan hapus) konten development ke posisi yang tepat, perkuat bagian kajian riset.

---

### [S2] Saran SP01 — APE tetap ada tapi porsinya dikurangi

**SP01** (~00:03:38):
> "Tapi kalau dibuang juga, masa iya kalau dibuat dibuang ya?... tapi tidak sesederhana itu penelitiannya. Misalnya, tadi untuk keperluan apa, pakai model siapa, gitu kan? Itu di metodologi diceritakan, nanti di mana arsitekturnya, gambaran besar aja."

**SP01** (~00:07:50):
> "tadi neton neton yang kalau pakai ini sehingga jadi vektor jalannya begini, itu metode telah aku tuntuk riset? Eksperimen, analisis eksperimen itu kan cengceng gitu loh."

**Artinya**:
- APE tetap ada di dokumen, tapi **porsi dan posisinya** harus diubah
- Di Metodologi: sebutkan untuk keperluan apa, pakai model apa (singkat)
- Arsitektur APE: gambaran besar saja
- Yang diperkuat: eksperimen dan analisis eksperimen

---

### [S3] Saran SP01 — Bab VI isinya salah

**SP01** (~00:29:39):
> "Pautkan yang diharapkan dari pengguna. Pengguna apa? Pengguna APE. Itu simbolan, kalau mau riset itu simbolan riset."

**SP01** (~00:30:18):
> "kalau saya analisis dampak hasil penelitian itu kalau yang pernah wisat, ya penelitian-penelitian kita itu. sejauh mana bermanfaat lah buat JTK atau JPL JTK bukan ngobrol dan aplikasi... Masak ngobrol fungsionalnya"

**Artinya**:
- Isi Bab VI saat ini membahas fungsionalitas APE → **SALAH**
- Bab VI seharusnya: **sejauh mana hasil penelitian bermanfaat bagi JTK/pengguna aktual**
- Bukan tentang APE, tapi tentang **dampak temuan riset**

---

### [S4] Saran SP01 — Tujuan penelitian harus lebih outcome-focused

**SP01** (~00:34:28):
> "Tujuan penelitian itu salah satunya, biasanya mengevaluasi performa deteksi indikator. Itu mengevaluasi, nanti di metodologi dijelaskan bagaimana mengevaluasi performa pipeline itu."

**SP01** (~00:35:51):
> "jangan merancang aplikasinya. Tapi membangun. Ini skevolin, legita skevolinnya."

**Artinya**:
- Tujuan penelitian saat ini terlalu berfokus pada *proses* ("merancang pipeline") bukan *evaluasi/outcome* ("mengevaluasi performa")
- Perlu direvisi agar tujuan jelas mengarah ke evaluasi/pembuktian

---

### [S5] Saran SP01 — Metodologi harus lebih kencang, menjawab RQ

**SP01** (~00:52:45):
> "kencangin metodologi sangat."

**SP01** (~00:51:27):
> "Layak diimplementasikan, dari mana Anda sampai layak itu? oh belum dielaborasi secara detail. Nah, artinya kesimpulan ini diambil dari Eksperimen, eksperimen."

**Artinya**:
- Metodologi perlu diperkuat — penjelasan bagaimana setiap tahap menghasilkan jawaban untuk RQ
- Kesimpulan "layak diimplementasikan" harus bisa ditelusuri ke hasil eksperimen yang tertulis

---

### [S6] Saran SP01 — Teori tentang model embedding tidak perlu mendalam

**SP01** (~00:40:33):
> "Untuk itu, bikin aplikasi ini diperlukan. Ketika bikin aplikasi pakai model algoritme apa, algoritme apa, itu disebutkan saja, nggak bisa dibahas di teori. Kalau dibahas di teori, akibatnya apa? eh kamu tadi ditanyain juga kok apa lo lebih tanyamung dan tanyain"

**Artinya**: Membahas teori mendalam tentang model embedding di Bab II → menyebabkan pertanyaan teknis yang tidak bisa dijawab. Cukup sebut nama model dan alasan pemilihan di metodologi.

---

### [S7] Saran tentang Bab II — kaitan teori dengan penelitian

**SP01** (~00:51:44):
> "nah itu kalau di babua ada bagian yang nggak ngomong-ngomong pasal kita, kalau babua maksudnya realm saja."

**Artinya**: Bab II harus ada bagian yang mengaitkan setiap teori dengan konteks penelitian — tapi jangan sampai Bab II menjadi "realm saja" (hanya teori tanpa kaitannya ke penelitian).

---

### [S8] Saran tentang penulisan/dokumen secara umum

**SP01** (~00:45:10):
> "nggak tau lah saya ah nggak tau asal capek saya menerangkan di tata tulis juga udah bolak-balik datang... kalian lagi bagus menulisnya sekini mah"

**SP01** (~00:45:32): "baca panduan"

**SP01** (~00:46:14):
> "supaya orang menikmati laporan kita itu enak. jangan terlalu terpapar bahannya"

**Artinya**:
- Pembimbing pernah memberikan catatan tata tulis berulang kali — belum semua diterapkan
- Laporan terasa "berat" karena terlalu banyak detail teknis
- Perlu penyaringan konten agar laporan mudah dinikmati pembaca

---

### [S9] Saran SP00 / Mahasiswa sendiri — Laporan terpolusi development

**SP00** (~00:18:03):
> "gitu jadi eh terpolusi risetnya karena terlalu banyak developmentnya iya tapi emang kan kerjaannya banyak developmentnya iya nggak bisa dipungkuri juga iya cuma kalau niatnya mau melakukan riset gitu loh si risetnya harus lebih"

**SP01** (~00:18:06):
> "lebih menonjol daripada itu."

**Artinya**: Mahasiswa sendiri mengakui bahwa laporan "terpolusi" oleh development. Ini menjadi dasar untuk revisi struktural yang signifikan.

---

## RINGKASAN TEMA UTAMA

| No | Tema Utama | Asal | Prioritas |
|---|---|---|---|
| 1 | Laporan terlalu development-heavy — riset perlu lebih menonjol | SP01, SP03, SP04 | **KRITIS** |
| 2 | Batas kajian (scope) harus eksplisit di dokumen | SP01, SP03 | **KRITIS** |
| 3 | Tujuan penelitian perlu direvisi ke lebih outcome-focused | SP01 | **TINGGI** |
| 4 | Metodologi perlu diperkuat — bagaimana tiap tahap menjawab RQ | SP01 | **TINGGI** |
| 5 | Bab VI isinya salah — bukan fungsionalitas APE tapi dampak riset | SP01 | **TINGGI** |
| 6 | Penjelasan threshold/kalibrasi/grid search perlu lebih jelas | SP01, SP03 | **TINGGI** |
| 7 | Rekognisi mitra dan rencana keberlanjutan (Bab VI-VII) belum ada | SP00 (pengakuan) | **TINGGI** |
| 8 | Teori mendalam model embedding tidak perlu (di luar kajian) | SP01, SP03 | **SEDANG** |
| 9 | Terminologi "intervensi" vs "rekomendasi" perlu diklarifikasi | SP01, SP03 | **SEDANG** |
| 10 | Kesimpulan "layak diimplementasikan" perlu elaborasi dari eksperimen | SP01 | **SEDANG** |
| 11 | Abstrak dan kata pengantar belum selesai/rapi | SP00 (pengakuan) | **SEDANG** |
| 12 | Ada pencampuran konten antar bab — perlu audit penempatan | SP01 | **SEDANG** |
| 13 | Laporan terlalu "berat" — perlu penyaringan konten | SP01 | **SEDANG** |
| 14 | Pengujian APE perlu per indikator dengan test case berbeda | SP01 | **SEDANG** |

---

*Sumber: `Transcribe/Sesi Presentasi + Tanya Jawab.txt` (986 baris) dan `Transcribe/Sesi Saran.txt` (527 baris)*
*Dibuat: 2026-07-04 — Fase 3 (Pembersihan dan Ekstraksi Transcript)*
