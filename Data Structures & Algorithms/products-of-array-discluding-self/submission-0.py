class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        total_product = 1
        is_zero = 0
        for num in nums:
            if num == 0:
                is_zero += 1
            else:
                total_product *= num
        if is_zero > 1:
            return result
        for index,num in enumerate(nums):
            if is_zero == 0 or num == 0:
                result[index] = int(total_product) if num == 0 else int(total_product/num)
            else:
                result[index] = 0
        return result
            
            