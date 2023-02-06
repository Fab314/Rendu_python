import random

def devinette():

 nombre_mystere = random.randint(0, 123)
 devine = True


 while devine:
        nombre = int(input("Entrer un nombre au hasard: "))
        if nombre == nombre_mystere:
           print("bravo c'est good")
           devine = False
        elif nombre < nombre_mystere:
           print("trop petit")
      
        else:
           print("trop grand")

devinette()
