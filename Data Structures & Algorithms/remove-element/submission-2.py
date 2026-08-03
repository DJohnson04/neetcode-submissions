class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = len(nums)
        left = 0
        right = len(nums) - 1
        if left <= right:
            if right < left:
                return 0
            if right == left:
                if nums[0] == val:
                    return 0
                else:
                    return 1
        while left < right:
            while nums[right] == val:
                right -= 1
                count -= 1
                if right < 0:
                    return 0
            if nums[left] == val:
                nums[left] = nums[right]
                nums[right] = val
                right -= 1
                count -= 1
            left += 1
        return count