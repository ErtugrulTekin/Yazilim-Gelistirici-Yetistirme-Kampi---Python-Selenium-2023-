print("Kodlama.io")
baslik = "Tasit Kredisi"
print(baslik)

# string => metinsel ifade
baslik = "Ihtiyac Kredisi"
print(baslik)

# int, integer => tam sayi
vade = 36
ekVade = 6
vade2 = "36"

# float, decimal, double
aylikOdeme = 200.50

# boolean, bool => true veya false (karar  yapilarinda bolca kullanılır)
yukselisteMi = True

# matematiksel operatorler

# +
print(5 + 5)
print(vade + 12)
print(vade + ekVade)
print(36 + 6)

# -
print(5 - 5)
print(vade - 12)
print(vade - ekVade)
print(36 - 6)

# * 
print(5 * 5)
print(vade * 2)
print(vade * ekVade)
print(10 * 10)

# /
print(5 / 5)
print(vade / 2)
print(vade / ekVade)
print(10 / 2)


yeniVade = vade / 2
fiyat = 100
indirimliFiyat = fiyat - 20

print(yeniVade)
print(indirimliFiyat)

# % => mod operator
print(10 % 2)
print(vade % 5)
print(vade % ekVade)
print(30 % 10)

# mantiksal operatorler 
print(1 == 1) 

print(1 > 2)
print(3 > 1)
print(1 > 1)
print(1 >= 1)

print(1 < 2)
print(3 < 1)
print(1 < 1)
print(1 <= 1)

print(1 != 1)
print(1 != 2)

# or & and
print(1 > 2 or 5 > 2)
print(1 > 2 and 5 > 2)
print(1 > 2 or 5 > 2 and 3 > 2)
print(1 > 2 and 5 > 2 and 3 > 2)
print(2 > 1 or 1 > 2 and 3 > 2)

# karar yapilari 
# if - else
sayi1 = 15
sayi2 = 15 

# sayi1 sayi2'den daha buyukse ekrana sayi1 daha buyuk yazdir
# condition 

# indent
if sayi1 <= sayi2:
    print("Sayi1 Sayi2'den kucuktur.")
elif sayi1 == sayi2:
    print("Iki sayi esittir.")
    # eger if ve else bloklarindan hicbirine girmez ise;
else:
    print("Sayi1 Sayi2'den buyuktur.")

print("**********************************")

if sayi1 <= sayi2:
    print("Sayi1 Sayi2'den kucuktur.")
if sayi1 == sayi2:
    print("Iki sayi esittir.")
else:
    print("Sayi1 Sayi2'den buyuktur.")

print("Burasi if blogunun disidir.")

