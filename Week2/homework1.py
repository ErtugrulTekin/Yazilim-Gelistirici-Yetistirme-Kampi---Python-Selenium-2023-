ogrenci = ["Enes Sahin", "Ertugrul Tekin", "Dogus Saglam"]

while True:
    print("")
    print("Ogrenci Kayit Sistemine Hos Geldiniz!")
    print("<Ogrenci Kayit Sistemi>")
    print(" 1.Ogrenci Kayit Ekleme")
    print(" 2.Ogrenci Kayit Silme")
    print(" 3.Birden Fazla Ogrenci Kayit Ekleme")
    print(" 4.Birden Fazla Ogrenci Kayit Silme")
    print(" 5.Butun Ogrencileri Listeleme")
    print(" 6.Ogrenci Numarasi Sorgulama")
    print(" 7.Sistemden Cikis Yap")
    
    islem = input("Lutfen Yapmak Istediginiz Islemi Seciniz : ")

    def addStudent():
        print("Ogrenci Kayit Ekleme")
        ad = input("Eklemek Istediginiz Ogrencinin Adini lutfen giriniz: ")
        soyad = input("Eklemek Istediginiz Ogrencinin Soyadini lutfen giriniz: ")
        ogrenci.append(ad + " " + soyad)
        print("Kayit sisteme eklenmistir.")

    def deleteStudent():
        print("Ogrenci Kayit Silme")
        ad = input("Silmek Istediginiz Ogrencinin Adini lutfen giriniz: ")
        soyad = input("Silmek Istediginiz Ogrencinin Soyadini lutfen giriniz: ")
        ogrenci.remove(ad + " " + soyad)
        print("Kayit sistemden silinmistir.")

    def addingMultipleStudents():
        print("Birden Fazla Ogrenci Ekleme")
        deger = int(input("Eklemek Istediginiz Ogrenci Sayisini Giriniz: "))
        for i in range(deger):
            ad = input(f"{i + 1}.Eklemek Istediginiz Ogrencinin Adini lutfen giriniz: ")
            soyad = input(f"{i + 1}.Eklemek Istediginiz Ogrencinin Soyadini lutfen giriniz: ")
            ogrenci.append(ad + " " + soyad)
        print(f"{deger} kayit sisteme eklenmiştir.")

    def deletingMultipleStudents():
        print("Birden Fazla Ogrenci Silme")
        deger = int(input("Silmek Istediginiz Ogrenci Sayisini Giriniz: "))
        for i in range(deger):
            ad = input(f"{i + 1}.Silmek Istediginiz Ogrencinin Adini lutfen giriniz: ")
            soyad = input(f"{i + 1}.Silmek Istediginiz Ogrencinin Soyadini lutfen giriniz: ")
            ogrenci.remove(ad + " " + soyad)
        print(f"{deger} kayit sisteme eklenmiştir.")

    def studentListing():
        print("Ogrenci Listesi")
        studentNumber = 0
        for i in ogrenci:
            print(f"{studentNumber} : {i}")
            studentNumber += 1

    def studentNumber():
        print("Ogrenci Numarasi")
        ad = input("Ogrencinin Adini lutfen giriniz: ")
        soyad = input("Ogrencinin Soyadini lutfen giriniz: ")
        number = ogrenci.index(ad + " " + soyad)
        print(f"Ogrencinin numarasi: {number}")

    if islem == "1":
        addStudent()

    elif islem == "2":
        deleteStudent()

    elif islem == "3":
        addingMultipleStudents()

    elif islem == "4":
        deletingMultipleStudents()

    elif islem == "5":
        studentListing()

    elif islem == "6":
        studentNumber()

    elif islem == "7":
        print("Sistemden Cikis Yaptiniz, Tekrar Gorusmek Uzere!")
        break

    else:
        print("Gecersiz Bir Islem Sectiniz!")
        
    
