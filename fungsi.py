from time import sleep

# Function / Method
# Function / Method adalah sebuah ringkasan dari fungsionalitas yang dapat dipanggil atau dipakai
# Bisa dibilang function itu untuk menghindari duplikasi kode

# 1. Function Void (Fungsi yang tidak mengembalikan apapun)
def say_hello(name):
    print(f"Hello {name}, How are you?")

# say_hello("Budi")

# 2. Function Return (Fungsi yang mengembalikan nilai)
def hitung_kalkulasi(a: int, b: int): # a dan b adalah parameter / argument
    return a + b

nilai_1 = 1
nilai_2 = 2

# print(hitung_kalkulasi(nilai_1, nilai_2))


# 3. Function With Default Parameter (Fungsi yang punya default parameter)
# jika parameter tidak diisi maka fungsi tetap bisa dijalankan
def say_welcome(age, name = "Anonim"): # Default Parameter / Argument
    print(f"Welcome {name} - age : {age}, How are you?")

# say_welcome(12, "Agung")

def hitung_berat(mobil, motor = 10):
    return mobil + motor

# print(hitung_berat(10, 32))



# 4. Recursive Function (Fungsi yang dapat memanggil dirinya sendiri)
def hitungin(n: int):
    if n == 1:
        return
    
    print(f"Hitung mundur ke - {n-1}")
    sleep(1)
    hitungin(n-1)

# def hitungin2(n: int):
#     while n > 0:
#         print(f"Hitung mundur ke - {n-1}")
#         sleep(1)
#         n -= 1

# hitungin(10)

# Simulasi 1
# print("Hitung mundur ke - 9")
# hitungin(9)

# Simulasi 2
# print("Hitung mundur ke - 8")
# hitungin(8)

# Faktorial, misal 5! = 5x4x3x2x1
def faktorial(n):
    if n == 1:
        return 1
    return n * faktorial(n - 1) # misal 5
    # 5 * (4 * (3 * (2 * (1 * 1))))
    
def faktorial_loop(n): # misal n = 5
    hasil = n # 5
    while n > 0:
        print(f"Antrian saat ini - {n}")
        if (n - 1) > 0:
            hasil *= (n - 1)
        
        n -= 1
        
    return hasil

# num = input("Angka mundur yang kamu inginkan : ")
# hitung_mundur(int(num))

num = input("Berikan angka faktorial : ")
res = faktorial_loop(int(num))
print(f"Faktorial dari {num} adalah : {res}")
