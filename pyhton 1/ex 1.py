def factorielle(n):  # la fonction factorielle calcul le factoriel d'un element en utlisant la recursivite
    if n == 0:
        return 1
    else:
        return n * factorielle(n - 1)


S = 0  # S  va contenir le factoriel du nombre divise par lui meme
D = 0  # D va contenir la somme de S
a = int(input("donnez le nombre de termes :")) # l'utilisateur entre le nombre de termes
for i in range(1, a):
    S = factorielle(a) / a
    D = D + S
print(S) # on affiche le resultat