class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)-1):
            complement = -(numbers[i]-target)
            if complement in numbers and numbers.index(complement) != i:
                left, right = min(i, numbers.index(complement)), max(i, numbers.index(complement))
                return [left + 1, right + 1]