class AntrianPasien:
    def init(self):
        self.antrian = []

    def tambah_pasien(self, nama):
        self.antrian.append(nama)
        print(f"Pasien {nama} telah ditambahkan ke antrian.")

    def proses_pasien(self):
        if self.antrian:
            pasien = self.antrian.pop(0)
            print(f"Memproses pasien: {pasien}")
        else:
            print("Tidak ada pasien dalam antrian.")

    def tampilkan_antrian(self):
        if self.antrian:
            print("Antrian Pasien saat ini:")
            for i, pasien in enumerate(self.antrian, start=1):
                print(f"{i}. {pasien}")
        else:
            print("Antrian kosong.")

def main():
    sistem_antrian = AntrianPasien()

    while True:
        print("\nSistem Manajemen Antrian Pasien Klinik")
        print("1. Tambah Pasien")
        print("2. Proses Pasien")
        print("3. Tampilkan Antrian")
        print("4. Keluar")
        
        pilihan = input("Pilih opsi (1-4): ")

        if pilihan == '1':
            nama_pasien = input("Masukkan nama pasien: ")
            sistem_antrian.tambah_pasien(nama_pasien)
        elif pilihan == '2':
            sistem_antrian.proses_pasien()
        elif pilihan == '3':
            sistem_antrian.tampilkan_antrian()
        elif pilihan == '4':
            print("Keluar dari sistem.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if _name_ == "_main_":
    main()
