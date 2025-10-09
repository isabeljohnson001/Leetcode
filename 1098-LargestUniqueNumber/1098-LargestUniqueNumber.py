# Last updated: 10/8/2025, 9:49:25 PM
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        from collections import Counter
        
        
        
        count=Counter(nums)
        for num in sorted(count.keys(),reverse=True):
            if count[num]==1:
                return num
        return -1
            
        
        
        
            