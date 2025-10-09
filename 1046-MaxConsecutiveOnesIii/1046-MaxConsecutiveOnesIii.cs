// Last updated: 10/8/2025, 9:49:36 PM
public class Solution {
    public int LongestOnes(int[] nums, int k) {
        
        /*Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
        Output: 6
        Explanation: [1,1,1,0,0,1,1,1,1,1,1]
        r=5,l=0,curr=3,count=6
        r=5,curr=2,l=1,count=5
        r=10,l=2
        r=11,l=2,curr=2, count=8
        
        */
            int left = 0;
            int count = 0;
            int curr = 0;
            int ans = 0;
            int right = 0;
            for (right = 0; right < nums.Length; right++)
            {

                if (nums[right] == 0)
                {
                    curr++;

                }
                while (curr > k)
                {
                    if (nums[left] == 0)
                        curr--;
                    left++;

                }
                ans = Math.Max(ans, right - left + 1);
            }
            
            return ans;
        
    }
}