# 1 OOP (Object Oriented Programming) adalah cara menulis program
# dengan merepresentasikan dunia nyata ke dalam bentuk OBJECT

# Contoh dunia nyata:
# Mobil -> punya warna, merk, kecepatan -> attribute
# Mobil -> bisa jalan, bisa berhenti -> function / method

# 2 Class & Object
# CLASS adalah blueprint / cetakan
# OBJECT adalah hasil dari class tersebut -> intansiasi dari sebuah class

# class Mobil:
#     # attribute / properti
#     warna = "Hitam"
#     merk = "Toyota"

# # Membuat object dari class
# mobil_1 = Mobil()
# mobil_2 = Mobil()

# mobil_1.warna = "Putih"
# print(mobil_1.warna)
# print(mobil_2.warna)

# class User:
#     username = "hhhhh"
#     password = "hhhhh"
#     email = "hhhh@gmail.com"
#     is_role = "user"

# # admin itu bisa bla bla bla
# admin = User()
# admin.is_role = "admin"

# # budi itu bisa nnnnn
# budi = User()

# 3 Constructor adalah function yang otomatis dipanggil
# saat object dibuat

# class Mobil2:
#     def __init__(self, warna, merk, size_big=0): 
#         self.warna = warna   # self menunjuk ke object itu sendiri
#         self.merk = merk # Mobil2.merk = merk

# mobil_1 = Mobil2(merk="Honda", warna="Merah")
# mobil_2 = Mobil2("Hitam", "Toyota")

# print(mobil_1.warna, mobil_1.merk)
# print(mobil_2.warna, mobil_2.merk)

#4 method (function class) 
# class Mobil3:
#     def __init__(self, merk):
#         # Attribute / Property -> data
#         self.merk = merk
#         self.kecepatan = 0

#     # Method / Func -> sifat/perilaku
#     def gas(self):
#         self.kecepatan += 10
#         print(f"Mobil {self.merk} melaju {self.kecepatan} km/jam")

#     def rem(self):
#         self.kecepatan -= 5
#         print(f"Mobil {self.merk} melambat {self.kecepatan} km/jam")

# mobil = Mobil3("Suzuki")
# mobil.gas()
# mobil.gas()
# mobil.rem()


# Ada Class Hewan -> harus ada constructor
# Hewan itu punya nama, kecepatan, wilayah (darat, air)
# Hewan bisa bersuara (by parameter)

# class Hewan:
#     def __init__(self, nama, kecepatan, wilayah="Darat"):
#         self.nama = nama
#         self.kecepatan = kecepatan
#         self.wilayah = wilayah
    
#     def bersuara(self, suara):
#         print(f"Suara dari {self.nama} : {suara}")
        
# hewan1 = Hewan('Kucing', 10)
# hewan2 = Hewan('Ikan', 8, "Air")

# hewan1.bersuara('Meong Meong')
# hewan2.bersuara('Shh shh')













# 5 Attribute and method
# Attribute -> data / sifat
# Method -> aksi / perilaku

# class User2:
#     def __init__(self, username):
#         self.username = username  # attribute

#     def login(self):             # method
#         print(f"{self.username} berhasil login")

# user = User2("admin")
# user.login()








# 6 Encapsulation = membatasi akses data (Public, Private)

# class AkunBank:
#     def __init__(self, saldo):
#         self.__saldo = saldo  # private attribute __ -> Underscore 2x

#     def lihat_saldo(self):
#         print(f"Saldo anda: {self.__saldo}")

#     def tarik_uang(self, jumlah):
#         if jumlah <= self.__saldo:
#             self.__saldo -= jumlah
#             print("Penarikan berhasil")
#         else:
#             print("Saldo tidak cukup")
            
#     # Getter and Setter
#     def get_saldo(self): # Getter -> Function Return Value
#         return self.__saldo
    
#     def set_saldo(self, saldo): # Setter -> Function Void
#         self.__saldo = saldo

# akun = AkunBank(100000)
# # akun.lihat_saldo()
# # akun.tarik_uang(30000)
# # akun.lihat_saldo()
# akun.set_saldo(25000)
# print(akun.get_saldo())


















# 7 Inheritance = class anak mewarisi class induk -> Pewarisan

# class User:
#     def __init__(self, name):
#         self.name = name

#     def login(self):
#         print(f"{self.name} login")
    
#     def logout(self):
#         print(f"{self.name} telah keluar")

# class Admin(User):
#     # Method Tambahan / Method Yang Hanya Dipunya Oleh Anaknya (Walaupun ada method induknya)
#     def delete_user(self):
#         print("User dihapus oleh admin")

# admin = Admin("Budi")
# admin.login()          # method dari parent
# admin.logout()          # method dari parent
# admin.delete_user()    # method dari child

# admin2 = User("Anita")
# admin2.login()
# admin2.logout()











# 8 Polymorphism (Method sama perilaku beda) / Method overriding
# class Hewan:
#     def bersuara(self):
#         print("Hewan bersuara")

# class Kucing(Hewan): # Pewarisan -> Inheritance
#     def bersuara(self):
#         print("Meong")

# class Anjing(Hewan):
#     def bersuara(self):
#         print("Guk guk")

# hewan = [Kucing(), Anjing()]

# for h in hewan:
#     h.bersuara() # karena method bersuara itu telah di timpa oleh method bersuara childnya




# Studi kasus
class Produk:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga
        
class SabunMandi(Produk):
    def tampilkan_harga(self):
        print(f"Harga sabun {self.harga + 10000}")

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

nasi = Produk("Nasi", 5000)
sabunm = SabunMandi("Sabun Mandi", nasi.harga)
kasir = Kasir()

kasir.tambah_produk(sabunm)
kasir.bayar(10000)