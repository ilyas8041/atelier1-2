def fibonacci(n):   # on utilise la recursivite pour determiner les termes de fibonacci
    if(n <= 1):
        return n
    else:
        return (fibonacci(n - 1) + fibonacci(n - 2))

n = int(input("Entrez le nombre de termes:")) # l'utilisateur entre le nombre de termes souhaitées
print("Suite de Fibonacci :")
for i in range(n):
    print(fibonacci(i)) # on affiche les resultat