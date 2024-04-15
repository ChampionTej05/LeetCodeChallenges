
'''
Take left part array with product 
Take right part array with product 
combine both 
'''
def arrayOfProducts(array):
    # Write your code here.
    if len(array)< 0:
        return [] 
    left = [1]*len(array)
    right = [1]*len(array)

    result = [1] * len(array)
    left[0]=array[0]
    for i in range(1, len(array)):
        left[i] = left[i-1] * array[i]

    print(left)

    right[-1] = array[-1]
    for i in range(len(array)-2, -1, -1):
        right[i] = right[i+1]* array[i]
    
    print(right)

    for i in range(len(array)):
        if i ==0 :
            result[i] = right[i+1]
        elif i== len(array)-1:
            result[i] = left[i-1]
        else:
            result[i] = right[i+1] * left[i-1]

    return result 

num = [1,2,3,4 ]
print(arrayOfProducts(num))

