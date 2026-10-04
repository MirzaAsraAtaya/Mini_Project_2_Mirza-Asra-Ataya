#import library yang dipake
import os #untuk mengakses fungsi sistem operasi
import pwinput #untuk mengakses fungsi input password supaya hidden
from prettytable import PrettyTable  #untuk mengakses fungsi tabel supaya lebih rapi

os.system("cls") #untuk membersihkan layar terminal

#Dictionary untuk menyimpan username, password, dan role pengguna
users = {
    "admin": {
        "password": "123",
        "role": "admin"
    },
    "mirza": {
        "password": "043",
        "role": "user"
    },
    "ataya": {
        "password": "044",
        "role": "user"
    }
}

#Tuple untuk menyimpan data ruangan yang tersedia
ruangan = ("C401", "C402", "C403", "C404", "C405", "C406", "C407", "C408")

#List untuk menyimpan data peminjaman ruangan
peminjaman = []

#Halaman login
#Function untuk login
def login():
    while True:
        print("==========================================================")
        print("====== Selamat Datang di Sistem Peminjaman Ruangan =======")
        print("======================== FT UNMUL ========================")
        print("===========================2.0============================")
        print("==========================================================")
        print("1. Login")
        print("2. Keluar")
        print("")

        #try-except untuk menangani input yang tidak valid
        try:
            #pengguna memilih menu login atau keluar dari program
            pilihan = int(input("Pilih menu: "))

            #percabangan untuk menu login
            if pilihan == 1:

                nama_user = input("Masukkan username: ")

                #Memeriksa apakah username terdapat di dalam Dictionary users
                if nama_user not in users:
                    print("Username tidak ditemukan.")
                    continue

                #Meminta password dengan tampilan password disembunyikan
                password = pwinput.pwinput("Masukkan password: ")

                #Memeriksa kesesuaian password dengan data pada Dictionary
                if password == users[nama_user]["password"]:

                    #Mengambil role pengguna dari Dictionary
                    role = users[nama_user]["role"]

                    print("Login berhasil.")
                    print(f"Selamat datang, {nama_user}!")
                    print("")

                    #Mengembalikan username dan role ke program utama
                    return nama_user, role

                else:
                    print("Password salah.")

            elif pilihan == 2:
                #Mengembalikan nilai None jika pengguna memilih keluar
                return None, None

            else:
                print("Pilihan menu hanya tersedia 1 atau 2.")

        #Bagian except untuk menangani input yang tidak valid (bukan angka) daripada menampilkan ValueError, program akan menampilkan pesan kesalahan dan meminta input ulang
        except ValueError:
            print("Input harus berupa angka.")

#Function untuk mengubah peminjaman ruangan (Menu 3)
def ubah_peminjaman(nama_user, role):

    print("========================================")
    print("         UBAH PEMINJAMAN RUANGAN")
    print("========================================")
    print("")

    #Mencari data peminjaman berdasarkan ID
    id_peminjaman = input("Masukkan ID peminjaman yang ingin diubah: ")
    id_ditemukan = False
    index_data = 0

    #Mencari posisi data yang sesuai dengan ID peminjaman
    for data in peminjaman:
        if data[0] == id_peminjaman:
            id_ditemukan = True
            break
        index_data = index_data + 1

    #Jika ID tidak ditemukan, proses pengubahan dihentikan
    if not id_ditemukan:
        print(f"ID '{id_peminjaman}' tidak ditemukan.")
        return

    ##User hanya dapat mengubah peminjaman miliknya sendiri
    if role == "user":

        if peminjaman[index_data][1] != nama_user:
            print("Anda tidak memiliki hak untuk mengubah peminjaman ini.")
            print("")
            return

    print("Data peminjaman ditemukan.")

    while True:
        kode_ruangan_baru = input(
            "Masukkan kode ruangan yang baru (C401 - C408): "
        )

        if kode_ruangan_baru not in ruangan:
            print("Ruangan tidak tersedia, silahkan pilih C401 - C408.")
            continue

        tanggal_baru = input(
            "Masukkan tanggal peminjaman yang baru (Contoh: 12/09/2026): "
        )

        waktu_baru = input(
            "Masukkan waktu peminjaman yang baru (Contoh: 13:00): "
        )

        jadwal_bentrok = False

        for data in peminjaman:

            if data[0] != id_peminjaman:

                if (data[2] == kode_ruangan_baru
                        and data[3] == tanggal_baru
                        and data[4] == waktu_baru):

                    jadwal_bentrok = True
                    break

        if jadwal_bentrok:
            print("Maaf, jadwal yang baru sudah digunakan orang lain.")
            continue

        #Mengubah list data ruangan, tanggal, dan waktu peminjaman
        peminjaman[index_data][2] = kode_ruangan_baru
        peminjaman[index_data][3] = tanggal_baru
        peminjaman[index_data][4] = waktu_baru

        print("Data peminjaman berhasil diubah.")
        print("")
        break

