'''
https://leetcode.com/problems/palindromic-substrings/description/?envType=daily-question&envId=2024-02-08

Approach 
1. If we consider each character in string as pallindrome, then there can be two possibilities 
    a. Even length pallindrome starting from it char[i], char[i+1]
    b. Odd length pallindrome around the elements char[i-1] char[i+1]
    c. For each check, keep on incrementing count as you find the pallindromic substring on left and right 
    c. Update the count if either of is pallindromic substring 

2. Start the solution with count = len(string) as there is always one single pallindromic substring, which is single letter 
'''


class Solution(object):
    def is_pallindromic(self, s, left, right):
        if left <0 or right > len(s):
            return  0 

        count = 0 
        print("String got : ", s[left:right+1])
        while ( left >=0 and right < len(s)):

            if s[left] == s[right]:
                count +=1 
                left -=1 
                right +=1 
            else:
                return count 
            
        return count


        

    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = len(s) 
        for i in range(0, len(s)-1):
            even_length = self.is_pallindromic(s, i, i+1)
            print("even length string index passed: {} -> {}, and results: {}".format( i , i+1 , even_length))
            odd_length = self.is_pallindromic(s, i-1, i+1)
            print("odd length string passed: {} -> {}, and results: {}".format(i-1, i+1, odd_length))
            count = count + even_length
            count = count + odd_length

        print(count)
        return count
        



input = "aba"
# input = "aaaaa"
obj = Solution ()
obj.countSubstrings(input)
