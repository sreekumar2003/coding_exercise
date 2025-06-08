#Best method

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit

  #simple method but takes more time

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        sum = 0
        for i in range (0,length-1):
            for j in range(i+1,length):
               if prices[j]-prices[i]>sum:
                    sum = prices[j]-prices[i]
        return sum

        
