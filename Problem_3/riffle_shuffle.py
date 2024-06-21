items = [1, 2, 3, 4, 5, 6, 7, 8]

items = ['bob', 'jack']

size_items = int(len(items))

indic = False

if indic == True:
    items_0 = items[:int(size_items/2)]
    items_1 = items[int(size_items/2):]
elif indic == False:
    items_1 = items[:int(size_items/2)]
    items_0 = items[int(size_items/2):]

items_comp = [items_0, items_1]

new = [[row[i] for row in items_comp] for i in range(int(len(items_0)))]

new_final = [num for elem in new for num in elem]