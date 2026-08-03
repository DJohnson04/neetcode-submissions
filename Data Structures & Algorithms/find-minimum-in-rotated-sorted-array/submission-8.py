class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        mid = len(nums)//2
        right = len(nums) - 1
        while True:
            if nums[mid] < nums[right]:
                right = mid
                mid = left
            if nums[mid] > nums[right]:
                left = mid
                mid = (right - left) // 2 + left

            if mid + 1 >= right:
                return  min(nums[mid], nums[left], nums[right])
                