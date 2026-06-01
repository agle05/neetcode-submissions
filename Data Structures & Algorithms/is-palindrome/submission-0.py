class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ("".join(char for char in s if char.isalnum())).lower()
        left, right = 0, len(cleaned) - 1
        
        while left < right:
            if cleaned[left] != cleaned[right]:
                return False
            else:
                left += 1
                right -= 1

        return True