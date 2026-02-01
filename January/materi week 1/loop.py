## Operator Logika
# <=    -->  Kurang dari dan sama dengan 
# <     -->  Kurang dari
# >     -->  Lebih dari
# >=    -->  Lebih dari dan sama dengan
# ==    -->  Dua parameter / argumen harus memiliki kesamaan contoh : 2 == 2
# !=    -->  Dua parameter / argumen harus memiliki ketidaksamaan contoh : 2 != 3
# !     -->  Negasi : Ketika sebuah parameter / argumen itu harus dibalikkan fakta atau keadaannya
# contoh negasi : 2 + 2 == 4 : True, !2+2 == 4 : False

## DAN -> && -> Jika suatu kondisi salah satunya False atau salah maka hasilnya pasti salah(FALSE)
# Fakta : Budi makan mangga (true)
# Soal : Budi makan mangga (true) DAN Budi tidak makan mangga (false)
# Kesimpulan : Budi tidak makan mangga (false)

## ATAU -> || -> jika ada salah satu kondisi benar maka kondisi akhirnya pasti benar (TRUE)
# Fakta : Budi makan mangga (true)
# Soal : Budi makan mangga (true) ATAU Budi tidak makan mangga (false) 
# Kesimpulan : Budi makan mangga (true)

## Soal
# fakta : putri tidak bisa terbang (false)
# soal : putri tidak bisa terbang (false) || putri tidak bisa terbang (false)
# Kesimpulan : Putri tidak bisa terbang (false)
# alesannya : Karena kedua argumen itu sifatnya salah (false) dengan aturan 'ATAU' jika salah satu argumen ada yang benar maka hasilnya benar, dalam soal kedua argumen itu salah (false), maka hasilnya salah (false)

# B = Benar
# S = Salah

## && -> 
# B = B = B
# B = S = S
# S = B = S
# S = S = S

## || -> 
# B = B = B
# B = S = B
# S = B = B
# S = S = S

## LOOPING (FOR, WHILE, DO WHILE)

## FOR ##

# CARA 1
# for i in range(10):
#     print(f"{i+1} - Hello World")

# CARA 2
# for i in range(1, 11, 3): # buatkan urutan angka dari index 1 sampai batas < 11 dan dilompati 3
#     print(f"{i} - Hello World Pake FOR")


### OPERATOR MATEMATIKA ###
# + -> Ditambah 2 + 2 = 4
# - -> Dikurang 3 - 2 = 1
# * -> Dikali 3 * 2 = 6
# / -> Dibagi 6 / 2 = 3
# % -> Modulus 6 % 4 = 2 -> 12 % 5 = 2 -> Sisa Bagi
print("\n\n")
print("================ FOR ========================")

# for i in range(1, 11):
#     if (i % 2 == 0): # i = angka 1 sampe 10, misal i nya adalah 3 % 2 == 0
#         print(f"{i} - Hello World Pake FOR")
#     else:
#         print("Angka ini bukan genap woi")

for i in range(1, 11):
    if i == 1 or i == 3 or i == 5 or i == 7 or i == 9:
        continue
    print(f"{i} - Hello World Pake FOR")

print("\n\n")
print("================ WHILE ========================")

## WHILE ##
# num = 1 # Saya memiliki variable bertipe integer dengan value 1
# while num >= 1 and num < 11: # ketika variable saya lebih dari sama dengan 1 DAN (&&) variable saya < 11
#     print(f"{num} - Hello World Pake WHILE") # Jalankan perintah ini
#     num += 1 # Variable saya di tambahkan dengan 1 atau bisa juga mmemakai num = num + 1

num = 1 
while num > 0 and num <= 10:
    if num % 2 == 0:
        print(f"{num} - Hello World Pake WHILE")
    else:
        print("Angka ini bukan genap woi")
    
    num += 1

# Simulasi -> 1
# Perulangan ke 1 : Munculkan '1 - Hello World Pake WHILE'
# Tambahkan variable num (1) + 1

# Simulasi -> 2
# Perulangan ke 2 : Munculkan '2 - Hello World Pake WHILE'
# Tambahkan variable num (2) + 1

# Simulasi -> 3
# Perulangan ke 3 : Munculkan '3 - Hello World Pake WHILE'
# Tambahkan variable num (3) + 1

# Simulasi -> 4
# Perulangan ke 4 : Munculkan '4 - Hello World Pake WHILE'
# Tambahkan variable num (4) + 1

# Simulasi -> 10
# Perulangan ke 10 : Munculkan '10 - Hello World Pake WHILE'
# Tambahkan variable num (10) + 1

# num akhir itu angkanya 11

print("\n\n")
print("================== DO WHILE ======================")


## DO WHILE ##
num = 1 

while True:
    if num > 10: # jika tanpa ini akan jalan terus (infinity loop) 
        break # jika tanpa ini akan jalan terus (infinity loop)
    
    if num % 2 == 0:
        print(f"{num} - Hello World Pake DO WHILE")
    else:
        print("Angka ini bukan genap woi")
    
    num += 1 # jika tanpa ini akan jalan terus (infinity loop)