class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

'''
We can solve using length OR fast and slow pointer 

when fastptr reach end of the linked list, slowptr will be at the mid of the linkedlist 

for Odd length : fast.next == None 
for even length: fast == None

'''

def middleNode(linkedList):
    # Write your code here.
    
    if linkedList is None or linkedList.next is None:
        return linkedList

    slowPtr = linkedList
    fastPtr = linkedList

    
    while fastPtr and fastPtr.next :
        slowPtr = slowPtr.next 
        fastPtr = fastPtr.next.next 

    return slowPtr
