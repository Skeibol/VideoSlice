def greatestCommonDenominator(a,b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return int(a)

