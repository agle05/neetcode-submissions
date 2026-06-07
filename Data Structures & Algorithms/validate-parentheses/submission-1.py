from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', ']': '[', '}': '{'}
        stack = []

        for char in s:
            if char in pairs:
                if not stack or stack[-1] != pairs[char]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(char)
                
        if stack:
            return False
        else:
            return True