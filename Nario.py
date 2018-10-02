class Arbnario:
	def __init__(self,valor,hijos = []):
		self.valor = valor
		self.hijos = hijos
def buscar(arbol,valor):
	if arbol.valor==valor: return True
	return buscarHijos(arbol.hijos,valor)	

def buscarHijos(lista,valor):
	if lista ==[]:
		return False
	return buscar(lista[0],valor) or buscarHijos(lista[1:],valor)




arbol = Arbnario(2, [Arbnario (4, [Arbnario(12), Arbnario(24), Arbnario(40)]),
                   Arbnario(8, [Arbnario(16), Arbnario(32)]),
                   Arbnario(5, [Arbnario(25), Arbnario(50), Arbnario(100)])])

print(buscar(arbol,int(input())))
