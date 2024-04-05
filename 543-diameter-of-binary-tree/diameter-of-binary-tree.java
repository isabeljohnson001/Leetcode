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
public class Solution{
    public int daimeter;

public int diameterOfBinaryTree(TreeNode root) {
        daimeter=0;
        longestPath(root);
        return daimeter;
    }
    public int longestPath(TreeNode node){
        if(node==null){
            return 0;
        }
        int left=longestPath(node.left);
        int right=longestPath(node.right);
        daimeter=Math.max(daimeter, left+right);
        return Math.max(left,right)+1;
    }

}