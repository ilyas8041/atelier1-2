list_one = [47, 64, 69, 37, 76, 83, 95, 97]
dict_one = {'Yassine':47, 'Imane':69, 'Mohammed':76, 'Abir':97}
list_final = []
for element in list_one:
  if element in dict_one.values():
    list_final.append(element)  # on ajoute les elements qui existent dans la liste

print(list_final) # on affiche le resultat
