class Solution:
    def maxProfit(self, prices):
        hold = -prices[0]
        sell = 0
        sell_cd = 0
        
        for price in prices:
            hold, sell, sell_cd = max(hold, sell - price), max(sell, sell_cd), hold + price

        return max(sell, sell_cd)