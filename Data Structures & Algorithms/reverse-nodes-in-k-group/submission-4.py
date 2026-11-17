# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # s = []
        # curr = start = head
        # first = True
        # while curr:
        #     s.append(curr)
        #     if len(s) >= k:
        #         nxt = curr.next
        #         curr = s.pop() 
        #         if first:
        #             head = curr
        #             first = False
        #         start.next = curr
        #         while s:
        #             before = s.pop() 
        #             curr.next = before 
        #             curr = before 
        #         start = curr
        #         curr.next = nxt
        #         curr = nxt
        #     else:
        #         curr = curr.next
        # return head

        dummy = ListNode(0, head)
        l = dummy
        curr = head
        while curr:                
            r = curr
            for _ in range(k):
                if not r:
                    return dummy.next
                r = r.next
            group_first = curr
            prev = r
            while curr != r:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            l.next = prev
            l = group_first
        return dummy.next


