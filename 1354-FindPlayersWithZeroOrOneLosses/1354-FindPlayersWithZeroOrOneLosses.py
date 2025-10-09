# Last updated: 10/8/2025, 9:49:11 PM
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

        match_history=defaultdict(int)
        
        for win,loss in matches:
            
            match_history[loss]+=1
            if win not in match_history:
                match_history[win]=0
        
        wins=sorted([player for player,loss in match_history.items() if loss==0])
        win_1_match=sorted([player for player,loss in match_history.items() if loss==1])
        
        return [wins,win_1_match]