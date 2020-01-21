from random import randint
'''
Essa primeira função determina a posição das minas
e tem como parâmetro a altura e largura da matriz
e o total de minas a serem colocadas.
Foi usado conjuntos para não ser necessário criar
rotinas para verificar tuplas duplicadas
'''
def defineminas(h, w, total):
  conjunto=set()
  while len(conjunto)<total:
    conjunto.add((randint(2, h-2), randint(2, w-2)))
  return conjunto


def criamatriz(matriz, conjunto):
  '''
  coração do código. Primeiro ele marca a proximidade
  de todas as lajotas a uma bomba e em seguida
  marca as bombas
  '''
  for i in conjunto:
    x, y = i
    print (x, y)
    for j in range(-1, 2):
      for k in range(-1, 2):
        matriz[x+j][y+k]+=1
  for i in conjunto:
    x, y = i
    matriz[x][y]="x"
  return matriz

def desenhamatriz(matriz):
  for lin in matriz:
    for col in lin:
      print(col, end="  ")
    print("\n")

#Inicialmente implementei algo mais simples "[[0]*h]*w"
#mas infelizmente ele clonava celulas e tava dando
#erro
def GeraMatrizVazia(h, w):
  matriz=[]
  for i in range(0,h):
    linha=[]
    for j in range(0, w):
      linha.append(0)
    matriz.append(linha)
  return matriz

h, w, tot = 10, 10, 20
pos=list(defineminas(h, w, tot))
matrizv=(GeraMatrizVazia(h, w),)
novamatriz=criamatriz(matrizv[0], pos)
desenhamatriz(novamatriz)