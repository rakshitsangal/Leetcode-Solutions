class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        pos=-prices[0]
        profit=0
        n=len(prices)
        for i in range(1,n):
            pos=max(pos,profit-prices[i])
            profit=max(profit,pos+prices[i]-fee)
        return profit
        
