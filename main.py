
sData= []

with open("student.csv","w") as file:
		file.write("num,name,surname,lesdata1,lesdata2,avg,result\n")
		file.close()

def sCheck(lesdata1,lesdata2):
	avg= lesdata1*0.4+lesdata2*0.6
	if avg >100:
		return False
	elif avg >84:
		return "AA GEÇTİ"
	elif avg >65:
		return "BB GEÇTİ"
	elif avg >50:
		return "CC GEÇTİ"
	else :
		return "KALDI"
		

def kayit():
	while True:
		sName= input("öğrenci ad :")
		sSurName =input("öğrenci soyad :")
		sNum= input("öğrenci No :")
		lesData1 = int(input("Vize Notu :"))
		lesData2 = int(input("Final Notu :"))
		breakup = input("Devam >> e Tamam >> w :")
		sData.append([sNum,sName,sSurName,lesData1,lesData2,(lesData1*0.4+lesData2*0.6),sCheck(lesData1,lesData2)])
		if breakup == "w":
			break
		
	with open("student.csv","a") as file:
			for i in sData:
				file.write(f"{i[0]},{i[1]},{i[2]},{i[3]},{i[4]},{i[5]},{i[6]}\n")
			file.close()
			
def sList():
	datal =[]
	with open("student.csv","r") as file:
			datal = file.readlines()
			for i in range(0,len(datal)):
				if i == 0:
					continue
				else:
					print(datal[i])
			
while True:
	print("öğrenci otomasyonu".upper().center(5,"*"))
	chs= input("Öğrenci kayıt >> n \nÖğrenci listesi >> k\nNot durum >> h\nlütfen işlem seçiniz :")
	if chs == "n":
		kayit()
	elif chs=="k":
		sList()
	elif chs == "h":
		pass
	else:
		print("Hatalı giriş tekrar deneyiniz")
		continue