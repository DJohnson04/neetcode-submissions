class Solution:
    def hammingWeight(self, n: int) -> int:
        i = 0
        count = 0
        while i < 32:
            if (1 << i) & n:
                count +=1
            i+=1
        return count