'''
It could be translated into 2 sum problem, where we need to find closest value in array 
Conditions:
- Values must be +ve and -ve each 
- Sorted in order 
'''



#brute force 
def sweetAndSavory_BruteForce(dishes, target):
    # Write your code here.
    import sys
    
    #let us keep the sweet and savory dishes apart 

    sweetDishes  = [dish for dish in dishes if dish <0]
    savoryDishes = [dish for dish in dishes if dish >0 ]


    sweetDishes.sort(reverse=True)
    savoryDishes.sort()

    print(sweetDishes, savoryDishes)

    sweetIdx, savoryIdx = 0, 0 
    globalMinDiff = sys.maxsize
    bestPair  = [0,0]
    for d1 in sweetDishes:
        for d2 in savoryDishes:
            currentSum = d1 + d2
            localDiff = abs(target - currentSum )
            #no too savory
            if currentSum <= target:

                if localDiff ==0 :
                    bestPair = [d1, d2]
                    return bestPair 
                
                if localDiff < globalMinDiff:
                    globalMinDiff = localDiff
                    bestPair = [d1, d2]

    
    print("bestPair: {}".format(bestPair))
    return bestPair

   
def sweetAndSavory(dishes, target):

    sweetDishes  = [dish for dish in dishes if dish <0]
    savoryDishes = [dish for dish in dishes if dish >0 ]


    sweetDishes.sort(reverse=True)
    savoryDishes.sort()

    print(sweetDishes, savoryDishes)

    idx1, idx2 = 0 , 0 
    smallest_difference = float("inf")
    best_pair = [0,0]

    while idx1 < len(sweetDishes) and idx2 < len(savoryDishes):
        current_sum = sweetDishes[idx1] + savoryDishes[idx2]
        if current_sum <=target:

            difference = target-current_sum
            if difference < smallest_difference:
                smallest_difference = difference
                best_pair = [sweetDishes[idx1],savoryDishes[idx2] ]
            idx2 = idx2 +1
        else:
            idx1 = idx1+1

    print("bestPair: {}".format(best_pair))
    return best_pair

dishes = [-3,-5,1,7]
# dishes = [-3,-5,2,7]
# dishes = [5, -10]
# dishes = [2, 5, -4, -7,12,-25, 100]

target = 8
sweetAndSavory(dishes, target)