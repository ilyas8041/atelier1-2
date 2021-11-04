List1 = [3, 6, 9, 12, 15, 18, 21]
List2 = [4, 8, 12, 16, 20, 24, 28]
List3 =[]
for i in range(len(List1)):  # parcourir toute la liste
    if i % 2 != 0:       # on ajoute les elements d'index impair
        List3.append(List1[i])
for i in range(len(List2)):
    if i % 2 == 0:       # on ajoute les elements d'index pair
        List3.append(List2[i])

print(List3) # on affiche la liste