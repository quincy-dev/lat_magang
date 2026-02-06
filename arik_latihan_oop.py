#soal 1
class Buah: 
    nama = "apel" 
    warna = "merah" 

Buah1 = Buah()
Buah2 = Buah()
    
print(Buah1.nama) 
print(Buah1.warna)

print("-----")
#soal 2
class Laptop:
    def __init__(self, merk, ram, harga):
        self.merk = merk
        self.ram = ram
        self.harga = harga

laptop1 = Laptop("Asus", "8GB", 8000000)
laptop2 = Laptop("Acer", "16GB", 12000000)

print(laptop1.merk, laptop1.ram, laptop1.harga)
print(laptop2.merk, laptop2.ram, laptop2.harga)

print("-----")
#soal 3
class KipasAngin:
    def __init__(self, kecepatan=0):
        self.kecepatan = kecepatan

    def nyala(self):
        self.kecepatan += 1
        print(f"Kipas angin menyala dengan kecepatan {self.kecepatan}")

    def mati(self):
        self.kecepatan = 0
        print("Kipas angin mati")

kipas = KipasAngin()
kipas.nyala()
kipas.mati()

print("-----")
#soal 4
class Manusia:
    def berbicara(self, kata):
        print(f"Manusia berkata: {kata}")

orang = Manusia()
orang.berbicara("Halo, apa kabar?")

print("-----")
#soal 5
class AkunGame:
    def __init__(self, username, level):
        self.username = username
        self.level = level

    def naik_level(self):
        self.level += 1
        print(f"{self.username} naik ke level {self.level}")

akun1 = AkunGame("PlayerOne", 5)
akun1.naik_level()

print("-----")
#soal 6
class Dompet:
    def __init__(self, uang):
        self.__uang = uang  

    def lihat_uang(self):
        print(f"Uang dalam dompet: {self.__uang}")
    
    def tambah_uang(self, jumlah):
        self.__uang += jumlah
        print(f"Uang ditambah sebesar {jumlah}. Total uang sekarang: {self.__uang}")

    def kurangi_uang(self, jumlah):
        if jumlah > self.__uang:
            print("Uang tidak cukup!")
        else:
            self.__uang -= jumlah
            print(f"Uang dikurangi sebesar {jumlah}. Total uang sekarang: {self.__uang}")

dompet_saya = Dompet(100000)
dompet_saya.lihat_uang()
dompet_saya.tambah_uang(50000)
dompet_saya.kurangi_uang(30000)

print("-----")
#soal 7
class Dompet:
    def __init__(self, uang):
        self.__uang = uang  

    def lihat_uang(self):
        print(f"Uang dalam dompet: {self.__uang}")
    
    def tambah_uang(self, jumlah):
        self.__uang += jumlah
        print(f"Uang ditambah sebesar {jumlah}. Total uang sekarang: {self.__uang}")

    def kurangi_uang(self, jumlah):
        if jumlah > self.__uang:
            print("Uang tidak cukup!")
        else:
            self.__uang -= jumlah
            print(f"Uang dikurangi sebesar {jumlah}. Total uang sekarang: {self.__uang}")

    def get_uang(self):
        return self.__uang
    def set_uang(self, uang):
        self.__uang = uang


dompet_saya = Dompet(100000)
# dompet_saya.lihat_uang()
# dompet_saya.tambah_uang(50000)
# dompet_saya.kurangi_uang(30000)
dompet_saya.set_uang(200000)
print(dompet_saya.get_uang())

print("-----")
#soal 8 
class Kendaraan:
    def jalan(self):
        print("Kendaraan berjalan")

class Motor(Kendaraan):
    def roda_dua(self):
        print("Motor dengan dua roda")

class Mobil(Kendaraan):
    def roda_empat(self):
        print("Mobil dengan empat roda")

motor_saya = Motor()
motor_saya.jalan()
motor_saya.roda_dua()
mobil_saya = Mobil()
mobil_saya.jalan()
mobil_saya.roda_empat()


print("-----")
#soal 9
class Pegawai:
    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji

class Manager(Pegawai):
    def bonus(self, jumlah_bonus):
        total_gaji = self.gaji + jumlah_bonus
        print(f"Total gaji Manager {self.nama} setelah bonus adalah {total_gaji}")

manager1 = Manager("Budi", 10000000)
manager1.bonus(2000000)

print("-----")
#soal 10
class Burung:
    def suara(self):
        print("Suara burung")
class Ayam(Burung):
    def suara(self):
        print("Petok petok")
class Bebek(Burung):
    def suara(self):
        print("Kwek kwek")

ayam1 = Ayam()
ayam1.suara()
bebek1 = Bebek()
bebek1.suara()

print("-----")
#soal 11
class Hewan:
    def suara(self):
        pass

class Ayam(Hewan):
    def suara(self):
        print("Petok petok")
class Bebek(Hewan):
    def suara(self):
        print("Kwek kwek")

hewan_list = [Ayam(), Bebek()]

for hewan in hewan_list:
    hewan.suara()

print("-----")
#soal 12
class Barang:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga


class Toko:
    def __init__(self):
        self.daftar_barang = []

    def tambah_barang(self, barang):
        self.daftar_barang.append(barang)
        print(f"{barang.nama} ditambahkan ke keranjang")

    def hitung_total(self):
        total = 0
        for barang in self.daftar_barang:
            total += barang.harga
        print(f"Total harga: {total}")

toko = Toko()

b1 = Barang("Baju", 150000)
b2 = Barang("Celana", 200000)

