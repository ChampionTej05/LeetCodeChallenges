# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    # Write your code here.
    backPtr = head
    forwardPtr = head
    prevPtr = head

    #set the forward ptr at kth location
    count = 0
    while (count < k):
        forwardPtr = forwardPtr.next
        count += 1

    # move both pointers till forwardPtr reaches end i.e forwardPtr will travel N-K steps

    while (forwardPtr != None):
        prevPtr = backPtr
        backPtr = backPtr.next
        forwardPtr = forwardPtr.next

    #now backPtr will be at (N-K)th node from beginning i.e Kth node from the last

    # print("Back Ptr valueL ", backPtr.value)

    #remove node by copying it's data
    if (backPtr.next != None):
        backPtr.value = backPtr.next.value
        backPtr.next = backPtr.next.next
    else:
        prevPtr.next = None 
    return 

    

    
    
