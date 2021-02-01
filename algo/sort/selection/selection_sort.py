def selection_sort(arr):
    new_arr = []
    for _ in range(len(arr)):
        smallest = get_min(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


def get_min(arr):
    min_item = arr[0]
    min_index = 0
    for i in range(1, len(arr)):
        if arr[i] < min_item:
            min_item = arr[i]
            min_index = i
    return min_index

