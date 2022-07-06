import pandas as pd  # pandas kütüphanesını dahıl et


class Otomasyon():               #otomasyon adında bir class oluştur
    def __init__(self):          # obje oluşturduğunda studentInfo.csv adında bır dosya oluştur
        with open("studentInfo.csv","w") as file:
            file.write("num,name,surname,les1,les2,avg,status\n")
            file.close()

    def kayit(self,name,sName,sNum,les1,les2): # kayıt adında bır class fonksyonu tanımladık
        listData =[]       #fonksyon çağırıldığında lıstData adında boş bir liste oluştur fonksyon parametrelerini liste olaral listeye ekle
        listData.append([name,sName,sNum,les1,les2,self.avg(les1,les2),self.durum(self.avg(les1,les2))])
        with open("studentInfo.csv","a") as file: #oluşturulan csv dosyasını append modunda aç ve listData listesindeki verileri dosyaya ekle
            file.write(f"{listData[0][2]},{listData[0][0]},{listData[0][1]},{listData[0][3]},{listData[0][4]},{listData[0][5]},{listData[0][6]}\n")
            print("student registered") # terminale mesaj yaz 
            file.close()  # dosyayı kapat

    def durum(self,avg): # avg parametresıne gore bır değer dönduren fonksyon tanımla
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
    def avg(self,les1,les2): #ortalama hesaplayan fonkyan tanımla
        return (les1*0.4+les2*0.6)

    def dataframe(self,excel=0): # dataframe ve excel dosyası oluşturmak için bir fonksyon tanımla excel parametresi varsayılan olarak 0 olsun 
        if excel == 0: #excel parametresı 0 ise csv dosyasından bir dataframe oluştur
            print(pd.read_csv("studentInfo.csv"))
        else:          #excel parametresı 1 ise csv dosyasından bir excel dosyası oluştur
            dF_new = pd.read_csv("studentInfo.csv")
            GFG = pd.ExcelWriter('Names.xlsx')
            dF_new.to_excel(GFG, index=False)
            GFG.save()
            
    



ob = Otomasyon() # ob adında bir otomasyon objesi olustur

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
        
ob.dataframe() # dataframe oluştur
ob.dataframe(excel=1) #excel dosyası oluştur




