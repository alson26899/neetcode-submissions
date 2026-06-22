class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx_profit = 0
        min_price = prices[0]

        for i in range(len(prices)):
            min_price=min(min_price,prices[i])

            profit = prices[i] - min_price

            mx_profit = max(mx_profit,profit)

        return mx_profit


 