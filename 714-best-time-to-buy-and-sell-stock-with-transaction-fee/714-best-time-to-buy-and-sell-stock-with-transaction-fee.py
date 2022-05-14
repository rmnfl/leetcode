class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy = -prices[0]
        sell = 0
        
        for p in prices:
            buy, sell = max(buy, sell - p), max(sell, buy + p - fee)
            
        return sell
