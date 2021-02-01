from algo.search.binary.binary_search_step import binary_search_step


def test_binary_serch_step():
    test_list = [1, 3, 5, 7, 8, 9, 10, 11, 12]
    target = 3

    assert binary_search_step(test_list, target) == 2
