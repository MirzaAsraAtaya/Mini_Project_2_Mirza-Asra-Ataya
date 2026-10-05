# Minpro-2-DDP-SistemPeminjamanRuanganFTUNMUL

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

<img width="426" height="192" alt="Screenshot 2026-10-05 201534" src="https://github.com/user-attachments/assets/4920dadf-a9df-4c03-8201-c00995bf9d02" />

Halaman Login ketika nama user tidak ditemukan

Setelah program dijalankan, program akan menampilkan halaman login. Pada bagian ini pengguna harus memasukkan username dan password yang sudah tersedia di dalam Dictionary. Password menggunakan library pwinput, sehingga password yang diketik tidak ditampilkan secara langsung. Jika username dan password benar, program akan membaca role dari pengguna tersebut dan menampilkan menu sesuai dengan role yang dimiliki. Pada program ini terdapat dua jenis role, yaitu admin dan user. Admin memiliki akses penuh untuk melihat, menambah, mengubah, dan membatalkan seluruh data peminjaman. Sedangkan user juga dapat menggunakan menu yang sama, tetapi user hanya dapat mengubah dan membatalkan data peminjaman yang dibuat oleh dirinya sendiri.

# Menu (1) Lihat Jadwal Peminjaman

<img width="297" height="247" alt="Screenshot 2026-10-04 205455" src="https://github.com/user-attachments/assets/5799f9cc-81b5-469a-a287-47f84013e5d5" />

Output ketika belum ada jadwal peminjaman

<img width="352" height="207" alt="Screenshot 2026-10-04 211941" src="https://github.com/user-attachments/assets/32c2684d-1274-4514-9dc6-43a36cd4593c" />

Output ketika sudah ada jadwal peminjaman

Menu pertama digunakan untuk melihat data peminjaman ruangan yang sudah tersimpan. Pada menu ini saya menggunakan library PrettyTable untuk membuat tampilan data peminjaman menjadi lebih rapi dalam bentuk tabel. Data yang ditampilkan terdiri dari ID, nama, kode ruangan, tanggal, dan waktu peminjaman. Jika belum terdapat data peminjaman, program akan menampilkan pesan bahwa belum ada data peminjaman. Jika sudah terdapat data, maka seluruh data peminjaman akan ditampilkan dalam bentuk tabel.

# Menu (2) Tambah Peminjaman Ruangan

<img width="513" height="637" alt="Screenshot 2026-10-04 204740" src="https://github.com/user-attachments/assets/59bec2e0-4aa3-4a59-8573-c25a180ba62c" />

Output ketika melakukan peminjaman ruangan (Berlaku buat role admin juga)

<img width="407" height="280" alt="Screenshot 2026-10-04 212111" src="https://github.com/user-attachments/assets/f0b0d730-2578-4260-8d01-75d9cfd3ff1b" />

Output ketika ingin menambahkan ruang tapi ternyata ID-nya sudah digunakan

<img width="512" height="192" alt="Screenshot 2026-10-04 212429" src="https://github.com/user-attachments/assets/8bb2d276-6393-4aa7-81be-606ae3b5802c" />

Output ketika user ingin mengubah data tapi ternyata jadwalnya bentrok/sudah ada yang makai (berlaku untuk menu 3 juga)

<img width="462" height="126" alt="Screenshot 2026-10-04 214118" src="https://github.com/user-attachments/assets/4da895ca-0597-42a6-9ed1-b50539df88bf" />

Output ketika ruangan yang dipilih di luar dari ruangan yang disediakan (berlaku untuk menu 3 juga)

Menu kedua digunakan untuk menambahkan data peminjaman ruangan baru. Mekanismenya masih kurang lebih sama seperti pada Mini Project 1, tetapi pada Mini Project 2 terdapat beberapa validasi tambahan. Program akan meminta pengguna untuk memasukkan ID, ruangan, tanggal, dan waktu peminjaman. Setelah itu program akan melakukan beberapa pengecekan, yaitu mengecek apakah ID sudah digunakan, mengecek apakah kode ruangan tersedia, dan mengecek apakah ruangan dan jadwal yang dipilih mengalami bentrok dengan data peminjaman yang sudah ada.

Jika ID sudah digunakan, pengguna akan diminta untuk memasukkan ID yang berbeda. Jika ruangan tidak tersedia atau jadwalnya bentrok, pengguna juga akan diminta untuk memilih kembali. Jika semua data sudah sesuai, data peminjaman akan dimasukkan ke dalam list peminjaman.

# Menu (3) Ubah Peminjaman

<img width="521" height="357" alt="Screenshot 2026-10-04 205839" src="https://github.com/user-attachments/assets/8a402343-fdbc-4556-bbca-b1335c0fa2a9" />

Output ketika user (mirza) mengubah datanya sendiri

<img width="397" height="290" alt="Screenshot 2026-10-04 205900" src="https://github.com/user-attachments/assets/a2e601fc-8c23-40c7-9634-d99d1b123984" />

