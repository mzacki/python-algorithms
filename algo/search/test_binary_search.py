from algo.search.binary_search import binary_serch


def test_binary_serch():
    test_list = [1, 3, 5, 7, 9]
    target = 3
    non_existing_target = -1

    assert binary_serch(test_list, target) == 1
    assert binary_serch(test_list, non_existing_target) is None
