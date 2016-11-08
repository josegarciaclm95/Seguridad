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
            print('x de Alice: %i' % i)
        if deco == bob:
            print('x de Bob: %i' % i)

# Ejemplo https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange

n = int(7245627542842336859)  #65537 #5
p = int(3523269789483225643)  #1372933 #23

'''
xa = 2930009534032416290
xb = 6290936979721568605

alice =  ExpM(n,xa,p) # 8
print('Alice: %i' % alice)

bob = ExpM(n,xb,p)
print('Bob: %i' % bob)

alice_s = ExpM(bob,xa,p)
print('Alice s: %i' % alice_s)

bob_s = ExpM(alice,xb,p)
print('Bob s: %i' % bob_s)
'''

alice = int(2930009534032416290)#6
bob = int(6290936979721568605) #15 # Bob el más grande siempre.


def espacio(number):
    number *= 10000000
    while True:
        print('---Ataque de %i a %i ---' % (number, number + 10000000))
        ataque(n,p,alice,bob,number,number + 10000000)
        number += 40000000

p_list = []

if __name__ == '__main__':
    for number in range(4):
        p = Process(target=espacio, args=(number,))
        p_list.append(p)

for p in p_list:
    p.start()