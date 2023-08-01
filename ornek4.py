import string
parola=input('Parolanızı oluşturun: ')
rakamlar=string.digits
semboller=string.punctuation
kucuk_harfler=string.ascii_lowercase
buyuk_harfler=string.ascii_uppercase
if len(parola) in range(7,31) and parola!='parola': 
    print("Parola kabul edildi")
elif rakamlar==True and semboller==True and kucuk_harfler==True and buyuk_harfler==True:
    print("Parolanız kabul edildi")
else:
    print("parola kabul edilmedi")