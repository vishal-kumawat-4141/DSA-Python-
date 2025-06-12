# check the array is sorted or not
l = [1, 2, 3, 4, 5, 6, 7, 8]


def check(l):
    for i in range(1, len(l) - 1):
        if l[i] > l[i + 1]:
            return "False"
    return "True"


print(check(l))


# for false condition:-->
l = [1, 2, 3, 4, 8, 6, 7, 8]


def check(l):
    for i in range(0, len(l) - 1):
        if l[i] > l[i + 1]:
            return False
    return True


print(check(l))
