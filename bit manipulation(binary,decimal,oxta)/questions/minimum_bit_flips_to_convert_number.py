# find the minimum bit flips to convert number:-->
# Method 1:--> T.C = O(32) ,S.C = O(1)
start = 10
goal = 7
ans = start ^ goal
count = 0
for i in range(0, 32):
    if ans & (1 << i) != 0:
        count += 1
print(f"The number of bits flips to convert {start} to {goal} is :--> {count}")

# Method 2:--> T.C = O(log2(n)) ,S.C = O(1)
start = 10
goal = 7
ans = start ^ goal
count = 0
while ans > 0:
    if ans % 2 == 1:
        count += 1
    ans = ans // 2
print(count)
