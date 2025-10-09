// Last updated: 10/8/2025, 9:48:54 PM
class Solution {
    public String makeGood(String s) {
        Stack<Character> stack=new Stack<>();
        for(char c:s.toCharArray()){
            if (!stack.isEmpty()&& Math.abs(stack.peek()-c)==32){
                    stack.pop();
        }else{stack.push(c);}
        }
        StringBuilder st=new StringBuilder();
        for(char item :stack){
            st.append(item);
        }
        return st.toString();
    }
}