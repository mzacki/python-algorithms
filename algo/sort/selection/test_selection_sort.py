from algo.sort.selection.selection_sort import selection_sort


def test_selection_sort():
    unsorted_list = [9, 3, 4, 8, 2, 1]

    assert selection_sort(unsorted_list) == [1, 2, 3, 4, 8, 9]


