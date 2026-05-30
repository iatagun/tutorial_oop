## test.py ve test2.py Adim Adim Aciklama

Bu bolumde dosyalarda yapilanlar adim adim, mekanik ve ogretici bir sekilde anlatilir.
Her adimda iki sey var:
- Ne yapiliyor?
- Neden onemli?

### test.py

1. `Phone` sinifi tanimlanir.
   - Neden onemli: Sinif, benzer nesneler icin bir sablon gorevi gorur.
2. `__init__(self, name, number)` ile telefon nesnesine `name` ve `number` atanir.
   - Neden onemli: Her yeni nesne olusurken temel bilgiler otomatik yuklenir.
3. `dial()` metodu, `"{isim} is dialing..."` yazdirir.
   - Neden onemli: Nesnenin bir davranisini metoda donusturme ornegi.
4. `call()` metodu, `"{isim} is calling..."` yazdirir.
   - Neden onemli: Bir sinifta birden fazla davranis tanimlanabilecegini gosterir.
5. `add_number(name, new_number)` metodu:
   - `self.name` alanini yeni isimle gunceller.
   - `self.number` alanini yeni numarayla gunceller.
   - bilgi mesaji dondurur.
   - Neden onemli: Nesnenin durumunun sonradan degistirilebildigini gosterir.
6. `test = Phone("Annem", "1234567890")` ile bir nesne olusturulur.
   - Neden onemli: Sinif tanimi tek basina yetmez; kullanmak icin nesne uretilir.
7. `test.call()` cagrilir ve arama mesaji yazdirilir.
   - Neden onemli: Metot cagirma pratigi.
8. `test.dial()` cagrilir ve cevirme mesaji yazdirilir.
   - Neden onemli: Ayni nesne uzerinden farkli metotlarin cagrilmasi.
9. `test.add_number("babam", "0987654321")` ile bilgiler guncellenir.
   - Neden onemli: Nesnenin ic verisi (state) degisir.
10. Guncellenen `test.name` ve `test.number` ekrana yazdirilir.
    - Neden onemli: Degisimin gercekten oldugunu dogrulama adimi.
11. `test.dial()` tekrar cagrilir; bu kez guncel isimle yazdirir.
    - Neden onemli: Metotlar her zaman nesnenin guncel verisiyle calisir.
12. `Smartphone(Phone)` sinifi tanimlanir (kalitim).
    - Neden onemli: Kod tekrarini azaltir; var olan ozellikler yeniden kullanilir.
13. `Smartphone.__init__` icinde `super().__init__(name, number)` ile ust sinif kurucusu cagrilir.
    - Neden onemli: Alt sinif, ust sinifin kurulumunu dogru sekilde devralir.
14. `brand` ozelligi eklenir.
    - Neden onemli: Alt sinif, kendi ek ozelliklerini tanimlayabilir.
15. `browse()` metodu, internette gezinme mesaji yazdirir.
    - Neden onemli: Alt sinifa yeni davranis ekleme ornegi.
16. `iphone = Smartphone("Annem", "1234567890", "iPhone")` olusturulur.
    - Neden onemli: Kalitimli siniftan nesne uretimi gorulur.
17. `iphone.call()`, `iphone.dial()`, `iphone.browse()` cagrilariyla hem miras gelen hem yeni metotlar calistirilir.
    - Neden onemli: Bir nesnede hem ust sinif hem alt sinif davranislari birlikte calisir.

### test2.py

1. `Point` sinifi tanimlanir.
    - Neden onemli: Matematiksel bir noktayi nesne olarak modellemeyi ogreniriz.
2. `__init__(self, x=0, y=0)`:
    - `x` ve `y` koordinatlari atanir.
    - `coords` adli tuple olusturulur.
    - Neden onemli: Varsayilan degerlerle (0,0) esnek nesne uretimi saglanir.
