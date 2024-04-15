'''
https://leetcode.com/problems/number-of-people-aware-of-a-secret/description/

Two Queues:
shareTime: keeps track of available share time after the expiry of person sharing the secret 

Data Structure
obj : {gotTime, canShareTime, expireTime} for each person 

Algorithm:

expire(t) function: expires all the records at time t 
shareTime = 1+delay 
shareQueue.append(shareTime)
object = {}
for time t in 1 to N+1 :
    expire(t) 
    if t < shareQueue[0]:
        continue 
    obj = {gotTime=t, shareTime=t+delay, expireTime = t+forgot}
    # num = available.pop()
    shareQueue.append(t+delay)
    object[num] = obj
    
    
return N - len(available)
def expire(t):
    
    for num in objects:
        if object[num].expireTime >=t :
            objects.pop(num)
            # available.append(num)
            shareQueue.pop()
        

'''

class Solution(object):
    
    MOD = 10**9+7
    
    def __init__(self):
        from collections import deque
        self.objects = {}
        self.available_share_time = deque()
    
    def expire(self, t, people_with_secret ):
        objects_to_be_deleted = []
        for num in self.objects:
            if self.objects[num]["expireTime"] <=t:
                # expire object 
                # del self.objects[num]
                objects_to_be_deleted.append(num)
                self.available_share_time.popleft()
                
        print("object to be removed at t: {} , List: {}".format(t, objects_to_be_deleted))
        self.remove_objects(objects_to_be_deleted)
        
        return people_with_secret-len(objects_to_be_deleted)
        
    def remove_objects(self, objects_to_deleted):
        for num in objects_to_deleted:
            del self.objects[num]
                        
    def run_time(self, N, delay, forget):
        # first available share time 
        self.available_share_time.append(1+delay)
    
        
        # first one has got the secret already
        
        self.objects[0] = {'expireTime': 1+forget, 'shareTime': 1+delay}
        people_with_secret = 1 
        
        print('start')
        print('self.objects', self.objects)
        print('share queue', self.available_share_time)
        print('end')
        people = 0
        for t in range(1, N+1):
            print("t : ", t)
            people_with_secret = self.expire(t, people_with_secret)
            
            if t < self.available_share_time[0]:
                continue
            
            new_objects = {}
            for num in self.objects:
                if self.objects[num]['shareTime'] <= t:
                    # it can share the secret 

                    obj = {
                        'expireTime': t+forget, 
                        'shareTime': t+delay
                    }
                    self.available_share_time.append(t+delay)
                    
                    people = people+1 
                    new_objects[people] = obj 
                    
                    print('new objects : ', new_objects)
                    people_with_secret+=1 
                    
            self.objects.update(new_objects)
            print("self.objects : {} , at t = {}".format(self.objects, t))
            
        return people_with_secret
        
    
    def peopleAwareOfSecret(self, n, delay, forget):
        """
        :type n: int
        :type delay: int
        :type forget: int
        :rtype: int
        """
        
        return self.run_time(n, delay, forget)
    
    
# n = 6
# delay = 2
# forget = 4


n = 4
delay = 1 
forget = 3 
obj = Solution()
print(obj.peopleAwareOfSecret(n, delay, forget))