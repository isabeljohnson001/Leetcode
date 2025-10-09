# Last updated: 10/8/2025, 9:52:35 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if not head and left==right:
            return head
        
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy

        for _ in range(left-1):
            prev=prev.next

        curr=prev.next
        nextNode=None

        for _ in range(right-left):
            nextNode=curr.next
            curr.next=nextNode.next
            nextNode.next=prev.next
            prev.next=nextNode
        
        return dummy.next

        