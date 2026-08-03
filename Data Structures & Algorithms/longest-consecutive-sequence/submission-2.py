class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numset = set(nums)
        for p in numset:
            if (p-1) not in numset:
                length = 1
                while p+1 in numset:
                    length += 1
                    p += 1
                if length > longest:
                    longest = length
        return longest

