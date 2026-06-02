class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr = sorted(nums)
        output = []

        for i in range(len(arr) - 2):
            if i > 0 and arr[i] == arr[i - 1]:
                continue

            left, right = i + 1, len(arr) - 1

            while left < right:
                total = arr[left] + arr[right] + arr[i]

                if total == 0:
                    output.append([arr[i], arr[left], arr[right]])
                    while left < right and arr[left] == arr[left + 1]:
                        left += 1
                    while left < right and arr[right] == arr[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total > 0:
                    right -= 1
                else:
                    left += 1

        return output