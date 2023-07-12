class Solution(object):
    def tallestBillboard(self, rods):
        """
        :type rods: List[int]
        :rtype: int
        """
        a=sum(rods)//2
        for i in range(len(rods)):
            if sum(rods[0:i+1])==a and sum(rods[i+1:])==a:
                return a
        return 0
