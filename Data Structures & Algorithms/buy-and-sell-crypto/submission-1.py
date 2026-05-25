class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1

        maxP = 0

        while r < len(prices) and l < r:
            if prices[r] < prices[l]:
                l = r
                r = r + 1
                continue
            
            maxP = max(maxP, prices[r] - prices[l])
            r += 1
            print(maxP)
        
        return maxP