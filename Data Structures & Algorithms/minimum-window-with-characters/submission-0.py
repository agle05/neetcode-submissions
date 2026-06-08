from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left: int = 0
        seen: int = 0
        shortest: float = float('inf')

        res_left: int
        res_right: int

        count_s, count_t = defaultdict(int), defaultdict(int)

        for char in t:
            count_t[char] += 1

        for right in range(len(s)):
            count_s[s[right]] += 1
            if s[right] in t and count_s[s[right]] == count_t[s[right]]: seen += 1
            if seen == len(count_t): # shrink window
                while seen == len(count_t):
                    if right-left+1 < shortest:
                        shortest = right-left+1
                        res_left, res_right = left, right
                    count_s[s[left]] -= 1
                    if s[left] in t and count_s[s[left]] < count_t[s[left]]:
                        seen -= 1
                    left += 1

        if shortest == float('inf'): return ""
        else: return s[res_left:res_right+1]
                    
            
