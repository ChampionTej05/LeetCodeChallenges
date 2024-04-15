

'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
'''

def is_pallindrome(s):
    i, j = 0, len(s)-1
    while i <= j :
        if s[i] != s[j]:
            return False
        i = i +1
        j = j -1 

    return True 

import re
def valid_pallindrome_phrase(s):
    #remove spaces 
    s = s.replace(" ", "")
    
    s = re.sub(r'[^a-zA-Z0-9]','', s)
    s = s.lower()

    return is_pallindrome(s)

s = "A man, a plan, a canal: Panama"
s1 = "0P"
print(valid_pallindrome_phrase(s1))

