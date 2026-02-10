def tampilkan_menu(nama_pembeli):
    print("==============================")
    print(f"Selamat Datang di Bioskop XXI, {nama_pembeli}")
    print("Silahkan Pilih Menu Di bawah")
    print("1. Reguler   :   35000")
    print("2. VIP       :   50000")
    print("3. Couple    :   90000")
    print("4. 3D        :   60000")
    print("5. Selesai")
    pilihan = input("Silahkan pilih menu dari (1-5): ")
    print("==============================")
    return pilihan
def main():
    harga_tiket = {
        "1" : 35000,
        "2" : 50000,
        "3" : 90000,
        "4" : 60000
    }
    nama_pembeli = input("Masukkan Nama Anda : ")
    total_harga = 0
    while True:
        pilihan = tampilkan_menu(nama_pembeli)
        if pilihan in ["1", "2", "3", "4"]: #harga_tiket.keys()
            jumlah_tiket = int(input("Masukkan jumlah tiket yang ingin dibeli: "))
            total_harga += harga_tiket[pilihan] * jumlah_tiket
            print(f"Tiket berhasil ditambahkan. Total harga sementara: Rp {total_harga}")
        elif pilihan == "5":
            print(f"Total harga yang harus dibayar: Rp {total_harga}")
            pembayaran = int(input("Masukkan jumlah pembayar  an: Rp "))
            if pembayaran >= total_harga:
                kembalian = pembayaran - total_harga
                print(f"Pembayaran berhasil. Kembalian Anda: Rp {kembalian}")
            else:
                print("Maaf, pembayaran Anda kurang.")
            break
        else:
            print("Pilihan tidak valid, silahkan coba lagi.")
if __name__ == "__main__":
    main()

