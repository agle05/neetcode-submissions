class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()

        for num in nums:
            seen.add(num)

        longest = 0

        for num in seen:
            if num - 1 not in seen:  # sequence start
                length = 1
                while num + length in seen:  # count upward
                    length += 1
                longest = max(longest, length)


        return longest