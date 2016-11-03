def ExponenciacionModular(n,x,p):
    z, arrastre, a, c, i = 1, -1, 1, -1, 0
    """
    arrastre = -1
    a = 1
    c = -1
    i = 0
    """
    while(x != 0):
        i += 1
        c = x % 2
        x = x // 2
        arrastre = (n ** a) % p
        if (c == 1):
            z = (z * arrastre) % p
        a *= 2
    return z

print(ExponenciacionModular(33,47,1999))