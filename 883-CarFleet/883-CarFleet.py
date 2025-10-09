# Last updated: 10/8/2025, 9:49:45 PM
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        #hint - in this question....we have combined two arrays using zip and srted and taken in revere..we look at first car close to target..and comapre it with 2ndlast..compute the time it takes to reach the target..if 2nd last taakes lessaer time than the last one..then there ill be a car feelt...so we remove the lesser one after...and end we retrun the len of sthe stack
        pairs=[[p,s] for p,s in zip(position,speed)]

        stack=[]
        for p,s in sorted(pairs)[::-1]:
            stack.append((target-p)/s)
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)
        