class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * (len(nums) * 2)
        for index, element in enumerate(nums):
            ans[index] = element
            ans[index + len(nums)] = element
        return ans