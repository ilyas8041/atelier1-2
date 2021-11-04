def tri_insertion(tab):
    n = len(tab)
    for i in range(1,n):
        k = tab[i]
        j = i-1
        while j >= 0 and k < tab[j] :   # tant que la condition est vraie, on echange les deux element
                tab[j + 1] = tab[j]
                j -= 1
        tab[j + 1] = k

tab = [10,2,15,55,23,44,77]  #exemple d'utilisation
tri_insertion(tab)
print ("Le tableau trié est:")
for i in range(len(tab)):
    print(tab[i])   # on affiche les elements tries du tableau