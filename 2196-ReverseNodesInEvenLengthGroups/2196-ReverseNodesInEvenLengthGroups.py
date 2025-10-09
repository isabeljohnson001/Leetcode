# Last updated: 10/8/2025, 9:48:03 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseLinkedList(self,head, k):
        prev, curr = None, head
        while k > 0:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            k -= 1
        return prev, head

    def reverseEvenLengthGroups(self,head):
        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy
        current = head
        group_length = 1
        
        while current:
            last_node_of_group = current
            count = 0
            
            # Find the last node of the current group
            while count < group_length and last_node_of_group:
                last_node_of_group = last_node_of_group.next
                count += 1
            
            if count % 2 == 0:  # Even group
                next_group_start = last_node_of_group
                # Reverse this group
                reversed_head, reversed_tail = self.reverseLinkedList(current, count)
                # Link the reversed group
                prev_group_end.next = reversed_head
                reversed_tail.next = next_group_start
                prev_group_end = reversed_tail
                current = next_group_start
            else:  # Odd group, move the prev_group_end
                while count > 0 and current:
                    prev_group_end = current
                    current = current.next
                    count -= 1
            
            group_length += 1

        return dummy.next