otopark=int(input("Kaldığınız süreyi giriniz:"))
if otopark <1:
    print("Ödeyeceğiniz miktar:5 TL")
elif otopark >1 and otopark <5:
    print("Ödeyeceğiniz miktar:",otopark*4)
elif otopark >=5:
    print("Ödeyeceğiniz miktar:",otopark*5)
else:
    print("yanlış bilgi girdiniz")