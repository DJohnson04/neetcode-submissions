class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        dic = {}
        l = []
        for num in nums:
            dic[num] = 1
        
        for num in dic.keys():
            if num - 1 not in dic:
                l.append(num)
        po = 0
        for p in l:
            po = 1
            while p+1 in dic.keys():
                print(p)
                p+=1
                po += 1
            if po > longest:
                longest = po
        return longest
        print(l)

