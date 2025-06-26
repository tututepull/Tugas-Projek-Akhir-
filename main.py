from modul_mahasiswa import *

def menu():
    while True:
        print("\n=== Aplikasi Data Mahasiswa ===")
        print("1. Tambah data mahasiswa")
        print("2. Tampilkan data mahasiswa")
        print("3. Hapus data mahasiswa")
        print("4. Perbarui data mahasiswa")
        print("5. Keluar")
        pilihan = input("Masukkan pilihan (1-5): ")

        if pilihan == '1':
            tambah_data_mahasiswa()
        elif pilihan == '2':
            tampilkan_data_mahasiswa()
        elif pilihan == '3':
            hapus_data_mahasiswa()
        elif pilihan == '4':
            perbarui_data_mahasiswa()
        elif pilihan == '5':
            print("Keluar dari aplikasi.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    menu()
