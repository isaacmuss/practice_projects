# Problem 2
# Ascending list function

def is_ascending(items):

    check_list = []
    
    lowest_val = min(items) - 1
            
    for i in items:
        if i > lowest_val:
            check_list.append(True)
        else:
            check_list.append(False)
        lowest_val = i

    final_determination = all(check_list)

    return final_determination