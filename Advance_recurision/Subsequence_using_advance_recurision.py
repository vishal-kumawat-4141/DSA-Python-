# find the all subsequences of the list:--->
# T.C = O(2**n) ,S.C = O(n) where n is stack space
def sub(index, subset):
    global result
    global nums
    if index >= len(nums):
        result.append(subset.copy())
        return
    subset.append(nums[index])
    sub(index + 1, subset)
    subset.pop()
    sub(index + 1, subset)


nums = [5, 6, 7]
result = []
subset = []
sub(index=0, subset=[])
print(result)
