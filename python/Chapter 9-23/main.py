def reverse_array(items):
    new_list = []
    for item in range(len(items)-1, -1):
        new_list.append(items[item])
    return new_list