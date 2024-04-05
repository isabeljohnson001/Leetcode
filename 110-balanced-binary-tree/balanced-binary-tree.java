
    class TreeInfo{
        int height;
        boolean balanced;

        TreeInfo(int height,boolean balanced){
            this.height=height;
            this.balanced=balanced;
        }
    }
    class Solution{
        public TreeInfo dfs(TreeNode root){
            if(root==null){
                return new TreeInfo(-1,true);
            }
            TreeInfo left=dfs(root.left);
            if(!left.balanced){
                return new TreeInfo(-1,false);
            }
            TreeInfo right=dfs(root.right);
            if(!right.balanced){
                return new TreeInfo(-1,false);
            }
            if(Math.abs(left.height- right.height)<2){
                return new TreeInfo(Math.max(left.height,right.height)+1,true);
            }

            return new TreeInfo(-1,false);
        }
        
        public boolean isBalanced(TreeNode root){
            return dfs(root).balanced;
        }
    }