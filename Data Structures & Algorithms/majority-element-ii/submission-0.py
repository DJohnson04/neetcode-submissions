class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        majority = []
        dic = {}
        for item in nums:
            if item in dic.keys():
                dic[item] += 1
            else:
                dic[item] = 1
        for num, val in dic.items():
            if val > len(nums)/3:
                majority.append(num)
        return majority