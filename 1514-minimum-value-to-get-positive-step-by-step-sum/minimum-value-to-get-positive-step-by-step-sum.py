class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        startValue=1
        while(True):
            total=startValue;
            isValid=True
            for i in range(0,len(nums)):
                total+=nums[i]
                if(total<1):
                    isValid=False
                    break
            if(isValid):
                return startValue
            else:
                startValue=startValue+1

        