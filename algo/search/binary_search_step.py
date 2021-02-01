def binary_serch_step(array, item):
    low = 0
    high = len(array) - 1
    counter = 0

    while low <= high:
        mid = (low + high) // 2
        index = array[mid]
        counter = counter + 1
        if index == item:
            return counter
        if index > item:
            high = mid - 1
        else:
            low = mid + 1
    return None
