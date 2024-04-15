'''
https://leetcode.com/problems/remove-k-digits/?envType=daily-question&envId=2024-04-11

Can we create Monotonically increasing sequence out of the given number

Everytime there is chr[i]>chr[i+1], we can safely remove chr[i] as that would always ensure we get lower number rather than removing chr[i+1]
ex: 978, better to remove 9 instead of 7 

Use stack to keep track of numbers getting added. Always compare the top of stack with current number 

If we still need to remove more elements, then we can simply pop from end of the stack as remaining number would be in "INCREASING ORDER" as per our above condition i.e s[i] < s[i+1] 
Simply remove those many elements from the back 
'''

class Solution(object):
    def optimisedVersion(self, num, k):
        charStack   = []
        
        N = len(num)
        
        i = 0 
        while i < N:
            
            while charStack and k > 0 and int(charStack[-1]) > int(num[i]):
                charStack.pop()
                k-=1
            
            charStack.append(num[i])
            i+=1
            
        # if there are any further elements to be removed, remove them from the back of the array 
        while(charStack and k):
            charStack.pop()
            k-=1 
        
        if len(charStack) == 0:
            return "0"
        
        # remove leading zero ex: s= "0010"
        a_num = int("".join(charStack))
        return str(a_num)
        
        
    
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        
        arr = [i for i in num]
        toBeRemoved = []
        
        N = len(arr)
        removedCount = 0
        
        charStack = []
        i =0 
        while i < N:
            
            while charStack and int(charStack[-1]) > int(arr[i]) :
                charStack.pop()
                removedCount+=1
                if removedCount == k:
                    print("Current stack Element: ", charStack)
                    print("Current array elements ", arr[i:])
                    print("Elements to be returned",  )
                    print("Removed leading 0 zeros if any", int("".join(charStack + arr[i:])))
                    new_arr = charStack + arr[i:]
                    if len(new_arr) == 0 :
                        return "0"
                    return str(int("".join(new_arr)))
                
                print("CharStack", charStack)
                
            charStack.append(arr[i])
            i+=1 
            
        
        
        print("Number remaining",  charStack)
        # Now we need to removed last K-removedCount elements 
        
        M = k - removedCount
        print("M", M)
        N = len(charStack)
        if N==0:
            return "0"
        new_arr = charStack[:-M]
        if len(new_arr) == 0 :
            return "0"
        print("New Arr", new_arr)
        print("Leading zeros removed", int("".join(new_arr)))
        return str(int("".join(new_arr)))
                    
        
        # for i in range(N-1):
        #     if int(arr[i])>int(arr[i+1]):
        #         toBeRemoved.append(i)
        #         removedCount+=1
        #         arr[i]  =""
        #         i-=1
                
        #     if removedCount==k:
        #         num = int("".join(arr), 10 )
        #         print("Number returned", num)
        #         return str(num)
            
            
       
        # we need to removed some more from end now 
        
        # new_arr = "".join(arr)
        # arr = [i for i in new_arr]
        # N = len(arr)
        # for j in range(k-removedCount):
        #     arr[N-1-j] = ""

        # n = int("".join(arr), 10 )
        # print("n ", n)
        # return str(n)
            
            
        print("Remove")
            
            
obj = Solution()

num , k = "982", 1
num, k = "1432219", 3
num, k = "1432219", 5
num, k = "10200", 1
# num, k = "10", 2

print(obj.optimisedVersion(num, k))
        
        