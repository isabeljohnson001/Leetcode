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
    public int getMinimumDifference(TreeNode root) {
            int ans=Integer.MAX_VALUE;
            List<Integer> values=new ArrayList<>();
            dfs(root,values);
            for(int i=1;i<values.size();i++){
                ans=Math.min(ans,values.get(i)-values.get(i-1));
            }
            return ans;

        }
        public List<Integer> dfs(TreeNode node,List<Integer> ls){
            if(node==null){
                return new ArrayList<>();
            }
            dfs(node.left,ls);
            ls.add(node.val);
            dfs(node.right,ls);
            return ls;
        }
}