# Video Compressor Web App

Aplikasi ini adalah **web-based Video Compressor** untuk mengunggah dan mengompresi video langsung dari browser. Dibangun dengan Python (Flask) dan Bootstrap, aplikasi ini memanfaatkan **FFmpeg** untuk mengurangi ukuran file video secara efisien tanpa mengorbankan kualitas secara signifikan.

🔗 **Demo:** *(jalankan secara lokal atau di server Docker Anda)*

---

## Fitur Utama
- Unggah video langsung dari browser
- Kompresi otomatis menggunakan FFmpeg
- Unduh hasil kompresi langsung tanpa penyimpanan jangka panjang
- **Auto-delete** file hasil kompresi setelah diunduh atau dalam beberapa menit
- Dukungan `.env` untuk konfigurasi port dan variabel rahasia
- Dapat dijalankan di Docker untuk kemudahan deploy
- Antarmuka responsif dan bersih berbasis Bootstrap
- Siap dikembangkan lebih lanjut untuk fitur tambahan seperti **progress bar** atau **enkripsi video**

---

## Teknologi
- Python (Flask)
- FFmpeg
- Bootstrap 5
- Docker & Docker Compose

---

## Keamanan
- File video yang diunggah tidak disimpan permanen
- File otomatis dihapus dari server setelah proses selesai
- Mendukung konfigurasi variabel rahasia melalui `.env`

---

## Lisensi
Proyek ini dikembangkan sebagai alat bantu pribadi dan edukatif.
Bebas digunakan dan dimodifikasi sesuai kebutuhan Anda.

---

© 2025 - wedeh.my.id