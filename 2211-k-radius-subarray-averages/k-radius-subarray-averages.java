class Solution {
    public int[] getAverages(int[] nums, int k) {
        
        if(k==0){
            return nums;
        }
        int n=nums.length;
        int windowSize=2*k+1;
        int[] averages=new int[n];
        Arrays.fill(averages,-1);
        long[] prefix=new long[n+1];
        if(windowSize>n){
            return averages;

        }
            for(int i=0;i<n;i++){
                prefix[i+1]=prefix[i]+nums[i];
            }

            for(int i=k;i<(n-k);++i){
                int leftBound=i-k;
                int rightBound=i+k;
                long sum=prefix[rightBound+1]-prefix[leftBound];
                int average=(int)(sum/windowSize);
                averages[i]=average;
            }
            return averages;
        
    }
}