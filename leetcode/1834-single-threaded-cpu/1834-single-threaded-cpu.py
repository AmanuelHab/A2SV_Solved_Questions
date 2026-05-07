class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        time = 0
        ready_queue = []
        answer = []
        tasks_table = []
        for i in range(len(tasks)):
            tasks_table.append((tasks[i][0], tasks[i][1], i))
        tasks_table.sort(reverse=True) # Reverse sort to optimize the removal of tasks

        while True:
            if not tasks_table and not ready_queue: # If all tasks are done
                break
            while tasks_table and tasks_table[-1][0] <= time: # Add tasks to ready queue
                e, p, i = tasks_table.pop()
                heappush(ready_queue, (p, i))
            if ready_queue: # Implement a task if there is one in ready_queue
                p, i = heappop(ready_queue)
                time += p
                answer.append(i)
            else:
                # Fast forward to the next task
                time += tasks_table[-1][0] - time

        return answer