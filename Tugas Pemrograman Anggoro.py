class DatabaseMahasiswa:
    def __init__(self):
        self.mahasiswa = []

    def input_data(self, nama, nim, prodi, nilai):
        data_mahasiswa = {
            'nama': nama,
            'nim': nim,
            'prodi': prodi,
            'nilai': nilai
        }
        self.mahasiswa.append(data_mahasiswa)

    def tampilkan_data(self):
        if not self.mahasiswa:
            print("Tidak ada data mahasiswa.")
            return
        for mhs in self.mahasiswa:
            print(f"Nama: {mhs['nama']}, NIM: {mhs['nim']}, Prodi: {mhs['prodi']}, Nilai: {mhs['nilai']}")

    def hitung_rata_rata_nilai(self):
        if not self.mahasiswa:
            print("Tidak ada data mahasiswa untuk menghitung rata-rata nilai.")
            return
        total_nilai = sum(mhs['nilai'] for mhs in self.mahasiswa)
        rata_rata_nilai = total_nilai / len(self.mahasiswa)
        print(f"Rata-rata Nilai: {rata_rata_nilai:.2f}")

    def cari_nilai_tertinggi_dan_terendah(self):
        if not self.mahasiswa:
            print("Tidak ada data mahasiswa untuk mencari nilai tertinggi dan terendah.")
            return
        mahasiswa_tertinggi = max(self.mahasiswa, key=lambda x: x['nilai'])
        mahasiswa_terendah = min(self.mahasiswa, key=lambda x: x['nilai'])
        print(f"Mahasiswa dengan nilai tertinggi: {mahasiswa_tertinggi['nama']} - {mahasiswa_tertinggi['nilai']}")
        print(f"Mahasiswa dengan nilai terendah: {mahasiswa_terendah['nama']} - {mahasiswa_terendah['nilai']}")


class InventarisBarang:
    def __init__(self):
        self.barang = []

    def input_data(self, nama_barang, kode_barang, jumlah_barang):
        data_barang = {
            'nama_barang': nama_barang,
            'kode_barang': kode_barang,
            'jumlah_barang': jumlah_barang
        }
        self.barang.append(data_barang)

    def tampilkan_semua_barang(self):
        if not self.barang:
            print("Tidak ada data barang.")
            return
        for brg in self.barang:
            print(f"Nama Barang: {brg['nama_barang']}, Kode Barang: {brg['kode_barang']}, Jumlah Barang: {brg['jumlah_barang']}")

    def cari_barang_berdasarkan_kode(self, kode_barang):
        for brg in self.barang:
            if brg['kode_barang'] == kode_barang:
                print(f"Nama Barang: {brg['nama_barang']}, Kode Barang: {brg['kode_barang']}, Jumlah Barang: {brg['jumlah_barang']}")
                return
        print(f"Barang dengan kode {kode_barang} tidak ditemukan.")

    def hapus_barang_berdasarkan_kode(self, kode_barang):
        for brg in self.barang:
            if brg['kode_barang'] == kode_barang:
                self.barang.remove(brg)
                print(f"Barang dengan kode {kode_barang} telah dihapus.")
                return
        print(f"Barang dengan kode {kode_barang} tidak ditemukan.")


class KeuanganPribadi:
    def __init__(self):
        self.transaksi = []

    def input_transaksi(self, tipe, jumlah, deskripsi):
        transaksi_baru = {
            'tipe': tipe,  # "pemasukan" atau "pengeluaran"
            'jumlah': jumlah,
            'deskripsi': deskripsi
        }
        self.transaksi.append(transaksi_baru)

    def tampilkan_semua_transaksi(self):
        if not self.transaksi:
            print("Tidak ada transaksi.")
            return
        for trx in self.transaksi:
            print(f"Tipe: {trx['tipe']}, Jumlah: {trx['jumlah']}, Deskripsi: {trx['deskripsi']}")

    def hitung_total_pemasukan(self):
        total_pemasukan = sum(trx['jumlah'] for trx in self.transaksi if trx['tipe'] == 'pemasukan')
        print(f"Total Pemasukan: {total_pemasukan}")

    def hitung_total_pengeluaran(self):
        total_pengeluaran = sum(trx['jumlah'] for trx in self.transaksi if trx['tipe'] == 'pengeluaran')
        print(f"Total Pengeluaran: {total_pengeluaran}")

    def hitung_saldo_akhir(self):
        total_pemasukan = sum(trx['jumlah'] for trx in self.transaksi if trx['tipe'] == 'pemasukan')
        total_pengeluaran = sum(trx['jumlah'] for trx in self.transaksi if trx['tipe'] == 'pengeluaran')
        saldo_akhir = total_pemasukan - total_pengeluaran
        print(f"Saldo Akhir: {saldo_akhir}")


