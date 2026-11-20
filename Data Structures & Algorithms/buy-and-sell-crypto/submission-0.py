class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min = prices[0]
        max_profit = 0
        for r in range(len(prices)):
            if prices[r] < curr_min:
                curr_min = prices[r]
            profit = prices[r] - curr_min
            max_profit = max(max_profit, profit)
        return max_profit
