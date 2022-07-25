# O(N^2) ->T.C and O(1) ->S.C
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[j]>prices[i]:
                    profit = max(profit, prices[j]-prices[i])
        return profit
        
##################################################################################

# O(N) ->T.C and O(1) ->S.C
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy,sell = float('inf'),0
        for stock in prices:
            buy = min(buy, stock)
            sell = max(sell, stock - buy)
        return sell

####################################################################################

# O(N) ->T.C and O(1) ->S.C
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy, sell = prices[0],0
        for stock in prices:
            if stock<buy:
                buy = stock
            if stock - buy > sell:
                sell = stock - buy
        return sell
