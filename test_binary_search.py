from binary_search import binary_serch


def test_binary_serch():
    test_list = [1, 3, 5, 7, 9]
    goal = 3
    non_existing_goal = -1

    assert binary_serch(test_list, goal) == 1
    assert binary_serch(test_list, non_existing_goal) is None
