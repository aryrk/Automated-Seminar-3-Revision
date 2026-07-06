STRUKTUR DATA PENELITIAN
(PEER ASSESSMENT, SELF ASSESSMENT, RUBIK)
LAMPIRAN TUGAS AKHIR
Lampiran ini disusun untuk memenuhi salah satu syarat menyelesaikan
Pendidikan Program Sarjana Terapan Program Studi Teknik Informatika di
Jurusan Teknik Komputer dan Informatika
Oleh:
Aryo Rakatama 221524003
Muhammad Rama Nurimani 221524021
PROGRAM SARJANA TERAPAN
PROGRAM STUDI TEKNIK INFORMATIKA
JURUSAN TEKNIK KOMPUTER DAN INFORMATIKA
POLITEKNIK NEGERI BANDUNG
2026

DAFTAR ISI
DAFTAR ISI ........................................................................................................... i
DAFTAR TABEL ................................................................................................. ii
BAB I STRUKTUR DATA PENELITIAN ......................................................... 3
I.1 Struktur Data Self dan Peer Assessment........................................................ 3
I.2 Struktur Data Rubrik ...................................................................................... 4
DAFTAR PUSTAKA ............................................................................................. 6
i

DAFTAR TABEL
Tabel I.1. Struktur Data Peer Assessment 3
Tabel I.2. Struktur Data Self Assessment 3
Tabel I.3. Struktur Data Rubrik 4
ii

BAB I
STRUKTUR DATA PENELITIAN

Lampiran ini memuat perancangan struktur data eksperimen secara rinci, termasuk
skema parameter model dan tabel penyimpanan instruksi scaffolding.

I.1 Struktur Data Self dan Peer Assessment
Bagian pertama dari data pengembangan adalah data self dan peer assessment yang
digunakan  untuk  mengevaluasi  arsitektur  pipeline  pada  tahap  pengembangan,
sebagaimana disajikan pada Tabel I.1 dan Tabel I.2.
Tabel I.1. Struktur Data Peer Assessment
| Atribut   |                                         |     | Deskripsi  |     |     | Tipe data  |
| --------- | --------------------------------------- | --- | ---------- | --- | --- | ---------- |
| class_id  | Kelas dari mahasiswa penulis feedback.  |     |            |     |     | String     |
Contoh: 1A
| assesor_id  | Nomor induk mahasiswa penulis feedback.  |     |     |     |     | String  |
| ----------- | ---------------------------------------- | --- | --- | --- | --- | ------- |
Contoh: 221524003
| group_id  | Kelompok mahasiswa dalam PjBL.  |     |     |     |     | Integer  |
| --------- | ------------------------------- | --- | --- | --- | --- | -------- |
Contoh: 1
No. urut rekan tim yang  Nomor  urut  siswa  penerima  feedback  pada  Integer
| akan dinilai  | kelompok PjBL.  |     |     |     |     |     |
| ------------- | --------------- | --- | --- | --- | --- | --- |
Contoh: 1
assessee_id  Nomor induk mahasiswa penerima feedback.  String
Contoh: 221524021
timepoint  Waktu pengambilan feedback. Berisi mid/end.  String
Contoh: mid
| indicator  | Pertanyaan kuantitatif pada feedback.  |           |              |       |        | String  |
| ---------- | -------------------------------------- | --------- | ------------ | ----- | ------ | ------- |
|            | Contoh:                                | Seberapa  | baik  rekan  | Anda  | dalam  |         |
mengumpulkan iklan lowongan kerja dari platform
yang ditugaskan? (Nilai dari skala 1-5)
| question  | Pertanyaan kualitatif pada feedback.  |           |           |         |           | String  |
| --------- | ------------------------------------- | --------- | --------- | ------- | --------- | ------- |
|           | Contoh:                               | Mengapa?  | (Berikan  | contoh  | spesifik  |         |
kontribusi rekan Anda dalam pengumpulan data.
Apakah rekan Anda menghadapi kesulitan dalam
mengumpulkan iklan)
peer_score  Skor kuantitatif yang diberikan penulis feedback.  Integer
Contoh: 5
peer_comment  Narasi kualitatif yang diberikan penulis feedback.  String
Contoh: Siswa sangat baik dalam mengumpulkan
|     | iklan  baik  | di  | platform  seperti  | linkedin  | dan  |     |
| --- | ------------ | --- | ------------------ | --------- | ---- | --- |
instagram

Tabel I.2. Struktur Data Self Assessment
3

|     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |

