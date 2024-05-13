import pymysql
from collections import deque

mycon = pymysql.connect(

  host='localhost', 

  port=3307, 

  user='root', 

  password='', 

  database='spotify'
)

ejecutorDeQueries=mycon.cursor()

ejecutorDeQueries.execute("SELECT id_usuario, nombre, apellido FROM usuarios")

datos = ejecutorDeQueries.fetchall() #Tupla de usarios

ejecutorDeQueries.execute("SELECT id_genero, nombre FROM genero_musical")

generos = ejecutorDeQueries.fetchall() #Tupla de generos

ejecutorDeQueries.execute("SELECT id_gustos, id_genero, id_usuario FROM gustos")

gustos = ejecutorDeQueries.fetchall() #Tupla de gustos



#==================================================================================================


#Creamos los generos con la informacion de generos

generosNames = [0] #Desde 1 para que coincida con los indices de los nodos

for genero in generos:
  generosNames.append(genero[1])


nodos = []

#Creamos los nodos con la informacion de usuarios

for i in range(len(datos)):
  nodos.append([datos[i][1]])


aristas = []


#Creamos las aristas con la informacion de gustos
for i in range(len(gustos)):
  aristas.append([gustos[i][2], gustos[i][1]])


#Creamos el grafo
grafo = [[] for _ in range(len(nodos)+len(generos)+1)]

#Agregamos los nodos al grafo
grafo[0].append(0)
for i in range(1,len(generos)+1):
  grafo[i].append(generos[i-1][1])
for i in range(0,len(nodos)):
  grafo[51+i].append(nodos[i][0])




mycon.close()

#Agregar aristas
for i in range(len(aristas)):
  grafo[aristas[i][0]+50].append(aristas[i][1])
  grafo[aristas[i][1]].append(aristas[i][0]+50)

#Mostar grafo como lista de adyacencia
for i in range(len(grafo)):
  print (i, grafo[i])



#Encontrar el indice de un nodo (Usuario) en el grafo
def getIndex(nodo):
    for i in range(len(grafo)):
        if grafo[i][0] == nodo:
          return i
    return -1


#==================================================================================================



vis = [False] * (len(nodos)+len(generos)+1)
# Niveles de los nodos
niveles = [0] * (len(nodos)+len(generos)+1)

count = [0] * (len(nodos)+len(generos)+1)

# BFS
def BFS(nodoInicial):
  cola = deque()
  cola.append(nodoInicial)
  niveles[nodoInicial] = 0

  while cola:
    nodoActual = cola.popleft()
    if vis[nodoActual]:
      continue 
    vis[nodoActual] = True

    for i in range(1,len(grafo[nodoActual])):
      amigo = grafo[nodoActual][i]

      if not vis[amigo]:
        niveles[amigo] = niveles[nodoActual] + 1
        cola.append(amigo)
      if niveles[amigo] == 2:
        if niveles[nodoActual] == 1:
          count[amigo] += 8
        else:
          count[amigo] += 2
      if niveles[amigo] == 4:
        count[amigo] += 1

nodoRaiz = getIndex("Daniel")
# print(nodoRaiz)

BFS(nodoRaiz)

print("COUNT ========================")
print(count[51:])
print("NIVELES ========================")
print(niveles[51:])

newArray = count[51:]

indices_ordenados = sorted(range(len(newArray)), key=lambda i: newArray[i], reverse=True)

def colaDeIndices():
  cola=deque()
  for indice in indices_ordenados:
    cola.append(indice)
  return cola

colita = colaDeIndices()

print(colita.popleft())

print("COLA ================")
print(colaDeIndices())

def getGraph():
  return grafo

def getNames():
  sim = []
  for i in range(len(niveles)):
    if (niveles[i] != 0):
      sim.append(grafo[i][0])
  return sim

def getUserGenres(id):
  return grafo[id+50][1:]

def getGenreNames(idsGenresArray): #Recibe un array de ids de generos
  names = []
  for id in idsGenresArray:
    names.append(grafo[id][0])
  return names
