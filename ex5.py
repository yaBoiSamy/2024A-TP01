
#TODO: Analyser la chaîne de caractères saisie et compter le nombre de médailles.
#      Attention si la chaîne est invalide, un message d'erreur est attendu.


pays = input('Pays concerné ? ' )
medals = input("Chaine représentant les médailles ? ")
gold, silver, bronze = medals.count("G"), medals.count("S"), medals.count("B")
if len(medals) > gold+silver+bronze:
    print("Veuillez entrer une chaîne valide.")
else:
    print(f"{pays}Médailles:\n- Or: {gold}\n- Argent: {silver}\n- Bronze: {bronze}")
