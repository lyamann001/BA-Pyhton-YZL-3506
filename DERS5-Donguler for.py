#Aralik(range) Tanimlama

# aralik=range(5) 
# aralik=range(3,7) #3,4,5,6
# aralik=range(2,12,3) # 2 den basla 12 ye kadar 3 er 3 er artir

# for i in range(10): # 0 dan 10 a kadar (10 haric) sayilari ekrana yazdiran program
#     print(i)
# #20 den basla 200 e kadar 5 er 5 er artir
# for i in range(20,200,5):
#     if(i==35):
#         break
#     print(i)

#soru: 2den klavyeden girilen sayiya kadar olan cift sayilari ekrana yaziniz
# sayi=int(input("sayi giriniz:"))
# for i in  range(2,sayi,2):
#         print(i)

#ikiside dogru 
# for i in range(2,sayi,1):
#    if (i%2==0):
#        print(i)     

# for i in range (10,0,-1):
#     print(i)

# for i in range(10):
#     for j in range(10):
#         print(f"x:{i} y: {j}")


     

#sutun(yildiz)

# for satir in range(1,6): 
#     for sutun in range(satir):
#         print("*", end="") # satir sayisi kadar yildiz yazdir.
#     print()    

#diger yolu
# for satir in range(1,6):
#     print("*" * satir)

'''
**************
*            *
*            *
*            *
**************
'''
#s=> satir
# u=> sutun
# for s in range (1,6):
    
#         if(s==1 or s==5):
#             print("*"*10)
#         else:
#             print("*",end="")
#             print(" "*8, end="")
#             print("*")


#SORU: Kullanicidan personel sayisi isteyin
#her personelin adini, cocuk sayisini,ismini
#her personel icin cocuk sayisi isteyin ve her personelon 
#kendi ve cocuklarinin adlarini ekrana yazdirin

#Ali celik => ESRa, behiye, tugce

# personelsayi=int(input(" personel sayisini giriniz:"))
# cikti=""


# for i in range(1,personelsayi+1):
#     isim=input(f"{i}.Personel adi:")
#     cocS=int(input(f"{i}. personelin cocuk sayisi:"))
#     cikti += isim +"=>"
#    # print(f"{isim} =>", end="")
#     for j in range(1, cocS+1):
        
#       cocAd=input(f"{j}. cocuk adi:")
#       cikti+=str(j)+":"+ cocAd+" "
#     cikti+="\n"
#     print(cikti)  

#soru : matrix icin x ve y bilgisi istenecek 3x5 lik  x satur, y column.her eleman icin
#1-100 arasinda sayi uretilecek
#matrix string olarak yazilsin str

from random import randint


cikti=""
x=int(input(" satir sayisi giriniz"))
y=int(input("column giriniz"))


for i in range(x):
    for j in range(y):
        sayi=randint(0,100)
        cikti+=str(sayi)+" "
        #print(sayi, end=" ")
    #print()   
    cikti+="\n"
print(cikti)     






  
