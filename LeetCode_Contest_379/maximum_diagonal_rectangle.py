'''
https://leetcode.com/contest/weekly-contest-379/problems/maximum-area-of-longest-diagonal-rectangle/
'''

def maximumDiagonalRectangle(dimmensions:list[list[int]]):


    if len(dimmensions)==1:
        return dimmensions[0][0] * dimmensions[0][1]
    import math
    # comparing squares is simple than sqrt as a,b>0
    maxDiagonal = dimmensions[0][0]**2 + dimmensions[0][1]**2
    maxArea = dimmensions[0][1] * dimmensions[0][0]

    # print("maxDiagonal {}".format(maxDiagonal))
    # print("maxArea: {}".format(maxArea))

    for i in range(1, len(dimmensions)):
        diagonal = dimmensions[i][0]**2 + dimmensions[i][1]**2
        area  = dimmensions[i][0]*dimmensions[i][1]
        if diagonal > maxDiagonal:
            maxDiagonal = diagonal 
            maxArea = area
        elif diagonal == maxDiagonal and area > maxArea:
            maxArea = area 
            maxDiagonal = diagonal

    return maxArea
             

dimensions = [[10,3],[5,9],[8,3]]
print(maximumDiagonalRectangle(dimensions))