
'''
leetcode: https://leetcode.com/problems/insert-interval/
'''

'''
Solution Approach : 
1. Insert new interval into sorted set of intervals 
2. Assuming the new array is sorted 
3. Merge overlapping intervals if any
'''



def merge_overlapping_intervals(intervals):

    if len(intervals) < 2:
        return intervals 
    interval_start = intervals[0][0]
    interval_end = intervals[0][1]
    results = []


    for interval in intervals[1:]:
        # print("Start: {}, end : {}", interval_start, interval_end)
        if interval_end >= interval[0]:
            #interval continue
            interval_end = max(interval_end, interval[1])
        else:
            #overlapping ended 

            results.append([interval_start, interval_end])
            interval_start, interval_end = interval


    #merge last interval 
    results.append([interval_start, interval_end])
    return results



def insert_in_sorted_intervals(intervals, interval):

    intervals.append(interval)

    results = sorted(intervals, key = lambda x : x[0])
    return results 


def insert(intervals, newInterval):

    intervals = insert_in_sorted_intervals(intervals, newInterval)
    # print("Sorted Intervals : ", intervals)
    results = merge_overlapping_intervals(intervals)
    # print(results)

    return results 




intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]

insert(intervals, newInterval)