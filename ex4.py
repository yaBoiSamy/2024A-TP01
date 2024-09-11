# TODO: Écrire un programme qui demande le pourcentage de charge actuel de la batterie du bateau,
#        calcule la distance restante en km en fonction de ce pourcentage,
#        et affiche le résultat au format "XX km".
#        Assurez une gestion du pourcentage valide au cours de votre programme (% toujours dans [0 ; 100]).

print("Pourcentage de batterie:", end=" ")
pourcentage = int(input())
map = { 50:2, 25:0.5, 10:1, 5:2.5, 0:6 }
autonomie = 0

for key in sorted(list(map.keys()))[::-1]:
    if pourcentage > key:
        autonomie += (pourcentage-key)*map[key]
    pourcentage = key

print(f"La distance possible est de {autonomie}km")