"""
A şirketinin sattığı bilgisayarın bazılarının bozuk olduğu tespit edilmiştir.
Bilgisyar üreten 3 şirket (A, B ve C) olduğunu varsayımı altında,
bu şirketlerin bilgisayar üretim miktarı ve bozuk üretim olasılıkları şu şekildedir:

Toplam Üretim Yüzdesi P(A)=0.40 P(B)=0.40 P(C)=0.20

Hatalı Üretim Olasılığı

P(D|A)=0.015 P(D|B)=0.020 P(D|C)=0.010

Rastgele seçilen bir bozuk bir bilgisayarın B şirketi tarafından üretilme olasılığı nedir?
"""

bozuk_b_pc = 0.40 * 0.020
tüm_bozuklar = (0.40 * 0.015) + (0.40*0.020) + (0.20*0.010)

olasılık = bozuk_b_pc/tüm_bozuklar

print(olasılık)