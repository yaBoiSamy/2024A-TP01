from math import ceil
eau = float(input("Quelle quantité d'eau faut-il assainir ? "))
print(f'''Voici les éléments requis pour assainir {eau}L d'eau:
\t- Filtre(s) : {ceil(eau*0.2)}
\t- Lampe(s) UV : {ceil(eau*0.6)}
\t- Chlore : {eau*0.1}kg''')

