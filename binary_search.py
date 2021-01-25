def binary_serch(array, item):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        predict = array[mid]
        if predict == item:
            return mid
        if predict > item:
            high = mid - 1
        else:
            low = mid + 1
    return None
