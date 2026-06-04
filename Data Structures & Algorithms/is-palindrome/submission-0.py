class Solution:
    def isPalindrome(self, s: str) -> bool:
        no_space = ''.join(char for char in s if char.isalnum())
        no_space_sent = no_space.lower()
        l = 0
        r = len(no_space_sent) - 1
        while l < r:
            if no_space_sent[l] == no_space_sent[r]:
                l += 1
                r -= 1
            else:
                return False

        return True
        