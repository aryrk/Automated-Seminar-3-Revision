<div align="center">

# LAMPIRAN 1
## TEORI NATURAL LANGUAGE PROCESSING DAN ARSITEKTUR TRANSFORMER

</div>

---

### Daftar Tabel
- Tabel L1.1: Selain itu pendekatan ini memiliki batasan interpretabilitas. Representasi vektor yang dihasilkan bersifat laten dan tidak memiliki padanan linguistik eksplisit pada tingkat token atau frasa (Senel et al., 2018) . Keterbatasan ini diterima sebagai konsekuensi yang dapat dikelola selama sinyal yang dihasilkan menunjukkan keselarasan yang memadai dengan penilaian manusia pada data anotasi yang dievaluasi melalui F1 score pada subbab L1.1.4.

### Daftar Gambar
- Gambar L1.1: menggambarkan arsitektur SBERT untuk mencari kesamaan dalam dua teks.
- Gambar L1.2: Gambar L1.2. Perbandingan Arsitektur Cross-Encoder dan Bi-Encoder
- Gambar L1.3: merepresentasikan bagaimana teks feedback dalam penelitian ini disimpan ke dalam representasi vektor menggunakan model embedding, narasi "Iklan yang dikumpulkan amir dikumpulkan dari platform yang beragam" dilakukan transformasi menjadi nilai matematis berupa koordinat dalam ruang vektor.
- Gambar L1.4: Cosine Similarity dalam Ruang Vektor
- Gambar L1.5: Gambar L1.5. Representasi Pipeline Penelitian
- Gambar L1.6: Precision mengukur ketepatan model dalam memprediksi kelas positif dari keseluruhan hasil yang diprediksi positif oleh sistem, sedangkan Recall mengukur banyaknya kelas positif yang dideteksi dengan benar, dibandingkan dengan total data positif yang sebenarnya.

### Daftar Rumus
- Rumus L1.1
- Rumus L1.2
- Rumus L1.3
- Rumus L1.4

---

Lampiran ini menyajikan landasan teoretis komprehensif mengenai Natural Language Processing (NLP) dan arsitektur Transformer yang menjadi dasar komputasional dalam penelitian ini. Penjabaran pada lampiran ini difokuskan pada aspek teknis model semantic embedding dan metrik evaluasi kinerja.

## L1.1 Natural Language Processing (NLP) dan Arsitektur Transformer

Natural Language Processing (NLP) merupakan bagian dari ilmu komputer dan artificial intelligence yang memungkinkan mesin untuk memahami, memproses, dan menganalisis bahasa alami yang digunakan manusia (C. Manning & Hinrich, 1999), seperti yang dikutip oleh Torfi et al. (2021). Salah satu komponennya adalah Natural Language Understanding (NLU), yang berfokus pada ekstraksi makna semantik dari teks sehingga sistem dapat menginterpretasikan isi bahasa secara komputasional.

Perkembangan NLP didorong oleh penggunaan arsitektur transformer, yang memungkinkan pembentukan representasi teks yang bersifat kontekstual melalui mekanisme pemrosesan yang mempertimbangkan hubungan antar elemen dalam satu sequence secara menyeluruh (Vaswani et al., 2023). Arsitektur ini menjadi dasar bagi berbagai model embedding pre-trained, termasuk Sentence Bidirectional Encoder Representations from Transformers (SBERT) (Reimers & Gurevych, 2019), yang memanfaatkan pemahaman dua arah untuk menangkap hubungan kontekstual dalam teks, dengan Gambar L1.1 menggambarkan arsitektur SBERT untuk mencari kesamaan dalam dua teks.

Gambar L1.1. Arsitektur SBERT untuk Regresi Teks

