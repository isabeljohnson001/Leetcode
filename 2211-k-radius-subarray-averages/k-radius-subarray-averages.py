class Solution(object):
    def getAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if(k==0):
            return nums
        n=len(nums);
        windowSize=2*k+1;
        averages=[]
        for i in range(0,n):
            averages.append(-1)
        #averages=[-1]*n
        prefix=[]
        if(windowSize>n):
            return averages
        prefix=[0] * (n + 1)
        for i in range(0,n):
            prefix[i+1]=prefix[i]+nums[i]
        for i in range(k,n-k):
            leftBound=i-k
            rightBound=i+k
            sum=prefix[rightBound+1]-prefix[leftBound]
            average=sum/windowSize
            averages[i]=average
        return averages