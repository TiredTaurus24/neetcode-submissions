class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for i in s:
            if i not in Map:
                stack.append(i)
                continue
            if not stack or stack[-1] != Map[i]:
                return False
            stack.pop()

        return not stack     