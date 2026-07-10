# MEGA CHEAT SHEET SIDANG TUGAS AKHIR
**"Ultimate Question Proof Defense"**

Gunakan dokumen ini sebagai perisai absolut Anda. Setiap poin berisi:
1. **[LOGIKA]**: Penjelasan bahasa manusia biasa untuk Anda tangkap maknanya.
2. **[SIDANG]**: Bahasa akademis tingkat tinggi untuk dilontarkan ke penguji.
3. **[NGELES]**: Taktik defensif jika diserang balik atau dipojokkan.

---

## SEKTOR 1: PONDASI TEORI PEDAGOGI (MENGAPA SISTEM INI ADA?)

### 1.1 Masalah Utama: Evaluative Judgement vs Feedback Literacy
* **[LOGIKA]:** Mahasiswa S1 belum punya insting dosen. Kalau disuruh menilai teman (peer-assessment), komentarnya sering "Bagus", "Mantap", atau "Sudah sesuai". Mereka tidak tahu cara memakai rubrik untuk merangkai argumen kritis (feedback literacy).
* **[SIDANG]:** "Berdasarkan literatur Setiawan (2026) dan Carless & Boud (2018), akar masalah pada metode *Project-Based Learning* (PjBL) bukan sekadar kurangnya instrumen, melainkan rendahnya kapasitas *Evaluative Judgement* mahasiswa. Mereka kesulitan menerjemahkan ekspektasi rubrik menjadi narasi *feedback* yang bermakna dan konstruktif."
* **[NGELES]:** (Jika dosen bilang: *Kan sudah dikasih rubrik, harusnya mereka bisa baca dong?*) -> "Rubrik hanyalah dokumen mati, Pak/Bu. *Feedback literacy* adalah keterampilan kognitif yang butuh dilatih *real-time*. Membaca rubrik tidak serta-merta membuat seseorang pandai merangkai narasi kritis."

### 1.2 Kenapa namanya "Scaffolding Nudge" & "Affective Scaffolding"?
* **[LOGIKA]:** Kita tidak memblokir tombol submit kalau narasinya jelek. Kita cuma ngasih notifikasi (*pop-up*) "Eh, kurang ini lho." Ini sengaja, biar mereka mikir sendiri (Zone of Proximal Development - ZPD).
* **[SIDANG]:** "Sistem ini menggunakan pendekatan *Scaffolding Nudge* (Oosterum, 2026) yang bersifat non-koersif (tidak memaksa). Tujuannya memberikan stimulus kognitif *just-in-time* tanpa mengambil alih otonomi berpikir mahasiswa, agar mereka menyelesaikan masalah di dalam *Zone of Proximal Development* (Vygotsky) mereka secara mandiri."
* **[NGELES]:** (Jika dosen bilang: *Kenapa nggak dipaksa aja kalau indikatornya belum hijau nggak bisa submit?*) -> "Jika dipaksa (*coercive*), itu akan merusak *Affective Scaffolding* (Jang et al., 2025). Pemaksaan memicu frustrasi dan *cognitive overload*, yang berujung pada *gaming the system* (mahasiswa mengetik asal-asalan sekadar untuk lolos sensor)."

---

## SEKTOR 2: POSISI RISET VS DEVELOPMENT (BOM WAKTU SEMINAR 3)

### 2.1 "Ini TA Bikin Web atau Riset Ilmiah?"
* **[LOGIKA]:** Dosen sering bingung, kalau ini riset kuantitatif, kok ada aplikasi web-nya? Kita harus tegas misahin: Aplikasi web cuma "alat ukur" (kayak stetoskop), sedangkan "risetnya" adalah nyari tahu orang yang pakai stetoskop itu sehat atau sakit.
* **[SIDANG]:** "Fokus utama Tugas Akhir ini murni pada **Riset Eksperimental Kuantitatif** dan **Pedagogi Komputasional**, Bapak/Ibu. Aplikasi Pendukung Eksperimen (APE) yang saya bangun hanyalah instrumen pengumpulan data. Itulah mengapa seluruh dokumen *Software Development Life Cycle* (SDLC) seperti arsitektur, testing fungsional, dan *use case* saya isolasi di Lampiran 6 & 7."
* **[NGELES]:** (Jika dosen terus mencecar soal kodingan PHP/React/Web) -> "Mohon maaf Bapak/Ibu, sesuai arahan batasan masalah, validasi teknis kode aplikasi telah diselesaikan dalam tahap *pilot testing* sebelum eksperimen dimulai. Fokus pengujian Bab V difokuskan pada keandalan NLP sebagai alat ukur dan dampak statistik intervensi terhadap kualitas teks mahasiswa."

