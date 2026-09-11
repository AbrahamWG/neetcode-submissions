# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # use helper to compute 

        def helper(node):
            count = 0
            ret = 0
            curr = node
            while curr:
                ret += curr.val * 10 ** count
                count += 1
                curr = curr.next
            return ret
        
        SUM = list(str(helper(l1) + helper(l2)))
        res = ListNode()
        curr = res

        while SUM:
            curr.val = int(SUM.pop())
            if len(SUM) == 0:
                return res
            curr.next = ListNode()
            curr = curr.next