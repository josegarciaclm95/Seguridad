#Seguridad - Práctica 1
from enigma_classes import Rotor
from enigma_classes import Enigma
import sys
######################### TODOOOOOOOOOOOOOOOOOOOOOOOOOO
## CAMBIAR LOGICA DE MOVIMIENTO
#rotor2 = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE","A",None);
#rotor3 = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO","A",rotor2);
#print(rotor3.cypher("A"));
key = list(sys.argv[1])
message = str(sys.argv[2])
rotor3 = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", key[0],"V")
rotor2 = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", key[1],"E")
rotor1 = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", key[2],"Q")

machine = Enigma("YRUHQSLDPXNGOKMIEBFZCWVJAT")
machine.appendRotor(rotor3)
machine.appendRotor(rotor2)
machine.appendRotor(rotor1)
coded_message = machine.startCypher(message)
print("Mensaje es " + message + ", version cifrada -> " + coded_message)
machine.restart()
print("Mensaje cifrado es es " + coded_message + ", version cifrada -> " + machine.startCypher(coded_message))

# print("Mensaje codificado es IIBGHPRUMHLNLVTNARVVYPKNJZXQ, version decodificada -> ",machine.startCypher("IIBGHPRUMHLNLVTNARVVYPKNJZXQ"))
# machine.setKeys("POF")
# print("Mensaje es HOLAMELLAMOJOSEMARIAYESTUDIOINGENIERIAINFORMATICA, version cifrada -> " + machine.startCypher("HOLAMELLAMOJOSEMARIAYESTUDIOINGENIERIAINFORMATICA"));
# machine.restart();
# print("Mensaje es VYZLWTEKZEBDWTLUTHDWUNUZHZLNMBPYIDMGUKOYPABVOFCRS, version cifrada -> " + machine.startCypher("VYZLWTEKZEBDWTLUTHDWUNUZHZLNMBPYIDMGUKOYPABVOFCRS"));


#print(rotor3);