Dalam implementasinya, terdapat dua pendekatan utama dalam pemrosesan pasangan teks, yaitu cross-encoder dan bi-encoder. Pendekatan cross-encoder memproses dua teks secara bersamaan sehingga memungkinkan interaksi penuh antar token, namun memiliki kompleksitas komputasi yang tinggi. Sebaliknya, pendekatan bi-encoder merepresentasikan setiap teks secara independen ke dalam ruang vektor yang sama, sehingga memungkinkan perbandingan semantik dilakukan secara efisien tanpa memerlukan pemrosesan ulang terhadap seluruh pasangan teks (Devlin et al., 2019; T. Gao et al., 2022; Reimers & Gurevych, 2019). Ilustrasi kedua pendekatan tersebut disajikan pada Gambar L1.2.

Gambar L1.2. Perbandingan Arsitektur Cross-Encoder dan Bi-Encoder

Dalam penelitian ini, komponen NLU diimplementasikan melalui pendekatan berbasis bi-encoder untuk menghasilkan representasi vektor (embedding) dari teks yang lebih lanjut dijelaskan pada subbab L1.1.1. Representasi ini kemudian digunakan untuk mengukur hubungan semantik antar teks secara kuantitatif. Kesamaan semantik antara dua teks diukur menggunakan cosine similarity yang dijelaskan lebih lanjut pada subbab L1.1.2. Pendekatan ini memungkinkan sistem membandingkan makna narasi feedback mahasiswa dengan deskripsi kriteria secara matematis terlepas dari perbedaan kata yang digunakan, dan hasilnya digunakan sebagai dasar dalam mekanisme pengambilan keputusan berbasis semantik dalam sistem.

### L1.1.1 Vector Embedding Sebagai Representasi

Fondasi komputasional dari pemahaman semantik teks adalah representasi teks sebagai vektor dalam ruang berdimensi. Secara formal, diberikan suatu teks sebuah fungsi representasi memetakan teks tersebut ke dalam ruang vektor berdimensi , dipetakan pada rumus L1.1.

$$f_w(x) \to \mathbb{R}^d$$
 (L1.1)

Prinsip dasar dari pendekatan ini berakar pada distributional hypothesis bahwa kata-kata atau ekspresi yang muncul dalam konteks serupa cenderung memiliki makna yang berdekatan (Harris, 1954). Gambar L1.3 merepresentasikan bagaimana teks feedback dalam penelitian ini disimpan ke dalam representasi vektor menggunakan model embedding, narasi "Iklan yang dikumpulkan amir dikumpulkan dari platform yang beragam" dilakukan transformasi menjadi nilai matematis berupa koordinat dalam ruang vektor.

Gambar L1.3. Rerpesentasi Ruang Vektor

Transformasi ini mengubah data teks yang bersifat simbolik menjadi data numerik. Tanpa representasi vektor, sistem tidak dapat melakukan operasi matematika untuk mengukur semantic similarity. Dengan representasi ini, narasi "Sangat baik" dan "Luar biasa" akan memiliki posisi koordinat yang berdekatan dalam ruang vektor.

Sebagai contoh, jika terdapat narasi ="Rekan saya berhasil mengumpulkan 30 data iklan", maka fungsi akan melakukan transformasi teks menjadi sebuah koordinat vektor seperti [0.12, −0.45, … ,0.89] dengan panjang dimensi = 1024 tergantung pada arsitektur model yang digunakan.

Representasi vektor memiliki properti yang tidak dimiliki representasi simbolik di mana ia memungkinkan pengukuran gradasi kemiripan antar konsep. Dalam penelitian ini, fungsi representasi diimplementasikan menggunakan model pretrained yang parameternya tidak dimodifikasi selama pipeline beroperasi. Konsekuensinya, kualitas representasi semantik yang dihasilkan termasuk sejauh mana vektor narasi mahasiswa dapat dibandingkan secara bermakna dengan vektor deskripsi rubrik sepenuhnya bergantung pada geometri ruang yang telah dikodekan model selama pre-training. Pilihan model pre-trained yang tepat menjadi keputusan desain kritis dalam penelitian ini dan dibahas lebih lanjut pada Bab IV.

### L1.1.2 Cosine Similiarity untuk Eksploitasi Ruang Vektor

Cosine similarity mengukur sudut antara dua vektor tanpa bergantung pada magnitudonya (C. D. Manning et al., 2009). Formula cosine similarity disajikan pada rumus L1.2.

