class Solution(object):
    def profitableSchemes(self, n, minProfit, group, profit):
        """
        :type n: int
        :type minProfit: int
        :type group: List[int]
        :type profit: List[int]
        :rtype: int
        """
        mod=10**9+7
        m=len(group)
        @cache
        def dp(idx,p,cnt):
            if idx==m:
                return 1 if p>=minProfit and cnt<=n else 0
            if cnt>n: return 0
            ans=0
            #dont consider this idx
            ans+=dp(idx+1,p,cnt)
            #consider it
            ans+=dp(idx+1,min(minProfit,p+profit[idx]),cnt+group[idx])
            return ans%mod
        return dp(0,0,0)
            
        
        
