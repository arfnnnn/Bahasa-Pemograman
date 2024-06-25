def pencarian_biner(database, nama_vaksin):
    """
    Fungsi untuk melakukan Pencarian Biner pada database vaksin yang sudah diurutkan.
    
    Parameter:
    database (list): Daftar yang berisi informasi vaksin yang sudah diurutkan berdasarkan nama.
    nama_vaksin (str): Nama vaksin yang dicari.
    
    Mengembalikan:
    int: Indeks elemen jika ditemukan, jika tidak -1.
    """
    rendah = 0
    tinggi = len(database) - 1

    while rendah <= tinggi:
        tengah = (rendah + tinggi) // 2
        vaksin_tengah = database[tengah]['nama']

        # Jika nama vaksin di tengah sama dengan nama_vaksin yang dicari
        if vaksin_tengah == nama_vaksin:
            return tengah

        # Jika nama vaksin di tengah lebih kecil dari nama_vaksin yang dicari, abaikan bagian kiri
        elif vaksin_tengah < nama_vaksin:
            rendah = tengah + 1

        # Jika nama vaksin di tengah lebih besar dari nama_vaksin yang dicari, abaikan bagian kanan
        else:
            tinggi = tengah - 1

    # Jika kita sampai di sini, berarti vaksin tidak ditemukan
    return -1

def tambah_vaksin(database, nama, produsen, efikasi):
    """
    Fungsi untuk menambahkan vaksin baru ke database.
    
    Parameter:
    database (list): Daftar yang berisi informasi vaksin.
    nama (str): Nama vaksin.
    produsen (str): Produsen vaksin.
    efikasi (int): Efikasi vaksin.
    """
    database.append({'nama': nama, 'produsen': produsen, 'efikasi': efikasi})
    # Mengurutkan database setelah penambahan
    database.sort(key=lambda x: x['nama'])
    print("Vaksin berhasil ditambahkan!")

def hapus_vaksin(database, nama_vaksin):
    """
    Fungsi untuk menghapus vaksin dari database.
    
    Parameter:
    database (list): Daftar yang berisi informasi vaksin.
    nama_vaksin (str): Nama vaksin yang akan dihapus.
    """
    indeks = pencarian_biner(database, nama_vaksin)
    if indeks != -1:
        del database[indeks]
        print("Vaksin berhasil dihapus!")
    else:
        print("Vaksin tidak ditemukan dalam database.")

def tampilkan_menu():
    """
    Fungsi untuk menampilkan menu pilihan.
    """
    print("\nMenu:")
    print("1. Cari Vaksin")
    print("2. Tambah Vaksin")
    print("3. Hapus Vaksin")
    print("4. Tampilkan Database")
    print("5. Keluar")

# Contoh database vaksin
database_vaksin = [
    {'nama': 'Vaksin A', 'produsen': 'Produsen 1', 'efikasi': 90},
    {'nama': 'Vaksin B', 'produsen': 'Produsen 2', 'efikasi': 85},
    {'nama': 'Vaksin C', 'produsen': 'Produsen 3', 'efikasi': 80},
]

# Mengurutkan database vaksin berdasarkan nama sebelum pencarian biner
database_vaksin.sort(key=lambda x: x['nama'])

# Program utama
while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (1-5): ")
    
    if pilihan == '1':
        nama_vaksin_dicari = input("Masukkan nama vaksin yang dicari: ")
        indeks = pencarian_biner(database_vaksin, nama_vaksin_dicari)
        if indeks != -1:
            print(f"Vaksin ditemukan pada indeks {indeks}: {database_vaksin[indeks]}")
        else:
            print("Vaksin tidak ditemukan dalam database")
    
    elif pilihan == '2':
        nama = input("Masukkan nama vaksin: ")
        produsen = input("Masukkan produsen vaksin: ")
        efikasi = int(input("Masukkan efikasi vaksin: "))
        tambah_vaksin(database_vaksin, nama, produsen, efikasi)
    
    elif pilihan == '3':
        nama_vaksin_dicari = input("Masukkan nama vaksin yang akan dihapus: ")
        hapus_vaksin(database_vaksin, nama_vaksin_dicari)
    
    elif pilihan == '4':
        print("Database Vaksin:")
        for vaksin in database_vaksin:
            print(vaksin)
    
    elif pilihan == '5':
        print("Keluar dari program.")
        break
    
    else:
        print("Pilihan tidak valid. Silakan pilih menu (1-5).")
