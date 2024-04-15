'''
https://leetcode.com/contest/weekly-contest-381/problems/minimum-number-of-pushes-to-type-word-ii/

1. Find the value needed to press the key for each letter, value = (index//8+1)
2. Answer = sum (counter(letter)*value[letter])
'''


class Solution:
    def minimumPushes(self, word: str) -> int:
        N = len(word)
        from collections import Counter 

        cnt = Counter(word)

        print("Counter : {}".format(cnt))

        index = 0
        sorted_counter = sorted(cnt.items(),key = lambda x: x[1], reverse=True)
        print("Sorted Counter", sorted_counter)
        # keys = sorted_counter.keys()
        keys = [ key for key, _ in sorted_counter]
        print("Keys", keys)
        mapper = {} 
        for key in keys:
            if key not in mapper:
                mapper[key] = (index//8)+1 
                index+=1
            
        print("Mapper: {}".format(mapper))
        pushes = 0
        for key, value in cnt.items():
            pushes += (value*mapper[key])
        
        return pushes
    

word = "xyz"*4 
word = "aabbccddeeffgghhiiiiii"
# word = "abzaqsqcyrbzsrvamylmyxdjl"

print(word)

obj = Solution()
print(obj.minimumPushes(word))
        
        
