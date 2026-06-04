import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        final_rate = r

        while l <= r:
            rate = (l+r)//2
            time = sum(math.ceil(a/rate) for a in piles)
            if time <= h:
                final_rate = rate
                r = rate - 1
            else:
                l = rate + 1
        return final_rate




        
        