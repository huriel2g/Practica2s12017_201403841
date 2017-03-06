

class NodoL: 
	def _init_(self, palabra, indice, siguiente):
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


indice = 0
#Realizando la conexion con Netbeans
from flask import Flask, request, Response
app = Flask("EDD_Practica2") 
ls = ListaS()

@app.route('/agregarLista',methods=['POST'])  
def hello():
	palabra = str(request.form['palabra'])
	self.indice = indice + 1
	nodo = NodoL(palabra, indice, None)
	ls.agregar(nodo)
	return "Se agrego a: " + str(palabra) +"con indice: "+ str(indice) +"!"

@app.route("/e")
def hellof():
	return "Hello World2!"

if __name__ == "__main__":
  app.run(debug=True, host='127.0.0.1')