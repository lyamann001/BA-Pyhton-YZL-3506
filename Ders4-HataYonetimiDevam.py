

'''islem = input("Toplama : T\nÇıkarma : Ç \nÇarma : X\nBölme : B :")
try:
    rakam1 = input("Rakam1: ")
    rakam1 = rakam1[0]
    rakam1 = int(rakam1)
except ValueError:
    try:
        rakam1 = input("Rakam1: ")
        rakam1 = rakam1[0]
        rakam1 = int(rakam1)
    except ValueError:
        print("Yine hatalı girdiniz. Rakam1 1 oldu.")
        rakam1 = 1
    except IndexError: # Hiçbirşey girmeden enter'a bastıysa index eror alır. 0. index olmadığı için.
        print("Birşey girmediniz. Rakam1 1 oldu.")
        rakam1 = 1

try:
    rakam2 = input("Rakam2: ")
    rakam2 = rakam2[0]
    rakam2 = int(rakam2)
except ValueError:
    try:
        rakam2 = input("Rakam2: ")
        rakam2 = rakam2[0]
        rakam2 = int(rakam2)
    except ValueError:
        print("Yine hatalı girdiniz. Rakam2 1 oldu.")
        rakam2 = 1
    except IndexError:
        print("Birşey girmediniz. Rakam2 1 oldu.")
        rakam2 = 1

if(islem=="T"):
    print(f"Rakamların toplamı : {rakam1+rakam2}")
elif(islem=="Ç"):
    print(f"Rakamların farkı : {rakam1-rakam2}")
elif(islem=="X"):
    print(f"Rakamların çarpımı : {rakam1*rakam2}")
elif(islem=="B"):
    try:
        print(f"Rakamların bölümü : {rakam1/rakam2}")
    except ZeroDivisionError:
        rakam2 = 1
        print(f"Rakamların bölümü : {rakam1/rakam2}")
    finally: # her koşulda çalışacaktır.
        print("Öyle yada böyle buralara geldik.")
        print("Her iki ihtimalde de bu blok çalışır.")
else:
    print("HATALI İSLEM GİRİŞİ !!!")
    print("LÜTFEN ŞU HARFLERDEN BİRİNİ GİRİNİZ : X,T,B,Ç")

'''
#ders4
#el yardimi ile hata firlama
'''dersNot=0
try:
     dersNot=int(input("Ders notunuzu giriniz:"))

except ValueError as degerHatasi:
    print(f"Luften sadece rakam giriniz! {degerHatasi} ")

if(dersNot<0 or dersNot>100):
    raise OverflowError("Hatali not girdiniz!!!")'''

#MemoryError,Value Error, IndexError ve ZerodivisionError da firlatilabilir

#Assert
'''eposta=input("Dogru e posta adresi giriniz:")
assert eposta =="bilge@adam.com"
print("Eposta dogru girildi")'''

#DERS4 Donguler (loop)
'''kosul=True #false olarasa loopa girmez. loopin ici hemise dogru olmalidir
while(kosul):
    print("Kosul dogru oldugu surece calisacak bu kod")

print("Dongu sonrasi")'''

#0-10
'''sayi=0

while(sayi<=10):
    print(f"Sayi: {sayi}")
    sayi=sayi+1
'''

# 1 den 100 e kadar cift sayilari ekrana yazdirin
a=1

while(a<100):
    if(a%2==0):
        print(f"sayi:{a}")
        a=a+1       
    
















