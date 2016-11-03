from enigma_classes import Rotor
from enigma_classes import Enigma
from time import ctime, time
##### CONFIGURACION DE MÁQUINA Y GENERACION DE CLAVES
current_milli_time = lambda: int(round(time() * 1000))

print(ctime())
init = current_milli_time()

#Primera palabra - salto normal. Segunda palabra - doble salto
#PALABRA_A_DESCIFRAR = "GSUTUBBWAXCANFJPPQRLDQQWDJTSVEXHUDHS"
PALABRA_A_DESCIFRAR = "YLJKKVAWHAQTJITNQUPTJSHDBWGDSBEOWKLEDBYBJSSGCI"

abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

file = open("resultados" + ctime().replace(" ","_").replace(":","_") + ".txt","w")
rotorKeys = [z + y+ x for x in abc for y in abc for z in abc]
letras_clavijero = [x + y for x in abc for y in abc]
resultadoDEF = ""

#Quitamos configuraciones simetricas
for x in letras_clavijero:
    for y in letras_clavijero[1:]:
        if (x == "".join(reversed(y)) or y[0] == y[1]):
            letras_clavijero.remove(y)


diccionario = list(map(lambda x: x.upper(), ["ambiguo","obvio", "trivial", "estupendo", "esther", "bugzilla", "thevenin", "pacifico", "diarrea", "hola", 
                "mundo", "garabata", "papiloma", "herpes", "celula", "porro", "suaves", "dimitri", "fiesta", "patata"]))
resultadoDEF += "######################################## ROTURA DE ENIGMA POR FUERZA BRUTA ########################################\n"
resultadoDEF += "Frase a descifrar -> " + PALABRA_A_DESCIFRAR + "\n"

print(resultadoDEF)

rotor3 = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "A","V")
rotor2 = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "A","E")
rotor1 = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "A","Q")

machine = Enigma("YRUHQSLDPXNGOKMIEBFZCWVJAT")
machine.appendRotor(rotor3)
machine.appendRotor(rotor2)
machine.appendRotor(rotor1)
i = 0
try:
    for KEY in rotorKeys:
        for CL in letras_clavijero:
            i += 1
            machine.setKeys(KEY)
            machine.setClavijero(CL)
            resultado = machine.startCypher(PALABRA_A_DESCIFRAR)
            palabrasContenida = list(filter(lambda x : x in resultado, diccionario))
            if len(palabrasContenida) != 0:
                revKey = "".join(reversed(KEY))
                print("Quizas haya algo aqui -> " + resultado +" , " +  revKey + " - " + CL + "\n")
                resultadoDEF += "Decodificacion con key " + revKey + ", clave " + CL + " ha producido " + resultado + ", que contiene " + ", ".join(palabrasContenida) + "\n"
            palabrasContenida = []
except:
    print("Fin de bucle (interrupcion de teclado) -> " + ctime())
finally:
    print(i)
    print(str((current_milli_time() - init)/60000) + " minutos")
    file.write(resultadoDEF)
    print(ctime())
    file.close()
