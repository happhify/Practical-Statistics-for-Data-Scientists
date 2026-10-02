# Practical Statistics for Data Scientists

Repository belajar dan reproduksi Python untuk tugas individu mata kuliah **Machine Learning**, S1 Teknik Komputer. Prioritas tugas: **Bab 1–4**, deadline **3 Oktober 2026**. Keempat notebook telah dijalankan dari kernel baru dan menyimpan hasil angka, tabel, serta grafik.

Referensi: Peter Bruce, Andrew Bruce, Peter Gedeck. *Practical Statistics for Data Scientists: 50+ Essential Concepts Using R and Python*, edisi kedua, O’Reilly, 2020. ISBN **978-1-492-07294-2**. Cakupan mengikuti PDF pengguna; kode dan dataset diadaptasi dari [repository resmi edisi kedua](https://github.com/gedeck/practical-statistics-for-data-scientists/tree/8a6d3bb6468e979c861d4b37215e1413702dfdfa). Nama folder/repository: `Practical-Statistics-for-Data-Scientists`.

## Identitas mahasiswa

| Informasi | Isian |
|---|---|
| Nama | Hadi Nugroho |
| NIM | 101032330235 |
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

Total **79 sel kode**, **34 keluaran gambar** (beberapa berisi lebih dari satu panel), dan **119 subbab** dipetakan di [COVERAGE.md](COVERAGE.md). Bagian konseptual tetap dijelaskan tanpa mengarang data. Setiap notebook memuat tujuan, ringkasan, deskripsi data, rumus/asumsi yang relevan, kode, interpretasi, kesimpulan, referensi, dan latihan refleksi.

Contoh hasil yang telah diperiksa:

- Bab 1: mean populasi 6.162.876,3; weighted murder rate ≈4,445834 per 100.000; subset properti 432.693 baris.
- Bab 2: median pendapatan USD62.000; bootstrap SE ≈USD211,65; peluang binomial tepat dua sukses dari lima (p=0,1) = 0,0729.
- Bab 3: selisih mean sesi B−A ≈35,6667 detik; Welch p≈0,140762; ANOVA F≈2,739825, p≈0,077586; Fisher exact 2×3 p≈0,482414.
- Bab 4: slope Exposure ≈−4,184576; R² model rumah dasar ≈0,540588; RMSE latih ≈USD261.220. Skor latih dibedakan dari cross-validation.

Laporan mesin: [execution.json](reports/execution.json) mencatat interpreter, waktu, dan hasil eksekusi; [validation.json](reports/validation.json) mencatat audit output, cakupan, dependency, serta checksum notebook. Waktu di laporan menggunakan UTC; waktu lokal Jakarta = UTC+7. Hasil acak dapat berbeda dari output R buku karena seed, generator, dan definisi metode.

## Struktur file

```text
Practical-Statistics-for-Data-Scientists/
├── Chapter_01.ipynb … Chapter_04.ipynb
├── README.md
├── COVERAGE.md
├── requirements.txt
├── LICENSE
├── THIRD_PARTY_NOTICES.md
├── .gitignore
├── .vscode/settings.json
├── data/
│   ├── README.md
│   ├── manifest.json
│   └── 14 file CSV/CSV.GZ (disertakan dalam repository)
├── scripts/
│   ├── download_data.py
│   ├── execute_notebooks.py
│   └── verify_artifacts.py
└── reports/
    ├── coverage.json
    ├── execution.json
    └── validation.json
```

## Environment yang dipakai

Pemeriksaan awal menemukan `.venv` dan `.venv-1`, keduanya Python **3.13.5** dan saat itu hanya memiliki pip. Dipilih **`.venv`** secara konsisten; `.venv-1` tetap dipertahankan. Tidak dibuat environment ketiga. Pengujian dilakukan pada macOS Intel menggunakan `.venv/bin/python`. Tidak ditemukan `AGENTS.md` pada workspace maupun direktori induk yang diperiksa, dan belum ada notebook/kode pengguna saat pengerjaan dimulai.

`requirements.txt` hanya memuat dependency analisis dan notebook yang digunakan, dengan versi yang cocok pada environment pengujian. `ipykernel` dipakai sebagai kernel VS Code, `nbclient`/`nbformat` untuk eksekusi dan audit; tidak diperlukan instalasi JupyterLab/server penuh. `pypdf` 6.19.0 dipakai sekali untuk membaca PDF lokal saat penyusunan dan tidak diperlukan untuk menjalankan notebook. Resolver memilih SciPy 1.16.3 bersama pyGAM 0.12.0; kombinasi tersebut telah diuji, sehingga tidak perlu mengubah versi untuk menyamai tahun buku.

Di terminal VS Code, masuk ke folder proyek (path mengandung spasi):

```sh
cd "/Users/happhify/Telkom/Machine Learning/Practical-Statistics-for-Data-Scientists"
source ".venv/bin/activate"
python -c "import sys; print(sys.executable); print(sys.version)"
python -m pip install -r requirements.txt
python -m pip check
```

Pastikan interpreter yang tercetak berakhir dengan `Practical-Statistics-for-Data-Scientists/.venv/bin/python`. Instalasi paket pada workspace ini sudah selesai; perintah instalasi disediakan untuk pemulihan atau reproduksi.

Untuk salinan proyek pada komputer lain **yang belum memiliki `.venv`**, buat satu environment terlebih dahulu, lalu gunakan langkah aktivasi/instalasi di atas:

```sh
python3.13 -m venv ".venv"
```

Jangan membuat ulang `.venv` yang sudah berfungsi atau mengaktifkan kedua environment sekaligus. Versi terkunci diuji pada Python 3.13.5/macOS Intel; platform lain belum diuji. Jika instalasi gagal, simpan pesan error, pastikan interpreter yang dipakai, lalu diagnosis dependency yang disebut pesan tersebut.

## Membuka di VS Code

1. Buka **folder proyek**, bukan hanya file notebook, lewat **File → Open Folder**.
2. Pastikan ekstensi **Python** dan **Jupyter** dari Microsoft tersedia.
3. Jalankan **Python: Select Interpreter**, pilih `.venv/bin/python`. Konfigurasi default sudah ada di `.vscode/settings.json`.
4. Buka `Chapter_01.ipynb`, klik **Select Kernel → Python Environments**, lalu pilih Python `.venv`. Kernel notebook perlu dipilih walaupun interpreter editor sudah benar.
5. Pilih **Restart Kernel**, lalu **Run All**. Lanjutkan Bab 2, 3, dan 4 secara berurutan. Sel setup mencetak interpreter aktual.

Output yang disimpan dapat langsung dibaca tanpa menjalankan ulang. Pengujian otomatis memakai interpreter `.venv` yang sama dan kernel baru per notebook; interaksi klik pada UI VS Code tidak diuji secara otomatis.

## Dataset dan reproduksi

Dataset sudah disertakan di `data/`, sehingga notebook dapat langsung dijalankan setelah clone. Untuk memeriksa keutuhan file (atau mengunduh ulang file yang hilang), jalankan:

```sh
python scripts/download_data.py
python scripts/download_data.py --check
```

Skrip mengunduh dari commit tetap, memvalidasi SHA-256, melewati file yang sudah benar, dan menolak menimpa file lokal dengan checksum berbeda. Tidak ada kredensial yang dibutuhkan untuk data publik ini. Setelah data tersedia, semua notebook dapat dijalankan tanpa internet. Detail kolom dan batas metadata ada di [data/README.md](data/README.md).

Untuk mengeksekusi seluruh notebook dari terminal dan menyimpan output:

```sh
python scripts/execute_notebooks.py
python scripts/verify_artifacts.py
```

Atau jalankan satu bab, misalnya `python scripts/execute_notebooks.py 4`. Eksekutor memakai kernel sementara yang diarahkan ke interpreter aktif, tidak memasang kernelspec global, dan menghentikan proses pada error. Output lama dibersihkan sebelum eksekusi. Keempat notebook tidak saling bergantung pada variabel dalam memori. Cache proyek berada dalam `.cache/` dan diabaikan Git.

Eksekusi oleh agen sempat memerlukan izin di luar sandbox karena kernel Jupyter membuka socket localhost; ini pembatasan lingkungan eksekusi agen, bukan kebutuhan mengganti Python atau menginstal ulang environment pengguna.

## Adaptasi dan keterbatasan

Rincian lengkap ada di [COVERAGE.md](COVERAGE.md). Beberapa perubahan penting:

- API pandas/seaborn diperbarui; unit, denominator, seed, dan arti statistik diperjelas.
- Eksponensial menggunakan `scale=5` untuk rate 0,2. Arah permutasi konversi konsisten; permutasi headline mempertahankan margin. F/p ANOVA tidak dibagi dua dan residual df=16.
- Fisher 2×3 dari contoh R dibuat sebagai enumerasi Python exact. Stepwise AIC memakai helper lokal transparan agar tidak membutuhkan `dmba`; hasil fitur cocok dengan contoh buku.
- CV, bootstrap CI/PI, VIF, dan HC3 diberi label tambahan. CV berdasarkan `PropertyID` mencegah transaksi properti sama berada di dua fold. `ZipGroup` berbasis target seluruh data hanya dipakai untuk reproduksi in-sample, bukan penilaian generalisasi.
- Transformasi NFLX direproduksi literal tetapi belum tervalidasi sebagai return harian; metadata harga mentah tidak tersedia. Satuan PEFR dan periode observasi airline tidak diada-adakan.
- Two-way ANOVA dijelaskan secara konseptual; CSV tidak memiliki faktor hari. Foto tokoh, dokumen, dan ilustrasi historis tidak disalin. Semua grafik analitis yang relevan direproduksi atau diberi padanan yang dijelaskan.
- Tidak ada hambatan memperoleh dataset atau menjalankan Bab 1–4. Bab 5–7, validasi prospektif/kausal, dan pengujian platform selain environment di atas belum termasuk hasil ini.

## Orisinalitas, lisensi, dan bantuan AI

Penjelasan Indonesia ditulis ulang, dengan atribusi pada buku. Kode merupakan **adaptasi/reproduksi**, bukan klaim kode sepenuhnya asli. Lisensi GNU GPL v3 upstream disertakan dalam [LICENSE](LICENSE); lihat [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). PDF buku tetap berada di lokasi pengguna dan tidak disalin ke repository. `.gitignore` mengecualikan PDF, environment, cache, dan pola file credential.

**Pengungkapan bantuan AI:** Codex membantu membaca pengantar dan Bab 1–4 PDF, memetakan cakupan, menulis penjelasan Indonesia, mengadaptasi dan menambah kode belajar, menyiapkan dependency/data, menjalankan notebook, mendiagnosis kesalahan, memeriksa output, dan menyusun dokumentasi. Jadi bantuan AI pada hasil ini mencakup **kode dan dokumentasi**, lebih luas daripada teori saja. Ketentuan yang diberikan secara eksplisit mengizinkan LLM untuk penjelasan teori; README ini mengungkap penggunaan sebenarnya agar mahasiswa tidak menyatakan bantuan hanya terbatas pada teori.

Sebelum dikumpulkan, isi identitas, baca interpretasi, jalankan ulang, dan tuliskan refleksi dengan pemahaman sendiri. Bila ketentuan dosen membatasi bantuan AI pada teori, gunakan pengungkapan ini untuk menyesuaikan proses pengerjaan dan pastikan bagian kode yang dikumpulkan memenuhi ketentuan tersebut.

## Cara belajar dari hasil

Baca setiap bagian dengan urutan **pertanyaan → asumsi → kode → output → interpretasi**. Coba ubah satu parameter, lalu jelaskan mengapa hasil berubah. Notebook menyediakan pertanyaan refleksi di akhir bab. Catatan singkat yang disarankan: metode apa yang dipakai, unit outputnya, asumsi terpenting, dan kesimpulan apa yang tidak boleh ditarik. Jangan mengubah output secara manual; jalankan kembali sel setelah mengubah kode.
