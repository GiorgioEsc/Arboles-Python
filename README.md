# Universidad Distrital Francisco José de Caldas

## Facultad Ingenieria

### Modelos de programación II

#### Creador:

##### Jorge Antonio Escobar Bohorquez - 20152020120

#### Arboles:

Los árboles se usan en muchas áreas de las ciencias de la computación, incluyendo sistemas operativos, gráficos, sistemas de bases de datos y redes de computadoras. Las estructuras de datos tipo árbol tienen muchas cosas en común con sus primos botánicos. Una estructura de datos tipo árbol tiene una raíz, ramas y hojas. La diferencia entre un árbol de la naturaleza y un árbol de las ciencias de la computación es que una estructura de datos tipo árbol tiene su raíz en la parte superior y sus hojas en la parte inferior.

![Imagen Arbol](http://interactivepython.org/runestone/static/pythoned/_images/biology.png "Arboles")
La primera propiedad que este ejemplo demuestra es que los árboles son jerárquicos. Por jerárquico, queremos decir que los árboles están estructurados en capas con las cosas más generales cerca de la parte superior y las cosas más específicas cerca de la parte inferior. La parte superior de la jerarquía es el Reino, la siguiente capa del árbol (los “hijos” de la capa superior) es el Filo, luego está la Clase, y así sucesivamente. Sin embargo, no importa cuán profundo vayamos en el árbol de clasificación, todos los organismos siguen siendo animales.


##### EJEMPLO EN PYTHON 

Este es un ejemplo de arboles N-arios desarrollado en python.
``` python
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

print (buscar(arbol,int(input())))

```

### Árbol de análisis

Con la implementación de nuestra estructura de datos de árbol completa, miremos ahora un ejemplo de cómo puede usarse un árbol para resolver algunos problemas reales. En esta sección examinaremos los árboles de análisis. Los árboles de análisis se pueden usar para representar construcciones del mundo real como oraciones o expresiones matemáticas.


![Imagen Arbol](http://interactivepython.org/runestone/static/pythoned/_images/nlParse.png
 "Arboles")
 
 Figura 1: Un árbol de análisis para una oración simple

 
 
La Figura 1 muestra la estructura jerárquica de una oración simple. Representar una oración como una estructura de árbol nos permite trabajar con las partes individuales de la oración usando subárboles.
