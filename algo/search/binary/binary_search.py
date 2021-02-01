def binary_search(array, item):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        index = array[mid]
        if index == item:
            return mid
        if index > item:
            high = mid - 1
        else:
            low = mid + 1
    return None
