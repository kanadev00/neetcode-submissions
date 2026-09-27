class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #iterate through prices
        max_benefit = 0
        min_price = prices[0]
        for i in range(1, len(prices)):
            if min_price > prices[i-1]:
                min_price = prices[i-1]
            # calculate benefit with minimal value of the left side of the buying date(i)
            benefit = prices[i]- min_price

            if max_benefit < benefit:
                max_benefit = benefit

        return max_benefit
                