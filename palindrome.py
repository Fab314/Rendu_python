def palindrome(test):
    return test == test[::-1]

string = str(input("Entrer un mot: "))
if palindrome(string):
    print("C'est un palindrome")
else:
    print("Ce n'est pas un palindrome")
