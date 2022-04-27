# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = res_head = ListNode()
        sum = 0
        
        while l1 or l2 or sum:
            if l1:
                sum += l1.val
                l1 = l1.next
            
            if l2:
                sum += l2.val
                l2 = l2.next
        
            res.val = sum % 10
            sum = sum // 10
        
            if l1 or l2 or sum:
                res.next = ListNode()
                res = res.next
        
        return res_head