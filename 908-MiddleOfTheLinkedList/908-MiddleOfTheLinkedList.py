# Last updated: 10/8/2025, 9:49:42 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        middle=head
        end=head
        while end and end.next:
            middle=middle.next
            end=end.next.next
        return middle

        