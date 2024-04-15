

class Sorts:

    def __init__(self, array):
        self.arr= array 

    
    def print_arr(self):
        print(self.arr)

    def bubble_sort(self):

        for i in range(len(self.arr)):
            # after each iteration, smallest element will be in place
            for j in range(i+1, len(self.arr)):
                if self.arr[i]>self.arr[j]:
                    self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    # each insertion ensures correct place for that element in array 
    def insertion_sort(self):

        for i in range(1, len(self.arr)):
            j = i-1 
            key = self.arr[i]

            while j>=0 and  key < self.arr[j]:
                self.arr[j+1] = self.arr[j]
                j-=1

            self.arr[j+1] = key 

         
    def merge_sort(self):

        arr_copy = self.arr.copy()
        self.merge_sort_helper(arr_copy) 
        self.arr = arr_copy

    def merge_sort_helper(self,arr):
        if len(arr) > 1:
            mid = len(arr)//2 

            left = arr[:mid]
            right = arr[mid:]

            #sorting the two halves
            self.merge_sort_helper(left)
            self.merge_sort_helper(right)

            self.merge(arr, left, right)

    
    def merge(self, arr, left, right):

        i , j , k = 0, 0, 0 

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i +=1 
            else:
                arr[k] = right[j]
                j+=1
            k+=1

        # put remaining elements 
            
        while i < len(left):
            arr[k] = left[i]
            i +=1 
            k+=1

        while j < len(right):
            arr[k] = right[j]
            j +=1 
            k+=1
    
        
        
        




        
    

arr  = [11,5,4,6,10,2,90]
sorts = Sorts(arr)
# sorts.bubble_sort()
# sorts.insertion_sort()
sorts.merge_sort()
sorts.print_arr()