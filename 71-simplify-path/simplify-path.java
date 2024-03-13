class Solution {
    public String simplifyPath(String path) {
        StringBuilder s=new StringBuilder();
        Stack<String> stack=new Stack<>();
        String[] arr=path.split("/");
        for(String c : arr){
            if(c.isEmpty()||c.equals("/")||c.equals(".")) {continue;}
            else{
                if(c.equals("..")){
                if(!stack.isEmpty())
                    stack.pop();
                }
                else{
                stack.push(c);}
            }
        }
        for(String item: stack){
            s.append("/");
            s.append(item);

        }
        return s.length()>0?s.toString():"/";
    }
}
