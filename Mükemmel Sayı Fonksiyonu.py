def muk (sayi):
    liste = []
    for i in range(2,sayi+1):
        toplam = 0
        for y in range(1,i+1):
            if i % y == 0:
                toplam += y
                if toplam == i:
                    liste.append(i)
    return liste

while True:
    sayi = input("Hangi sayıya kadar olan mükemmel sayıları bulmak istersiniz ? : ")
    if sayi == "q":
        break
    else:
        sayi = int(sayi)
        print("Bu aralıktaki mükemmel sayılar: ", muk(sayi))








