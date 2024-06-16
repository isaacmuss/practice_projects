
items = [1, 2, 3, 4, 5, 6, 7, 8]

items_0 = items[:int((len(items))/2)]

items_1 = items[int((len(items)/2)):]

indic = True 

new = []

for num, val in enumerate(items):
    print(num + 1, val)
    new.append(val)
    if num in range(int(len(items)/2),int(len(items))):
        new.append(val)



# for num in items_0:
#     for num_2 in items_1:
#         new.append(num)
#         new.append(num_2)
#         continue
#     continue

print(new)
# shuffle = [(i) for i in range(items)]