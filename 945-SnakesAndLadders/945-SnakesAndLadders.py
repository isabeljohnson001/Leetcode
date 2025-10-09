# Last updated: 10/8/2025, 9:49:37 PM
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        n=len(board)
        visited=set()
        start,end=1,n*n
        def findCoordiates(cur_position):
            row=n-1 -(cur_position-1)//n
            col=(cur_position-1)%n
            if row%2==n%2:
                return (row,n-1-col)
            else:
                return (row,col)



        queue=collections.deque()
        queue.append((1,0))
        while queue:

            curr_pos, steps=queue.popleft()
            if curr_pos==end:
                return steps
            
            for dice in range(1,7):
                #find corrdinates
                if curr_pos+dice>end:
                    break
                next_row,next_col=findCoordiates(curr_pos+dice)
                if (next_row,next_col) not in visited:
                    visited.add((next_row,next_col))
                    if board[next_row][next_col]!=-1:
                        queue.append((board[next_row][next_col],steps+1))
                    else:
                        queue.append((curr_pos+dice,steps+1))
        return -1