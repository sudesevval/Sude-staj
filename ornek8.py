def fonksiyon(sayi):
    sayi_str = str(sayi)
    yeni_str = ""
    i = 0
    while i < len(sayi_str) - 1:
        if int(sayi_str[i]) % 2 == 1 and int(sayi_str[i + 1]) % 2 == 1:
            yeni_str += sayi_str[i] + '-'
        else:
            yeni_str += sayi_str[i]
        i += 1
    yeni_str += sayi_str[i]
    return yeni_str
sayi = input("Bir sayı girin: ")
sonuc = fonksiyon(sayi)
print("Sonuç:", sonuc)
