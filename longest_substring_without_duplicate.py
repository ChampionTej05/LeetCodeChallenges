def lengthOfLongestSubstring( s):
        """
        :type s: str
        :rtype: int
        """

        mapper = {}

        
        maxSubstringLength = 0
        start = 0
        end = 0 

        interval = [start, end]

        while end < len(s):
            chr = s[end]
            if chr not in mapper:
                mapper[chr] = end
            else:
                #remove all values between s[start] .. s[duplicateCharacter]
                duplicateCharIdx = mapper[chr]
                idx = start 
                while idx <= duplicateCharIdx:
                    mapper.pop(s[idx])
                    idx+=1 

                #update the global maxium length 

                currentSubstringLength = end - start #not doing +1 for length because end is duplicate character, so ideally we would like to skip it 
                if currentSubstringLength >= maxSubstringLength :
                    maxSubstringLength = currentSubstringLength 
                    interval = [start, end]

                # set on non-duplicate char idx
                start = idx 

                mapper[chr] = end
            end+=1 

        
        #after complete traversal 
        currentSubstringLength = end - start 
        if currentSubstringLength >= maxSubstringLength :
            maxSubstringLength = currentSubstringLength 
            interval = [start, end]

        
        print(interval)
        return maxSubstringLength