$$sim(v_i, v_j) = \frac{f_w(v_i) \cdot f_w(v_j)}{||f_w(v_i)|| \cdot ||f_w(v_j)||}$$
(L1.2)

Di mana merupakan fungsi embedding yang didefinisikan pada subbab L1.1.1. Nilai akhir similarity berada dalam rentang [-1,1], Invarians terhadap magnitude menjadikannya lebih robust untuk teks dengan panjang berbeda dibandingkan dengan Euclidean distance karena komponen yang diukur adalah arah/orientasi maknanya dalam ruang vektor (C. D. Manning et al., 2009). Cosine similarity mengeksploitasi properti ruang vektor yang sudah terstruktur secara semantik (Weinberger & Saul, 2009).

Contoh penggunaan rumus disajikan pada Gambar L1.4, dua teks dalam ruang vektor dapat dikomputasi menggunakan cosine similarity untuk mengukur derajat sudut yang menentukan persentase similarity terhadap teks tersebut.

Gambar L1.4. Cosine Similarity dalam Ruang Vektor

Dalam penelitian ini, cosine similarity digunakan sebagai alat ukur objektif untuk menentukan apakah sebuah feedback telah mencakup aspek yang diminta oleh rubrik. Sebagai contoh, terdapat dua vektor hasil embedding, yaitu vektor narasi mahasiswa (+,+) dan vektor deskripsi rubrik (-, ), jika hasil perhitungan rumus L1.2 mendekati nilai 1, misalnya 0,92, maka kedua teks tersebut dianggap memiliki semantic similarity yang sangat tinggi. Sebaliknya, jika mendekati 0, misalnya 0,15, maka narasi mahasiswa dianggap tidak berkaitan dengan kriteria rubrik tersebut.

### L1.1.3 Landasan Komputasional

Komponen embedding dan cosine similiarity yang telah dijabarkan pada subbab L1.1.1 dan L1.1.2 menghasilkan sinyal numerik berupa nilai similiarity antar dua unit teks. Subbab ini menjelaskan bagaimana sinyal tersebut berfungsi sebagai basis inferensi yaitu bagaimana nilai kontinu yang dihasilkan ruang vektor dapat di transformasikan menjadi sebuah keputusan.

Nilai similiarity yang dihasilkan merupakan ukuran angular closeness atau sudut orientasi dalam ruang representasi vektor untuk memprediksi kemiripan. Transformasi dari kedekatan ini menjadi keputusan yang dapat ditindaklanjuti memerlukan tambahan yang dibangun di atas lapisan embedding. Alur transformasi dinyatakan pada

$$x \to v_x \to sim(v_x, v_{f_i}) \to \mathcal{D}$$
 (L1.3)

Dengan contoh penggunaan,

1. : Mahasiswa menulis narasi "Data diambil dari LinkedIn".
2. , : Teks diubah menjadi vektor [0.11,0.54, … ].
3. / , #& : Vektor dibandingkan dengan vektor kriteria rubrik (#& ) "Keragaman Platform", menghasilkan similarity score 0,87.
4. .: Karena skor 0,87 ≥ threshold (misalnya 0,84), maka sistem mengambil keputusan (.) bahwa kriteria tersebut terpenuhi.

Di mana teks dipetakan menjadi representasi vektor ,, dibandingkan dalam ruang yang sama pada vektor #& , dan menghasilkan suatu keputusan (.) yang bergantung pada mekanisme yang akan dibangun diatasnya sehingga dapat dikatakan bahwa komponen embedding hanya bertugas menghasilkan sinyal dan interpretasi atas sinyal merupakan tanggung jawab lapisan sistem yang lebih tinggi.

