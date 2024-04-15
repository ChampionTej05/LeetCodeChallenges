'''
https://leetcode.com/problems/merge-intervals/
'''


def mergeIntervals(intervals):
    if len(intervals) <=1:
        return intervals
    

    result = []

    intervals = sorted(intervals, key = lambda x: (x[0],x[1]))

    interval_start = intervals[0][0]
    interval_end = intervals[0][1]

    for i in range(1, len(intervals)):
        start, end = intervals[i]
        if start <= interval_end:
            interval_end = max(end, interval_end) 
        else:
            #finish of current concurrent interval 
            result.append([interval_start, interval_end])
            interval_start = start 
            interval_end = end 

    

    result.append([interval_start, interval_end])

    return result 



intervals = [[1,3],[2,6],[8,10],[15,18]]

# output = [[1,6],[8,10],[15,18]]

# assert output == mergeIntervals(intervals)

intervals = [ [3,5],[4,6], [0,4]]
print(mergeIntervals(intervals))