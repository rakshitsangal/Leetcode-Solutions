class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        l,i=len(arr)-1,0
        while i<l and arr[i]<arr[i+1]:
            i+=1
        if i==0 or i==l:
            return False
        while i<l and arr[i]>arr[i+1]:
            i+=1
        return i==l
