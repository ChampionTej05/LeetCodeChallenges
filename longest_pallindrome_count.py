def longestPalindrome(s):
    '''
    Idea : 
    Any pallindrome can max have one element with odd count and all other ones with even count 

    so maximum size pallindrome = how many even count letters + max odd count letter 

    ex: s= 'aaAabbccdd' , counter = {a:3,A:1,c:2,b:2,d:2}, maxLength = 2+2+2+ 3 = 9 which would be dbcaaacbd


    refinement, we can still consider even part of odd-count of character to be used and we will only one odd-count length fully. 
    so let us say n is odd, then we will add "n-1" as even part and keep 1 separate to be used during central if needed(we will use it of largest odd count only )

    Keep track of whether you've used an odd-count character fully (for the center of the palindrome).
    For each character:
    If its count is even, add it all to the length.
    If its count is odd, add count - 1 to the length and check if you've already placed an odd-count character in the center. If not, add 1 more to the length (for the center).

    '''


    from collections import Counter 

    cnt = Counter(s)
    print(cnt)
    even_sum = 0
    max_odd_count = 0

    for val in cnt.values():
        if val%2==0:
            even_sum = even_sum + val 
        else:
            max_odd_count = max(max_odd_count, val)
            even_sum = even_sum + (val -1) 

    
    central_char = 1 if max_odd_count !=0 else 0
    longest_pallindrome_length = even_sum + central_char 

    # print(longest_pallindrome_length)
    return longest_pallindrome_length

s1 = 'aaAabbccddvvvkkklll'
print(longestPalindrome(s1))
s2= 'aaA'
print(longestPalindrome(s2))
s3='a'
print(longestPalindrome(s3))