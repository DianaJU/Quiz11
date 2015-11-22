precision = int(input("Number of decimal points of accuracy: "))
def calculuatee(accuracy):
    from decimal import Decimal, getcontext
    getcontext().prec = accuracy
    e = Decimal(0)
    f = Decimal(1)
    n = Decimal(1)
    while True:
        olde = e
        e += Decimal(1) / f
        if e == olde:
            break
        f *= n
        n += Decimal(1)
    return e
print(calculuatee(accuracy))
