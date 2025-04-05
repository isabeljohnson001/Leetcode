class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        mid=0
        left=0
        right=len(nums)-1   
        while(left<=right):
            mid=(left+right)/2
            num=nums[mid]
            if(num==target):
                return mid
            if target<num:
                right=mid-1
            if target>num:
                left=mid+1
        return -1