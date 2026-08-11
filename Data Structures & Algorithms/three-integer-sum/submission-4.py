
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()
        
        for index, num in enumerate(nums):
            left_pointer = index + 1
            right_pointer = len(nums) - 1
            while left_pointer < right_pointer:
                if nums[left_pointer] + nums[right_pointer] + num == 0:
                    result.add((num, nums[left_pointer], nums[right_pointer]))
                    left_pointer += 1
                    right_pointer -= 1
    
                elif nums[left_pointer] + nums[right_pointer] + num < 0:
                    left_pointer += 1
                else:
                    right_pointer -= 1
        return list(result)


