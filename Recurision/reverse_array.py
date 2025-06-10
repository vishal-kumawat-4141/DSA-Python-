# reverse an array using recurision
l = [1, 2, 3, 4, 5, 6, 7, 8]


def reverse(left, right):
    global l
    if left >= right:
        return
    l[left], l[right] = l[right], l[left]
    return reverse(left + 1, right - 1)


reverse(2, 7)
print(f"reversed list according to left and right : ", l)
