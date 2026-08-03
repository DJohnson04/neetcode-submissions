class Solution:
    def climbStairs(self, n: int) -> int:
        l = [1,2]
        if n == 1:
            return 1
        for num in range(2, n):
            l.append(l[num - 2] + l[num-1])
        return l[-1]