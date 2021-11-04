def tri_bulle(tab):
    n = len(tab)
    for i in range(n):
        for j in range(0, n - i - 1):
            if tab[j] > tab[j + 1]:
                tab[j], tab[j + 1] = tab[j + 1], tab[j] # on échange les elements si l'element trouvé est plus grand que le suivant

tab = [10,2,15,55,23,44,77]      #exemple d'utilisation du fonction
tri_bulle(tab)
print("Le tableau trié est:")
for i in range(len(tab)):
    print(tab[i])   # on affiche les elements tries du tableau