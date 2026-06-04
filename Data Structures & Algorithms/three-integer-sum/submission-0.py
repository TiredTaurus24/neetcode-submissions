class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, num in enumerate(nums):
            if num > 0:
                break
            if i > 0 and num == nums[i-1]:
                continue
            l = i+1
            r = len(nums) - 1
            while l < r:
                cursum = num + nums[l] + nums[r]
                if cursum < 0:
                    l = l+1
                elif cursum > 0:
                    r = r-1
                else:
                    res.append([num,nums[l],nums[r]])
                    l = l+1
                    r = r-1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res 
        