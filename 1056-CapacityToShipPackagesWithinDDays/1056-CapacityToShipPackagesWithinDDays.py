# Last updated: 10/8/2025, 9:49:26 PM
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def daysNeeds(weight_for_one_day):
            d=1
            curr_w=0
            for w in weights:
                if curr_w+w>weight_for_one_day:
                    d+=1
                    curr_w=0
                curr_w+=w
            return d

        l=max(weights)
        r=sum(weights)

        while l<r:
            #compute the possible weights
            m=(l+r)//2

            if daysNeeds(m)<=days:
                r=m
            else:
                l=m+1
        return r


        