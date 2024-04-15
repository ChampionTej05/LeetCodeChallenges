'''
leetcode: https://leetcode.com/problems/flood-fill/description/

Idea:
Mark all pixels which needs to be colored as "negative 1" (as color is always positive)
We need to be recursively or iteratively find pixels which needs to be colored and marked
Do one more pass and mark all those with "color" value


helper(m,n,sr, sc, color):
    arr[sr][sc] = -1

    if sr+1<m and sc < n and arr[sr+1][sc] == color:
        helper(m,n,sr+1, sc, color)
    if sr-1< m and sc < n and arr[sr-1][sc] == color:
        helper(m,n,sr-1,sc,color)
    if sr < m and sc+1 < n and arr[sr][sc+1] == color :
        helper(m,n,sr,sc+1,color)
    if sr < m and sc-1 < n and arr[sr][sc-1] == color:
        helper(m,n,sr,sc-1,color)
    
    

algo(m,n,sr,sc):
    color= arr[sr][sc]
    helper(m,n,sr,sc,color)

    #mark all elements in arr with negative 1 value with color 
    for i in m:
        for j in n:
            if arr[i][j]==-1:
                arr[i][j]=color 



'''


def helper(image, sr, sc, start_color):
    m = len(image)
    n = len(image[0])
    
    image[sr][sc] = -1
 
    if -1<sr+1<m and -1<sc < n and image[sr+1][sc] == start_color:
        helper(image,sr+1, sc, start_color)
    if -1<sr-1< m and -1<sc < n and image[sr-1][sc] == start_color:
        helper(image,sr-1,sc,start_color)
    if -1<sr < m and -1<sc+1 < n and image[sr][sc+1] == start_color :
        helper(image,sr,sc+1,start_color)
    if -1<sr < m and -1<sc-1 < n and image[sr][sc-1] == start_color:
        helper(image,sr,sc-1,start_color)
    
    


def flood_fill(image, sr, sc, color):

    start_color = image[sr][sc]
    helper(image,sr, sc, start_color)

    for i in range(len(image)):
        for j in range(len(image[0])):
            if image[i][j] == -1:
                image[i][j]= color 

    return image 

image = [[1,1,1],[1,1,0],[1,0,1], [1,0,0], [1,1,1],[1,0,1]]
sr = 1
sc = 1
color = 2

flood_fill(image,sr,sc,2)

print(image)
print(len(image))
print(len(image[0]))