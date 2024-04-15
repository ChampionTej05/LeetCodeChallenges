'''
https://leetcode.com/problems/time-based-key-value-store/

Approach : 

We would maintain the Map[Array(object)] Data structure 
Array would be by default sorted since timestamps will be 
Object = (timestamp, value)

Ex: 
map = {
"key": [
(v1, t1), 
(v2, t2)
]
}


    
## Simpler approach 

1. Use bisect right function to find the index of the timestamp in the array for that key 
    a. Bisect right will give the timestamp which is exactly just greater than current passed timestamp 
    b. Our answer would be at index - 1 
        ex: arr = [[1, "v1"], [2,"v2"], [5,"v3"], [10,"v4"]] , bisect_right(arr, [10,""]), will give index = 3
        our answer would be index - 1=2 which is 
'''
#  return the index of element that is just greater than target
def find_upper_bound_element(arr, target):
    N = len(arr)
    start = 0
    end = N  # this is because of the index returned could be out of array boundary ex: target is greater than last element of the array 
    
    while (start < end):
        mid = start + (end - start) // 2
        
        # print(start, mid, end)


        timestamp = arr[mid][0]
        # for getting upperbound element
        if timestamp < target: 
            start = mid + 1 
        elif timestamp > target:
            #  we are not doing end = mid -1 because mid still could element just greater than target 
            # ex: 
            end = mid 
        else:
            #  this would be index of element just greater than target (as mid = index of target element)
            return mid + 1
    return start


timemap = {}

def set_key(key, value, timestamp):
    if key in timemap:
        timemap[key].append((timestamp, value))
    else:
        timemap[key] = [(timestamp, value)]

def get(key, timestamp):
    if key in timemap:
        index = find_upper_bound_element(timemap[key], timestamp)
        if index>0:
            print("Index obtained  ", index)
            return timemap[key][index-1][1]
        else:
            return ""
    else:
        return ""
def get_v1( key, timestamp):
    import bisect
    if key not in timemap or not timemap[key]:
        return ""

    # Get the list of (timestamp, value) tuples for the key
    time_values = timemap[key]

    # Find the index where the given timestamp would be inserted
    i = bisect.bisect_right(time_values, (timestamp, chr(127)))

    # If i is 0, it means all timestamps in time_values are greater than the timestamp
    if i == 0:
        return ""
    else:
        # Return the value at the last index where the timestamp is less than or equal to the given timestamp
        return time_values[i - 1][1]

# import bisect 

# def get_v1(key, timestamp):
#     if key in timemap :
#         index = 

# arr = [[1, 'v1'], [2, 'v2'], [5, 'v3'], [10, 'v4']]
# for obj in arr:
#     set("a", obj[1], obj[0])


# brr = [0, 1, 2, 3, 5, 7, 10, 11]
# for t in brr:
#     print("Request : {} , Result : {}".format(t , get_v1("a", t)))
    
instructions = ["TimeMap","set","set","get","get","get","get","get"]

data = [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]

for idx in range(len(instructions)):
    instruction = instructions[idx]
    obj = data[idx] 
    if instruction == "set":
        set_key(obj[0], obj[1], obj[2])
    elif instruction == "get":

        print("Request : {} , Answer: {}".format (obj[1], get_v1(obj[0], obj[1])))