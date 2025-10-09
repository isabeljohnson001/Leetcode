# Last updated: 10/8/2025, 9:49:57 PM
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums)%k!=0:
            return False

        nums.sort(reverse=True)
        target=sum(nums)//k
        if nums[0]>target:
            return False
        used=[False]*len(nums)
        def backtrack(start,k,currSum):
            if k==0:
                return True
            if currSum==target:
                return backtrack(0,k-1,0)
            prev=-1
            for j in range(start,len(nums)):

                x=nums[j]
                if used[j] or currSum+x>target or prev==x:
                    continue
                currSum+=x
                used[j]=True
                if backtrack(j+1,k,currSum):
                    return True
                currSum-=x
                used[j]=False
                prev=x
            return False
        return backtrack(0,k,0)
                




