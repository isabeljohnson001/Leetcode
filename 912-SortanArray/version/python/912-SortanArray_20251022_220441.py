# Last updated: 10/22/2025, 10:04:41 PM
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        n=len(nums)
        if n<=1:
            return nums
        
        mid=n//2
        left=nums[0:mid]
        right=nums[mid:n]
        left=self.sortArray(left)
        right=self.sortArray(right)
        return self.merge(left,right)
        
    
    def merge(self,left,right):

        nl=len(left)
        nr=len(right)
        i,j=0,0
        merged=[]
        while i<nl and j<nr:
            if left[i]<=right[j]:
                merged.append(left[i])
                i=i+1
            else:
                merged.append(right[j])
                j=j+1
        merged.extend(left[i:nl])
        merged.extend(right[j:nr])
        return merged



    

    