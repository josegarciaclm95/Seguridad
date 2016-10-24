from enigma_classes import Rotor
from enigma_classes import Enigma
from time import ctime
##### CONFIGURACION DE MÁQUINA Y GENERACION DE CLAVES

print(ctime())
PALABRA_A_DESCIFRAR = "GSUTUBBWAXCANFJPPQRLDQQWDJTSVEXHUDHS"
#PALABRA_A_DESCIFRAR = "BYLQFPMX"
abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
file = open("resultados2.txt","w")
rotorKeys = [x + y + z for x in abc for y in abc for z in abc]
letras_clavijero = [x + y for x in abc for y in abc if x != y]

#Quitamos configuraciones simetricas
for x in letras_clavijero:
    for y in letras_clavijero:
        if (x == "".join(reversed(y))):
            letras_clavijero.remove(y)

diccionario = list(map(lambda x: x.upper(), ["ambiguo","obvio", "trivial", "estupendo", "esther", "bugzilla", "thevenin", "pacifico", "diarrea", "hola", 
                "mundo", "garabata", "papiloma", "herpes", "celula", "porro", "suaves", "dimitri", "fiesta", "patata"]))

def writeToFile(result,key,cl, words):
    #print("Decodificacion con key " + key + ", clave " + cl + " ha producido " + result + ", que contiene " + ", ".join(words) + "\n")
    file.write("Decodificacion con key " + key + ", clave " + cl + " ha producido " + result + ", que contiene " + ", ".join(words) + "\n")

file.write("######################################## ROTURA DE ENIGMA POR FUERZA BRUTA ########################################\n")
file.write("Frase a descifrar -> " + PALABRA_A_DESCIFRAR + "\n")
print("######################################## ROTURA DE ENIGMA POR FUERZA BRUTA ########################################\n")
print("Frase a descifrar -> " + PALABRA_A_DESCIFRAR + "\n")

rotor3 = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "A","V")
rotor2 = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "A","E")
rotor1 = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "A","Q")

machine = Enigma("YRUHQSLDPXNGOKMIEBFZCWVJAT")
machine.appendRotor(rotor3)
machine.appendRotor(rotor2)
machine.appendRotor(rotor1)

for KEY in rotorKeys:
    machine.setKeys(KEY)
    for CL in letras_clavijero:
        #print(key + " - " + cl)
        machine.setClavijero(([CL],))
        #print(PALABRA_A_DESCIFRAR)
        resultado = machine.startCypher(PALABRA_A_DESCIFRAR)
        #print(resultado)
        palabrasContenida = list(filter(lambda x : x in resultado, diccionario))
        if len(palabrasContenida) != 0:
            #print(ctime())
            #print("Quizas haya algo aqui -> " + resultado + " \n")
            writeToFile(resultado, KEY, CL, palabrasContenida)
        palabrasContenida = []
    if KEY == "MMM":
        print(KEY + " \n")

print(ctime())
file.close()

