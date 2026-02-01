def say_tamu(name):
    print(f"Nama tamu yang sudah hadir : {name}")

def nama_tamu_kapital(name: str):
    if name.upper().startswith("F"):
        print("Ini huruf nya F diawal")
    else:
        print("Tanpa f huruf awalnya")

def pertambahan(a,b):
    return a+b

# print("Sambut tamu")
# nama_tamu = input("Nama tamu anda : ")

# nama_tamu_kapital(nama_tamu)

print("Hitung dong")
a = input("Masukan angka pertama: ")
b = input("Masukan angka kedua: ")


print(pertambahan(int(a), int(b)))

