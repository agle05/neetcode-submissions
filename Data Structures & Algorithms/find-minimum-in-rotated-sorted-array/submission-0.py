class Solution:
    def findMin(self, nums: List[int]) -> int:
        output = 1001
        for num in nums:
            output = min(output, num)

        return output