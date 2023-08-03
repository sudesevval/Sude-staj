def fonksiyon(number):
    number_str = str(number)
    result = ""
    prev_is_odd = False

    for digit in number_str:
        if digit == "0":
            result += digit
        elif prev_is_odd and int(digit) % 2 != 0:
            result += "-" + digit
        else:
            result += digit

        prev_is_odd = int(digit) % 2 != 0
    return result

user_input = input("Bir sayı girin: ")
modified_number = fonksiyon(user_input)
print("Değiştirilmiş sayı:", modified_number)