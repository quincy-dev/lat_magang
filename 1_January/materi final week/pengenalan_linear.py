# LINEAR SEARCH
data = [2, 5, 8, 10, 9, 1] # LIST / ARRAY

# for i in range(10) - Looping For


# Cari angka yang jika dikali 2 hasilnya kurang dari 15
# for d in data: # Looping ForEach
#     if (d*2) < 15:
#         print(d)
        

# DEEP LINEAR SEARCH
data2 = [ [5, 2, 3, 4], [7, 1, 2, 6] ] # LIST / ARRAY 2 DIMENSI

# Cari angka yang jika dikali 2 hasilnya kurang dari 12
# [5, 2, 3, 4]
# [7, 1, 2, 6]
dict_data = {}
for x in data2: # Looping ForEach
    for y in x:
        if(y * 2) < 12:
            dict_data[str(y)] = 1 # dict_data["2"] = 1
            
for key, val in dict_data.items():
    print(key) 