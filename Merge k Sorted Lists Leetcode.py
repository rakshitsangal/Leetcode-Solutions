# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        n=len(lists)
        min_heap=[]
        heapq.heapify(min_heap)
        for i in range(n):
            if lists[i]:
                temp_val=lists[i].val
                lists[i]=lists[i].next
                heapq.heappush(min_heap,[temp_val,i])
        head=ListNode()
        node=head
        
        while min_heap:
            val,ind=heapq.heappop(min_heap)
            node_i=ListNode(val=val)
            node.next=node_i
            node=node.next
            if lists[ind]:
                temp_val=lists[ind].val
                lists[ind]=lists[ind].next
                heapq.heappush(min_heap,[temp_val,ind])
        return head.next
