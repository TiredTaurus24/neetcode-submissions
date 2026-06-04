class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = nums[0]
        cur_min = nums[0]
        res = nums[0]

        for i in nums[1:]:
            temp_max = max(i, i*cur_max, i*cur_min)
            cur_min = min(i, i*cur_max, i*cur_min)
            cur_max = temp_max

            res = max(res, cur_max)

        return res
        