def frequence(C) :
    str2 = str(input("donnez la lettre :")) # l'utilisateur donne le lettre a chercher
    cmpt = 0
    for i in range (0,len(str1)) : # parcourir toute la chaine
        if str1[i] == str2 :
            cmpt = cmpt + 1
    return (cmpt)

str1 = str(input("donnez la chaine de caractere :"))  # l'utilisateur entre la chaine
print(frequence(str1))    # on affiche le resultat









