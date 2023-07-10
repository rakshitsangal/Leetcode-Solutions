class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.append(0)
        for i in range(len(cost)-3,-1,-1) :
            cost[i] += min(cost[i+1],cost[i+2])
        return min(cost[0],cost[1])
