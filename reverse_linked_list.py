# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

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
    
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head is None or head.next is None:
            return head 
        
        prev = None 
        p1 = head 
        p2 = head.next 
        
        
        while True:
            
            p1.next = prev 
            prev = p1 
            p1 = p2 
            if not p2:
                break 
            
            p2 = p2.next 
            
        return prev
    
    def reverseListV1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """


        if head is None or head.next is None:
            return head 

        current = head 
        previous = None 

        while current is not None:

            saveNode = current.next 
            current.next = previous 
            previous = current 
            current = saveNode 

        
        return previous 
    
    def recursiveSolution(self,head, newHead):
        
        if head is None:
            return newHead 
        
        saveNode = head.next   
        head.next = newHead 
        
        return self.recursiveSolution(saveNode, head)
    
import unittest 
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        test = LinkedList(1).addMany([ 2,3])
        expected = LinkedList(3).addMany([2,1])
        obj = Solution()
        actual = obj.reverseList(test)
        self.assertEqual(actual.getNodesInArray(), expected.getNodesInArray())



obj = TestProgram()
obj.test_case_1()