
class NodoL: 
	def _init_(self, palabra = None, indice = None, siguiente = None):
		self.palabra = palabra
		self.indice = indice
		self.siguiente = siguiente

	def _str_(self):
		return "%s %s" %(self.palabra, self.indice)


class ListaS:
	def _init_ (self):
		self.inicio = None
		self.fin = None

	def agregar(self, elemento):
		if self.inicio == None:
			self.inicio = elemento

		if self.fin != None:
			self.fin.siguiente = elemento

		self.fin = None

if __name__ == "_main_":
	ls = ListaS()
	while (True):
		print("---Menu--- \n"+
			"1. Agregar Palabra")
		num = input("Ingrese la opcion: ")
		if num == "1":
			palabra = input("ingrese la palabra: ")
			indice = input("ingrese indice: ")
			nodo = NodoL(palabra, indice)
			ls.agregar(nodo)



