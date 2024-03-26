class Solution {
    public int equalPairs(int[][] grid) {
    HashMap<String,Integer> hs=new HashMap<>();

    for(int[] row:grid){
        String key=ConvertToString(row);
        hs.put(key, hs.getOrDefault(key,0)+1);
    }

    HashMap<String,Integer> hs2=new HashMap<>();
    for(int col=0;col<grid[0].length;col++){
        int[] colArr=new int[grid.length];
        for(int row=0;row<grid.length;row++){
            colArr[row]=grid[row][col];
        }
        String key=ConvertToString(colArr);
        hs2.put(key,hs2.getOrDefault(key,0)+1);

    }
    int ans=0;
    for(String key:hs.keySet()) {
        ans += hs.get(key) * hs2.getOrDefault(key,0);
    }
    return ans;
    }

    public String ConvertToString(int[] arr){
        StringBuilder s=new StringBuilder();
        for(int i=0;i< arr.length;i++){
            s.append(arr[i]);
            s.append(",");
        }
        return s.toString();
    }
}