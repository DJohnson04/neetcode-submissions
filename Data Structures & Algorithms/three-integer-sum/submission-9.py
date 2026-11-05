class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right and left < len(nums) - 1:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                if sum > 0:
                    right -= 1
                if sum == 0:
                    results.append((nums[i],nums[left],nums[right]))
                    left += 1
                    right -= 1
                    
        return list(set(results))