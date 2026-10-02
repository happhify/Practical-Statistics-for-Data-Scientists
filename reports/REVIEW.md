# Catatan pemeriksaan akhir

Pengerjaan dan pemeriksaan: 26–27 September 2026. Hasil rinci dan waktu UTC tersedia pada `execution.json` dan `validation.json`.

- [x] Pengantar dan seluruh teks Bab 1–4 dibaca dari PDF lokal, bukan hanya judul/daftar isi; daftar isi dipetakan sebelum penyusunan.
- [x] 119 subbab mempunyai anchor dan pembahasan pada notebook; termasuk materi teoritis tanpa kode.
- [x] 4 notebook dijalankan berurutan, tiap notebook dengan kernel baru; 79 sel kode lulus dan tidak ada output error tersimpan.
- [x] 34 keluaran gambar diperiksa secara visual melalui ekstraksi output PNG: judul, sumbu, unit, keterbacaan, dan pola dibandingkan dengan interpretasi.
- [x] Pemeriksaan angka acuan tercantum sebagai assertion pada sel yang relevan, termasuk populasi, hitungan bin, jumlah pinjaman, probabilitas binomial, Welch, ANOVA, exact test, koefisien, dan outlier.
- [x] Seluruh 14 dataset diunduh ulang menggunakan `scripts/download_data.py` ke direktori sementara kosong; semua SHA-256 cocok, kemudian mode `--check` juga lulus. Data kerja tidak ditimpa oleh pengujian.
- [x] Versi paket pada requirements cocok dengan environment dan `python -m pip check` tidak menemukan dependency rusak.
- [x] Sintaks semua sel, format notebook, urutan execution count, pemetaan halaman, dan checksum dataset diperiksa otomatis.
- [x] `.venv` digunakan konsisten; `.venv-1` dipertahankan; tidak dibuat environment tambahan.
- [x] Atribusi, lisensi, bantuan AI, koreksi kode sumber, dan batas interpretasi dijelaskan.
- [x] PDF/ekstraksi teks buku tetap di luar repository.

Temuan yang diperbaiki selama eksekusi: peringatan API pandas/set_index dan konfigurasi marker scatter Bab 1; tanda kurung pada tabel GAM Bab 4; perbedaan label indeks file rumah dengan posisi baris; angka ukuran sampel dalam interpretasi Bab 3. Setelah perubahan kode, notebook terkait dijalankan ulang penuh. Perapian uraian sesudahnya tidak mengubah kode atau output.

Catatan yang sengaja dipertahankan: histogram murder rate mengikuti bin 1–11 dari buku, sehingga New Hampshire (0,9) tidak masuk histogram tetapi tetap masuk KDE; batas tersebut dinyatakan di interpretasi. Rangkuman OLS menampilkan condition number/skewness sebagai informasi diagnostik, bukan error eksekusi.

Belum diverifikasi: metadata sumber primer yang tidak tersedia pada dataset pendamping, semantik return NFLX, unit PEFR spesifik, periode observasi airline, interaksi UI VS Code secara otomatis, dan platform selain Python 3.13.5/macOS Intel. Tidak ada klaim inferensi kausal atau validasi prediksi masa depan. Two-way ANOVA merupakan uraian konseptual karena faktor kedua tidak disediakan buku sebagai data.
