# Last updated: 10/8/2025, 9:49:09 PM
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def check(k):
            sum=0
            for num in nums:
                sum=math.ceil(sum)
                sum+=num/k
            
            return sum<=threshold


        l=1
        r=10**6
        while l<=r:
            m=(l+r)//2

            if check(m):
                r=m-1
            else:
                l=m+1
        return l
        