# find the second largest element from array

# using sorting :----> T.C = O(nlog(n)) , S.C = O(1)
# l = l = [1, 4, 55, 76, 94, 140, 37]
# l.sort()
# print(l[-2])


# using 2 for loops without sorting  :---> T.C = O(n+n) ~~ O(n) , S.C = O(1)
# l = l = [1, 4, 55, 76, 94, 140, 37, 140]
# largest = float("-inf")
# S_largest = float("-inf")
# n = len(l)
# for i in range(0, n):
#     largest = max(largest, l[i])

# for i in range(0, n):
#     if l[i] != largest and l[i] > S_largest:
#         S_largest = l[i]
# print(f"second largest element is : ", S_largest)


# only use one for loop without sorting :---> T.C =  O(n) , S.C = O(1)
l = l = [1, 4, 55, 76, 94, 140, 37, 140]
largest = float("-inf")
S_largest = float("-inf")
n = len(l)
for i in range(0, n):
    if l[i] > largest:
        S_largest = largest
        largest = l[i]
    elif l[i] > S_largest and l[i] != largest:
        S_largest = l[i]
print(f"second largest element is : {S_largest}")
