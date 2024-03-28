class Pair{
    TreeNode node;
    int depth;
    Pair(TreeNode node,int depth){
        this.node=node;
        this.depth=depth;
    }
}

class Solution {

    public int minDepth(TreeNode root) {

        if(root ==null){
            return 0;
        }
        Stack<Pair> stack=new Stack();
        stack.push(new Pair(root,1));
        int ans=Integer.MAX_VALUE;

        while(!stack.empty()){
            Pair pair=stack.pop();
            TreeNode node=pair.node;
            int depth=pair.depth;
            if(node.left==null && node.right==null){
                ans=Math.min(ans,depth);
            }
            
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