|           | Atribut  |                                         |     | Deskripsi  |     |     | Tipe data  |
| --------- | -------- | --------------------------------------- | --- | ---------- | --- | --- | ---------- |
| class_id  |          | Kelas dari mahasiswa penulis feedback.  |     |            |     |     | String     |
Contoh: 1A
| student_id  |     | Nomor induk mahasiswa penulis feedback.  |     |     |     |     | String  |
| ----------- | --- | ---------------------------------------- | --- | --- | --- | --- | ------- |
Contoh: 221524003
| group_id  |     | Kelompok mahasiswa dalam PjBL.  |     |     |     |     | Integer  |
| --------- | --- | ------------------------------- | --- | --- | --- | --- | -------- |
Contoh: 1
timepoint  Waktu pengambilan feedback. Berisi mid/end.  String
Contoh: mid
| indicator  |     | Pertanyaan kuantitatif pada feedback.  |           |              |       |        | String  |
| ---------- | --- | -------------------------------------- | --------- | ------------ | ----- | ------ | ------- |
|            |     | Contoh:                                | Seberapa  | baik  rekan  | Anda  | dalam  |         |
mengumpulkan iklan lowongan kerja dari platform
 yang ditugaskan? (Nilai dari skala 1-5)
| question  |     | Pertanyaan kualitatif pada feedback.  |           |           |         |           | String  |
| --------- | --- | ------------------------------------- | --------- | --------- | ------- | --------- | ------- |
|           |     | Contoh:                               | Mengapa?  | (Berikan  | contoh  | spesifik  |         |
kontribusi rekan Anda dalam pengumpulan data.
Apakah rekan Anda menghadapi kesulitan dalam
mengumpulkan iklan)
self_score  Skor kuantitatif yang diberikan penulis feedback.  Integer
Contoh: 5
self_comment  Narasi kualitatif yang diberikan penulis feedback.  String
Contoh: Siswa sangat baik dalam mengumpulkan
|     |     | iklan  baik  | di  | platform  seperti  | linkedin  | dan  |     |
| --- | --- | ------------ | --- | ------------------ | --------- | ---- | --- |
instagram

Data dikumpulkan secara resmi oleh pihak pengajar PjBL melalui google form
sebagai  instrumen  self  dan  peer  assessment  yang  telah  digunakan  sebagai
komponen pembelajaran.

I.2 Struktur Data Rubrik
Bagian kedua dari data pengembangan adalah data rubrik. Data ini mencakup aspek
penilaian, kriteria, serta hubungan dengan skor yang digunakan sebagai dasar
pertanyaan  kuantitatif  dan  kualitatif pada feedback  dengan  struktur  data  yang
disajikan pada Tabel I.3.
Tabel I.3. Struktur Data Rubrik
|        | Atribut  |                                          |     | Deskripsi  |     |     | Tipe data  |
| ------ | -------- | ---------------------------------------- | --- | ---------- | --- | --- | ---------- |
| Aspek  |          | Aspek spesifik dari kriteria penilaian.  |     |            |     |     | String     |
Contoh: Pengumpulan Iklan Lowongan Kerja
| Kriteria  |     | Deskripsi kriteria yang dinilai.  |     |     |     |     | String  |
| --------- | --- | --------------------------------- | --- | --- | --- | --- | ------- |
Contoh: Banyaknya iklan dan keragaman platform
yang digunakan.
Pertanyaan Kuantitatif  Pertanyaan kuantitatif pada feedback.  String
|     |     | Contoh:  | Seberapa  | baik  rekan  | Anda  | dalam  |     |
| --- | --- | -------- | --------- | ------------ | ----- | ------ | --- |
mengumpulkan iklan lowongan kerja dari platform
yang ditugaskan? (Nilai dari skala 1-5)

4

Atribut Deskripsi Tipe data
Pertanyaan Kualitatif Pertanyaan kualitatif pada feedback. String
Contoh: Mengapa? (Berikan contoh spesifik
kontribusi rekan Anda dalam pengumpulan data.
Apakah rekan Anda menghadapi kesulitan dalam
mengumpulkan iklan)
Skala 1 (Sangat Kurang) Deskripsi kriteria untuk feedback dengan skor String
bernilai 1.
Contoh: Mengumpulkan sedikit iklan.
Skala 3 (Cukup) Deskripsi kriteria untuk feedback dengan skor String
bernilai 3.
Contoh: Mengumpulkan cukup iklan.
Skala 5 (Sangat Baik) Deskripsi kriteria untuk feedback dengan skor String
bernilai 5.
Contoh: Mengumpulkan banyak dan relevan dari
platform yang bervariasi.
Penelitian ini menggunakan rubrik sebagai dasar evaluasi sistem digital scaffolding
pada tahap pengembangan, dengan tambahan tahap feature extraction sebagai
dekomposisi dari rubrik tersebut. Implementasi feature extraction didasarkan pada
beberapa pertimbangan berikut.
1. Memastikan setiap eksekusi pipeline menghasilkan output yang konsisten untuk
input yang sama sebagai upaya reproducibility
2. Literatur educational data mining Romero & Ventura (2020) menegaskan
bahwa preprocessing dan penataan data pendidikan sering kali menjadi
kontribusi penelitian yang berdiri sendiri, mengingat kompleksitas spesifik
domain, seperti struktur hierarkis dan longitudinal, dalam konteks pendidikan.
5

6
DAFTAR PUSTAKA
Romero, C., & Ventura, S. (2020). Educational data mining and learning analytics:
An updated survey. Wiley Interdisciplinary Reviews: Data Mining and
Knowledge Discovery, 10(3). https://doi.org/10.1002/widm.1355
