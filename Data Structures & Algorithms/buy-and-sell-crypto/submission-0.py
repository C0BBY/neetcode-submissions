class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = 0
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = sell = prices[i]
            if prices[i] > sell:
                sell = prices[i]
            profit = max(profit, sell - buy)

        
        return profit                