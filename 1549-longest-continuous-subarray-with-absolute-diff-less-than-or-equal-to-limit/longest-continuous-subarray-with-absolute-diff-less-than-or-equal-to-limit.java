class Solution {
    public int longestSubarray(int[] nums, int limit) {
        Deque<Integer> increase=new ArrayDeque<>();
    Deque<Integer> decrease=new ArrayDeque<>();
    int ans=0;
    int left=0;
    //[8,2,4,7] k=4
    for(int right=0;right<nums.length;right++) {
        while (!increase.isEmpty() && increase.getLast() > nums[right]) {
            increase.removeLast();
        }
        while (!decrease.isEmpty() && decrease.getLast() < nums[right]) {
            decrease.removeLast();
        }
        increase.addLast(nums[right]);
        decrease.addLast(nums[right]);

        while (decrease.getFirst()-increase.getFirst()>limit)
        {
            if(increase.getFirst()==nums[left]){
                increase.removeFirst();
            }
            if(decrease.getFirst()==nums[left]){
                decrease.removeFirst();
            }
            left++;
        }
        ans=Math.max(ans,right-left+1);
        }
    return ans;
    }
}