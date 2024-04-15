'''
https://leetcode.com/problems/maximum-good-people-based-on-statements/description/?orderBy=most_votes

isValid(curr) --> Validates if the solution that we have got is valid configuratin or not, by checking with input statements 
if the curr[i]==1 (good person),so all statements made by that person in the input should be concurrent to what we got in curr 

i.e curr[i] == S[i][j] 
'''


class Solution(object):
    GOOD = 1
    BAD = 0 
    NO_COMMENT = 2
    def isConfigurationValidAsPerStatements(self, current_config, statements):
        N = len(current_config)
        for i in range(N):
            # telling the truth 
            if current_config[i] == Solution.GOOD:
                #  then check for all the input statements said by the person 
                for j in range(N):
                    if statements[i][j] != Solution.NO_COMMENT and statements[i][j] != current_config[j]:
                        # Found at least one config, which is not as per the input statements
                        return False
                    
        return True 
    
    def explore_solutions(self, current_config, statements, start, current_good_people_count, ans):
        
        if start == len(statements):
            print("Config generated: ", current_config)
            if self.isConfigurationValidAsPerStatements(current_config, statements):
                print("For config: {}, good people count: {}".format(current_config, current_good_people_count))
                ans[0] = max(ans[0], current_good_people_count)
            return
        
        #exploration step 
        
        # person is bad
        current_config.append(Solution.BAD)
        self.explore_solutions(current_config, statements, start+1, current_good_people_count, ans)
        
        # person is good
        current_config[-1] = Solution.GOOD 
        self.explore_solutions(current_config, statements, start+1, current_good_people_count+1, ans)
        
        # person is skipped to be considered 
        current_config.pop()
    
    def maximumGood(self, statements):
        """
        :type statements: List[List[int]]
        :rtype: int
        """
        
        ans = [0]
        
        self.explore_solutions([], statements, 0, 0, ans )
        
        return ans[0]
    
    
statements = [[2,1,2],[1,2,2],[2,0,2]]
statements = [[2,0],[0,2]]
obj = Solution()

print(obj.maximumGood(statements))