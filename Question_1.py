"""Entez x pour connaitre f(x)"""
def Polynome (x) : 
  res = x**3-1.5*x**2-6*x+5
  return res

Polynome(5)

"""Entrez la valeur x pour connaitre son factoriel"""

def factoriel (x):
  if (x== 0) :
    return 1
  if (x== 1) : 
    return 1
  else :      
    return x*factoriel(x-1)

factoriel(5)

"""Entrez une valeur n en parametre de la fonction pour contaire le n ème nombre de la suite de fibonnaci """

def fibonnaci(n) : 
    if(n== 0) : 
      return 0
    if (n==1) :
      return 1
    else :
      return fibonnaci(n-1)+fibonnaci(n-2)