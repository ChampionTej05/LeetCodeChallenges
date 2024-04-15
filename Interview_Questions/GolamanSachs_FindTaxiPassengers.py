def max_passengers(matrix, n):
    # Initialize DP matrices for to-station and to-start paths
    to_station = [[0 for _ in range(n)] for _ in range(n)]
    to_start = [[0 for _ in range(n)] for _ in range(n)]

    # Check if a cell is valid for travel
    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < n and matrix[x][y] != -1

    # Populate the to_station matrix
    for i in range(n):
        for j in range(n):
            if not is_valid(i, j):
                continue
            to_station[i][j] = (matrix[i][j] == 1) + max(to_station[i-1][j] if i > 0 else 0,
                                                         to_station[i][j-1] if j > 0 else 0)
            # if matrix[i][j] == 1:
            #     matrix[i][j] = 0 

    print("ToStation: ", to_station)
    # Populate the to_start matrix
    for i in range(n-1, -1, -1):
        for j in range(n-1, -1, -1):
            if not is_valid(i, j):
                continue
            to_start[i][j] = (matrix[i][j] == 1 and to_station[i][j] == 0) + max(to_start[i+1][j] if i < n-1 else 0,
                                                                                  to_start[i][j+1] if j < n-1 else 0)
            # if matrix[i][j] == 1:
            #     matrix[i][j] = 0

    print("ToStart: ", to_start)

    # Total passengers are the sum at the end and start cells
    return to_station[n-1][n-1] + to_start[0][0]

def maxPassengers(grid):
    if not grid or grid[0][0] == -1 or grid[-1][-1] == -1:
        return 0
    
    n = len(grid)
    
    def dfs(x, y, passengers):
        if x == n - 1 and y == n - 1:
            return passengers
        
        max_passengers = passengers
        original_value = grid[x][y]
        
        if original_value == 1:
            passengers += 1
        
        grid[x][y] = -1  # Mark the cell as visited
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # Right, Down, Left, Up
        
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < n and 0 <= new_y < n and grid[new_x][new_y] >= 0:
                max_passengers = max(max_passengers, dfs(new_x, new_y, passengers))
        
        grid[x][y] = original_value  # Restore the original cell value
        return max_passengers
    
    result = dfs(0, 0, 0)
    return result

# # Example usage:
# grid = [[0, 1], [-1, 0]]
# print(maxPassengers(grid))  # Output: 1


# Example matrix
matrix = [
    [0, 1, -1],
    [0, 0, 1],
    [1, 0, 0]
]

# Calculate total passengers
n = len(matrix)
total_passengers = maxPassengers(matrix)
print(total_passengers)

