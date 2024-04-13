class Solution {
    Set<String> roads=new HashSet<>();
        HashMap<Integer,List<Integer>> graph=new HashMap<>();
        Set<Integer> seen=new HashSet<>();
    public int minReorder(int n, int[][] connections) {
            ///seen,graph,roads
            
            for(int i=0;i<n;i++){
                graph.put(i,new ArrayList<>());
            }
            for(int[] connection :connections){
                int x=connection[0];
                int y=connection[1];
                graph.get(x).add(y);
                graph.get(y).add(x);
                roads.add(convertToHash(x,y));
            }
            seen.add(0);
            return dfsGraph2(0);
        }
        public int dfsGraph2(int node){
            int ans=0;
            for(int neighbour:graph.get(node)){
                if(!seen.contains(neighbour)){
                    if(roads.contains(convertToHash(node,neighbour))){
                        ans++;
                    }
                    seen.add(neighbour);
                    ans+=dfsGraph2(neighbour);
                }
            }

return ans;
        }

        public String convertToHash(int x,int y){
            return String.valueOf(x)+","+String.valueOf(y);
        }
}