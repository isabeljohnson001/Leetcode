// Last updated: 10/8/2025, 9:49:02 PM
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
 class Pair{
    TreeNode node;
    int maxSoFar;
    Pair(TreeNode node, int maxSoFar){
        this.node=node;
        this.maxSoFar=maxSoFar;
    }
 }
class Solution {
    public int goodNodes(TreeNode root) {
        
        if(root==null){
            return 0;
        }
        Stack<Pair> stack =new Stack();
        stack.push(new Pair(root,Integer.MIN_VALUE));
        int ans=0;
        while(!stack.empty()){
            Pair pair=stack.pop();
            TreeNode node=pair.node;
            int maxSoFar=pair.maxSoFar;
            if(node.val>=maxSoFar){
                ans++;
            }
            if(node.left!=null){
                stack.push(new Pair(node.left,Math.max(maxSoFar,node.val)));
            }
            if(node.right!=null){
                stack.push(new Pair(node.right,Math.max(maxSoFar,node.val)));
            }
        }
        return ans;
    }
}