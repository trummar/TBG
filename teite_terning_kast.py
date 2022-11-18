
import random

#number = random.randint(1,6)
kast_liste = []
enere = 0
toere = 0
trere = 0 
firere = 0
femmere = 0
seksere = 0

#print(number)

antall_kast = int(input("Hvor mange terningkast vil du gjøre? "))

for i in range(1,antall_kast+1):
    kast = random.randint(1,6)
    kast_liste.append(kast)
    #print(kast) 

print("*************")    
print(len(kast_liste))   

for i in kast_liste:
    if i == 1:
        enere += 1
    elif i == 2:
        toere += 1
    elif i == 3:
        trere += 1
    elif i == 4:
        firere += 1
    elif i == 5:
        femmere += 1
    elif i == 6:
        seksere += 1
    else:
        pass
print("*************")
print(enere)
print(toere)
print(trere)
print(firere)
print(femmere)
print(seksere)

sannsyn_enere = enere/antall_kast
sannsyn_toere = toere/antall_kast
sannsyn_trere = trere/antall_kast
sannsyn_firere = firere/antall_kast
sannsyn_femmere = femmere/antall_kast
sannsyn_seksere = seksere/antall_kast

print("*************")
print(sannsyn_enere)
print(sannsyn_toere)
print(sannsyn_trere)
print(sannsyn_firere)
print(sannsyn_femmere)
print(sannsyn_seksere)
