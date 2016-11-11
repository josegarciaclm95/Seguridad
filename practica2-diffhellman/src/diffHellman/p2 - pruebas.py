from multiprocessing import Process

def ExpM (n,x,p):
    #b = bin(x)[2:]
    b ="{0:b}".format(x)


    final = 1
    lenb = len(b) - 1
    n %= p
    if b[lenb] == '1':
        final = n
    while (lenb != 0):
        n = (n*n) % p
        lenb -= 1
        if b[lenb] == '1':
            final *= n
    return (final % p)

def ataque (n,p, alice, bob, i,j):
    while i != j :
        i += 1
        deco = ExpM(n,i,p)
        if deco == alice:
            print('x de Jose: %i' % i)
        if deco == bob:
            print('x de Dani: %i' % i)

# Ejemplo https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange

n = int(33)  #65537 #5
p = int(1999)  #1372933 #23
xjose = int(6041)
resJose = ExpM(n,xjose,p)
print('Resultado Jose: %i' % resJose)

xdani = int(6111)
resDani = ExpM(n,xdani,p)
print('Resultado Dani: %i' % resDani)

resJose_s = ExpM(resDani,xjose,p)
print('Resultado secreto Jose: %i' % resJose_s)

resDani_s = ExpM(resJose,xdani,p)
print('Resultado secreto Dani: %i' % resDani_s)
