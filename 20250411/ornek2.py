havasicaklik=int(input("Hava sicaklığını giriniz"))
if havasicaklik<=5:
    print("SOĞUK")
elif havasicaklik>=6 and havasicaklik<=14:
    print("ILIK")
elif havasicaklik>=15:
    print("SICAK")
else:
    print("yanlış bilgi girdiniz")