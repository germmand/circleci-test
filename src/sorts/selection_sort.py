def selection_sort(data):
    length = len(data)
    for i in range(length - 1):
        least = i
        for k in range(i + 1, length):
            if data[k] < data[least]:
                least = k
                data[least], data[i] = data[i], data[least]
    return data
