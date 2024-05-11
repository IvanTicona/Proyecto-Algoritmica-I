import pymysql  
from collections import deque #se importan librerias de mysql y deque



mycon = pymysql.connect( #se realiza la conexion con la base de datos

  host='localhost', #se especifica el servidor

  port=3307, #puerto donde se almacena la base de datos

  user='root', #se define el nombre como root para tener acceso completo a la base de datos

  password='', #se define el password como vacio

  database='spotify' #nombre de la base de datos a utilizar
)

ejecutorDeQueries=mycon.cursor() #objeto que actua como controlador que permite ejecutar consultas SQL y recuperar resultados de la base de datos

ejecutorDeQueries.execute("SELECT id_usuario, nombre, apellido FROM usuarios") #para ejecutar consultas 

datos = ejecutorDeQueries.fetchall() #Tupla de usarios

ejecutorDeQueries.execute("SELECT id_genero, nombre FROM genero_musical") #para ejecutar consultas 

generos = ejecutorDeQueries.fetchall() #Tupla de generos

ejecutorDeQueries.execute("SELECT id_gustos, id_genero, id_usuario FROM gustos") #para ejecutar consultas 

gustos = ejecutorDeQueries.fetchall() #Tupla de gustos



#==================================================================================================


#Creamos los generos con la informacion de generos

generosNames = [0] #Desde 1 para que coincida con los indices de los nodos

for genero in generos: #
  generosNames.append(genero[1])
#[(112, Pop),
#(279,Rock),
#(345, Rap)]
#generosNames = [0,Pop,Rock,Rap]

nodos = [] #declara "nodos"

#Creamos los nodos con la informacion de usuarios

for i in range(len(datos)): #recorre un interador hasta la longitud de la columnda de id's
  nodos.append([datos[i][1]]) #nodos = [nombre,nombre2,nombre3]


aristas = [] # declara "aristas"


#Creamos las aristas con la informacion de gustos
for i in range(len(gustos)): #recorre un iterador hasta la columnda de id's
  aristas.append([gustos[i][2], gustos[i][1]]) #aristas = [(id_usuario1,id_genero1),(id_usuario2,id_genero2)]


#Creamos el grafo
grafo = [[] for _ in range(len(nodos)+len(generos)+1)] 
#vector<int> grafo [] (se aumenta +1 para que exista la posicion n)


#Agregamos los nodos al grafo
grafo[0].append(0) #se agrega un 0 a la posicion 0 porque comenzaremos a utilizar el grafo desde la posicion 1
for i in range(1,len(generos)+1): 
  grafo[i].append(generos[i-1][1]) #se itera desde 1 hasta generos+1 y se agregan al grafo los 50 generos
for i in range(0,len(nodos)):
  grafo[51+i].append(nodos[i][0]) #se itera desde 0 hasta el tamaño de nodos para agregar los usuarios luego de agregar los generos




mycon.close() #cerramos la conexion con la base de datos

#Agregar aristas
for i in range(len(aristas)):
  grafo[aristas[i][0]+50].append(aristas[i][1]) #en la posicion [i][0]+50 agregamos a la lista el id del genero que le gusta para que este relacionado con el usuario anteriormente agregado
  grafo[aristas[i][1]].append(aristas[i][0]+50) #se hace lo mismo pero al reves para que sea un grafo no dirigido

#Mostar grafo como lista de adyacencia
for i in range(len(grafo)):
  print (i, grafo[i])
#imprime todas las listas del grafo


#Encontrar el indice de un nodo (Usuario) en el grafo


def getIndex(nodo):
    for i in range(len(grafo)):
        if grafo[i][0] == nodo:
          return i
    return -1
# metodo para buscar un usuario y que devuelva el indice de la posicion de la lista en la que se encuentra


#==================================================================================================



vis = [False] * len(nodos) #se crea un array de tamaño len(nodos) y se los llena con falso

niveles = [0] * (len(nodos)+len(generos)+1)



def BFS(nodoInicial):
  cola=deque()
  cola.append(nodoInicial)
  niveles[nodoInicial]=0
  while cola:
    nodoActual = cola.popleft()
    if(niveles[nodoActual]>=2):
      continue
    for i in range(1,len(grafo[nodoActual])):
      amigo = grafo[nodoActual][i]
      if(niveles[amigo]<2):
        niveles[amigo]=niveles[nodoActual]+1
        cola.append(amigo)


nodoRaiz = getIndex("Ernesto")
# print(nodoRaiz)
BFS(nodoRaiz)

print(niveles[50:])