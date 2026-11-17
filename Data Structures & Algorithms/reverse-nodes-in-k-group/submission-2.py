# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        s = []
        curr = start = head
        first = True
        while curr:
            s.append(curr)
            if len(s) >= k:
                nxt = curr.next
                curr = s.pop() 
                if first:
                    head = curr
                    first = False
                start.next = curr
                while s:
                    before = s.pop() 
                    curr.next = before 
                    curr = before 
                start = curr
                curr.next = nxt
                curr = nxt
            else:
                curr = curr.next
        return head