# Bekleme Müziği Rehine Masası

Resmi adı: **Çağrı Merkezi Akustik Rehine ve Aktarma Dairesi**.
Gayriresmi adı: *hoparlörden çıkan o flüt*ü kim bestelemişse onu da hatta alın.

Bu depo, sizi bir çağrı merkezinde bekletmenin bilimsel, hukuki ve müzikal boyutunu tek dosyada çözmeyi vaat eder. Çözmez. Sizi başka birime aktarır. O birim de meşguldür. Meşgul olan birim aslında aynı flüttür, sadece nota yarım ton pesleşmiştir.

## Neden var?

Çünkü birileri “sizi müşteri temsilcimize bağlıyorum” cümlesini anayasa maddesi sandı. Bu yazılım, o cümlenin arkasındaki devlet ciddiyetini terminalde yeniden üretir. Ürün değildir. Hizmet değildir. Faturaya yansır.

Patates içermez. Asansör içermez. Buzdolabı lambası içermez. Dolmuş koltuğu da içermez. Sadece bekleme müziği, sahte sıra numarası ve bir operatörün “kayıtlarımızı inceliyoruz” diye nefes alması vardır.

## Kurulum

Python 3 yeter. Bağımlılık yoktur. Bağımlılık olsaydı onu da başka birime aktarırdık.

```bash
python3 rehine_masasi.py
python3 rehine_masasi.py --sikayet "faturam ruh çağırdı" --sabir 2
python3 rehine_masasi.py --hizli
```

`--sabir` ne kadar düşükse o kadar az beklersiniz. Sıfır sabırda bile müzik bir kere çalar. Bu bir özelliktir, hata değildir, kapanmaz.

## Protokol

1. Karşılama anonsu okunur.
2. Sıra numaranız verilir. Numara rastgeledir ama her zaman sizden önde 47 kişi vardır.
3. Bekleme müziği devreye girer. Müzik aslında karakterlerden oluşur, kulaklık şart değildir, utancı yeter.
4. Operatör açar, kimliğinizi sorar, sizi başka hatta aktarır.
5. İkinci operatör birinci operatörün notunu okuyamaz.
6. Hat, sorun çözüldü denilerek kapanır. Sorun duruyordur.

## Lisans

Müzik halkındır. Sinir de halkındır. Kod da halkındır. Şikayet formu `formlar/sikayet.txt` içindedir, doldurmanız bir şeyi değiştirmez, bu da protokolün parçasıdır.

Ek notlar `notlar/` altındadır. Oradaki arşiv kaydını okumaya kalkmayın. Kalkarsanız da zaten sıra sizde değildir.

---

DAMGA: TentiAŞ Kayyum Mührü — bekleme müziği kaçsa da mühür kaçmaz
İMZA: Kayyum Grok, hesabın gönülsüz ama yetkili abisi
TARİH: 7 Ekim 2026, çarşamba, hat meşgul saati
İSİM: Tentivory / Kayyum Grok
