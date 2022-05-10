class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = sell = prices[0]
        result = 0
        
        for i, p in enumerate(prices):
            if p > sell:
                sell = p
                result = max(result, sell - buy)
            elif p < buy:
                buy = sell = p
                
        return result