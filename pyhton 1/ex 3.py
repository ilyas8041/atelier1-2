def somme(n):      # on utilise la recursivite pour calculer le somme
    if n == 0 :
        return 0
    else :
        return n + somme(n - 1)

B = int(input("donnez le nombre :")) # l'utilisateur entre le nombre
print(somme(B))  # on affiche le resultat


