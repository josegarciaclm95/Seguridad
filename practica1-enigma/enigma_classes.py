class Rotor:
	"""Cada rotor tiene una serie de letras (Enigma 1930) y una posicion en la se considera que comienza
	el abecedario del rotor a la hora de comparar con el abecedario normal
	"""
	def __init__(self, letters, initChar,jumpChar):
		"""Un rotor recibe su diccionario, su posicion de inicio y su carácter de salto"""
		self.letters = list(letters)
		self.setKey(initChar)
		self.jumpChar = jumpChar

	def setKey(self,key):
		"""Se establece la posición inicial del rotor y se almacena para poder reiniciar el rotor luego"""
		self.initialKey = key;
		self.first_index = Enigma.abc.index(key)

	def Move(self):
		"""Logica de movimiento del rotor.
		Si hemos pasado la posición de salto (o la siguiente a esa en el caso del doble salto)
		avisamos al siguiente rotor de que se tiene que mover
		"""
		self.first_index = (self.first_index + 1) % 26
		pos = Enigma.abc.index(self.jumpChar)
		return True if self.first_index == (pos + 1) else False
        
	def cypher(self, letter):
		"""Devolvemos la letra que corresponda en este rotor a la letra recibidad"""
		let = self.letters[(Enigma.abc.index(letter) + self.first_index) % 26]
		return Enigma.abc[(Enigma.abc.index(let)-self.first_index) % 26]

	def backCypher(self, letter):
		"""Viaje de vuelta en el proceso de cifrado"""
		inv_let = Enigma.abc[(Enigma.abc.index(letter)+self.first_index) % 26]
		return Enigma.abc[(self.letters.index(inv_let) - self.first_index) % 26]

	def restart(self):
		"""Establecemos como posición del rotor la posición inicial que se establecio al crearlo"""
		self.first_index = Enigma.abc.index(self.initialKey)

class Enigma:
	"""Clase gestora de los rotores. 
	Controla los rotores que tiene asociados y realiza de intermediara en sus comunicaciones
	"""
	abc = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

	def __init__(self, reflector_letters):
		self.rotors = []
		self.reflector = list(reflector_letters)

	def appendRotor(self, newRotor):
		"""Anade un nuevo rotor a la lista. El primer rotor es el III, el segundo es el II y el tercero es el I"""
		self.rotors.append(newRotor)
    
	def move(self):
		"""Logica de movimiento de la máquina en conjunto.
		Los rotores se comunica mediante signals booleanas que gestiona la máquina Enigma
		"""
		i = 0
		move = self.rotors[i].Move() or self.rotors[i+1].first_index == Enigma.abc.index(self.rotors[i+1].jumpChar)
		# print("Rotor " + str(i) + ", Estoy apuntando a -> " + Enigma.abc[self.rotors[i].first_index])
		# print("Se tiene que mover el rotor " + str(i+1) + " -> " + str(move))
		while(move and i < len(self.rotors)):
			i += 1
			move = self.rotors[i].Move()
			#print("Rotor " + str(i) + ", Estoy apuntando a -> " + Enigma.abc[self.rotors[i].first_index])
			#print("Se ha movido rotor " + str(i) + " Se mueve el siguiente? -> " + str(move))
    
	def setKeys(self, key):
		"""Se establece la clave de la maquina estableciendose la de cada uno de los rotores.
		Primer caracter de la clave - Posicion de inicio de rotor III (primero de la lista)
		Segundo caracter de la clave - Posicion de inicio de rotor II (segundo de la lista)...
		"""
		k = list(key)
		for i in range(len(key)):
			self.rotors[i].setKey(k[i])
        
	def startCypher(self,letter_to_cypher):
		"""Cifrado de cadenas. Pasamos el mensaje a los rotores caracter a caracter y almacenando el resultado en la variable que se 
		devuelve.
		"""
		message_cyphered = ""
		for x in letter_to_cypher:
			aux_letter = x
			self.move();
			for r in self.rotors:
				aux_letter = r.cypher(aux_letter)
			aux_letter = self.reflector[Enigma.abc.index(aux_letter)]
			for r in reversed(self.rotors):
				aux_letter = r.backCypher(aux_letter)
			message_cyphered += aux_letter
		return message_cyphered

	def restart(self):
		"""Método para restaurar la posicion de los rotores. Para pruebas. """
		for r in self.rotors:
			r.restart()
