import re

def isim_soyisim_kontrol(isim_soyisim):
    isim_soyisim_pattern = r'^[A-Z][a-zA-Z]*\s|[A-Z][a-zA-Z]*\s|^[A-ZÜÖŞİÇĞ]*$'
                           
    return bool(re.match(isim_soyisim_pattern, isim_soyisim))
isim_soyisim = input("İsim ve soyisim giriniz (örn: Cemre MENGU veya Sude Sevval CILOGLU): ")
if isim_soyisim_kontrol(isim_soyisim):
    print("İsim ve soyisim doğru formatta.")
else:
    print("İsim ve soyisim yanlış formatta! İsim ilk harfi büyük olmalı, soyisim tamamen büyük harflerden oluşmalı, isim ve soyisim alanları zorunlu olmalıdır ve ikinci isim varsa ilk harfi büyük olmalıdır.")

