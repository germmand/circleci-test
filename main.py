from src.sorts import bubble_sort

def main():
    data = [87, 14, 65, 23, 98]
    print("Unsorted data: ")
    print(data)
    data = bubble_sort(data)
    print("Sorted data: ")
    print(data)

if __name__ == '__main__':
    main()
