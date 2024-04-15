'''
https://leetcode.com/problems/subsets/


'''

def generate_subsets(arr,index,path, result):
    result.append(path)
    for i in range(index, len(arr)):
        generate_subsets(arr, i+1, path+[arr[i]],result)


def generate(arr):
    result = set()
    N = len(arr)
    def generate_s(index, current_subset):
        if index == N:
            result.add(tuple(current_subset))
            return 
        
        #inclue element 
        current_subset.append(arr[index])
        generate_s(index+1, current_subset)
        
        #exclure element 
        current_subset.pop()
        generate_s(index+1, current_subset)
        
    generate(0, [])
    return [ list(i) for i in result]
        
        
def subsets_using_loop( nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    

    result=[[]]


    for num in nums:

        #tmpResult=result[:]
        newSubset=[]
        for item in result:
            newSubset.append(item +[num])
        
        result +=newSubset
        
    return result
        

def subsets(arr):

    result = []

    generate_subsets(arr, 0, [], result)
    print(result)


arr = [1,2,3]
subsets(arr)
