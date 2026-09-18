class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left, right, target):
            while left <= right:
                mid =left + (right - left) // 2
                if target < nums[mid]:
                    right = mid - 1
                elif target > nums[mid]:
                    left = mid + 1
                elif target == nums[mid]:
                    return mid
            return -1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) //2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return max(binary_search(0,left, target), binary_search(left, len(nums) - 1, target))
        