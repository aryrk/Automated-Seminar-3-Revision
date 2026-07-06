<div align="center">

# LAMPIRAN 7 & 8
## PENGUJIAN FUNGSIONALITAS DAN USABILITAS APE SAPA

</div>

---

### Daftar Tabel
- Tabel III.3: Hasil pengujian yang didokumentasikan pada Lampiran 7 menunjukkan 41 dari 42 test case dinyatakan lolos, termasuk pengujian fungsionalitas part-of-speech tagging yang terbukti berhasil menyaring input teks acak atau tidak bermakna sebelum diproses oleh model.

---

### Daftar Gambar
(Tidak ada gambar pada lampiran ini)

---

Lampiran ini menyajikan dokumentasi lengkap mengenai hasil pengujian sistem yang dilakukan sebelum pelaksanaan eksperimen. Fokus pengujian mencakup verifikasi Functional Requirement (FR), analisis batasan sistem (Non-Functional Requirement), serta evaluasi usabilitas aplikasi oleh pengguna.

## L7.1 Hasil Evaluasi Kinerja dan Kegunaan Aplikasi Setelah Implementasi Hasil Penelitian

Subbab ini mengevaluasi kinerja dan kegunaan APE SAPA secara keseluruhan setelah pipeline digital scaffolding diterapkan, mencakup pengujian fungsionalitas pada subbab L7.1.1, serta pengujian usabilitas pada subbab L7.1.2.

### L7.1.1 Pengujian Fungsionalitas

Pengujian fungsionalitas terhadap APE SAPA telah dilaksanakan sebagaimana dipaparkan pada tahapan pengujian aplikasi utama. Pengujian dilakukan terhadap 42 test case yang mencakup pemeriksaan antarmuka, dekomposisi rubrik, dan seluruh indikator tekstual narasi yang didefinisikan pada Tabel III.3. Hasil pengujian yang didokumentasikan pada Lampiran 6 (Test Case) menunjukkan 41 dari 42 test case dinyatakan lolos, termasuk pengujian fungsionalitas part-of-speech tagging yang terbukti berhasil menyaring input teks acak atau tidak bermakna sebelum diproses oleh model.

Satu test case yang dinyatakan gagal terjadi pada pengujian indikator koherensi skor-narasi dengan skenario narasi yang kontradiktif, yaitu kondisi saat pengguna memasukkan skor tinggi namun menuliskan narasi yang merepresentasikan performa rendah. Sistem secara fungsional berhasil mendeteksi adanya inkonsistensi antara skor dan narasi, namun arsitektur model belum mampu mengekstraksi dan memprediksi angka skor aktual yang tersirat di dalam narasi

secara presisi. Secara keseluruhan, hasil pengujian menunjukkan bahwa fitur-fitur utama APE SAPA hasil integrasi digital scaffolding bekerja sesuai spesifikasi yang dirancang pada subbab L4.2, dengan satu limitasi spesifik pada kasus narasi yang bersentimen negatif.

### L7.1.2 Pengujian Usabilitas

Pengujian usabilitas dilakukan melalui kuesioner evaluasi pengguna terhadap kelompok treatment sebagaimana dipaparkan pada tahapan pengujian usabilitas, dengan data yang dihimpun dari 11 mahasiswa yang secara aktif menggunakan sistem digital scaffolding. Berdasarkan skala Likert 1-5, mahasiswa menilai bahwa intervensi digital scaffolding membantu mereka mengingat kriteria rubrik yang terlewat dengan skor rata-rata tertinggi, yaitu 4,00. Aspek kegunaan keseluruhan dan fleksibilitas interaksi mencatat rata-rata 3,91, diikuti oleh kejelasan instruksi dan kemudian memahami struktur penilaian dengan skor 3,82. Temuan ini menujukan perceived usefulness yang secara umum positif terhadap sistem.

Meskipun demikian, hasil kuesioner juga mengindikasikan adanya extraneous cognitive load. Pertanyaan yang mengukur perasaan pusing akibat informasi yang teralu padat dan gangguan konsentrasi saat mengetik masing-masing mencatat skor 3,45. Identifikasi komponen antarmuka menunjukkan pola yang ironis, yaitu komponen "arahan mengenai apa yang harus ditulis (Sentence Starter)" merupakan komponen yang paling banyak dipilih sebagai paling membantu, namun pada saat yang sama juga menjadi komponen yang paling banyak dikeluhkan sebagai pengganggu. Saran kualitatif dari subjek eksperimen juga menyoroti isu teknis berupa pergeseran layar otomatis yang membingungkan saat teks scaffolding diperbaharui selagi mahasiswa mengetik. Secara keseluruhan, pengujian usabilitas menunjukkan bahwa sistem dinilai bermanfaat secara fungsional oleh penggunanya, tetapi masih memerlukan penyempurnaan pada sisi pengalaman pengguna agar manfaat tersebut tidak disertai gangguan konsentrasi yang berarti.

### L7.1.3 Rekognisi Mitra atas Kebermanfaatan Hasil Penelitian
