// Last updated: 10/8/2025, 9:52:04 PM
class Solution {
    public static List<Integer> rightSideView(TreeNode root) {
            if (root == null) {
                return new ArrayList<>();
            }
            int value=0;
            List<TreeNode> que = new ArrayList<>();
            List<Integer> ans = new ArrayList<>();
            que.add(root);
            while (!que.isEmpty()) {
                int currentLevel = que.size();
                for (int i = 0; i < currentLevel; i++) {
                    TreeNode node = que.removeFirst();
                    value = node.val;
                    if(node.left!=null){que.add(node.left);}
                    if(node.right!=null){que.add(node.right);}
                }
                ans.add(value);
            }
            return ans;

        }
}