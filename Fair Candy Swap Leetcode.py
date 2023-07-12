class Solution(object):
    def bs (self,arr,j):
        l=0
        r= len(arr)-1
        while l<=r:
            m = (l+r)//2
            if arr[m]==j:
                return True
            if  arr[m]<j:
                l=m+1
            else:
                r= m-1
        return False 
    def fairCandySwap(self, aliceSizes, bobSizes):
        """
        :type aliceSizes: List[int]
        :type bobSizes: List[int]
        :rtype: List[int]
        """
        aliceSum= sum(aliceSizes)
        bobSum = sum(bobSizes)
        aliceSizes.sort()
        const = (aliceSum-bobSum)//2
        for i in bobSizes:
            diff = i+const
            x = self.bs(aliceSizes,diff)
            if x:
                return [diff,i]
            
