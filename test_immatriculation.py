
entree = input("enttrer les premières lettres de l'immatriculation")


if type(entree) == int:
    print("Mauvais numero")
elif type(entree) == str:
    print("Entrer la deuxieme partie de l'immatriculation")

entree_2 = input("")

if type(entree_2) == int:
    print("bon vol")
elif type(entree_2) == str:
    print("Mauvais numero")

