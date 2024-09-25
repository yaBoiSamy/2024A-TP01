print('Pays concerné ? ')
pays = input()
print("Chaine représentant les médailles ?", end=" ")
medals = input()
gold, silver, bronze = medals.count("G"), medals.count("S"), medals.count("B")
if len(medals) > gold+silver+bronze:
    print("Veuillez entrer une chaîne valide.")
else:
    print(f"{pays}Médailles:\n- Or: {gold}\n- Argent: {silver}\n- Bronze: {bronze}")
