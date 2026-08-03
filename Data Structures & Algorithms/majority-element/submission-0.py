class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ma = {}
        for i in nums:
            if i not in ma:
                ma[i] = 1
            else:
                ma[i] += 1
        for key, value in ma.items():
            if value > (len(nums)/2):
                return key
        