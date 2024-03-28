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
    int curr;
    Pair(TreeNode node, int curr){
        this.node=node;
        this.curr=curr;
    }
}
class Solution {
    public boolean hasPathSum(TreeNode root, int targetSum) {
        if(root==null){
            return false;
        }
        Stack<Pair> stack=new Stack();
        stack.push(new Pair(root,0));
        while(!stack.empty()){
            Pair pair=stack.pop();
            TreeNode node=pair.node;
            int curr=pair.curr;

            if(node.left==null && node.right ==null){
                if(curr+node.val==targetSum){
                    return true;
                }}
            curr+=node.val;
            if(node.left!=null){
                stack.push(new Pair(node.left,curr));
            }
            if(node.right!=null){
                stack.push(new Pair(node.right,curr));
            }
            
        }
        return false;
        
    }
}