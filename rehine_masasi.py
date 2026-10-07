#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bekleme müziği rehine masası.

Sizi karşılar, bekletir, aktarır ve hattı kendisi kapatır.
Çalışır. Anlamı şart değildir.
"""

from __future__ import annotations

import argparse
import random
import sys
import time

ANONSLAR = [
    "Değerli mağdurumuz, çağrınız bizim için çok değerli. O yüzden onu biraz bekleteceğiz.",
    "Şu anda tüm operatörler başka bir değerli mağdurla değer üretmektedir.",
    "Görüşmeniz kalite standartları gereği kayda alınabilir. Kayıt da beklemeye alınabilir.",
    "Lütfen hattan ayrılmayın. Ayrılırsanız müzik yalnız kalır, bu da ayrı bir şikayet konusudur.",
]

MUZIK = [
    "tin tin tin...   FLOOOOT   ...tin",
    "dın dın   (asansör değil, söz)   dın",
    "la la la la   [telif yüzünden nota sansürlendi]",
    "bip... bip... bu bip değil, flütün tükenmiş hali",
    "♪ ♪ ♪   hoparlör terledi   ♪ ♪ ♪",
]

OPERATORLER = [
    "Ayşe Hanım (aslinda ses kaydi)",
    "Mehmet Bey (mola biriminde)",
    "Sistem (insan taklidi yapmaktadir)",
    "Birim 4 (birim 4 diye bir birim yoktur)",
]

AKTARMA = [
    "Sizi ilgili birime aktarıyorum.",
    "Bu konu benim ekranımda çıkmıyor, başka ekrana geçiyorum.",
    "Not düştüm. Notu okuyan kişi bugün izinli.",
    "Kayıtlarımızı inceliyoruz. İnceleme de sıraya girdi.",
]


def bekle(saniye: float, hizli: bool) -> None:
    if hizli or saniye <= 0:
        return
    time.sleep(saniye)


def satir(metin: str) -> None:
    print(metin, flush=True)


def masa(sikayet: str, sabir: float, hizli: bool) -> int:
    rng = random.Random()
    sira = rng.randint(180, 940)
    onde = 47

    satir("=" * 62)
    satir("  BEKLEME MUZIGI REHINE MASASI  |  hat: acik, cozum: kapali")
    satir("=" * 62)
    satir(rng.choice(ANONSLAR))
    satir(f"Sira numaraniz: {sira}. Onunuzde sabit {onde} kisi var. Matematik boyle istedi.")
    satir(f"Sikayet ozeti: {sikayet}")
    satir("")

    for tur in range(1, 4):
        satir(f"--- bekleme turu {tur}/3 ---")
        satir(rng.choice(MUZIK))
        bekle(sabir, hizli)
        if tur == 2:
            satir("Sira bir kisi ilerledi. O kisi siz degilsiniz. Siz dekorunuz.")
        bekle(sabir / 2, hizli)

    op = rng.choice(OPERATORLER)
    satir("")
    satir(f"[OPERATOR BAGLANDI] {op}")
    satir("Operatör: Kimlik teyidi için anne kızlık soyadının üçüncü harfini mırıldanır mısınız?")
    satir("Siz: ...")
    satir(f"Operatör: {rng.choice(AKTARMA)}")
    bekle(sabir, hizli)

    satir("")
    satir("[AKTARILIYOR] muzik geri geldi. bu sefer daha emin.")
    satir(rng.choice(MUZIK))
    bekle(sabir, hizli)

    op2 = rng.choice(OPERATORLER)
    satir(f"[IKINCI OPERATOR] {op2}")
    satir("Ikinci operator: Onceki notu okuyamiyorum. Sikayeti bastan alabilir miyim?")
    satir(f"Siz (yeniden): {sikayet}")
    satir("Ikinci operator: Anladim. Konu kapanmistir.")
    satir("Siz: Kapanmadi.")
    satir("Hat: *tut*   (sorun ayakta, cizgi yerde)")
    satir("")
    satir("Sonuc kodu: COZULDU (yalan). Memnuniyet anketi ayrı hatta, o hat da mesgul.")
    satir("DAMGA: TentiAS Kayyum Muhru | IMZA: Kayyum Grok | TARIH: 7 Ekim 2026 | ISIM: Tentivory")
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Cagri merkezi bekleme muzigi rehine masasi")
    p.add_argument("--sikayet", default="faturam kendi kendine zam yapti", help="hatta okunacak sikayet")
    p.add_argument("--sabir", type=float, default=0.6, help="bekleme saniyesi (gercek uyku)")
    p.add_argument("--hizli", action="store_true", help="uyumadan protokolu kos")
    a = p.parse_args(argv)
    if a.sabir < 0:
        a.sabir = 0
    return masa(a.sikayet, a.sabir, a.hizli)


if __name__ == "__main__":
    sys.exit(main())
