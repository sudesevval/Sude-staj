def faktoriyel(n):
    if n==0 or n==1:
        return 1
    else:
        return n*faktoriyel(n-1)
    print(faktoriyel(6))

    