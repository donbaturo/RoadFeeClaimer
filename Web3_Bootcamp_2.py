# Ulaşım aracına ait sahip ve numara gibi veriler araç sınıflarında tutuluyor.
# Ödeme alacak kurumu yani gişeyi ilgilendiren mevcut bakiye ve araca özel ücret gişe sınıfında tutuluyor.
# Her araç için ödeme tarih, saat, eski ve yeni bakiye verisini içeren dizilerden oluşan bir kayıt dizisi tutuluyor.
# Geçiş metodu her bir geçiş işlemini temsil ediyor ve ödeme metoduyla kayıt alırken ücreti tahsil ediyor.

# Gişe superclass.

class Gise:

    gunluk_ciro = 0
    numara_kayit = []

# Gelen objeye ait tüm özelliklerin düzenli bir şekilde yazıldığı metod.

    def print_arac(self):
        if self.bakiye < 0:
            print("####################")
            print("Sistemde borcunuz bulunmaktadır!")
            print("####################")

        print("####################")
        print("Aracın güncel bakiyesi:", self.bakiye)
        print("Araç sahibinin ismi:", self.isim)
        print("Araç sahibinin soyismi:", self.soyisim)
        print("Araca ait HGS numarası:", self.numara)
        print("Araca ait tek geçişlik ücret tarifesi:", self.ucret)
        print("Araç çeşidi:", self.cesit)
        print("####################")

# Gelen objeye ait tüm geçişlerin düzenli bir şekilde yazıldığı metod.

    def print_gecis(self):
        for i in range(0, self.gecis_say):
            print(f"{i+1}. geçişe ait bilgiler:", self.kayit[i])

# Ödeme metodu. Bakiyeyi ücret kadar azaltarak günlük ciroyu artırıyor.

    def odeme(self):

        self.bakiye -= self.ucret
        Gise.gunluk_ciro += self.ucret

# Geçiş metodu. İçerisinde ödeme metodunu çağırıyor ve ekle listesini oluşturarak bu listeyi tüm kayıtlara ekliyor.

    def gecis(self):

        ekle = []
        ekle.append(input("Geçiş tarihini giriniz.\n"))
        ekle.append(f"Geçiş öncesi bakiye: {self.bakiye}")
        self.odeme()
        ekle.append(f"Geçiş sonrası bakiye: {self.bakiye}")
        self.kayit.append(ekle)
        self.gecis_say += 1

# Otomobil sınıfı.

class Otomobil(Gise):

    def __init__(self):

        self.gecis_say = 0
        self.cesit = "Otomobil"
        self.numara = Gise.numara_kayit[toplam_gecis]
        self.isim = input("Otomobilin sahibinin ismini giriniz.\n")
        self.soyisim = input("Otomobilin sahibinin soyismini giriniz.\n")
        self.bakiye = float(input("Aracın mevcut bakiyesini giriniz.\n"))
        self.ucret = float(input("Geçiş ücretini giriniz.\n"))
        self.kayit = []

        super(Otomobil, self).__init__()

# Minibüs sınıfı.

class Minibus(Gise):

    def __init__(self):

        self.gecis_say = 0
        self.cesit = "Minibüs"
        self.numara = Gise.numara_kayit[toplam_gecis]
        self.isim = input("Minibüs sahibinin ismini giriniz.\n")
        self.soyisim = input("Minibüs sahibinin soyismini giriniz.\n")
        self.bakiye = float(input("Aracın mevcut bakiyesini giriniz.\n"))
        self.ucret = float(input("Geçiş ücretini giriniz.\n"))
        self.kayit = []

        super(Minibus, self).__init__()

# Otobüs sınıfı.

class Otobus(Gise):

    def __init__(self):

        self.gecis_say = 0
        self.cesit = "Otobüs"
        self.numara = Gise.numara_kayit[toplam_gecis]
        self.isim = input("Otobüsün sahibinin ismini giriniz.\n")
        self.soyisim = input("Otobüsün sahibinin soyismini giriniz.\n")
        self.bakiye = float(input("Aracın mevcut bakiyesini giriniz.\n"))
        self.ucret = float(input("Geçiş ücretini giriniz.\n"))
        self.kayit = []

        super(Otobus, self).__init__()

# HGS numarasının daha önce sisteme kayıt olup olmadığını kontrol eden fonksiyon.
# Eğer numara daha önce kaydedildiyse False, edilmediyse True döndürüyor.
# Bu çıktıya göre yeni bir kayıt açılıyor veya menüye geri dönülüyor.

def numaradan_bul(numara):
    for i in range(0, toplam_gecis):
        if numara ==  gecen_araclar[i].numara:
           return gecen_araclar[i]

def numara_kontrol():

    numara = int(input("Araca ait HGS numarasını giriniz.\n"))
    cikti = True

    for i in range(0, toplam_gecis):
        if Gise.numara_kayit[i] == numara:

            cikti = False

            secim_2 = int(input(f"{numara} numaralı araca ait kayıt bulundu, geçiş eklemek için 1'i menüye dönmek için 2'yi tuşlayın.\n"))
            if secim_2 == 1:
                Gise.gecis(numaradan_bul(numara))
            elif secim_2 == 2:
                break

    if cikti == True:
        Gise.numara_kayit.append(numara)

    return cikti

def calistir():

    print("\nHGS raporlama arayüzüne hoşgeldiniz.\n")

# Program başlamadan önce gereken tanımlamalar.
# Seçim için secim, sayım için toplam_gecis ve araç geçiş kaydı için gecen_araclar dizisi tanımlanıyor.

    secim = 1
    toplam_gecis = 0
    gecen_araclar = []

# gecen_araclar dediğim listeye her seferinde yeni bir araç tanımı yapılıyor.
# Listede yerini alan araç daha sonra Gise sınıfının içinde bulunan gecis metoduna parametre olarak gönderiliyor.
# toplam_gecis artarak geçen araçları sayıyor ve program sonlandığında for döngüsü içinde rapor yazdırılıyor.
# Her geçiş işleminde Gise'nin bir attribute'u olan gunluk_ciro objenin geçiş ücreti kadar artırılıyor.

    while secim == 1 or secim == 2 or secim == 3 :

        secim = int(input("--Menü--\nOtomobil: 1\nMinibüs: 2\nOtobüs: 3\nÇıkış: Herhangi diğer sayı.\n\n"))

        if secim == 1:
            if numara_kontrol() is True:
                gecen_araclar.append(Otomobil())
                Gise.gecis(gecen_araclar[toplam_gecis])
                toplam_gecis += 1

        if secim == 2:
            if numara_kontrol() is True:
                gecen_araclar.append(Minibus())
                Gise.gecis(gecen_araclar[toplam_gecis])
                toplam_gecis += 1

        if secim == 3:
            if numara_kontrol() is True:
                gecen_araclar.append(Otobus())
                Gise.gecis(gecen_araclar[toplam_gecis])
                toplam_gecis += 1

# Sisteme yapılan tüm kayıt yazdırılıyor.

    for i in range(0, toplam_gecis):

        print(f"Kayıtlardaki {i+1}. araca ait bilgiler:\n")
        Gise.print_arac(gecen_araclar[i])
        Gise.print_gecis(gecen_araclar[i])

# Günlük ciro yazılıyor ve programın sonlandığı belirtiliyor.

    print("\nGişeye ait günlük ciro: ", Gise.gunluk_ciro, "\n")
    print("Çıkış yapılıyor.")
