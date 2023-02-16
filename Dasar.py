#Output terminal
print('Hello world')

#Variable
#Integer
nilaiAwal = 0
nilaiAkhir = 10
#Float
nilaiFloat = 1.5
#String
sebuahString = "Kata"
#Boolean
nilaiBoolean = True
#Type Data Khusus
dataComplex = complex(5,6)

print("Nilai Awal :", nilaiAwal)
print("Nilai Akhir :", nilaiAkhir)
print("Dijumlahkan : ", nilaiAwal + nilaiAkhir)

#Type
print("Type dari nilai Awal :", type(nilaiAwal))
print("Type dari nilai Float :", type(nilaiFloat))
print("Type dari sebuah String :", type(sebuahString))
print("Type dari nilai boolean :", type(nilaiBoolean))
print("Type dari data Complex :", type(dataComplex))

#Casting(merubah dari satu type ke type lain)
data_int = 9;
print(f"data = {data_int}, type {type(data_int)}")
#untuk merubah dapat menggunakan operator casting
data_float = float(data_int)
print(f"data = {data_float}, type {type(data_float)}")
data_bool = bool(data_int)
print(f"data = {data_bool}, type {type(data_bool)}")
data_str = str(data_int)
print(f"data = {data_str}, type {type(data_str)}")
