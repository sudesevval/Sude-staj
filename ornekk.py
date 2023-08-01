def fonksiyon(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
number = int(input("Bir sayı girin: "))
result = fonksiyon(number)
print(result)
