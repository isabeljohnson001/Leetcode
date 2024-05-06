class Solution(object):
    def answerQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        nums.sort()
        ans=[]
        
        for query in queries:
            count=0
            for num in nums:
                if query>=num:
                    query-=num
                    count+=1
                else:
                    break
            ans.append(count)
        return ans