class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        prev = prices[0]
        
        for i, p in enumerate(prices):
            if prev < p:
                profit += p - prev
            prev = p
            
        return profit