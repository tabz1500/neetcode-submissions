class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minS = prices[0]
        maxP = 0

        for i in range(1, len(prices)):
            minS = min(minS, prices[i])
            maxP = max(maxP, prices[i] - minS)
        return maxP