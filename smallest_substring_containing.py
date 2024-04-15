

'''
We will first try to find the substring which contains all characters of smallString 
and then try to find smallest one 
'''
def substringContaining(bigString, smallString):
    # Write your code here.
    from collections import Counter

    mapper = {}
    for chr in smallString:
        if chr in mapper:
            mapper[chr] = mapper[chr] +1 
        else:
            mapper[chr] = 1 

    print("Mapper small string", mapper)
    startIdx = -1
    endIdx = -1
    for idx, chr in enumerate(bigString):
        if chr in mapper :

            #found first matching character?
            if startIdx == -1:
                startIdx = idx 
            

            mapper[chr] = mapper[chr]-1
            if mapper[chr] == 0:
                mapper.pop(chr)

        if not mapper:
            print("End of substring here")
            endIdx = idx
            break
            


    print("start idx ,", startIdx)
    print("Substring  : ", bigString[startIdx:endIdx+1])

    return startIdx, endIdx+1
        
'''
Once we found out the, first matching substring, we would use sliding windows to get tighter bounds on it 
or
find better one in each iteration of substring function 

to give tighter bound 
1. Contract the window from left side
2. if the character at left was in smallString, replish it's count in frequeny map 
3. Update substring bounds if less than current one 



'''
def smallestSubstringContaining(bigString, smallString):
    from collections import Counter

    # Initialize the frequency map for smallString
    targetCharCount = Counter(smallString)

    # Variables for tracking the smallest substring
    substringBounds = [0, float("inf")]
    substringCharCount = Counter()
    numUniqueChars = len(targetCharCount) # will help to handle duplicates 
    numUniqueCharsDone = 0

    # Sliding window indices
    leftIdx = 0
    rightIdx = 0

    # Expand the window
    while rightIdx < len(bigString):
        char = bigString[rightIdx]
        if char in targetCharCount:
            substringCharCount[char] += 1
            # all occurences char have been found 
            if substringCharCount[char] == targetCharCount[char]:
                numUniqueCharsDone += 1

        # at this point of time, substring is found 
        # Contract the window and update the smallest substring
        while numUniqueCharsDone == numUniqueChars and leftIdx <= rightIdx:
            substringBounds = [leftIdx, rightIdx] if rightIdx-leftIdx < substringBounds[1]-substringBounds[0] else substringBounds

            leftChar = bigString[leftIdx]

            if leftChar in targetCharCount:
                # if this leftChar was part of smallString, replish its count
                if substringCharCount[leftChar] == targetCharCount[leftChar]:
                    numUniqueCharsDone -= 1
                substringCharCount[leftChar] -= 1

            leftIdx += 1

        rightIdx += 1

    # Return the smallest substring found or an empty string if not found
    if substringBounds[1] == float("inf"):
        return ""
    else:
        start, end = substringBounds
        return bigString[start:end + 1]
  



smallString = "$$abf"
bigString = "abcd$ef$axb$c$"
print(smallestSubstringContaining(bigString, smallString))