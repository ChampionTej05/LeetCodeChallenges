'''

Merge two sorted linked list, in-place 

https://leetcode.com/problems/merge-two-sorted-lists/ 

Approach: Two pointer approach , using dummy-head. 
Dummy-head is used to fix the head pointer of the resulted linkedlist so that we don't have to write 
separate condition for checking head. It will be initialised with the dummy value of '0'
'''

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1,list2):
    dummy_head = ListNode(0) # this will be fixed always 
    current = dummy_head # this will increment 

    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1 
            list1 = list1.next 
        else:
            current.next = list2 
            list2 = list2.next 
        current = current.next 

    
    current.next = list1 or list2 
    # after dummy_head our original list is appeneded, so we are returning that list 
    return dummy_head.next 


def mergeTwoListsRecursive(list1, list2):
    if not list1:
        return list2 
    if not list2:
        return list1
    

    result = None
    if list1.val < list2.val:
        result = list1
        result.next = mergeTwoListsRecursive(list1.next, list2)
    else:
        result = list2 
        result.next = mergeTwoListsRecursive(list1, list2.next)

    return result
def test_mergeTwoLists():
    # Helper function to create a linked list from a list of values
    def create_linked_list(values):
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    # Helper function to convert a linked list to a list for comparison
    def linked_list_to_list(head):
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result
    
    # Test cases
    # Test case 1: Merge two non-empty linked lists
    l1 = create_linked_list([1, 3, 5])
    l2 = create_linked_list([2, 4, 6])
    merged = mergeTwoLists(l1, l2)
    assert linked_list_to_list(merged) == [1, 2, 3, 4, 5, 6]
    print("test 1 passed")

    # Test case 2: One of the linked lists is empty
    l1 = create_linked_list([])
    l2 = create_linked_list([1, 2, 3])
    merged = mergeTwoLists(l1, l2)
    assert linked_list_to_list(merged) == [1, 2, 3]
    print("test 2 passed")

    # Test case 3: Both linked lists are empty
    l1 = create_linked_list([])
    l2 = create_linked_list([])
    merged = mergeTwoLists(l1, l2)
    assert linked_list_to_list(merged) == []
    print("test 3 passed")

    print("All test cases passed!")


test_mergeTwoLists()