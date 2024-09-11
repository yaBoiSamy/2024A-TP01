#TODO: Analyser la chaîne de caractères saisie et compter le nombre de médailles.
#      Attention si la chaîne est invalide, un message d'erreur est attendu.

print("Résultat du pays:", end=" ")
medals = {"G":0, "S":0, "B":0}
for medal in input():
    if medal in medals:
        medals[medal]+=1
    else:
        medals = None
if medals != None:
    print(f"Médailles:\n- Or: {medals['G']}\n- Argent: {medals['S']}\n- Bronze: {medals['B']}")
else:
    print("Veuillez entrer une chaîne valide.")

