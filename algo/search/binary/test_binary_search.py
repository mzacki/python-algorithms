from algo.search.binary.binary_search import binary_search


def test_binary_serch():
    test_list = [1, 3, 5, 7, 9]
    target = 3
    non_existing_target = -1

    assert binary_search(test_list, target) == 1
    assert binary_search(test_list, non_existing_target) is None
