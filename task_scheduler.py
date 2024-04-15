'''
https://leetcode.com/problems/task-scheduler/

Algorithm Steps:

Count the frequency of each task.
Use a max heap to store tasks based on their frequency.
On each iteration (or unit of time), select the most frequent task that is not on cooldown and execute it.
If no task is available (due to cooldown), the CPU is idle.
Keep a cooldown tracker to know when a task is available again.


'''

def leastInterval(tasks,n):
    if n == 0:
        return len(tasks) # no idle period between tasks 
    
    from collections import Counter
    import heapq
    cooldown_mapper = {} #tracks at till what time CPU is IDLE 
    counter = Counter(tasks)

    max_heap = []
    for value in counter.values():
        #negative values
        max_heap.append(-value)

    #create max heap for highest frequency tasks 
    heapq.heapify(max_heap)

    time = 0 
    print("Max Heap at the start , max_heap :{}".format(max_heap))
    # run this till either there is tasks waiting CPU or Tasks left in the processing
    while max_heap or cooldown_mapper:
        time +=1
        

        if time in cooldown_mapper:
            #at this time, some task was suppose to be scheduled which is waiting for CPU 
            count = cooldown_mapper.pop(time)
            # add item on the heap again
            heapq.heappush(max_heap, count)

        if max_heap:
            current_task_count = heapq.heappop(max_heap)
            current_task_count = current_task_count + 1 # since the count is negative, adding 1, will reduce its value 

            if current_task_count != 0:
                # CPU would be needed for this task 
                next_time_task_requires_cpu = time + n + 1 # extra since we are counting that second
                cooldown_mapper[next_time_task_requires_cpu] = current_task_count
        # print("time: {}, cooldown : {}, max_heap  : {}".format(time, cooldown_mapper, max_heap))
    # print("time elapased: {}".format(time))     
    return time



def mathematicalSolution(tasks, cooling_period):
    '''
    Read this: https://medium.com/@satyem77/task-scheduler-leetcode-39d579f3440
    '''
    from collections import Counter 
    N = len(tasks)
    maxFrequencyTasks = 0

    taskCounter = Counter(tasks) 
    mostCommonTasks = taskCounter.most_common()

    # this gives (task, frequency)
    maxFrequency = mostCommonTasks[0][1]

    # find tasks with this frequency 
    for task, frequency in taskCounter.items():
        if frequency==maxFrequency:
            maxFrequencyTasks+=1 

    print("Total max Frequency Tasks = ", maxFrequencyTasks)
    A = (cooling_period+1)*(maxFrequency-1) + maxFrequencyTasks
    B = N

    print(A)
    print(B)

    return max(A,B)

# Incorrect Solution yet
def revisionSolution(tasks, cooling_period):
    from collections import Counter, deque
    import heapq
    N = len(tasks)

    max_heap = []
    task_queue = deque()
    # tuple : (next_time_task_available, task_name, task_count_left)
    
    
    time = 0 
    
    # initialise min_heap 
    cnt = Counter(tasks)
    for k, v in cnt.items():
        # frequency , task_name
        max_heap.append( ( -v, k))
    
    heapq.heapify(max_heap)
    print("Current Max Heap ", max_heap)
    
    
    while max_heap or task_queue:
        time+=1 
        
        # all tasks which can be executed at time = current time, we will push it on queue to be executed based on their frequency count 
        while task_queue and task_queue[0][2] == time:
            task = task_queue.popleft()
            heapq.heappush(max_heap, (task[0], task[1]))
            
            
        
        # pop the task which can be performed at this time from heap 
        if max_heap:
            task_freq, task_name  = heapq.heappop(max_heap)
            
            # perform this task 
            
            task_freq+=1 # since value is negative, we increase it
            
            if task_freq !=0:
                # put this on queue to be executed in the future 
                next_time_this_task_would_be_available = time + cooling_period + 1
                # if time = 2, N =2 , then task can be executed at time = 5
                task_queue.append( ( task_freq, task_name,  next_time_this_task_would_be_available ))
                
        print("Time = {}, queue = {}, heap : {}".format(time, task_queue, max_heap))
            
            
    print("Time : ", time)
    return time 
    


def chatGPTSolution():
    '''
    Code Explanation Aligned with Grid Logic:
    Count the Frequency of Each Task:
    Use Python's Counter to count occurrences of each task.
    Identify the Most Frequent Task and Its Frequency:
    Find the maximum frequency among tasks. For 'A', it's 4.
    Calculate the Grid Dimensions:
    Rows in the grid: max_count - 1, where max_count is the frequency of the most frequent task.
    Columns in the grid: n + 1 (the cooldown period plus one slot for the task).
    Calculate the Total Number of Slots:
    This is given by rows times columns.
    Place the Most Frequent Task and Calculate Idle Slots:
    Initially, all slots except the ones occupied by 'A' are considered idle.
    Fill Idle Slots with Other Tasks and Adjust Idle Count:
    Deduct the count of other tasks from the idle slots. This simulates placing other tasks in the grid.
    Handle Remaining Idle Slots:
    If there are still idle slots left after placing all tasks, these slots represent idle times.
    Calculate the Total Time:
    Add up the number of tasks and the remaining idle slots.
    '''

    from collections import Counter

    def leastInterval(tasks, n):
        task_counts = Counter(tasks)
        max_count = max(task_counts.values())  # Frequency of the most frequent task
        max_count_tasks = sum(count == max_count for count in task_counts.values())  # Number of tasks with max frequency

        part_count = max_count - 1  # Number of parts (rows in the grid)
        part_length = n - (max_count_tasks - 1)  # Length of each part (columns in the grid)
        empty_slots = part_count * part_length  # Total empty slots in the grid
        available_tasks = len(tasks) - max_count * max_count_tasks  # Tasks that can fill the empty slots
        idles = max(0, empty_slots - available_tasks)  # Remaining idle slots after placing other tasks

        return len(tasks) + idles  # Total time is sum of all tasks and idle slots

    # Example usage
    tasks = ["A", "A", "A", "A", "B", "B", "B"]
    n = 3
    print(leastInterval(tasks, n))  # Output: 13


tasks = ["A","A","A","A","B", "B","B"]
n = 3

tasks = ["A"] * 3 + ["B"] * 3 + ["C"] + ["D"]*2 
n = 2

tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 1

tasks = ["B","F","J","J","H","A","D","C","C","D","J","E","B","E","C","H","E","E","G","E","H","I","I","E","H","F","C","G","H","F","E","E","I","D","D","A"]
n = 5


# tasks = ["B","F","J","J","E","E","I","D","D","A"]
# n = 5

revisionSolution(tasks, n)
print("Maths solution", mathematicalSolution(tasks, n))
