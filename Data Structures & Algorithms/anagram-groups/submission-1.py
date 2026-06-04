class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}

        for s in strs:
            sorted_strs = ''.join(sorted(s))
            if sorted_strs in anagram:
                anagram[sorted_strs].append(s)
            else:
                anagram[sorted_strs] = [s]
            
        return list(anagram.values())