#Function untuk membatalkan peminjaman ruangan (Menu 4)
def batalkan_peminjaman(nama_user, role):

    print("========================================")
    print("       BATALKAN PEMINJAMAN RUANGAN")
    print("========================================")

    #Mencari data peminjaman berdasarkan ID
    id_peminjaman = input("Masukkan ID peminjaman yang ingin dibatalkan: ")

    id_ditemukan = False # digunakan untuk menandai apakah ID peminjaman ditemukan atau tidak
    index_data = 0 # digunakan sebagai penanda posisi awal data dalam list.

    #Mencari posisi data yang akan dibatalkan
    for data in peminjaman:
        if data[0] == id_peminjaman:
            id_ditemukan = True
            break

        index_data = index_data + 1 #Digunakan untuk menambah posisi tersebut setiap kali data yang diperiksa belum sesuai, sampai ID yang dicari ditemukan.

    if not id_ditemukan:
        print(f"ID '{id_peminjaman}' tidak ditemukan.")
        return

    ##User hanya dapat mengubah peminjaman miliknya sendiri
    if role == "user":
        if peminjaman[index_data][1] != nama_user:
            print("Anda tidak memiliki hak untuk membatalkan peminjaman ini.")
            return

    #Menghapus data peminjaman dari List berdasarkan posisi datanya
    peminjaman.pop(index_data)

    print("Peminjaman berhasil dibatalkan.")

