'''a=1
while(a<100):
    if(a%2==0):
        print(f"sayi:{a}")
    a=a+1  
'''

#Soru: Yukaridaki soruyu break kullanarak yapmak.

'''sayac=1
while(True):
    if(sayac%2==0):
        print(sayac)
    sayac+=1
    if(sayac==101):
        break    # sayac 100 oldugunda donguden cik'''



#soru 1- limit sayiya kimi girilen sayilar ekrana yazilsin
# hata yakalama dikkate alinsin. while dongusu kullanarak


'''sayac=1
try:
   limitSayi=int(input("sayinizi giriniz:/n"))
except Exception as hata:
    print(f"Hata : {hata}") 


while(sayac<=limitSayi):
      print(sayac)
      sayac+=1  
      '''


#soru: 1'den klavyeyee girilen sayilya olan kadar sayilarin karelerini toplamini gosterin
'''
sayac=1
sum=0
try:
   limitSayi=int(input(f"sayinizi giriniz\n"))
except Exception as hata:
    print(f"Hata : {hata}") 

while(sayac<=limitSayi):
    a=sayac**2
    sum=sum+a
    sayac+=1
print(sum)    '''

#soru:
#klavyeden girilen -1 olana kadara
#girilen pozitiv sayilari toplayip toplami en son ekrana yazdiran program
#-1 haric kac pozitiv kav negativ sayi girildigini son olarak prog sonunda yazdirsin

'''toplam=0
totalnegativ=0 #negativlerin sayiis
totalpozitiv=0 #pozitivlerin sayisi
while(True):
    sayi=int(input("sayi giriniz:"))

    if(sayi==-1):
        break
    if(sayi>0):
       toplam+=sayi
       totalpozitiv+=1
    elif(sayi<-1):
        totalnegativ+=1   


     
    
print(f"girilen pozitif sayilarin toplami : {toplam} \n {totalpozitiv} adet pozitiv sayi girildi.\n {totalnegativ} adetnegativ sayi girildi")    
'''

#soru: klavyeden 10 adet sayi alip bu sayilari toplayan programi yaziniz.
'''sayac=1
sum=0
while(sayac<=10):
    sayi=int(input("sayi giriniz:"))
    sum=sum+sayi
    sayac+=1
    
print(sum)    '''

#soru: 50'den 150 e kadar olan sayilari ve karelerini ekrana yazdiran prog yaziniz;
#zor gelirse once sayilari sonra karesini
'''sum=0
sayac=1
try:
    limit=int(input("adet/limit giriniz:"))

except:
    print("sayi girisi hatali!!!")
    exit() 
while(sayac<=limit):
    try:
        ab=int(input("sayi giriniz:"))
        print(ab)
    except:
        print("Hatali giris!!!")
        continue #continue girilirse while dongusune dondurur. bu yuzden sayi artmadan devam etmis oluruz
    
    sum=sum+ab
    sayac=sayac+1
    ''''''kare=sayac**2
    print(f"sayi:{sayac}, karesi:{kare}")'''
'''

print(f"artihm ortalamasi:{sum//limit}")    
'''

#kullanicidan adet(limit) bilgiisi alip bu sayi kadar artihmetik ortalama yazdirin

#soru: kullanicidan kac sayi girilenecgini isteyin, kullanicinin girdigi sayi cift degilse tekrar isteyin.
#enson toplamlarini ekrana yazdirin

sum=0
sayac=1

try:
    limit=int(input("adet giriniz:"))

except:
    print("sayi girisi hatali!!!")
    exit() 

while(sayac<=limit):
   
    sayi=int(input("sayi giriniz:"))
    if(sayi%2==0):
       sayac=sayac+1
       sum=sum+sayi 
    else:
      print("luften cift sayi giriniz!")

print(f"toplam:{sum}")     
    
    
    



        