---

## SEKTOR 3: METODOLOGI & SAMPLING (THE "HOW")

### 3.1 Kenapa Post-test Only Control Group? (Kenapa tidak pre-test?)
* **[LOGIKA]:** Kalau kita ukur di awal (pre-test), mahasiswa jadi tahu rahasia eksperimen kita. Nanti pas disuruh nulis *feedback* lagi, mereka pura-pura bagus karena udah tau dinilai (*priming effect*).
* **[SIDANG]:** "Saya menghindari desain *pre-test* untuk mencegah *Testing Threat* dan *Priming Effect*. Pemberian tes awal akan membuat subjek menyadari kriteria penilaian dan merubah perilaku alamiah mereka. Melalui alokasi sampel acak (*Randomized Controlled Trial*), kelompok perlakuan dan kontrol diasumsikan berangkat dari *baseline* setara."

### 3.2 Kenapa 30 Sampel? Dari mana rumusnya?
* **[LOGIKA]:** Karena mahasiswa sekelas jumlahnya dikit. Jadi kita hitung matematis pakai rumus Cochran biar minimal 30 orang itu sah menurut ilmu statistik.
* **[SIDANG]:** "Populasi kelas sangat terbatas (32 mahasiswa). Saya menggunakan formula Cochran untuk populasi terbatas dengan presisi $5\%$ dan interval kepercayaan $95\%$, menghasilkan ukuran sampel minimum 30 individu yang memadai untuk mencegah *low statistical power*."

---

## SEKTOR 4: DAPUR NLP & S-BERT (MENJAWAB "HALUSINASI")

### 4.1 Bagaimana teks "Nama saya Yudi" berubah jadi angka?
* **[LOGIKA]:** AI tidak bisa baca huruf, bisanya baca angka (koordinat). S-BERT mengubah kalimat panjang jadi kumpulan ratusan titik koordinat (*vector*) di ruang 3D super besar (*Embedding Space*). Kalau maknanya mirip, koordinatnya berdekatan.
* **[SIDANG]:** "Pemrosesan bahasa alami menggunakan arsitektur *Siamese Sentence-BERT*. Kalimat mentah di-tokenisasi lalu dilewatkan pada lapisan *Transformer* yang sudah melalui *pre-training* bahasa Indonesia, menghasilkan *dense vector* (vektor dimensi tinggi). Kedekatan semantik kemudian dikalkulasi berdasarkan jarak spasial antar vektor menggunakan rumus *Cosine Similarity*."

### 4.2 Kenapa S-BERT? Kenapa tidak Word2Vec / TF-IDF / ChatGPT (LLM)?
* **[SIDANG & NGELES]:** 
  - **Kenapa bukan TF-IDF/Word2Vec?** "Metode konvensional tersebut buta terhadap konteks berurutan (*contextual blindness*). Kata 'bisa' (ular) dan 'bisa' (mampu) akan dianggap sama oleh TF-IDF. S-BERT menggunakan atensi dua arah (*Bidirectional Attention*) untuk memahami konteks kalimat utuh."
  - **Kenapa bukan LLM (ChatGPT/Claude)?** "LLM murni (*Generative AI*) memiliki dua kelemahan fatal untuk instrumen ukur: Pertama, ia rentan *hallucination* (halusinasi argumen). Kedua, ia tidak deterministik (diberi soal sama, bisa dijawab berbeda setiap hari). S-BERT bersifat *deterministik* murni—jarak vektor akan selalu absolut sama untuk dua kalimat yang sama, menjamin reliabilitas alat ukur."

---

## SEKTOR 5: ALGORITMA PER INDIKATOR

### 5.1 Bagaimana mengukur Cakupan Rubrik?
* **[LOGIKA]:** Dicek apakah tiap baris di rubrik (dimensi) dibahas di narasi mahasiswa. 
* **[SIDANG]:** "Sistem memecah narasi mahasiswa per kalimat, lalu menghitung *Cosine Similarity* kalimat tersebut terhadap *prompt* definisi masing-masing dimensi rubrik."

