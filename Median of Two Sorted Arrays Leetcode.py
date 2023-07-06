class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums1.sort()
        if len(nums1)%2==0:
            r=len(nums1)/2
            return float(nums1[r]+nums1[r-1])/float(2)
        else:
            r=len(nums1)/2
            return float(nums1[r]) 
