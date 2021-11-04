list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
dict = {}
for element in list:
  dict[element] = dict.get(element, 0) + 1 # on ajoute 1 chaque fois o trouve l'element

print(dict) # on affiche le resultat

