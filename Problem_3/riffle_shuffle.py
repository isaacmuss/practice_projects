def riffle(items, out=True):
    ''' Function to perform perfect riffle '''

    # Get size of items list
    size_items = int(len(items))

    # Check if list has even number of elements
    if size_items % 2 != 0:
        raise ValueError(
            'The number of items in the list is not even, try again')

    # Determine out-shuffle or in-shuffle
    if out == True:
        items_0 = items[:int(size_items/2)]
        items_1 = items[int(size_items/2):]
    elif out == False:
        items_1 = items[:int(size_items/2)]
        items_0 = items[int(size_items/2):]

    # Construct list of lists with two halves of the original list
    items_comp = [items_0, items_1]

    # Perform the shuffle with list comprehension
    new = [[row[i] for row in items_comp] for i in range(int(len(items_0)))]

    # Flatten list with final result
    new_final = [num for elem in new for num in elem]

    return new_final