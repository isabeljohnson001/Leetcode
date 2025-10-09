// Last updated: 10/8/2025, 9:48:51 PM
class Solution {
    public boolean isPathCrossing(String path) {
      boolean visited=false;
        Map<Character, int[]> moves=new HashMap();
        moves.put('N',new int[]{0,1});
        moves.put('S',new int[]{0,-1});
        moves.put('W',new int[]{1,0});
        moves.put('E',new int[]{-1,0});

        Set<String> hs=new HashSet<>();
        String position="0,0";
        hs.add(position);
        int x=0;
        int y=0;
        char[] nodes=path.toCharArray();
        for(int i=0;i<nodes.length;i++){
            int[] pos=moves.get(nodes[i]);
            int dx=pos[0];
            int dy=pos[1];
            x+=dx;
            y+=dy;
            position=x+","+y;
            if(hs.contains(position)){
                visited=true;
                break;
            }
            hs.add(position);
        }
        return visited;
    }
}