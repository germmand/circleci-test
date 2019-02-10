def bubble_sort(data):
    length = len(data)
    for i in range(length - 1):
        swapped = False
        for j in range(length - 1 - i):
            if data[j] > data[j + 1]:
                swapped = True
                data[j], data[j + 1] = data [j + 1], data[j]
        if not swapped:
            break
    return data
