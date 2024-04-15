# '''
# https://www.algoexpert.io/questions/calendar-matching
# '''



# class CalendarTime:

#     # def __init__(self,hour, minutes):
#     #     self.hours = int(hour)
#     #     self.minutes = int(minutes)

#     def __init__(self, timeString:str):
#         splitTime = timeString.split(":")
#         self.hours = int(splitTime[0])
#         self.minutes = int(splitTime[1])


#     def to_timestring(self):
#         return self.hours + ":" + self.minutes

#     @staticmethod
#     def substract(time1, time2):
        
#         # assuming time1 > time2 
#         result = CalendarTime.isGreaterThan(time1, time2)
#         if result == - 1 : 
#             time2, time1 = time1, time2
        
        
#         print("Time1 ", time1)

#         time2_min = time2.minutes
#         time1_min = time1.minutes 

#         hour_carry = 0 
#         if time1_min < time2_min: 
#             hour_carry = 1 
#             time1_min = 60 

#         result_mins = time1_min - time2_min
#         result_hours = time1.hours - time2.hours - hour_carry
        
#         timeString = str(result_hours) + ":" + str(result_mins) 
#         return CalendarTime(timeString)
        
#     def isGreaterThan( time1:object, time2: object):
#         #  1 --> first time is greater 
#         #  -1 --> second time is greater 
#         # 0 --> both are equal 
        
#         if time1.hours > time2.hours:
#             return 1 
#         if time2.hours > time1.hours:
#             return -1 
        
#         # hours are equal 

#         if time1.minutes > time2.minutes:
#             return 1 
#         if time2.minutes > time1.minutes:
#             return -1 
        
#         return 0 
    
#     def convertToString(self):
    

#         minutes = ""
#         if self.minutes < 10 :
#             minutes = "0" + str(self.minutes)
#         else:
#             minutes = str(self.minutes)

#         return str(self.hours) + ":" + minutes
    
#     def __str__(self) -> str:
#         return self.convertToString()


# # Brute Force (Not correct solution )

# def createFreeSlotsFromCalendar(dailyBounds, calendar):
#     startTime, endTime = dailyBounds
#     intervals = []
#     for i in range(len(calendar)):
#         tStart, tEnd = calendar[i]
#         if CalendarTime.isGreaterThan(CalendarTime(tStart), CalendarTime(startTime)) == 1:
#             intervals.append([startTime, tStart])
#         startTime = tEnd 

#     if startTime < endTime:
#         intervals.append([startTime, endTime])
#     return intervals 



# def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
#     # Write your code here.

    
#     intervals1 = [dailyBounds1] if len(calendar1) ==0 else createFreeSlotsFromCalendar(dailyBounds1, calendar1)
#     print(intervals1)

#     intervals2 =  [dailyBounds2] if len(calendar2) ==0 else createFreeSlotsFromCalendar(dailyBounds2, calendar2)
#     print(intervals2)

#     results = []
#     for i in range(len(intervals1)):
#         startTime, endTime = CalendarTime(intervals1[i][0]), CalendarTime(intervals1[i][1])
#         for j in range(len(intervals2)):
#             tStart, tEnd = CalendarTime(intervals2[j][0]), CalendarTime(intervals2[j][1])

            
#             if CalendarTime.isGreaterThan(startTime, tEnd) == 1:
#                 # no need to look further for this 
#                 continue

#             if CalendarTime.isGreaterThan(tStart, endTime) == 1:
#                 continue

#             print("i {}, j  {}, tStart: {}, tEnd {}".format(i, j, tStart, tEnd))
#             maxStartTime = tStart if CalendarTime.isGreaterThan(tStart, startTime) == 1 else startTime
#             minEndTime = tEnd if CalendarTime.isGreaterThan(tEnd, endTime) == -1 else endTime

#             print("i {}, j  {}, maxStartTime: {}, minEndTime {}".format(i, j, maxStartTime, minEndTime))

#             meetingCalendartime = CalendarTime("00:" +str(meetingDuration))
#             print("meeting Duration", meetingCalendartime)
#             endTimeDuration = CalendarTime.substract(minEndTime, meetingCalendartime)
#             print("EndTimeDuration ", endTimeDuration)
#             if CalendarTime.isGreaterThan(maxStartTime, endTimeDuration) in [0,-1]:
#                 results.append([maxStartTime.convertToString(), minEndTime.convertToString()])

#     print(results)


