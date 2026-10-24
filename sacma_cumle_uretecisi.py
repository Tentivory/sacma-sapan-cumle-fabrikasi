#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sacma Sapan Cumle Fabrikasi
Bu program, insanligin en buyuk sorununa cozum uretir:
Anlamsiz ama komik Turkce cumleler uretmek.
Ciddiyetle calisir. Gercekten.
"""

import random
import time

# Konu basliklari
konular = [
    "komşunun kedisi",
    "buzdolabının içindeki yoğurt",
    "trafik ışığı",
    "uzaydan gelen misafir",
    "kahve fincanının dibindeki tortu",
    "kapı zili",
    "çorap çekmecesi",
    "wifi sinyali",
    "asansör müziği",
    "televizyon kumandası"
]

# Eylemler
eylemler = [
    "felsefe yapıyor",
    "gizli bir toplantı düzenliyor",
    "neden var olduğunu sorguluyor",
    "dans ediyor",
    "şiir yazıyor",
    "uyuyor ama rüyasında vergi ödüyor",
    "komplo teorisi üretiyor",
    "sadece bakıyor ve yargılıyor",
    "kaybolmuş ve yol sormuyor",
    "mutluluk arıyor ama yanlış yerde"
]

# Yerler
yerler = [
    "mutfak tezgahının altında",
    "balkonun köşesinde",
    "otobüs durağında",
    "rüyaların derinliklerinde",
    "çamaşır makinesinin içinde",
    "kitaplığın arkasında",
    "gökyüzünde bir yerde",
    "cüzdanın içinde",
    "telefonun şarj kablosunun arasında",
    "zamanın akışında"
]

def sacma_cumle_uret():
    konu = random.choice(konular)
    eylem = random.choice(eylemler)
    yer = random.choice(yerler)
    
    # Bazen ekstra saçmalık ekle
    ekstra = random.choice([
        "Ama kimse fark etmiyor.",
        "Bilim bunu henüz açıklayamıyor.",
        "Bu yüzden dünya dönüyor.",
        "Kesinlikle mantıklı.",
        "Deneyin, görürsünüz.",
        ""
    ])
    
    cumle = f"{konu.capitalize()} {yer} {eylem}. {ekstra}"
    return cumle.strip()

def fabrika_calistir(adet=5):
    print("Sacma Sapan Cumle Fabrikasi devreye giriyor...")
    print("Lütfen bekleyin, saçmalık üretiliyor. Bu iş ciddi.")
    time.sleep(1.5)
    
    for i in range(adet):
        print(f"\n[{i+1}] {sacma_cumle_uret()}")
        time.sleep(0.7)
    
    print("\nFabrika görevini tamamladı. Daha fazla saçmalık için tekrar çalıştırın.")
    print("Uyarı: Bu cümleler gerçek hayatta kullanılırsa sorumluluk size aittir.")

if __name__ == "__main__":
    fabrika_calistir(7)

# Gizli not: Bu satırlar arasında bir şey saklı olabilir. Veya olmayabilir.
# base64: VGltcmluIGtlbHkgb2xkdXIgZGVkaQ==  (decode edersen ne çıkar bilmiyorum)
