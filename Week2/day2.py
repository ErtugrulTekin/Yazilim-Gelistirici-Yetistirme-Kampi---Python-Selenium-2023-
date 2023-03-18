faiz = 1.59
vade = "36"
krediAdi = "Ihtiyac Kredisi"

print(type(faiz))
print(type(vade))
print(type(krediAdi))

print(int(vade) + 12)
#print(int(krediAdi)),
faiz = str(faiz)
print(type(faiz))

vade = 36 #int(input("Lutfen istediginiz vade sayisini giriniz: "))
print(type(vade))
vade = vade + 12

#string interpolation
# Seçtiğiniz vade sonucu ortaya çıkan vade: 
print("Sectiginiz vade sonucu ortaya cikan vade: " + str(vade))
print("Sectiginzi vade sonucu ortaya cikan vade: {vadeSayisi}".format(vadeSayisi=vade))
print(f"Sectiginiz vade sonucu ortaya cikan vade: {vade}")

isim = "Halit" #input("Isminizi giriniz: ")
metin = "Merhaba {name}".format(name = 123)
print(metin)

# f - string
metin = f"Hosgeldiniz {1 + 1}"
print(metin)

#Listeler
#Döngüler
#Fonksiyonlar

dizi = ["Ihtiyac Kredisi", 10, 5.2, True]
print(dizi)

krediler = ["Ihtiyac Kredisi", "Tasit Kredisi", "Konut Kredisi"]
print(type(krediler))
print(krediler[0])

print(len(krediler)) #length
# print(krediler[3]) -> hata verir

krediler.append("Ozel Kredi")
print(krediler)

krediler.append("X Listesi")
print(krediler)

krediler.pop(0)
print(krediler)

krediler.append("Tasit Kredisi")
print(krediler)

krediler.remove("Tasit Kredisi")
print(krediler)

krediler.extend(["Y Kredisi", "Z Kredisi"])
print(krediler)

# for
# i=0 i<10
x = 10
for i in range(x):
    print("xx")
    print(i)

print("#########################")

for i in range(5, 11):
    print(i)

print("#########################")

for i in range(0, 51, 10):
    print(i)

print("#########################")
#for i in range(0.1, 0.5):
#    print(i)

krediler = ["Ihtiyac Kredisi", "Tasit Kredisi", "Konut Kredisi"]

for kredi in krediler:
    print(kredi)

print("#########################")

for i in range(len(krediler)):
    print(krediler[i])

print("#########################")

#sonsuz döngü
i = 0
while i < 10:
    print("x")
    i += 1
print("y")

print("#########################")

while True:
    print("x")
    break

print("#########################")

i = 0
while i < len(krediler):
    i += 1
    print(i)
    print(krediler[i])
    if krediler[i] == "Konut Kredisi":
        break

print("#########################")

# Fonksiyonlar

fiyat = 100
indirim = 20

#definition define
def calculate():
    print(100 - 20)

def calculateWithParams(fiyat, indirim):    
    print(fiyat - indirim)

def sayHello(name):
    print(f"Merhaba {name}")

calculate()
calculateWithParams(100, 20)
calculateWithParams(100, 30)
sayHello("Halit")
sayHello("Arif")
sayHello("Mevlut")

def calculateAndReturn(price, discount):
    return price - discount

yeniFiyat = calculateAndReturn(200, 50)
print(yeniFiyat)

def calculatePrice(price, discount):
    print(price - discount)

def calculatePriceAndReturn(price, discount):
    return price - discount

print("#######SON DONGU#######")

fonk1 = calculatePrice(100,50)
fonk2 = calculatePriceAndReturn(300,100)
print(f"160.Satir: {fonk1}")
print(f"161.Satir: {fonk2 + 200}")

print("#######SON DONGU#######")

