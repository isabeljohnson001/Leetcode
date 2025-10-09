// Last updated: 10/8/2025, 9:51:15 PM
class Solution {
    public int missingNumber(int[] nums) {
     Set<Integer> hs=new HashSet<Integer>();
     for(int i=0;i<nums.length;i++){
         hs.add(nums[i]);
     }   

     for(int i=0;i<=nums.length;i++){
         if(!hs.contains(i)){
             return i;
         }}
         return -1;

     
    }
}