#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
### Modules import

### Variables initialization
avengers = ['Black Widow', 'Tony Stark', 'Hulk', 'Captain America', 'Spiderman', 'Dr Strange']

### Code
print(avengers,"\n")

print(avengers[0],"\n")      # 1ère voiture
print(avengers[2],"\n")      # 3e voiture
print(avengers[-1],"\n")     # dernière voiture

avengers[2]='HawkEye'         # Remplace la 3e par HawkEye
print(avengers,"\n")

avengers.append('AntMan')      # ajoute AntMan à la fin
print(avengers,"\n")

avengers.insert(2,'Winter Soldier')        # ajoute Winter Soldier en 3e position
print(avengers,"\n")

del avengers[1]              # supprime la 2e entrée
print(avengers,"\n")

avengers.remove('Winter Soldier')  # supprime l'entrée par sa valeur
print(avengers,"\n")

avengers.reverse()           # tri par ordre inversé
print(avengers,"\n")

avengers.sort()              # tri par ordre alphabétique
print(avengers,"\n")

print(avengers[0:3],"\n")           # découpage d'une liste
print(avengers[4:],"\n")            # découpage d'une liste

for chaque in avengers:            # parcourir une liste
    print('-',chaque)

print("\n")

stock_1={                           # dictionnaire
    'type':'Black Widow',
    'costume':'moulant'
}

print(stock_1,"\n")

print(stock_1['type'],"\n")         # accèder à des valeurs par la clé
print(stock_1['costume'],"\n")

stock_1['annee']=2014               # ajouter d'une nouvelle clé+valeur
print(stock_1,"\n")

stock_1['annee']=2021               # modifier la valeur
print(stock_1,"\n")

del stock_1['costume']              # supprimer un couple clé+valeur
print(stock_1,"\n")

DC_Comics={                          # parcourir un dictionnaire
    'WondeWoman':'incroyable',
    'Superman':'en collant'
}
for nom, descriptif in DC_Comics.items():
    print(nom, descriptif)

print("\n")

### End
