# Last updated: 10/8/2025, 9:49:07 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        val=[]

        while head:
            val.append(head.val)
            head=head.next
        binary_string = "".join(map(str, val))  # No spaces
        return int(binary_string,2)
        