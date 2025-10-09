// Last updated: 10/8/2025, 9:49:22 PM
class Solution {
    public String removeDuplicates(String s) {
        StringBuilder stack=new StringBuilder();
        for(char c:s.toCharArray()){
            if(stack.length()>0 && stack.charAt(stack.length()-1)==c){
                        stack.deleteCharAt(stack.length()-1);
                    }else{
                        stack.append(c);
            }}
        return stack.toString();
        }
    }