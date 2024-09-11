# TODO: Créer un script pour calculer les ressources nécessaires pour assainir la Seine.
# TODO: Importer les modules nécessaires.

print("Quantité d'eau à assainir (en L):", end=" ")
portionsEau = int(input())/5
print(f"Voici les matériaux requis pour l'assainissement de 10L d'eau:\n- {portionsEau} filtres\n- {portionsEau*3} lampes UV\n- {portionsEau/2}kg de chlore")

