class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        if len(nums)<=1:
            return nums
        i=0
        j=i+1
        while i<j and j<len(nums):
            if nums[i]==0 and nums[j]==0:
                j+=1
                continue
            if nums[i]==0:
                nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j+=1
        return nums