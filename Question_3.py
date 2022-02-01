import numpy as np
from scipy.stats import norm
def bonus() :
  s = float(input(" prix actuel : "))
  x = float(input(" Prix d'exercice de l'option "))
  T = int(input(" Temps restant avant l'expiration de l'option en j :"))
  r = float(input(" Taux d'interet sans risque :"))
  sig = float(input (" Volatilite implicite du prix de l'action "))
  
  T= (T/365) *100

  d1 = (np.log(s/x)+(r+(sig**2)/2)*T) /sig * np.sqrt(T)
  d2 = d1-sig * np.sqrt(T)

  c= s*norm.cdf(d1)-x*np.exp(-r*T)*norm.cdf(d2)
  p= x*np.exp(-r*T)*norm.cdf(-d2)-s*norm.cdf(-d1)

  print("")
  print ("call option : %f" % c)
  print ("put option : %d"% p)

bonus()