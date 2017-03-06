

"""---------------Lista Simple-----------------"""
class NodoL: 
	def __init__(self):
		self.palabra = ""
		self.indice = 0
		self.siguiente = None
		self.anterior = None
	def setPalabra(self, palabra):
		self.palabra = palabra
	def setIndice(self, ind):
		self.indice = ind
	def setSiguiente(self, sig):
		self.siguiente = sig
	def setAnterior(self, ant):
		self.anterior = ant
	def getPalabra(self):
		return str(self.palabra)
	def getIndice(self):
		return str(self.indice)
	def getSiguiente(self):
		return self.siguiente
	def getAnterior(self):
		return self.anterior
	def __str__(self):
		return "%s %s" %(self.palabra, self.indice)

class ListaS:	
	def __init__(self):
		self.inicio = None
		self.fin = None
		self.cont = 0
	def agregar(self, palabra):
		
		nuevo = NodoL()
		nuevo.setPalabra(palabra) 
		nuevo.setIndice(self.cont)
		if self.inicio == None:
			self.inicio = nuevo
			self.fin = nuevo
		if self.inicio != None:
			
			self.fin.setSiguiente(nuevo)
			nuevo.setAnterior(self.fin)
			self.fin = nuevo
			self.cont = self.cont + 1
	def mostrar(self): 
		outfile= open('ListaSimple.txt', 'w')
		if self.inicio == None :
			outfile.write("La lista esta vacia...!!!")
		else:
			validar = True
			temp = NodoL()
			temp = self.inicio
			outfile.write("digraph G { \n")
			outfile.write("node [shape=circle]; \n")
			outfile.write("node [style=filled]; \n")
			outfile.write("node [fillcolor=\"#EEEEEE\"]; \n")
			outfile.write("node [color=\"#EEEEEE\"]; \n")
			outfile.write("edge [color=\"#31CEF0\"]; \n")		
			while (validar):
				#escribir = str (temp.indice)+ str(temp.palabra)
				escribir =str(temp.palabra)
				if(temp == self.fin):
					validar = False
				temp = temp.getSiguiente()
				if (validar == True):
					escribir2 = escribir + "->"+ str(temp.palabra) +" \n"
					outfile.write(escribir2)
			outfile.write("rankdir=LR; \n }")
		outfile.close()				
	def buscar(self, palabra):
		validar = True
		respuesta = "-1"
		temp = NodoL()
		temp = self.inicio
		while (validar):
			if(temp == self.fin):
				validar = False

			if(palabra == temp.palabra):
				validar = False
				respuesta= str(temp.indice)
			temp = temp.getSiguiente()		
		return respuesta	
	def eliminar(self, indi):		
		if (self.inicio.indice == indi):
			self.inicio = self.inicio.getSiguiente() 
		if (self.fin == indi):
			self.fin = self.fin.getanterior()
		else:
			temp = self.inicio
			while (temp.siguiente.indice != indi):
				temp = temp.getSiguiente()
			siguiente = NodoL()
			siguiente = temp.getSiguiente().getSiguiente()
			temp.setSiguiente(siguiente)
	def restaurarContador(self):
		self.cont = 0
		validar = True
		temp = self.inicio
		while (validar):
			if(temp == self.fin):
				validar = False
			temp.setIndice(self.cont)
			self.cont = self.cont + 1
			temp = temp.getSiguiente()		

"""---------------Cola-----------------"""
class NodoC: 
	def __init__(self):
		self.valor = 0
		self.siguiente = None
	def setValor(self, valor):
		self.valor = valor
	def setSiguiente(self, sig):
		self.siguiente = sig
	def getValor(self):
		return str(self.valor)
	def getSiguiente(self):
		return self.siguiente
	def __str__(self):
		return "%s" %(self.valor)
class Cola:
	def __init__(self):
		self.inicioCola = None
		self.finCola = None
		self.valor = 0
	def queue(self, val):
		nuevo = NodoC()
		nuevo.setValor(val)
		if self.inicioCola == None:
			self.inicioCola = nuevo
			self.finCola = nuevo
		if self.inicioCola != None:
			self.finCola.setSiguiente(nuevo)
			self.finCola = nuevo
	def mostrar(self): 
		outfile= open('Cola.txt', 'w')
		if self.inicioCola == None :
			outfile.write("La Cola esta vacia...!!!")
		else:
			validar = True
			temp = NodoC()
			temp = self.inicioCola
			outfile.write("digraph G { \n")
			outfile.write("node [shape=circle]; \n")
			outfile.write("node [style=filled]; \n")
			outfile.write("node [fillcolor=\"#EEEEEE\"]; \n")
			outfile.write("node [color=\"#EEEEEE\"]; \n")
			outfile.write("edge [color=\"#31CEF0\"]; \n")
			while (validar):
				escribir =str (temp.valor)
				if(temp == self.finCola):
					validar = False
				temp = temp.getSiguiente()
				if (validar == True):
					escribir2 = escribir + "->"+ str (temp.valor) + "\n"
					outfile.write(escribir2)	
		outfile.write("rankdir=LR; \n }")
		outfile.close()
	def dequeue(self):
		sacar = self.inicioCola.valor
		self.inicioCola = self.inicioCola.getSiguiente() 
		return str(sacar)