### 5.2 Bagaimana mengukur Koherensi Skor dan Narasi?
* **[LOGIKA]:** Kalau mahasiswanya ngasih nilai "Sangat Baik" (skor 4), tapi narasinya mirip dengan teks rubrik skor "Buruk" (skor 1), berarti dia asal klik.
* **[SIDANG]:** "Algoritma menghitung *Euclidean distance* atau beda ordinal antara skor kuantitatif yang dipilih pengguna dengan kategori rubrik yang paling semantis-mirip dengan narasinya. Jika prediksinya lompat $>1$ level ordinal (misal: skor 4 tapi narasinya bernada skor 1), koherensi dinilai *false*."

### 5.3 Bagaimana mengukur Kedalaman Elaborasi?
* **[LOGIKA]:** Nggak pakai AI yang pusing, cukup dihitung jumlah kata dan variasinya.
* **[SIDANG]:** "Ini adalah indikator deterministik murni (*rule-based heuristic*). Diukur berdasarkan densitas leksikal (jumlah kata minimal), tanpa melibatkan komputasi jarak vektor."

### 5.4 Bagaimana mengukur Relevansi Topik?
* **[LOGIKA]:** Dihitung apakah narasi bahas mata kuliah yang bener, atau malah bahas hal di luar topik.
* **[SIDANG]:** "Model menghitung vektor narasi terhadap dokumen acuan (*golden standard* / RPP) untuk memastikan *domain-specific relevance*."

---

## SEKTOR 6: KALIBRASI & METRIK NLP (F1, PRECISION, RECALL)

### 6.1 Metafora Penggaris: Kenapa threshold-nya berubah-ubah (0.84, 0.89)?
* **[LOGIKA]:** Komputer bilang kemiripannya 85%. Apakah 85% itu lulus atau gagal? Ya tergantung "batas KKM"-nya (*threshold*). Karena kampus/jurusan beda-beda gaya bahasanya, batas KKM ini dicari dulu pakai data tes awal (kalibrasi).
* **[SIDANG]:** "*Threshold similarity* NLP bukan konstanta fisika absolut. Angka tersebut adalah *hyperparameter* yang ditemukan melalui fase kalibrasi (*grid-search*) terhadap 70 pasang anotasi manual data *pilot study* spesifik di kelas ini. Ini memastikan bahwa sensitivitas algoritma disesuaikan (*tailored*) dengan kekhasan diksi jurusan tersebut."

### 6.2 Kenapa F1-Score Relevansi Topik paling jelek (0.43)?
* **[LOGIKA]:** Relevansi topik itu paling susah diukur pakai AI kelas ringan. "Topik" itu luas. Kadang mahasiswa nyindir soal proyek, pakai perumpamaan, tapi menurut S-BERT itu dianggap di luar topik.
* **[SIDANG]:** "Relevansi topik memiliki metrik F1-Score yang buruk (0.43) karena indikator ini memerlukan **Inferensi Leksikal Kognitif Tingkat Tinggi**. S-BERT sangat mahir melakukan pencocokan semantik permukaan (seperti Cakupan Rubrik), namun kesulitan memetakan korelasi implisit ketika mahasiswa menggunakan analogi atau jargon *open-ended* di luar *golden dataset*."

---

## SEKTOR 7: JUSTIFIKASI STATISTIK INFERENSIAL (MANOVA)

### 7.1 Kenapa pakai MANOVA (Multivariat)? Bukan ANOVA atau T-Test biasa?
* **[LOGIKA]:** Karena nilai dari keempat indikator (Cakupan, Koherensi, Kedalaman, Relevansi) itu saling berkaitan. Kalau diuji satu-satu (4 kali T-Test), error statistiknya jadi berkali lipat.
* **[SIDANG]:** "Sesuai prosedur statistik parametrik multivariat, keempat indikator tekstual tersebut secara teoretis tidak independen (saling beririsan kognitif). Menggunakan 4 uji ANOVA terpisah akan memicu inflasi *Family-wise Type I Error* (peluang mengklaim efek yang sebenarnya tidak ada). MANOVA menyatukan matriks pengujian secara simultan."

