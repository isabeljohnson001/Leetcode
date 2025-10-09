// Last updated: 10/8/2025, 9:49:34 PM
class Solution {
    public int longestOnes(int[] nums, int k) {
        
        
        int left=0;
        int right=0;
        int curr=0;
        int ans=0;
        for(right=0;right<nums.length;right++){
            if(nums[right]==0)
                curr++;
            while(curr>k){
                if(nums[left]==0)
                    curr--;
                left++;
            }
            ans=Math.max(ans,right-left+1);
        }
        return ans;
    }
}