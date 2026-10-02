# Dataset Bab 1–4

Seluruh file berasal dari folder `data/` [repository pendamping edisi kedua](https://github.com/gedeck/practical-statistics-for-data-scientists/tree/8a6d3bb6468e979c861d4b37215e1413702dfdfa/data). `manifest.json` mencatat commit, ukuran byte, dan SHA-256 dari 14 file. Seluruh CSV disertakan dalam repository ini sehingga notebook dapat langsung dijalankan setelah clone. Skrip di bawah dipakai untuk memvalidasi checksum atau mengunduh ulang file yang hilang.

```sh
python scripts/download_data.py
python scripts/download_data.py --check
```

Jalankan dari root proyek sesudah mengaktifkan `.venv`. Unduhan memakai pustaka standar Python. File yang sudah valid dilewati. File lokal dengan checksum berbeda tidak ditimpa. Notebook tidak mengunduh diam-diam dan dapat dijalankan tanpa jaringan setelah dataset tersedia.

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
| house_sales.csv | 4 | 22.687 transaksi, 22 kolom data + label baris asal tanpa header; separator **tab**; label dibaca sebagai indeks |

Konteks asli sebagaimana dijelaskan buku: sensus AS, statistik keterlambatan penerbangan, seri saham/ETF, properti King County, Lending Club, eksperimen web, studi fungsi paru, serta contoh frekuensi digit. Repository digunakan sebagai sumber distribusi data; metadata sumber primer/tanggal tidak lengkap untuk semua file, sehingga tidak dibuat klaim verifikasi langsung terhadap instansi asal.

Catatan makna data: `sp500_data` memuat nilai negatif dan diperlakukan sebagai seri perubahan yang disediakan buku, bukan harga penutupan mentah. Transformasi NFLX buku direproduksi dengan keterbatasan tersebut. CSV maskapai tidak mencantumkan periode, maka label grafik tidak mengklaim harian. DFW berisi agregat pecahan dan dipertahankan apa adanya. Pada sesi A/B, `Time` dikali 100 sesuai kode resmi sehingga hasil dinyatakan dalam detik; ini bukan konversi menit ×60. `four_sessions.Time` sudah dalam detik. `AdjSalePrice` adalah harga rumah yang telah disesuaikan, bukan `SalePrice` mentah.
