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
    public ListNode deleteDuplicatesUnsorted(ListNode head) {
        ListNode curr=head;
        HashMap<Integer,Integer> hs=new HashMap<>();
        while (curr!=null){
            hs.put(curr.val, hs.getOrDefault(curr.val,0)+1);
            curr=curr.next;
        }
        ListNode dummy=new ListNode(0);
        curr=dummy;
        while (head!=null){
            if(hs.get(head.val)==1){
                curr.next=head;
                curr=curr.next;
            }
            head=head.next;
        }
        curr.next=null;
        return dummy.next;
    }
}