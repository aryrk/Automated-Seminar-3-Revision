<div align="center">

# LAMPIRAN 3
## STRUKTUR DATA PENELITIAN (PEER ASSESSMENT, SELF ASSESSMENT, RUBRIK)

</div>

---

### Daftar Tabel
- Tabel L3.1: Struktur Data Peer Assessment
- Tabel L3.2: Struktur Data Self Assessment
- Tabel L3.3: Tabel L3.3. Struktur Data Rubrik
- Tabel L3.4: sebagai dasar evaluasi sistem digital scaffolding pada tahap pengembangan, dengan tambahan tahap feature extraction yang dijelaskan secara konseptual pada landasan teori sebagai dekomposisi dari rubrik tersebut. Implementasi feature extraction didasarkan pada beberapa pertimbangan berikut.

---

Lampiran ini memuat perancangan struktur data eksperimen secara rinci, termasuk skema parameter model dan tabel penyimpanan instruksi scaffolding.

## L3.1 Struktur Data Self dan Peer Assessment

Tabel L3.1. Struktur Data Peer Assessment

Atribut  |  Deskripsi  |  Tipe data
class_id  |  Kelas dari mahasiswa penulis feedback. Contoh: 1A  |  String
assesor_id  |  Nomor induk mahasiswa penulis feedback. Contoh: 221524003  |  String
group_id  |  Kelompok mahasiswa dalam PjBL. Contoh: 1  |  Integer
No. urut rekan tim yang akan dinilai  |  Nomor urut siswa penerima feedback pada kelompok PjBL. Contoh: 1  |  Integer
assessee_id  |  Nomor induk mahasiswa penerima feedback. Contoh: 221524021  |  String
timepoint  |  Waktu pengambilan feedback. Berisi mid/end. Contoh: mid  |  String
indicator  |  Pertanyaan kuantitatif pada feedback. Contoh: Seberapa baik rekan Anda dalam mengumpulkan iklan lowongan kerja dari platform yang ditugaskan? (Nilai dari skala 1-5)  |  String
question  |  Pertanyaan kualitatif pada feedback. Contoh: Mengapa? (Berikan contoh spesifik kontribusi rekan Anda dalam pengumpulan data. Apakah rekan Anda menghadapi kesulitan dalam mengumpulkan iklan)  |  String
peer_score  |  Skor kuantitatif yang diberikan penulis feedback. Contoh: 5  |  Integer
peer_comment  |  Narasi kualitatif yang diberikan penulis feedback. Contoh: Siswa sangat baik dalam mengumpulkan iklan baik di platform seperti linkedin dan instagram  |  String

Tabel L3.2. Struktur Data Self Assessment

Atribut  |  Deskripsi  |  Tipe data
class_id  |  Kelas dari mahasiswa penulis feedback. Contoh: 1A  |  String
student_id  |  Nomor induk mahasiswa penulis feedback. Contoh: 221524003  |  String
group_id  |  Kelompok mahasiswa dalam PjBL. Contoh: 1  |  Integer
timepoint  |  Waktu pengambilan feedback. Berisi mid/end. Contoh: mid  |  String
indicator  |  Pertanyaan kuantitatif pada feedback.  |  String

Atribut  |  Deskripsi  |  Tipe data
Contoh: Seberapa baik rekan Anda dalam mengumpulkan iklan lowongan kerja dari platform yang ditugaskan? (Nilai dari skala 1-5)
question  |  Pertanyaan kualitatif pada feedback. Contoh: Mengapa? (Berikan contoh spesifik kontribusi rekan Anda dalam pengumpulan data. Apakah rekan Anda menghadapi kesulitan dalam mengumpulkan iklan)  |  String
self_score  |  Skor kuantitatif yang diberikan penulis feedback. Contoh: 5  |  Integer
self_comment  |  Narasi kualitatif yang diberikan penulis feedback. Contoh: Siswa sangat baik dalam mengumpulkan iklan baik di platform seperti linkedin dan instagram  |  String

Data dikumpulkan secara resmi oleh pihak pengajar PjBL melalui google form sebagai instrumen self dan peer assessment yang telah digunakan sebagai komponen pembelajaran.
## L3.2 Struktur Data Rubrik


Bagian kedua dari data pengembangan adalah data rubrik. Data ini mencakup aspek penilaian, kriteria, serta hubungan dengan skor yang digunakan sebagai dasar pertanyaan kuantitatif dan kualitatif pada feedback dengan struktur data yang disajikan pada Tabel L3.3.

Tabel L3.3. Struktur Data Rubrik

Atribut  |  Deskripsi  |  Tipe data
Aspek  |  Aspek spesifik dari kriteria penilaian.  |  String
Contoh: Pengumpulan Iklan Lowongan Kerja
Kriteria  |  Deskripsi kriteria yang dinilai.  |  String
Contoh: Banyaknya iklan dan keragaman platform
yang digunakan.
Pertanyaan Kuantitatif  |  Pertanyaan kuantitatif pada feedback.  |  String
Contoh: Seberapa baik rekan Anda dalam
mengumpulkan iklan lowongan kerja dari platform
yang ditugaskan? (Nilai dari skala 1-5)
Pertanyaan Kualitatif  |  Pertanyaan kualitatif pada feedback.  |  String
Contoh: Mengapa? (Berikan contoh spesifik
kontribusi rekan Anda dalam pengumpulan data.
Apakah rekan Anda menghadapi kesulitan dalam
mengumpulkan iklan)
Skala 1 (Sangat Kurang)  |  Deskripsi kriteria untuk feedback dengan skor  |  String
bernilai 1.
Contoh: Mengumpulkan sedikit iklan.

Atribut  |  Deskripsi  |  Tipe data
Skala 3 (Cukup)  |  Deskripsi kriteria untuk feedback dengan skor  |  String
bernilai 3.
Contoh: Mengumpulkan cukup iklan.
Skala 5 (Sangat Baik)  |  Deskripsi kriteria untuk feedback dengan skor  |  String
bernilai 5.
Contoh: Mengumpulkan banyak dan relevan dari
platform yang bervariasi.

Penelitian ini menggunakan rubrik pada Tabel L3.4 sebagai dasar evaluasi sistem digital scaffolding pada tahap pengembangan, dengan tambahan tahap feature extraction yang dijelaskan secara konseptual pada landasan teori sebagai dekomposisi dari rubrik tersebut. Implementasi feature extraction didasarkan pada beberapa pertimbangan berikut.

1. Memastikan setiap eksekusi pipeline menghasilkan output yang konsisten untuk input yang sama sebagai upaya reproducibility
2. Literatur educational data mining Romero & Ventura (2020) menegaskan bahwa preprocessing dan penataan data pendidikan sering kali menjadi kontribusi penelitian yang berdiri sendiri, mengingat kompleksitas spesifik domain, seperti struktur hierarkis dan longitudinal, dalam konteks pendidikan.
