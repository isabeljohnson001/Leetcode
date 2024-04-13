class Solution {
    public void dfsGraph(int node,int[][] isConnected,boolean[] visit){
            visit[node]=true;
            int n= isConnected.length;
            for(int i=0;i<n;i++){

                if(isConnected[node][i]==1 && !visit[i]){
                dfsGraph(i,isConnected,visit);
            }

        }}
        public int findCircleNum(int[][] isConnected) {
            int n=isConnected.length;
            boolean[] visited=new boolean[n];
            int provinces=0;

            for(int i=0;i<n;i++){
                if(!visited[i]){
                    provinces++;
                    dfsGraph(i,isConnected,visited);
                }

            }
            return provinces;

        }
}