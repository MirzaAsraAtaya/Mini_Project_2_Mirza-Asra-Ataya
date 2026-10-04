# Mini_Project_2_Mirza-Asra-Ataya

Nama: Mirza Asra Ataya 

NIM: 2609116043

Kelas B 26'

# 1. Deskripsi Singkat Program

Pada Mini Project 2 ini saya mengembangkan Sistem Peminjaman Ruangan FT UNMUL yang sebelumnya saya buat pada Mini Project 1. Sistem ini masih memiliki fungsi utama yang sama, yaitu 1) melihat jadwal ruangan yang telah dipinjam (READ), 2) menambah data peminjaman ruangan dan jadwal (CREATE), 3) mengubah data peminjaman (UPDATE), serta 4) membatalkan atau menghapus data peminjaman (DELETE). Sistem ini tetap dibuat dengan tujuan untuk membantu pengguna dalam mengelola peminjaman ruangan dan menghindari bentrok jadwal.

Pada Mini Project 2, saya mengembangkan sistem sebelumnya dengan menambahkan fitur login dan dua jenis role, yaitu admin dan user. Admin punya akses untuk mengelola seluruh data peminjaman, sedangkan user hanya dapat mengubah dan membatalkan peminjaman miliknya sendiri. Nah selanjutnya sesuai instruksi, pada versi ini saya juga menerapkan Dictionary untuk menyimpan data pengguna dan role, Function untuk beberapa proses program, serta beberapa library Python seperti pwinput untuk menyembunyikan password dan PrettyTable untuk menampilkan data peminjaman dalam bentuk tabel yangg rapi, serta os supaya tampilan terminalnya bersih. Sistem ini juga ditambah dengan validasi input supaya kesalahan saat memasukkan data tidak langsung membuat program berhenti.


# 2. Gambar Flowchart

<img width="2667" height="4670" alt="Flowchart Minpro 2 drawio(3)" src="https://github.com/user-attachments/assets/e263a558-09b0-4439-b37e-2ff4cbd8fd72" />


Program dimulai dari halaman login. Pengguna harus memasukkan username dan password yang telah tersedia di dalam Dictionary. Kalau username atau password salah, pengguna diminta untuk mencoba kembali. Kalau login berhasil, sistem akan secara otomatis membaca role pengguna dan menampilkan menu sesuai dengan role tersebut.

Ada dua role dalam program yang saya buat ini, yaitu admin dengan pw 123 dan user (mirza dengan pw 043 dan ataya dengan pw 044). Admin punya akses penuh terhadap data peminjaman ruangan, jadi admin ini bisa melihat, menambah, mengubah, atau menghapus semua data yang ada. Sedangkan user, juga bisa melihat, menambah, mengubah, atau menghapus, tapi yang membedakannya adalah khusus untuk user dia hanya bisa mengubah atau menghapus data miliknya sendiri.

Pada menu utama, pengguna dapat memilih beberapa menu, yaitu melihat jadwal (Menu 1), menambah peminjaman (Menu 2), mengubah peminjaman (Menu 3), membatalkan peminjaman (Menu 4), atau logout (Menu 5).

Saat menambah peminjaman, program melakukan pengecekan ID agar tidak terjadi ID yang sama. Program juga memeriksa ketersediaan ruangan dan mengecek apakah ruangan, tanggal, dan waktu yang dipilih sudah digunakan atau belum oleh peminjaman lain.

Pada proses perubahan dan pembatalan, program terlebih dahulu mencari ID peminjaman. Jika pengguna memiliki role user, program juga melakukan pengecekan kepemilikan data (ID). Setelah proses selesai, pengguna dapat kembali menggunakan menu atau melakukan logout.

Nah yang terakhir, Jika pengguna melakukan logout, program akan kembali ke halaman login. Program akan terus berjalan sampai pengguna memilih menu keluar dari halaman login.