### 7.2 Apa itu Asumsi *Box's M* yang gagal? Kenapa eksperimen lanjut?
* **[LOGIKA]:** Variansi kelompok treatment dan kontrol ternyata beda jauh. Box's M-nya merah (P < 0.05). Kalau di ilmu statistik jadul, eksperimen batal. Tapi ilmu modern bilang: tenang aja, baca angka *Pillai's Trace*.
* **[SIDANG]:** "Memang benar uji asumsi homogenitas matriks kovarians (*Box's M test*) menolak asumsi kesetaraan. Namun, menurut literatur Tabachnick & Fidell, pelanggaran *Box's M* seringkali diakibatkan sensitivitas algoritma, bukan kerusakan data fatal. Oleh karena itu, *test statistic* yang digunakan dielevasi dari *Wilks' Lambda* menjadi **Pillai's Trace**, karena metrik ini paling *robust* (kebal) terhadap heterogenitas ketika ukuran sampel per kelompok seimbang."

---

## SEKTOR 8: HASIL EKSPERIMEN STATISTIK

### 8.1 P-Value 0.0441 itu artinya apa?
* **[LOGIKA]:** Karena di bawah 0.05 (batas error 5%), berarti intervensi web Anda "terbukti sah" ngefek, bukan karena kebetulan (hoki).
* **[SIDANG]:** "Nilai p multivariat $0.0441 < \alpha (0.05)$ pada pengujian *Peer Assessment* menunjukkan penolakan H0 yang sukses. Secara empiris, ada perbedaan vektor pemenuhan indikator tekstual yang signifikan akibat intervensi *digital scaffolding*."

### 8.2 Partial Eta Squared (0.30) itu maksudnya apa?
* **[LOGIKA]:** OKE alatnya ngefek, tapi seberapa hebat efeknya? Angka 0.3 artinya sistem web Anda menyumbang 30% perbaikan, sisanya 70% dari faktor lain (mungkin mahasiswa pinter dari sononya).
* **[SIDANG]:** "*Partial Eta Squared* adalah metrik ukur *Effect Size*. Nilai 0.30 menunjukkan bahwa intervensi menyumbangkan 30% varians terhadap kualitas narasi gabungan. Ini tergolong impak berskala *moderate-to-large* di ranah eksperimen pedagogi sosial."

---

## SEKTOR 9: DINAMIKA LOG MAHASISWA & ANOMALI

### 9.1 Kenapa cuma "Kedalaman Elaborasi" yang naik signifikan di Univariat?
* **[LOGIKA]:** Waktu mahasiswa disuruh ngerevisi narasi yang kurang koheren, mereka cuma nambahin kalimat panjang-panjang (*insertion*). Alhasil, teksnya emang makin panjang (Kedalaman naik), tapi logika skor-narasinya belum tentu makin koheren.
* **[SIDANG]:** "Analisis *micro-log* menunjukkan perilaku penyelesaian dominan (*dominant resolution pattern*) berupa operasi *Insertion* (penambahan sintaks teks). Operasi superfisial ini sangat relevan untuk mengangkat skor kuantitas kata (Kedalaman Elaborasi), namun belum menyentuh restrukturisasi kognitif mendalam seperti *Replacement* (merombak) yang dibutuhkan untuk memperbaiki Koherensi Skor-Narasi."

---

## SEKTOR 10: KETERBATASAN & KESIMPULAN (JURUS ULTIMATE)

### 10.1 "Berarti sistem Anda masih banyak kurangnya, bikin mahasiswa pusing (Cognitive Load)?"
* **[LOGIKA]:** Emang bener, baca pop-up peringatan sambil ngetik itu bikin mata pedih. Tapi itu temuan jujur kita.
* **[SIDANG / NGELES ABSOLUT]:** "Sangat benar, Bapak/Ibu. Kelemahan UI *Split-Attention Effect* yang tertangkap dari kuesioner eksplanatori TAM ini justru menjadi **temuan riset emas** di Bab V. Keterbatasan kognitif akibat *text-based scaffolding* ini persis membuktikan argumen Jang et al. (2025). Oleh karena itu, Kesimpulan TA ini secara akademik merekomendasikan transisi ke arah asisten obrolan (Generative AI Chatbot) sebagai *Future Work* utama. Saya tidak menutupi kelemahan, melainkan merasionalisasinya menggunakan literatur terkini."

---

## SEKTOR 11: GELOMBANG SERANGAN EKSTREM (THE DEVIL'S ADVOCATE)
*Bagian ini adalah pertahanan lapis baja untuk menghadapi dosen penguji yang sangat kritis dan mencoba mencari celah metodologis dari anomali-anomali kecil di dokumen Anda.*

