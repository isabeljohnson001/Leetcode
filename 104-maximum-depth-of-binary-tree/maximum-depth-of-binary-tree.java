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

 // Definition for a binary tree node.

class Pair{
    TreeNode node;
    int depth;
    Pair(TreeNode node,int depth){
        this.node=node;
        this.depth=depth;
    }
}

class Solution {

    public int maxDepth(TreeNode root) {

        if(root ==null){
            return 0;
        }
        Stack<Pair> stack=new Stack();
        stack.push(new Pair(root,1));
        int ans=0;

        while(!stack.empty()){
            Pair pair=stack.pop();
            TreeNode node=pair.node;
            int depth=pair.depth;
            ans=Math.max(ans,depth);
            if(node.left!=null){
                stack.push(new Pair(node.left,depth+1));
            }
            if(node.right!=null){
                stack.push(new Pair(node.right,depth+1));
            }

        }
        return ans;       
    }
}