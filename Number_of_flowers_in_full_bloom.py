'''
https://leetcode.com/problems/number-of-flowers-in-full-bloom/description/?envType=daily-question&envId=2024-03-06

using Binary search 

bisect_right: right most index which has value strictly greater than current 
bisect_left: leftmost index which has value less or equal to current 

1. For every t in people, we find how many flowers are blooming 
    = Flowers that are boomed - flowers that have stopped blooming 
    = bisect_right(start, t) - bisect_left(end, t)
2. bisect_right(start, t) --> gives the index of flower which  has start value greater than t 
3. bisect_left(end, t) --> gives index of flower which has end value less than or equal to t 
4. all the flowers in between this two would have been blooming at t 

ex: flowers = [[1,6],[3,7],[9,12],[4,13]], people = [2,3,7,11]

start = [1,3,4,9]
end = [6,7,12,13]
 
for t = 7, 
flowers bloomed = bisect_right(start, 7) = 3 (all flowers before this have been bloomed)
flower stopped = bisect_left(end, 7) = 1 (all flowers from this point before have  stopped blooming at t ) [ we got index 1]

ans for t = 7 : 3-1 = 2 
'''

class Solution(object):
    def fullBloomFlowers(self, flowers, people):
        """
        :type flowers: List[List[int]]
        :type people: List[int]
        :rtype: List[int]
        """
        import bisect 
        
        flower_blooming_start = sorted([x[0] for x in flowers])
        flower_blooming_end = sorted([x[1] for x in flowers])
        
        ans = []
        
        for person_t in people:
            # at this person_t 
            # flowers that would have bloomed 
            flowers_that_would_have_bloomed = bisect.bisect_right(flower_blooming_start, person_t)
            
            flowers_that_have_stopped_blooming = bisect.bisect_left(flower_blooming_end, person_t)
            
            ans.append(flowers_that_would_have_bloomed-flowers_that_have_stopped_blooming)
            
        return ans
    
    def fullBloomFlowersHeapSolution(self, flowers, people):
        import heapq
        sorted_arrival_times = sorted(people)
        flowers.sort()  # Sort the flower intervals based on their start times.
        
        bloom_counts = {}  # Dictionary to store counts of flowers in bloom for each arrival time.
        bloom_end_times = []  # Min heap to track flower bloom end times.

        flower_idx = 0
        for person_time in sorted_arrival_times:
            # Add flowers that are in bloom at the person's arrival time.
            while flower_idx < len(flowers) and flowers[flower_idx][0] <= person_time:
                heapq.heappush(bloom_end_times, flowers[flower_idx][1])
                flower_idx += 1

            # Remove flowers that are no longer in bloom.
            while bloom_end_times and bloom_end_times[0] < person_time:
                heapq.heappop(bloom_end_times)

            # Store the count of flowers in bloom for the person's arrival time.
            bloom_counts[person_time] = len(bloom_end_times)

        # Resulting list to store flower counts for each person.
        flower_counts = [bloom_counts[arrival_time] for arrival_time in people]

        return flower_counts  # Return the counts of flowers in bloom for each person'