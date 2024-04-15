'''
In place sorting, we can use insertion - sort 



'''

def insertion_sort(arr):
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1 

        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-=1 

        arr[j+1] = key 

    
    # print(arr)
    return arr

arr = [5,4,3,2,1]
arr = [4,1,2,3,4,4,0,10,0]
print(insertion_sort(arr))