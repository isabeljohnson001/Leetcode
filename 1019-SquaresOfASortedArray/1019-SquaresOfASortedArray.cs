// Last updated: 10/8/2025, 9:49:38 PM
public class Solution {
    public int[] SortedSquares(int[] nums) {
            int right = nums.Length-1;
            while (right>-1)
            {
                int left = 0;
                while (left < right)
                {
                    if (Math.Abs(nums[left]) > Math.Abs(nums[right]))
                    {
                        int temp=nums[left];
                        nums[left] = nums[right];
                        nums[right] = temp;
                    }
                    left++;
                    
                }
                nums[right] = nums[right] * nums[right];
                right--;
            }
            return nums;
    }
}