def tri_selection(tab):
    n = len(tab)
    for i in range(n):
        min = i   # on trouve le plus petit element
        for j in range(i + 1, n):
            if tab[min] > tab[j]:  # si la condition est vraie, on echange les positions
                min = j
        tmp = tab[i]
        tab[i] = tab[min]
        tab[min] = tmp
    return tab

tab = [10,2,15,55,23,44,77]    #exemple d'utilisation
tri_selection(tab)
print("Le tableau trié est:")
for i in range(len(tab)):
    print(tab[i])   # on affiche les elements tries du tableau


