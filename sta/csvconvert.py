import json

with open("C:/hospital.json", "r", encoding="euc-kr") as file_1:
	data1 = json.load(file_1)

with open("C:/pharmacy.json", "r", encoding="euc-kr")as file_2:
	data2 = json.load(file_2)

with open("C:/clinic.json", "r", encoding="euc-kr")as file_3:
	data3 = json.load(file_3)

with open("newfile", "w") as new_file:
	json.dump(data1+data2+data3, new_file)