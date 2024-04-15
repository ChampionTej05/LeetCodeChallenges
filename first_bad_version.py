''' 
https://leetcode.com/problems/first-bad-version/description/
'''

global_version = 5
def isBadVersion(version):
    print("call to bad version, version>= global_version  ", version, version>= global_version)
    return version>= global_version


def firstBadVersion(n):

    #modified binary search 

    start = 0 
    end = n-1 

    while start <=end:
        mid = start + (end-start)//2
        print("mid, ", mid)
        if (isBadVersion(mid+1)) :
            #search in left for first bad version
            
            end = mid -1 
            if end >=0:
                print("end, ", end+1)
                if not isBadVersion(end+1):
                    return mid+1
            else:
                return mid + 1


        else:
            #search in right for first bad version
            start = mid +1 



def firstBadVersionv1(n):
    start = 1 
    end = n

    while start < end :
        mid = start + (end-start)//2
        if (isBadVersion(mid)):
            end = mid # we don't subtract 1 from mid while updating end because if mid is indeed the first bad version, we want to include it in the search range.
        else:
            start = mid +1 
    return start 
n = 9
print(firstBadVersionv1(n))

        

