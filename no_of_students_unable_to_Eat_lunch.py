'''
https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/description/?envType=daily-question&envId=2024-04-07

1. To stack pop and queue pop if the top of both match and reset the count =0 
2. if not, then increate count and put the student on the back of queue
3. if count = len(queue), that means, after all students tried to take top sandwich, none of them were able to acquire it. So they will be starved to death.
'''

class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        
        
        from collections import deque
        
        studentQueue = deque()
        sandwichesStack = deque()
        
        for sandwich in reversed(sandwiches):
            sandwichesStack.append(sandwich)
            
            
        for student in students:
            studentQueue.append(student)
            
        # this is used, to check if all the students in the current queue at any moment, has tried to check if 
        # they can eat the sandwich or not
        count = 0
        while count < len(studentQueue):
            
            # write break condition 
            
            if sandwichesStack[-1] == studentQueue[0]:
                sandwichesStack.pop()
                studentQueue.popleft()
                count = 0 
                
            else:
                studentQueue.append(studentQueue.popleft())
                count+=1 
            
        return len(studentQueue)
            
            

        
        
obj = Solution()
students, sandwiches = [1,1,0,0], [0,1,0,1]
students ,sandwiches = [1,1,1,0,0,1], [1,0,0,0,1,1]

students ,sandwiches = [1,1,1,1], [0,0,0,1,1]
print(obj.countStudents(students, sandwiches))