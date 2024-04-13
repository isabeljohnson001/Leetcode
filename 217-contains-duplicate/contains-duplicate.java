class Solution {
    public boolean containsDuplicate(int[] nums) {
            HashMap<Integer,Integer> hs=new HashMap<>();
            for(int num:nums){
                if(hs.containsKey(num)){
                    return true;
                }
                hs.put(num,0);
            }
            return false;
        }
}