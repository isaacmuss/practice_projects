items = [1, 2, 3, 4, 5, 6, 7, 8]

items_dict = dict()

for num, val in enumerate(items):
    items_dict[num] = val

size = int(len(items_dict))

rango_1 = list(range(0,int(size/2)))

rango_2 = list(range(int(size/2),size))

new = []

for i in range(int(size/2)):
    new.append(items_dict[rango_1[i]])    
    new.append(items_dict[rango_2[i]])