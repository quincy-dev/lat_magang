from time import sleep

#fungsi void
def say_no(name):
    print(f"Hello {name}, How are you?")
say_no("yolo")

# print("\n")

#fungsi return
def hitung(a,b):
    return a + b
n1 = 3
n2 = 8

# print(hitung(n1,n2))

print("\n")

#fungsi default parameter
def hberat(kardus,kertas = 12):
    return kardus + kertas
# print(hberat(21,))

print("\n")

#fungsi recursive
# def hitungm(n):
#     if n == 0:
#         return
    
#     print(f"hitung mundur {n}")
#     sleep(1)
#     hitungm(n - 1)

# hitungm(5)




print("\n")
def say_goodbye(nama):
    print(f"Goodbye {nama}, see you again!")
say_goodbye("agus")

print("\n")
def info_siswa():
    namas = input('Masukkan nama anda : ')
    jurusan = input('Masukkan jurusan anda : ')
    print(f"nama siswa {namas}\njurusan {jurusan}")

info_siswa()