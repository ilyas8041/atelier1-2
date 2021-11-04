import math    # la bibliothaque math pour utiliser ceil
List1 = [11,45,8,23,14,12,78,45,89]
List=[]            # la fonction ceil retourne  le plus petit entier plus grand ou égal à un nombre
for i in range (0, len(List1)-1, math.ceil(len(List1)/3)):
    p= List1[i: i + math.ceil(len(List1)/3)]
    p.reverse()     # on renverse les listes
    List.append(p)

print(List) # on affiche le resulat