while True:

    #Memanggil function login untuk meminta username dan password pengguna
    nama_user, role = login()

    #Jika pengguna memilih keluar dari program, maka program akan berhenti
    if nama_user is None:
        print("Program selesai.")
        break

    if role == "admin":

        while True:
            print("========================================")
            print("===============MENU ADMIN===============")
            print("========================================")
            print("1. Lihat Jadwal Peminjaman")
            print("2. Tambah Peminjaman")
            print("3. Ubah Peminjaman")
            print("4. Batalkan Peminjaman")
            print("5. Logout")
            print("")

            try:
                pilihan = int(input("Pilih menu: "))

                if pilihan == 1:
                    print("========================================")
                    print("       JADWAL PEMINJAMAN RUANGAN")
                    print("========================================")

                    #len disini berfungsi untuk menghitung jumlah item atau elemen yang ada di dalam list peminjaman. Jika peminjaman == 0 maka belum ada jadwal yang masuk
                    if len(peminjaman) == 0:
                        print("Belum ada data peminjaman.")
                    else:
                        tabel = PrettyTable()
                        tabel.field_names = ["ID", "Nama", "Ruangan", "Tanggal", "Waktu"]

                        for data in peminjaman:
                            tabel.add_row(data)

                        print(tabel)

                elif pilihan == 2:
                    print("========================================")
                    print("        TAMBAH PEMINJAMAN RUANGAN")
                    print("========================================")

                    while True:
                        id_peminjaman = input(
                            "Masukkan ID peminjaman (Contoh: P001, P002, dst.): "
                        )

                        id_ditemukan = False

                        for data in peminjaman:
                            if data[0] == id_peminjaman:
                                id_ditemukan = True
                                break

                        if id_ditemukan:
                            print(f"ID '{id_peminjaman}' sudah digunakan, silahkan gunakan ID lain.")
                        else:
                            break

                    nama_mahasiswa = input(
                        "Masukkan nama mahasiswa yang ingin meminjam ruangan: "
                    )

                    while True:
                        kode_ruangan = input(
                            "Masukkan kode ruangan yang ingin dipinjam (C401 - C408): "
                        )

                        #Memeriksa apakah ruangan yang dipilih tersedia
                        if kode_ruangan not in ruangan:
                            print(
                                f"Ruangan '{kode_ruangan}' tidak tersedia, "
                                "pilih ulang ruangan C401 - C408."
                            )
                            continue

                        tanggal = input(
                            "Masukkan tanggal peminjaman ruangan (Contoh: 12/09/2026): "
                        )

                        waktu = input(
                            "Masukkan waktu peminjaman ruangan (Contoh: 13:00): "
                        )

                        #Memeriksa apakah jadwal baru sudah digunakan oleh peminjaman lain
                        jadwal_bentrok = False

                        for data in peminjaman:
                            if data[2] == kode_ruangan and data[3] == tanggal and data[4] == waktu:
                                jadwal_bentrok = True
                                break

                        if jadwal_bentrok:
                            print("Maaf, jadwal yang anda pilih sudah digunakan orang lain.")
                        else:
                            break

                    data_baru = [
                        id_peminjaman,
                        nama_mahasiswa,
                        kode_ruangan,
                        tanggal,
                        waktu
                    ]

                    peminjaman.append(data_baru)

                    print("Peminjaman ruangan berhasil ditambahkan.")
                    print("")

                elif pilihan == 3:
                    ubah_peminjaman(nama_user, role)

                elif pilihan == 4:
                    batalkan_peminjaman(nama_user, role)

                elif pilihan == 5:
                    print("Logout berhasil.")
                    print("")
                    break

                else:
                    print("Pilihan menu hanya tersedia 1 sampai 5.")

            except ValueError:
                print("Input harus berupa angka.")

    elif role == "user":

        while True:
            print("========================================")
            print("               MENU USER")
            print("========================================")
            print("1. Lihat Jadwal Peminjaman")
            print("2. Tambah Peminjaman")
            print("3. Ubah Peminjaman")
            print("4. Batalkan Peminjaman")
            print("5. Logout")
            print("========================================")

            try:
                pilihan = int(input("Pilih menu: "))

                if pilihan == 1:
                    print("========================================")
                    print("       JADWAL PEMINJAMAN RUANGAN")
                    print("========================================")

                    if len(peminjaman) == 0:
                        print("Belum ada data peminjaman.")
                        print("")
                    else:
                        print("Berikut adalah jadwal peminjaman ruangan:")
                        tabel = PrettyTable()
                
                        tabel.field_names = ["ID", "Nama", "Ruangan", "Tanggal", "Waktu"]
                
                        for data in peminjaman:
                            tabel.add_row(data)
                
                        print(tabel)

                elif pilihan == 2:
                    print("========================================")
                    print("        TAMBAH PEMINJAMAN RUANGAN")
                    print("========================================")

                    while True:
                        id_peminjaman = input(
                            "Masukkan ID peminjaman (Contoh: P001, P002, dst.): "
                        )

                        id_ditemukan = False

                        for data in peminjaman:
                            if data[0] == id_peminjaman:
                                id_ditemukan = True
                                break

                        if id_ditemukan:
                            print(f"ID '{id_peminjaman}' sudah digunakan, silahkan gunakan ID lain.")
                        else:
                            break

                    nama_mahasiswa = nama_user

                    while True:
                        kode_ruangan = input(
                            "Masukkan kode ruangan yang ingin dipinjam (C401 - C408): "
                        )

                        #Memeriksa apakah ruangan yang dipilih tersedia
                        if kode_ruangan not in ruangan:
                            print(
                                f"Ruangan '{kode_ruangan}' tidak tersedia, "
                                "pilih ulang ruangan C401 - C408."
                            )
                            continue

                        tanggal = input(
                            "Masukkan tanggal peminjaman ruangan (Contoh: 12/09/2026): "
                        )

                        waktu = input(
                            "Masukkan waktu peminjaman ruangan (Contoh: 13:00): "
                        )

                        #Memeriksa apakah jadwal baru sudah digunakan oleh peminjaman lain
                        jadwal_bentrok = False

                        for data in peminjaman:
                            if data[2] == kode_ruangan and data[3] == tanggal and data[4] == waktu:
                                jadwal_bentrok = True
                                break

                        if jadwal_bentrok:
                            print("Maaf, jadwal yang anda pilih sudah digunakan orang lain.")
                        else:
                            break

                    #Membuat list data baru untuk peminjaman
                    data_baru = [
                        id_peminjaman,
                        nama_mahasiswa,
                        kode_ruangan,
                        tanggal,
                        waktu
                    ]

                    #Menambahkan data peminjaman baru ke dalam list peminjaman 
                    peminjaman.append(data_baru)

                    print("Peminjaman ruangan berhasil ditambahkan.")

                #Menu 3 untuk mengubah peminjaman ruangan, memanggil function ubah_peminjaman
                elif pilihan == 3:
                    ubah_peminjaman(nama_user, role)

                #Menu 4 untuk membatalkan peminjaman ruangan, memanggil function batalkan_peminjaman
                elif pilihan == 4:
                    batalkan_peminjaman(nama_user, role)

                #Menu 5 untuk logout dari sistem peminjaman ruangan
                elif pilihan == 5:
                    print("Logout berhasil.")
                    break

                else:
                    print("Pilihan menu hanya tersedia 1 sampai 5.")

            except ValueError:
                print("Input harus berupa angka.")