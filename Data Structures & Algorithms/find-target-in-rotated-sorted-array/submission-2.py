class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid

            # First half sorted
            if nums[mid] >= nums[left]:
                # Target in first half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                # Target in second half
                else:
                    left = mid + 1
            # Right half sorted
            else: 
                # Target in second half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                # Target in first half
                else:
                    right = mid - 1
        # Target not in arr
        return -1
            
            