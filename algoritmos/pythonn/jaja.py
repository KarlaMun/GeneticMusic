import copy
import random

tabler=[]
tablero=[] #tablero inicial aleatorio
for i in range(5):
    lista=[]
    for j in range(5):
        kk=random.randrange(2)
        lista.append(kk)
    tablero.append(lista)
    print(lista)

def imprime(mat):
    print("IMPRIMIR SIGUIENTE TURNO")
    for i in mat:
        print(i)
  
    
def turno(tablero):
    mat2=copy.deepcopy(tablero)
    for renglon in range(len(tablero)):
        for columna in range(len(tablero[renglon])):
            futuro=0
            for indice1 in range(renglon-1,renglon+2):
                for indice2 in range(columna-1,columna+2):
                    if indice2<len(tablero[renglon]) and indice1<len(tablero):
                       if (indice2+1)>0 and (indice1+1)>0:
                           futuro+=tablero[indice1][indice2]
            if tablero[renglon][columna]==0:
                if futuro==3:
                    mat2[renglon][columna]=1
            elif tablero[renglon][columna]==1:
                if futuro!=4 and futuro!=3:
                    mat2[renglon][columna]=0
    imprime(mat2)
    return mat2

while not tabler==tablero: 
    tabler=copy.deepcopy(tablero)
    tablero=turno(tablero)