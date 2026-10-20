# Dataset Bab 1–6

Seluruh file berasal dari folder `data/` [repository pendamping edisi kedua](https://github.com/gedeck/practical-statistics-for-data-scientists/tree/8a6d3bb6468e979c861d4b37215e1413702dfdfa/data). `manifest.json` mencatat commit, ukuran byte, dan SHA-256 dari 18 file. Seluruh CSV disertakan dalam repository ini sehingga notebook dapat langsung dijalankan setelah clone.

Notebook membaca file langsung dari folder ini dan tidak mengunduh apa pun, sehingga dapat dijalankan tanpa jaringan.

| Dataset | Bab | Isi dan ukuran |
|---|---|---|
| state.csv | 1 | 50 negara bagian; populasi dan murder rate |
| dfw_airline.csv | 1 | 1 baris, 5 penyebab keterlambatan DFW |
| sp500_data.csv.gz | 1, 2 | 5.647 tanggal × 517 simbol; kolom tanggal menjadi indeks |
| sp500_sectors.csv | 1 | 517 simbol beserta sektor |
| kc_tax.csv.gz | 1 | 498.249 properti; taksiran, luas, kode pos |
| lc_loans.csv | 1 | 450.961 pinjaman; grade dan status |
| airline_stats.csv | 1 | 33.468 observasi maskapai; persentase keterlambatan |
| loans_income.csv | 2 | 50.000 pendapatan pemohon pinjaman |
| web_page_data.csv | 3 | 36 sesi; A=21 dan B=15 |
| four_sessions.csv | 3 | 20 sesi, masing-masing 5 per halaman |
| click_rates.csv | 3 | 6 sel tabel klik tiga headline; `Rate` berisi hitungan |
| imanishi_data.csv | 3 | Frekuensi 10 digit; nama kolom dibersihkan dari spasi |
| LungDisease.csv | 4 | 122 pengamatan paparan debu kapas dan PEFR |
| house_sales.csv | 4, 6 | 22.687 transaksi, 22 kolom data + label baris asal tanpa header; separator **tab**; label dibaca sebagai indeks. Bab 6 memakainya ulang untuk demonstrasi regression tree |
| loan_data.csv.gz | 5, 6 | 45.342 pinjaman Lending Club **seimbang** (22.671 default, 22.671 paid off), 21 kolom; `Unnamed: 0` = nomor baris asal |
| loan3000.csv | 5, 6 | 3.000 pinjaman (1.445 default); `borrower_score`, `payment_inc_ratio`, `dti`, `purpose_` |
| full_train_set.csv.gz | 5 | 119.987 pinjaman tidak seimbang (18,89% default), 19 kolom, tanpa `borrower_score` |
| loan200.csv | 6 | 201 baris: baris pertama berlabel `target` (pinjaman baru), 200 lainnya data latih KNN; `payment_inc_ratio`, `dti` |

Konteks asli sebagaimana dijelaskan buku: sensus AS, statistik keterlambatan penerbangan, seri saham/ETF, properti King County, Lending Club, eksperimen web, studi fungsi paru, serta contoh frekuensi digit. Metadata sumber primer dan tanggal tidak lengkap untuk semua file.

Catatan makna data: `sp500_data` memuat nilai negatif dan diperlakukan sebagai seri perubahan yang disediakan buku, bukan harga penutupan mentah. Transformasi NFLX buku direproduksi dengan keterbatasan tersebut. CSV maskapai tidak mencantumkan periode. DFW berisi agregat pecahan dan dipertahankan apa adanya. Pada sesi A/B, `Time` dikali 100 sesuai kode resmi sehingga hasil dinyatakan dalam detik; ini bukan konversi menit ×60. `four_sessions.Time` sudah dalam detik. `AdjSalePrice` adalah harga rumah yang telah disesuaikan, bukan `SalePrice` mentah.

Catatan data pinjaman (Bab 5–6): `outcome` diturunkan dari `status` (Charged Off/Default → default; Fully Paid → paid off), sehingga `status` tidak dipakai sebagai prediktor. `borrower_score` adalah fitur turunan buku: proporsi 20 tetangga terdekat (KNN tanpa standardisasi) yang paid off berdasarkan `dti`, `revol_bal`, `revol_util`, `open_acc`, `delinq_2yrs_zero`, dan `pub_rec_zero`; notebook Bab 6 memverifikasi nilainya identik pada 99,83% (45.266 dari 45.342) record. Karena dihitung in-sample dari outcome data yang sama, fitur ini mengandung leakage. `emp_len_` diawali spasi (` < 1 Year`, ` > 1 Year`). Satuan `payment_inc_ratio` dan `dti` tidak dicantumkan eksplisit di CSV.
