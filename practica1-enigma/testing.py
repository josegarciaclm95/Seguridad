#Seguridad - Práctica 1
from enigma_classes import Rotor;
from enigma_classes import Enigma;
import unittest

class EnigmaTesting(unittest.TestCase):
	def setUp(self):
		rotor3 = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "A","V");
		rotor2 = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "A","E");
		rotor1 = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "A","Q");
		self.machine = Enigma("YRUHQSLDPXNGOKMIEBFZCWVJAT");
		self.machine.appendRotor(rotor3);
		self.machine.appendRotor(rotor2);
		self.machine.appendRotor(rotor1);
    
	def tearDown(self):
		self.machine.restart()
        
	#Pasa
	def testAAA(self):
		self.assertEqual(self.machine.startCypher("A"),"B")
		self.assertEqual(self.machine.startCypher("C"),"R")
		self.assertEqual(self.machine.startCypher("Z"),"A")
		self.assertEqual(self.machine.startCypher("S"),"N")
		self.assertEqual(self.machine.startCypher("Q"),"W")
		self.assertEqual(self.machine.startCypher("I"),"L")
	#Pasa

	def testOKI(self):
		self.machine.setKeys("OKI")
		self.assertEqual(self.machine.startCypher("A"),"W")
		self.assertEqual(self.machine.startCypher("C"),"A")
		self.assertEqual(self.machine.startCypher("Z"),"O")
		self.assertEqual(self.machine.startCypher("S"),"V")
		self.assertEqual(self.machine.startCypher("Q"),"E")
		self.assertEqual(self.machine.startCypher("I"),"E") 
	#Pasa

	def testTDBCorto(self):
		self.machine.setKeys("TDB")
		self.assertEqual(self.machine.startCypher("A"),"M")
		self.assertEqual(self.machine.startCypher("C"),"R")
		self.assertEqual(self.machine.startCypher("Z"),"F")
		self.assertEqual(self.machine.startCypher("S"),"C")
		self.assertEqual(self.machine.startCypher("Q"),"A")
		self.assertEqual(self.machine.startCypher("I"),"O") 

	def testAAA_longer_sentence(self):
		self.assertEqual(self.machine.startCypher("HOLAMUNDONOMEPUEDOCREERQUEES"),"IIBGHPRUMHLNLVTNARVVYPKNJZXQ")

	def testKFH_longer_sentence(self):
		self.machine.setKeys("KFH")
		self.assertEqual(self.machine.startCypher("HOLAMELLAMOJOSEMARIAYESTUDIOINGENIERIAINFORMATICA"),
												"XDUPUUUCUHVRFRLBHSSWGFMIZUVPLOHGCCYJXQGYOBUKOVHZT")

	def testAAA_decode(self):
		self.assertEqual(self.machine.startCypher("B"),"A")
		self.assertEqual(self.machine.startCypher("R"),"C")
		self.assertEqual(self.machine.startCypher("A"),"Z")
		self.assertEqual(self.machine.startCypher("N"),"S")
		self.assertEqual(self.machine.startCypher("W"),"Q")
		self.assertEqual(self.machine.startCypher("L"),"I")

	def testKFH_longer_sentence_decode(self):
		self.machine.setKeys("KFH")
		self.assertEqual(self.machine.startCypher("XDUPUUUCUHVRFRLBHSSWGFMIZUVPLOHGCCYJXQGYOBUKOVHZT"),
												"HOLAMELLAMOJOSEMARIAYESTUDIOINGENIERIAINFORMATICA")
    
	def testUIZ_longer_sentence_decode(self):
		self.machine.setKeys("UIZ")
		self.assertEqual(self.machine.startCypher("UCMDVHYDZKWCSTWVLYYDQNZODKRTIGPSNFHTMDERCUDHSJQFFEBKGJCLTCKVAZOUKBKU"),
                                                    "ESTAMOSAHORAMISMOENSEGURIDADDESISTEMASYESTAMOSAMARTESYMANANAESFIESTA")
	def test49caracteres(self):
		self.machine.setKeys("AAA")
		self.assertEqual(self.machine.startCypher("HOLAMUNDOMELLAMOJOSEMARIAYVOYAPROBARENCUARENTAYNU"),
                            "IIBGHPRUMVNRETAVGRRPAUKUFLJLQXKJLRFISALOXVMHWNBBX");
	def testMuchosCaracteres(self):
		self.machine.setKeys("AAA")
		self.assertEqual(self.machine.startCypher("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"),
                            "BDZGOWCXLTKSBTMCDLPBMUQOFXYHCXTGYJFLINHNXSHIUNTH");
	def testMuchosCaracteres2(self):
		self.machine.setKeys("TDB")
		self.assertEqual(self.machine.startCypher("JDLSIEURJNZMAKFLDPOEUERUNVMNXJDHEYHHHHWJXBSKQUERHBSKJNA"),
                            "PJECCUVYMVMQGVDZPBIWJGHFHZREWMYIHSCCBIDVGJOTJBFKKCHFPYD");

if __name__ == '__main__':
    unittest.main()
