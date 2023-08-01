def faktoriyel(x):
    if x == 0:
        return 1
    else:
        return x * faktoriyel(x-1)