"""---------------Pila-----------------"""
class NodoP: 
	def __init__(self):
		self.valor = 0
		self.siguiente = None
		self.anterior = None
	def setValor(self, valor):
		self.valor = valor
	def setSiguiente(self, sig):
		self.siguiente = sig
	def getValor(self):
		return str(self.valor)
	def getSiguiente(self):
		return self.siguiente
	def setAnterior(self, ant):
		self.anterior = ant
	def getAnterior(self):
		return self.anterior
	def __str__(self):
		return "%s" %(self.valor)
class Pila:
	def __init__(self):
		self.Fondo = None
		self.Top = None
		self.valor = 0
	def push(self, val):
		nuevo = NodoP()
		nuevo.setValor(val)
		if self.Fondo == None:
			self.Fondo = nuevo
			self.Top = nuevo
		if self.Fondo != None:
			self.Top.setSiguiente(nuevo)
			nuevo.setAnterior(self.Top)
			self.Top = nuevo
	def mostrar(self): 
		outfile= open('Pila.txt', 'w')
		if self.Fondo == None :
			outfile.write("La Pila esta vacia...!!!")
		else:
			validar = True
			temp = NodoP()
			temp = self.Fondo
			outfile.write("digraph G { \n")
			outfile.write("node [shape=circle]; \n")
			outfile.write("node [style=filled]; \n")
			outfile.write("node [fillcolor=\"#EEEEEE\"]; \n")
			outfile.write("node [color=\"#EEEEEE\"]; \n")
			outfile.write("edge [color=\"#31CEF0\"]; \n")
			while (validar):
				escribir =str (temp.valor)
				if(temp == self.Top):
					validar = False
				temp = temp.getSiguiente()
				if (validar == True):
					escribir2 = escribir + "->"+ str (temp.valor) + "\n"
					outfile.write(escribir2)		
		outfile.write("rankdir=LR; \n }")
		outfile.close()
	def pop(self):
		sacar = self.Top.valor
		self.Top = self.Top.getAnterior() 
		return str(sacar)

"""----------------Matriz Dispersa-------------------"""
class NodoLetra: 
	def __init__(self):
		self.Letra = ""
		self.Arriba = None
		self.Abajo = None
		self.Siguiente = None
	def setLetra(self, letra):
		self.Letra = letra
	def setArriba(self, arriba):
		self.Arriba = arriba
	def setAbajo(self, abajo):
		self.Abajo = abajo
	def setSiguiente(self, siguiente):
		self.Siguiente = siguiente 
	def getArriba(self):
		return self.Arriba
	def getAbajo(self):
		return self.Abajo
	def getSiguiente(self):
		return self.Siguiente
	def __str__(self):
		return "%s" %(self.Letra)

class NodoDominio: 
	def __init__(self):
		self.Dominio = ""
		self.Siguiente = None
		self.Anterior = None
		self.Abajo = None
	def setDominio(self, dominio):
		self.Dominio = dominio
	def setSiguiente(self, siguiente):
		self.Siguiente = siguiente
	def setAnterior(self, anterior):
		self.Anterior = anterior
	def setAbajo(self, abajo):
		self.Abajo = abajo
	def getAnterior(self):
		return self.Anterior 
	def getSiguiente(self):
		return self.Siguiente
	def getAbajo(self):
		return self.Abajo
	def __str__(self):
		return "%s" %(self.Dominio)

class NodoNombre: 
	def __init__(self):
		self.Nombre = ""
		self.Siguiente = None
		self.Anterior = None
		self.Arriba = None
		self.Abajo = None
		self.Top = None
		self.Fondo = None
	def setNombre(self, nombre):
		self.Nombre = nombre
	def setSiguiente(self, siguiente):
		self.Siguiente = siguiente
	def setAnterior(self, anterior):
		self.Anterior = anterior
	def setArriba(self, arriba):
		self.Arriba = arriba
	def setAbajo(self, abajo):
		self.Abajo = abajo	
	def setTop(self, top):
		self.Top = top
	def setFondo(self, fondo):
		self.Fondo = fondo
	def getAnterior(self):
		return self.Anterior 
	def getSiguiente(self):
		return self.Siguiente
	def getArriba(self):
		return self.Arriba
	def getAbajo(self):
		return self.Abajo
	def getTop(self):
		return self.Top
	def getFondo(self):
		return self.Fondo
	def __str__(self):
		return "%s" %(self.Nombre)

