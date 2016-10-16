class Rotor:
    """Cada rotor tiene una serie de letras (Enigma 1930) y una posicion en la se considera que comienza
    el abecedario del rotor a la hora de comparar con el abecedario normal"""
    def __init__(self, letters, initChar,jumpChar):
        self.letters = list(letters)
        self.setKey(initChar)
        self.jumpChar = jumpChar

    def setKey(self,key):
        self.initialKey = key;
        self.first_index = Enigma.abc.index(key)

    def Move(self):
        self.first_index = (self.first_index + 1) % 26
        return True if self.first_index == (Enigma.abc.index(self.jumpChar) + 1) else False
        
    def cypher(self, letter):
        let = self.letters[(Enigma.abc.index(letter) + self.first_index) % 26]
        return Enigma.abc[(Enigma.abc.index(let)-self.first_index) % 26]

    def backCypher(self, letter):
        inv_let = Enigma.abc[(Enigma.abc.index(letter)+self.first_index) % 26]
        return Enigma.abc[(self.letters.index(inv_let) - self.first_index) % 26]

    def restart(self):
        self.first_index = Enigma.abc.index(self.initialKey)

class Enigma:
    abc = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ");
    
    def __init__(self, reflector_letters):
        self.rotors = []
        self.reflector = list(reflector_letters)

    def appendRotor(self, newRotor):
        self.rotors.append(newRotor)
    
    def move(self):
        i = 0
        move = self.rotors[i].Move()
        print("Rotor " + str(i) + ", Estoy apuntando a -> " + Enigma.abc[self.rotors[i].first_index])
        print("Se tiene que mover el rotor " + str(i+1) + " -> " + str(move))
        while(move and i < len(self.rotors)):
            i += 1
            move = self.rotors[i].Move()
            print("Rotor " + str(i) + ", Estoy apuntando a -> " + Enigma.abc[self.rotors[i].first_index])
            print("Se ha movido rotor " + str(i) + " Se mueve el siguiente? -> " + str(move))
    
    def setKeys(self, key):
        k = list(key)
        for i in range(len(key)):
            self.rotors[i].setKey(k[i])
        
    def startCypher(self,letter_to_cypher):
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
        for r in self.rotors:
            r.restart()
            