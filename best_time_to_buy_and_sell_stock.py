class Solution:
    def maxProfit(self, prices):
        min_value = float('inf') # Start with a very high number such as infinity
        max_profit = 0
        for price in prices:
            if price < min_value:
                min_value = price
            else:
                profit = price - min_value
                if profit > max_profit:
                    max_profit = profit

        return max_profit

    

prices = [7,1,5,3,6,4]
S1 = Solution()
result = S1.maxProfit(prices)
print(result)