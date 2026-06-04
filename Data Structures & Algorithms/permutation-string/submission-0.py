class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1count = {}
        s2count = {}
        l = 0
        for i in range(len(s1)):
            s1count[s1[i]] = 1 + s1count.get(s1[i],0)
        for r in range(len(s2)):
            s2count[s2[r]] = 1 + s2count.get(s2[r], 0)
            while (r-l+1) >= len(s1):
                if s1count == s2count:
                    return True
                else:
                    if s2count[s2[l]] == 1:
                        s2count.pop(s2[l])
                    else:
                        s2count[s2[l]] -= 1
                    l += 1
        return False

        
