# Last updated: 10/8/2025, 9:47:47 PM
class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:

        players.sort()
        trainers.sort()
        i=0
        j=0
        match=0
        while i<len(players) and j<len(trainers):

            if players[i]<=trainers[j]:
                i+=1
                j+=1
                match+=1
            else:
                j+=1
        return match
        