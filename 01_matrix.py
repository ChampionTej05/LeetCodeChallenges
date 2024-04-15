'''
leetcode: https://leetcode.com/problems/01-matrix/

Brute force won't work 
We can use backtracking or DP mechanism here 

dist[i,j] = 0 if arr[i,j] ==0 else min(dist[i-1, j] , dist[i, j-1], dist[i][j+1], dist[i+1][j]) + 1 

Above equation won't handle all cases, example when boundary elements are 1, so we won't be able to find optimal distance 

So let us do two pass DP solution to find the optimal distance 
Dist = Infinity for all except where mat[i][j] = 0

1. TopLeft - bottom right : dist[i][j] = min(dist[i][j], min(dist[i-1][j], dist[i][j-1]) + 1) if arr[i][j] != 0
2. Bottom right - top left : dist[i][j] = min(dist[i][j], min(dist[i+1][j], dist[i][j+1]) + 1) 

'''




def build_dist_matrix(mat):

    rows = len(mat)
    cols = len(mat[0])

    dist = [ [ float('inf') ] * cols for _ in range(rows)]

    # first pass to build up the solution 

    # top left (i,j-1), (i-1,j)

    for i in range(rows):
        for j in range(cols):
            if mat[i][j]==0:
                dist[i][j]=0
            else:
                # build matrix 
                if i>0 and j>0:
                    dist[i][j] = min(dist[i][j], min(dist[i-1][j], dist[i][j-1]) + 1 )
                elif i > 0:
                    dist[i][j] = min(dist[i][j], dist[i-1][j]+1)
                elif j > 0:
                    dist[i][j] = min(dist[i][j], dist[i][j-1]+1)

    
    # print(dist)

    #second pass 

    # bottom right (i,j+1) , (i+1, j)

    for i in reversed(range(rows)):
        for j in reversed(range(cols)):
            if i < rows-1 and j < cols-1:
                dist[i][j]  = min(dist[i][j], min(dist[i][j+1], dist[i+1][j])+1)
            elif i < rows-1:
                dist[i][j] = min(dist[i][j], dist[i+1][j]+1)
            elif j < cols-1:
                dist[i][j] = min(dist[i][j], dist[i][j+1]+1)

    print(dist)
    return dist



# rows = 2
# cols = 5
# matrix = [[column for column in range(cols)] for row in range(rows)]
# create_dp(matrix)
mat = [[1,1,0],[0,1,0],[1,1,1]]
build_dist_matrix(mat)