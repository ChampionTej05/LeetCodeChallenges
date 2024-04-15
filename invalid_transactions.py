'''
https://leetcode.com/problems/invalid-transactions/description/

O(N*N) should work provided constraints are very small
'''


class Solution(object):
    
    def parse_input(self, transactions):
        
        N = len(transactions)
        names= []
        period =[]
        amount = []
        city = []
        for i in range(N):
            ans = transactions[i].split(",")
            names.append(ans[0])
            period.append(int(ans[1],10))
            amount.append(int(ans[2], 10))
            city.append(ans[3])
            
        return names, period, amount, city
            
    
    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        
        names, period, amount, city = self.parse_input(transactions)
        results = []
        visited = [False]*len(transactions)
        for i in range(len(transactions)):
            if amount[i] > 1000 and visited[i] == False:
                results.append(transactions[i])
                continue
                
            for j in range(len(transactions)):
                if i!=j and abs(period[i]-period[j])<=60 and names[i] == names[j] and city[i]!=city[j] and visited[i] == False:
                    results.append(transactions[i])
                    visited[i] = True 
                    
        return results 
                

