'''
https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/description/?envType=daily-question&envId=2024-01-23

Algorithm Brute Force O(26*26*16)

1. For each string, create new unique string in unsorted order and check its length 
2. Compare its length with maximum length maintained till now 
globalLength

# we will try to model this around generate_subsets problem

prefix = "" 
globalLength = 0 

function(arr, index, prefix, globalLength):
    globallength = max(len(prefix), globalLength)
    # check all possible subsets from this prefix 
    globalLength = function(arr, index+1, prefix+arr[i], globalLength)
    return globalLength 


#Optimised Bitmap (Incorrect but good approach)
Convert each string in the input arr into a bitmask, where each bit represents the presence of a character in the alphabet (assuming lowercase English letters only).
Create a list of bitmasks corresponding to the strings in arr.
Iterate through all possible bitmasks and check if their bitwise OR operation results in a bitmask with unique characters. If yes, update the maximum length.

ex: ["ab", "bd" , "ce", "aa" ]
bitmask = ["0011", "1010", "10100", "0" ]
 aa =0 as there are duplicate so don't consider it during calculations 

 # we converted strings into bitmaps, so that comparasions is O(1) instead of O(N)

Maximum answer possible is 26 anyways ( that is count of unique letters)


'''

def generate_subsets(arr, index, prefix, uniqueLength):
    # get the unique characters of current prefix string 
    # print("Prefix received : ", prefix)
    aset = set(prefix)
    if len(aset) == len(prefix):
        # that means whatever string that we are computing has unique characters in itself ex: ["aa", "bb"]
        uniqueLength = max(uniqueLength, len(prefix))
    
        for i in range(index, len(arr)):
            newString = set(prefix+arr[i])
            # to find if the two string to be combined has any common character. If yes, skip the combo ex: "uniq" + "ue"
            if len(newString) == len(aset^set(arr[i])):
                uniqueLength = generate_subsets(arr, index+1, prefix+arr[i], uniqueLength)
    #else simply skip this prefix to be used further
    return uniqueLength
# gives TLE 
def get_maximum_subset_length (arr, index, prefix, uniqueLength):
    aset = set(prefix)
    if len(aset) != len(prefix): #O(N)
        return uniqueLength
    
    uniqueLength = max(uniqueLength, len(aset))
    #explore all subsets leading from this string 
    for i in range(index, len(arr)):
        bset = set(arr[i])
        if len(bset) != len(arr[i]):
            # not a unique string in itself
            continue

        newSet = set(prefix+arr[i])
        if len(newSet) == len(prefix+arr[i]):
            #unique new String formed 
            uniqueLength = generate_subsets(arr, index+1, prefix+arr[i], uniqueLength)
    
    return uniqueLength

# working solution 
def maxLength(arr):

    def backtrace(index, current, max_length):
        max_length[0] = max(max_length[0] , len(current))

        for i in range(index, len(arr)):
            if len(set(current+arr[i])) == len(current+arr[i]):
                backtrace(i+1, current+arr[i], max_length)

    
    max_length = [0]
    backtrace(0, "", max_length)
    return max_length[0]
# Using Bitmap Technique as characters are limited 
# not correct solution 
# def maxLengthUsingBitmap(arr):
#     bitmasks = []
#     # needed so that we can first count big unique strings instead of small ones to get better overall count
#     # ex: ["cha","r","act","ers"], we should consider "cha" + "ers" and not "cha"+"r"
    
#     def string_to_bit(s):
#         bitmap = 0
#         for chr in s:
#             # since everything is small
#             index_of_chr = ord(chr) - ord('a')
#             #if already bit is set that means this str has dupliate characters, no need to consider this during calculations 
#             if bitmap & (1 << index_of_chr) !=0 :
#                 return 0 
#             bitmap |= (1<<index_of_chr)
#         return bitmap
    
#     for s in arr:
#         bitmasks.append(string_to_bit(s))

#     bitmasks = sorted(bitmasks , key = lambda x:bin(x).count('1'), reverse=True)
#     print([bin(bitmask) for bitmask in bitmasks])
#     bitmap = 0 
#     for bitmask in bitmasks:
#         if bitmask == 0 :
#             continue
#         #no common characters in new string
#         if bitmap & bitmask == 0:
#             bitmap |= bitmask

#     return bin(bitmap).count('1')

def maxLengthUsingBitmap(arr):

    # needed so that we can first count big unique strings instead of small ones to get better overall count
    # ex: ["cha","r","act","ers"], we should consider "cha" + "ers" and not "cha"+"r"
    
    def string_to_bit(s):
        bitmap = 0
        for chr in s:
            # since everything is small
            index_of_chr = ord(chr) - ord('a')
            #if already bit is set that means this str has dupliate characters, no need to consider this during calculations 
            if bitmap & (1 << index_of_chr) !=0 :
                return 0 
            bitmap |= (1<<index_of_chr)
        return bitmap
    
    bitmasks = [string_to_bit(s) for s in arr]
    print([bin(bitmask) for bitmask in bitmasks])
    # uniqueLength = 0 

    maxLength = [0] # so that values can be passed as always

    def backtraceComputation(index, bitmask, current_length):
        maxLength[0] = max(current_length, maxLength[0] )

        for i in range(index, len(bitmasks)):
            if bitmask & bitmasks[i] == 0: 
                # no duplicates found in current bitmask and new that we are trying 
                backtraceComputation(i+1, bitmask | bitmasks[i], current_length + bin(bitmasks[i]).count('1') )

        
    
    backtraceComputation(0, 0, 0)
    return maxLength[0]




def maxLength(arr):
    prefix = ""
    uniqueLength = len(prefix)

    # uniqueLength = get_maximum_subset_length(arr, 0, prefix, uniqueLength)
    uniqueLength = maxLengthUsingBitmap(arr)
    print("Unique length: ", uniqueLength)
    return uniqueLength


# arr = ["un","iq","ue"]
# arr = ["cha","r","act","ers"]
# arr = [ "abcdefghijklmnopqrstuvwxyz" ]
# arr = ["aa", "bb"]
# arr= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"]
arr = ["ab","cd","cde","cdef","efg","fgh","abxyz"]
print(maxLength(arr))

    