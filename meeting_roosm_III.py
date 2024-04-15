'''
https://leetcode.com/problems/meeting-rooms-iii/description/?envType=daily-question&envId=2024-02-08


'''

from heapq import heapify, heappop, heappush
class Solution(object):
    
    def init_object(self, no_of_rooms):
        self.available_rooms = [ i for i in range(no_of_rooms)]
        self.booked_rooms = []
        self.room_counter = [0]* no_of_rooms
        heapify(self.available_rooms)
        heapify(self.booked_rooms)
        
        
    def is_room_free(self):
        return len(self.available_rooms) > 0 
        
    # 
    def book_free_room(self,meeting_end):
        free_room = heappop(self.available_rooms)
        # push when this meeting room will be empty 
        heappush(self.booked_rooms, (meeting_end, free_room))
        self.room_counter[free_room]+=1
        
    def book_lowest_number_meeting_room(self, meeting_start, meeting_end):
        booked_room_end_time, booked_room = heappop(self.booked_rooms)
        heappush(self.booked_rooms, ( booked_room_end_time + (meeting_end-meeting_start), booked_room))
        self.room_counter[booked_room]+=1
    
    # can we get free meeting rooms at time=startTime
    def free_meeting_rooms(self, meeting_start):    
        
        # as long as there are meeeting rooms which have end time less than current meeting_start, free them 
        while len(self.booked_rooms) > 0 and self.booked_rooms[0][0] <= meeting_start:
            booking_end_time, booked_room = heappop(self.booked_rooms)
            heappush(self.available_rooms, booked_room)
            
            
    
    def mostBooked(self, n, meetings):
        """
        :type n: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        
        self.init_object(n)
        
        # sort byt start time 
        meetings.sort(key = lambda x: x[0])
        
        for meeting_start, meeting_end in meetings:
            # for this meeting, can we clear any meeting rooms 
            
            self.free_meeting_rooms(meeting_start)
            
            # are there any rooms free now?
            if self.is_room_free():
                #book that free room 
                self.book_free_room(meeting_end) 
            else:
                #room is not free, so find which could be room which has least end time, and book that one 
                self.book_lowest_number_meeting_room(meeting_start, meeting_end)
                
        
        print(self.room_counter)
        
        max_booked_room = -1 
        max_count = 0
        for room, count in enumerate(self.room_counter):
            if count > max_count:
                max_count = count 
                max_booked_room = room 
                
        return max_booked_room
            