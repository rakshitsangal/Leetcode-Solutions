# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        current = result
        carry = 0
        current_val = 0
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            current_val = val1 + val2 + carry
            carry = current_val // 10
            current.val = current_val % 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            if l1 or l2:
              current.next = ListNode(0)
              current = current.next
        if carry > 0:
            current.next = ListNode(carry)
        return result
