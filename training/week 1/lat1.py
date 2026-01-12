# # nama = ""
# # input_user = input("Masukkan nama Anda: ")
# # if input_user:
# #     nama = input_user
# # print("Halo, " + nama)

# # #===========================================

# # nilai = 80
# # hadir = 85
# # if nilai >= 75 and hadir >80:
# #     print("Selamat, Anda Lulus")
# # else:
# #     print("Maaf, Anda Tidak Lulus")

# # #===========================================

# # buah = ["apel", "jeruk", "mangga", "pisang", "semangka"]
# # a, b, c, d, e = buah
# # print(a)
# # import datetime
# # print(datetime.datetime.now())

# # nama_anda = ""
# # nilai1 = ""
# # nilai2 = ""
# # input_user = input("masukkan nama anda:")
# # if input_user:
# #     nama_anda = input_user
# # print("Halo, " + nama_anda)
# # input_nilai = input("masukkan nilai anda :")
# # if input_nilai:
# #     nilai1 = input_nilai
# #     print("Nilai anda adalah : " + nilai1)
# # input_nilai2 = input("masukkan nilai ke 2 anda :")
# # if input_nilai2:
# #     nilai2 = input_nilai2
# #     print("Nilai ke 2 anda adalah : " + nilai2)
# #     print("Total nilai anda adalah : " + str(int(nilai1) + int(nilai2)))




# # Loop through and print out all even numbers from the numbers list in the same order they are received. Don't print any numbers that come after 237 in the sequence.
# # numbers = [
# #     951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
# #     615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
# #     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
# #     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
# #     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
# #     958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
# #     743, 527
# # ]

# # # your code goes here
# # for number in numbers:
# #     if number == 237:
# #         break
# #     if number % 2 == 0:
# #         print(number)



# # SOAL 1
# # Perhatikan ketentuan berikut.
# # Seorang karyawan dinyatakan MENDAPAT BONUS jika memenuhi syarat:
# # Lama kerja lebih dari atau sama dengan 3 tahun
# # Nilai kinerja lebih dari 85
# # Diketahui:
# # Lama kerja karyawan = 4 tahun
# # Nilai kinerja = 80
# # Tugas:
# # Buatlah sebuah program untuk menentukan apakah karyawan tersebut MENDAPAT BONUS atau TIDAK MENDAPAT BONUS menggunakan operator logika.

# durasi_kerja = 4
# nilai_kinerja = 80
# if durasi_kerja >= 3 and nilai_kinerja > 85:
#     print("MENDAPAT BONUS")
# else:
#     print("TIDAK MENDAPAT BONUS")


# # SOAL 2
# # Sebuah aplikasi hanya dapat dijalankan jika:
# # Username terdaftar
# # Password benar
# # Diketahui kondisi:
# # Username = BENAR
# # Password = BENAR
# # Tugas:
# # Buatlah program untuk menampilkan:
# # "Login Berhasil" jika kedua kondisi bernilai benar
# # "Login Gagal" jika salah satu kondisi bernilai salah
# # Gunakan operator logika DAN (&&).

# username = True
# password = True
# if username and password:
#     print("Login Berhasil")
# else:
#     print("Login Gagal")


# # SOAL 3
# # Buatlah sebuah program yang menampilkan bilangan dari 1 sampai 20 menggunakan perulangan FOR dengan ketentuan berikut:
# # Jika sebuah bilangan (X) habis dibagi 5, tampilkan:
# # ========== Angka X - Kelipatan 5 ==========
# # Jika tidak, tampilkan:
# # ========== Angka X - Bukan Kelipatan 5 ==========
# # Gunakan operator modulus (%) untuk menentukan kelipatan.

# for x in range (1, 21):
#     if x % 5 == 0:
#         print(f"Angka {x} - Kelipatan 5")
#     else:
#         print(f"Angka {x} - Bukan Kelipatan 5")


# # SOAL 4
# # Sebuah sistem lampu otomatis akan aktif selama nilai variabel counter memenuhi kondisi:
# # counter lebih dari atau sama dengan 1
# # counter kurang dari 8
# # Nilai awal:
# # counter = 1
# # variabel ditandai dengan huruf X
# # Setiap perulangan:
# # Jika counter merupakan bilangan genap, tampilkan:
# # Lampu X - Menyala
# # Jika counter merupakan bilangan ganjil, tampilkan:
# # Lampu X - Mati
# # Tugas:
# # Buatlah program menggunakan perulangan WHILE dan operator logika.
# counter = 1
# while counter >= 1 and counter < 8:
#     if counter % 2 == 0:
#         print(f"Lampu {counter} - Menyala")
#     else:
#         print(f"Lampu {counter} - Mati")
#     counter += 1


# # SOAL 5
# # Sebuah sistem game melakukan pengecekan level pemain minimal satu kali.
# # Aturan sistem:
# # Game akan berhenti jika level lebih dari 12
# # Ketentuan tampilan:
# # Jika level kurang dari 4 ATAU level bukan bilangan ganjil, tampilkan:
# # Level X - Skill Rendah
# # Jika tidak memenuhi kondisi tersebut, tampilkan:
# # Level X - Skill Tinggi
# # Nilai awal variabel:
# # level = 1
# # Tugas:
# # Buatlah program menggunakan:
# # Konsep DO WHILE (while True dan break)
# # Operator logika ATAU (||)
# # Operator negasi (!)
# # Operator modulus (%)

# level = 1
# while True:
#     if level > 12:
#         break
#     if level < 4 or level % 2 == 0:
#         print(f"Level {level} - Skill Rendah")
#     else:
#         print(f"Level {level} - Skill Tinggi")
#     level += 1

# txt = "yolololololololololololo"
# print(len(txt))

print("\n\n")
text = ["na", "ma", "pa"]
print(text[1])