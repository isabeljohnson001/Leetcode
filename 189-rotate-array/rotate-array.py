class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        res=[0]*n
        startIndex=k

        for i in range(n):
                startIndex=(i+k)%n
                res[startIndex]=nums[i]
        nums[:]=res
        return nums


            
        