### 11.1 Tragedi Sampel 30 vs Populasi 32
* **[LOGIKA]:** Populasi kelas 32 orang. Sampel 30. Kenapa harus repot hitung rumus Cochran kalau ujungnya cuma "membuang" 2 orang? Kesannya seperti sok akademis.
* **[SIDANG]:** "Penentuan sampel 30 responden bukan sekadar untuk menggugurkan kewajiban rumus Cochran, melainkan keharusan prosedural. Sisa 2 mahasiswa dari populasi 32 orang tersebut sengaja diisolasi sebagai subjek *pilot testing* (uji coba fungsionalitas APE dan kalibrasi *threshold*). Jika 2 orang ini digabungkan ke eksperimen utama, hal tersebut akan mencemari kemurnian data karena mereka sudah terekspos (*priming*) oleh instrumen sebelum pre-test."
* **[NGELES]:** "Memaksakan penggunaan total populasi (sensus) tanpa menyisihkan subjek untuk fase kalibrasi NLP akan berisiko menghasilkan instrumen yang bias."

### 11.2 Validitas Bodong Kuesioner TAM
* **[LOGIKA]:** Dosen akan menyerang: "Anda pakai teori penerimaan TAM. Tapi yang isi kuesioner cuma 15 orang (kelompok treatment). TAM itu regresi kuantitatif yang butuh ratusan responden biar valid!"
* **[SIDANG]:** "Penggunaan kuesioner pada subbab V.2.5 di laporan ini berstatus **Eksplanatori Murni**, bukan untuk pengujian hipotesis struktural TAM. Data ini dikumpulkan semata-mata sebagai konteks kualitatif (suara pengguna) untuk menjawab teka-teki mengapa mahasiswa melakukan revisi *insertion* secara masif. Ini berfungsi untuk memberikan konteks, bukan pembuktian komputasional."
* **[NGELES]:** "Betul Bapak/Ibu, jika tujuannya memvalidasi model TAM, 15 sampel sangatlah cacat statistik. Namun tujuan saya murni pemetaan kualitatif (deskriptif) terhadap beban kognitif."

### 11.3 Plin-Plan Generative AI (Menjilat Ludah Sendiri)
* **[LOGIKA]:** Dosen nyinyir: "Di Bab 1 Anda ngotot menolak LLM (ChatGPT) karena halusinasi dan lambat. Tapi di Bab 7 Anda malah menyarankan bikin Chatbot buat ngatasin layar *split-attention*. Bukankah itu kontradiksi?"
* **[SIDANG]:** "Tidak kontradiksi, Bapak/Ibu. Konsep *future work* di Bab 7 merujuk pada arsitektur **RAG (Retrieval-Augmented Generation)**. Dalam arsitektur tersebut, S-BERT tetap bertindak sebagai otak utama (kalkulator deterministik) yang menilai dokumen secara objektif, sementara Chatbot (Generative AI) hanya diposisikan sebagai **Antarmuka (Interface)** untuk mengkomunikasikan hasil dari S-BERT agar lebih interaktif, BUKAN untuk melakukan penilaian itu sendiri."

### 11.4 Pedagogi yang Gagal ("Gaming the System")
* **[LOGIKA]:** Dosen nyerang: "Tadi Anda bilang mahasiswa cuma menambah kata (*insertion*) biar lampu indikator Kedalaman-nya jadi hijau, padahal koherensinya tidak nyambung. Berarti sistem Anda gagal mendidik, malah mengajarkan mahasiswa untuk ngakalin mesin!"
* **[SIDANG]:** "Fenomena ini lazim dalam adopsi teknologi pendidikan fase awal, dikenal sebagai *gaming the system*. Namun dari kacamata *Zone of Proximal Development* (ZPD), ini adalah batu loncatan yang wajar. Peningkatan kuantitas (insertion) adalah transisi tahap pertama. Restrukturisasi kognitif (perbaikan kualitas koherensi) menuntut internalisasi jangka panjang yang sulit dicapai hanya dalam satu siklus proyek. Ini menunjukkan bahwa sistem saya berhasil mendeteksi batasan kemampuan mahasiswa secara presisi."
* **[NGELES]:** "Justru inilah temuan terpenting riset ini: Bahwa instrumen *text-based scaffolding* sangat efektif mendongkrak kuantitas tulisan, tapi punya keterbatasan alami dalam mengubah cara pikir (*mindset*) evaluatif dalam waktu singkat."

