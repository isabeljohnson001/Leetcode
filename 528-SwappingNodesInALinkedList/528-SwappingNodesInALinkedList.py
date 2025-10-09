# Last updated: 10/8/2025, 9:50:39 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        length=1
        curr=head
        
        while curr.next:
            length+=1
            curr=curr.next
        
        curr=head
        frontNode=head
        endNode=head

        for _ in range(k-1):
            frontNode=frontNode.next
        for _ in range(length-k):
            endNode=endNode.next

        frontNode.val,endNode.val=endNode.val,frontNode.val

        return head