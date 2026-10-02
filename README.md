# Practical Statistics for Data Scientists

Repository belajar dan reproduksi Python untuk tugas individu mata kuliah **Machine Learning**, S1 Teknik Komputer. Prioritas tugas: **Bab 1–4**, deadline **3 Oktober 2026**. Keempat notebook telah dijalankan dari kernel baru dan menyimpan hasil angka, tabel, serta grafik.

Referensi: Peter Bruce, Andrew Bruce, Peter Gedeck. *Practical Statistics for Data Scientists: 50+ Essential Concepts Using R and Python*, edisi kedua, O’Reilly, 2020. ISBN **978-1-492-07294-2**. Cakupan mengikuti PDF pengguna; kode dan dataset diadaptasi dari [repository resmi edisi kedua](https://github.com/gedeck/practical-statistics-for-data-scientists/tree/8a6d3bb6468e979c861d4b37215e1413702dfdfa). Nama folder/repository: `Practical-Statistics-for-Data-Scientists`.

## Identitas mahasiswa

| Informasi | Isian |
|---|---|
| Nama | Hadi Nugroho |
| NIM | 101032330235 |
| Kelas | TK4702 |
| Program studi | S1 Teknik Komputer |
| Universitas | Telkom University |
| Dosen | DR. Risman Adnan Mattotorang |
| Mata kuliah | Machine Learning |

## Isi dan hasil eksekusi

| Notebook | Fokus pembelajaran | Sel kode lulus | Keluaran gambar |
|---|---|---:|---:|
| [Chapter_01.ipynb](Chapter_01.ipynb) | Tipe data, lokasi/variasi, histogram, KDE, kategori, korelasi, contingency table, visualisasi multivariabel | 17/17 | 9 |
| [Chapter_02.ipynb](Chapter_02.ipynb) | Sampling/bias, CLT, standard error, bootstrap, CI, normal/t/binomial/chi-square/F/Poisson/eksponensial/Weibull | 18/18 | 10 |
| [Chapter_03.ipynb](Chapter_03.ipynb) | A/B, hipotesis, permutasi, p-value, t-test, multiple testing, ANOVA, chi-square/Fisher, bandit, power | 17/17 | 5 |
| [Chapter_04.ipynb](Chapter_04.ipynb) | OLS, evaluasi/CV, stepwise, bobot, CI/PI, kategori, interaksi, diagnostik, polinomial/spline/GAM | 27/27 | 10 |

Total **79 sel kode**, **34 keluaran gambar** (beberapa berisi lebih dari satu panel), dan **119 subbab** dibahas di keempat notebook. Bagian konseptual tetap dijelaskan tanpa mengarang data. Setiap notebook memuat tujuan, ringkasan, deskripsi data, rumus/asumsi yang relevan, kode, interpretasi, kesimpulan, referensi, dan latihan refleksi.

Contoh hasil yang telah diperiksa:

- Bab 1: mean populasi 6.162.876,3; weighted murder rate ≈4,445834 per 100.000; subset properti 432.693 baris.
- Bab 2: median pendapatan USD62.000; bootstrap SE ≈USD211,65; peluang binomial tepat dua sukses dari lima (p=0,1) = 0,0729.
- Bab 3: selisih mean sesi B−A ≈35,6667 detik; Welch p≈0,140762; ANOVA F≈2,739825, p≈0,077586; Fisher exact 2×3 p≈0,482414.
- Bab 4: slope Exposure ≈−4,184576; R² model rumah dasar ≈0,540588; RMSE latih ≈USD261.220. Skor latih dibedakan dari cross-validation.

Hasil acak dapat berbeda dari output R buku karena seed, generator, dan definisi metode.

## Struktur file

```text
Practical-Statistics-for-Data-Scientists/
├── Chapter_01.ipynb … Chapter_04.ipynb
├── README.md
├── LICENSE
└── data/
    ├── README.md
    ├── manifest.json
    └── 14 file CSV/CSV.GZ
```

## Cara menjalankan

Notebook diuji dengan Python **3.13.5** di macOS. Output sudah tersimpan, jadi notebook bisa langsung dibaca di GitHub tanpa dijalankan ulang. Untuk menjalankan sendiri, buat environment lalu pasang library berikut (versi yang dipakai saat pengujian):

```sh
python3.13 -m venv .venv
source .venv/bin/activate
pip install numpy==2.5.3 pandas==3.0.6 scipy==1.16.3 matplotlib==3.11.2 seaborn==0.13.2 \
    statsmodels==0.15.0 scikit-learn==1.9.1 wquantiles==0.6 pygam==0.12.0 patsy==1.0.3 ipykernel==7.3.0
```

Di VS Code:

1. Buka **folder proyek**, bukan hanya file notebook, lewat **File → Open Folder**. Sel setup mencari `data/manifest.json` dari folder kerja.
2. Pastikan ekstensi **Python** dan **Jupyter** dari Microsoft tersedia.
3. Buka `Chapter_01.ipynb`, klik **Select Kernel → Python Environments**, lalu pilih `.venv`.
4. Pilih **Restart Kernel**, lalu **Run All**. Keempat notebook tidak saling bergantung, sehingga dapat dijalankan dalam urutan apa pun.

## Dataset

Ke-14 dataset sudah disertakan di `data/`, sehingga notebook dapat dijalankan setelah clone tanpa unduhan tambahan maupun koneksi internet. File berasal dari folder `data/` repository resmi edisi kedua; commit sumber, ukuran, dan SHA-256 tiap file dicatat di [data/manifest.json](data/manifest.json). Detail kolom dan batas metadata ada di [data/README.md](data/README.md).

## Adaptasi dan keterbatasan

Rincian per bagian dicatat di dekat sel terkait pada masing-masing notebook. Beberapa perubahan penting:

- API pandas/seaborn diperbarui; unit, denominator, seed, dan arti statistik diperjelas.
- Eksponensial menggunakan `scale=5` untuk rate 0,2. Arah permutasi konversi konsisten; permutasi headline mempertahankan margin. F/p ANOVA tidak dibagi dua dan residual df=16.
- Fisher 2×3 dari contoh R dibuat sebagai enumerasi Python exact. Stepwise AIC memakai helper lokal transparan agar tidak membutuhkan `dmba`; hasil fitur cocok dengan contoh buku.
- CV, bootstrap CI/PI, VIF, dan HC3 diberi label tambahan. CV berdasarkan `PropertyID` mencegah transaksi properti sama berada di dua fold. `ZipGroup` berbasis target seluruh data hanya dipakai untuk reproduksi in-sample, bukan penilaian generalisasi.
- Transformasi NFLX direproduksi literal tetapi belum tervalidasi sebagai return harian; metadata harga mentah tidak tersedia. Satuan PEFR dan periode observasi airline tidak diada-adakan.
- Two-way ANOVA dijelaskan secara konseptual; CSV tidak memiliki faktor hari. Foto tokoh, dokumen, dan ilustrasi historis tidak disalin. Semua grafik analitis yang relevan direproduksi atau diberi padanan yang dijelaskan.
- Tidak ada hambatan memperoleh dataset atau menjalankan Bab 1–4. Bab 5–7, validasi prospektif/kausal, dan pengujian platform selain environment di atas belum termasuk hasil ini.

## Orisinalitas, lisensi, dan bantuan AI

Penjelasan Indonesia ditulis ulang, dengan atribusi pada buku. Kode merupakan **adaptasi/reproduksi**, bukan klaim kode sepenuhnya asli. Kode diadaptasi dari `python/code/Chapter 1 … Chapter 4` dan notebook pendamping pada [repository resmi edisi kedua](https://github.com/gedeck/practical-statistics-for-data-scientists/tree/8a6d3bb6468e979c861d4b37215e1413702dfdfa) (commit `8a6d3bb`), © 2019 Peter C. Bruce, Andrew Bruce, Peter Gedeck, berlisensi GNU GPL v3. Adaptasi kode di repository ini didistribusikan dengan lisensi yang sama; teks lengkapnya ada di [LICENSE](LICENSE). Lisensi kode tersebut tidak mengubah hak cipta buku atau hak sumber asli dataset. PDF buku tidak disalin ke repository.

**Pengungkapan bantuan AI:** Codex membantu membaca pengantar dan Bab 1–4 PDF, memetakan cakupan, menulis penjelasan Indonesia, mengadaptasi dan menambah kode belajar, menyiapkan dependency/data, menjalankan notebook, mendiagnosis kesalahan, memeriksa output, dan menyusun dokumentasi. Jadi bantuan AI pada hasil ini mencakup **kode dan dokumentasi**, lebih luas daripada teori saja. Ketentuan yang diberikan secara eksplisit mengizinkan LLM untuk penjelasan teori; README ini mengungkap penggunaan sebenarnya agar mahasiswa tidak menyatakan bantuan hanya terbatas pada teori.

Sebelum dikumpulkan, isi identitas, baca interpretasi, jalankan ulang, dan tuliskan refleksi dengan pemahaman sendiri. Bila ketentuan dosen membatasi bantuan AI pada teori, gunakan pengungkapan ini untuk menyesuaikan proses pengerjaan dan pastikan bagian kode yang dikumpulkan memenuhi ketentuan tersebut.

## Cara belajar dari hasil

Baca setiap bagian dengan urutan **pertanyaan → asumsi → kode → output → interpretasi**. Coba ubah satu parameter, lalu jelaskan mengapa hasil berubah. Notebook menyediakan pertanyaan refleksi di akhir bab. Catatan singkat yang disarankan: metode apa yang dipakai, unit outputnya, asumsi terpenting, dan kesimpulan apa yang tidak boleh ditarik. Jangan mengubah output secara manual; jalankan kembali sel setelah mengubah kode.