### 11.5 Lisensi Open-Source & Komersialisasi B2B
* **[LOGIKA]:** Dosen IT: "Anda bilang mau komersialisasi (B2B) algoritma ini ke kampus lain. S-BERT itu *open-source*, Anda mau jual barang gratisan?"
* **[SIDANG]:** "Model dasar S-BERT memang bersifat *open-source*. Namun, yang menjadi *Intellectual Property* (Kekayaan Intelektual) dan dapat dilisensikan dalam skema B2B adalah **Arsitektur Pipeline Spesifik** yang saya bangun. Yakni: integrasi algoritma *similarity* dengan *rule-based heuristic* berjenjang, mekanisme penentuan *dynamic threshold*, serta integrasinya dengan basis data rubrik akademik spesifik kampus."

---

## SEKTOR 12: SERANGAN META-PENELITIAN & TEKNIS INFRASTRUKTUR
*Penguji kadang tidak menyerang isi TA Anda, melainkan menyerang aspek fundamental dari tata laksana riset Anda, etika, dan kelayakan sistem di dunia nyata.*

### 12.1 Serangan Etika Riset (Informed Consent)
* **[LOGIKA]:** Dosen kepo: "Mahasiswa yang dijadikan kelinci percobaan ini tau nggak kalau narasinya lagi dimata-matai sama sistem Anda?"
* **[SIDANG]:** "Eksperimen ini dijalankan secara terintegrasi dengan modul mata kuliah berjalan (Manajemen Kualitas Terpadu). Log aktivitas dikumpulkan pada tataran metadata operasional sistem, dan identitas mahasiswa telah di-anonimasi (*anonymized*) saat analisis data. Fokus penelitian ini adalah pada tren agregat perilaku kelompok, bukan penilaian individu."

### 12.2 Serangan "Originalitas" (State of the Art)
* **[LOGIKA]:** Dosen julid: "Kalau teori *Scaffolding* dari Jang (2025) dan NLP *Similarity* sudah ada, lalu bedanya TA kamu apa? Cuma replikasi/nyalin doang?"
* **[SIDANG]:** "Kebaruan (*novelty*) dari riset ini bukan pada penciptaan algoritma NLP baru, melainkan pada **Integrasi Arsitektural**. Penelitian sebelumnya (seperti Jang) mayoritas membahas *scaffolding* pada STEM (matematika/koding). TA ini membawa konsep tersebut ke ranah linguistik evaluatif (bahasa Indonesia) dengan mengawinkan model semantik S-BERT dan aturan heuristik spesifik-rubrik, yang mana *pipeline* hibrida ini belum pernah dikembangkan untuk konteks *peer-assessment* di Polban."

### 12.3 Serangan "Garbage In, Garbage Out" (Rubrik Jelek)
* **[LOGIKA]:** "Sistem Anda kan nyocokin tulisan mahasiswa sama rubrik dosen. Kalau dosennya bikin rubrik yang kata-katanya ambigu atau jelek, sistem Anda bakal ngaco dong?"
* **[SIDANG]:** "Sangat tepat, Bapak/Ibu. Model *Semantic Textual Similarity* yang saya bangun ini menjunjung prinsip *Garbage In, Garbage Out* (GIGO). Kinerja *pipeline* sangat bergantung pada kualitas RPP (*golden standard*). Oleh karena itu, pada tahap pra-pemrosesan, kalimat dalam rubrik harus di-ekstraksi dan di-formulasikan ulang menjadi *prompt* deklaratif agar S-BERT dapat mendeteksinya secara optimal. Ini adalah kelemahan sistem yang diakui."

### 12.4 Serangan Bias Anotator (Siapa yang bikin Golden Data?)
* **[LOGIKA]:** "Di Bab 4, untuk ngetes sistem Anda bagus atau tidak, Anda membandingkan prediksi AI dengan hasil nilai manusia (Anotasi). Yang nganotasi siapa? Kamu sendiri? Berarti hasilnya subjektif dan bias dong?"
* **[SIDANG / NGELES]:** "Mengingat keterbatasan sumber daya riset Tugas Akhir, anotasi 70 sampel *pilot study* memang dilakukan oleh peneliti secara mandiri. Namun, proses anotasi ini tidak dilakukan secara impresif (asal-asalan), melainkan dipandu secara ketat menggunakan *Codebook* indikator tekstual yang didefinisikan secara operasional di Bab 3. Untuk *future work*, pengujian dengan *Inter-Rater Reliability* (misalnya dengan 3 dosen penilai) sangat direkomendasikan."

