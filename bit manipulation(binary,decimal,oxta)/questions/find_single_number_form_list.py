# find the single number from list :--->
# mehtod 1 :--> using dectonary (T.C = O(n) ,T.C = O(n/2+1) ~~O(n))
arr = [5, 1, 3, 3, 7, 1, 7]
hash_map = {}
for i in arr:
    hash_map[i] = hash_map.get(i, 0) + 1

for key in hash_map:
    if hash_map[key] == 1:
        print(key)

# method 2:---> T.C = O(n) ,S.C = 1
arr = [5, 1, 3, 3, 7, 1, 7]
ans = 0
for i in arr:
    ans = ans ^ i
print(ans)
