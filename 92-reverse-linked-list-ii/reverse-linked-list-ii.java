/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseBetween(ListNode head, int left, int right) {
    if(left==right){
        return head;
    }
    ListNode dummy=new ListNode(0);
    dummy.next=head;
    ListNode prev=dummy;
    ListNode curr =head;
    for(int i=0;i<left-1;i++){
        prev=prev.next;
        curr=curr.next;
    }
    for(int i=0;i<right-left;i++){
        // head = [1,2,3,4,5], left = 2, right = 4
        ListNode nextNode = curr.next;
        curr.next = nextNode.next;
        nextNode.next = prev.next;
        prev.next = nextNode;
    }
    return dummy.next;
    }
}