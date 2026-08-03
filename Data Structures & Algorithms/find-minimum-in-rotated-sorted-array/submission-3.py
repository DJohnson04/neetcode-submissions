class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        mid = len(nums)//2
        right = len(nums) - 1
        i = 0
        while i < len(nums):
            print(left, mid, right,'values: ', nums[left], nums[mid], nums[right])

            if nums[mid] < nums[right]:
                right = mid
                mid = left
            if nums[mid] > nums[right]:
                left = mid
                mid = (right - left) // 2 + left
            if mid + 1 >= right:
                return min(nums[left], nums[mid], nums[right])
            i+=1
                