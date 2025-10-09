# Last updated: 10/8/2025, 9:49:35 PM
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left=0
        right=len(nums)-1
        ans=[]
        pos=-1
        while left<=right:
            
            if abs(nums[left])>abs(nums[right]):
                ans.append(nums[left]**2)
                left+=1
            else:
                ans.append(nums[right]**2)
                right-=1
        return ans[::-1]
                
        