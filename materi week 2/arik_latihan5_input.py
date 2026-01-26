#soal 1
def cetak_sapaan(nama: str):
    print(f"Halo, {nama}! Selamat datang!")
nama_user = input("Masukkan nama Anda: ")
cetak_sapaan(nama_user)

print("\n")

#soal 2
def hitung_usia_lahir(tahun_lahir):
    usia = 2025 - tahun_lahir
    return usia
tahun_lahir = int(input("Masukkan Tahun Lahir Anda : "))
hasil = hitung_usia_lahir(tahun_lahir)
print(f"Usia kamu adalah : ", hasil)

print("\n")

#soal 3
def info_paket(nama_paket, durasi=30):
    print("Nama Paket :", nama_paket)
    print("Durasi     :", durasi, "hari")

info_paket("Internet Bulanan")

print("\n")

#soal 4
nilai_ujian = []
for i in range(5):
    nilai = int(input(f"Masukkan nilai ujian ke -{i+1}: "))
    nilai_ujian.append(nilai)
def cetak_nilai(nilai_list):
    print("Nilai Ujian:")
    for nilai in nilai_list:
        print(nilai)
cetak_nilai(nilai_ujian)

print("\n")

#soal 5
def hitung_rata_rata(nilai_list):
    return sum(nilai_list) / len(nilai_list)
rata_rata = hitung_rata_rata(nilai_ujian)
print(f"Rata-rata nilai ujian adalah: {rata_rata}")

print("\n")

#soal 6
def hitung_lulus(nilai_list):
    count = 0
    for nilai in nilai_list:
        if nilai >= 60:
            count += 1
    return count
lulus_count = hitung_lulus(nilai_ujian)
print(f"Jumlah nilai lulus (>=60): {lulus_count}")

print("\n")

#soal 7
nama_siswa = []
for name in range(5):
    nama = input(f"Masukkan Naman Siswa ke - {name+1}:")
    nama_siswa.append(nama)
def cetak_nama(nama_list):
    print("Nama Siswa:")
    for nama in nama_list:
        print(nama)
cetak_nama(nama_siswa)

print("\n")

#soal 8
def hitung_total(harga, pajak=0.10):
    total = harga + (pajak * harga)
    return total
harga_barang = float(input("Masukkan harga barang: "))
total_harga = hitung_total(harga_barang)
print(f"Total harga setelah pajak: {total_harga}")

print("\n")

#soal 9
def tampilkan_menu():
    print("Menu:")
    print("1. Lihat Profil")
    print("2. Hitung Usia")
    print("3. Keluar")
def pilih_menu():
    pilihan = input("Pilih menu (1-3): ")
    return pilihan
tampilkan_menu()
menu_terpilih = pilih_menu()
print(f"Menu yang dipilih: {menu_terpilih}")

print("\n")

#soal 10
def pendataan_nilai():
    niai_siswa = []
    jumlah_siswa = int(input("Masukkan jumlah siswa: "))
    for jumlah in range(jumlah_siswa):
        nilai = int(input(f"Masukkan nilai siswa ke - {jumlah+1}: "))
        niai_siswa.append(nilai)
    return niai_siswa
def hitung_rata_rata(nilai_list):
    return sum(nilai_list) / len(nilai_list)
def hitung_lulus(nilai_list):
    count = 0
    for nilai in nilai_list:
        if nilai >= 60:
            count += 1
    return count
nilai_siswa = pendataan_nilai()
rata_rata_siswa = hitung_rata_rata(nilai_siswa)
jumlah_lulus = hitung_lulus(nilai_siswa)
print(f"Rata-rata nilai siswa: {rata_rata_siswa}")
print(f"Jumlah siswa lulus (>=60): {jumlah_lulus}")
