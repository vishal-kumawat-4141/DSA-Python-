# T.C = O(2**n) ,S.C = O(n) where n is stack space
def backtrack_sub(index, subset):
    global result
    global nums
    global target
    if index >= len(nums):
        if sum(subset) == target:
            result.append(subset.copy())
            return
        else:
            return
    subset.append(nums[index])
    backtrack_sub(index + 1, subset)
    subset.pop()
    backtrack_sub(index + 1, subset)


nums = [5, 9, 4, 0]
result = []
target = 9
backtrack_sub(index=0, subset=[])
print(result)


# method 2:---->
def backtrack(index, total, subset):
    global target
    global nums
    global result
    if total == target:
        result.append(subset.copy())
        return

    elif total > target:
        return

    if index >= len(nums):
        return
    subset.append(nums[index])
    sum = total + nums[index]
    backtrack(index + 1, sum, subset)
    e = subset.pop()
    sum = sum - e
    backtrack(index + 1, sum, subset)


target = 9
result = []
nums = [5, 9, 4]
backtrack(index=0, total=0, subset=[])
print(result)
