class Solution:
    def threeSum(nums): 
        nums.sort()
        result = []
        if not nums or len(nums) < 3:
            return result
        for i in range(len(nums) - 2):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
        return result


# test1 = [-1,0,1,2,-1,-4]
# result = Solution.threeSum(test1)
# print(result)

test1 = [0, 0, 0, 0]
result = Solution.threeSum(test1)
print(result)
            
        