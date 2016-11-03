#Seguridad - Práctica 1
from enigma_classes import Rotor
from enigma_classes import Enigma
import sys
###### CONFIGURACIÓN Y CREACIÓN DE LA MÁQUINA
if(len(sys.argv) < 4):
    raise Exception("Faltan parametros. Hay que pasar minimo una key, un mensaje y una pareja de stickers")
key = list(sys.argv[1])
message = str(sys.argv[2])
clavijero_letters = list(sys.argv[3])
rotor3 = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", key[0],"V")
rotor2 = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", key[1],"E")
rotor1 = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", key[2],"Q")

machine = Enigma("YRUHQSLDPXNGOKMIEBFZCWVJAT")
machine.setClavijero(clavijero_letters)
machine.appendRotor(rotor3)
machine.appendRotor(rotor2)
machine.appendRotor(rotor1)
coded_message = machine.startCypher(message)
print("Mensaje es " + message + ", version cifrada -> " + coded_message)
machine.restart()
print("Mensaje cifrado es es " + coded_message + ", version cifrada -> " + machine.startCypher(coded_message))

