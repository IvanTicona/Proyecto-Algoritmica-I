import pymysql
import flet as ft
from collections import deque

mycon = pymysql.connect(

  host='localhost',

  port=3307,

  user='root', 

  password='', 

  database='spotify'
)

ejecutorDeQueries=mycon.cursor()

ejecutorDeQueries.execute("SELECT id_usuario, nombre, apellido, edad, descripcion FROM usuarios")

datos = ejecutorDeQueries.fetchall() #Tupla de usarios

ejecutorDeQueries.execute("SELECT id_genero, nombre FROM genero_musical")

generos = ejecutorDeQueries.fetchall() #Tupla de generos

ejecutorDeQueries.execute("SELECT id_gustos, id_genero, id_usuario FROM gustos")

gustos = ejecutorDeQueries.fetchall() #Tupla de gustos

# ejecutorDeQueries.execute()



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




# mycon.close()

#Agregar aristas
for i in range(len(aristas)):
  grafo[aristas[i][0]+50].append(aristas[i][1])
  grafo[aristas[i][1]].append(aristas[i][0]+50)

#Mostar grafo como lista de adyacencia
# for i in range(len(grafo)):
  # print (i, grafo[i])



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

  return sorted(range(len(count[51:])), key=lambda i: count[51:][i], reverse=True)


# nodoRaiz = getIndex("Fernanda")
# print(nodoRaiz)

# BFS(nodoRaiz)

# print("COUNT ========================")
# print(count[51:])
# print("NIVELES ========================")
# print(niveles[51:])

newArray = count[51:]

# indices_ordenados = sorted(range(len(newArray)), key=lambda i: newArray[i], reverse=True)
# indices_ordenados = 

def colaDeIndices():
  cola=deque()
  for indice in indices_ordenados:
    cola.append(indice)
  return cola

# print("COLA ================")
# print(colaDeIndices())

# git merge algunaRama


#nodoRaiz = getIndex("Ernesto")
#print(nodoRaiz)
#BFS(nodoRaiz)

#print(niveles[51:])
#print(count[51:])

def getGraph():
  return grafo

def getNames():
  sim = []
  for i in range(len(niveles)):
    if (niveles[i] != 0):
      sim.append(grafo[i][0])
  return sim

def getUserName(id):
  return datos[id-1][1]

#print(getUserName(1))


def getUserGenres(id):
  return grafo[id+50][1:]

def getGenreNames(idsGenresArray): #Recibe un array de ids de generos
  names = []
  for id in idsGenresArray:
    names.append(grafo[id][0])
  return names

def getAllGenresNames():
  return generosNames

def getAllUserNames():
  user_names=[]
  for i in range (0, len(datos)):
    user_names.append(datos[i][1])
  return user_names
  
#print(getAllUserNames())

#print(generosNames)
def getUserAge(id):
  return datos[id-1][3]

def getUserDescription(id):
  return datos[id-1][4]
#print(getUserAge(1))


#AsignarImagenesALosGeneros
all_genre_names = getAllGenresNames()
genres_images = {}
for genre_name in range(1,len(all_genre_names)):
      image_genre = f"{all_genre_names[genre_name]}.png"  
      genres_images[all_genre_names[genre_name]] = image_genre


#AsignarImagenesALosUsuarios
all_user_names = getAllUserNames()
user_images = {}
for user_name in range(0,len(all_user_names)):
      image_user = f"{all_user_names[user_name]}.png"  
      user_images[all_user_names[user_name]] = image_user




