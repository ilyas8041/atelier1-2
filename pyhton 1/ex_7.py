def inverse(str1):
    str1 = str(input("donnez la chaine : "))
    str2 = ""
    i = len(str1) - 1  # index du dernier caractere de ch1
    while i >= 0:
        str2 += str1[i]  # on concatene un caractere de ch1  a ch2
        i -= 1
    return(str2)

print(inverse(str)) # on affiche le resultat


