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

# 3. Dokumentasi Program & Output

# Halaman Login + Menu (Admin & User)

<img width="432" height="402" alt="Screenshot 2026-10-04 204146" src="https://github.com/user-attachments/assets/933e8a0d-2ed9-488c-8151-0c08c4ebd2b8" />

Halaman Login User

<img width="428" height="387" alt="Screenshot 2026-10-04 204452" src="https://github.com/user-attachments/assets/083ca00a-9797-4a9e-a2fc-7a92163cd9c4" />

Halaman Login Admin

Halaman login digunakan untuk masuk ke dalam sistem. Pengguna memasukkan username dan password yang sudah terdaftar. Password diketik menggunakan library pwinput jadi passwordnya akan terlihat seperti bintang bintang (hidden). Setelah login berhasil, program akan menentukan role pengguna dan menampilkan menu yang sesuai.

Dari tampilan, admin dan user memang memiliki menu yang saya, tetapi sebenarnya admin memiliki akses yang lebih luas daripada user. Admin memiliki akses untuk melihat, menambah, mengubah, dan membatalkan seluruh data peminjaman ruangan, sedangkan user hanya memiliki akses untuk melihat, menambah, mengubah, dan membatalkan data peminjaman ruangan miliknya sendiri.

# Menu (1) Lihat Jadwal Peminjaman

<img width="297" height="247" alt="Screenshot 2026-10-04 205455" src="https://github.com/user-attachments/assets/5799f9cc-81b5-469a-a287-47f84013e5d5" />

Output ketika belum ada jadwal peminjaman

<img width="352" height="207" alt="Screenshot 2026-10-04 211941" src="https://github.com/user-attachments/assets/32c2684d-1274-4514-9dc6-43a36cd4593c" />

Output ketika sudah ada jadwal peminjaman

Data peminjaman ditampilkan dalam bentuk tabel menggunakan library PrettyTable. Informasi yang ditampilkan terdiri dari ID, Nama, Ruangan, Tanggal, Waktu. Jika belum terdapat data peminjaman, program akan menampilkan pesan bahwa belum ada data peminjaman.

# Menu (2) Tambah Peminjaman Ruangan

<img width="513" height="637" alt="Screenshot 2026-10-04 204740" src="https://github.com/user-attachments/assets/59bec2e0-4aa3-4a59-8573-c25a180ba62c" />

Output ketika melakukan peminjaman ruangan (Berlaku buat role admin juga)

<img width="407" height="280" alt="Screenshot 2026-10-04 212111" src="https://github.com/user-attachments/assets/f0b0d730-2578-4260-8d01-75d9cfd3ff1b" />

Output ketika ingin menambahkan ruang tapi ternyata ID-nya sudah digunakan

<img width="512" height="192" alt="Screenshot 2026-10-04 212429" src="https://github.com/user-attachments/assets/8bb2d276-6393-4aa7-81be-606ae3b5802c" />

Output ketika user ingin mengubah data tapi ternyata jadwalnya bentrok/sudah ada yang makai (berlaku untuk menu 3 juga)

<img width="462" height="126" alt="Screenshot 2026-10-04 214118" src="https://github.com/user-attachments/assets/4da895ca-0597-42a6-9ed1-b50539df88bf" />

Output ketika ruangan yang dipilih di luar dari ruangan yang disediakan (berlaku untuk menu 3 juga)

Menu tambah peminjaman digunakan untuk memasukkan data peminjaman baru. Program akan melakukan beberapa pengecekan sebelum data disimpan, yaitu:

- Memeriksa apakah ID sudah digunakan.
- Memeriksa apakah ruangan tersedia.
- Memeriksa apakah jadwal yang dipilih mengalami bentrok dengan peminjaman lain.

Jika semua pengecekan berhasil, data akan disimpan ke dalam list peminjaman. Kalau gagal, maka user akan menginput ulang data yang ada.

# Menu (3) Ubah Peminjaman

<img width="521" height="357" alt="Screenshot 2026-10-04 205839" src="https://github.com/user-attachments/assets/8a402343-fdbc-4556-bbca-b1335c0fa2a9" />

Output ketika user (mirza) mengubah datanya sendiri

<img width="397" height="290" alt="Screenshot 2026-10-04 205900" src="https://github.com/user-attachments/assets/a2e601fc-8c23-40c7-9634-d99d1b123984" />

Output ketika user (ataya) mengubah data user lain (mirza)

<img width="517" height="356" alt="Screenshot 2026-10-04 210159" src="https://github.com/user-attachments/assets/09f28ae7-abc5-48f0-87b8-359345f72594" />

Output ketika admin mengubah data user (mirza)

<img width="340" height="103" alt="Screenshot 2026-10-04 212730" src="https://github.com/user-attachments/assets/62dca955-5a5d-416c-815a-ced2564d4b2c" />

Output ketika user ingin mengubah data tapi ternyata ID-nya salah/tidak ditemukan (berlaku untuk menu 4 juga)

Menu ubah peminjaman digunakan untuk mengubah ruangan, tanggal, dan waktu dari data peminjaman. Admin dapat mengubah data peminjaman apa saja, sedangkan user hanya dapat mengubah peminjaman yang menggunakan username miliknya. Program juga akan melakukan pengecekan jadwal agar data yang baru tidak bertabrakan dengan peminjaman lain.

# Menu (4) Batalkan Peminjaman

<img width="371" height="265" alt="Screenshot 2026-10-04 210826" src="https://github.com/user-attachments/assets/5c018360-28c8-467d-a396-ce96f8d2a992" />

Output ketika user (mirza) membatalkan datanya sendiri

<img width="413" height="267" alt="Screenshot 2026-10-04 210904" src="https://github.com/user-attachments/assets/99c29a2c-3e02-48fb-8217-a57d7168e44c" />

Output ketika user (ataya) membatalkan data user lain (mirza)

<img width="368" height="262" alt="Screenshot 2026-10-04 210927" src="https://github.com/user-attachments/assets/bef7a782-f61e-4497-82c3-7a17958cfaf7" />

Output ketika admin membatalkan data user (mirza)

Menu batalkan peminjaman digunakan untuk menghapus data peminjaman berdasarkan ID. Admin dapat membatalkan peminjaman apa saja, sedangkan user hanya dapat membatalkan peminjaman miliknya sendiri, data yang berhasil dibatalkan akan dihapus dari list peminjaman.

# Menu (5) Logout

<img width="433" height="352" alt="Screenshot 2026-10-04 211252" src="https://github.com/user-attachments/assets/c7396789-b94f-4086-9861-e046366826de" />

Output ketika logout (berlaku buat role admin juga)

program akan kembali ke halaman login dan akan selesai jika pengguna keluar dari program.

# Penerapan Nilai Tambah













