'''
https://leetcode.com/contest/biweekly-contest-126/problems/replace-question-marks-in-string-to-minimize-its-value/
'''
class Solution(object):
    def minimizeStringValue(self, s):
        """
        :type s: str
        :rtype: str
        
        
        We can keep values in place of ? in any order as the order won't increase or decrease the TOTAL cost 
        
        ex: s = 'a?bbx?c"  possible ? values are = d, e 
        if keep e first and d later, s = 'aebbxdc' , total cost = 0+0+0+1+0+0+0
        and same with d and e too 
        
        So we will sort the ? values and replace them by taking smallest first so that LEXICOGRAPHICALLY Shortest can be created 
        """
        
        freqMapper = [0 for _ in range(26)]

        # precomputation is needed
        # because if we compute on fly, then we might place worse element by just considering past count 
        # ex: s = 'a??b', we might place 'b' in place of first '?' if we don't pre compute all count 
        for i in range(len(s)):
            if s[i] != "?":
                freqMapper[ord(s[i])-ord('a')]+=1
        
        values_idx = []
        
        ans = [ch for ch in s]
        
        for idx, s in enumerate(s):
            
            if s != "?":
                continue
            else:    
                minCostPossible = float("inf")
                alphabet_choosen = 0
                
                #  can be done this way too 
                # for i in range(26):
                #     occurence_of_alphabet = freqMapper[i]
                #     currentCost = occurence_of_alphabet
                    
                #     if currentCost < minCostPossible:
                #         minCostPossible = currentCost 
                #         alphabet_choosen = i


                # find which letter has lowest frequency and having lowest index too 
                alphabet_choosen = freqMapper.index(min(freqMapper))
                freqMapper[alphabet_choosen]+=1 
                # ### Do not update yet, instead store which are possible ? values 
                # ans[idx] = chr(alphabet_choosen+ord('a'))
                values_idx.append((idx, chr(alphabet_choosen+ord('a'))))
                
        
        #  sort the question mark values , so that we can keep 'smaller value' at the front 
        values_idx_1 = sorted(values_idx, key = lambda x: x[1])
        print(values_idx_1)
        i = 0 
        # keep those smaller values at the front 
        for idx in range(len(ans)):
            if ans[idx] == "?":
                ans[idx] = values_idx_1[i][1]
                i+=1 

        return ''.join(ans)
                