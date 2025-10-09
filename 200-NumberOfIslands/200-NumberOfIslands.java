// Last updated: 10/8/2025, 9:52:01 PM
class Solution {
    private int m;
    private int n;
    public int[][]  dirs=new int[][]{{0,1},{0,-1},{-1,0},{1,0}};
            public int numIslands(char[][] grid) {
            int count=0;
            //numner rows and column..iterate in forloop..if we find ==1..cout ++;bfs()
            m= grid.length;
            n=grid[0].length;
            for(int i=0;i<m;i++){
                for(int j=0;j<n;j++){
                    if(grid[i][j]=='1'){
                        count++;
                        bfsGraph3(grid,i,j);
                    }
                }

            }

            return count;

        }

        public void bfsGraph3(char[][] grid,int r,int c){
            Queue<int[]> que=new LinkedList<>();
            
            que.add(new int[]{r,c});
            while ((!que.isEmpty())){
                int[] curr=que.poll();
                for(int[] dir: dirs){
                int nr=curr[0]+dir[0];
                int nc=curr[1]+dir[1];
                if(0<=nr && nr<m && 0<=nc && nc<n && grid[nr][nc]=='1'){
                grid[nr][nc]='0';
                que.offer(new int[]{nr,nc});
                }
                }
            }
        }
}