'''
https://leetcode.com/problems/maximum-profit-in-job-scheduling/description/?envType=daily-question&envId=2024-01-06
'''
from bisect import bisect_left, bisect_right
def find_next_index(start_times, end_time):
    # Extract the start times into a separate list
    

    # Given end time

    # Find the index of the element with the start time just greater than the given end time
    index = bisect_left(start_times, end_time)

    return index


        
# not working

   
# def handle_processing_iterative(startTime, endTime, profit):
#     jobs = sorted(zip(endTime, startTime, profit))
#     end_times = [x[0] for x in jobs]
#     N = len(endTime)
#     dp = [0] * (N+1)
    
#     print("Jobs: ", jobs)
    
#     for index in range(len(jobs)) :
#         end, start, profit = jobs[index]
#         next_
        
        
        
        
    

#     return dp[N]


def handle_processing_recursive(startTime, endTime, profit):
    jobs = sorted(zip(startTime, endTime, profit))
    N = len(startTime)
    start_times = [x[0] for x in jobs]
    print("Jobs: {}".format(jobs))
    
    dp= [0]* (N+1)
    def profit_scheduler(index, dp):
        
        if index>=N:
            return 0
        
        if dp[index] !=0:
            return dp[index]
        
        start, end, profit = jobs[index]
        
        profit_excluding_current_job = profit_scheduler(index+1, dp)
        
        
        
        next_index = find_next_index(start_times, end) 
        profit_including_current_job = profit + profit_scheduler(next_index, dp)
        
        print("Index: {}, exclude: {}, include: {}".format(index, profit_excluding_current_job, profit_including_current_job))
        print("Next Index for this index: {}".format(next_index))
        
        dp[index]  = max(profit_including_current_job, profit_excluding_current_job)
        print(" Index: {}, DP: {}".format(index, dp))
        return dp[index]
    
    
    profit = profit_scheduler(0, dp)
    print("Profit: ", profit)
        
     
     
startTime = [1,2,3,4,6]
endTime = [3,5,10,6,9]
profit = [20,20,100,70,60]

# startTime = [1,1,1]
# endTime = [2,3,4]
# profit = [5,6,4]

print(handle_processing(startTime, endTime, profit))