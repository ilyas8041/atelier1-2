set_one = {23, 42, 65, 57, 78, 83, 29}
set_two = {57, 83, 29, 67, 73, 43, 48}
set_first = []
for element in set_one:
  if element in set_two:
    set_first.append(element)

set_final = set()
for element in set_one:
  if not element in set_first:
    set_final.add(element)

print(set_first)
print(set_final)