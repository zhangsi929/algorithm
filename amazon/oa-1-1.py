# 第一题 密码题
def encrypt(nums):
    temp = nums
    while len(temp) != 2:
        ans = []
        for i in range (len(temp) - 1):
            r = (temp[i] + temp[i + 1]) % 10
            ans.append(r)
        temp = ans
    return "".join([str(x) for x in temp])

test1 = [4, 5, 6, 7]


print(encrypt(test1))


# 第二题 电影分组, 最少能分多少组？

def makeGroup(nums, k):
    nums.sort()
    n = len(nums)
    res = []
    temp = []
    start = 0
    for end in range(n):
        if nums[end] - nums[start] <= k:
            temp.append(nums[end])
        else:
            res.append(list(temp))
            temp.clear()
            start = end
            temp.append(nums[end])
    if temp:
        res.append(list(temp))
    return res


test1 = [1, 5, 4, 6, 8, 9, 2]

print(makeGroup(test1, 3))

