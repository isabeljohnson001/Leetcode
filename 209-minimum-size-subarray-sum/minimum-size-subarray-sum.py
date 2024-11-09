class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans=float("inf")
        curr=0
        left=0
        for right in range(len(nums)):
            curr+=nums[right]
            print(str(nums[right])+"-"+str(curr))
            while(curr>=target):
                ans=min(ans,(right-left)+1)
                curr-=nums[left]
                print(curr)
                left+=1
                
        return ans if ans != float("inf") else 0

        