def conversion(n):
    S = 0
    F = 1
    while n > 0 :
        R = n % 2  # R va contenir le reste de la division
        S += R * F
        F *= 10    # multiplication par 10 pour monter vers les douzaines.... etc
        n = n // 2
    return S

nombre = int(input("Entrez un nombre decimal: "))  # l'utilisateur entre le nombre
print(conversion(nombre))   # on affiche le resultat










