class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start: int = 0
        end: int = 0
        maximum: int = 0
        chars = set()

        while end < len(s):
            if s[end] in chars:
                while s[start] != s[end]:
                    chars.remove(s[start])
                    start += 1
                chars.remove(s[start])
                start += 1
            else:
                chars.add(s[end])
                maximum = max(maximum, end-start+1)
                end += 1

        return maximum