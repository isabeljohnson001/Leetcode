class Solution {
    public int minimumCardPickup(int[] cards) {
        int ans=Integer.MAX_VALUE;
        HashMap<Integer,Integer> hs=new HashMap<>();
        for(int i=0;i<cards.length;i++){
            int num=cards[i];
            if(hs.containsKey(num)){
                ans=Math.min(ans,i-hs.get(num)+1);
            }
            hs.put(num,i);
        }

        if(ans==Integer.MAX_VALUE){
            return -1;
        }
        return ans;
    }
}