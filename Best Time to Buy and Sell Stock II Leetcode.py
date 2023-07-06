class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(max(b-a,0) for a,b in zip(prices, prices[1:]))
