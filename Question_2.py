"""Entrez une valeur n en parametre de la fonction pour contaire le n ème nombre de la suite de fibonnaci """

def fibonnaci(n) : 
    if(n== 0) : 
      return 0
    if (n==1) :
      return 1
    else :
      return fibonnaci(n-1)+fibonnaci(n-2)

"""Appelez la fonction fibo pour appeler les n premiers élements de la suite de fibonacci.
puisque la complexité de la fibonnaci est expenentielle elle a était limité à 15
J'ai volentairement choisi d'utiliser un print au lieu de l'éxception pour que si le nombre et trop grand ou inferieur à 0 on aurait pas besoin de relancer la fonction.
J'ai aussi fait une version fibo2() avec des raise Exception pour ne pas etre hors sujet.
En ce qui concerne les string les complexe et les trop petits nombre le fait d'appeler le input en tant que int permet de ne pas accepter d'ofice les autres types.
"""

def fibo():
  n= int(input("Entrez un nombre :"))
  while(n < 0 ) : 
    print("Le nombre est négatif, entrez un nombre positif")
    n= int(input("Entrez un nombre :"))
  while(n >15) :
    print(" Le nombre entré est trop grand, Entrez un nombre plus petit") 
    n= int(input("Entrez un nombre :"))  
  print("La suite de fibonnaci est :")
  for i in range(0,n):
    print(fibonnaci(i),end ="," )

def fibo2 :
  n= int(input("Entrez un nombre :"))  
  if(n < 0 ) : 
    raise Exception("Le nombre est négatif, entrez un nombre positif")
  if(n >100) :
    raise Exception(" Le nombre entré est trop grand, Entrez un nombre plus petit") 
  print("La suite de fibonnaci est :")
  for i in range(0,n):
    print(fibonnaci(i),end ="," )