class Matriz_Dispersa:	
	def __init__(self):
		self.primerLetra = None
		self.ultimaLetra = None
		#self.inicioDominio = None
		#self.finDominio = None
		



	def agregarLetra(self, letra):
		nuevoL = NodoLetra()
		nuevoL.setLetra(letra)
		if self.primerLetra == None:
			self.primerLetra = nuevoL
			self.ultimaLetra = nuevoL
		else:
			if (self.primerLetra.Letra > letra):
				nuevoL.setAbajo(self.primerLetra)
				self.primerLetra.setArriba(nuevoL)
				self.primerLetra = nuevoL
			else:
				if self.ultimaLetra.Letra < letra :
					self.ultimaLetra.setAbajo(nuevoL)
					nuevoL.setArriba(self.ultimaLetra)
					self.ultimaLetra = nuevoL
				else:
					if self.primerLetra != None:
						temp = self.primerLetra
						while temp.getAbajo.Letra <=letra:
							temp = temp.getAbajo()
						nuevoL.setAbajo(temp.getAbajo())
						nuevoL.setArriba(temp)
						temp.setAbajo(nuevoL)
						nuevoL.getAbajo.setArriba(nuevoL)
					#if(nuevoL.getAbajo == None):
					#	self.ultimaLetra = nuevoL



			#self.ultimaLetra.setAbajo(nuevoL)
			#nuevoL.setArriba(self.ultimaLetra)
			#self.ultimaLetra = nuevoL
			


	def comparar(self, le):
		resp = "no"
		if le > "a":
			resp = "si"
		return resp

	def mostrarMatriz(self): 
		outfile= open('Matriz.txt', 'w')
		if self.primerLetra == None :
			outfile.write("La Matriz esta vacia...!!!")
		else:
			temp = self.primerLetra
			outfile.write("digraph G { \n")
			outfile.write("node [shape=circle]; \n")
			#outfile.write("node [style=filled]; \n")
			#outfile.write("node [fillcolor=\"#EEEEEE\"]; \n")
			outfile.write("node [color=\"#EEEEEE\"]; \n")
			outfile.write("edge [color=\"#31CEF0\"]; \n")		
			while (temp != self.ultimaLetra):
				escribir =str(temp.Letra)
				temp = temp.getAbajo()
				if (temp.getAbajo != None):
					escribir2 = escribir + "->"+ str(temp.Letra) +" \n"
					outfile.write(escribir2)
			outfile.write("rankdir=LR; \n }")
		outfile.close()	


















"""--------------- agregando a las Estructuras-----------------------"""
from flask import Flask, request, Response
app = Flask("EDD_Practica2") 
ls = ListaS()
c = Cola()
p = Pila()
m = Matriz_Dispersa()

@app.route('/agregarLista',methods=['POST'])  
def hello():  
	palabra = str(request.form['palabra'])
	ls.agregar(palabra)
	ls.mostrar()
	return "Se agrego a: " + str(palabra) +"...!!!!"

@app.route('/buscarLista',methods=['POST'])  
def hellolb():  
	palabrab = str(request.form['palabrabuscar'])
	valor = ls.buscar(palabrab)
	return valor

@app.route('/eliminardeLista',methods=['POST'])  
def hellole():  
	palabrae = str(request.form['palabraeliminar'])
	ls.eliminar(int(palabrae))
	ls.restaurarContador()
	ls.mostrar()
	return "Se elimino la palabra"

@app.route('/encolar',methods=['POST'])  
def helloenc():  
	num = str(request.form['valorenc'])
	c.queue(int(num))
	c.mostrar()
	return "Se encolo: " + str(num) 

@app.route('/desencolar',methods=['POST'])  
def hellodesen():  
	numd = str(request.form['valordesenc'])
	r = c.dequeue()
	c.mostrar()
	return "Se desencolo: "+ str(r)

@app.route('/push',methods=['POST'])  
def helloenp():  
	num = str(request.form['valorp'])
	p.push(int(num))
	p.mostrar()
	return "Se agrego a la pila: " + str(num) 

@app.route('/pop',methods=['POST'])  
def hellodesenp():  
	nume = str(request.form['valorep'])
	r = p.pop()
	p.mostrar()
	return "Se saco: "+ str(r)

@app.route('/agregarMatriz',methods=['POST'])  
def agregarAmatriz():  
	l = str(request.form['letra'])
	n = str(request.form['nombre'])
	d = str(request.form['dominio'])
	m.agregarLetra(l)
	m.mostrarMatriz()
	#resp = m.comparar(l)
	return "Se agrego: "+ str(n)+"@"+str(d)

@app.route("/e") 
def hellof():
	return "Hello World2!"
if __name__ == "__main__":
  app.run(debug=True, host='127.0.0.1')


