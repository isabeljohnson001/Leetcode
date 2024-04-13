class Solution {
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
     boolean[] seen=new boolean[rooms.size()];
        Stack<Integer> s=new Stack();
        seen[0]=true;
        s.push(0);
        while(!s.isEmpty()){
            int node=s.pop();
            for(int key:rooms.get(node)){
             if(!seen[key]){
                 seen[key]=true;
                 s.push(key);
                 
             }   
            }
        }
        for(boolean visit:seen){
            if(!visit){return  false;}
        }


                return true;
        }
}