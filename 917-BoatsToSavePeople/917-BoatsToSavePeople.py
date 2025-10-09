# Last updated: 10/8/2025, 9:49:41 PM
class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()

        i=0
        j=len(people)-1
        ans=0
        while(i<=j):
            if people[i]+people[j]<=limit:
                i+=1
            j-=1
            ans+=1
        return ans
        