toko.tambah_barang(b1)
toko.tambah_barang(b2)
toko.hitung_total()


print("-----")
#soal 13
class Kendaraan:
    def __init__(self, plat, jenis):
        self.plat = plat
        self.jenis = jenis

class Parkiran:
    def __init__(self):
        self.biaya_parkir = 0

    def hitung_biaya(self, kendaraan: Kendaraan, jam_parkir):
        if kendaraan.jenis == "mobil":
            self.biaya_parkir = jam_parkir * 5000
        elif kendaraan.jenis == "motor":
            self.biaya_parkir = jam_parkir * 2000
        print(f"Biaya parkir untuk {kendaraan.jenis} dengan plat {kendaraan.plat} selama {jam_parkir} jam adalah {self.biaya_parkir}")

kendaraan1 = Kendaraan("AA 5144 PP", "mobil")
parkiran_saya = Parkiran()
parkiran_saya.hitung_biaya(kendaraan1, 3)

print("-----")
#soal 14
class Siswa:
    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai

    def lulus(self):
        if self.nilai >= 75:
            print(f"{self.nama} lulus dengan nilai {self.nilai}")
        else:
            print(f"{self.nama} tidak lulus dengan nilai {self.nilai}")

siswa1 = Siswa("Andi", 80)
siswa1.lulus()
siswa2 = Siswa("Budi", 65)
siswa2.lulus()

print("-----")
#soal 15
class Rekening:
    def __init__(self, saldo):
        self.__saldo = saldo  

    def setor(self, jumlah):
        self.__saldo += jumlah
        print(f"Saldo ditambah sebesar {jumlah}. Total saldo sekarang: {self.__saldo}")

    def tarik(self, jumlah):
        if jumlah > self.__saldo:
            print("Saldo tidak cukup!")
        else:
            self.__saldo -= jumlah
            print(f"Saldo dikurangi sebesar {jumlah}. Total saldo sekarang: {self.__saldo}")

    def get_saldo(self):
        return self.__saldo
    
rekening_saya = Rekening(500000)
rekening_saya.setor(200000)
rekening_saya.tarik(100000)
print(rekening_saya.get_saldo())

print("-----")
#soal 16  
class Shape:
    def luas(self):
        pass

class Persegi(Shape):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi * self.sisi
    
class Lingkaran(Shape):
    def __init__(self, radius):
        self.radius = radius

    def luas(self):
        return 3.14 * self.radius * self.radius
    
persegi1 = Persegi(4)
print(f"Luas persegi: {persegi1.luas()}")
lingkaran1 = Lingkaran(7)
print(f"Luas lingkaran: {lingkaran1.luas()}")

print("-----")
#soal 17
class Hewan:
    def bergerak(self):
        pass

class Ikan(Hewan):
    def bergerak(self):
        print("Ikan berenang di air")

class Burung(Hewan):
    def bergerak(self):
        print("Burung terbang di udara")

class Kucing(Hewan):
    def bergerak(self):
        print("Kucing berjalan di darat")
ikan1 = Ikan()
ikan1.bergerak()
burung1 = Burung()
burung1.bergerak()
kucing1 = Kucing()
kucing1.bergerak()

print("-----")
#soal 18
class Produk:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

class Kasir:
    def __init__(self):
        self.total = 0

    def tambah_produk(self, produk: Produk):
        self.total += produk.harga
        print(f"{produk.nama} ditambahkan")

    def bayar(self, uang):
        if uang >= self.total:
            print(f"Kembalian: {uang - self.total}")
        else:
            print("Uang tidak cukup")

produk1 = Produk("Sabun", 15000)
kasir = Kasir()
kasir.tambah_produk(produk1)
kasir.bayar(20000)

print("-----")
#soal 19 
class User:
    def __init__(self, nama):
        self.nama = nama

    def login(self):
        print(f"{self.nama} telah login")

class Admin(User):
    def hapus_user(self, user):
        print(f"Admin {self.nama} menghapus user {user.nama}")

class Member(User):
    def beli_produk(self, produk):
        print(f"Member {self.nama} membeli produk {produk}")

admin1 = Admin("Budi")
admin1.login()
admin1.hapus_user(Member("Andi"))
member1 = Member("Andi")
member1.login()
member1.beli_produk("Laptop")

print("-----")
#soal 20
class Buku:
    def __init__(self, judul, stok):
        self.judul = judul
        self.stok = stok

class Perpustakaan:
    def __init__(self):
        self.daftar_buku = []

    def tambah_buku(self, buku):
        self.daftar_buku.append(buku)
        print(f"Buku '{buku.judul}' berhasil ditambahkan")

    def pinjam_buku(self, judul):
        for buku in self.daftar_buku:
            if buku.judul == judul:
                if buku.stok > 0:
                    buku.stok -= 1
                    print(f"Berhasil meminjam buku '{judul}'")
                else:
                    print(f"Stok buku '{judul}' habis")
                return
        print(f"Buku '{judul}' tidak ditemukan")

    def tampilkan_buku(self):
        print("Daftar Buku:")
        for buku in self.daftar_buku:
            print(f"- {buku.judul} (Stok: {buku.stok})")

perpus = Perpustakaan()

buku1 = Buku("Python Dasar", 3)
buku2 = Buku("Algoritma", 2)

perpus.tambah_buku(buku1)
perpus.tambah_buku(buku2)

perpus.tampilkan_buku()

perpus.pinjam_buku("Python Dasar")
perpus.tampilkan_buku()












