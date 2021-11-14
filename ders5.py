# #eposta ve parola dogru girilene kadar tekrar istesin.
# kayitlieposta="necdet@bilge.com"
# kayitliparola="Zorluparolam123"

# girilenEposta=""
# girilenParola=""

# while(girilenEposta!=kayitlieposta or girilenParola!=kayitliparola):
#     girilenEposta=input("Eposta adresi:")
#     girilenParola=input("girilen parola:")


# print("basarili giris:")


# from random import randint
# rastgeleSayi=randint(0,100)
# print(rastgeleSayi)

# #soru: rastgele uretilen sayiyi bulana kadar klavyeden tahmin isteyen programi yaziniz.
# # daha kucuk ve daha buyuk bir sayi giriniz sekilinde yonergede bulunsun


# while(True):
#     sayi=int(input("sayi giriniz:"))
#     if(rastgeleSayi==sayi):
#          break
#     elif(sayi<rastgeleSayi):
#         print("daha buyuk giriniz")   
#     elif(sayi>rastgeleSayi):
#         print("daha kucuk giriniz")    
#     else:
#         continue

# print("basarili")   
    


#hocanin yazdigi; ikiside dogru 
from random import randint
rastgeleSayi=randint(0,100)
tahmin=-1
puan=1000

while(tahmin != rastgeleSayi):
    print(f"Puaniniz:{puan}")
    tahmin=int(input("sayi giriniz:"))
    if(puan==0):
        print(f"Basaramadin,\n Puanin: {puan}")
        break
    else:

        if(tahmin<rastgeleSayi):
            print("daha buyuk giriniz")  
            puan-=100 
        elif(tahmin>rastgeleSayi):
            print("daha kucuk giriniz")   
            puan-=100 
        else:
            print(f"tebrikler bildiniz\n Puaniniz : {puan}")

#Puanlama: Oyuncu 1000 puan ile baslar. her tahminden sonra 100 puan eksilir