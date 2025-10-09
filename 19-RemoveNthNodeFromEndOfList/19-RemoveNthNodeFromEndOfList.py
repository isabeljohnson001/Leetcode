# Last updated: 10/8/2025, 9:53:06 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy=ListNode(0)
        dummy.next=head
        length=1
        first=head
        while first.next:
            length+=1
            first=first.next
        pos=length-n
        first=dummy
        while(pos>0):
            first=first.next
            pos-=1
        first.next=first.next.next
        return dummy.next

