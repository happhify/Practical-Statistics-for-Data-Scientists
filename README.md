# Practical Statistics for Data Scientists

Repository belajar dan reproduksi Python untuk tugas individu mata kuliah **Machine Learning**, S1 Teknik Komputer, mencakup **Bab 1–6**: Bab 1–4 (tenggat 3 Oktober 2026) dan Bab 5–6 (tenggat 17 Oktober 2026).

Referensi: Peter Bruce, Andrew Bruce, Peter Gedeck. *Practical Statistics for Data Scientists: 50+ Essential Concepts Using R and Python*, edisi kedua, O’Reilly, 2020. ISBN **978-1-492-07294-2**. Kode dan dataset diadaptasi dari [repository resmi edisi kedua](https://github.com/gedeck/practical-statistics-for-data-scientists/tree/8a6d3bb6468e979c861d4b37215e1413702dfdfa).

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

| Notebook | Topik |
|---|---|
| [Chapter_01.ipynb](Chapter_01.ipynb) | Tipe data, lokasi/variasi, histogram, KDE, kategori, korelasi, contingency table, visualisasi multivariabel |
| [Chapter_02.ipynb](Chapter_02.ipynb) | Sampling/bias, CLT, standard error, bootstrap, CI, normal/t/binomial/chi-square/F/Poisson/eksponensial/Weibull |
| [Chapter_03.ipynb](Chapter_03.ipynb) | A/B, hipotesis, permutasi, p-value, t-test, multiple testing, ANOVA, chi-square/Fisher, bandit, power |
| [Chapter_04.ipynb](Chapter_04.ipynb) | OLS, evaluasi/CV, stepwise, bobot, CI/PI, kategori, interaksi, diagnostik, polinomial/spline/GAM |
| [Chapter_05.ipynb](Chapter_05.ipynb) | Naive Bayes, LDA/Fisher, regresi logistik dan GLM, odds ratio, confusion matrix, precision/recall/specificity, ROC/AUC, lift, undersampling/bobot/SMOTE, cost-based classification |
| [Chapter_06.ipynb](Chapter_06.ipynb) | KNN (jarak, one-hot, standardisasi, memilih K, feature engine), decision tree dan impurity, pruning, bagging, random forest/OOB/variable importance, AdaBoost, XGBoost, regularisasi, hyperparameter CV |

Setiap notebook memuat tujuan, ringkasan, deskripsi data, rumus/asumsi yang relevan, kode, interpretasi, kesimpulan, referensi, dan latihan.

Beberapa hasil utama:

- Bab 1: mean populasi 6.162.876,3; weighted murder rate ≈4,445834 per 100.000; subset properti 432.693 baris.
- Bab 2: median pendapatan USD62.000; bootstrap SE ≈USD211,65; peluang binomial tepat dua sukses dari lima (p=0,1) = 0,0729.
- Bab 3: selisih mean sesi B−A ≈35,6667 detik; Welch p≈0,140762; ANOVA F≈2,739825, p≈0,077586; Fisher exact 2×3 p≈0,482414.
- Bab 4: slope Exposure ≈−4,184576; R² model rumah dasar ≈0,540588; RMSE latih ≈USD261.220.
- Bab 5: naive Bayes P(default) pinjaman contoh ≈0,654; bobot LDA borrower_score ≈7,178; koefisien logistik borrower_score ≈−4,613, odds ratio small_business ≈3,37; AUC ≈0,692 (holdout ≈0,690); data tidak seimbang: 0,39% diprediksi default tanpa penanganan vs 57,7% dengan bobot 1/p.
- Bab 6: KNN K=20 pinjaman baru P(default)=0,45; borrower_score dataset identik dengan skor KNN in-sample pada 99,83% (45.266 dari 45.342) record; OOB accuracy random forest ≈0,575 (in-sample ≈0,999); error validasi XGBoost default ≈0,359 vs penalty ≈0,329; error CV terbaik ≈32,7% (eta 0,1, max_depth 3).

Hasil acak dapat berbeda dari output R buku karena seed, generator, dan definisi metode.

## Struktur file

```text
Practical-Statistics-for-Data-Scientists/
├── Chapter_01.ipynb … Chapter_06.ipynb
├── README.md
├── LICENSE
└── data/
    ├── README.md
    ├── manifest.json
    └── 18 file CSV/CSV.GZ
```

## Cara menjalankan

Bab 1–4 diuji dengan Python **3.13.5** di macOS; Bab 5–6 dijalankan dengan Python 3.13 (Linux) memakai versi library yang sama ditambah `imbalanced-learn` dan `xgboost`. Output sudah tersimpan, jadi notebook bisa langsung dibaca di GitHub tanpa dijalankan ulang. Untuk menjalankan sendiri, buat environment lalu pasang library berikut (versi yang dipakai saat pengujian):

```sh
python3.13 -m venv .venv
source .venv/bin/activate
pip install numpy==2.5.3 pandas==3.0.6 scipy==1.16.3 matplotlib==3.11.2 seaborn==0.13.2 \
    statsmodels==0.15.0 scikit-learn==1.9.1 wquantiles==0.6 pygam==0.12.0 patsy==1.0.3 ipykernel==7.3.0 \
    imbalanced-learn==0.14.2 xgboost==3.4.1
```

Di macOS, jika `import xgboost` gagal karena pustaka OpenMP (`libomp`) tidak ditemukan, pasang dengan `brew install libomp`. `Chapter_06.ipynb` paling berat (random forest 500 tree dan grid XGBoost 45 fit); di lingkungan uji Run All memerlukan sekitar 8 menit.

Di VS Code:

1. Buka **folder proyek**, bukan hanya file notebook, lewat **File → Open Folder**. Sel setup mencari `data/manifest.json` dari folder kerja.
2. Pastikan ekstensi **Python** dan **Jupyter** dari Microsoft tersedia.
3. Buka `Chapter_01.ipynb`, klik **Select Kernel → Python Environments**, lalu pilih `.venv`.
4. Pilih **Restart Kernel**, lalu **Run All**. Keenam notebook tidak saling bergantung, sehingga dapat dijalankan dalam urutan apa pun.

## Dataset

Ke-18 dataset sudah disertakan di `data/`, sehingga notebook dapat dijalankan setelah clone tanpa unduhan tambahan maupun koneksi internet. File berasal dari folder `data/` repository resmi edisi kedua; commit sumber, ukuran, dan SHA-256 tiap file dicatat di [data/manifest.json](data/manifest.json). Detail kolom dan batas metadata ada di [data/README.md](data/README.md).

## Adaptasi dan keterbatasan

Rincian per bagian dicatat di dekat sel terkait pada masing-masing notebook. Beberapa perubahan penting:

- API pandas/seaborn diperbarui; unit, denominator, seed, dan arti statistik diperjelas.
- Eksponensial menggunakan `scale=5` untuk rate 0,2. Arah permutasi konversi konsisten; permutasi headline mempertahankan margin. F/p ANOVA tidak dibagi dua dan residual df=16.
- Fisher 2×3 dari contoh R dibuat sebagai enumerasi Python exact. Stepwise AIC memakai helper lokal transparan agar tidak membutuhkan `dmba`; hasil fitur cocok dengan contoh buku.
- CV, bootstrap CI/PI, VIF, dan HC3 diberi label tambahan. CV berdasarkan `PropertyID` mencegah transaksi properti sama berada di dua fold. `ZipGroup` berbasis target seluruh data hanya dipakai untuk reproduksi in-sample, bukan penilaian generalisasi.
- Transformasi NFLX direproduksi literal tetapi belum tervalidasi sebagai return harian; metadata harga mentah tidak tersedia. Satuan PEFR dan periode observasi airline tidak tercantum di data.
- Two-way ANOVA dijelaskan secara konseptual; CSV tidak memiliki faktor hari.
- Bab 5: target 0/1 eksplisit (1 = default) agar tanda koefisien sama dengan R; regresi logistik tanpa penalti memakai `C=np.inf` + `newton-cholesky` karena `penalty` deprecated di scikit-learn 1.9 dan liblinear tidak konvergen baik pada data tidak seimbang (hasil 0,39% prediksi default kini cocok dengan versi R buku). Partial residual memakai working residual standar GLM. GAM memakai `LogisticGAM`. Holdout, lift, evaluasi strategi kelas langka, dan ilustrasi biaya hipotetis diberi label tambahan.
- Bab 6: `plot_tree`/`export_text` menggantikan `dmba`. Kolom probabilitas KNN feature engine dan `prob_default` XGBoost pada kode buku terbalik dan diperbaiki; `iteration_range` XGBoost dikoreksi menjadi `(0, n)`. OOB dihitung inkremental, prediksi random forest yang digambar adalah OOB, dan permutation importance memakai holdout. `borrower_score` terbukti dibuat dari outcome data yang sama (leakage), sehingga hasil yang memakainya diberi catatan.
- Bab 7 dan validasi prospektif/kausal belum dibahas.

## Orisinalitas, lisensi, dan bantuan AI

Penjelasan Indonesia ditulis ulang, dengan atribusi pada buku. Kode merupakan **adaptasi/reproduksi**, bukan klaim kode sepenuhnya asli. Kode diadaptasi dari `python/code/Chapter 1 … Chapter 6` dan notebook pendamping pada [repository resmi edisi kedua](https://github.com/gedeck/practical-statistics-for-data-scientists/tree/8a6d3bb6468e979c861d4b37215e1413702dfdfa) (commit `8a6d3bb`), © 2019 Peter C. Bruce, Andrew Bruce, Peter Gedeck, berlisensi GNU GPL v3. Adaptasi kode di repository ini didistribusikan dengan lisensi yang sama; teks lengkapnya ada di [LICENSE](LICENSE). Lisensi kode tersebut tidak mengubah hak cipta buku atau hak sumber asli dataset. PDF buku tidak disalin ke repository.

**Pengungkapan bantuan AI:** Codex membantu membaca pengantar dan Bab 1–4 PDF, memetakan cakupan, menulis penjelasan Indonesia, mengadaptasi dan menambah kode belajar, menyiapkan dependency/data, menjalankan notebook, mendiagnosis kesalahan, memeriksa output, dan menyusun dokumentasi. Jadi bantuan AI pada hasil ini mencakup **kode dan dokumentasi**, lebih luas daripada teori saja. Untuk Bab 5–6, Claude (Anthropic) membantu memetakan subbab edisi kedua, menulis penjelasan Indonesia, mengadaptasi dan memperbaiki kode buku, menambah demonstrasi belajar yang diberi label, menjalankan notebook, memeriksa angka terhadap output buku/repository resmi, serta memperbarui README dan manifest data. Ketentuan tugas secara eksplisit mengizinkan LLM untuk penjelasan teori, sehingga penggunaan di luar itu dicatat lengkap di sini.
