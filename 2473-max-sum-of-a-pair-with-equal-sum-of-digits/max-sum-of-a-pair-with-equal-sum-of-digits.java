class Solution {
    public int maximumSum(int[] nums) {
         int ans = -1;
        HashMap<Integer, Integer> hs = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int sum = digitSum(nums[i]);
            if (hs.containsKey(sum)) {
                ans=Math.max(ans,nums[i]+hs.get(sum));
            }
            hs.put(sum,Math.max(hs.getOrDefault(sum,0),nums[i]));
        }
        return ans;

    }

    public int digitSum(int num){
        int sum=0;
        while(num>0){
        sum+=num%10;
        num=num/10;}
        return sum;
    }
}