
x = int(input("Entrez le nombre de colonnes (X): "))
y = int(input("Entrez le nombre de lignes (Y): "))

if x > y:
  for i in range(y):
    print("@" * x)
else:
  print("Le nombre de colonnes doit être supérieur au nombre de lignes.")