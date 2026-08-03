class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dicts = {}
        for item in nums:
            if item in dicts:
                dicts[item] = dicts[item] + 1
            else:
                dicts[item] = 1
        num = [0] * 3
        for key,value in dicts.items():
            num[key] = value
        start = 0
        for index, count in enumerate(num):
            if index == 0:
                start = 0
            elif index == 2:
                start = num[0] + num[1]
            else:
                start = num[0]
            while count > 0:
                nums[start] = index
                count -= 1
                start += 1
            
                

                



            
        