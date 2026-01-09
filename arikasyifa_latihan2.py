#soal 1
nsiswa = 70
ksiswa = 90

if nsiswa >= 75 and ksiswa >80:
    print("Lulus")
else:
    print("Tidak Lulus")


print("\n\n")
#soal 2
kakses = True
pin = False
if kakses and pin:
    print("Akses Diizinkan")
else:
    print("Akses Ditolak")  

print("\n\n")
#soal 3
for x in range(15):
    x += 1
    if x % 3 == 0:
        print(f"{x} -  Kelipatan 3 ")
    else:
        print(f"{x} - Bukan Kelipatan 3 ")

print("\n\n")
#soal 4
counter = 1
X = "x"
while counter > 0 and counter <= 10:
    counter += 1
    if counter % 2 == 0:
        print(f"Counter {X} - Mesin Aktif")
    else:
        print(f"Counter {X} - Mesin Siaga")
        break


print("\n\n")
#soal 5
level = 1
while True:
    if level > 10:
        break
    if level < 5 or level % 2 != 0:
        print(f"Level {level} - Sistem Tidak Aman")
    else:
        print(f"Level {level} - Sistem Aman")
    level += 1