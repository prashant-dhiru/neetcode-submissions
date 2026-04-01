# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start, end = head, head
        
        #create gap between start and end
        for i in range(1,n):
            end = end.next
        
        #move start and end pts to end of the LL
        while end and end.next:
            start = start.next
            end = end.next
        
        if start == head:
            head = head.next
        
        curr = head
        while curr:
            if curr.next == start:
                curr.next = curr.next.next
                continue
            curr = curr.next

        return head
