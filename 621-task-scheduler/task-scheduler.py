class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count task frequencies
        task_count = Counter(tasks)
        task_list = [-count for count in task_count.values()]  # Get task frequencies
        heapq.heapify(task_list)

        cooldown = deque()  # Cooldown queue
        t = 0  # Time counter

        while task_list or cooldown:
            # Move tasks from cooldown to task_list if ready
            t += 1
            if task_list:
                count=1+heapq.heappop(task_list)
                if count<0:
                    cooldown.append((count,t+n))
            if cooldown and cooldown[0][1]<=t:
                heapq.heappush(task_list,cooldown.popleft()[0])

        return t


        