# class LinkedList:
#     def __init__(self, value):
#         self.value = value
#         self.next = None


def print_list(head):
    ptr = head
    while ptr!= None:
        print(ptr.value, end = ' -> ')
        ptr = ptr.next 

    print("None")

def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    if linkedList == None or linkedList.next == None:
        return linkedList
    

    ptr = linkedList
    while ptr != None:
        current = ptr.next 
        while current!=None  and current.value == ptr.value:
            current = current.next 

        ptr.next = current 
        ptr = current 

    
    return linkedList




# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!


import unittest


class LinkedList():
    def __init__(self, value):
        self.value = value
        self.next = None

    def addMany(self, values):
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self

    def getNodesInArray(self):
        nodes = []
        current = self
        while current is not None:
            nodes.append(current.value)
            current = current.next
        return nodes


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        test = LinkedList(1).addMany([1, 3, 4, 4, 4, 5, 6, 6])
        expected = LinkedList(1).addMany([3, 4, 5, 6])
        actual = removeDuplicatesFromLinkedList(test)
        self.assertEqual(actual.getNodesInArray(), expected.getNodesInArray())



obj = TestProgram()
obj.test_case_1()
