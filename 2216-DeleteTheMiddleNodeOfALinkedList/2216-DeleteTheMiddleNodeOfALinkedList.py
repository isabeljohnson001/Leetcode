# Last updated: 10/8/2025, 9:48:01 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head.next:
            return 
        length=1

        curr=head
        while  curr.next:
            length+=1
            curr=curr.next
        mid=length//2

        curr=head
        for _ in range(mid-1):
            curr=curr.next
        
        curr.next=curr.next.next
        return head


        