// Last updated: 10/8/2025, 9:49:06 PM
class Solution {
    public int minStartValue(int[] nums) {
        int startValue=1;
        int total=0;
        
        while(true){
            total=startValue;
            boolean isValid=true;
            for(int i=0;i<nums.length;i++){
                total+=nums[i];
                if(total<1){
                    isValid=false;
                    break;
                }
            }
            if(isValid){
                return startValue;
            }
            else{
                startValue=startValue+1;
            }
        }
    }
}