Output ketika user (ataya) mengubah data user lain (mirza)

<img width="517" height="356" alt="Screenshot 2026-10-04 210159" src="https://github.com/user-attachments/assets/09f28ae7-abc5-48f0-87b8-359345f72594" />

Output ketika admin mengubah data user (mirza)

<img width="340" height="103" alt="Screenshot 2026-10-04 212730" src="https://github.com/user-attachments/assets/62dca955-5a5d-416c-815a-ced2564d4b2c" />

Output ketika user ingin mengubah data tapi ternyata ID-nya salah/tidak ditemukan (berlaku untuk menu 4 juga)

Menu ketiga digunakan untuk mengubah data peminjaman yang sudah ada. Pada menu ini saya menggunakan Function ubah_peminjaman() untuk menjalankan proses perubahan data.
Program akan meminta pengguna memasukkan ID peminjaman yang ingin diubah. Setelah ID ditemukan, program akan mengecek role pengguna. Jika yang login adalah admin, maka admin dapat mengubah data peminjaman siapa saja. Sedangkan jika yang login adalah user, program akan mengecek apakah data tersebut merupakan milik user yang sedang login. Setelah data berhasil ditemukan dan pengguna memiliki hak akses, pengguna dapat memasukkan ruangan, tanggal, dan waktu yang baru. Program kemudian akan melakukan pengecekan kembali untuk memastikan data baru tidak mengalami bentrok dengan peminjaman lain.

# Menu (4) Batalkan Peminjaman

<img width="371" height="265" alt="Screenshot 2026-10-04 210826" src="https://github.com/user-attachments/assets/5c018360-28c8-467d-a396-ce96f8d2a992" />

Output ketika user (mirza) membatalkan datanya sendiri

<img width="413" height="267" alt="Screenshot 2026-10-04 210904" src="https://github.com/user-attachments/assets/99c29a2c-3e02-48fb-8217-a57d7168e44c" />

Output ketika user (ataya) membatalkan data user lain (mirza)

<img width="368" height="262" alt="Screenshot 2026-10-04 210927" src="https://github.com/user-attachments/assets/bef7a782-f61e-4497-82c3-7a17958cfaf7" />

Output ketika admin membatalkan data user (mirza)

Menu keempat digunakan untuk membatalkan atau menghapus data peminjaman. Pada menu ini saya menggunakan Function batalkan_peminjaman() untuk menjalankan proses pembatalan data. Pengguna terlebih dahulu memasukkan ID peminjaman yang ingin dibatalkan. Program kemudian mencari ID tersebut di dalam list peminjaman. Jika ID tidak ditemukan, program akan menampilkan pesan bahwa data tidak ditemukan. Untuk admin, data peminjaman apa saja dapat dibatalkan. Sedangkan untuk user, program akan mengecek terlebih dahulu apakah data tersebut merupakan miliknya. Jika data sesuai dengan hak akses pengguna, data tersebut akan dihapus dari list peminjaman.

# Menu (5) Logout

<img width="433" height="352" alt="Screenshot 2026-10-04 211252" src="https://github.com/user-attachments/assets/c7396789-b94f-4086-9861-e046366826de" />

Output ketika logout (berlaku buat role admin juga)

Menu kelima digunakan untuk melakukan logout dari akun yang sedang digunakan. Ketika pengguna memilih menu logout, perulangan menu berdasarkan role akan dihentikan dan program akan kembali ke halaman login, jadinyaa pengguna lain dapat melakukan login menggunakan akun yang berbeda dan program akan terus berjalan sampai pengguna memilih menu keluar pada halaman login.

# Penerapan Nilai Tambah

<img width="430" height="333" alt="gambar" src="https://github.com/user-attachments/assets/da624b73-837a-443b-a4e7-4b6951aa8e47" />

Output ketika pengguna bukannya ngetik angka malah ngetik kata "Login"

Pada program ini saya menggunakan try-except untuk menangani kesalahan input dari pengguna. Contohnya ketika pengguna memasukkan pilihan menu yang seharusnya berupa angka (1/2), tetapi pengguna memasukkan huruf atau input yang tidak sesuai (Login/Keluar). Dengan adanya try-except, program tidak langsung berhenti karena error (ValueError), tetapi akan menampilkan pesan bahwa input yang dimasukkan salah dan pengguna dapat mencoba kembali.

<img width="660" height="77" alt="Screenshot 2026-10-04 223132" src="https://github.com/user-attachments/assets/b08bf9b0-e088-435c-bdea-51e36d37337c" />

Library yang saya pakai

Saya menggunakan tiga library Python untuk menambahkan fungsi pada program. Library pwinput digunakan pada halaman login untuk menyembunyikan password ketika diketik. Kemudian PrettyTable digunakan untuk membuat tampilan data peminjaman menjadi lebih rapi dalam bentuk tabel. Saya juga menggunakan os untuk membersihkan tampilan terminal ketika berpindah halaman atau menu.
