# calendar1 = [["9:00", "10:30"], ["12:00", "13:00"], ["16:00", "18:00"]]
# dailyBounds1 = ["9:00", "20:00"]

# calendar2 = [["10:00", "11:30"], ["12:30", "14:30"], ["14:30", "15:00"], ["16:00", "17:00"]]
# dailyBounds2 = ["10:00", "18:30"]

# meetingDuration = 30


# # calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration)

# obj = {
#   "calendar1": [
#     ["9:00", "10:30"],
#     ["12:00", "13:00"],
#     ["16:00", "18:00"]
#   ],
#   "dailyBounds1": ["9:00", "20:00"],
#   "calendar2": [
#     ["10:00", "11:30"],
#     ["12:30", "14:30"],
#     ["14:30", "15:00"],
#     ["16:00", "17:00"]
#   ],
#   "dailyBounds2": ["10:00", "18:30"],
#   "meetingDuration": 45
# }

# obj = {
#   "calendar1": [],
#   "calendar2": [],
#   "dailyBounds1": ["9:30", "20:00"],
#   "dailyBounds2": ["9:00", "16:30"],
#   "meetingDuration": 60
# }



# calendarMatching(**obj)


## Refactored code for the above brute force approach 

class CalendarTime:
    def __init__(self, timeString: str):
        self.hours, self.minutes = map(int, timeString.split(":"))

    def to_time_string(self):
        return f"{self.hours:02d}:{self.minutes:02d}"

    @staticmethod
    def subtract(time1, time2):
        #  convert to minutes 
        minutes1 = time1.hours * 60 + time1.minutes
        minutes2 = time2.hours * 60 + time2.minutes
        difference = minutes1 - minutes2

        if difference < 0:
            # return
            return

        hours, minutes = divmod(difference, 60)
        return CalendarTime(f"{hours:02d}:{minutes:02d}")

    @staticmethod
    def compare(time1, time2):
        if time1.hours < time2.hours:
            return -1
        elif time1.hours > time2.hours:
            return 1
        elif time1.minutes < time2.minutes:
            return -1
        elif time1.minutes > time2.minutes:
            return 1
        else:
            return 0

    def __str__(self):
        return self.to_time_string()


def create_free_slots_from_calendar(daily_bounds, calendar):
    start_time, end_time = daily_bounds
    intervals = []
    for t_start, t_end in calendar:
        if CalendarTime.compare(CalendarTime(t_start), CalendarTime(start_time)) == 1:
            intervals.append([start_time, t_start])
        start_time = t_end
    if CalendarTime.compare(CalendarTime(start_time), CalendarTime(end_time)) == -1:
        intervals.append([start_time, end_time])
    return intervals


def calendar_matching(calendar1, daily_bounds1, calendar2, daily_bounds2, meeting_duration):
    intervals1 = [daily_bounds1] if not calendar1 else create_free_slots_from_calendar(daily_bounds1, calendar1)
    intervals2 = [daily_bounds2] if not calendar2 else create_free_slots_from_calendar(daily_bounds2, calendar2)
    results = []

    for start_time1, end_time1 in intervals1:
        for start_time2, end_time2 in intervals2:
            max_start_time =  CalendarTime(start_time1) if CalendarTime.compare(CalendarTime(start_time1), CalendarTime(start_time2)) == 1 else CalendarTime(start_time2)
            min_end_time = CalendarTime(end_time1) if CalendarTime.compare(CalendarTime(end_time1), CalendarTime(end_time2)) == -1 else CalendarTime(end_time2)
            meeting_duration_time = CalendarTime(f"00:{meeting_duration:02d}")
            end_time_duration = CalendarTime.subtract(min_end_time, meeting_duration_time)
            if end_time_duration:
                if CalendarTime.compare(max_start_time, end_time_duration) != 1:
                    results.append([max_start_time.to_time_string(), min_end_time.to_time_string()])

    return results

obj = {
  "calendar1": [
    ["9:00", "10:30"],
    ["12:00", "13:00"],
    ["16:00", "18:00"]
  ],
  "daily_bounds1": ["8:00", "20:00"],
  "calendar2": [
    ["10:00", "11:30"],
    ["12:30", "14:30"],
    ["14:30", "15:00"],
    ["16:00", "17:00"]
  ],
  "daily_bounds2": ["7:00", "18:30"],
  "meeting_duration": 45
}

print(calendar_matching(**obj))