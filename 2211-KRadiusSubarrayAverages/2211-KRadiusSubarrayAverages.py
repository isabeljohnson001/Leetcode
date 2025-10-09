# Last updated: 10/8/2025, 9:48:04 PM
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        
        n=len(nums)
        res=[-1]*n
        if 2*k+1>n:
            return res
        window_sum=sum(nums[:2*k+1])
        res[k]=window_sum//(2*k+1)
        for i in range(k+1,n-k):
            window_sum=window_sum-nums[i-k-1]+nums[i+k]
            res[i]=window_sum//(2*k+1)
        return res