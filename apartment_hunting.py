'''
https://www.algoexpert.io/questions/apartment-hunting
'''
# Brute Force 

# Brute Force
def apartmentHunting(blocks, reqs):
    # Write your code here.
    import sys
    max_distance = len(blocks)
    optimal_distance = len(blocks)
    result_idx = -1

    for i in range(len(blocks)):
        requirements = [max_distance for _ in range(len(reqs))]

        for j in range(len(blocks)):
            for k in range(len(reqs)):
                key = reqs[k]
                if blocks[j][key]:
                    requirements[k] = min(requirements[k], abs(j-i))

        print("Requirements : {} at i {}".format(requirements, i))
        # compute optimal distance 
        
        if max(requirements) <= optimal_distance:
            optimal_distance = max(requirements)
            result_idx = i 

    return result_idx

        
    
        
        