Rumus ini merepresentasikan pipeline evaluasi semantik dalam sistem, yaitu mencakup indikator cakupan rubrik, koherensi skor-narasi, dan relevansi topik. Indikator kedalaman elaborasi tidak melalui transformasi ruang vektor ini karena dievaluasi secara independen menggunakan aturan heuristik berbasis jumlah kata. Kegunaannya adalah untuk menunjukkan bahwa komponen embedding hanya bertugas menghasilkan sinyal, sementara keputusan akhir (.) untuk memicu atau tidak memicu scaffolding merupakan tanggung jawab lapisan logika sistem yang membandingkan sinyal tersebut dengan threshold tertentu. Alur komputasi komponen dalam penelitian ini disajikan pada Gambar L1.5.

Gambar L1.5. Representasi Pipeline Penelitian

Properti ini menilai kualitas inferensi yang dihasilkan dibatasi oleh kualitas representasi yang dihasilkan model, sehingga diperlukan pemilihan model embedding yang akan dikalibrasi pada data aktual sebagaimana dijabarkan pada Tabel L1.1. Selain itu pendekatan ini memiliki batasan interpretabilitas. Representasi vektor yang dihasilkan bersifat laten dan tidak memiliki padanan linguistik eksplisit pada tingkat token atau frasa (Senel et al., 2018) . Keterbatasan ini diterima sebagai konsekuensi yang dapat dikelola selama sinyal yang dihasilkan menunjukkan keselarasan yang memadai dengan penilaian manusia pada data anotasi yang dievaluasi melalui F1 score pada subbab L1.1.4.

### L1.1.4 Metrik Evaluasi Kinerja Model dan Kalibrasi Threshold

Dalam klasifikasi teks pada NLP, terutama pada dataset yang memiliki class imbalance, penggunaan F1-Score menjadi metrik utama untuk mengevaluasi kinerja model. F1-Score merupakan harmonic mean dari precission dan recall menggunakan II.4 (Riyanto et al., 2023) yang diilustrasikan pada Gambar L1.6. Precision mengukur ketepatan model dalam memprediksi kelas positif dari keseluruhan hasil yang diprediksi positif oleh sistem, sedangkan Recall mengukur banyaknya kelas positif yang dideteksi dengan benar, dibandingkan dengan total data positif yang sebenarnya.

$$F1 Score = \frac{2 \times Precission \times Recall}{Precission + Recall}$$
 (L1.4)

Dimana precission merupakan ukuran untuk mengukur akurasi prediksi yang benar menggunakan rumus L1.5.

$$Precission = \frac{TP}{TP + FP} \tag{II.5}$$

Sementara recall mengukur kemampuan untuk menemukan semua kemungkinan prediksi yang benar menggunakan rumus L1.6.

$$Recall = \frac{TP}{TP + FN} \tag{II.6}$$

Dengan,

1. 7 atau true positive merupakan jumlah label "TRUE" yang diidentifikasi dengan benar.
2. 7 atau false positive adalah jumlah label "FALSE", namun diidentifikasi sebagai "TRUE".
3. = atau false negative adalah jumlah label "TRUE", namun diidentifikasi sebagai "FALSE".

Gambar L1.6. Balancing Preccision dan Recall untuk F1-Score

Dalam skenario multi-label classification berbasis pasangan narasi dan kriteria pada penelitian ini, evaluasi F1-Score dilakukan menggunakan kerangka microaveraging, di mana setiap pasangan diperlakukan secara setara tanpa diberikan bobot berbeda (Sokolova & Lapalme, 2009). Pendekatan ini dipilih karena distribusi pasangan antar aspek rubrik tidak seimbang, sehingga aspek rubrik dengan kriteria yang lebih banyak akan menghasilkan pasangan kriteria evaluasi yang lebih banyak.

Lebih lanjut, dalam arsitektur digital scaffolding, F1-Score merupakan nilai acuan utama yang digunakan untuk melakukan kalibrasi threshold. Karena nilai cosine similarity yang dihasilkan oleh representasi vector embedding berupa nilai kontinu, sistem memerlukan mekanisme untuk menetapkan batas diskrit yang menentukan apakah suatu feedback memerlukan intervensi prompt atau tidak. Melalui pendekatan eksperimen optimasi seperti metode F1 sweep, untuk mencari threshold optimal yang memaksimalkan nilai F1-Score pada data anotasi (X. Gao et al., 2025).
