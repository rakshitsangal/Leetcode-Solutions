from heapq import *
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        heap=[]
        for i in range(min(k,len(nums1))):
            for j in range(min(k,len(nums2))):
                if len(heap)<k:
                    heappush(heap,(-(nums1[i]+nums2[j]),nums1[i],nums2[j]))

                else:
                    if nums1[i]+nums2[j]>-heap[0][0]:
                        break

                    else:
                        heappushpop(heap,(-(nums1[i]+nums2[j]),nums1[i],nums2[j]))


        return [[first,second] for _,first,second in heap]                        
