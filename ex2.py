# TODO: Créer un script pour calculer les ressources nécessaires pour assainir la Seine.
# TODO: Importer les modules nécessaires.

print("Quelle quantité d'eau faut-il assainir ? ", end='')

portionsEau = int(input())/5
print(f'''Voici les éléments requis pour assainir {portionsEau}L d'eau:\n
\t- Filtre(s) : {portionsEau}\n 
\t- Lampe(s) UV : {portionsEau*3}\n
\t- Chlore : {portionsEau/2}kg\n''')

