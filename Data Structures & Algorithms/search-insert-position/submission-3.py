class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if target > nums[0]:
                return 1
            else:
                return 0
        mid = int(len(nums) / 2)
        left, right = 0, len(nums) - 1
        while nums[mid] != target and left + 1 != right:
            if nums[mid] < target:
                left = mid
            if nums[mid] > target:
                right = mid
            mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if target > nums[right]:
            return right + 1
        if target > nums[left]:
            return left + 1
        else:
            return left
