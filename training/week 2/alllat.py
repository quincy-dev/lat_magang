#1
print("hallo")

#2
negara = {
    "nama" : "indonesia",
    "presiden"  : "Prabowo Subianto",
    "wapres" : "Gibran Rakabuming Raka",
    "informasi" : {
        "jumlah_pulau" : 34,
        "ras" : ["jawa", "batak", "sunda"]
    }
}

rang = negara["informasi"]["ras"][-1]
print(rang)
print(negara["informasi"]["ras"][1])
print(negara.get('presiden'))

#3
for i in range(5):
    i += 1
    print(i)

#4
fruits = ["apple", "banana", "cherry"]
for f in fruits:
    if f == "banana":
        break
    print(f)

#5
for num in range(1,16):
    if num % 2 == 0:
        print(f"{num} - kelipatan 2")
    else:
        print(f"{num} - bukan kelipatan 2")
        num += 1

#6
def allert(notif):
    print(f"ada pesan {notif}")
allert("yolo")

#7
def tambah(a, b):
    return a + b

a = 7
b = 7
print(tambah)