# Last updated: 10/8/2025, 9:48:00 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        current=head
        values=[]
        while current:
            values.append(current.val)
            current=current.next
        i=0
        j=len(values)-1
        maxSum=0
        while(i<j):
            maxSum=max(maxSum,values[i]+values[j])
            i+=1
            j-=1
        return maxSum

        