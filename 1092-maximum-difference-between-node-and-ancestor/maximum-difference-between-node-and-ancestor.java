/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int result=0;
    public int maxAncestorDiff(TreeNode root) {
        if(root==null){
            return 0;
        }
        helper(root,root.val,root.val);
        return result;
    }


    void helper(TreeNode node,int currMax, int currMin){
        if(node==null){
            return;
        }
        int possibleResult=Math.max(Math.abs(currMax-node.val),Math.abs(currMin-node.val));
        result=Math.max(result,possibleResult);
        currMax=Math.max(currMax,node.val);
        currMin=Math.min(currMin,node.val);
        helper(node.left,currMax,currMin);
        helper(node.right,currMax,currMin);
        return;

    }
}