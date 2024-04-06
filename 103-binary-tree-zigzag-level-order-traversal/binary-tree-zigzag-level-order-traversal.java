/**
 * Definition for a binary tree node.
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode() {}
 * TreeNode(int val) { this.val = val; }
 * TreeNode(int val, TreeNode left, TreeNode right) {
 * this.val = val;
 * this.left = left;
 * this.right = right;
 * }
 * }
 */
class Solution {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
            if (root == null) {
                return new ArrayList<List<Integer>>();
            }
            List<TreeNode> queue = new ArrayList<>();
            List<List<Integer>> ans = new ArrayList<List<Integer>>();
            queue.add(root);
            queue.add(null);
            List<Integer> nodes=new ArrayList<>();;
            boolean zigzag = true;
            while (queue.size()>0) {
                TreeNode node=queue.removeFirst();
                if(node!=null){
                    if(zigzag){nodes.addLast(node.val);
                    }
                    else{nodes.addFirst(node.val);}
                    if(node.left!=null){queue.add(node.left);}
                    if(node.right!=null){queue.addLast(node.right);}
                }
                else{

                    ans.add(nodes);
                    nodes= new ArrayList<>();
                    if (queue.size() > 0)
                        queue.addLast(null);
                    zigzag = !zigzag;
                }}
            return ans;
        }
}