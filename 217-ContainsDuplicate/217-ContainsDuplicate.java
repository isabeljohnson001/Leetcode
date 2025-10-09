// Last updated: 10/8/2025, 9:51:53 PM
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