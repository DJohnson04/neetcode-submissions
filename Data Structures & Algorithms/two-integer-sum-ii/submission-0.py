class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_p = 0
        right_p = len(numbers) - 1
        while left_p < right_p:
            if numbers[left_p] + numbers[right_p] == target:
                return [left_p + 1,right_p + 1]
            if numbers[left_p] + numbers[right_p] < target:
                left_p += 1
            else:
                right_p -= 1
            
            