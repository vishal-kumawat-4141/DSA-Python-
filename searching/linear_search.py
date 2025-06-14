# linear search :----> target value index find out and if not exist so return -1 ...
l = [1, 2, 10, 30, 50, 3, 100, 100, 1000]


def linear_search(l, target: int):
    for i in range(0, len(l)):
        if l[i] == target:
            return i
    return -1


# e = linear_search(l,-100)
# print(type(e))
print(linear_search(l, -100))
print(linear_search(l, 100))
