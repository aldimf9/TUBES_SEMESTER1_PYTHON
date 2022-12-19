# Membuat list data_barang dengan elemen dictionary
def list_data(filename):
    file = open(filename,"r")
    dict_minggu1 = {} # buat dictionary kosong
    dict_minggu2 = {}
    dict_minggu3 = {}
    dict_minggu4 = {}
    data = file.readline().replace("\n","") # membaca file dan menghapus \n dalam file
    while data != "":
        list_data = data.split() # membuat list_data berdasarkan spasi 
        
        # memasukkan data list_data menjadi dict_minnggu1,dict_minnggu2,dict_minnggu3,dict_minnggu4 dengan key nama_barang dan value setiap minggunya
        # minggu 1
        data_append = list(map(int,list_data[1:3])) 
        dict_minggu1[list_data[0]] = data_append

        # minggu 2
        data_append = list(map(int,list_data[3:5]))
        dict_minggu2[list_data[0]] = data_append

        # minggu 3
        data_append = list(map(int,list_data[5:7]))
        dict_minggu3[list_data[0]] = data_append

        # minggu 4
        data_append = list(map(int,list_data[7:]))
        dict_minggu4[list_data[0]] = data_append


        data = file.readline().replace("\n","")
    file.close()
    # memasukkan data dalam bentuk dictionary ke dalam list
    data_barang = [dict_minggu1,dict_minggu2,dict_minggu3,dict_minggu4]
    return data_barang

# Menampilkan dictionary
def print_data(data):
    list_minggu = ["1","2","3","4"] 
    i = 0
    # Untuk mencetak kata Minggu dengan list_minggu berdasarkan indeks i
    for elemen in data:
        print("Minggu:",list_minggu[i])
        # Untuk mencetak key dan value dalam list data_barang
        for key in elemen:
            print("\t",key,"=",elemen[key])
        print("\n")
        i += 1 

# Menampilkan daftar barang yang mengalami peningkatan produksi di setiap Minggu
def peningkatan(data):
    print("Data yang mengalami peningkatan di setiap minggunya:",end=" ")
    ada = False
    if data[0]["Pencil"][0] < data[1]["Pencil"][0] and data[1]["Pencil"][0] < data[2]["Pencil"][0] and data[2]["Pencil"][0] < data[3]["Pencil"][0] :
        print("Pencil",end=",")
        ada = True
    if data[0]["Pena_Biru"][0] < data[1]["Pena_Biru"][0] and data[1]["Pena_Biru"][0] < data[2]["Pena_Biru"][0] and data[2]["Pena_Biru"][0] < data[3]["Pena_Biru"][0] :
        print("Pena_Biru",end=",")
        ada = True
    if data[0]["Pena_Hitam"][0] < data[1]["Pena_Hitam"][0] and data[1]["Pena_Hitam"][0] < data[2]["Pena_Hitam"][0] and data[2]["Pena_Hitam"][0] < data[3]["Pena_Hitam"][0] :
        print("Pena_Hitam",end=",")
        ada = True
    if data[0]["Penggaris"][0] < data[1]["Penggaris"][0] and data[1]["Penggaris"][0] < data[2]["Penggaris"][0] and data[2]["Penggaris"][0] < data[3]["Penggaris"][0] :
        print("Penggaris",end=",")
        ada = True
    if data[0]["Penghapus"][0] < data[1]["Penghapus"][0] and data[1]["Penghapus"][0] < data[2]["Penghapus"][0] and data[2]["Penghapus"][0] < data[3]["Penghapus"][0] :
        print("Penghapus",end=",")
        ada = True
    if ada:
        print()
    if not ada:
        print("Tidak Ada")

# Menggembalikan rata-rata jumlah barang tertentu yang terjual
def report(data,nm_barang):
    a1,a2,a3,a4 = data[0][nm_barang][1],data[1][nm_barang][1],data[2][nm_barang][1],data[3][nm_barang][1]
    print("Jadi Rata-Rata Penjualan",nm_barang,"adalah",(a1 + a2 + a3 + a4) // 4,"barang") 

# Main Program Tubes_2021_1301213053_Aldi Muhammad  Farhan
# menampilkan dictionary dan fungsi yang di buat
# inisialisasi gudang.txt menjadi nama_file
nama_file = "gudang.txt"

# fungsi list_data
data_barang = list_data(nama_file)

# fungsi print_data
print_data(data_barang)

# fungsi peningkatan
peningkatan(data_barang)

# fungsi report 
print("\nNama Barang:")
barang = input()
barang = barang.title()
report(data_barang,barang)