3. `move(x, y)` metodu, mevcut noktayi verilen kadar kaydirir (`+=`).
    - Neden onemli: Nesne durumunu adim adim degistirme pratigi.
4. `__add__(other)` iki noktayi toplar ve yeni `Point` dondurur.
    - Neden onemli: `+` operatorunu sinifa ozel anlamiyla kullanmayi ogreniriz.
5. `__sub__(other)` iki noktayi cikarir ve yeni `Point` dondurur.
    - Neden onemli: `-` operatoru icin benzer mantik kurulur.
6. `__mul__(other)` koordinatlari carpar ve yeni `Point` dondurur.
    - Neden onemli: Operator asiri yukleme (overloading) farkli operatorlere genisletilir.
7. `length()` metodu noktanin orijine uzakligini hesaplar: `sqrt(x**2 + y**2)`.
    - Neden onemli: Karsilastirma icin ortak bir sayisal olcu uretilir.
8. Karsilastirma metotlari tanimlanir:
    - `__gt__`, `__ge__`, `__lt__`, `__le__` uzunluga gore karsilastirir.
    - `__eq__` koordinatlar birebir esit mi kontrol eder.
    - Neden onemli: `>`, `<`, `==` gibi ifadeler nesneyle dogal sekilde calisir.
9. `__str__` metodu, nesneyi `Point(x, y)` formatinda yazdirilabilir hale getirir.
    - Neden onemli: Debug ve ekrana yazdirma daha okunakli olur.
10. `p1`, `p2`, `p3`, `p4` nesneleri olusturulur.
     - Neden onemli: Farkli ornekler uzerinden metotlar test edilir.
11. `print(p1)` ile `__str__` otomatik cagrilir.
     - Neden onemli: Dunder metotlarin Python tarafindan otomatik kullanildigini goruruz.
12. `print(p1 + p2)`, `print(p1 - p2)`, `print(p1 * p2)` ile operator asiri yukleme metotlari calisir.
     - Neden onemli: Operatorlerin arkasinda gercekte bir metot cagrisi oldugu netlesir.
13. `print(p1 > p2)`, `>=`, `<`, `<=`, `==` ile karsilastirma metotlari calisir.
     - Neden onemli: Nesneleri kendi kurallarimiza gore karsilastirabiliriz.
14. `print(p1 == Point(3,4))` ile yeni olusturulan bir nesneye esitlik kontrolu yapilir.
     - Neden onemli: Referans esitligi yerine icerik esitligi kurali yazilmis olur.
15. Dosyanin son notu: Dunder metotlari Python tarafindan operatorler veya `print` gibi yapilar kullanilinca otomatik tetiklenir.
     - Neden onemli: Bu bilgi, sinif tasarlarken dilin nasil davrandigini anlamayi saglar.

### 5 Dakikada Tekrar

1. `test.py` bize sinif + nesne mantigini gosterir.
2. `__init__`, bir nesne olusurken ilk degerleri atar.
3. Metotlar (`call`, `dial`) nesnenin davranislarini temsil eder.
4. Bir metot (`add_number`) ile nesnenin verisi sonradan degistirilebilir.
5. Kalitimda (`Smartphone(Phone)`), alt sinif ust sinifin ozelliklerini alir.
6. `super()` alt sinifta ust sinif kurulumunu calistirmak icin kullanilir.
7. Alt sinif kendi yeni ozelligini (`brand`) ve metodunu (`browse`) ekleyebilir.
8. `test2.py` operator asiri yuklemeyi (dunder metotlari) gosterir.
9. `__add__`, `__sub__`, `__mul__` ile `+`, `-`, `*` operatorleri sinifa ozel davranir.
10. `__gt__`, `__lt__`, `__eq__` ile nesneler dogal sekilde karsilastirilir.
11. `__str__`, `print(nesne)` ciktisini okunur hale getirir.
12. Kisa ders: OOP'de sinif tasarimi, veriyi ve davranisi birlikte duzenli bir yapiya koyar.