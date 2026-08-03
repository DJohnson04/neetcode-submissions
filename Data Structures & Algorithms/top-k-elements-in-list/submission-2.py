class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maps = {}
        for num in nums:
            if num in maps:
                maps[num] += 1
            else:
                maps[num] = 1
        frequency = [[] for _ in range(len(nums) + 1)]
        result = []
        for key in maps:
            frequency[maps[key]].append(key)
        for i in range(len(frequency) - 1, 0, -1):
            for num in frequency[i]:
                if len(result) < k:
                    result.append(num)
                else:
                    return result
                
        return result

