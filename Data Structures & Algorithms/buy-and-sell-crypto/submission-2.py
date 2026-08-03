class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = []
        min = 101
        max_profit = 0
        for num in prices:
            if num < min:
                min = num
            else:
                if num - min > max_profit:
                    max_profit = num - min
        return max_profit

