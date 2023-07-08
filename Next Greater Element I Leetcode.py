class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        l=[]
        for i in nums1:
            fl=0
            for j in range(nums2.index(i),len(nums2)):
                if nums2[j]>i:
                    l.append(nums2[j])
                    fl=1
                    break
            if fl==0:
                l.append(-1)
        return l
