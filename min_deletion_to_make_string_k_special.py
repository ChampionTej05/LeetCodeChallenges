'''
https://leetcode.com/contest/weekly-contest-389/problems/minimum-deletions-to-make-string-k-special/


Convert the string into frequency mapper and then sort the mapper.values()

Now our question is : whether can we reduce all values in array somehow such that , all<=k for each other 

We will try this for each array interger and find out min moves required for each of them and then global min 

1. for i , j = i+1, find elements not in range. moves += abs(arr[j]-arr[i])-k : reductions needed to reduce the max element to lie within range 
2. This is sufficient to find for each element j , for given i 
3. Now when we move forward, how can we gurantee that all pairs will satisfy condition 
4. We simply take the sum of all previous count and add it in current move: This means that if we remove all the previous elements and 
    just consider array for j=i+1-->N and find minDeletions there, then we can get how many moves would be required for current I 

OR 

we delete all those previous chars frequency which have values less than current arr[i]
By this , we can simply omit all of them, and look for further reductions

'''

class Solution(object):


    def minimumDeletions(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """ 
        from collections import defaultdict
        
        mapper = defaultdict(int)
        
        
        for chr in word:
            mapper[chr]+=1 
            
        arr = list(mapper.values())
        N = len(arr)
        
        
        arr.sort()
        print("Arr", arr)
        
        # need to find min operation to make this k-special 
        globalMinMoves = float("inf")
        for i in range(N):
            localMinMoves = 0
            targetMin = arr[i]-k
            targetMax = arr[i]+k
            for j in range(i+1, N):
                
                # if targetMin <= arr[j] <= targetMax:
                #     continue
                # else:
                #     moves = abs(arr[j]-targetMin) if targetMin<arr[j] else arr[j]
                #     localMinMoves+= moves 
                if abs(arr[i]-arr[j])>k:
                    moves = abs(arr[i]-arr[j]) -k 
                    localMinMoves+= moves
                    # arr[j] = arr[j]-moves
            # since we left all values before current i, we will consider them in skip moves only 
            # ex: [1,2,4] , when on 2, we consider sum([1]) , when on 4, we consider sum([1,2]) as we are checking for which value 
            # all pairs in the array satisifies 
            localMinMoves += sum(arr[:i])
            print("Moves for i :{}, moves :{}".format(arr[i], localMinMoves))
            globalMinMoves = min(localMinMoves,  globalMinMoves)
            
        return globalMinMoves
    

obj = Solution()

word = "dabdcbdcdcd"
word = "aaabaaa"

k = 2

# word  = "aabcaba"
# k = 0

print(obj.minimumDeletions(word, k))