# Last updated: 10/8/2025, 9:49:53 PM
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        def neighbours(node):
            ans=[]
            
            for i in range(4):
                num=int(node[i])
                for change in [-1,1]:
                    x=(num+change)%10
                    ans.append(node[:i]+str(x)+node[i+1:])
            return ans


        if "0000" in deadends:
            return -1

        visited=set(deadends)
        visited.add(("0000"))

        queue=collections.deque()
        queue.append(("0000",0))
        while queue:
            current_node,steps=queue.popleft()
            if current_node==target:
                return steps
            for neighbour in neighbours(current_node):
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append((neighbour,steps+1))
        return -1