# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 08:45:24 2022

@author: vande

*******
Visulelt sett etter å ha kjørt programmet så er 3-sek regelen
unøyaktig fra ca 103km/t.  Skal også vise dette under her. 

"""

import numpy as np
import matplotlib.pyplot as plt

a  = 0.7
b = 0.08

x_ms = np.linspace(0,1000,1001)    # for nøyaktighet
x_kmh = x_ms * 3.6                  # meter pr sekund * 3.6 = km/t 

stort_array = np.array([])  # for å samle opp verdier der f1(v) 
                            # er større enn f2(v)

# print(x_kmh)

# to formler for stopplengde:
# Stopplengde = reaksjonslengde + bremselengde
# Må lage to funksjoner: f1 og f2
# Kurvene S1 og S2 skal vise hhv f1 og f2

def f1(v): #plottes rød
    # stopplengde totalt
    lengde_totalt = (a*v) + b*(v**2)
    return lengde_totalt

def f2(v):  #plottes grønn
    # s = v*t   
    lengde_totalt = v * 3  # multiplisere fart med sekunder gir meter
    return lengde_totalt

"""

Når verdiene fra f1(v) overstiger f2(), så vil ikke 3-sekundersregelen
ikke lenger fungere. Jeg velger en for løkke fordi jeg kan ikke vite 
om verdiene er direkte like for hver indeks. Jeg ser derfor for når verdiene 
for stopplengde i funksjonen f1() overstiger verdien i f2(). Da har jeg 
verdier for hvilken km/t som stopplengden for f1() er større enn f2()

Jeg populerer da alle verdiene til et nytt array og tar derfor og 
sjekker første verdien i dette arrayet. Det vil da være aktuell verdi 
for når f1() er større enn f2(). 

Ved å sette f1 lik f2, dvs: 3v = av +bv^2, så får man:
v(0,08v - 2,3) = 0   ; Denne løses ved enkel regning uten konstantledd.

v = 0 eller 0.08v = 2.3
0.08v = 2.3 gir v = 28.75

variabelen krysning gir svar 28.8 nå f1>f2. 

"""

for i in x_kmh:
    if f1(i+1) > f2(i+1):
        stort_array = np.append(stort_array, i)
        
    else:
        pass
        
krysning = stort_array[0]
print(krysning)

print("Verdien for når 3-sekunder-regelen")
print("ikke fungerer er", round(krysning,2)*3.6, "km/t")
print("Se også plott for når grønn og rød kurve har krysning.")
            

    
# Følgende kodesnutt er basert på eksempel fra temp.py av faglærer
# og er modifisert slik at den viser plottet riktig. 

plt.close('all')
plt.figure(1)
plt.plot(x_kmh*3.6, f1(x_kmh), 'r', label='S1: stopplengde formel')
plt.plot(x_kmh*3.6, f2(x_kmh), 'g', label='S2: stopplengde 3-sekundersregel') 
plt.axvline(x = (krysning*3.6), color = "b", label = "Krysning S1 og S2")
plt.legend()
plt.title('Stopplengde reelt og 3-sekunders regelen')
plt.xlabel('Fart m/s')
plt.ylabel('Stopplengde m')
# plt.xlim(0, 150)
# plt.ylim(0, 150)
plt.xlim(0, 150)
plt.ylim(0, 200)
plt.grid()
plt.show()




