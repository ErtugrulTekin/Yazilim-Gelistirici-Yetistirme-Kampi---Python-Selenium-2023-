  ## HTML Nedir?

  *Üst Metin İşaretleme Dili veya HTML (The HyperText Markup Language, or HTML), bir web tarayıcısında görüntülenmek üzere tasarlanmış belgeler için standart işaretleme dilidir (markup language). Basamaklı Stil Sayfaları (Cascading Style Sheets or CSS) gibi teknolojiler ve JavaScript gibi komut dosyası dilleri tarafından desteklenebilir.*

  *Genel bilinen yanlış kanının aksine HTML bir programlama dili değildir. Daha açık anlatmak gerekirse, Chrome, Firefox, Yandex gibi tarayıcıların okuyup anlamlandırdığı dil HTML dilidir.*

  *HTML, web tasarımcılarına sayfalar ve uygulamalar için yapı profilleri, bağlantılar, blok alıntılar, paragraflar ve başlıklar oluşturmalarında yardımcıdır. Bu konuda basit kod yapıları olan etiketler ve nitelikler kullanılarak web sayfaları şekillendirilebilir. HTML için aslında bir web sitesinin iskeleti denilebilir. Yani HTML kodları olmadan web sitesi kodlanamaz.*

  ## HTML Locators Nedir?

  `En yaygın locator çeşitleri`;

  * ID
  * Name
  * ClassName
  * TagName
  * LinkText
  * CssSelector
  * XPath

  *Web sitelerinde tagname’ler bulunur. Bu tagname’lerin sahip olduğu stil, name, id gibi attribute’ler vardır. Selenium’un anlayacağı şekilde nesneleri web elementlere çevirirken ilk önce id’si ve name’i var mı diye bakılır yok ise CssSelector ve Xpath ile nesneyi bulmaya çalışırız.*

  *Test otomasyonda kullanacağımız locator’lar için gerekli değerleri istediğimiz nesneye sağ tıkla ile incele(inspect) alanına tıklarız. İncele alanına tıkladıktan sonra objenin attribute’lerini görebiliriz.*

  ### `1. ID`

  *ID, web sayfasında her öğeye özgü olduğu düşünülerek öğeleri bulmanın en yaygın yoludur. Id’nin değişken olup olmadığı sayfa yenilenerek tekrar ilgili elemente ulaşıp kontrol ederek anlaşılabilir.*

  ```python
  driver.findElement(By.ID, "example_id")
  ```

  ### `2. ClassName`

  *ClassName locator, elementin class özelliği kullanılarak bulunmasını sağlar.*

  ```python
  driver.findElement(By.CLASSNAME, "example_className")
  ```

  ### `3. Name`

  *Selenium WebDriver’daki Name locator, ID gibi kullanılabilir.*

  ```python
  driver.findElement(By.NAME, "example_name")
  ```

  ### `4. Tag Name`

  *Selenium WebDriver’daki bu bulucu, div etiketi, etiket vb. gibi etiket adlarına sahip öğeleri tanımlamak için kullanılır.*

  ```python
  driver.findElements(By.TAGNAME, "a")
  driver.findElements(By.TAGNAME, "div")
  ```

  ### `5. LinkText`

  *Elementler, bağlantı metni aracılığıyla yerleştirilebilir. Aynı metnin birden çok bağlantısının bulunduğu bir senaryoda, ilk bağlantı seçilir.*

  *Örnek element;*
  ```
  <a href=”https://medium.com/@ertugrultekin98” target=”_blank”>Blog</a>
  ```
  *Elementi bulmak için linktext kullanımı;*

  ```python
  driver.findElements(By.LINKTEXT, "Blog")
  ```

  ### `6. CSS Selector`

  *Bir elementte ID ya da name ile ilgili bir bilgi yoksa veya bunlar değişken ise CSS selector ve Xpath ile elementi bulmaya çalışırız. Xpath ile karşılaştırıldığında CSS selector daha hızlı çalışmaktadır.*

  *CSS Seçicileri çeşitli biçimlerde bulunabilir:*

  * Tag ve ID
  * Tag ve Class
  * Tag ve Attribute
  * Tag, Class ve Attribute
  * Matches (Starts with, Ends with, Contains)
  * Child elementler

  ### `7. Xpath`

  *Xpath, XML ifadelerini kullanarak web sayfasındaki öğeleri bulmaya yardımcı olur.*

  *Xpath=//tagname[@Attribute=‘Value’]*

  *tagname= Hedeflediğiniz elementin etiketi, örneğin bir giriş(input) etiketini ve ya bağlantı(anchor) etiketini, vb. belirtir.*

  *attribute= ‘@‘ ön eki ve karşılık gelen değerleri ile tanımlanır. Name, ID, Class vb.olabilir.*

  *Xpath Seçicileri çeşitli biçimlerde bulunabilir:*

  * Standard Xpath
  * Contains
  * AND & OR
  * Starts-with
  * Text

  ### `8. DOM Locator`

  *Elementi ID ve Name yoluyla DOM’un “getElementById” ve “getElementsByName” gibi yöntemlerini kullanarak tanımlayabiliriz. GetElementById yöntemi bir kerede yalnızca bir öğeyi bulur, diğer yöntem ise bu adla bulunan bir dizi elementi sağlamak için kullanılır. Bir dizi elementin olması durumunda belirtilen spesifik bir öğeye erişmek için index kullanabiliriz.*

  ```
  document.getElementById("id")
  document.getElementsByNames("name")[index]
  ```

  ## Selenium'da Aksiyonlar Nedir?

  *Selenium'da kullanılan bazı yaygın aksiyonlar şunlardır:*

  * get(url): Belirtilen URL'ye gitmek için kullanılır.
  * find_element(): Belirtilen özelliklere göre bir elementi (bir metin kutusu, bir buton, bir bağlantı vb.) bulmak için kullanılır.
  * send_keys(keys) : Bir elemente metin girmek için kullanılır.
  * click() : Bir elementi tıklamak için kullanılır.
  * clear() : Bir metin kutusundaki mevcut metni silmek için kullanılır.
  * submit() : Bir formu göndermek için kullanılır.
  * back() : Önceki sayfaya dönmek için kullanılır.
  * forward() : İleri sayfaya gitmek için kullanılır.
  * refresh() : Sayfayı yenilemek için kullanılır.
  * execute_script(script) : Belirtilen JavaScript kodunu çalıştırmak için kullanılır.