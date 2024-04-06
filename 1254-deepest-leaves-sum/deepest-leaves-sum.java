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
    public int deepestLeavesSum(TreeNode root) {
            
            if(root==null){
                return 0;
            }
            List<TreeNode> queue=new ArrayList<>();
            queue.add(root);
            int sum=0;
            while(!queue.isEmpty()){
                int currentLevel= queue.size();
                sum=0;
                for(int i=0;i<currentLevel;i++){
                    TreeNode node=queue.removeFirst();
                    sum+=node.val;
                    if(node.left!=null){queue.add(node.left);}
                    if(node.right!=null){queue.add(node.right);}
                }
            }
            return sum;
        }
}