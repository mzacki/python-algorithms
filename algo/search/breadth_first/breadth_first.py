from collections import deque


def search(graph):
    queue = deque()
    queue += graph
    checked = []
    while queue:
        place = queue.popleft()
        if is_target(place):
            print(place + " is the target.")
            return True
        else:
            queue += graph[place]
            checked.append(place)
    return False


def is_target(place):
    return place[-1] == "d"

