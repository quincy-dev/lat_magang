## Penulisan Variable
# numFirst -> CamelCase -> js, java, c++, c#
# num_first -> snake_case -> python, go

## Penulisan Class
# NumFirst -> CapitalCase

a: int = 123

b: str = "Hello"

c: bool = False

d: float = 12.9

e: None = None

f: tuple[int,int,int,int,int] = (1, 2, 3, 3, 4)

g: list[int] = [1, 2, 3, 3, 4, 4] # angka double bebas ada

h: set[int] = { 1, 2, 3, 3, 4, 5, 6, 6 } # angka yang double atau sama itu dihilangkan (unique)

identitasSaya: dict = {
    "name": "Budi",
    "age": 12,
    "school": [ # list / array
        "SD Sukamaju", # index 0
        "SD Sukabelajar" # index 1
    ],
    "mother": { # Object
        "name": "Siti",
        "age": 65
    }
}

# "name" = key
# "siti" = value
# aturan : kalo dia hanya 1 object maka pake .get('key')
# kalo dia punya 2 object maka pakenya [][]

# namaIbuBudi = identitasSaya['mother']['name']
# print(namaIbuBudi)

# print(i["school"][0]) # SD Sukamaju


# print(i["school"[0]) # Error: Compiler / Interpreter Error
# print(i["school"][2]) # Error: Runtime Error


# g = [10, 11, 12]
# print(g)

# Soal hari ini
transportasi = {
    "name": "Mobil",
    "type": "BMW I8",
    "year": 2014,
    "owner": [
        {
            "name": "Angga",
            "age": 23
        },
        {
            "name": "Sandi",
            "age": 21
        },
        {
            "name": "Robert",
            "age": 29
        },
    ],
    "seller": {
        "year": 2024,
        "sell_list": [
            "Janu", # 0
            "Agus", # 1
            "Rama" # 2
        ]
    }
}

# soal 1 : Cara print nama Agus
nama_seller = transportasi["seller"]['sell_list'][1]
print(nama_seller)

# soal 2 : Cara mendapatkan umur Robert
umur_robert = transportasi["owner"][2]["age"]

# umur_robert = transportasi.get("owner")[2].get("age") -> tidak boleh

print(umur_robert)

