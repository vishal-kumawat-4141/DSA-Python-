# check subsequence is exist then return True else retrun false
# T.C = O(2**n) ,S.C = O(n) where n is stack space
def backtrack_sub(index, subset):
    global result
    global nums
    global target
    if index >= len(nums):
        if sum(subset) == target:
            result.append(subset.copy())
            return True
        else:
            return False
    subset.append(nums[index])
    pick = backtrack_sub(index + 1, subset)
    if pick == True:
        return True
    subset.pop()
    not_pick = backtrack_sub(index + 1, subset)
    return not_pick


nums = [5, 9, 4, 0]
result = []
target = 9
print(backtrack_sub(index=0, subset=[]))


# method 2:----># T.C = O(2**n) ,S.C = O(n) where n is stack space
def backtrack(index, total):
    global target
    global nums
    global result
    if total == target:
        return True

    elif total > target:
        return False

    if index >= len(nums):
        return False
    sum = total + nums[index]
    pick = backtrack(index + 1, sum)
    if pick == True:
        return True
    sum = total
    not_pick = backtrack(index + 1, sum)
    return not_pick


target = 9
result = []
nums = [5, 9, 4]
print(backtrack(index=0, total=0))
