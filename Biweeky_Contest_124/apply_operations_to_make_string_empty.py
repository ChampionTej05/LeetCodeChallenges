'''

https://leetcode.com/contest/biweekly-contest-124/problems/apply-operations-to-make-string-empty/

String at the last would the character which are having highest count in original string 

* count chr count of each character 
* find chr with highest count --> highChr
* start from end of the string, and accumulate strings if they are present in highChr 
* return reverse of it 
'''

class Solution(object):
    def lastNonEmptyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        from collections import Counter 
        
        cnt = Counter(s)
        most_common_elements = cnt.most_common()
        print("Most common elements", most_common_elements)
        mapper = {}
        
        #assuming at least one element exists in string at the start 
        
        max_count = most_common_elements[0][1]
        mapper[most_common_elements[0][0]] = True 
        for i in range(1, len(most_common_elements)):
            if most_common_elements[i][1] == max_count:
                mapper[most_common_elements[i][0]] = True 
        
        print(mapper)
        
        index = len(s)-1 
        result_set= set()
        result_list = list()
        while index>=0:
            if s[index] in mapper:
                if s[index] not in result_set:
                    result_set.add(s[index])
                    result_list.append(s[index])
                
            
            index = index - 1 
            
        print("result s ", result_list)
        print("list ", result_list)
        
        return "".join(result_list[::-1])
        
        
s  = "aabcbbchdehnoenoefuorefewnojsndowsnfojdbfdjsndlsancdkasmjjjjjjsjsjsjsjsjsjsjsaallllalaaaaaaaaa"
s = "abcd"
s = "aabcbbca"

obj = Solution()
print(obj.lastNonEmptyString(s))