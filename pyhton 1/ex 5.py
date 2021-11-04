def compteur(n):   # on utilise la recursivite pour compter le nombre de chiffre donné
    if n == 0 :
        return 0
    else :
        return 1+compteur(n // 10)

A = int(input(" donnez le nombre :")) # l'utilisateur entre le nombre
print(compteur(A))   # on affiche le resultat