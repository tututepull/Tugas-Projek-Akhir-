data_mahasiswa = {
    'Fathir Arrofi': '20240040272',
    'Asep Rohmat': '20240040273',
    'Ilyas Nazma': '20240040274',
    'Alief Hazel': '20240040275',
}

def tambah_data_mahasiswa():
    print("Menambahkan data mahasiswa")
    nama = input("Masukkan nama mahasiswa: ")
    nim = input("Masukkan NIM mahasiswa: ")
    data_mahasiswa[nama] = nim
    print(f"Data mahasiswa {nama} dengan NIM {nim} telah ditambahkan.")
    tampilkan_data_mahasiswa()

def tampilkan_data_mahasiswa():
    if not data_mahasiswa:
        print("Tidak ada data mahasiswa yang tersedia.")
    else:
        print("=== Data Mahasiswa ===")
        for nama, nim in data_mahasiswa.items():
            print(f"Nama: {nama}, NIM: {nim}")

def hapus_data_mahasiswa():
    print("Menghapus data mahasiswa")
    nama = input("Masukkan nama mahasiswa yang ingin dihapus: ")
    if nama in data_mahasiswa:
        del data_mahasiswa[nama]
        print(f"Data mahasiswa {nama} telah dihapus.")
    else:
        print(f"Data mahasiswa {nama} tidak ditemukan.")

def perbarui_data_mahasiswa():
    print("Memperbarui data mahasiswa")
    nama = input("Masukkan nama mahasiswa yang ingin diperbarui: ")
    if nama in data_mahasiswa:
        nim = input("Masukkan NIM baru: ")
        data_mahasiswa[nama] = nim
        print(f"Data mahasiswa {nama} telah diperbarui dengan NIM {nim}.")
    else:
        print(f"Data mahasiswa {nama} tidak ditemukan.")
