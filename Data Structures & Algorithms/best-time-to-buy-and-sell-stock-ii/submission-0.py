class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        first = 0
        index = 0
        while index < len(prices):
            while index + 1 < len(prices) and  prices[index + 1] > prices[index]:
                index += 1
            profit += (prices[index] - prices[first])
            if index < len(prices) - 1:
                first = index + 1
                index = index + 1
            else: 
                return profit
        return profit

            

        