def menu():
    db_mahasiswa = DatabaseMahasiswa()
    inv_barang = InventarisBarang()
    keuangan_pribadi = KeuanganPribadi()

    while True:
        print("\nMenu:")
        print("1. Kelola Data Mahasiswa")
        print("2. Kelola Inventaris Barang")
        print("3. Kelola Keuangan Pribadi")
        print("4. Keluar")
        pilihan = input("Pilih menu (1/2/3/4): ")

        if pilihan == '1':
            while True:
                print("\nMenu Mahasiswa:")
                print("1. Input Data Mahasiswa")
                print("2. Tampilkan Data Mahasiswa")
                print("3. Hitung Rata-rata Nilai Mahasiswa")
                print("4. Cari Nilai Tertinggi dan Terendah")
                print("5. Kembali ke Menu Utama")
                pilihan_mahasiswa = input("Pilih menu (1/2/3/4/5): ")

                if pilihan_mahasiswa == '1':
                    nama = input("Nama: ")
                    nim = input("NIM: ")
                    prodi = input("Prodi: ")
                    nilai = float(input("Nilai: "))
                    db_mahasiswa.input_data(nama, nim, prodi, nilai)
                elif pilihan_mahasiswa == '2':
                    db_mahasiswa.tampilkan_data()
                elif pilihan_mahasiswa == '3':
                    db_mahasiswa.hitung_rata_rata_nilai()
                elif pilihan_mahasiswa == '4':
                    db_mahasiswa.cari_nilai_tertinggi_dan_terendah()
                elif pilihan_mahasiswa == '5':
                    break
                else:
                    print("Pilihan tidak valid.")

        elif pilihan == '2':
            while True:
                print("\nMenu Inventaris Barang:")
                print("1. Input Data Barang")
                print("2. Tampilkan Semua Barang")
                print("3. Cari Barang Berdasarkan Kode")
                print("4. Hapus Barang Berdasarkan Kode")
                print("5. Kembali ke Menu Utama")
                pilihan_barang = input("Pilih menu (1/2/3/4/5): ")

                if pilihan_barang == '1':
                    nama_barang = input("Nama Barang: ")
                    kode_barang = input("Kode Barang: ")
                    jumlah_barang = int(input("Jumlah Barang: "))
                    inv_barang.input_data(nama_barang, kode_barang, jumlah_barang)
                elif pilihan_barang == '2':
                    inv_barang.tampilkan_semua_barang()
                elif pilihan_barang == '3':
                    kode_barang = input("Kode Barang: ")
                    inv_barang.cari_barang_berdasarkan_kode(kode_barang)
                elif pilihan_barang == '4':
                    kode_barang = input("Kode Barang: ")
                    inv_barang.hapus_barang_berdasarkan_kode(kode_barang)
                elif pilihan_barang == '5':
                    break
                else:
                    print("Pilihan tidak valid.")

        elif pilihan == '3':
            while True:
                print("\nMenu Keuangan Pribadi:")
                print("1. Input Transaksi")
                print("2. Tampilkan Semua Transaksi")
                print("3. Hitung Total Pemasukan")
                print("4. Hitung Total Pengeluaran")
                print("5. Hitung Saldo Akhir")
                print("6. Kembali ke Menu Utama")
                pilihan_keuangan = input("Pilih menu (1/2/3/4/5/6): ")

                if pilihan_keuangan == '1':
                    tipe = input("Tipe (pemasukan/pengeluaran): ")
                    jumlah = float(input("Jumlah: "))
                    deskripsi = input("Deskripsi: ")
                    keuangan_pribadi.input_transaksi(tipe, jumlah, deskripsi)
                elif pilihan_keuangan == '2':
                    keuangan_pribadi.tampilkan_semua_transaksi()
                elif pilihan_keuangan == '3':
                    keuangan_pribadi.hitung_total_pemasukan()
                elif pilihan_keuangan == '4':
                    keuangan_pribadi.hitung_total_pengeluaran()
                elif pilihan_keuangan == '5':
                    keuangan_pribadi.hitung_saldo_akhir()
                elif pilihan_keuangan == '6':
                    break
                else:
                    print("Pilihan tidak valid.")

        elif pilihan == '4':
            print("Terima kasih telah menggunakan program ini.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    menu()
