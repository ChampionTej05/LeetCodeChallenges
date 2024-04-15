'''
https://leetcode.com/problems/rotting-oranges/ 

It is again version of BFS where we need check the calls made to BFS to ensure all of them are rotten 


We need to find out how many levels would be in BFS in simplicity 

1. Find count of fresh oranges (will be used to decide whether we were able to rotten all or not)
2. Find all rotten oranges and store them in Queue 
3. Use level order now 
    a. pull all nodes from current queue and start putting their fresh neighbours in queue 
    b. Increment level by 1 , if there are any neighbours added in step 3-a
    c. Repeat it for nodes in queue 
'''


EMPTY = 0 
FRESH = 1 
ROTTEN = 2

def mark_rotten(grid, i, j, queue, fresh_oranges):
    rows = len(grid)
    cols = len(grid[0])
    if 0<=i<rows and 0<=j<cols:
        if grid[i][j] == FRESH:
            grid[i][j] = ROTTEN
            fresh_oranges -=1
            queue.append((i, j))

    return queue, fresh_oranges

def BFS(grid):
    
    from collections import deque

    queue = deque()
    # collect all rotten oranges and fresh oranges 
    fresh_oranges = 0 
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == FRESH:
                fresh_oranges +=1 
            elif grid[i][j] == ROTTEN:
                queue.append((i,j))


    # print(queue)
    # run BFS now 
    if queue:
        minute  = 0 
        while queue:
            minute +=1
            # print("Queue: ", queue)
            # print("Minute: ", minute)
            #collect all nodes in the queue 

            nodes = []
            
            while queue:
                nodes.append(queue.popleft())
            
            # print('Nodes: ', nodes)
            for node in nodes:
                i, j  = node
                
                #adjacent rotten 
                queue, fresh_oranges = mark_rotten(grid, i, j-1, queue, fresh_oranges)
                queue, fresh_oranges = mark_rotten(grid, i, j+1, queue, fresh_oranges)
                queue, fresh_oranges = mark_rotten(grid, i-1, j, queue, fresh_oranges)
                queue, fresh_oranges = mark_rotten(grid, i+1, j, queue, fresh_oranges)
        
        if fresh_oranges ==0:
            return minute -1 
        else:
            return -1
        
    else:
        if fresh_oranges ==0 :
            #no fresh orange in queue, no rotten orange 
            return 0 
        else:
            # fresh orange but no rotten orange 
            return -1  
    
def orangeRotten(grid):
    from collections import deque

    queue = deque()
    fresh_oranges = 0
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == FRESH:
                fresh_oranges += 1
            elif grid[i][j] == ROTTEN:
                queue.append((i, j))

    minute = 0
    while queue and fresh_oranges > 0:
        #processing only those nodes which are in current queue and not all 
        nodes_to_process = len(queue)
        for _ in range(nodes_to_process):
            i, j = queue.popleft()

            for x, y in [(i, j-1), (i, j+1), (i-1, j), (i+1, j)]:
                if 0 <= x < rows and 0 <= y < cols and grid[x][y] == FRESH:
                    grid[x][y] = ROTTEN
                    fresh_oranges -= 1
                    queue.append((x, y))
        
        minute += 1

    return minute if fresh_oranges == 0 else -1

# grid = [[2,1,1],[1,1,0],[0,1,1]] #4 

# grid = [[2,1,1],[0,1,1],[1,0,1]] 
grid = [
    [2, 1, 1],
    [1, 2, 1],
    [1, 1, 2]
]


print(orangeRotten(grid ))

