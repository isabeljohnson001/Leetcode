# Last updated: 10/8/2025, 9:51:49 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        prev=None
        while slow:
            nextNode=slow.next
            slow.next=prev
            prev=slow
            slow=nextNode
        
        left,right=head,prev
        while right:
            if left.val!=right.val:
                return False
            left=left.next
            right=right.next
        
        return True