// Last updated: 10/8/2025, 9:49:37 PM
class Solution {
    public int[] sortedSquares(int[] nums) {
        int n =nums.length;
        int[] result=new int[n];
        int left=0;
        int right=n-1;
        int square=0;
        for(int i=n-1;i>-1;i--){
            if(Math.abs(nums[left])>Math.abs(nums[right])){
                square=nums[left];
                left++;
            }
            else{
                square=nums[right];
                right--;
            }
            System.out.println(i);
            result[i]=square*square;
            
        }
        return result;
    }
}