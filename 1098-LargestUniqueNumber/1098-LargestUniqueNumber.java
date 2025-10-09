// Last updated: 10/8/2025, 9:49:28 PM
class Solution {
    public int largestUniqueNumber(int[] nums) {
        
        //Create hashmap
        HashMap<Integer,Integer> hs=new HashMap<Integer,Integer>();
        for (int num : nums){
            hs.put(num,hs.getOrDefault(num,0)+1);
        }
        int result=-1;
        for(Map.Entry<Integer,Integer> number : hs.entrySet()){
            if(number.getValue()==1){
                result=Math.max(result,number.getKey());
            }
        }
        return result;
        }
    }