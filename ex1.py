# TODO: Créer un script permettant le formattage du livre des records des JO.

country = input("De quelle nationalité est l'athlète ? ")
athlete = input('Quel est son nom? ')
date = input('Quelle est la date du record? ')
discipline = input('Dans quelle discipline? ')
categorie = input('Dans quelle catégorie spécifique? ')
record = input('Quel est le record? ')

print(f'Nouveau record: \n -------- \n {date} \n {discipline} - {categorie} \n {athlete} {country} - {record}')