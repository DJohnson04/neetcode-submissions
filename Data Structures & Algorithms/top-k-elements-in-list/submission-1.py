class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = [0] * 2002
        ## populate 
        for n in nums:
            num_count[abs(n) if n < 0  else n + 1000] = num_count[abs(n) if n < 0  else n + 1000] + 1
        highest = 0
        cur_index = 0
        result = []
        while (len(result) < k):
            for index, count in enumerate(num_count):
                if count > highest:
                    highest = count
                    cur_index = index
            if cur_index >= 1000:
                cur_index = cur_index - 1000
                result.append(cur_index)
                num_count[cur_index + 1000] = -1
            else:
                cur_index = cur_index * -1
                result.append(cur_index)
                num_count[cur_index * -1] = -1
            cur_index, highest = 0,0
            
        return result