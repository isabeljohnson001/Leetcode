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
   public List<Integer> largestValues(TreeNode root) {
        if(root==null){return new ArrayList<>();}
        List<TreeNode> que=new ArrayList<>();
        List<Integer> ans=new ArrayList<>();
        que.add(root);
        while(!que.isEmpty()){
            int currentLevel=que.size();
            int max=Integer.MIN_VALUE;
            for(int i=0;i<currentLevel;i++){
                TreeNode node=que.removeFirst();
                max=Math.max(max,node.val);
                if(node.left!=null){que.add(node.left);}
                if(node.right!=null){que.add(node.right);}
            }
            ans.add(max);
        }
        return ans;
        }
}