### 12.5 Serangan Infrastruktur (Deploy S-BERT)
* **[LOGIKA]:** Dosen Jaringan/Infrastruktur: "S-BERT itu berat. Kalau sistem ini beneran dipakai di Polban (SAPA), kuat nggak server Polban? Jangan-jangan sistem Anda cuma bisa jalan di laptop Anda doang?"
* **[SIDANG]:** "Berbeda dengan LLM generatif raksasa berukuran puluhan *Gigabyte*, S-BERT berbasis *distil-Transformer* yang saya gunakan relatif sangat ringan (*lightweight*). Model ini dirancang khusus untuk inferensi cepat tanpa memerlukan klaster GPU besar, dan dapat dijalankan secara asinkronus (API *stateless*) pada *virtual machine* standar. Ini menjamin kelayakan komputasional (*computational feasibility*) jika kelak diintegrasikan ke server internal institusi."

---

## SEKTOR 13: SERANGAN DATA LEAKAGE (BOM WAKTU METODOLOGI ML)
*Ini adalah pertahanan khusus jika Anda berhadapan dengan penguji (terutama Penguji 2) yang ahli dalam metodologi Machine Learning dan menyadari bahwa skor F1 Anda ter-inflasi.*

### 13.1 Serangan Evaluasi F1-Score yang "Overfit"
* **[LOGIKA]:** Penguji bilang: "Anda cari model terbaik, metode terbaik, dan threshold terbaik di dataset 384 anotasi. Lalu Anda bilang performanya 61%. Itu kan data yang sama! Wajar saja tinggi karena sistem Anda *menghafal* data itu. Ini namanya *Data Leakage*. Berarti angka 61% itu *overestimate* (palsu)!"
* **[SIDANG]:** "Kritik tersebut sangat valid, Bapak/Ibu. Mengingat kelangkaan dataset bersumber *crowdsourcing* (hanya tersedia 384 data anotasi pada *pilot study* awal), penelitian ini terpaksa melakukan pemilihan model, ekstraksi, dan kalibrasi *threshold* pada himpunan data yang sama tanpa melakukan uji silang (*cross-validation*). Saya telah mengakui secara transparan di subbab **V.4.4** bahwa F1-score 0.61 tersebut bersifat *optimistically biased*. Oleh karena itu, di Bab Kesimpulan, saya tidak mengklaim ini sebagai performa generalisasi absolut, melainkan 'performa optimal pada data kalibrasi'."
* **[NGELES]:** "Meski angka mutlak F1-score-nya mungkin ter-inflasi, tujuan utama dari pencarian *hyperparameter* di RQ1 ini bukanlah untuk mende-deploy model pendeteksi yang sempurna ke seluruh dunia, melainkan sebatas untuk mencari *baseline* terbaik yang cukup stabil untuk digunakan sebagai *trigger* intervensi (scaffolding) pada eksperimen lapangan di RQ2."

### 13.2 Serangan "Blind Deployment" ke Rubrik CATME
* **[LOGIKA]:** Penguji mengejar: "Kalau Anda tahu angkanya *overestimate* di data lama, kenapa Anda berani-beraninya pakai sistem ini ke eksperimen baru (RQ2) yang rubriknya beda total (CATME)? Anda ngetes alat kesehatan yang belum teruji ke pasien baru!"
* **[SIDANG]:** "Penerapan pada rubrik CATME di RQ2 memang merupakan lompatan empiris (*empirical leap*). Namun, arsitektur yang dibangun adalah pendekatan *zero-shot semantic similarity*, di mana S-BERT mencocokkan *prompt* deklaratif secara dinamis, bukan *supervised learning* konvensional yang dilatih khusus untuk teks rubrik tertentu. Meskipun akurasinya dipastikan mengalami degradasi saat berpindah domain rubrik, uji statistik multivariat (MANOVA) di RQ2 justru membuktikan bahwa meski dengan sistem yang tidak sempurna sekalipun, intervensi *scaffolding* tersebut secara empiris berhasil memberikan efek (*effect size*) yang signifikan terhadap kedalaman elaborasi mahasiswa."
