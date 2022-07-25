class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy,sell = float('inf'),0
        for stock in prices:
            buy = min(buy, stock)
            sell = max(sell, stock - buy)
        return sell

####################################################################################

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy, sell = prices[0],0
        for stock in prices:
            if stock<buy:
                buy = stock
            if stock - buy > sell:
                sell = stock - buy
        return sell
