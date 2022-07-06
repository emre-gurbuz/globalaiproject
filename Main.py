import pandas as pd


class Otomasyon():
    def __init__(self):
        with open("studentInfo.csv","w") as file:
            file.write("num,name,surname,les1,les2,avg,status\n")
            file.close()

    def kayit(self,name,sName,sNum,les1,les2):
        listData =[]
        listData.append([name,sName,sNum,les1,les2,self.avg(les1,les2),self.durum(self.avg(les1,les2))])
        with open("studentInfo.csv","a") as file:
            file.write(f"{listData[0][2]},{listData[0][0]},{listData[0][1]},{listData[0][3]},{listData[0][4]},{listData[0][5]},{listData[0][6]}\n")
            print("student registered")
            file.close()

    def durum(self,avg):
        if avg>90:
            return"AA "
        elif avg>80 :
            return"BA "
        elif avg>70 :
            return"BB "
        elif avg>60 :
            return"CB "
        elif avg>50 :
            return"CC "
        elif avg>40 :
            return"DC "
        else:
            return"FF "
    def avg(self,les1,les2):
        return (les1*0.4+les2*0.6)

    def dataframe(self,excel=0):
        if excel == 0:
            print(pd.read_csv("studentInfo.csv"))
        else:
            dF_new = pd.read_csv("studentInfo.csv")
            GFG = pd.ExcelWriter('Names.xlsx')
            dF_new.to_excel(GFG, index=False)
            GFG.save()
            
    



ob = Otomasyon()

while True:
    sayi = int(input("Kac ogrenci kaydedeceksiniz :"))
    for i in range(0,sayi):
        name = input("Name :")
        sName = input("Surname :")
        sNum = input("Student Number :")
        les1 = int(input("midterm exam grade :"))
        if les1>100:
            print("Vize notu 100'den büyük olamaz.Başa dönün")
            continue
        les2 = int(input("main exam grade :"))
        if les2>100:
            print("Final notu 100'den büyük olamaz.Başa dönün")
            continue
        ob.kayit(name,sName,sNum,les1,les2)
    break
        
ob.dataframe()
ob.dataframe(excel=1)




