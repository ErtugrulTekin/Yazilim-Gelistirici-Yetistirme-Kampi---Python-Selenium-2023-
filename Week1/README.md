  ## 1.Python'da Veri Tiplerini araştırınız, her bir veri tipi için kendi cümlelerinizle açıklamalar yazınız.
  
  `Text Type`: *str (String) olarak gösterilir. Çift Tırnak içerisinde metinsel ifade yazılarak kullanılır.*
  ```python
  a = "Merhaba Kodlama.io"
  b = "41"
  ```
  
  `Numeric Type`: *int (Integer), float ve complex sayısal veri tipleridir. int sınırsız uzunlukta pozitif ve negatif tam sayıları, float noktadan sonra bir veya daha fazla ondalık sayı içeren pozitif veya negatif sayıları ve complex ise daha çok ileri düzey matematik işlemlerindeki karmaşık sayıları ifade eder.*
  ```python
  x = 8   #int
  y = 3.5   #float 
  z = 55j   #complex
  ```
  
  `Sequence Types`: *list[], ve tuple() bu gruba giren veri tipleridir. tuple ve list birden çok ögeyi tek bir değişkende saklama imkanı verir. list'ler mutabledır yani elemanlarını değiştirebilir, silebilir ve eleman ekleyebiliriz. Ama tuple'lar immutabledır, elemanlarını değiştiremeyiz.*
  ```python
  aListe = ["Kitap", 34, 41, 6, "İstanbul"]
  aTuple = ("Kitap", 34, 41, 6, "İstanbul")
  ```
  
  `set`: *list ve tuple'lar gibi birden çok ögeyi tek bir değişkende saklama imkanı verir. Ama list ve tuple'ların aksine yinelenen elemanlara izin vermez ve sıralı değillerdir. Set öğeleri değiştirilemez, ancak öğeleri kaldırabilir ve yeni öğeler ekleyebilirsiniz.*
  ```python
  mySet = {"Simit", "Peynir", "Çay"}
  ```
  
  `dict`: *dictionarydir. Veri tiplerini key ve value şeklinde tutmamıza yarar. Böylece bir mapping işlemi yapmış oluruz. Duplicate değerlere izin vermez ve mutabledır.*
  ```python
  thisdict = {
  "brand": "BMW",
  "model": "3.20",
  "year": 2022
  }
  print(thisdict)
  ```
  
  `bool`: *boolean veri tipidir. True ve False olarak iki değer alır.*
  ```python
  isEmpty = True
  isEmpty = False
  ```
  
  ## 2.Kodlama.io sitesinde değişken olarak kullanıldığını düşündüğünüz verileri, veri tipleriyle birlikte örneklendiriniz.
  
  `String`: *Kurslarım, Tüm Kurslar, Kariyer, Sık Sorulan Sorular, kurs başlıkları..*

  `int`: *Kursları tamamlama yüzdesi*

  `liste`: *Kurslarıma tıklayınca gösterilen kurslar*
  
  ## 3.Kodlama.io sitesinde şart blokları kullanıldığını düşündüğünüz kısımları örneklendiriniz ve Python dilinde bu örnekleri koda dökünüz.
  
  Tüm kurslar altında kurs bul arama çubuğunda:
  ```python
  kursBul=input() #C#
  kurslar=["2022 Yazılım Geliştirici Yetiştirme Kampı(JAVA)","2023 Yazılım Geliştirici Yetiştirme Kampı(Python&Selenium)","Yazılım Geliştirici Yetiştirme Kampı(JAVA+REACT)","Yazılım Geliştirici Yetiştirme Kampı(JavaScript)", "Yazılım Geliştirici Yetiştirme Kampı(C# + Angular)", "Yazılım Geliştirici Yetiştirme Kampı(.Net)", "Programlamaya Giriş İçin Temel Kurs"]
  if(metin=="C#"):
    print("2022 Yazılım Geliştirici Yetiştirme Kampı(C# + Angular)")
  else:
    print("Kurs bulunamadı")
  ```
    
