class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = sell = prices[0]
        max_profit = 0
        
        for i, price in enumerate(prices):
            if price > sell:
                sell = price
                max_profit = max(max_profit, sell - buy)
            elif price < buy:
                buy = sell = price
                
        return max_profit
                
        