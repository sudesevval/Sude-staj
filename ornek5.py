import re

def parola_sorgulama(parola):
    if len(parola) < 7 or len(parola) > 30: 
           return False 
    if not re.match(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>])', parola):
          return False
    return True
parola = input("Parolanızı oluşturun: ")
if parola_sorgulama(parola):
      print("Parola geçerli.")
else: 
      print("Parola geçerli değil. Tekrar denemelisin :)) ")





      import re
def isim_soyisim_sorgulama(isim_soyisim):
    if len(isim_soyisim) < 7 or len(isim_soyisim) > 30: 
           return False 
    if not re.match(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>])',isim_soyisim):
          return False
    return True
    sorgu = input("İsim ve Soyisim bilgilerinizi giriniz: ")
    if isim_sorgulama(sorgu):
      print("İsim ve Soyisim kabul edilmiştir.")
    else:
      print("İsim ve Soyisim geçerli değil tekrar dene :))  ")

import re

def isim_soyisim_kontrol(isim_soyisim):
    isim_soyisim_pattern = r"^[A-Z][a-zA-ZğüşıöçĞÜŞİÖÇ']+(?:\s[A-Z][a-zA-ZğüşıöçĞÜŞİÖÇ']+\s[A-Z][a-zA-ZğüşıöçĞÜŞİÖÇ']+)?$"
    return bool(re.match(isim_soyisim_pattern, isim_soyisim))
isim_soyisim = input("İsim ve soyisim giriniz (Sude ÇİLOĞLU veya Sude Şevval ÇİLOĞLU gibi): ")
if isim_soyisim_kontrol(isim_soyisim):
    print("İsim ve soyisim doğru formatta.")
else:
    print("İsim ve soyisim yanlış formatta! İsim ilk harfi büyük olmalı, soyisim tamamen büyük harflerden oluşmalıdır ve her iki alan da zorunludur.")
