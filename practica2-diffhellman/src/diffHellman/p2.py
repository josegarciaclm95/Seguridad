def ExpM (n,x,p):
    b = bin(x)[2:]

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

def ataque (n,p, alice, bob):
    i = 0
    z = None
    flag = 2
    result = [-1,-1]
    while flag != 0:
        i += 1
        deco = ExpM(n,i,p)
        if deco == alice:
            print('x de Alice: %i' % i)
            result[0] = i
            flag -=1
        if deco == bob:
            print('x de Bob: %i' % i)
            flag -=1
            result[1] = i
    return result

# Ejemplo https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange

n = 65537#5
p = 1372933 #23
xa = 5858999999#6
xb = 7888899999 #15

alice =  ExpM(n,xa,p) # 8
print('Alice: %i' % alice)

bob = ExpM(n,xb,p)
print('Bob: %i' % bob)

alice_s = ExpM(bob,xa,p)
print('Alice s: %i' % alice_s)

bob_s = ExpM(alice,xb,p)
print('Bob s: %i' % bob_s)

print('---Ataque---')
sDescifrada = ataque(n,p,alice,bob)
print('Claves Alice-Bob:' + str(sDescifrada))
print('---Comprobacion de Ataque---')
aliceAgain = ExpM(n,sDescifrada[0],p)
bobAgain = ExpM(n,sDescifrada[1],p)
print('Alice: %i' % aliceAgain)
print('Bob: %i' % bobAgain)
#print('Clave descifrada: %i' % sDescifrada)
