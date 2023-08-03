import string
def parola_sorgulama(parola):
    if len(parola) < 7 or len(parola) > 30:
        return False
    if not any(char in string.ascii_uppercase for char in parola):
        return False
    if not any(char in string.ascii_lowercase for char in parola):
        return False
    if not any(char in string.digits for char in parola):
        return False
    if not any(char in string.punctuation for char in parola):
        return False
    return True
parola = input("Parolanızı oluşturun: ")
if parola_sorgulama(parola):
    print("Parola geçerli.")
else:
    print("Parola geçerli değil. Tekrar denemelisin :)) ")
