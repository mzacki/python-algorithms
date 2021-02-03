from algo.sort.quick.quick_sort import quick_sort


def test_quick_sort():

    unsorted_list = [9, 3, 4, 8, 2, 1]

    assert quick_sort(unsorted_list) == [1, 2, 3, 4, 8, 9]
